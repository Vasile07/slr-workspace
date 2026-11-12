#!/usr/bin/env python3
"""Download a direct open-access PDF for a DOI using Unpaywall metadata.

This script never logs in, uses institutional cookies, or attempts to bypass a
publisher paywall. It writes a file only when the response begins with a PDF
signature. If no usable OA PDF is available, it returns manual_required.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen

MAX_PDF_BYTES = 100 * 1024 * 1024
USER_AGENT = "CMES-SLR-OA-PDF-Retriever/1.0"


def emit(payload: dict, exit_code: int = 0) -> int:
    print(json.dumps(payload, ensure_ascii=False))
    return exit_code


def normalize_doi(value: str) -> str:
    doi = value.strip()
    doi = re.sub(r"^(?:https?://)?(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I)
    return doi.strip()


def safe_stem(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip()).strip("._-")
    return stem[:100] or "paper"


def get_unpaywall_record(doi: str, email: str) -> dict:
    doi_path = quote(doi, safe="/")
    query = urlencode({"email": email})
    url = f"https://api.unpaywall.org/v2/{doi_path}?{query}"
    request = Request(url, headers={"User-Agent": f"{USER_AGENT} (mailto:{email})", "Accept": "application/json"})
    with urlopen(request, timeout=30) as response:
        raw = response.read(5 * 1024 * 1024 + 1)
    if len(raw) > 5 * 1024 * 1024:
        raise ValueError("Unpaywall response exceeded the expected size.")
    return json.loads(raw.decode("utf-8"))


def pdf_locations(record: dict) -> list[dict]:
    if not record.get("is_oa"):
        return []
    candidates: list[dict] = []
    best = record.get("best_oa_location")
    if isinstance(best, dict):
        candidates.append(best)
    others = record.get("oa_locations")
    if isinstance(others, list):
        candidates.extend(item for item in others if isinstance(item, dict))

    seen: set[str] = set()
    result: list[dict] = []
    for location in candidates:
        url = location.get("url_for_pdf")
        if not isinstance(url, str) or url in seen:
            continue
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            continue
        seen.add(url)
        result.append(location)
    return result


def download_pdf(url: str, destination: Path) -> tuple[bool, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf"})
    temporary_path: Path | None = None
    try:
        with urlopen(request, timeout=45) as response:
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > MAX_PDF_BYTES:
                return False, "PDF exceeds the 100 MiB safety limit."
            with tempfile.NamedTemporaryFile(prefix="slr-", suffix=".part", dir=destination.parent, delete=False) as stream:
                temporary_path = Path(stream.name)
                total = 0
                signature = bytearray()
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    if len(signature) < 5:
                        signature.extend(chunk[: 5 - len(signature)])
                    total += len(chunk)
                    if total > MAX_PDF_BYTES:
                        return False, "PDF exceeds the 100 MiB safety limit."
                    stream.write(chunk)

        if bytes(signature) != b"%PDF-":
            return False, "The open-access URL did not return a PDF (possibly a landing or sign-in page)."
        if destination.exists():
            return False, "Destination already exists; refusing to overwrite it."
        os.replace(temporary_path, destination)
        temporary_path = None
        return True, "PDF signature verified."
    except (HTTPError, URLError, TimeoutError, OSError, ValueError) as error:
        return False, f"Download failed: {error}"
    finally:
        if temporary_path is not None:
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Download a DOI's direct open-access PDF without bypassing access controls.")
    parser.add_argument("--doi", required=True, help="Paper DOI")
    parser.add_argument("--paper-id", required=True, help="Stable project identifier, such as S01-P03")
    parser.add_argument("--title", default="", help="Expected title, recorded in the result for manual verification")
    parser.add_argument("--output-dir", required=True, help="Directory in which the PDF should be saved")
    args = parser.parse_args()

    doi = normalize_doi(args.doi)
    if not re.fullmatch(r"10\.\d{4,9}/\S+", doi):
        return emit({"status": "error", "doi": doi, "paper_id": args.paper_id, "message": "DOI format is invalid."}, 2)

    email = os.environ.get("UNPAYWALL_EMAIL", "").strip()
    if not email:
        return emit({"status": "manual_required", "doi": doi, "paper_id": args.paper_id, "title": args.title, "message": "Set UNPAYWALL_EMAIL to use the Unpaywall API, or retrieve this paper manually."})

    output_dir = Path(args.output_dir).expanduser().resolve()
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        return emit({"status": "error", "doi": doi, "paper_id": args.paper_id, "message": f"Cannot create output directory: {error}"}, 2)

    destination = output_dir / f"{safe_stem(args.paper_id)}.pdf"
    if destination.exists():
        try:
            with destination.open("rb") as existing:
                is_pdf = existing.read(5) == b"%PDF-"
        except OSError:
            is_pdf = False
        return emit({"status": "already_present" if is_pdf else "manual_required", "doi": doi, "paper_id": args.paper_id, "title": args.title, "saved_path": str(destination), "message": "A PDF already exists; verify its title." if is_pdf else "Destination exists but is not a PDF; refusing to overwrite it."})

    try:
        record = get_unpaywall_record(doi, email)
    except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
        return emit({"status": "manual_required", "doi": doi, "paper_id": args.paper_id, "title": args.title, "message": f"Could not retrieve open-access metadata: {error}"})

    retrieved_doi = normalize_doi(str(record.get("doi", "")))
    if retrieved_doi.lower() != doi.lower():
        return emit({"status": "manual_required", "doi": doi, "paper_id": args.paper_id, "title": args.title, "message": "The DOI returned by the metadata service did not match the requested DOI."})
    if not record.get("is_oa"):
        return emit({"status": "manual_required", "doi": doi, "paper_id": args.paper_id, "title": args.title, "retrieved_title": record.get("title"), "message": "No open-access location was reported."})

    failures: list[str] = []
    for location in pdf_locations(record):
        success, message = download_pdf(location["url_for_pdf"], destination)
        if success:
            return emit({
                "status": "downloaded",
                "doi": doi,
                "paper_id": args.paper_id,
                "title": args.title,
                "retrieved_title": record.get("title"),
                "saved_path": str(destination),
                "source_url": location.get("url_for_pdf"),
                "landing_page": location.get("url_for_landing_page"),
                "version": location.get("version"),
                "license": location.get("license"),
                "message": message + " Confirm the PDF title against the expected title.",
                "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            })
        failures.append(message)

    detail = "; ".join(failures) if failures else "No direct HTTPS PDF URL was listed."
    return emit({"status": "manual_required", "doi": doi, "paper_id": args.paper_id, "title": args.title, "retrieved_title": record.get("title"), "message": detail})


if __name__ == "__main__":
    sys.exit(main())
