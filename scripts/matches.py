# ZCAP member -> grants. Each grant: (project, grantee/org, role + evidence, link, first payment, ledger status).
# Every line was re-verified against the issue body / forum thread / ledger by the Sep 2026 audit (audit/findings).
GH="https://github.com/ZcashCommunityGrants/zcashcommunitygrants/issues/"
F="https://forum.zcashcommunity.com/t/"
M={}
def add(name,*grants): M.setdefault(name,[]).extend(grants)

# ---------------- Direct grantees ----------------
add("1337bytes (on the forum)",
 ("Elemental ZEC – Zcash UI Component Kit and Payment Processor","Elemental ZEC","Grantee (thread author 1337bytes; ZOMG approval 2021-10-13)",F+"elemental-zec-ui-component-kit-and-payment-processor/40110","Dec 2021","Completed"),
 ("Upgrade BTCPayServer Zcash Plugin for 2.1","1337bytes","Grantee (GitHub @macintoshhelper, blog 1337bytes.com; forum 1337bytes links #35)",GH+"35","May 2025","Completed"),
 ("BTCPayServer Multi-Account and 0conf Mempool Support","1337bytes","Grantee",GH+"269","May 2026","Completed"),
 ("BTCPayServer Multi-Store GraphQL Client","1337bytes","Grantee; approved, no payout yet",GH+"395","approved Aug 2026","Open, $0 paid"))
add("Andre Froes",("Zcash Network School","Weever / Zcash.me","Application owner @andr9froes, project lead",GH+"266","Apr 2026","Completed"))
add("Anton Livaja",("Bootstrapped and deterministic builds a la StageX","Distrust.co","Application owner @antonleviathan (GitHub name Anton Livaja), lead 'Co-Founder Distrust.co'",GH+"128","Dec 2025","Open"))
add("Batuhanyldrm",
 ("Zcash Global Turkish 2025","Batuhan","Application owner @BatuhanZcash, lead 'Batuhan' (forum name Batuhan Yıldırım)",GH+"7","Jan 2025","Completed"),
 ("Zcash Global Turkiye Q2; Q3-4","Batuhan","Application owner",GH+"38","May 2025","Completed"),
 ("Zcash Türkiye 2026 Q1-2; ZBase Vision; Istanbul Blockchain Week; RLAY HUB; 2026 Q3-4 → 2027","Batuhan / Zcash Türkiye","Application owner",GH+"163","Jan 2026","Completed/Open"))
add("Chidi",
 ("Zcash Nigeria 2025","Zcash Nigeria","Application owner 'lisa001 (Chidi)', Lead Ambassador; GitHub olisa001 = 'chidi olisa'",GH+"14","Feb 2025","Completed"),
 ("Zcash Nigeria 2025 v2.0; Aug-Oct; Nov-Dec","Zcash Nigeria","Application owner",GH+"40","Jun 2025","Completed"),
 ("Zcash Nigeria 2026","Zcash Nigeria","Application owner ('Lisa001 (Chidi Olisa)')",GH+"150","Mar 2026","Open"))
add("Cosmo Guerini",
 ("Grassroots Marketing at ETHDenver 2026","Zcash Grassroots Marketing Team (readymouse)","Named team member '@cos, Role: Developer Connection' (GitHub cosmojg = Cosmo; cosmo.red = Guerini)",GH+"193","Jan 2026","Completed"),
 ("Marketing at ETHCC + Exxxotica; DWeb Camp","Zcash Grassroots Marketing Team","Application co-owner ('readymouse, cosmojg, fabacab'; #283 'Cosmo (zcash @cos, github @cosmojg)')",GH+"229","Mar 2026","Completed"),
 ("Marketing at Berlin Blockchain Week","Zcash Grassroots Marketing Team","Named team member @cos",GH+"253","Apr 2026","Completed"))
