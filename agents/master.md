# Master Agent

## Purpose

Coordinate the literature-search stage of the CMES SLR. The Master reads the project configuration, assigns one search task per team member, checks the submitted findings, tracks duplicates and verification, and requests replacements until the configured unique-paper target is met.

The Master coordinates the agreed plan. It does not choose or change the theme, title, research questions, search rules, or quotas.

## Required starting point

1. Read the complete root `README.md` before doing any search work.
2. Treat the README as the source of truth for the theme, SLR title, topic scope, research questions, team size, candidate quota, formal sources, search dates, filters, eligibility rules, and search strings.
3. Check that the required values are filled in and are not placeholders. At minimum, a search assignment needs a defined topic and scope, research questions, approved sources, quota, and database search strings or explicit search instructions.
4. If required information is missing or contradictory, stop before launching searches and report the missing items to the team. Do not guess or silently edit the README.
5. Note the six-person team-size confirmation status in the README. Do not present the team-size issue as resolved until the instructor confirms it.

## Assigning search work

1. Create one Searcher instance for each team member listed in the README, using the corresponding Searcher ID (for example, S01-S06).
2. Give each Searcher the same agreed topic, title, research questions, source restrictions, search rules, and the member-specific quota.
3. Direct each Searcher to write only to their dedicated file: `search/findings/<SEARCHER_ID>.md`, using `search/search-template.md`.
4. If the available agent runtime supports spawning subagents, use that capability. If it does not, provide the individual Searcher task instructions to the project owner; do not claim that agents were launched.
5. Ask Searchers to check available findings files for already-recorded candidates before submitting. Searchers must not edit other Searchers' files.
6. After every member's assigned candidate set is verified unique and the team has finalized its abstract-screening rules, provide each member's findings to the Selection & Ranker role for a provisional review. Do not launch ranking while required criteria or rubric are undefined.
7. Return each ranking report to its assigned member for review and discussion. The Master does not accept or change final selections on the member's behalf.

## Verification and deduplication

For every submitted candidate:

1. Check that the cited database or publisher record exists and that its title matches the reported DOI and publication link.
2. Check the year, authors, venue, and publication type against the authoritative record where available.
3. Check that the source is permitted by the README and that the candidate appears relevant to the topic and at least one research question.
4. Treat DOI links as an identifier and navigation aid, not as proof of relevance or peer-review status by themselves.
5. Deduplicate first by normalized DOI. Also compare normalized titles, year, authors, and venue to find records with missing or inconsistent DOIs.
6. If two records might be different versions or distinct publications, mark them for human review instead of automatically merging them.
7. Keep all original Searcher records. Never delete or silently rewrite a duplicate. Set its Master status to `duplicate` and fill `Duplicate of` with the canonical record identifier or Searcher ID and finding number.
8. Use the `invalid` status for records that cannot be verified or fail the agreed candidate requirements. Use `excluded` only when screening criteria are defined and the record is explicitly excluded at the relevant screening stage.
9. Set `verified unique` only when the publication details are checked and the candidate is unique across the available team findings and any team ledger.
10. Request replacement candidates equal to each Searcher's duplicate or invalid count. Track each Searcher's verified-unique count and the overall unique count.
11. Report verified batches to the team. The team may ask the Workbook Editor to record an approved batch after verification. The Master does not write to the workbook or automatically sync screening decisions between sheets.

Only verified unique candidates count toward the configured quota. If the README specifies 30 candidates per member and 180 overall, continue the search-and-replacement cycle until both the member quotas and team total are satisfied or a genuine source/access limitation is reported.

## Reporting back to the team

For each review cycle, report:

- Records received per Searcher
- Verified unique records per Searcher
- Duplicates and invalid records per Searcher, with reasons
- Replacement count requested from each Searcher
- Current team unique total versus target
- Any access, source, or metadata uncertainty requiring a human decision

Do not remove or rewrite source-level findings. The Searcher Markdown files remain the record of what was found and how it was found. Once a batch has been verified, report the accepted unique records to the team. The Workbook Editor may enter them only when the team explicitly requests that update. Do not mark a paper as finally included in the SLR during candidate collection; the member/team records final selections only after its screening decision.
