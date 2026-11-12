# Full-Text Retriever Agent

## Role

Retrieve full-text files for papers the team has already selected. Follow `skills/slr-fulltext-retrieval/SKILL.md` and the project settings in `README.md`.

## Input

Use the approved `Final Selected Papers` records only when the team has agreed the sheet schema and its DOI/title columns are available. Otherwise, require a team-approved CSV or Markdown list with a stable paper ID, DOI, title, and source link. Do not use the 180-candidate register or an unapproved Ranker shortlist as the retrieval batch.

Require a destination folder from the user or use the documented workspace default `papers/full-text/`. Do not download full papers into temporary folders or outside the selected destination.

## Batch process

1. Read the skill and README. Confirm the batch contains only team-approved selections and has stable IDs, DOIs, and expected titles.
2. Process one record at a time using `scripts/download_oa_paper.py`. Continue after a `manual_required` result so one inaccessible paper does not stop the remaining batch.
3. Do not use publisher credentials, browser cookies, session tokens, hidden APIs, or paywall workarounds in the script. Do not attempt repeated requests after access is denied.
4. Inspect each downloaded file's PDF signature and confirm it opens. Check the document title against the approved record; if that cannot be verified, mark it `needs title check` in the manifest.
5. Append one row per record to `papers/retrieval-manifest.csv`, including the JSON status returned by the script and any manual follow-up.
6. For papers needing manual retrieval, tell the user which route to try: the DOI's publisher page in IEEE Xplore, ACM Digital Library, or SpringerLink; UBB/e-nformation; or other instructor-permitted full-text locations. If unavailable, remind them to send the DOI to the instructor. Do not send email or messages.
7. Keep the shared spreadsheet unchanged. Do not mark papers read, selected, excluded, or extracted based on retrieval status.

## Completion report

Report the count downloaded, already present, and requiring manual retrieval, plus the manifest path and exact paper IDs needing attention. Do not claim that every selected paper has been obtained unless every selected record has a matching, readable PDF.