add("David Boyer",
 ("Zcash Short Documentary","Zcash Media (37 Laines)","'David Boyer - Project organizer, Writer' (thread by 37L); ZF Grants team box 'David Boyer'",F+"zcash-mini-documentary-educational-series/39667","Aug 2021","Completed"),
 ("Zcash Media Launch Plan; Zcash Media 2023","Zcash Media (37 Laines)","Applicant (forum David_Heisenberg): 'Applicant name: David Boyer, Team member name: 37 Laines'. 2023 grant cancelled after 6 of 9 payouts",F+"zcash-media-launch-plan/41138","Mar 2022","Completed / 2023 cancelled"))
add("DecentralistDan (on the forum)",("ZcashZeal","ZcashZeal","Applicant ('My nym is @decentralistdan'; = Dan Wolande). Milestone 1 $2,754 paid, rest cancelled. Later ZF, now ECC comms; this grant predates both",F+"zcashzeal-multi-media-community-content-hub/38483","Feb 2021","Cancelled after milestone 1"))
add("dismad (on the forum)",
 ("ZecHub (2023)","ZecHub","Named applicant ('Applicant Names: Jason Rogers, Dismad, Tokidoki')",F+"zechub-open-source-education-for-zcash/43761","Mar 2023","Completed"),
 ("ZecHub: Proposal 2024; ZecHub 2024 continued","ZecHub","Named core team ('@Dismad @Squirrel @Tecnopapapi'); applicant of the continuation",F+"zechub-proposal-2024/46077","Jan 2024","Completed"),
 ("ZecHub 2025","ZecHub","Application owner (@Dismad, @zksquirrel, @vitozkp)",GH+"9","Jan 2025","Completed"),
 ("ZecHub 2026","ZecHub","Application owner",GH+"153","Jan 2026","Open"))
add("Dre ",("Zcash Onboarding @ Web3Lagos Conference 2026","Zcash Developer Onboarding","Application owner @drekal0 / 'Drekal'; forum thread by Dre_Nesthub links #349",GH+"349","Jul 2026","Completed"))
add("Elzz",("Zcash Ecosystem Onboarding At Women in DeFi Summit 2026","Zcash Ecosystem Onboarding","Application owner @elzz-ux",GH+"247","Apr 2026","Completed"))
add("Emersonian (on the forum)",("Zcash Lightwalletd Infrastructure Development and Maintenance","Emersonian & Zancas","Applicant ('Our proposal is below', post 2 of the RFP thread); zancas disclaimed any funds",F+"rfp-zcash-lightwalletd-infrastructure-development-and-maintenance/47080","Apr 2024","Completed"))
add("Eric Tu",("Chainsafe Systems (WebZjs continuation)","ChainSafe","Project lead 'Eric Tu, Principal Research Engineer' (GitHub/forum ec2)",GH+"2","Aug 2025","Completed"))
add("fabacab ",
 ("Grassroots Marketing at ETHDenver 2026","Zcash Grassroots Marketing Team","Application co-owner ('@zReadyMouse, @fabacab'), Technical Educator",GH+"193","Jan 2026","Completed"),
 ("ETHCC + Exxxotica; Berlin Blockchain Week; DWeb Camp; ZECsy Team in Amsterdam","ZECsy / Zcash Grassroots Marketing Team","Application co-owner ('Violet @fabacab')",GH+"229","Mar 2026","Completed"),
 ("ZECsy Community Building: 12 Months","ZECsy","Named team member (lead educator); owner is readymouse alone",GH+"402","Sep 2026","Open"))
