# -*- coding: utf-8 -*-
"""Svenska innehåll för valutapar-sidorna (”USD till EUR”).

PAIR_UI_L10N motsvarar strängarna i den engelska standardmallen
pair_pages.PAIR_UI (platshållarna {f} {t} {d} är oförändrade).
PAIR_CONTENT_L10N motsvarar de 15 paren ur PAIR_CONTENT med identiska
nycklar. build-lang-pages.py slår ihop allt med PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Omvandlare i realtid",
    "pairRateHead": "Aktuell växelkurs",
    "pairAsOf": "Referenskurs per {d}. Omvandlaren ovan hämtar alltid den senaste kursen — tabellerna nedan är en ögonblicksbild vid byggtillfället och enbart till orientering.",
    "pairAmounts": "Vanliga belopp: {f} till {t}",
    "pairReverse": "Vanliga belopp: {t} till {f}",
    "pairMore": "Fler {f}-omvandlingar",
    "pairMorePairs": "Fler valutapar",
    "pairIntroHead": "Om växelkursen {f}/{t}",
    "pairCurLinks": "Valutasidor",
    "pairMetaTmpl": ("Omvandla {f} till {t} med aktuella kurser: dagens {f}/{t}-kurs, en gratis kalkylator, "
                     "tabeller med vanliga belopp och vad som driver det här valutaparet."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD till EUR — dagens kurs, gratis omvandlare och beloppstabeller",
        "description": "Omvandla amerikanska dollar till euro med aktuella kurser: dagens USD/EUR-kurs, en gratis kalkylator, beloppstabeller och vad som driver paret.",
        "h1": "USD till EUR — omvandla amerikanska dollar till euro",
        "intro": [
            "USD/EUR är världens mest omsatta valutapar — ungefär en fjärdedel av all valutahandel — vilket är skälet till att det har de snälaste spreadarna och den djupaste marknaden av alla omvandlingar. Kursen är helt enkelt priset på en amerikansk dollar uttryckt i euro, satt kontinuerligt av global handel, investeringsflöden och räntegapet mellan den amerikanska centralbanken (Fed) och Europeiska centralbanken.",
            "Vid vardagsomvandlingar är den praktiska frågan vilket påslag du betalar gentemot den senkurs som visas här. Banker lägger typiskt till 1–4 procent; kort- och överföringstjänster varierar kraftigt. Att kontrollera den aktuella kursen före ett köp eller en överföring avslöjar omedelbart om en offert är rimlig.",
        ],
        "faq": [
            ("Hur bestäms växelkursen USD till EUR?",
             "Kursen flyter fritt — utbudet och efterfrågan på de två valutorna sätter priset dygnet runt, påverkat framför allt av Fed:s och ECB:s räntepolitik, inflationen på båda sidor om Atlanten och den globala riskstämningen. Det finns inget fast eller styrt mål."),
            ("När är den bästa tidpunkten att växla USD till EUR?",
             "Likviditeten är störst och spreadarna snälaste under överlappningen mellan den europeiska och amerikanska handelssessionen (ungefär 13:00–17:00 UTC). Ingen kan tillförlitligt förutsäga kortsiktiga riktningar, så vid stora belopp är det säkrare att växla i omgångar än att vänta på en bättre dag."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD till GBP — pundkurs i realtid, omvandlare och vanliga belopp",
        "description": "Omvandla amerikanska dollar till brittiska pund med aktuella kurser: USD/GBP-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver pundet.",
        "h1": "USD till GBP — omvandla amerikanska dollar till brittiskt pund",
        "intro": [
            "Kursen mellan dollar och pund, kallad ”cable” efter den transatlantiska telegrafkabel som först förde den på 1860-talet, är en av världens äldsta kontinuerligt noterade växelkurser. I dag speglar den räntegapet mellan Fed och Bank of England, den brittiska inflationen och tillståndet i Storbritanniens handel och statsfinanser.",
            "Sterling handlas mest aktivt under Londons börsstimmar, och paret är benäget att göra skarpa rörelser kring brittisk konjunkturdata och finanspolitiska besked. Att jämföra en offert mot senkursen nedan är det snabbaste sättet att se hur stort påslag en leverantör tar.",
        ],
        "faq": [
            ("Varför är ett brittiskt pund värt mer än en amerikansk dollar?",
             "Ett högre enhetspris betyder inte en starkare ekonomi — det speglar historia och valörer. Pundet var världens dominerande valuta när dollarn ännu inte fanns; siffran i sig säger inget om relativ ekonomisk styrka eller köpkraft."),
            ("Vad påverkar USD/GBP mest?",
             "Räntebeslut från Fed och Bank of England, brittiska inflationssiffror samt politiska och finanspolitiska nyheter från Westminster. I samband med brexitomröstningen 2016 föll pundet omkring 10 procent på en dag — en påminnelse om att sterling bär ett politiskt riskmoment som de flesta stora valutor saknar."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD till JPY — yenkurs i realtid, kalkylator och beloppstabeller",
        "description": "Omvandla amerikanska dollar till japanska yen med aktuella kurser: USD/JPY-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver yenen.",
        "h1": "USD till JPY — omvandla amerikanska dollar till japanska yen",
        "intro": [
            "USD/JPY är världens näst mest omsatta valutapar och den klassiska måttstocken för räntegapet mellan USA och Japan. Eftersom de japanska räntorna legat nära noll i årtionden blev yenen världens favoritfinansieringsvaluta — den försvagas när marknaderna är trygga och stärks kraftigt när kriser rullar upp de positionerna.",
            "Paret följs också med tanke på officiella japanska interventioner: finansministeriet har upprepade gånger köpt yen när den fallit för långt, för snabbt. Stora omvandlingar bör kontrolleras mot senkursen, eftersom detaljhandelspåslagen på JPY kan vara vilseledande breda.",
        ],
        "faq": [
            ("Varför faller yenen ibland så kraftigt mot dollarn?",
             "Framför allt på grund av räntegapet. När de amerikanska räntorna är höga och de japanska ligger kvar nära noll säljer investerare yen för att köpa högreavkastande dollartillgångar — carry-handeln. Yenen kan glida i månader för att sedan hoppa vilt när dessa positioner rullas upp."),
            ("Kan den japanska regeringen ändra USD/JPY-kursen?",
             "Den kan motverka marknaden, inte vända den. Japan har ingripit genom att köpa eller sälja yen när rörelserna blev oordnade, ibland för tiotals miljarder dollar i ett enda skede. Interventioner jämnar vägen; de ändrar sällan den långsiktiga riktning som grundförutsättningarna sätter."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD till CNY — yuan-kurs, gratis omvandlare och beloppstabeller",
        "description": "Omvandla amerikanska dollar till kinesiska yuan: dagens USD/CNY-kurs, en gratis kalkylator, beloppstabeller och hur den styrda kursen fungerar.",
        "h1": "USD till CNY — omvandla amerikanska dollar till kinesiska yuan",
        "intro": [
            "Kursen mellan dollar och yuan är det största valutapar som styrs av en centralbank. Varje morgon fastställer Folkbanken i Kina en daglig fixingskurs, och den onshore-noterade kursen (CNY) får bara röra sig inom ett band runt den — därför rör sig USD/CNY betydligt mindre dag för dag än dess ekonomiska vikt antyder.",
            "Kinas handelsöverskott, kapitalkontrollerna och de politiska målsättningarna formar alla kursen. Vid omvandlingar: notera att onshore-CNY och offshore-CNH kan avvika något, och att privat valutaväxling i Kina omfattas av kapitalkontrollsreglerna. Jämför alltid offerter mot referenskursen nedan.",
        ],
        "faq": [
            ("Är kinesiska yuan fritt konvertibel?",
             "Inte helt. Handelsrelaterad växling är enkel, men investeringsflöden över gränsen styrs av kvoter och godkännanden. Därför handlas offshore-varianten (CNH) till ett något annat pris än onshore-CNY — gapet visar hur dyrt det är att flytta pengar över gränsen."),
            ("Varför rör sig USD/CNY knappt jämfört med andra par?",
             "Eftersom centralbanken styr den. Den dagliga fixingskursen och handelsbandet håller kursen stabil relativt dollarn, i linje med Kinas preferens för förutsägbarhet i handeln. Styrt betyder inte fixerat: över månader och år tenderar kursen ändå att följa grundförutsättningarna."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD till INR — rupiekurs i realtid, omvandlare och vanliga belopp",
        "description": "Omvandla amerikanska dollar till indiska rupier med aktuella kurser: USD/INR-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver rupien.",
        "h1": "USD till INR — omvandla amerikanska dollar till indiska rupier",
        "intro": [
            "USD/INR är en av världens viktigaste överföringskorridorer — Indien tar emot fler hemöverföringar än något annat land — och ett hårt handlat tillväxtmarknadspar. Indiens centralbank (Reserve Bank of India) styr volatiliteten snarare än nivån: den jämnar ut skarpa rörelser med sina reserver men låter rupien hitta sin långsiktiga trend.",
            "Rupiens långsiktiga berättelse är en gradvis försvagning mot dollarn, driven av inflationsdifferenser och Indiens bytesbalans, avbruten av globala riskhändelser. För den som skickar pengar till Indien är gapet mellan senkursen och den erbjudna kursen där den verkliga kostnaden gömmer sig.",
        ],
        "faq": [
            ("Varför försvagas indiska rupien över tid?",
             "Framför allt på grund av inflationsdifferenser och handelsunderskottet: Indien importerar långt mer än det exporterar, och skillnaden finansieras av kapitalinflöden. RBI jämnar ut vägen, men över årtionden har rupien stadigt försvagats mot dollarn — normalt för en utvecklingsekonomi."),
            ("Hur får jag den bästa kursen när jag skickar pengar till Indien?",
             "Jämför den erbjudna kursen mot senkursen innan du skickar, inte bara avgifterna. Specialiserade överföringstjänster slår vanligtvis banköverföringarna på den här korridoren, och redan 1 procents skillnad väger tungt vid återkommande familjeöverföringar under ett år."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD till CAD — looniekurs, gratis omvandlare och beloppstabeller",
        "description": "Omvandla amerikanska dollar till kanadensiska dollar i realtid: USD/CAD-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver loonien.",
        "h1": "USD till CAD — omvandla amerikanska dollar till kanadensiska dollar",
        "intro": [
            "USD/CAD — i valutajargongen ”loonie” — är ett av världens fem mest omsatta par och vilar på en av jordens största handelsrelationer. Kanada skickar omkring tre fjärdedelar av sin export till USA, så paret handlas tungt på amerikansk tillväxt, energipriser (Kanada är en stor oljeexportör) och räntegapet mellan Fed och Kanadas centralbank.",
            "När oljan stiger tenderar CAD att stärkas; när global tillväxtoro slår till försvagas den med råvaruvalutorna i stort. Paret är likvidt dygnet runt, och offerter inom en bråkdel av en procent från senkursen är lätta att hitta — breda påslag är därför alltid värda att ifrågasätta.",
        ],
        "faq": [
            ("Varför kallas kanadensiska dollar loonie?",
             "Efter doppingen — fågeln på en-dollarmyntet som introducerades 1987. Smeknamnet fastnade och avser numera själva valutan i valutajargong, som i ”loonien drog iväg i dag”."),
            ("Påverkar oljepriset verkligen USD/CAD?",
             "Ja, påtagligt. Råolja och närliggande produkter är Kanadas största exportkategori, så stigande oljepriser tenderar att föra fler dollar till Kanada och lyfta CAD. Handlare behandlar paret som ett grovt spel på energimarknaderna — utöver de två ländernas räntor."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD till AUD — aussiekurs i realtid, kalkylator och tabeller",
        "description": "Omvandla amerikanska dollar till australiska dollar i realtid: dagens USD/AUD-kurs, en gratis kalkylator, beloppstabeller och vad som driver aussien.",
        "h1": "USD till AUD — omvandla amerikanska dollar till australiska dollar",
        "intro": [
            "Den australiska dollarn är den klassiska råvaruvalutan: dess öden följer exporten av järnmalm, kol och gas och framför allt den kinesiska efterfrågan på dem. USD/AUD är därmed en av de renaste realtidsindikatorerna på den globala riskaptiten — aussien stärks när världshandeln går bra och försvagas i riskavvikelser.",
            "Räntepolitiken från Australiens centralbank och Fed driver de kortare svängningarna. Australiens arbetande ungdomar och studenter gör USD→AUD (och tillbaka) till en vanlig återkommande omvandling, där redan ett kurspåslag på 1 procent ackumuleras snabbt.",
        ],
        "faq": [
            ("Varför är australiska dollar så känslig för Kina?",
             "Kina är med god marginal Australiens största exportmarknad, särskilt för järnmalm till stålproduktionen. När den kinesiska byggkonjunkturen kyls av faller vanligen råvarupriser och AUD tillsammans — valutan fungerar som ett realtidsbarometer för kinesisk tung industri."),
            ("Är AUD en trygg hamn?",
             "Tvärtom: handlare kallar den en riskvaluta. I globala panikskeden — 2008, 2020 — flyter pengar till amerikanska dollar och aussien faller oftast hårdast av de stora valutorna. Just den cykliska karaktären är skälet till att carry-handlare och tillväxtbevakare följer den så noggrant."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD till CHF — francens kurs, gratis omvandlare och beloppstabeller",
        "description": "Omvandla amerikanska dollar till schweiziska franc i realtid: USD/CHF-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver francen.",
        "h1": "USD till CHF — omvandla amerikanska dollar till schweiziska franc",
        "intro": [
            "Schweiziska francen är världens främsta trygghetsvaluta: när krig, bankstress eller marknadspanik slår till flyter pengar till Schweiz och CHF stärks. USD/CHF tenderar därför att falla i globala kriser även när dollarn själv är en tillflyktsort — francen är helt enkelt det starkare skyddsrummet.",
            "Schweiz nationalbank formar kursen aktivt, från det berömda eurogolvet 2011–2015 till omfattande interventioner sedan dess. För omvandlingar påminner Schweiz också om att ett rikt lands valutapar ändå kan bära breda detaljhandelspåslag, särskilt på flygplatser och hotell — kontrollera alltid senkursen som referens.",
        ],
        "faq": [
            ("Varför räknas schweiziska francen som en trygg hamn?",
             "Ett sekel av neutralitet, låg statsskuld, bytesbalansöverskott och en trovärdig centralbank gör francen till standardplatsen för pengar på flykt undan risk. Den schweiziska inflationen har dessutom legat långt under den amerikanska och eurozonen i årtionden, vilket bevarat valutans köpkraft."),
            ("Vad gjorde SNB i januari 2015?",
             "Den övergav abrupt sitt golv för francens styrka mot euron. USD/CHF och EUR/CHF kollapsade omkring 20–30 procent inom några minuter — en av de största intradagrörelserna någonsin i ett stort par, och skälet till att handlare fortfarande respekterar begreppet ”SNB-risk”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD till MXN — pesokurs i realtid, omvandlare och vanliga belopp",
        "description": "Omvandla amerikanska dollar till mexikanska pesos i realtid: USD/MXN-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver peson.",
        "h1": "USD till MXN — omvandla amerikanska dollar till mexikanska pesos",
        "intro": [
            "USD/MXN är det mest omsatta tillväxtmarknadsparet i Amerika och ett av världens mest likvida. Peson handlas på allt som rör den amerikanska ekonomin — handelspolitik, tillväxt, räntegapet mellan Fed och Mexikos centralbank (Banxico) — plus oljepriser och den enorma överföringskorridoren från USA.",
            "Eftersom paret är så likvidt reagerar det snabbt på den globala riskstämningen: det är ett klassiskt carry-mål som stärks i lugna marknader och kollapsar brant i panik. För resenärer och överföringsskickare är påslag om 3–6 procent vanliga på flygplatserna — senkursen nedan är riktmärket att jämföra mot.",
        ],
        "faq": [
            ("Varför är USD/MXN så volatilt?",
             "Höga räntor i Mexiko lockar kortfristiga carry-pengar som drar iväg snabbt i stress; peson är dessutom referenstillgången för hela handeln och den politiska nyhetsströmmen mellan USA och Mexiko. Kombinationen gör den likvid men lättstörd — stora dagsrörelser är normala, inte ett fel."),
            ("Vilket är det billigaste sättet att skicka dollar till Mexiko?",
             "Specialiserade överföringstjänster slår banker och kontanttransferbutiker regelbundet på den här korridoren. Jämför det belopp som anländer mot senkursen: på en överföring på 300 dollar kan skillnaden mellan en rimlig offert och ett påslag på 5 procent motsvara en hel dagslön på plats."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD till PHP — pesoskursen i dag, kalkylator och beloppstabeller",
        "description": "Omvandla amerikanska dollar till filippinska pesos i realtid: USD/PHP-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver peson.",
        "h1": "USD till PHP — omvandla amerikanska dollar till filippinska pesos",
        "intro": [
            "Den filippinska peson bär upp av ett av världens största överföringsflöden: miljontals filippinska arbetare utomlands skickar pengar hem, och de dollarinflödena är en pelare i ekonomin. USD/PHP handlas därför på global riskaptit, oljepriser (Filippinerna är nettoimportör) och politiken från Bangko Sentral ng Pilipinas.",
            "Den officiella kursen styrs med lätt hand — centralbanken tillåter gradvis anpassning samtidigt som toppar jämnas ut. För OFW-familjer och resenärer är spreadarna mellan leverantörer på den här korridoren breda, så att kontrollera senkursen innan du skickar är det enskilt enklaste sättet att spara.",
        ],
        "faq": [
            ("Hur påverkar hemöverföringarna den filippinska peson?",
             "Stadiga dollarinflöden från utlandarbetare stöder peson och landets betalningsbalans — flera procent av BNP varje år. När den globala risken stiger eller värdländerna försvagas mattas överföringarna av, och peson tenderar att följa efter."),
            ("Är det bättre att växla USD till PHP i USA eller på Filippinerna?",
             "Det beror på leverantören, inte på landet. På båda sidor av korridoren finns billiga och dyra alternativ; det avgörande talet är hur många pesos mottagaren faktiskt får. Jämför offerterna mot senkursen i stället för att lita på butiken som ligger närmast."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR till GBP — pundkurs, kalkylator och tabeller med vanliga belopp",
        "description": "Omvandla euro till brittiska pund med aktuella kurser: EUR/GBP-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver paret.",
        "h1": "EUR till GBP — omvandla euro till brittiskt pund",
        "intro": [
            "EUR/GBP är den klassiska europeiska korsen: två ekonomier som står för ungefär hälften av varandras handel, skilda av en enda valutagräns. Eftersom båda är utvecklade låginflationsvalutor rör sig paret betydligt mindre än dollarkorsen — i grunden är det ett spel på eurozonens och Storbritanniens relativa öden.",
            "Räntegapet mellan ECB och Bank of England driver större delen av trenden, medan brittiska politiska och finanspolitiska nyheter orsakar utslagen. För gränsarbetspendlare, pensionärer och företag gör parets stabilitet att små kursskillnader väger ännu tyngre: ett påslag på 1 procent är en stor andel av hela årets rörelse.",
        ],
        "faq": [
            ("Varför är EUR/GBP lugnare än EUR/USD?",
             "Varken euron eller pundet är en global riskvaluta, så säkerhetsflykter världen över passerar dem förbi. Paret speglar främst den relativa ekonomin mellan Storbritannien och EU samt räntedifferenser, som ändras långsamt — även om det kan slå ut hårt på brittisk politik, som 2016 visade."),
            ("Hur påverkar brexit fortfarande EUR/GBP?",
             "Strukturellt. Nytt handelsgnissel sedan 2021 har gjort den brittiska ekonomin något mindre öppen mot EU, vilket de flesta ekonomer förbinder med ett strukturellt svagare pund. Varje omgång förhandlingar mellan Storbritannien och EU om handelsregler flyttar fortfarande paret."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR till CHF — francens kurs, omvandlare och SNB:s roll",
        "description": "Omvandla euro till schweiziska franc med aktuella kurser: EUR/CHF-kursen i dag, en gratis kalkylator, beloppstabeller och SNB:s roll för paret.",
        "h1": "EUR till CHF — omvandla euro till schweiziska franc",
        "intro": [
            "EUR/CHF är Europas lackmustest för trygghetshamnar: när stressen i eurozonen stiger — skuldkrisen 2011, bankoro, krig på kontinenten — flyter pengar över den schweiziska gränsen och paret faller. Schweiz nationalbank följer den här kursen noggrannare än någon annan och har upprepade gånger ingripit för att francen inte ska kväva de schweiziska exporterna.",
            "Parets moderna historia är dramatisk: ett golv vid 1,20 från 2011, och därefter uppgivandet av golvet i januari 2015 som producerade en blixtkrasch om 20–30 procent på minuter. Sedan dess handlas francen som en ren, om ibland alltför stark, tillflyktsort — och SNB förblir en aktiv deltagare på den här marknaden.",
        ],
        "faq": [
            ("Varför bryr sig Schweiz nationalbank så mycket om EUR/CHF?",
             "Eftersom den schweiziska ekonomin säljer till Europa. En alltför stark franc gör schweiziska exporter okonkurrerbara och drar inflationen under målet, därför köper SNB utländsk valuta (och en gång införde negativa räntor) för att takla francens styrka. Banken ingriper i det här paret mer än nästan någon annan centralbank i en stor marknad."),
            ("Är EUR/CHF ett stabilt par att hålla?",
             "Det är stabilt i lugna tider och explosivt i kriser — motsatsen till diversifierat. Uppgivandet av golvet 2015 förblir läroboksvarningen om att en centralbanks löfte att takla en valuta kan dras tillbaka över en natt. Den som behandlade paret som riskfritt fick lära sig annat under en enda morgon."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR till PLN — zlotykurs i realtid, gratis omvandlare och tabeller",
        "description": "Omvandla euro till polska zloty med aktuella kurser: EUR/PLN-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver zlotyn.",
        "h1": "EUR till PLN — omvandla euro till polska zloty",
        "intro": [
            "Polen är EU:s sjätte största ekonomi som fortfarande har en egen valuta, och zlotyn är den mest handlade av unionens icke-eurovalutor. EUR/PLN handlas på räntegapet mot Polens nationalbank (NBP), EU-medel som flyter österut, tyska fabriksorder till den polska industrin och regionens geopolitiska risk.",
            "Sedan Polen gick med i EU 2004 har zlotyn både stärkts i boomer och fallit hårt i kriser — 2008 och 2022 drev paret till historiska ytterligheter. Med Polens framtida eurointräde fortfarande obeslutat förblir paret en strukturell del av den europeiska finansvärlden i flera år framåt.",
        ],
        "faq": [
            ("Kommer Polen att införa euron och avskaffa zlotyn?",
             "Polen är rättsligt förpliktat att så småningom gå med i euron men har ingen måltidpunkt, och allmänheten är skeptisk. Så länge det inte finns en trovärdig tidtabell förblir EUR/PLN ett aktivt handlat par — enbart politiska uttalanden om tidplanen kan flytta det."),
            ("Varför sken EUR/PLN upp 2022?",
             "Kriget i grannlandet Ukraina gjorde Polen till en frontekonomi över en natt: flyktingströmmar, försvarsutgifter och energichocker drabbade valutan hårt. Polens nationalbank ingrep för att stödja zlotyn — parets skarpaste rörelser på två decennier."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP till JPY — yenkurs, omvandlare och tabeller för det vilda paret",
        "description": "Omvandla brittiska pund till japanska yen i realtid: GBP/JPY-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver det volatila paret.",
        "h1": "GBP till JPY — omvandla brittiska pund till japanska yen",
        "intro": [
            "GBP/JPY — äldre handlare kallade det ”odjuret” eller ”draken” — är ett av de mest volatila stora valutaparen. Det staplar två riskmotorer ovanpå varandra: sterlings känslighet för brittisk politik och statsfinanser, och yenens roll som världens finansieringsvaluta, som får det att slå ut kraftigt varje gång den globala stämningen vänder.",
            "Paret är en favorit i carry-handeln: att låna nästan räntefria yen för att köpa högreavkastande pund. Det fungerar tills en kris tvingar alla att rulla upp samtidigt, vilket är skälet till att GBP/JPY tenderar att arbeta uppåt i åratal och falla vilt på veckor. Positionsstorlek och tajming spelar här större roll än i nästan något annat stort par.",
        ],
        "faq": [
            ("Varför är GBP/JPY mer volatilt än USD/JPY?",
             "Eftersom det multiplicerar två volatiliteter. Sterling lägger brittisk politik- och konjunkturrisiko ovanpå den globala riskstämning som redan driver USD/JPY. Paret saknar en gemensam ankarekonomi och handlas därför nästan uteslutande på räntegap och stämning — en recept på stora rörelser."),
            ("Vad är carry-handeln i GBP/JPY?",
             "Att låna yen till nästan nollprocentsränta i Japan och investera i pund till högre brittiska räntor, och komma undan med differensen. Det lönar sig medan marknaderna är lugna och straffar hårt när de inte är det: i riskavvikelser skjuter yenen i höjden när carry-positionerna rullas upp — ofta 10 procent eller mer mot pundet på några månader."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD till JPY — riskbarometern, kalkylator och vanliga belopp",
        "description": "Omvandla australiska dollar till japanska yen: AUD/JPY-kursen i dag, en gratis kalkylator, beloppstabeller och vad som driver riskbarometern.",
        "h1": "AUD till JPY — omvandla australiska dollar till japanska yen",
        "intro": [
            "AUD/JPY är valutamarknadens renaste riskbarometer. Den australiska dollarn representerar global tillväxt och råvaruefterfrågan — framför allt den kinesiska industriella efterfrågan — medan yenen representerar trygghet. När världsekonomin expanderar klättrar paret; när panik slår till faller det snabbare än nästan någon annan stor kors.",
            "Det är också det klassiska carry-paret: i decennier lånade investerare billiga yen för att köpa den högreavkastande aussien. Det flödet formar parets långa, sega uppgångar och dess vilda upprullningar — 2008 förblir det varnande exemplet, när AUD/JPY förlorade omkring hälften av sitt värde på några månader.",
        ],
        "faq": [
            ("Varför kallar handlare AUD/JPY en riskbarometer?",
             "Eftersom varje valuta står vid en motsatt pol: aussien stiger med global tillväxt och råvaruefterfrågan, yenen med rädsla. Paret rör sig därför med världsaktiemarknaderna i en grad som få andra kors når — när det faller hårt är riskavvikelsen på riktigt."),
            ("Vad hände med AUD/JPY i krisen 2008?",
             "Det halverades ungefär. När den globala krediten frös rullades carry-handeln upp: investerare sålde australiska dollar för att återbetala lånade yen, och paret störtade från över 100 till låga 50-tal på några månader. Det förblir standardexemplet på hur snabbt carry-strategier vänder."),
        ],
    },
}
