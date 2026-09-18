"""Headline numbers derived from data/zcap_zcg.json. Run: python3 scripts/stats.py"""
import json,re
from datetime import date
d=json.load(open('data/zcap_zcg.json'))
MON={m:i+1 for i,m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
def month(s):
    m=re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w* (\d{4})',s)
    return date(int(m.group(2)),MON[m.group(1)[:3]],1) if m else None
def joined(s):
    if "Before" in s: return date(2021,4,1)
    m=re.search(r'(\w+) (\d{4})',s); return date(int(m.group(2)),MON[m.group(1)[:3]],1)
def n_grants(r):
    if r['name'].startswith('Hanh'): return 13          # 13 paid grants in the ledger
    n=0
    for g in r['grants']:
        n+=len([x for x in re.split(r';|·',g['project']) if x.strip()])
        if '2024 Q1-Q4' in g['project']: n+=3            # four quarterly grants in the ledger
    return n
rec=[r for r in d if r['tier'] in ("Direct grantee","Named grant team member")]
multi=[r for r in rec if n_grants(r)>1]
after=[r for r in rec if any(month(g['date']) and month(g['date'])>joined(r['joined']) for g in r['grants'])]
N=len(d)
print(f"ZCAP members: {N}")
print(f"Received a ZCG grant (direct or named team member): {len(rec)} = {100*len(rec)/N:.1f}%")
print(f"  of which more than one grant: {len(multi)} = {100*len(multi)/len(rec):.0f}% of recipients, {100*len(multi)/N:.1f}% of ZCAP")
print(f"  of which received a grant after joining ZCAP: {len(after)} = {100*len(after)/len(rec):.0f}% of recipients, {100*len(after)/N:.1f}% of ZCAP (lower bound: bundled series use their first payment date)")