add("gottabeJay (on the forum)",("Telegram Anti Scam Bot - Grant Request","JRGB (Zcash Community Telegram Admin Group)","Applicant (thread author; 'We are the Admins of the Zcash community Telegram group'); $700 retroactive",F+"zcash-anti-scam-telegram-bot-grant/42845","May 2023","Completed"))
add("Hanh (on the forum)",
 ("Cold Wallet; CoinPayments Integration; Payment Gateway with BTCPay (2021-22)","Hanh","Grantee (hhanh00)",F+"cold-wallet/38664","Mar 2021","Completed"),
 ("YWallet; Orchard and UA for YWallet; Ledger shielded support; YWallet Maintenance (2022-23)","Hanh","Grantee",F+"orchard-and-ua-for-ywallet/43061","Sep 2022","Completed"),
 ("Maya DEX; Coin Voting 2.0 (2024-25)","Hanh","Grantee (Proof of Balance approved but never paid)",F+"transparent-shielded-dex-with-maya-protocol/46857","May 2024","Completed"),
 ("Zcash Infra 1 year; BTCPayServer Orchard+UA; Coin Voting maintenance; zaino Stability (2025-26)","Hanh","Application owner @hhanh00",GH+"5","Feb 2025","Completed/Open"))
add("Harry Halpin ",("The Nym mixnet for Network Privacy for Zcash","Nym Technologies","Applicant (thread author harryhalpin, Nym co-founder); approved Feb 2024 for $150,000",F+"the-nym-mixnet-for-network-privacy-for-zcash/46324","Oct 2024","Open"))
add("Jonathan Rouach",
 ("Zebra ZSA Integration","QEDIT","Named 'Co-Lead, CEO at QEDIT' (owner handle written @jonrouach)",GH+"6","Jan 2025","Completed"),
 ("ZSAs in NU7 H2 2025; Legal Compliance 2025; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Application owner @jonmrjr",GH+"44","Aug 2025","Completed/Open"))
add("Julian Abraham",("Zcash Name Service","ZcashMe, Inc","Application co-owner (GitHub craftsoldier = Julian Abraham) and 'Lead Engineer at ZcashMe'; approved May 2026, no payout yet",GH+"298","approved May 2026","Open, $0 paid"))
add("Kenbak ",("CipherScan","CipherScan","Application owner, Founder & Lead Developer",GH+"179","Feb 2026","Open"),("Zcash Integration for the Open Wallet Standard (OWS)","Atmosphere Labs","Application owner",GH+"255","Apr 2026","Completed"))
add("Kit Sturgeon (mrkit2u on the forum)",
 ("Zcash-Avalanche Elastic Subnet Bridge","red·dev (RedDev)","Applicant (thread author mrkit2u = Kit Sturgeon, 'CEO and founder of red·dev')",F+"zcash-elastic-subnet-bridge-on-avalanche/44220","May 2023","Open"),
 ("red·bridge Launch","RED.DEV INC","Application owner @kitpub (GitHub name Kit Sturgeon, twitter mrkit2u); label 'Startup Payment Completed'; not yet in the ledger",GH+"335","approved Jun 2026","Open (startup paid)"))
add("Mark Henderson",("Ziggurat 1.0 / 2.0 / 3.0; Zcash UniFFI Library","Equilibrium","Applicant (forum shieldedmark = Mark Henderson, VP Engineering; 'Mark here from Equilibrium'); GitHub aphelionz",F+"ziggurat-the-zcash-network-stability-framework/38758","Mar 2021","Completed"))
add("Maximilian Roszko ",("Bootstrapping liquidity for renZEC on Binance Smart Chain","Ren (RenZec)","Applicant for the Ren team (forum MaximilianR = Maximilian Roszko)",F+"bootstrapping-liquidity-for-renzec-on-binance-smart-chain/38849","Apr 2021","Completed"))
add("Michae2xl (on the forum)",
 ("Zcash Brazil 2023","Zcash Brazil","Applicant / ambassador",F+"zcash-brazil-2023-proposal/43499","Jan 2023","Completed"),
 ("Zcash Global <> Zcash Brazil (2024 Q1-Q4)","Zcash Brazil","Applicant",F+"zcash-global-zcash-brazil/46295","Jan 2024","Completed"),
 ("Zcash Brazil 2025","Zcash Brazil","Application owner",GH+"8","Jan 2025","Completed"),
 ("Zcash Brazil 2026","Zcash Brazil","Application owner",GH+"155","Jan 2026","Open"))
