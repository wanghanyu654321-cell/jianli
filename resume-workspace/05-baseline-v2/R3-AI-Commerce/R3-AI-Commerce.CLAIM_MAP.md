# R3 AI Commerce Claim Map

| bullet_id | resume location | claim_id | evidence locator | status |
|---|---|---|---|---|
| R3-S01 | Summary | FCT-09,FCT-17,FCT-18,FCT-21,FCT-22,FCT-03 | CLAIM_LEDGER FCT-03,FCT-09,FCT-17–FCT-22 | FACT_DOCUMENTED |
| R3-S02 | Core competencies | FCT-09,FCT-13,FCT-15,FCT-17,FCT-18,FCT-21,FCT-23 | DER-001:91-378 | FACT_DOCUMENTED |
| R3-W01 | 人瑞 bullet 1 | FCT-02,FCT-03,FCT-08 | DER-001:31-46,70-80 | FACT_DOCUMENTED |
| R3-W02 | 人瑞 bullet 2 | FCT-03,FCT-05 | DER-001:37-58 | FACT_DOCUMENTED |
| R3-W03 | 人瑞 bullet 3 | FCT-03,FCT-05 | DER-001:42-58 | FACT_DOCUMENTED |
| R3-W04 | 人瑞 bullet 4 | FCT-04,FCT-05 | DER-001:47-58 | FACT_DOCUMENTED |
| R3-W05 | 人瑞 bullet 5 | FCT-06,FCT-08 | DER-001:59-80 | FACT_DOCUMENTED |
| R3-W06 | 今宜 bullet 1 | FCT-09,FCT-12 | DER-001:91-136 | FACT_DOCUMENTED |
| R3-W07 | 今宜 bullet 2 | FCT-10,FCT-11 | DER-001:98-111 | FACT_DOCUMENTED |
| R3-W08 | 今宜 bullet 3 | FCT-13,FCT-14 | DER-001:137-175 | FACT_DOCUMENTED |
| R3-W09 | 今宜 bullet 4 | FCT-15 | DER-001:176-196 | FACT_DOCUMENTED |
| R3-W10 | 朗臻 bullet 1 | FCT-16,FCT-17 | DER-001:198-216 | FACT_DOCUMENTED |
| R3-W11 | 朗臻 bullet 2 | FCT-18 | DER-001:217-226 | FACT_DOCUMENTED |
| R3-W12 | 朗臻 bullet 3 | FCT-19,FCT-20 | DER-001:227-247 | FACT_DOCUMENTED |
| R3-W13 | 朗臻 bullet 4 | FCT-21,FCT-22 | DER-001:276-307 | FACT_DOCUMENTED |
| R3-W14 | 朗臻 bullet 5 | FCT-23 | DER-001:308-378 | FACT_DOCUMENTED |
| R3-P01 | Agent bullet 1 | FCT-28 | DER-001:514-536 | FACT_DOCUMENTED |
| R3-P02 | Agent bullet 2 | FCT-24,FCT-25,FCT-26 | DER-001:379-490 | DOCUMENTED_ONLY |
| R3-P03 | Agent bullet 3 | FCT-28 | DER-001:514-536 | FACT_DOCUMENTED |
| R3-A01 | Project tools | FCT-25,FCT-28 | DER-001:394-402,514-522 | DOCUMENTED_ONLY / FACT_DOCUMENTED |

## Semantic grounding audit

| Resume surface | Semantic status | Revalidation basis |
|---|---|---|
| Summary | FULLY_GROUNDED | Every independent summary assertion maps to current FCT claims; no experience-year claim is inferred. |
| Core competencies | FULLY_GROUNDED | Each listed capability is grounded in the mapped work or project claims; unsupported JD keywords were not added. |
| Work experience bullets | FULLY_GROUNDED | Each bullet's role, date, action, metric and boundary has a current FCT mapping; dates use the re-read timeline. |
| Project bullets | PARTIALLY_GROUNDED | Each independent project assertion maps to FCT-24–FCT-28, but the project remains DOCUMENTED_ONLY because the matching checkout is unavailable. |
| Project tools / skills | PARTIALLY_GROUNDED | Technology names map to FCT-25/FCT-28 and remain project-practice evidence, not production proof. |
| Education marker | FULLY_GROUNDED | `[LOCAL_ONLY_EDUCATION]` makes no public school or graduation claim; the fact source contains no graduation date. |

Semantic audit result: all independent factual statements in the resume surfaces are either FULLY_GROUNDED or explicitly PARTIALLY_GROUNDED with a documented-only boundary; no UNGROUNDED statement is retained.
