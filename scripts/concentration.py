"""Concentration of ZCG payouts by grantee, and the share tied to ZCAP members. Run: python3 scripts/concentration.py"""
import csv,re
from collections import defaultdict
rows=[r for r in list(csv.reader(open('data/grants.csv')))[1:] if len(r)>=12]
def amt(r): return float(re.sub(r'[^\d.\-]','',r[5]) or 0) if r[5].strip() else 0
MERGE={"NightHawk":"Nighthawk","Tmek":"tm3k"}
paid=defaultdict(float); byproj=defaultdict(float); n=defaultdict(set)
for r in rows:
    if not r[7].strip(): continue
    g=MERGE.get(r[1].strip(),r[1].strip()) or r[0].strip(); paid[g]+=amt(r); byproj[(r[0].strip(),r[1].strip())]+=amt(r); n[g].add(r[0].strip())
T=sum(paid.values()); s=sorted(paid.items(),key=lambda x:-x[1])
print(f"ZCG paid out ${T:,.0f} to {sum(1 for v in paid.values() if v>0)} grantees (2021 – Sep 2026)")
for k in (1,5,10,20): print(f"  top {k:>2} grantees: {100*sum(v for _,v in s[:k])/T:.0f}%")
print("  top 10:"); [print(f"    {100*v/T:4.1f}%  ${v:>10,.0f}  {g} ({len(n[g])} grants)") for g,v in s[:10]]
# share of payouts on grants where a ZCAP member is grantee or named team (any date)
src=open("scripts/after_join.py").read(); from datetime import date; ns={"date":date}
exec(src.split("zc={r[0]")[0].split("# member -> ")[1].split("\n",1)[1],ns)   # loads MAP + regex helpers
MAP=ns['MAP']; hit=set()
for (p,g) in byproj:
    for pats in MAP.values():
        if any(re.search(gp,g) and re.search(pp,p) for gp,pp in pats): hit.add((p,g)); break
z=sum(byproj[k] for k in hit)
print(f"paid on grants with a ZCAP member as grantee or named team: ${z:,.0f} = {100*z/T:.0f}% ({len(hit)} of {len(byproj)} paid grants)")
