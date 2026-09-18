# ZCAP × ZCG grants

Which members of the Zcash Community Advisory Panel (ZCAP) have received a Zcash Community Grant (ZCG), 2021 to September 2026.

**Result: 72 of 201 ZCAP members (36%)** — 45 direct grantees, 27 named team members of a grantee. Two more were approved but paid nothing.

- `zcap-zcg-grants.csv` — one row per member/grant with project, org, role, proposal link, first payment, status.
- `zcap-zcg.html` — the same as a filterable page (also at https://claude.ai/artifact/PHduP7iegoVQkY5ihoTsX7).
- `data/` — the two source sheets (ZCG grants ledger, ZCAP list) and the derived JSON.
- `scripts/` — `matches.py` holds every match with its evidence; `build.py` joins it to the ZCAP list; `page.py` renders the HTML.

## Derived numbers (`scripts/stats.py`)

| | Count | Share of ZCAP | Share of recipients |
|---|---|---|---|
| Received a ZCG grant | 72 | 36% | |
| More than one grant | 50 | 25% | 69% |
| Received a grant after joining ZCAP | 45 | 22.4% | 63% |

A "grant" is a distinct ledger grant; renewals and new quarters count separately. The after-joining figure is a lower bound: bundled series are dated by their first payment.

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

## Audit (Sep 2026)

Twelve independent adversarial passes re-verified every row against the issue bodies, forum threads, profiles and the ledger (`audit/findings/`). Net effect on the count: zero. Changes made:

- Removed Bryan Gillespie (Inversed Tech co-founder, but not on the 2023 grant; joined the forum after approval) and Eran Tromer (self-described unpaid advisor on both the Columbia and QEDIT grants).
- Added AAmandita and Rodrigo Schönell: the Zcash Brazil 2026 application names no individuals, but its monthly milestone reports name both as team members.
- Julian Abraham moved to direct grantee (GitHub craftsoldier, co-owner of the Zcash Name Service application).
- Dropped grant lines that did not hold: Michae2xl on Zcash Network School (unpaid advisor), Olli Tiainen on Ziggurat (not named; CEO of the org), Yoditar on Generation Z (Roosevelt's personal grant), zancas "Sofia" (never paid).
- Corrected dates, links and evidence on about twenty lines; every series now links its own issues.
- Reclassified Amber O'Hearn (Least Authority board and former ZCG committee member, never ECC/ZF) to not matched; Natalie E. and Scott Onder to ECC/ZF.

Residual uncertainty: the "Tron" row rests on the name and join date (the paid ZecHub contributor uses GitHub onajifortune and has no linkable forum account); Max Hampshire is identified from commit authorship and posting behaviour rather than a page naming him. The forum user "Emmanuel" is a different person from Zcash Nigeria's emmalexo and is not counted. ZCG's 2022-23 Global Ambassador Program paid Eric Vaughn, AidenZ and artkor directly, but that is a program contract, not a grant, and is not in the ledger; they are not counted.
