# CMES Systematic Literature Review Workspace

## Project status

- **Status:** Planning
- **Course:** Computational Models for Embedded Systems (CMES), 2026-2027
- **SLR theme:** [TO BE DECIDED BY THE TEAM]
- **SLR paper title:** [TO BE DECIDED]
- **Topic scope:** [TO BE DEFINED]
- **Default full-text download folder:** `papers/full-text/`
- **Extraction sheet name:** `Data Extraction` [TEAM TO CREATE MANUALLY IN THE SHARED WORKBOOK]
- **Last updated:** 2026-11-12

This README is the project source of truth for the SLR title, topic, research questions, team size, paper targets, and agreed search rules. The Master agent must read this file before assigning search work. If a required value is missing or unclear, it should ask the team rather than invent or change it.

## Team and paper targets

- **Number of team members:** 6 [CONFIRMED BY TEAM; confirm team-size exception with instructor]
- **Candidate papers per team member:** 30
- **Target unique candidate papers across the team:** 180
- **Full-text papers to select per team member after abstract screening:** 10
- **Expected full-text papers across the team:** Up to 60, subject to screening and deduplication

The 180-paper target means 180 distinct candidate papers across all team members. A duplicate does not count toward a member's 30-paper quota or the team total. Duplicate findings must be retained and marked; they must not be deleted. The responsible searcher should find replacement papers until their unique, verified quota is met. Only after verification does the team manually enter accepted unique candidates in the workbook.

> **Instructor confirmation needed:** The course brief states teams of 3-5 students. This project currently has six members. Confirm that the six-person team is accepted before treating the team size as final for submission.

## Team members

| Searcher ID | Name | Contact / identifier | Candidate quota | Status |
|---|---|---|---:|---|
| S01 | [NAME] | [IDENTIFIER] | 30 | To assign |
| S02 | [NAME] | [IDENTIFIER] | 30 | To assign |
| S03 | [NAME] | [IDENTIFIER] | 30 | To assign |
| S04 | [NAME] | [IDENTIFIER] | 30 | To assign |
| S05 | [NAME] | [IDENTIFIER] | 30 | To assign |
| S06 | [NAME] | [IDENTIFIER] | 30 | To assign |

## Research definition

### SLR title

[TO BE DECIDED]

### Topic and scope

[TO BE DECIDED WITH THE TEAM]

### Research questions

1. [RQ1 - TO BE DEFINED]
2. [RQ2 - TO BE DEFINED]
3. [RQ3 - TO BE DEFINED]

Add or remove questions as agreed by the team. These questions should guide the search, inclusion criteria, extraction form, analysis, and report.

### Data extraction characteristics and codebook

Complete this section only after the theme, scope, and RQs are agreed. The characteristics must help describe the studies or answer one or more RQs. The course brief requires extracting at least five relevant characteristics; the final list and definitions are a team decision.

| ID | Characteristic | Operational definition / allowed values | Related RQ(s) | Missing-data rule |
|---|---|---|---|---|
| C1 | [TO BE DEFINED] | [WHAT TO RECORD; VALUES/CATEGORIES IF APPLICABLE] | [RQ IDs] | [NOT REPORTED / UNCLEAR / NOT APPLICABLE] |
| C2 | [TO BE DEFINED] | [WHAT TO RECORD; VALUES/CATEGORIES IF APPLICABLE] | [RQ IDs] | [NOT REPORTED / UNCLEAR / NOT APPLICABLE] |
| C3 | [TO BE DEFINED] | [WHAT TO RECORD; VALUES/CATEGORIES IF APPLICABLE] | [RQ IDs] | [NOT REPORTED / UNCLEAR / NOT APPLICABLE] |
| C4 | [TO BE DEFINED] | [WHAT TO RECORD; VALUES/CATEGORIES IF APPLICABLE] | [RQ IDs] | [NOT REPORTED / UNCLEAR / NOT APPLICABLE] |
| C5 | [TO BE DEFINED] | [WHAT TO RECORD; VALUES/CATEGORIES IF APPLICABLE] | [RQ IDs] | [NOT REPORTED / UNCLEAR / NOT APPLICABLE] |

- **Codebook version/date:** [TO BE SET]
- **Pilot paper(s):** [TO BE SELECTED]
- **Team review/approval:** [NAMES AND DATE]
- **Required summary fields:** approach, method, dataset/system or study context, and results (one paragraph per selected paper)
- **Evidence rule:** each extracted value needs a concise evidence paraphrase and page/section locator in its Markdown record; do not guess missing information.

Do not start substantive extraction while the characteristics remain placeholders. Pilot the agreed form on one or two papers, resolve interpretation differences, then freeze/version the codebook before the full extraction batch.

## Search rules

### Formal search sources

The course brief specifies these sources for the initial formal search:

- IEEE Xplore
- ACM Digital Library
- SpringerLink
- Web of Science

The 2026 conference program websites discussed during topic exploration can be used to discover themes or seed papers. They do not replace searches in the approved sources. Snowballing should be recorded separately and follow the course instructions and the team's agreed protocol.

