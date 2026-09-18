# ZCAP member -> list of (project, grantee/org, role/evidence, link, first paid / date, status)
GH="https://github.com/ZcashCommunityGrants/zcashcommunitygrants/issues/"
M={}
def add(name,*grants):
    M.setdefault(name,[]).extend(grants)

# ---- direct grantees / named paid team members (GitHub era, verified in issue bodies) ----
add("1337bytes (on the forum)",
 ("Upgrade BTCPayServer Zcash Plugin for 2.1","1337bytes","Grantee (GitHub @macintoshhelper)",GH+"35","May 2025","Completed"),
 ("BTCPayServer Multi-Account and 0conf Mempool Support","1337bytes","Grantee",GH+"269","May 2026","Completed"),
 ("BTCPayServer Multi-Store GraphQL Client","1337bytes","Grantee",GH+"395","Aug 2026 (approved, not yet paid)","Open"))
add("Hardaeborla",
 ("Zcash Nigeria 2025 / v2.0 / Aug-Oct / Nov-Dec / 2026","Zcash Nigeria","Named team member, $600/month",GH+"14",'Feb 2025',"Completed/Open"))
add("Aescobar Michael",
 ("Rhea Zcash Gateway","Rhea Finance","Named team member (Operational Lead)",GH+"239","Apr 2026","Completed"),
 ("Zcash WalletConnect Integration","Noir Wallet","Named team member (Operational Lead)",GH+"391","Sep 2026","Open"))
add("Andre Froes",("Zcash Network School","Weever / Zcash.me","Grantee / project lead",GH+"266","Apr 2026","Completed"))
add("Anton Livaja",("Bootstrapped and deterministic builds a la StageX","Distrust.co","Grantee / project lead (co-founder Distrust)",GH+"128","Dec 2025","Open"))
add("Arlo Byrne (idky137 on the forum)",("Zaino grants (Build Zaino, Completion, Respecification, Zallet Release, Release Stabilization)","Zingo Labs","Zingo Labs engineer (forum title 'Zingo Labs'; #1 Zaino contributor)",GH+"16","Oct 2024","Completed"))
add("Aura Brito (AuraBritoSM on the forum)",
 ("Zcash Global en Español 2025 / 2026","Zcash Español","Named team member, $1200/month",GH+"10","Feb 2025","Completed/Open"),
 ("Zk Av Club Community Support 2025 / 2026","ZK AV Club","Named team member",GH+"11","Feb 2025","Completed/Open"))
