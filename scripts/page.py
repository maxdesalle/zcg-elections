import json
data=json.load(open('data/zcap_zcg.json'))
from collections import Counter
c=Counter(r['tier'] for r in data)
recip=sum(v for k,v in c.items() if k in ("Direct grantee","Named grant team member"))
tpl=open('scripts/template.html').read()
html=tpl.replace('__DATA__',json.dumps(data,ensure_ascii=False)).replace('__N__',str(len(data))).replace('__RECIP__',str(recip)).replace('__ZF__',str(c["ZF / ECC (excluded by rule)"])).replace('__UNPAID__',str(c["Approved, $0 paid"])).replace('__DIRECT__',str(c["Direct grantee"])).replace('__TEAM__',str(c["Named grant team member"]))
open('zcap-zcg.html','w').write(html); print(len(html))
