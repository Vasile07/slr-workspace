---
name: slr-verified-workbook-entry
description: Record team-verified SLR papers and team-approved selections in the shared workbook when explicitly asked. Use for controlled spreadsheet entry, not automatic imports or selection decisions.
---

# SLR Verified Workbook Entry

Use this skill only for an explicit, user-requested update to the SLR workbook. Search findings and rankings remain in Markdown until the team verifies or approves them.

## Inputs and readiness

1. Read the workbook URL and current sheet names from the root `README.md`.
2. Require the requested batch to be identified as (a) team-verified unique candidates, (b) team-approved selected papers, or (c) team-approved extraction records. Never infer approval from a Searcher record, Master/Ranker recommendation, draft extraction, or status formula.
3. Inspect the workbook structure and target sheet before writing. Read the headers and existing rows to identify the exact destination and available columns.
4. The workbook schema is still subject to team agreement. If the target sheet has no approved headers or a required field-to-column mapping is missing, do not create headers, invent a schema, or write data; present the proposed mapping for team approval.
5. If the source records, approval status, destination, or mapping conflict, stop and ask for clarification.

## Controlled update

- Use the Spreadsheets plugin's spreadsheet information, read, and write tools when available.
- Use the exact spreadsheet ID and sheet ID from the README and current workbook inspection. Pass through the exact `conversation_id` returned by the plugin for every subsequent operation.
- Add only the explicitly approved batch to the requested sheet. Do not automatically import new findings, sync statuses between sheets, or run in the background.
- Preserve source provenance where the agreed columns allow it. Do not invent missing metadata; leave it blank or stop if the team's data rules require a value.
- Check existing DOI values and likely title/year duplicates before adding rows. If a conflict or duplicate is found, do not resolve it silently; report it to the team.
- Append new rows without overwriting existing content. Do not delete, clear, sort, reformat, add sheets, change formulas, or change headers unless the user separately requests that specific change.
- After writing, read back the changed range and confirm that the values match the approved input.

## Supported entry modes

### Verified candidate batch

Enter only candidates the team has verified as unique and accepted for the Candidate Register. Do not add rejected, unverified, or duplicate records as if they were accepted candidates. Keep their search and duplicate history in their Markdown findings files.

### Team-approved selected papers

Enter only papers that the member/team explicitly selected after abstract screening. A Ranker recommendation or provisional top-ten list is not sufficient. Do not automatically copy records from the Candidate Register; use the approved batch and the agreed Final Selected Papers columns.

### Team-approved extraction records

Enter records in `Data Extraction` only when each paper's Markdown extraction file is explicitly marked `Approved for workbook` by a team member, has no unresolved correction requests, and maps to the agreed extraction columns. Preserve the Paper ID and extraction-file link so values remain traceable to their evidence. Do not resolve disputed or unclear scientific interpretations while entering data; return them to the team for review.

Future workbook sheets, including data extraction, tabulation, and charts, may be updated only after their schemas and source data are agreed and the user requests the action.

## Completion report

After an update, report the target sheet, number of rows added, identifiers of the added papers, and the read-back result. If no write occurred, state what approval or schema detail is missing.
