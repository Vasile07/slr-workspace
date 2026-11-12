---
name: slr-fulltext-retrieval
description: Retrieve full-text SLR papers from DOI records into a chosen local folder. Uses direct open-access PDF locations and gives manual retrieval steps when institutional access is needed.
---

# SLR Full-Text Retrieval

Use this skill after the team has selected papers for full-text review. It supports either one paper (DOI plus output location) or a team-approved list of selected papers. It does not search for papers or change the selected-paper list.

## Required inputs

For each paper, obtain:

- Stable project paper ID
- DOI
- Expected title
- Selected status approved by the member/team
- Requested output directory
- Source database or publisher link, when known

If the approved paper list or required fields are missing, ask for them. Do not infer that a paper is selected from a ranking recommendation. If reading from the Google Sheet, first inspect its current sheet and headers; if its schema is not agreed, ask for an exported or otherwise confirmed list.

## Retrieval method

1. Read `README.md` and use the team's chosen full-text folder. The workspace default is `papers/full-text/`.
2. The downloader requires `UNPAYWALL_EMAIL` to be set to an email address for Unpaywall API requests. If it is missing, explain the one-time setup requirement; the script will report `manual_required` and will not attempt a network lookup.
3. For each approved paper, run `scripts/download_oa_paper.py` with the DOI, paper ID, expected title, and output directory. The script queries Unpaywall for a direct open-access PDF and reports its location, version, and license when available.
4. The script only downloads an HTTPS direct PDF URL returned as an open-access location. It does not log in, use institutional cookies, scrape paywalled pages, or bypass publisher access controls. It validates the PDF signature and refuses to overwrite existing files.
5. For every saved PDF, check that it opens and that the article title and version correspond to the selected record. A successful HTTP download alone is not confirmation that it is the right paper.
6. Record one result per paper in `papers/retrieval-manifest.csv`: paper ID, DOI, expected/retrieved title, status, source URL, version, license, local path, date, and notes. Do not write this information into the shared spreadsheet unless the team separately requests that update.
7. Process batches sequentially and respect API/source limits. Do not repeatedly retry a failed or restricted source.

## Manual fallback

When the result is `manual_required`, explain the reason and provide the paper's DOI and expected title. Suggest the appropriate publisher page (IEEE Xplore, ACM Digital Library, or SpringerLink), the university library/e-nformation access mentioned in the course brief, or the other full-text routes permitted by the instructor (ResearchGate, arXiv, or the researchers' homepage). Web of Science is a formal search database, not a full-text download route by itself.

If the team still cannot obtain a paper, tell the user the course brief says to send the DOI to the instructor. Do not send a message or email on the user's behalf.

## Reporting

Summarize the batch as downloaded, already present, or manual retrieval required. Include the destination folder, paper IDs, and unresolved papers. Do not claim full-text review is complete until the team has opened and checked each PDF.