### Search parameters to complete

- **Search start date:** [DATE]
- **Search end date / publication cutoff:** [DATE OR NONE]
- **Language:** [TO BE AGREED]
- **Eligible publication types:** [TO BE AGREED]
- **Inclusion criteria:** [TO BE AGREED]
- **Exclusion criteria:** [TO BE AGREED]
- **Snowballing procedure:** [TO BE AGREED]
- **Search strings by database:** [TO BE DEFINED AFTER THE TOPIC AND RQs]

Every search run must record the database, exact query, search date, filters, searcher, and result count. Save exports or search evidence under `search/exports/` when available and permitted.

## Agent workflow

Agent role instructions are stored in [`agents/master.md`](agents/master.md), [`agents/searcher.md`](agents/searcher.md), [`agents/selection-ranker.md`](agents/selection-ranker.md), [`agents/workbook-editor.md`](agents/workbook-editor.md), [`agents/full-text-retriever.md`](agents/full-text-retriever.md), and [`agents/paper-extractor.md`](agents/paper-extractor.md). Reusable task guidance is stored in `skills/`. Each Searcher uses [`search/search-template.md`](search/search-template.md) to create its findings file under `search/findings/`.

### Master agent

1. Read this README and use its values as the assignment configuration.
2. Start one Searcher agent per team member, passing the agreed topic, research questions, approved sources, search rules, and that searcher's quota.
3. Collect each Searcher's Markdown findings file from `search/findings/`.
4. Verify publication metadata and links, identify duplicates, and mark each finding's status in its findings file.
5. Mark duplicates or invalid records and request replacement candidates from the responsible Searcher.
6. Track verified unique counts until every member's quota and the team target are met.
7. After the team verifies a batch, the team can ask the Workbook Editor to record those verified unique papers in the Candidate Register. There is no automatic import of findings.
8. Once the abstract-screening rules are agreed, provide each member's verified candidate set to the Selection & Ranker for a provisional, explained recommendation. The member reviews and decides; the agent does not choose the final papers.
9. After the member/team confirms its selections, the team can ask the Workbook Editor to record them in Final Selected Papers. There is no automatic synchronization between sheets.
10. Give the Full-Text Retriever the team-approved selected-paper list and a destination folder. It attempts open-access retrieval and records papers needing manual retrieval; it does not edit the workbook.
11. Do not change the topic, research questions, search rules, or quotas. If information is missing, ask the team.

### Searcher agent

Each Searcher has one job: find the assigned number of relevant research papers using the approved sources and document the evidence in its dedicated Markdown file. Searchers must not delete submitted findings or claim a paper is verified without a matching database or publisher record.

### Selection & Ranker agent

The Selection & Ranker uses [`skills/slr-screening-ranking/SKILL.md`](skills/slr-screening-ranking/SKILL.md) to screen a member's verified candidates against the agreed criteria and, when an approved rubric exists, provide provisional rankings with reasons. It writes review notes under `search/rankings/`; the member makes the final selection.

### Workbook Editor agent

The Workbook Editor uses [`skills/slr-verified-workbook-entry/SKILL.md`](skills/slr-verified-workbook-entry/SKILL.md) for explicit, team-requested data-entry tasks. It writes only approved records, does not automatically import findings or sync sheets, and stops if the target sheet's schema has not been agreed.

### Full-Text Retriever agent

The Full-Text Retriever uses [`skills/slr-fulltext-retrieval/SKILL.md`](skills/slr-fulltext-retrieval/SKILL.md) and [`scripts/download_oa_paper.py`](scripts/download_oa_paper.py) to try DOI-based open-access retrieval for the team-approved selected papers. PDFs are saved under `papers/full-text/` by default and retrieval outcomes are recorded in [`papers/retrieval-manifest.csv`](papers/retrieval-manifest.csv). When no suitable open PDF is available, the agent records that manual retrieval is needed through the instructor-approved publisher or university access routes. It does not bypass access controls or edit the workbook.

### Paper Extractor agent

The Paper Extractor uses [`skills/slr-paper-extraction/SKILL.md`](skills/slr-paper-extraction/SKILL.md) and [`papers/extractions/TEMPLATE.md`](papers/extractions/TEMPLATE.md) to extract only team-selected, readable full-text papers. It writes one Markdown record per paper under `papers/extractions/`, including a value, evidence paraphrase, and page/section locator for each agreed characteristic. It leaves each record awaiting team review and does not edit the workbook.

### Extraction review and workbook entry

The team reviews the Markdown records and requests corrections as needed. Only explicitly approved records may be entered by the Workbook Editor in the `Data Extraction` sheet, after the team has created the sheet and agreed the final characteristic columns. The Markdown record remains the evidence trail; workbook entry is a separate, explicit action.

### Finding record

Use one record per candidate paper. The full copy-ready template and instructions are maintained in [`search/search-template.md`](search/search-template.md).

