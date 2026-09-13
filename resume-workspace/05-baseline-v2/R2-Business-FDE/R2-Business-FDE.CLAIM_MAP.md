# R2 Business FDE Claim Map

| bullet_id | resume location | claim_id | evidence locator | status |
|---|---|---|---|---|
| R2-S01 | Summary | FCT-02,FCT-03,FCT-12,FCT-21,FCT-28 | CLAIM_LEDGER FCT-02,FCT-03,FCT-12,FCT-21,FCT-28 | FACT_DOCUMENTED |
| R2-S02 | Core competencies | FCT-03,FCT-12,FCT-22,FCT-24,FCT-25,FCT-28 | DER-001:35-58,276-378,379-453,514-536 | FACT_DOCUMENTED / DOCUMENTED_ONLY |
| R2-P01 | Agent bullet 1 | FCT-28 | DER-001:514-536 | FACT_DOCUMENTED |
| R2-P02 | Agent bullet 2 | FCT-25,FCT-26 | DER-001:403-453 | DOCUMENTED_ONLY |
| R2-P03 | Agent bullet 3 | FCT-25,FCT-26 | DER-001:454-490 | DOCUMENTED_ONLY |
| R2-P04 | Agent bullet 4 | FCT-25,FCT-26 | DER-001:439-453 | DOCUMENTED_ONLY |
| R2-P05 | Agent bullet 5 | FCT-28 | DER-001:514-536 | FACT_DOCUMENTED |
| R2-W01 | 人瑞 bullet 1 | FCT-03 | DER-001:35-46 | FACT_DOCUMENTED |
| R2-W02 | 人瑞 bullet 2 | FCT-03,FCT-05 | DER-001:37-58 | FACT_DOCUMENTED |
| R2-W03 | 人瑞 bullet 3 | FCT-04,FCT-05 | DER-001:47-58 | FACT_DOCUMENTED |
| R2-W04 | 人瑞 bullet 4 | FCT-06 | DER-001:59-67 | FACT_DOCUMENTED |
| R2-W05 | 今宜 bullet 1 | FCT-09,FCT-12,FCT-13,FCT-14 | DER-001:91-175 | FACT_DOCUMENTED |
| R2-W06 | 今宜 bullet 2 | FCT-10,FCT-11 | DER-001:98-111 | FACT_DOCUMENTED |
| R2-W07 | 今宜 bullet 3 | FCT-13,FCT-15 | DER-001:137-196 | FACT_DOCUMENTED |
| R2-W08 | 朗臻 bullet 1 | FCT-21,FCT-22 | DER-001:276-307 | FACT_DOCUMENTED |
| R2-W09 | 朗臻 bullet 2 | FCT-23 | DER-001:308-355 | FACT_DOCUMENTED |
| R2-W10 | 朗臻 bullet 3 | FCT-20,FCT-23 | DER-001:257-378 | FACT_DOCUMENTED |
| R2-A01 | Project tool line | FCT-25,FCT-28 | DER-001:394-402,514-523 | DOCUMENTED_ONLY / FACT_DOCUMENTED |

## Semantic grounding audit

| Resume surface | Semantic status | Revalidation basis |
|---|---|---|
| Summary | FULLY_GROUNDED | Every independent summary assertion maps to one or more current FCT claims; no experience-year claim is inferred. |
| Core competencies | FULLY_GROUNDED | Each listed capability is grounded in the mapped work or project claims; unsupported JD keywords were not added. |
| Work experience bullets | FULLY_GROUNDED | Each bullet's role, date, action, metric and boundary has a current FCT mapping; dates use the re-read timeline. |
| Project bullets | PARTIALLY_GROUNDED | Each independent project assertion maps to FCT-24–FCT-28, but the project remains DOCUMENTED_ONLY because the matching checkout is unavailable. |
| Project tools / skills | PARTIALLY_GROUNDED | Technology names map to FCT-25/FCT-28 and remain project-practice evidence, not production proof. |
| Education marker | FULLY_GROUNDED | `[LOCAL_ONLY_EDUCATION]` makes no public school or graduation claim; the fact source contains no graduation date. |

Semantic audit result: all independent factual statements in the resume surfaces are either FULLY_GROUNDED or explicitly PARTIALLY_GROUNDED with a documented-only boundary; no UNGROUNDED statement is retained.
