# ZCAP × ZCG grants

Which members of the Zcash Community Advisory Panel (ZCAP) have received a Zcash Community Grant (ZCG), 2021 to September 2026.

**Result: 72 of 200 ZCAP members (36%)** — 44 direct grantees, 28 named team members of a grantee. Two more were approved but paid nothing.

- `zcap-zcg-grants.csv` — one row per member/grant with project, org, role, proposal link, first payment, status.
- `zcap-zcg.html` — the same as a filterable page (also at https://claude.ai/artifact/PHduP7iegoVQkY5ihoTsX7).
- `data/` — the two source sheets (ZCG grants ledger, ZCAP list) and the derived JSON.
- `scripts/` — `matches.py` holds every match with its evidence; `build.py` joins it to the ZCAP list; `page.py` renders the HTML.

## Rules

- Founders' reward and ECC / ZF employment do not count. ZF or ECC people who separately took a ZCG grant do (DecentralistDan, Taylor Hornby).
- Being on the actual team of an organisation that received a grant counts (named in the application, or staff of the grantee). DAO membership, ambassador programs and unpaid advisor roles do not.
- A cancelled grant counts only if a milestone was actually paid.
- Unpaid advisors do not count.

## Method

1. ZCG grants ledger (189 project/grantee pairs) and ZCAP list pulled from the two Google Sheets.
2. Bodies of all 90 approved applications in the ZCG GitHub repo grepped for every ZCAP name and handle; each hit read in context.
3. The 74 grants from 2021 to 2024 predate the GitHub repo; applicants and named team members were taken from the forum threads and archived ZF Grants pages.
4. Handle-only matches verified against forum or GitHub profiles.

Rebuild: `python3 scripts/build.py && python3 scripts/page.py`.