add("Batuhanyldrm",("Zcash Global Turkish 2025, Q2, Q3-4; Zcash Türkiye 2026 Q1-2, ZBase, Istanbul BW, RLAY HUB, 2026 Q3-4→2027","Batuhan / Zcash Türkiye","Grantee",GH+"7","Jan 2025","Completed/Open"))
add("Chidi",("Zcash Nigeria 2025 / v2.0 / Aug-Oct / Nov-Dec / 2026","Zcash Nigeria","Grantee / lead (lisa001)",GH+"14","Feb 2025","Completed/Open"))
add("Constance Beguier",("Zebra ZSA Integration; ZSAs in NU7 H2 2025; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Named team member (Cryptography)",GH+"6","Jan 2025","Completed/Open"))
add("Cosmo Guerini",("Marketing at ETHCC + Exxxotica; Berlin Blockchain Week; DWeb Camp","Zcash Grassroots Marketing Team (readymouse)","Application co-owner (@cosmojg)",GH+"229","Mar 2026","Completed"))
add("dismad (on the forum)",("ZecHub 2025; ZecHub 2026","ZecHub","Core team, grantee",GH+"9","Jan 2025","Completed/Open"))
add("Dorian",("Zaino grants","Zingo Labs","Zingo Labs engineer (GitHub company @zingolabs; public org member; 278 Zaino commits)",GH+"16","Oct 2024","Completed"))
add("Dre ",("Zcash Onboarding @ Web3Lagos Conference 2026","Zcash Developer Onboarding","Grantee / project lead (Drekal; forum thread posted by Dre_Nesthub)",GH+"349","Jul 2026","Completed"))
add("Edickson González (Edicksonjga on the forum)",("Zcash Global en Español 2025 / 2026","Zcash Español","Named team member",GH+"10","Feb 2025","Completed/Open"))
add("Elzz",("Zcash Ecosystem Onboarding At Women in DeFi Summit 2026","Zcash Ecosystem Onboarding","Grantee",GH+"247","Apr 2026","Completed"))
add("Emersonian (on the forum)",("Zcash Lightwalletd Infrastructure Development and Maintenance","Emersonian & Zancas","Grantee","https://forum.zcashcommunity.com/t/rfp-zcash-lightwalletd-infrastructure-development-and-maintenance/47080","Apr 2024","Completed"))
add("emmalexo",("Zcash Nigeria 2025 v2.0 / Aug-Oct / Nov-Dec / 2026","Zcash Nigeria","Named team member, $600/month",GH+"40","Jun 2025","Completed/Open"))
add("Eric Tu",("Chainsafe Systems (WebZjs continuation)","ChainSafe","Project lead (Principal Research Engineer)",GH+"2","Aug 2025","Completed"))
add("E-zec on the forum",("Zcash Brazil 2025 / 2026","Zcash Brazil","Named core team (Head & growth)",GH+"8","Jan 2025","Completed/Open"))
add("fabacab ",("ETHDenver; ETHCC; Berlin BW; DWeb Camp; ZECsy Amsterdam; ZECsy 12 Months","ZECsy / Zcash Grassroots Marketing Team","Application co-owner, lead educator",GH+"193","Jan 2026","Completed/Open"))
add("Cjfrankie",("Zcash Nigeria 2025 / v2.0 / Aug-Oct / Nov-Dec / 2026","Zcash Nigeria","Named team member, $600/month",GH+"14","Feb 2025","Completed/Open"))
add("Hanh (on the forum)",("Zcash Infra 1 year; BTCPayServer Orchard+UA; Coin Voting maintenance; zaino Stability (GitHub era) + Cold Wallet, YWallet, Ledger, Maya DEX, Coin Voting 2.0 etc. (2021-2025)","Hanh","Grantee (many grants)",GH+"5","Mar 2021","Completed/Open"))
add("Iogy (on the forum)",("Zcash Brazil 2025 / 2026","Zcash Brazil","Named core team (Design)",GH+"8","Jan 2025","Completed/Open"))
add("J.W. Verret",("Pretty Good Policy for Zcash","Pretty Good Policy for Zcash","Named team member (Board Director)",GH+"396","Sep 2026","Open"))
add("James Katz",("Zcash Brazil 2025 / 2026","Zcash Brazil","Named core team (Dev)",GH+"8","Jan 2025","Completed/Open"))
add("Jonathan Rouach",("Zebra ZSA Integration; ZSAs in NU7; Legal Compliance 2025; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Grantee / application owner (@jonmrjr)",GH+"6","Jan 2025","Completed/Open"))
add("Julian Abraham",("Zcash Name Service","ZcashMe, Inc","Named team member (Protocol Engineer, Lead Engineer at ZcashMe)",GH+"298","approved May 2026 (no payout in sheet yet)","Open"))
add("Kenbak ",("CipherScan","CipherScan","Grantee",GH+"179","Feb 2026","Open"),("Zcash Integration for the Open Wallet Standard (OWS)","Atmosphere Labs","Grantee",GH+"255","Apr 2026","Completed"))
add("Kit Sturgeon (mrkit2u on the forum)",("red·bridge Launch","RED.DEV INC","Grantee / project lead (@kitpub)",GH+"335","approved Jun 2026; label 'Startup Payment Completed' (not yet in the sheet)","Open"))
add("Kroy",("ZecHub 2026","ZecHub","Named core team (@theKroy), $53,760",GH+"153","Jan 2026","Open"))
add("Maxime Desalle",("Mastering Zcash Video Series","maxdesalle","Approved then cancelled; $0 paid",GH+"263","Apr 2026","Cancelled, $0 paid"))
add("Michae2xl (on the forum)",("Zcash Brazil 2023, 2024 (x4), 2025, 2026","Zcash Brazil","Grantee / lead",GH+"8","Jan 2023","Completed/Open"),("Zcash Network School","Weever / Zcash.me","Named team member",GH+"266","Apr 2026","Completed"))
add("Minevg (on the forum)",("Zcash Brazil 2025 / 2026","Zcash Brazil","Named core team (Design)",GH+"8","Jan 2025","Completed/Open"))
add("readymouse",("ETHDenver; ETHCC; Berlin BW; DWeb Camp; ZECsy Amsterdam; ZECsy 12 Months","readymouse / ZECsy","Grantee",GH+"193","Jan 2026","Completed/Open"))
add("ogasky (on the forum)",("Zcash Ghana Apr-Jun 2026; Jul-Sep 2026","ZcashGH","Grantee",GH+"252","May 2026","Completed"))
add("Olli Tiainen",("ZEC-NAM shielded airdrop protocol","Eiger / Equilibrium Group","Grantee / application owner",GH+"116","Jan 2026","Completed"))
add("Pablo K",("Zebra ZSA Integration; ZSAs in NU7; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Project lead (Pablo Kogan, Director of Engineering)",GH+"6","Jan 2025","Completed/Open"))
add("Pacu",("Zcash Developer Relations Engineer (2025) + Zcash Wallet Community Developer 2023, 2024, 2024 Q2","Pacu","Grantee",GH+"18","Aug 2023","Completed"))
add("Paul Brigner",("PGP* for Crypto Events; Cypherpunk Policy Dinner","PGP for Crypto, LLC","Grantee",GH+"65","Sep 2025","Completed"),("Pretty Good Policy for Zcash","Pretty Good Policy for Zcash","Named team member",GH+"396","Sep 2026","Open"))
add("Rene Vergara (pitmutt on the forum)",("ZGo 2025 (Retroactive) + ZGo 2022, ZGo Support 2024, Zenith Full Node Wallet","Vergara Technologies","Grantee",GH+"137","Jun 2022","Completed"))
add("Robmarn (on the forum)",("Zcash Global en Español 2025 / 2026","Zcash Español","Named team member",GH+"10","Feb 2025","Completed/Open"),("Zk Av Club 2025 / 2026","ZK AV Club","Named team member",GH+"11","Feb 2025","Completed/Open"))
add("Roosevelt Gordones",("Zcash Global en Español 2025 / 2026","Zcash Español","Named team member, $1200/month",GH+"10","Feb 2025","Completed/Open"),("Zk Av Club 2025 / 2026","ZK AV Club","Named team member",GH+"11","Feb 2025","Completed/Open"))
add("Ryan Taylor",("Zk Av Club Community Support 2025; Zcash Community Media Infrastructure 2026","ZK AV Club","Grantee / project lead",GH+"11","Feb 2025","Completed/Open"))
add("Taylor Hornby",("Zcash Ecosystem Security Lead","Taylor Hornby","Grantee","https://forum.zcashcommunity.com/t/zcash-ecosystem-security-lead/42090","Nov 2022","Completed"))
add("Tm3k (on the forum)",("Twitter Ambassador Program by @_tm3k","tm3k","Grantee",GH+"74","2025","Completed"),("Proposal to fund zcash skydives!","Tmek","Grantee","https://forum.zcashcommunity.com/t/proposal-to-fund-zcash-skydives/40447","Nov 2021","Completed"))
add("Tron",("ZecHub 2026","ZecHub","Named core team (@tron / onajifortune), $53,760",GH+"153","Jan 2026","Open"))
add("vito (on the forum)",("ZecHub 2025; ZecHub 2026","ZecHub","Named core team, $61,440 / $69,120",GH+"9","Jan 2025","Completed/Open"))
add("Vivek Arte",("Zebra ZSA Integration; ZSAs in NU7; Legal Compliance 2025; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Grantee / application owner (@vivek-arte)",GH+"6","Jan 2025","Completed/Open"))
add("Yoditar (on the forum)",("Zcash Global en Español 2025 / 2026 + Generation Z camp (2024), Zcash Global en Español (2024)","Zcash Español","Grantee / lead",GH+"10","Aug 2024","Completed/Open"))
add("zancas (on the forum)",("Zaino grants; Sofia/Prague collaboration; Hackfest + Zingo Labs 2022-2023 grants; Lightwalletd Infra (with Emersonian)","Zingo Labs","Grantee / lead",GH+"16","Nov 2022","Completed/Open"))
add("ZArabia (on the forum)",("ZcashArabia Q1 2026; May-Sep 2026; Aug-Dec 2026","ZcashArabia","Grantee (org account; GitHub @Cryptoblarabi)",GH+"160","Mar 2026","Completed/Open"))
add("zksquirrel",("ZecHub 2025; ZecHub 2026","ZecHub","Core team, grantee",GH+"9","Jan 2025","Completed/Open"))

