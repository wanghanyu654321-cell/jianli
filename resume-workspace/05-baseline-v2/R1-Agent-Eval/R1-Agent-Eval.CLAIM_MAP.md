# R1 Agent Eval Claim Map

| bullet_id | resume location | claim_id | evidence locator | status |
|---|---|---|---|---|
| R1-S01 | Summary | FCT-02,FCT-03,FCT-05,FCT-08,FCT-28 | CLAIM_LEDGER FCT-02–FCT-08,FCT-28 | FACT_DOCUMENTED |
| R1-S02 | Core competencies | FCT-03,FCT-05,FCT-08,FCT-13,FCT-18,FCT-28 | DER-001:35-46,54-80,137-163,217-232,514-536 | FACT_DOCUMENTED |
| R1-W01 | 人瑞 bullet 1 | FCT-03 | DER-001:35-46 | FACT_DOCUMENTED |
| R1-W02 | 人瑞 bullet 2 | FCT-03,FCT-05 | DER-001:37-58 | FACT_DOCUMENTED |
| R1-W03 | 人瑞 bullet 3 | FCT-03 | DER-001:42-44 | FACT_DOCUMENTED |
| R1-W04 | 人瑞 bullet 4 | FCT-04 | DER-001:47-53 | FACT_DOCUMENTED |
| R1-W05 | 人瑞 bullet 5 | FCT-05 | DER-001:54-58 | FACT_DOCUMENTED |
| R1-W06 | 人瑞 bullet 6 | FCT-06 | DER-001:59-67 | FACT_DOCUMENTED |
| R1-W07 | 今宜 bullet 1 | FCT-09,FCT-12,FCT-13,FCT-14 | DER-001:91-97,112-175 | FACT_DOCUMENTED |
| R1-W08 | 今宜 bullet 2 | FCT-12,FCT-13 | DER-001:137-163 | FACT_DOCUMENTED |
| R1-W09 | 今宜 bullet 3 | FCT-15 | DER-001:176-196 | FACT_DOCUMENTED |
| R1-W10 | 朗臻 bullet 1 | FCT-18 | DER-001:217-226 | FACT_DOCUMENTED |
| R1-W11 | 朗臻 bullet 2 | FCT-19,FCT-20 | DER-001:227-247 | FACT_DOCUMENTED |
| R1-W12 | 朗臻 bullet 3 | FCT-17,FCT-19 | DER-001:208-232 | FACT_DOCUMENTED |
| R1-P01 | Agent bullet 1 | FCT-28 | DER-001:514-536 | FACT_DOCUMENTED |
| R1-P02 | Agent bullet 2 | FCT-25,FCT-26 | DER-001:454-490 | DOCUMENTED_ONLY |
| R1-P03 | Agent bullet 3 | FCT-25,FCT-26,FCT-27 | DER-001:403-453,491-512 | DOCUMENTED_ONLY |
| R1-P04 | Agent bullet 4 | FCT-24,FCT-25,FCT-28 | DER-001:379-418,514-536 | DOCUMENTED_ONLY |
| R1-P05 | Agent bullet 5 | FCT-27 | DER-001:491-512 | DOCUMENTED_ONLY |
| R1-A01 | Additional tools | FCT-25,FCT-28 | DER-001:394-402,514-523 | DOCUMENTED_ONLY / FACT_DOCUMENTED |

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