The DOI and link should resolve to matching publication information. A working URL by itself does not establish relevance, peer-review status, or eligibility. Searchers leave `Master status` as `pending`; only the Master updates that field and `Duplicate of`.

## End-to-end workflow

1. Agree the theme, title, scope, and research questions with the team; fill in this README.
2. Confirm the six-person team arrangement with the instructor.
3. Agree eligibility criteria, search parameters, keywords, and database-specific queries.
4. Search the approved databases and record up to 30 unique candidates per member, targeting 180 unique candidates overall. Conduct and log snowballing as agreed.
5. Verify candidate records, deduplicate, and backfill invalid or duplicate entries.
6. Screen abstracts and select 10 papers per member for full-text review.
7. Define and approve the extraction codebook after the topic and RQs are settled; pilot it on one or two papers.
8. Extract at least five agreed characteristics per selected paper into individual Markdown records, including page/section evidence and the required summary paragraph.
9. Have the team review and correct the records; enter only approved records in the `Data Extraction` sheet using the Workbook Editor.
10. Analyze the extracted data; create at least five charts and answer each research question.
11. Discuss results, gaps, challenges, open issues, future work, and recommendations.
12. Complete the report using the course template, prepare the 10-minute Pecha Kucha presentation and video, and create the poster.
13. Check and submit the final Excel workbook, PDF report, video, and poster in the course Teams assignment.

## Deliverables

- **Shared spreadsheet name:** CMES SLR Research Papers
- **Shared Google Sheets workbook:** CMES SLR Research Papers. The live link is kept in the local-only `private-links.md` file and should be shared directly with team members, not published in this public repository.
- **Agreed initial sheets:** `Candidate Register` (verified unique candidates entered after review) and `Final Selected Papers` (team-confirmed selections entered after screening)
- **Data Extraction sheet:** `Data Extraction` [CREATE MANUALLY AFTER TEAM AGREES THE STRUCTURE]
- **Data Extraction layout:** One row per selected paper; base columns: Paper ID, Title, DOI, Authors, Year, Journal/Conference, Extraction status, Reviewer, Review date, Extraction record link; add one column per agreed characteristic (C1-C5 or more)
- **Evidence location:** Paper-specific Markdown records in `papers/extractions/`, with evidence paraphrases and page/section locators for each value
- **Data Extraction column schema approval:** [TO BE AGREED AFTER THEME, RQs, AND CODEBOOK ARE FINAL]
- **Candidate Register column schema:** [TO BE AGREED BEFORE ENTRY]
- **Final Selected Papers column schema:** [TO BE AGREED BEFORE ENTRY]
- **Planned additional sheets:** data extraction, tabulated results, and charts
- **SLR report PDF:** use the provided course LaTeX template. The downloaded template bundle is under `report/2024_CMES_SLR_Student1Student2Student3/`; its main source is [`2022_SLR_Student1Student2Student3.tex`](report/2024_CMES_SLR_Student1Student2Student3/2022_SLR_Student1Student2Student3.tex). Preserve this downloaded copy and make a working copy with the team-approved author list before writing the report.
- **Recorded 10-minute Pecha Kucha presentation**
- **Poster**

## Workspace map

```text
CMES-SLR/
├── README.md                 # Project source of truth and workflow
├── protocol/                 # Search, eligibility, and review protocol
├── agents/
│   ├── master.md             # Master agent instructions
│   ├── searcher.md           # Searcher agent instructions
│   ├── selection-ranker.md   # Provisional screening/ranking role
│   ├── workbook-editor.md    # On-demand, approved workbook updates
│   ├── full-text-retriever.md # Attempts open-access PDF retrieval for selected papers
│   ├── paper-extractor.md    # Extracts evidence into reviewable per-paper Markdown files
│   └── prompts/              # Optional runtime-specific launch prompts
├── search/
│   ├── search-template.md    # Copy-ready candidate finding template
│   ├── exports/              # Database exports and search evidence
│   ├── findings/             # One findings Markdown file per Searcher
│   └── rankings/             # Member review and provisional ranking notes
├── skills/
│   ├── slr-screening-ranking/       # Agreed-criteria abstract screening guidance
│   ├── slr-verified-workbook-entry/ # Controlled workbook entry guidance
│   ├── slr-fulltext-retrieval/      # DOI-based open-access retrieval and manual fallback
│   └── slr-paper-extraction/        # Evidence-based extraction with team review gate
├── scripts/
│   └── download_oa_paper.py  # Safe DOI-to-open-access-PDF downloader
├── papers/
│   ├── full-text/            # Retrieved PDFs for selected papers
│   ├── extractions/          # One reviewable extraction record per selected paper
│   │   └── TEMPLATE.md       # Copy for each Paper ID
│   └── retrieval-manifest.csv # Retrieval status and provenance log
├── references/               # Course guidance and reference material
├── report/                   # Report working files and final PDF
├── presentation/             # Slides and recorded presentation
└── poster/                   # Poster working files and final version
```

The course PDFs and example papers currently at the workspace root remain in place. They can be organized into `references/` later if the team wants that change.