# ---- pre-GitHub (2021-2024) matches, from forum threads / archived ZF Grants pages ----
F="https://forum.zcashcommunity.com/t/"
add("Michael Harms ",("1 year of ZECpages servers; ZECpages Testnet Faucet","ZecPages","Grantee (ZECpages creator, forum BrunchTime)",F+"1-year-of-zecpages-servers/38823","Mar 2021","Completed"))
add("DecentralistDan (on the forum)",("ZcashZeal","ZcashZeal","Grantee (applicant decentralistdan / Dan Wolande); milestone 1 paid, then cancelled. Now ZF staff, but this grant predates that",F+"zcashzeal-multi-media-community-content-hub/38483","Feb 2021","Cancelled after milestone 1"))
add("Mark Henderson",("Ziggurat 1.0 / 2.0 / 3.0; Zcash UniFFI Library","Equilibrium","Applicant / project lead ('Mark here from Equilibrium', VP Engineering)",F+"ziggurat-the-zcash-network-stability-framework/38758","Mar 2021","Completed"))
add("Maximilian Roszko ",("Bootstrapping liquidity for renZEC on Binance Smart Chain","Ren (RenZec)","Applicant on behalf of the Ren team (forum MaximilianR)",F+"bootstrapping-liquidity-for-renzec-on-binance-smart-chain/38849","Apr 2021","Completed"))
add("fireice_uk (on the forum)",("A Metamask-style browser extension for Zcash (Zephyr)","Zypher","Named team member ('Fireice is a freelance C++ developer'); milestone 1 ($30k) paid, rest cancelled",F+"zephyr-a-metamask-style-browser-extension-for-zcash/39112","May 2021","Cancelled after milestone 1"))
add("Nick Mathewson",("Arti: a pure-Rust Tor implementation (2021); Arti onion services and beyond (2022-2024)","Tor Project","Applicant ('I'm Nick Mathewson, one of the co-founders of Tor')",F+"arti-a-pure-rust-tor-implementation-for-zcash-and-beyond/38776","Jun 2021","Completed"))
add("Natasha Mynhier ",("Zcash Short Documentary; Ceremony/Powers of Tau/Halo video; Zcash Media Launch Plan; Zcash Media 2023","Zcash Media (37 Laines)","Director / Producer; 37 Laines 'run by Natasha Mynhier and Jeff Hammerton'",F+"zcash-mini-documentary-educational-series/39667","Aug 2021","Completed / 2023 cancelled"))
add("David Boyer",("Zcash Short Documentary; Zcash Media Launch Plan; Zcash Media 2023","Zcash Media (37 Laines)","Applicant / Producer-Writer (forum David_Heisenberg; ZF Grants team box 'David Boyer')",F+"zcash-media-launch-plan/41138","Aug 2021","Completed / 2023 cancelled"))
add("1337bytes (on the forum)",("Elemental ZEC – Zcash UI Component Kit and Payment Processor","Elemental ZEC","Grantee",F+"elemental-zec-ui-component-kit-and-payment-processor/40110","Dec 2021","Completed"))
add("Eran Tromer ",
 ("Oblivious Message Retrieval","Columbia University","Co-proposer with Zeyu Liu; $22k paid then fully returned",F+"oblivious-message-retrieval/40715","Jan 2022","Cancelled, funds returned"),
 ("Zcash Shielded Assets - Asset Swaps and Beyond","QEDIT","Named QEDIT team member ('includes Pablo Kogan, Alexey Koren, Constance Beguier, Eran Tromer, ...')",F+"zcash-shielded-assets-asset-swaps-and-beyond/44497","May 2023","Completed"))
