import csv,json,html
exec(open('scripts/matches.py').read())
TIER={}  # name -> tier code
A="Direct grantee"; B="Named grant team member"; C="Org member (indirect)"; D="Approved, $0 paid"; Z="ZF / ECC (excluded by rule)"
for n in ["1337bytes (on the forum)","Andre Froes","Anton Livaja","Batuhanyldrm","Chidi","dismad (on the forum)","Dre ","Elzz","Emersonian (on the forum)","Hanh (on the forum)","Jonathan Rouach","Kenbak ","Kit Sturgeon (mrkit2u on the forum)","Michae2xl (on the forum)","readymouse","ogasky (on the forum)","Olli Tiainen","Pacu","Paul Brigner","Rene Vergara (pitmutt on the forum)","Ryan Taylor","Taylor Hornby","Tm3k (on the forum)","Vivek Arte","Yoditar (on the forum)","zancas (on the forum)","ZArabia (on the forum)","zksquirrel","Cosmo Guerini","fabacab ","Eric Tu","Pablo K","Michael Harms ","DecentralistDan (on the forum)","Mark Henderson","Maximilian Roszko ","Nick Mathewson","Natasha Mynhier ","David Boyer","Skylar Saveland ","gottabeJay (on the forum)","Peacemonger (on the forum)","Harry Halpin ","Roosevelt Gordones"]: TIER[n]=A
for n in ["Hardaeborla","Aescobar Michael","Arlo Byrne (idky137 on the forum)","Aura Brito (AuraBritoSM on the forum)","Constance Beguier","Dorian","Edickson González (Edicksonjga on the forum)","emmalexo","E-zec on the forum","Cjfrankie","Iogy (on the forum)","J.W. Verret","James Katz","Julian Abraham","Kroy","Minevg (on the forum)","Robmarn (on the forum)","Tron","vito (on the forum)","fireice_uk (on the forum)","Eran Tromer ","Jonathan Bird (birdify on the forum)","Juan Carlos Carmona Calvo (Juanky on the forum)","tokidoki (on the forum)","Samaraanni (on the forum)","Bryan Gillespie","Tecnopapapi (on the forum)","Max Hampshire"]: TIER[n]=B
for n in ["Palmar ","AidenZ (on the forum)","artkor (on the forum)","LaDale Terrell (Lowo88 on forum)","Zerodartz (on the forum)","Jason McGee (aquietinvestor on the forum)","Tim  ","Olek (on the forum)"]: TIER[n]=C
TIER["Maxime Desalle"]=D; TIER["Lai Ying Tong"]=D
ZFECC={"Alex Bornstein","Alfredo Garcia ","Amber O'Hearn ","Arya Solhi","Conrado Gouvea","Daira Hopwood ","Danika Delano","DC ","DecentralistDan (on the forum)","Elise Hamdon","Jack Gavigan ","Jack Grigg ","Josh Swihart ","Kris Nuttycombe","Marek","Paige (on the forum)","Pili Guerra","Sean Bowe","Teor","Zooko Wilcox","Autotunafish (on the forum)"}
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