add("Michael Harms ",("1 year of ZECpages servers; ZECpages Testnet Faucet","ZecPages","Grantee (forum BrunchTime: 'I, Michael Harms, am a full stack web developer. I first built ZECpages.com')",F+"1-year-of-zecpages-servers/38823","Mar 2021","Completed"))
add("readymouse",
 ("Grassroots Marketing at ETHDenver 2026","readymouse","Application owner @zReadyMouse (Mylo Bennett)",GH+"193","Jan 2026","Completed"),
 ("ETHCC + Exxxotica; Berlin Blockchain Week; DWeb Camp; ZECsy Amsterdam","readymouse / ZECsy","Application owner",GH+"229","Mar 2026","Completed"),
 ("ZECsy Community Building: 12 Months","ZECsy","Application owner",GH+"402","Sep 2026","Open"))
add("Natasha Mynhier ",("Zcash Short Documentary; Ceremony/Powers of Tau/Halo video; Zcash Media Launch Plan; Zcash Media 2023","Zcash Media (37 Laines)","'37 Laines is an award winning film production company run by Natasha Mynhier and Jeff Hammerton'; Director/Producer (posts as 37L)",F+"zcash-mini-documentary-educational-series/39667","Aug 2021","Completed / 2023 cancelled"))
add("Nick Mathewson",
 ("Arti: a pure-Rust Tor implementation for Zcash and beyond","Tor Project","Applicant ('I'm Nick Mathewson, one of the co-founders of Tor')",F+"arti-a-pure-rust-tor-implementation-for-zcash-and-beyond/38776","Jun 2021","Completed"),
 ("Arti: onion services and beyond (Year II)","Tor Project","Authored the Year II plan thread; formal application filed by Tor staff (alsmith)",F+"41387","Mar 2024","Completed"))
add("ogasky (on the forum)",("Zcash Ghana Apr-Jun 2026; Jul-Sep 2026","ZcashGH","Application owner, Team Lead",GH+"252","May 2026","Completed"))
add("Olli Tiainen",("ZEC-NAM shielded airdrop protocol","Eiger (Equilibrium Group)","Application owner @olliten",GH+"116","Jan 2026","Completed"))
add("Pablo K",("Zebra ZSA Integration; ZSAs in NU7; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Project lead 'Pablo Kogan, Director of Engineering at QEDIT' on all four",GH+"6","Jan 2025","Completed/Open"))
add("Pacu",
 ("Zcash Wallet Community Developer 2023; 2024 Q1; 2024 Q2","Pacu","Applicant, solo",F+"zcash-wallet-community-developer/45096","Aug 2023","Completed"),
 ("Developer Relations Engineer","Pacu","Applicant, solo (ledger milestones from Oct 2024; GitHub re-post Feb 2025)",GH+"18","Oct 2024","Completed"))
add("Paul Brigner",
 ("PGP* (Pretty Good Policy) for Crypto Events; Cypherpunk Policy Dinner","PGP for Crypto, LLC","Application owner @paulbrigner, Event Organizer",GH+"65","Sep 2025","Completed"),
 ("Pretty Good Policy for Zcash","Pretty Good Policy for Zcash","Named team member: 'Chairman of the Board of Directors ... Founder of Pretty Good Policy for Zcash' (board compensated per application)",GH+"396","Sep 2026","Open"))
add("Rene Vergara (pitmutt on the forum)",
 ("ZGo - The Zcash Register; ZGo Support 2024; Zenith Full Node Wallet","Vergara Technologies","Applicant (pitmutt; 'father-and-son team ... Rene Vergara Larrea, MSc, PMP')",F+"zgo-the-zcash-register/41885","Jun 2022","Completed"),
 ("ZGo 2025 (Retroactive)","Vergara Technologies","Project lead 'Rene Vergara Larrea, Owner'",GH+"137","Dec 2025","Completed"))
