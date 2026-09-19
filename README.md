# ZCAP × ZCG grants

Which members of the Zcash Community Advisory Panel (ZCAP) have received a Zcash Community Grant (ZCG), 2021 to September 2026.

| | Count | Share of ZCAP |
|---|---|---|
| ZCAP members | 201 | |
| Received a ZCG grant | 72 | 36% |
| More than one grant | 50 | 25% |
| Received a grant after joining ZCAP | 48 | 24% |

The 48 were named on 89 grants approved after they joined ZCAP: $12,270,936 approved, $10,008,338 paid to date (`scripts/after_join.py`).

## Where the money went (`scripts/concentration.py`)

ZCG has paid out $20.1M to 78 grantees. The top 5 grantees received 57% of it, the top 10 76%, the top 20 90%. QEDIT alone received 29%; Hanh, one person, 8%.

By count: 171 paid grants went to 79 grantees; 27 grantees received more than one. The top 10 grantees hold 72 grants (42%), the top 20 hold 105 (61%). Hanh alone has 12.

ZCAP members are the grantee or a named team member on 120 of the 171 paid grants (70%), carrying 75% of the money ($15.1M).

## Files

- `zcap-zcg-grants.csv` — one row per member and grant: project, org, role, evidence, proposal link, first payment, status
- `zcap-zcg.html` — the same as a filterable page
- `data/` — the ZCG ledger, the ZCAP list, and the derived JSON
- `scripts/` — `matches.py` (every match with its evidence), `build.py`, `page.py`, `stats.py`, `after_join.py`, `concentration.py`
- `audit/` — twelve independent adversarial re-verifications of every row

## Rules

- Counts direct grantees and people named on the grant as team members or staff of the grantee.
- Does not count DAO membership, ambassador programs, unpaid advisors, founders' reward, or ECC / ZF employment.
- A cancelled grant counts only if a milestone was paid. Approved but unpaid grants are listed separately and not counted.
- Team membership is taken from the application or from the grantee's milestone reports to ZCG; org staff count only for grants they are shown working on.
- "After joining" means the grant was approved in a month strictly after the member's ZCAP join month (earliest ledger payment is the proxy; the exclusions where approval is known to be earlier are listed in `scripts/after_join.py`). Dollar totals count each grant once; red·bridge Launch ($477,658, startup paid, not yet in the ledger) is included.

## Weakest rows

Tron (linked to ZecHub's paid "@tron" by name and join date only), Max Hampshire (Nym engineer delivering the grant, self-identified in the thread), Arlo Byrne (Zingo Labs staff by forum title and commits; applications withhold names), J.W. Verret and Paul Brigner (board directors of Pretty Good Policy for Zcash, compensated per the application), AAmandita, Rodrigo Schönell and Patrick Diniz (Zcash Brazil 2026 team per monthly reports, not the application). Details in `audit/`.
