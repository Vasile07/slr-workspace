---
name: slr-screening-ranking
description: Screen and rank SLR candidates using the team's agreed eligibility rules and research questions. Use after Master verification and deduplication; do not make final inclusion decisions.
---

# SLR Screening and Ranking

Use this skill after candidate records have been verified and deduplicated, when the team is screening abstracts and deciding which papers should proceed to full-text review.

## Inputs and readiness

- Read the root `README.md` and the agreed protocol files under `protocol/`.
- Use the topic, scope, RQs, date/type limits, and inclusion/exclusion criteria exactly as agreed.
- Work only on candidate records that the Master has marked `verified unique` and assigned to the relevant member.
- If the scope, criteria, RQs, or ranking rules are blank or contradictory, stop and ask the team to resolve them before screening. Do not invent screening or scoring rules.

## Decision method

1. Assess each candidate against every applicable inclusion and exclusion criterion using the title and abstract.
2. Classify each as `Include`, `Exclude`, or `Unclear` for full-text consideration. For each exclusion, name the criterion and cite the evidence in the record that supports it. Use `Unclear` when the abstract does not provide enough evidence.
3. Separate eligibility from relevance ranking and from study quality. Do not exclude a paper just because another seems stronger. Do not use venue prestige, citation count, author identity, or personal preference unless an agreed protocol explicitly makes it relevant.
4. Rank eligible and unresolved candidates for usefulness to the RQs only if a ranking rubric has been agreed in the protocol. Apply the same rubric to all candidates in that assignment. If no rubric exists, prepare criterion-based screening recommendations and ask the team to approve a rubric before assigning rank numbers.
5. Tie every recommendation to concise evidence from the title/abstract and the relevant RQ or criterion. Do not invent paper findings that are not in the abstract.
6. Return a provisional top-ten recommendation and a small set of alternates, while preserving the full disposition of all candidates. The assigned member makes and records the final selection.

## Output

Create or update `search/rankings/<SEARCHER_ID>.md`. Include:

- Topic, RQs, criteria, and rubric version used
- Candidate ID, exact title, DOI, and abstract-screening disposition
- Criterion evidence and brief rationale
- Provisional rank where the approved rubric supports ranking
- Confidence or unresolved questions
- Provisional top ten and alternates
- Member decision for each paper (`accepted`, `changed`, or `pending`)
- If changed, the member's reason and date

Keep the original recommendation visible when a member changes a decision. The ranking report is a review record, not a substitute for the team's final selection log.

## Boundaries

- Do not search for replacement papers; send gaps or shortfalls to the Master.
- Do not edit Searcher findings or mark their Master verification fields.
- Do not write to or synchronize the spreadsheet.
- Do not treat a provisional rank as final selection. Only the member/team can approve the final papers.