add("Roosevelt Gordones",
 ("Generation Z - Educational camp for youth","Zcash Español (gordonesTV)","Applicant, solo ('camp ... that I run since 2017'); $3,500",F+"generation-z-grant-proposal/48434","Aug 2024","Completed"),
 ("Zcash Global en Español (2024)","Zcash Español","Named team member ('team consists of 5 members: @AuraBritoSM, @gordonesTV, @Edicksonjga, @robmarn, @yoditar')",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"),
 ("Zcash Global en Español 2025; 2026","Zcash Español","Named team member, $1,200/month",GH+"10","Feb 2025","Completed/Open"),
 ("Zk Av Club 2025; Community Media Infrastructure 2026","ZK AV Club","Named team member (Curriculum; Community Workshops Coordinator)",GH+"11","Feb 2025","Completed/Open"))
add("Ryan Taylor",("Zk Av Club Community Support 2025; Zcash Community Media Infrastructure 2026","ZK AV Club","Applicant / project lead (GitHub copernicus-mogley = Ryan Taylor)",GH+"11","Feb 2025","Completed/Open"))
add("Skylar Saveland ",
 ("Free2Z; Free2Z legal expenses","Free2Z (2Z Inc)","Applicant (forum skyl), CEO",F+"free2-whats-your/41289","Jun 2022","Completed"),
 ("Free2Z: Preparing the Garden For Spring","Free2Z (2Z Inc)","Named CEO/co-founder (application filed by birdify)",F+"free2z-preparing-the-garden-for-spring/43979","Mar 2023","Completed"))
add("Peacemonger (on the forum)",("Zcash User Research & Engagement (ZURE), Phase 1","Tatyana","Applicant (forum peacemonger = Tatyana; bio 'ZURE ... ZCG recipient'); $35,000",F+"zcash-user-research-engagement-zure-phase-1/45820","Jan 2024","Completed"))
add("Taylor Hornby",("Zcash Ecosystem Security Lead","Taylor Hornby","Applicant, solo (forum earthrise); ex-ECC",F+"zcash-ecosystem-security-lead/42090","Nov 2022","Completed"))
add("Tm3k (on the forum)",
 ("Proposal to fund zcash skydives!","Tmek","Applicant ('I am @_tm3k on twitter')",F+"proposal-to-fund-zcash-skydives/40447","Nov 2021","Completed"),
 ("Twitter Ambassador Program by @_tm3k","tm3k","Application owner @tm3k",GH+"74","Oct 2025","Completed"))
add("Vivek Arte",("Zebra ZSA Integration; ZSAs in NU7; Legal Compliance 2025; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Application owner / author @vivek-arte on all five",GH+"6","Jan 2025","Completed/Open"))
add("Yoditar (on the forum)",
 ("Zcash Global en Español (2024)","Zcash Español","Applicant",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"),
 ("Zcash Global en Español 2025; 2026","Zcash Español","Application owner @yoditar",GH+"10","Feb 2025","Completed/Open"))
add("zancas (on the forum)",
 ("Implement Orchard Funded Amendment; Zingo! Onward (Authentic Financial Insight)","Zingo Labs","Applicant",F+"implement-orchard/42706","Nov 2022","Completed"),
 ("Build Zaino; Zaino Completion; Respecification; Zallet Release; Release Stabilization; Prague collaboration; Hackfest","Zingo Labs","Application owner @zancas (Za Wil)",GH+"16","Oct 2024","Completed/Open"))
add("ZArabia (on the forum)",("ZcashArabia Q1 2026; May-Sep 2026; Aug-Dec 2026","ZcashArabia","Grantee org account (forum ZArabia links #160; GitHub cryptoblarabi, lead Mostafa)",GH+"160","Mar 2026","Completed/Open"))
add("zksquirrel",
 ("Community Note Taker","Jason Rogers","Grantee ('Jason Rogers (@zksquirrel) will be attending the bi-weekly Arborist calls'; forum squirrel)",F+"rfp-community-note-taker/41656","Jul 2022","Completed"),
 ("ZecHub 2023; 2024; 2024 continued","ZecHub","Named applicant / core team",F+"zechub-open-source-education-for-zcash/43761","Mar 2023","Completed"),
 ("ZecHub 2025; ZecHub 2026","ZecHub","Application owner / project lead",GH+"9","Jan 2025","Completed/Open"))

# ---------------- Named team members / staff of the grantee ----------------
add("AAmandita",
 ("Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Joined the team Apr 2024 per milestone report ('2 new members ... AAmandita_')",F+"46295/33","Apr 2024","Completed"),
 ("Zcash Brazil 2026","Zcash Brazil","Team member per 2026 milestone reports ('@AAmandita: Already an integral part of the team ... interviews, Zebra Talk, Zona Z'); application names no individuals",F+"53702/14","Jan 2026","Open"))
add("Aescobar Michael",
 ("Rhea Zcash Gateway","Rhea Finance","Named team member 'Aescobar, Operational Lead' (forum: 'Aescobar (Michael) | COO of RHEA Finance & Core Contributor of Noir Wallet')",GH+"239","Apr 2026","Completed"),
 ("Zcash WalletConnect Integration","Noir Wallet","Named team member 'Aescobar, Operational Lead'",GH+"391","Sep 2026","Open"))
add("Arlo Byrne (idky137 on the forum)",("Build Zaino; Zaino Completion; Respecification; Zallet Release; Release Stabilization","Zingo Labs","Zingo Labs engineer 2024-25: zancas 'In collaboration with @idky137 and @AloeareV internally'; idky137 posted 'ZingoLabs are pleased to have now released Zaino' (Milestone 1); forum title 'Zingo Labs'; top Zaino contributor. Founded Umbriel Systems ~Mar 2026",F+"zingo-labs-accelerates-zcashd-deprecation-with-zaino/48545","Oct 2024","Completed/Open"))
add("Aura Brito (AuraBritoSM on the forum)",
 ("Zcash Global en Español (2024)","Zcash Español","Named team member (one of 5)",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"),
 ("Zcash Global en Español 2025; 2026","Zcash Español","Named team member, $1,200/month (2026 as SoyAuraBrito, $1,725/month)",GH+"10","Feb 2025","Completed/Open"),
 ("Zk Av Club 2025; Community Media Infrastructure 2026","ZK AV Club","Named team member (Curriculum; Community Workshops Coordinator)",GH+"11","Feb 2025","Completed/Open"))
add("Constance Beguier",("Zebra ZSA Integration; ZSAs in NU7 H2 2025; OrchardZSA finalization; Feature Branch Testnet","QEDIT","Named team member 'Cryptography Research Engineer at QEDIT' on all four",GH+"6","Jan 2025","Completed/Open"))
add("Dorian",("Zaino Completion; Respecification; Zallet Release; Release Stabilization","Zingo Labs","Zingo Labs engineer (GitHub company @zingolabs, public org member; 278 Zaino commits from May 2025); zancas: '@dorianvp, $SomeNym, and @pacu have completed 10 of the MS1 RPCs'",GH+"30","May 2025","Open/Completed"))
add("Edickson González (Edicksonjga on the forum)",
 ("Zcash Global en Español (2024)","Zcash Español","Named team member (one of 5)",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"),
 ("Zcash Global en Español 2025; 2026","Zcash Español","Named team member / application co-owner (#157)",GH+"10","Feb 2025","Completed/Open"))
add("emmalexo",("Zcash Nigeria 2025 v2.0; Aug-Oct; Nov-Dec; 2026","Zcash Nigeria","Named team member, $600/month ('@Emmalexo Emmanuel is currently a member of the zcash team Nigeria'); the Feb 2025 application tagged the same bio as @Emmanuel by mistake",GH+"40","Jun 2025","Completed/Open"))
add("E-zec on the forum",
 ("Zcash Brazil 2023; Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Named team member (moderator)",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"),
 ("Zcash Brazil 2025","Zcash Brazil","Named core team (Head & growth), $84k for two",GH+"8","Jan 2025","Completed"),
 ("Zcash Brazil 2026","Zcash Brazil","Team member per milestone reports ('Community Support - E-zec report'); application names no individuals",F+"53702/14","Jan 2026","Open"))
add("fireice_uk (on the forum)",("A Metamask-style browser extension for Zcash (Zephyr)","Zypher","Named team member ('@fireice_uk and I are also happy to add ... @mistfpga to the team'; ZOMG: 'Congratulations to the whole team @fireice_uk and @mistfpga'). Milestone 1 $30,100 paid, rest cancelled",F+"zephyr-a-metamask-style-browser-extension-for-zcash/39112","May 2021","Cancelled after milestone 1"))
add("Cjfrankie",("Zcash Nigeria 2025; v2.0; Aug-Oct; Nov-Dec; 2026","Zcash Nigeria","Named team member, $600/month on every application (forum name Frank Chukwurah)",GH+"14","Feb 2025","Completed/Open"))
add("Hardaeborla",("Zcash Nigeria 2025; v2.0; Aug-Oct; Nov-Dec; 2026","Zcash Nigeria","Named team member, $600/month on every application",GH+"14","Feb 2025","Completed/Open"))
add("Iogy (on the forum)",
 ("Zcash Brazil 2023; Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Named team member (design), $900/month in 2024 reports",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"),
 ("Zcash Brazil 2025","Zcash Brazil","Named core team (Design), $60k for two",GH+"8","Jan 2025","Completed"),
 ("Zcash Brazil 2026","Zcash Brazil","Team member per milestone reports ('Design Team @iogy & @Minevg'); application names no individuals",F+"53702/14","Jan 2026","Open"))
add("J.W. Verret",("Pretty Good Policy for Zcash","Pretty Good Policy for Zcash","Named team member 'Board Director' (application: board receives 'modest compensation'); also a ZF director",GH+"396","Sep 2026","Open"))
add("James Katz",
 ("Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Named team member (dev), $1,000/month",F+"zcash-global-zcash-brazil/46295","Jan 2024","Completed"),
 ("Zcash Brazil 2025","Zcash Brazil","Named core team (Dev), $45,000",GH+"8","Jan 2025","Completed"),
 ("Zcash Brazil 2026","Zcash Brazil","Implied only ('junior Dev (to help James)', links to his repos); application names no individuals",GH+"155","Jan 2026","Open"))
add("Jonathan Bird (birdify on the forum)",
 ("Free2Z; Free2Z legal expenses","Free2Z (2Z Inc)","Named in application ('Jonathan Bird, PhD. is a senior software engineer at SAP'); co-founder/CFO",F+"free2-whats-your/41289","Jun 2022","Completed"),
 ("Free2Z: Preparing the Garden For Spring","Free2Z (2Z Inc)","Applicant (thread author birdify): '2Z Inc ... founded by Skylar Saveland (CEO) and Jonathan Bird (CFO)'",F+"free2z-preparing-the-garden-for-spring/43979","Mar 2023","Completed"))
add("Juan Carlos Carmona Calvo (Juanky on the forum)",("Implement Orchard Funded Amendment; Zingo! Onward","Zingo Labs","Named team ('Now there are 3 of us (Za, Juanky, Gygaxis)'; applicants incl. juanky@zingolabs.org; 'Juanky - TypeScript, FrontEnd, UX/UI'); forum title Zingo Labs",F+"implement-orchard/42706","Nov 2022","Completed"))
add("Kroy",("ZecHub 2026","ZecHub","Application co-owner @theKroy, 'Core Contributor'; '@Kroy $53,760' (forum theKroy 'Designer | ZecHub')",GH+"153","Jan 2026","Open"))
add("Max Hampshire",("The Nym mixnet for Network Privacy for Zcash","Nym Technologies","Nym engineer delivering the milestones (posts as maxnym/mxx: 'I have created a module in our SDK'; branch nymtech/nym max/lwd-stream-patch; nymtech commits by 'Max Hampshire'); not named in the proposal",F+"revised-nym-for-zcash-network-level-privacy/46688","Oct 2024","Open"))
add("Minevg (on the forum)",
 ("Zcash Brazil 2023; Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Named team member ('Mine', design; 2024: '@Minevg: Graduated in graphic design in 2006')",F+"zcash-global-zcash-brazil/46295","Jan 2023","Completed"),
 ("Zcash Brazil 2025","Zcash Brazil","Named core team (Design)",GH+"8","Jan 2025","Completed"),
 ("Zcash Brazil 2026","Zcash Brazil","Team member per milestone reports ('Design Team @iogy & @Minevg'); application names no individuals",F+"53702/14","Jan 2026","Open"))
add("Robmarn (on the forum)",
 ("Zcash Global en Español (2024)","Zcash Español","Named team member (one of 5)",F+"zcash-global-en-espanol-q4/49019","Nov 2024","Completed"),
 ("Zcash Global en Español 2025; 2026","Zcash Español","Named team member, $1,200/month; co-owner on #157",GH+"10","Feb 2025","Completed/Open"),
 ("Zk Av Club 2025; Community Media Infrastructure 2026","ZK AV Club","Named team member 'Robmar Enoe' (Technical Director 2026)",GH+"11","Feb 2025","Completed/Open"))
add("Rodrigo Schönell",("Zcash Brazil 2026","Zcash Brazil","Team member per 2026 milestone reports ('@Schönell ... moderates our channels'; 'Event management: Schonell'); application names no individuals",F+"53702/14","Jan 2026","Open"))
add("Samaraanni (on the forum)",
 ("Zcash Brazil 2023","Zcash Brazil","Named team member ('Team members name: Vito Mine Iogy E-zec Samara', PR)",F+"zcash-brazil-2023-proposal/43499","Jan 2023","Completed"),
 ("Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Named on the proposal ('@Samaraanni: Graduated in business administration ... public relations'); absent from the 2024 payout reports",F+"zcash-global-zcash-brazil/46295","Jan 2024","Completed"))
add("Tecnopapapi (on the forum)",("ZecHub: Proposal 2024","ZecHub","Named core team ('@Dismad @Squirrel @Tecnopapapi'; '@tecnopapapi $82 * 5hrs * 22 weeks')",F+"zechub-proposal-2024/46077","Jan 2024","Completed"))
add("tokidoki (on the forum)",("ZecHub (2023)","ZecHub","Named applicant ('Applicant Names: Jason Rogers, Dismad, Tokidoki'; 'compensation for three main contributors @dismad @squirrel @tokidoki')",F+"zechub-open-source-education-for-zcash/43761","Mar 2023","Completed"))
add("Tron",("ZecHub 2026","ZecHub","Core contributor '@tron $53,760' (= GitHub onajifortune, 'Fortune', by list order); ZecHub: 'development server ... set up by Tron and Dismad'. Identity link to ZCAP 'Tron' rests on the name and the Dec 2025 join date; the forum account Tron is a dormant 2016 user",GH+"153","Jan 2026","Open"))
add("vito (on the forum)",
 ("Zcash Brazil 2023; Zcash Global <> Zcash Brazil (2024)","Zcash Brazil","Named team member ('@vito: Victor is a Community Manager'; PR $1,000/month in 2024 reports)",F+"zcash-brazil-2023-proposal/43499","Jan 2023","Completed"),
 ("ZecHub 2025; ZecHub 2026","ZecHub","Application co-owner @vitozkp, core team, $61,440 / $69,120",GH+"9","Jan 2025","Completed/Open"))

# ---------------- Approved, nothing paid ----------------
add("Maxime Desalle",("Mastering Zcash Video Series","maxdesalle","Approved then cancelled; $0 paid",GH+"263","Apr 2026","Cancelled, $0 paid"))
add("Lai Ying Tong",("halo2 Community Manager","Ying Tong","Approved Feb 2023, retroactively withdrawn Jan 2024; $0 paid",F+"halo2-community-manager/43795","Feb 2023","Cancelled, $0 paid"))
