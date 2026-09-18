# ZCAP × ZCG grants

Which members of the Zcash Community Advisory Panel (ZCAP) have received a Zcash Community Grant (ZCG), 2021 to September 2026.

| | Count | Share of ZCAP |
|---|---|---|
| ZCAP members | 201 | |
| Received a ZCG grant | 72 | 36% |
| More than one grant | 50 | 25% |
| Received a grant after joining ZCAP | 53 | 26% |

## Files

- `zcap-zcg-grants.csv` — one row per member and grant: project, org, role, evidence, proposal link, first payment, status
- `zcap-zcg.html` — the same as a filterable page
- `data/` — the ZCG ledger, the ZCAP list, and the derived JSON
- `scripts/` — `matches.py` (every match with its evidence), `build.py`, `page.py`, `stats.py`, `after_join.py`
- `audit/` — twelve independent adversarial re-verifications of every row

## Rules

- Counts direct grantees and people named on the grant as team members or staff of the grantee.
- Does not count DAO membership, ambassador programs, unpaid advisors, founders' reward, or ECC / ZF employment.
- A cancelled grant counts only if a milestone was paid. Approved but unpaid grants are listed separately and not counted.

## Method

Every ZCAP name and handle was searched in the 90 approved GitHub applications and in the forum threads of the 74 earlier grants. Each hit was read in context, and handle-only matches were checked against forum or GitHub profiles. The result was then audited row by row against the same sources.

Known soft spots: the "Tron" row rests on the name and join date; Max Hampshire is identified from commit authorship rather than a page naming him.

Rebuild: `python3 scripts/build.py && python3 scripts/page.py && python3 scripts/stats.py`
