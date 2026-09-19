import csv,json,html
exec(open('scripts/matches.py').read())
TIER={}  # name -> tier code
A="Direct grantee"; B="Named grant team member"; C="Org member (indirect)"; D="Approved, $0 paid"; Z="ZF / ECC (excluded by rule)"
exec(open('scripts/matches.py').read())
src=open('scripts/matches.py').read()
direct=src.split('# ---------------- Named team members')[0]
team=src.split('# ---------------- Named team members')[1].split('# ---------------- Approved, nothing paid')[0]
for n in M:
    if 'add("%s"'%n in direct: TIER[n]=A
    elif 'add("%s"'%n in team: TIER[n]=B
TIER["Maxime Desalle"]=D; TIER["Lai Ying Tong"]=D; TIER["Julian Abraham"]=D
ZFECC={"Natalie E.","Scott Onder","Alex Bornstein","Alfredo Garcia ","Arya Solhi","Conrado Gouvea","Daira Hopwood ","Danika Delano","DC ","DecentralistDan (on the forum)","Elise Hamdon","Jack Gavigan ","Jack Grigg ","Josh Swihart ","Kris Nuttycombe","Marek","Paige (on the forum)","Pili Guerra","Sean Bowe","Teor","Zooko Wilcox","Autotunafish (on the forum)"}
rows=list(csv.reader(open('data/zcap.csv')))[1:]
names=[r[0] for r in rows]
missing=[n for n in M if n not in names]; assert not missing, missing
out=[]
for name,handle,joined in rows:
    g=M.get(name,[])
    tier=TIER.get(name) or (Z if name in ZFECC else ("" if not g else B))
    out.append(dict(name=name.strip(),handle=handle.strip(),joined=joined.strip(),tier=tier,grants=[dict(project=p,org=o,role=r,link=l,date=d,status=s) for p,o,r,l,d,s in g]))
json.dump(out,open('data/zcap_zcg.json','w'),ensure_ascii=False,indent=0)
# CSV export
with open('zcap-zcg-grants.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(["ZCAP member","Handle","Joined ZCAP","Tier","Project","Grantee org","Role / evidence","Proposal link","First payment / date","Status"])
    for r in out:
        if r['grants']:
            for g in r['grants']: w.writerow([r['name'],r['handle'],r['joined'],r['tier'],g['project'],g['org'],g['role'],g['link'],g['date'],g['status']])
        else: w.writerow([r['name'],r['handle'],r['joined'],r['tier'] or "Not matched","","","","","",""])
from collections import Counter
print(Counter(r['tier'] for r in out))