add("Skylar Saveland ",("Free2Z (legal expenses; Free2Z; Preparing the Garden for Spring)","Free2Z (2Z Inc)","Grantee, CEO/co-founder",F+"free2-whats-your/41289","May 2022","Completed"))
add("Jonathan Bird (birdify on the forum)",("Free2Z (legal expenses; Free2Z; Preparing the Garden for Spring)","Free2Z (2Z Inc)","Co-founder / CFO ('founded by Skylar Saveland (CEO) and Jonathan Bird (CFO)')",F+"free2-whats-your/41289","May 2022","Completed"))
add("gottabeJay (on the forum)",("Telegram Anti Scam Bot - Grant Request","JRGB (Zcash Telegram admins)","Applicant (thread author, $700 retroactive grant)",F+"zcash-anti-scam-telegram-bot-grant/42845","May 2023","Completed"))
add("Juan Carlos Carmona Calvo (Juanky on the forum)",("Implement Orchard Funded Amendment; Authentic Financial Insight (Zingo! Onward)","Zingo Labs","Named team member ('Za, Juanky, Gygaxis'; juanky@zingolabs.org; forum title 'Zingo Labs')",F+"implement-orchard/42706","Nov 2022","Completed"))
add("tokidoki (on the forum)",("ZecHub (first grant, 2023)","ZecHub","Named applicant / team member ('Applicant Names: Jason Rogers, Dismad, Tokidoki')",F+"zechub-open-source-education-for-zcash/43761","Mar 2023","Completed"))
add("Samaraanni (on the forum)",("Zcash Brazil 2023; Zcash Global <> Zcash Brazil 2024 (Q1-Q4)","Zcash Brazil","Named team member (Samara, PR)",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"))
add("Kit Sturgeon (mrkit2u on the forum)",("Zcash-Avalanche Elastic Subnet Bridge","red·dev (RedDev)","Applicant (forum mrkit2u)",F+"zcash-elastic-subnet-bridge-on-avalanche/44220","May 2023","Open"))
add("Bryan Gillespie",("Crypto Lounge Experience and The Hunting of The Snark","Inversed Tech","Co-founder / Chief Security Officer of Inversed Tech; forum bgillespie: 'Collaborators on the project are @LeCryptoMath and myself from Inversed Tech'",F+"proposal-the-crypto-lounge-experience-event-in-barcelona/44729","Jul 2023","Completed"))
add("Peacemonger (on the forum)",("Zcash User Research & Engagement (ZURE), Phase 1","Tatyana","Grantee (forum peacemonger = Tatyana, ex-ECC), $35,000",F+"zcash-user-research-engagement-zure-phase-1/45820","Jan 2024","Completed"))
add("Tecnopapapi (on the forum)",("ZecHub: Proposal 2024","ZecHub","Named core team member (dismad, squirrel, Tecnopapapi)",F+"zechub-proposal-2024/46077","Jan 2024","Completed"))
add("Harry Halpin ",("The Nym mixnet for Network Privacy for Zcash","Nym Technologies","Applicant (thread author, Nym CEO)",F+"the-nym-mixnet-for-network-privacy-for-zcash/46324","Oct 2024","Open"))
add("Max Hampshire",("The Nym mixnet for Network Privacy for Zcash","Nym Technologies","Nym team; posts grant updates as maxnym",F+"revised-nym-for-zcash-network-level-privacy/46688","Oct 2024","Open"))
add("Roosevelt Gordones",("Generation Z - Educational camp for youth","Zcash Español (gordonesTV)","Grantee (applied personally), $3,500",F+"generation-z-grant-proposal/48434","Aug 2024","Completed"))
add("Lai Ying Tong",("halo2 Community Manager","Ying Tong","Approved Feb 2023, retroactively withdrawn Jan 2024; $0 paid",F+"halo2-community-manager/43795","Feb 2023","Cancelled, $0 paid"))
add("dismad (on the forum)",("ZecHub 2023; ZecHub 2024; ZecHub 2024 continued","ZecHub","Core team / applicant",F+"zechub-proposal-2024/46077","Mar 2023","Completed"))
add("zksquirrel",("Community Note Taker (2022); ZecHub 2023 / 2024","ZecHub / Jason Rogers","Grantee (Jason Rogers = zksquirrel)",F+"rfp-community-note-taker/41656","Jul 2022","Completed"))
add("vito (on the forum)",("Zcash Brazil 2023; Zcash Global <> Zcash Brazil 2024","Zcash Brazil","Named team member (Vito, PR / community)",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"))
add("Minevg (on the forum)",("Zcash Brazil 2023; Zcash Global <> Zcash Brazil 2024","Zcash Brazil","Named team member (Mine, design)",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"))
add("Iogy (on the forum)",("Zcash Brazil 2023; Zcash Global <> Zcash Brazil 2024","Zcash Brazil","Named team member (design)",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"))
add("E-zec on the forum",("Zcash Brazil 2023; Zcash Global <> Zcash Brazil 2024","Zcash Brazil","Named team member (moderator)",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"))
add("James Katz",("Zcash Global <> Zcash Brazil 2024","Zcash Brazil","Named team member (Dev)",F+"zcash-global-zcash-brazil/46295","Jan 2024","Completed"))
add("Yoditar (on the forum)",("Zcash Global en Español (2024) and Q4 2024","Zcash Español","Grantee / lead",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"))
for n in ["Aura Brito (AuraBritoSM on the forum)","Edickson González (Edicksonjga on the forum)","Robmarn (on the forum)","Roosevelt Gordones"]:
    add(n,("Zcash Global en Español Q4 2024","Zcash Español","Named team member ('The Zcash en Español team consists of 5 members')",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"))
add("Arlo Byrne (idky137 on the forum)",("Build Zaino To Deprecate Zcashd (2024 proposal)","Zingo Labs","Named in proposal: 'In collaboration with @idky137 and @AloeareV internally'",F+"zingo-labs-accelerates-zcashd-deprecation-with-zaino/48545","Oct 2024","Completed"))
add("Olli Tiainen",("Ziggurat 1.0-3.0; Zcash UniFFI Library (2021-2023)","Equilibrium","Equilibrium co-founder (org that received the grants; applicant was Mark Henderson)",F+"ziggurat-the-zcash-network-stability-framework/38758","Mar 2021","Completed"))

# put the strongest evidence first
for n in ["Tecnopapapi (on the forum)","Roosevelt Gordones"]:
    M[n].sort(key=lambda g: 0 if ("core team" in g[2] or "Grantee" in g[2]) else 1)
