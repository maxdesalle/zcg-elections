"""Dollars raised by ZCAP members through grants that began AFTER they joined ZCAP.
A grant counts if its first payment month is strictly after the member's ZCAP join month.
Each member is credited with the whole grant they were named on (so org totals overlap across
members); the unique total dedups grants. Run: python3 scripts/after_join.py"""
import csv,re,json
from datetime import date
MON={m:i+1 for i,m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
def month(s):
    m=re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w* (\d{4})',s)
    return date(int(m.group(2)),MON[m.group(1)[:3]],1) if m else None
def joined(s):
    if "Before" in s: return date(2021,4,1)
    m=re.search(r'(\w+) (\d{4})',s); return date(int(m.group(2)),MON[m.group(1)[:3]],1)
# ledger -> {(project,grantee): [approved, paid, first_paid]}
L={}
for r in list(csv.reader(open('data/grants.csv')))[1:]:
    if len(r)<12: continue
    k=(r[0].strip(),r[1].strip()); amt=float(re.sub(r'[^\d.\-]','',r[5]) or 0) if r[5].strip() else 0
    e=L.setdefault(k,[0,0,None]); e[0]+=amt
    if r[7].strip():
        e[1]+=amt
        if e[2] is None: e[2]=month(r[7])
# member -> [(grantee regex, project regex)]  (grants the member is named on; see scripts/matches.py)
ESP=r"^Zcash Global en Espa"; NIG=r"^Zcash Nigeria"; BRA=r"^Zcash (Global <> Zcash )?Brazil"; QED25=r"ZSAs in NU7|OrchardZSA|Feature Branch"
MAP={
 "1337bytes (on the forum)":[("1337bytes",".")],
 "Aescobar Michael":[("Rhea Finance","."),("Noir Wallet",".")],
 "AAmandita":[("Zcash Brazil",r"Global <> Zcash Brazil|Zcash Brazil 2026")],
 "Arlo Byrne (idky137 on the forum)":[("Zingo Labs","Zaino")],
 "Aura Brito (AuraBritoSM on the forum)":[("Zcash Español",ESP),("ZK AV Club",".")],
 "Batuhanyldrm":[("^Batuhan$",".")],
 "Chidi":[("Zcash Nigeria",".")],
 "Cjfrankie":[("Zcash Nigeria",".")],
 "Constance Beguier":[("QEDIT",QED25)],
 "Cosmo Guerini":[("readymouse","ETHDenver|ETHCC|Berlin|DWeb")],
 "David Boyer":[("Zcash Media","Short Documentary|Launch Plan|Zcash Media 2023")],
 "dismad (on the forum)":[("ZecHub",".")],
 "Dorian":[("Zingo Labs","Zaino Completion|Respecification|Zallet|Stabilization")],
 "Dre ":[("^Zcash Onboarding$",".")],
 "Edickson González (Edicksonjga on the forum)":[("Zcash Español",ESP)],
 "Elzz":[("Zcash Ecosystem Onboarding",".")],
 "Emersonian (on the forum)":[("Emersonian",".")],
 "emmalexo":[("Zcash Nigeria",r"v\.2\.0|August|November|2026")],
 "Eric Tu":[("ChainSafe","^Chainsafe Systems$")],
 "E-zec on the forum":[("Zcash Brazil",".")],
 "fabacab ":[("readymouse",".")],
 "gottabeJay (on the forum)":[("JRGB",".")],
 "Hanh (on the forum)":[("^Hanh$",".")],
 "Hardaeborla":[("Zcash Nigeria",".")],
 "Harry Halpin ":[("Nym",".")],
 "Iogy (on the forum)":[("Zcash Brazil",".")],
 "J.W. Verret":[("Pretty Good Policy for Zcash",".")],
 "James Katz":[("Zcash Brazil",r"Global <> Zcash Brazil|Zcash Brazil \| 2025")],
 "Jonathan Bird (birdify on the forum)":[("Free2Z",".")],
 "Jonathan Rouach":[("QEDIT",QED25+"|Legal Compliance Activities \\(2025\\)")],
 "Juan Carlos Carmona Calvo (Juanky on the forum)":[("Zingo Labs","Implement Orchard|Authentic Financial")],
 "Julian Abraham":[("ZcashMe",".")],
 "Kenbak ":[("CipherScan","."),("Atmosphere Labs",".")],
 "Kit Sturgeon (mrkit2u on the forum)":[("RedDev",".")],
 "Kroy":[("ZecHub","ZecHub 2026")],
 "Mark Henderson":[("Equilibrium","Ziggurat|^ZCash UniFFI Library$")],
 "Max Hampshire":[("Nym",".")],
 "Michae2xl (on the forum)":[("Zcash Brazil",".")],
 "Michael Harms ":[("ZecPages",".")],
 "Minevg (on the forum)":[("Zcash Brazil",".")],
 "Natasha Mynhier ":[("Zcash Media",".")],
 "Nick Mathewson":[("^Tor$","pure-Rust")],   # Arti II was approved Sep 2022, a year before he joined ZCAP; excluded by hand
 "ogasky (on the forum)":[("ZcashGH",".")],
 "Olli Tiainen":[("Equilibrium","ZEC-NAM")],
 "Pablo K":[("QEDIT",QED25)],
 "Pacu":[("^Pacu$",".")],
 "Paul Brigner":[("PGP for Crypto","."),("Pretty Good Policy for Zcash",".")],
 "Peacemonger (on the forum)":[("Tatyana",".")],
 "readymouse":[("readymouse",".")],
 "Rene Vergara (pitmutt on the forum)":[("Vergara",".")],
 "Robmarn (on the forum)":[("Zcash Español",ESP),("ZK AV Club",".")],
 "Rodrigo Schönell":[("Zcash Brazil","Zcash Brazil 2026")],
 "Roosevelt Gordones":[("Zcash Español","."),("ZK AV Club",".")],
 "Ryan Taylor":[("ZK AV Club",".")],
 "Samaraanni (on the forum)":[("Zcash Brazil","Zcash Brazil 2023|Global <> Zcash Brazil")],
 "Skylar Saveland ":[("Free2Z",".")],
 "Taylor Hornby":[("Taylor Hornby",".")],
 "Tecnopapapi (on the forum)":[("ZecHub","An open source education hub")],
 "Tm3k (on the forum)":[("Tmek","."),("tm3k",".")],
 "tokidoki (on the forum)":[("ZecHub","^ZecHub$")],
 "Tron":[("ZecHub","ZecHub 2026")],
 "Vivek Arte":[("QEDIT",QED25+"|Legal Compliance|Asset Swaps|User-Control")],
 "vito (on the forum)":[("Zcash Brazil","Zcash Brazil 2023|Global <> Zcash Brazil"),("ZecHub","ZecHub 202[56]")],
 "Yoditar (on the forum)":[("Zcash Español",ESP)],
 "zancas (on the forum)":[("^Zingo Labs$",".")],
 "ZArabia (on the forum)":[("ZcashArabia",".")],
 "zksquirrel":[("Jason Rogers","."),("ZecHub",".")],
 "DecentralistDan (on the forum)":[("ZcashZeal",".")],"fireice_uk (on the forum)":[("Zypher",".")],
 "Maximilian Roszko ":[("RenZec",".")],"Andre Froes":[("Weever",".")],"Anton Livaja":[("Distrust",".")],
}
EXTRA={"Kit Sturgeon (mrkit2u on the forum)":("red·bridge Launch (approved Jun 2026, not yet in ledger)",477658,date(2026,6,1))}
zc={r[0]:r[2] for r in list(csv.reader(open('data/zcap.csv')))[1:]}
rows=[];uniq={}
for m,pats in MAP.items():
    j=joined(zc[m]); got=[]
    for (p,g),(a,pd_,first) in L.items():
        if any(re.search(gp,g) and re.search(pp,p) for gp,pp in pats) and first and first>j: got.append((p,a,pd_,first))
    if m in EXTRA and EXTRA[m][2]>j: got.append((EXTRA[m][0],EXTRA[m][1],0,EXTRA[m][2]))
    if got:
        rows.append((m.strip(),zc[m],len(got),sum(x[1] for x in got),sum(x[2] for x in got),got))
        for p,a,pd_,f in got: uniq[p]=(a,pd_)
rows.sort(key=lambda x:-x[3])
print(f"members with a grant after joining ZCAP: {len(rows)}")
print(f"unique grants: {len(uniq)}  approved ${sum(a for a,_ in uniq.values()):,.0f}  paid to date ${sum(p for _,p in uniq.values()):,.0f}")
print(f"sum of per-member attributed totals (overlapping): ${sum(r[3] for r in rows):,.0f}")
for m,j,n,a,pd_,got in rows: print(f"{a:>12,.0f}  {pd_:>12,.0f}  {n:>2}  {m} (joined {j})")
json.dump([dict(member=m,joined=j,grants=[dict(project=p,approved=a,paid=pd_,first=f.strftime('%b %Y')) for p,a,pd_,f in got]) for m,j,n,a,pd_,got in rows],open('data/after_join.json','w'),indent=1,ensure_ascii=False)
