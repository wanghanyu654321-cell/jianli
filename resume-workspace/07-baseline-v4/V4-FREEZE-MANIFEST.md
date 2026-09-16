# V4 Baseline Freeze Manifest

Status: **FROZEN**  
Branch: `resume/baseline-v2-r1-r3`  
Freeze basis: user-approved complete R1–R6 master supplied in the current resume review cycle.

## Freeze Rule

The six files below are the authoritative V4 baseline for all subsequent optimization.

- Do not delete, merge, summarize, compress, reorder, or rewrite baseline content unless the user explicitly approves that exact change.
- JD-specific delivery versions must be derived from this frozen baseline; optimization must not silently modify the baseline itself.
- Weak-link bullets remain part of the baseline unless explicitly removed by the user.
- Recruiter review, prioritization, and compression belong to derived delivery versions, not to this frozen source.
- Future factual corrections must be made only after explicit user confirmation and must be traceable as a deliberate baseline revision.

## Integrity Verification

The written GitHub blobs were mechanically verified against the corresponding R1–R6 sections of the user-approved source. The Git blob SHA returned by GitHub exactly matches the Git blob SHA computed from each source section, so the stored bytes are exact for all six sections.

| Version | File | Commit | Git Blob SHA | Source Section SHA-256 |
|---|---|---|---|---|
| R1 | `R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | `3f5551650294ecac5c49502e9756b2c51a2fde36` | `a42c0fa175fa5c70e89645d7dd34b133431c48ea` | `ed1bd9f3935ce388f73f026018475af3fc9b770ab8f36a6634ce41fd4eae075d` |
| R2 | `R2-Business-FDE/R2-Business-FDE.RESUME.md` | `4ca085abe4ecf4a3e96e7c64c28951663cba6505` | `539be5c80edbb7c5ce0d4b7467b75192aaee3382` | `c528bd51d6670cf1f8390ca54bc3b286ebbb9270f873e778ef93c2bdf4c51ead` |
| R3 | `R3-AI-Commerce/R3-AI-Commerce.RESUME.md` | `9db8899c5ef42ff512e9fd330654868c09ce8bbd` | `3e89a15ffd2971c8bed6700149c2f24820180c6d` | `18f3e65c47efadae4acd6af79c491cc5ae34f1410aa4becffa9c878340151236` |
| R4 | `R4-AI-Product-Ops/R4-AI-Product-Ops.RESUME.md` | `045c94c4f2ce73856d4e8fec0b06db7b799525ee` | `4d0940d5e4520cc0eddd35b9d6e185b0e7f2984d` | `136b1bc5c20b34c32024b88d037be37c7e872aedc4fad8e5d1bb91b69414c171` |
| R5 | `R5-Agent-Solution/R5-Agent-Solution.RESUME.md` | `2b5fefcf9dc6a041b57388f3bce093fa3092ed1b` | `bcaa36720b8201999bec6f77f99d7f5277448935` | `cc110b8450dd56fc6d9295c00f8ceea0b2e41cfe19c91db2c221dcf8fe538be2` |
| R6 | `R6-AI-Solution/R6-AI-Solution.RESUME.md` | `f3c24f10240963a4de089f6621b2d85ecbc9d874` | `993829d2bf156a1ae0967e0dd74d635c90069135` | `19f580042708cbc874442309b4fb2e3893cdd9423f0d2573c1b0654f527bb133` |

Approved source file SHA-256: `c6c3a0f1d2f2b1d5d20a729b5e99e3940e2c8602a13d648179a25a6960f24fda`

## Baseline Meaning

This freeze preserves the complete reasoning chains and role-specific evidence currently approved for R1–R6. It is the restoration point if any later editing introduces accidental compression, omission, hallucinated facts, or role drift.
