---
name: slr-paper-extraction
description: Extract and document evidence from a team-selected SLR paper using the team's agreed characteristics and research questions.
---

# SLR Paper Extraction

Use this skill only for papers the team has selected for full-text review. Read the root `README.md`, the approved extraction codebook, and `papers/extractions/TEMPLATE.md` before extracting.

## Readiness

- Confirm the paper is team-selected and has a stable Paper ID.
- Confirm the full-text PDF is available and readable.
- Confirm the topic, RQs, and extraction characteristics have been agreed and filled in the README/codebook. If they are still placeholders, do not invent fields or begin a substantive extraction; report what needs agreement.
- Work on one paper per file at `papers/extractions/<PAPER_ID>.md`.

## Extraction

- Extract only information supported by the paper. For each field, record the value, a concise paraphrase of supporting evidence, and its page number or section. Avoid long verbatim quotations.
- Use the agreed missing-data labels (initial placeholder: `Not reported`, `Unclear`, or `Not applicable`) and explain ambiguity. Do not infer an unstated result or method.
- Map each characteristic to the relevant RQ(s), where the codebook defines that mapping.
- Include the paper's approach, method, dataset/system or study context, and results in the per-paper summary required by the course workflow.
- Mark uncertainty explicitly and set status to `Needs review` rather than filling gaps with assumptions.

## Review and handoff

- Start each file as `Draft — team review required`.
- Incorporate requested corrections in the same file, preserving a short review history with reviewer, date, requested change, and resolution.
- Only set `Approved for workbook` after a team member has reviewed the extracted values and evidence and confirms the file is ready.
- Do not edit the spreadsheet. The Workbook Editor enters only files explicitly approved by the team, using the agreed `Data Extraction` sheet schema.

## Completion

Report the Paper ID, extraction file path, any fields marked unclear/not reported, review status, and corrections still needed. Do not claim an extraction batch is complete while any paper is unreadable or awaiting review.
