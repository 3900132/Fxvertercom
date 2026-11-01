# -*- coding: utf-8 -*-
"""Nederlandse inhoud voor de valutapaar-pagina’s (‘USD naar EUR’).

PAIR_UI_L10N komt overeen met de strings uit pair_pages.PAIR_UI (de
placeholders {f} {t} {d} blijven ongewijzigd). PAIR_CONTENT_L10N komt overeen
met de 15 paren uit PAIR_CONTENT; de sleutels zijn identiek aan de Engelse
versie. build-lang-pages.py voegt beide samen in PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Live omrekenaar",
    "pairRateHead": "Actuele wisselkoers",
    "pairAsOf": "Referentiekoers van {d}. De live omrekenaar hierboven haalt altijd de nieuwste koers op — de tabellen hieronder zijn een momentopname bij het bouwen van de site, ter oriëntatie.",
    "pairAmounts": "Gebruikelijke bedragen: {f} in {t}",
    "pairReverse": "Gebruikelijke bedragen: {t} in {f}",
    "pairMore": "Meer {f}-omrekeningen",
    "pairMorePairs": "Meer valutaparen",
    "pairIntroHead": "Over de wisselkoers van {f} naar {t}",
    "pairCurLinks": "Valutapagina’s",
    "pairMetaTmpl": ("Bereken {f} naar {t} met actuele wisselkoersen: de koers {f}/{t} van vandaag, een gratis omrekenaar, "
                     "tabellen met gebruikelijke bedragen en wat dit valutapaar beweegt."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD naar EUR — koers van vandaag, gratis omrekenaar en bedragtabellen",
        "description": "Dollar naar euro omrekenen met live koersen: de USD/EUR-koers van vandaag, een gratis omrekenaar, tabellen met gebruikelijke bedragen en wat dit paar beweegt.",
        "h1": "USD naar EUR — Amerikaanse dollar naar euro omrekenen",
        "intro": [
            "USD/EUR is het meest verhandelde valutapaar ter wereld — ruwweg een kwart van de totale deviezenomzet — en heeft daardoor de nauwste spreads en de diepste markt van alle omrekeningen. De koers is niets meer of minder dan de prijs van één Amerikaanse dollar in euro’s, voortdurend vastgesteld door wereldhandel, investeringsstromen en de rentekloof tussen de Federal Reserve en de Europese Centrale Bank.",
            "Bij alledaagse omrekeningen is de praktische vraag welke marge u betaalt boven de middenkoers die hier staat. Banken tellen doorgaans 1–4 procent op; kaart- en overschrijvingsdiensten lopen sterk uiteen. Wie vóór een aankoop of overboeking de live koers controleert, ziet meteen of een aanbod eerlijk is.",
        ],
        "faq": [
            ("Hoe wordt de wisselkoers USD naar EUR bepaald?",
             "Hij zweeft vrij — vraag en aanbod naar de twee munten bepalen de koers rond de klok, beïnvloed vooral door het rentebeleid van de Fed en de ECB, de inflatie aan weerszijden van de Atlantische Oceaan en het wereldwijde risicosentiment. Er bestaat geen vast of beheerd doel."),
            ("Wanneer is het beste moment om USD naar EUR om te rekenen?",
             "De liquiditeit is het diepst en de spreads het nauwst tijdens de overlapping van de Europese en Amerikaanse handelsuren (ruwweg 13:00–17:00 UTC). Niemand kan de korte termijnrichting betrouwbaar voorspellen, dus voor grote bedragen is het verstandiger in delen om te rekenen dan op een betere dag te wachten."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD naar GBP — actuele wisselkoers, omrekenaar en wat het pond beweegt",
        "description": "Amerikaanse dollars naar Britse ponden omrekenen met live koersen: de USD/GBP-koers van vandaag, een gratis omrekenaar en wat het pond beweegt.",
        "h1": "USD naar GBP — Amerikaanse dollar naar Brits pond omrekenen",
        "intro": [
            "De koers tussen dollar en pond — bij handelaren ‘cable’ genoemd, naar de transatlantische telegraafkabel die hem in de jaren 1860 voor het eerst doorgaf — behoort tot de oudste doorlopend genoteerde wisselkoersen ter wereld. Vandaag weerspiegelt hij de rentekloof tussen de Federal Reserve en de Bank of England, de Britse inflatie en de staat van de Britse handel en overheidsfinanciën.",
            "Sterling handelt het actiefst tijdens de Londense uren, en het paar is gevoelig voor scherpe bewegingen rond Britse economische cijfers en begrotingsaankondigingen. Elke offerte vergelijken met de middenkoers hieronder is de snelste manier om te zien hoeveel marge een aanbieder neemt.",
        ],
        "faq": [
            ("Waarom is het Britse pond meer waard dan de Amerikaanse dollar?",
             "Een hogere eenheidsprijs betekent geen sterkere economie — hij weerspiegelt geschiedenis en denominaties. Het pond was de dominante munt van de wereld toen de dollar nog niet bestond; het getal zelf zegt niets over relatieve economische kracht of koopkracht."),
            ("Wat beweegt USD/GBP het sterkst?",
             "Rentebesluiten van de Fed en de Bank of England, Britse inflatiecijfers en politiek of begrotingsnieuws uit Westminster. Tijdens de Brexit-stemming van 2016 zakte het pond op één dag zo’n 10 procent — een herinnering dat sterling een politiek risico draagt dat de meeste grote munten niet kennen."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD naar JPY — yen-koers van vandaag met gratis omrekenaar en tabellen",
        "description": "Dollar naar Japanse yen omrekenen met live koersen: de USD/JPY-koers van vandaag, een gratis omrekenaar, bedragtabellen en uitleg over de rentekloof.",
        "h1": "USD naar JPY — Amerikaanse dollar naar Japanse yen omrekenen",
        "intro": [
            "USD/JPY is het op één na meest verhandelde valutapaar ter wereld en de klassieke barometer van de rentekloof tussen de Verenigde Staten en Japan. Omdat de Japanse rente decennialang rond nul lag, werd de yen de favoriete financieringsmunt van de wereld — hij verzwakt wanneer de markten zelfverzekerd zijn en trekt scherp aan wanneer crises die posities afwikkelen.",
            "Het paar wordt ook gevolgd vanwege officiële Japanse interventies: het ministerie van Financiën heeft herhaaldelijk yen gekocht wanneer hij te ver en te snel daalde. Controleer grote omrekeningen altijd tegen de middenkoers, want retailmarges op de JPY kunnen verrassend breed zijn.",
        ],
        "faq": [
            ("Waarom zakt de yen soms zo ver tegenover de dollar?",
             "Vooral door de rentekloof. Wanneer de Amerikaanse rente hoog is en de Japanse rond nul blijft, verkopen beleggers yen om hoger renderende dollaractiva te kopen — de carry trade. De yen kan maandenlang afdalen en dan gewelddadig opspringen wanneer die transacties worden afgerold."),
            ("Kan de Japanse overheid de koers USD/JPY veranderen?",
             "Zij kan tegen de markt in leunen, hem niet omkeren. Japan heeft ingegrepen door yen te kopen of te verkopen wanneer bewegingen wanordelijk werden, soms met tientallen miljarden dollars in één episode. Interventies gladstrijken het pad; ze veranderen zelden de langetermijnrichting die de fundamenten bepalen."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD naar CNY — actuele koers, omrekenaar en uitleg over de yuan",
        "description": "Dollar naar Chinese yuan omrekenen met live koersen: de USD/CNY-koers van vandaag, een gratis omrekenaar en hoe de beheerde koers van China werkt.",
        "h1": "USD naar CNY — Amerikaanse dollar naar Chinese yuan omrekenen",
        "intro": [
            "De koers tussen dollar en yuan is het grootste valutapaar dat door een centrale bank wordt beheerd. Elke ochtend stelt de People’s Bank of China een officiële fixing vast, en de onshore koers (CNY) mag zich alleen binnen een band daaromheen bewegen — daarom beweegt USD/CNY van dag tot dag veel minder dan zijn economische gewicht doet vermoeden.",
            "Het handelsoverschot van China, de kapitaalcontroles en de beleidsdoelen sturen allemaal de koers. Bij omrekeningen geldt: onshore CNY en offshore CNH kunnen licht verschillen, en particuliere valutaconversie in China valt onder de kapitaalregelgeving. Vergelijk aanbiedingen altijd met de referentiekoers hieronder.",
        ],
        "faq": [
            ("Is de Chinese yuan vrij converteerbaar?",
             "Niet volledig. Conversie voor handel is eenvoudig, maar investeringsstromen over de grens vallen onder quota en goedkeuringen. Daarom noteert de offshorevariant (CNH) iets anders dan de onshore CNY — het gat laat zien hoe duur het is om geld over de grens te bewegen."),
            ("Waarom beweegt USD/CNY nauwelijks vergeleken met andere paren?",
             "Omdat de centrale bank hem beheert. De dagelijkse fixing en de handelsband houden de koers stabiel ten opzichte van de dollar, in lijn met de voorkeur van China voor voorspelbaarheid in de handel. Beheerd betekent niet vast: over maanden en jaren beweegt de koers toch met de fundamenten mee."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD naar INR — actuele roepie-koers, gratis omrekenaar en bedragtabellen",
        "description": "Dollar naar Indiase roepie omrekenen met live koersen: de USD/INR-koers van vandaag, een gratis omrekenaar, bedragtabellen en overmaaktips.",
        "h1": "USD naar INR — Amerikaanse dollar naar Indiase roepie omrekenen",
        "intro": [
            "USD/INR is een van de belangrijkste corridors voor geldovermakingen ter wereld — India ontvangt meer overmakingen dan enig ander land — en een intens verhandeld opkomend-marktpaar. De Reserve Bank of India beheert de volatiliteit, niet het niveau: ze gladt scherpe bewegingen met haar reserves, maar laat de roepie zijn langetermijntraject vinden.",
            "Het structurele verhaal van de roepie is geleidelijke depreciatie tegenover de dollar, aangedreven door inflatieverschillen en de lopende rekening van India, afgewisseld met mondiale risicogebeurtenissen. Voor wie geld naar India stuurt schuilt de werkelijke kost in het gat tussen de middenkoers en de geboden koers.",
        ],
        "faq": [
            ("Waarom verliest de Indiase roepie door de jaren heen waarde?",
             "Vooral inflatieverschillen en het handelstekort: India importeert veel meer dan het exporteert, en het verschil wordt gefinancierd door kapitaalinstroom. De RBI gladt het pad, maar decennia lang is de roepie gestaag zwakker geworden tegenover de dollar — normaal voor een ontwikkelingseconomie."),
            ("Hoe krijgt u de beste koers bij het sturen van geld naar India?",
             "Vergelijk vóór het versturen de geboden koers met de middenkoers, niet alleen de kosten. Gespecialiseerde overmakingsdiensten verslaan op deze corridor meestal de bankoverschrijving, en zelfs een verschil van 1 procent weegt op over een jaar van regelmatige gezinsoverboekingen."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD naar CAD — wisselkoers van vandaag en omrekenaar voor de loonie",
        "description": "US-dollar naar Canadese dollar omrekenen met live koersen: de USD/CAD-koers van vandaag, een gratis omrekenaar en wat de loonie beweegt.",
        "h1": "USD naar CAD — Amerikaanse dollar naar Canadese dollar omrekenen",
        "intro": [
            "USD/CAD — in FX-jargon de ‘loonie’ — behoort tot de vijf meest verhandelde paren ter wereld en rust op een van de grootste handelsrelaties op aarde. Canada stuurt ruwweg driekwart van zijn export naar de Verenigde Staten, dus het paar handelt sterk op Amerikaanse groei, energieprijzen (Canada is een belangrijke olie-exporteur) en de rentekloof tussen de Fed en de Bank of Canada.",
            "Stijgt de olie, dan wordt de CAD meestal sterker; treffen wereldwijde groeizorgen, dan zwakt hij af met de grondstoffenmunten. Het paar is rond de klok liquide, en offertes binnen een fractie van een procent van de middenkoers zijn gemakkelijk te vinden — brede marges zijn dus altijd een waarschuwing.",
        ],
        "faq": [
            ("Waarom heet de Canadese dollar de loonie?",
             "Naar de ijsduiker — de vogel op het muntstuk van één dollar dat in 1987 werd ingevoerd. De bijnaam bleef hangen en verwijst in FX-kringen nu naar de munt zelf, zoals in ‘de loonie trok vandaag aan’."),
            ("Beïnvloedt de olieprijs USD/CAD echt?",
             "Ja, zichtbaar. Ruwe olie en aanverwante producten zijn de grootste exportcategorie van Canada, dus stijgende olieprijzen brengen doorgaans meer dollars naar Canada en tillen de CAD. Handelaren behandelen het paar als een ruwe inzet op de energiemarkten, naast de rente van beide landen."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD naar AUD — actuele koers, gratis omrekenaar en wat de Aussie beweegt",
        "description": "Amerikaanse dollar naar Australische dollar omrekenen: de USD/AUD-koers van vandaag, een gratis omrekenaar, bedragtabellen en wat de Aussie beweegt.",
        "h1": "USD naar AUD — Amerikaanse dollar naar Australische dollar omrekenen",
        "intro": [
            "De Australische dollar is de klassieke grondstoffenmunt: zijn fortuin loopt mee met de ijzererts-, kolen- en gasexport en bovenal met de Chinese vraag daarnaar. USD/AUD is daarmee een van de zuiverste realtime indicatoren van de wereldwijde risicobereidheid — de Aussie sterkt aan wanneer de wereldhandel bloeit en verzwakt in risicoperiodes.",
            "Het rentebeleid van de Reserve Bank of Australia en de Fed stuurt de kortere schommelingen. De working-holiday- en studentenbevolking van Australië maken USD naar AUD (en terug) tot een veelvoorkomende terugkerende omrekening, waarbij zelfs een koersmarge van 1 procent snel optelt.",
        ],
        "faq": [
            ("Waarom reageert de Australische dollar zo gevoelig op China?",
             "China is bij lange na de grootste exportmarkt van Australië, vooral voor ijzererts voor de staalproductie. Wanneer de Chinese bouw afkoelt, dalen grondstofprijzen en de AUD meestal samen — de munt fungeert als realtime barometer van de Chinese zware industrie."),
            ("Is de AUD een veilige haven?",
             "Integendeel: handelaren noemen hem een risicomunt. In mondiale paniek — 2008, 2020 — stroomt geld naar Amerikaanse dollars en valt de Aussie doorgaans het hardst van de grote munten. Precies die cycliciteit is de reden dat carry traders en groeiwaarnemers hem zo nauwlettend volgen."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD naar CHF — wisselkoers van vandaag, omrekenaar en de Zwitserse frank",
        "description": "Dollar naar Zwitserse frank omrekenen met live koersen: de USD/CHF-koers van vandaag, een gratis omrekenaar en wat de frank beweegt.",
        "h1": "USD naar CHF — Amerikaanse dollar naar Zwitserse frank omrekenen",
        "intro": [
            "De Zwitserse frank is de belangrijkste veilige haven ter wereld: bij oorlog, bankstress of marktpaniek stroomt geld naar Zwitserland en sterkt de CHF aan. USD/CHF daalt daarom vaak in mondiale crises, zelfs wanneer de dollar zelf een toevlucht is — de frank is simpelweg de sterkere schuilplaats.",
            "De Zwitserse Nationale Bank geeft de koers actief vorm, van de beroemde eurovloer van 1,20 in 2011–2015 tot zware interventies sindsdien. Voor omrekeningen herinnert Zwitserland er ook aan dat een welvarend land geen nauwe retailmarges garandeert, vooral op luchthavens en in hotels — controleer altijd de middenkoers als referentie.",
        ],
        "faq": [
            ("Waarom geldt de Zwitserse frank als veilige haven?",
             "Een eeuw neutraliteit, lage schulden, een overschot op de lopende rekening en een geloofwaardige centrale bank maken de frank tot de standaardparkeerplaats voor geld op de vlucht voor risico. De Zwitserse inflatie lag decennialang ook ver onder die van de VS en de eurozone, wat de koopkracht van de munt bewaarde."),
            ("Wat deed de SNB in januari 2015?",
             "Zij schrapte abrupt haar plafond op de sterkte van de frank tegenover de euro. USD/CHF en EUR/CHF stortten binnen minuten zo’n 20–30 procent in — een van de grootste intraday-bewegingen ooit in een groot paar, en de reden dat handelaren de term ‘SNB-risico’ tot op vandaag respecteren."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD naar MXN — actuele peso-koers, gratis omrekenaar en bedragtabellen",
        "description": "Dollar naar Mexicaanse peso omrekenen met live koersen: de USD/MXN-koers van vandaag, een gratis omrekenaar, bedragtabellen en overmaaktips.",
        "h1": "USD naar MXN — Amerikaanse dollar naar Mexicaanse peso omrekenen",
        "intro": [
            "USD/MXN is het meest verhandelde opkomend-marktpaar van Amerika en een van de meest liquide ter wereld. De peso handelt op alles wat de Amerikaanse economie beweegt — handelsbeleid, groei, de rentekloof tussen de Fed en Banxico — plus olieprijzen en de enorme overmakingscorridor vanuit de Verenigde Staten.",
            "Omdat het paar zo liquide is, reageert het snel op het wereldwijde risicosentiment: een klassiek carry trade-doel dat sterkt in rustige markten en bij paniek gewelddadige sprongen maakt. Reizigers en overmakers vinden op luchthavens vaak marges van 3–6 procent — de middenkoers hieronder is de maatstaf om mee te vergelijken.",
        ],
        "faq": [
            ("Waarom is USD/MXN zo volatiel?",
             "Hoge rentes in Mexico trekken kortlopend carry-geld aan dat bij stress snel vertrekt; de peso is bovendien het referentieactivum voor alle handel en politieke nieuwsberichten tussen de VS en Mexico. Samen maakt dat hem liquide maar springerig — grote dagbewegingen zijn normaal, geen storing."),
            ("Wat is de goedkoopste manier om dollars naar Mexico te sturen?",
             "Gespecialiseerde overmakingsdiensten verslaan banken en contante transferwinkels op deze corridor steevast. Vergelijk het aangekomen bedrag met de middenkoers: bij een overboeking van 300 dollar kan het verschil tussen een eerlijke offerte en een marge van 5 procent een volledig dagloon ter plekke zijn."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD naar PHP — wisselkoers van vandaag en gratis omrekenaar voor de peso",
        "description": "Dollar naar Filipijnse peso omrekenen met live koersen: de USD/PHP-koers van vandaag, een gratis omrekenaar en wat de peso beweegt.",
        "h1": "USD naar PHP — Amerikaanse dollar naar Filipijnse peso omrekenen",
        "intro": [
            "De Filipijnse peso is verankerd in een van de grootste overmakingsstromen ter wereld: miljoenen Filipijnse arbeiders in het buitenland sturen geld naar huis, en die dollarinstroom is een pijler van de economie. USD/PHP handelt daarom op de wereldwijde risicobereidheid, olieprijzen (de Filipijnen zijn netto-importeur) en het beleid van de Bangko Sentral ng Pilipinas.",
            "De officiële koers wordt met een lichte hand beheerd — de centrale bank staat geleidelijke aanpassing toe en gladt pieken weg. Voor OFW-gezinnen en reizigers lopen de spreads tussen aanbieders op deze corridor breed uiteen, dus de middenkoers controleren vóór het versturen is de eenvoudigste besparing die er bestaat.",
        ],
        "faq": [
            ("Hoe beïnvloeden overmakingen de Filipijnse peso?",
             "Gestage dollarinstroom van arbeiders in het buitenland steunt de peso en de betalingsbalans — jaarlijks enkele procenten van het bbp. Wanneer het mondiale risico stijgt of gastlanden zwakker worden, laten de overmakingen na en volgt de peso doorgaans."),
            ("Is het beter om USD naar PHP om te rekenen in de VS of op de Filipijnen?",
             "Het hangt af van de aanbieder, niet van het land. Aan beide kanten van de corridor zijn goedkope en dure opties; het beslissende getal is hoeveel peso’s de ontvanger werkelijk krijgt. Vergelijk offertes met de middenkoers in plaats van de dichtstbijzijnde winkel te vertrouwen."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR naar GBP — actuele koers, omrekenaar en wat dit Europese paar beweegt",
        "description": "Euro naar Brits pond omrekenen met live koersen: de EUR/GBP-koers van vandaag, een gratis omrekenaar, bedragtabellen en wat dit paar beweegt.",
        "h1": "EUR naar GBP — euro naar Brits pond omrekenen",
        "intro": [
            "EUR/GBP is de klassieke Europese cross: twee economieën die ruwweg de helft van hun handel met elkaar doen, gescheiden door slechts één valutagrens. Omdat beide ontwikkelde, laaginflatie munten zijn, beweegt het paar veel minder dan dollarcrossen — in wezen is het een weddenschap op de relatieve fortuinen van de eurozone en het Verenigd Koninkrijk.",
            "De rentekloof tussen de ECB en de Bank of England stuurt het grootste deel van de trend, terwijl Brits politiek en begrotingsnieuws de pieken veroorzaken. Voor grensarbeiders, gepensioneerden en bedrijven maakt de stabiliteit van het paar kleine koersverschillen juist belangrijker: een marge van 1 procent is een groot deel van de totale jaarbeweging.",
        ],
        "faq": [
            ("Waarom is EUR/GBP rustiger dan EUR/USD?",
             "Noch de euro noch het pond is een mondiale risicomunt, dus wereldwijde vluchtbewegingen naar veiligheid passeren hen door. Het paar weerspiegelt vooral de relatieve economie van het VK en de EU en traag veranderende renteverschillen — al kan het hard uithalen op Brits politiek nieuws, zoals 2016 liet zien."),
            ("Hoe werkt de Brexit nog door in EUR/GBP?",
             "Structureel. Nieuwe handelsbelemmeringen sinds 2021 maakten de Britse economie iets minder open richting de EU, wat de meeste economen koppelen aan een structureel zwakker pond. Elke ronde van de VK-EU-onderhandelingen over handelsregels beweegt het paar nog steeds."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR naar CHF — wisselkoers van vandaag, gratis omrekenaar en de rol van de SNB",
        "description": "Euro naar Zwitserse frank omrekenen met live koersen: de EUR/CHF-koers van vandaag, een gratis omrekenaar en de rol van de SNB bij dit paar.",
        "h1": "EUR naar CHF — euro naar Zwitserse frank omrekenen",
        "intro": [
            "EUR/CHF is de lakmoesproef voor de veilige haven van Europa: zodra de stress in de eurozone toeneemt — de schuldencrisis van 2011, bankpaniek, oorlog op het continent — stroomt geld de Zwitserse grens over en daalt het paar. De Zwitserse Nationale Bank volgt deze koers nauwkeuriger dan enige andere en heeft herhaaldelijk ingegrepen om te voorkomen dat de frank de Zwitserse export verstikt.",
            "De moderne geschiedenis van het paar is dramatisch: een vloer op 1,20 vanaf 2011, toen het abrupte loslaten van die vloer in januari 2015, dat in minuten een flashcrash van 20–30 procent produceerde. Sindsdien handelt de frank als een schone, al soms te sterke toevlucht — en de SNB blijft een actieve speler op deze markt.",
        ],
        "faq": [
            ("Waarom doet de SNB zo veel om EUR/CHF?",
             "Omdat de Zwitserse economie naar Europa verkoopt. Een te sterke frank maakt Zwitserse exporteurs onconcurrentieel en drukt de inflatie onder het doel, dus koopt de SNB vreemde valuta (en legde ooit negatieve rente op) om de franksterkte te beteugelen. Ze grijpt in dit paar vaker in dan bijna elke andere centrale bank in een grote markt."),
            ("Is EUR/CHF een stabiel paar om aan te houden?",
             "Stabiel in rustige tijden en explosief in crises — het tegendeel van gespreid. Het loslaten van de vloer in 2015 blijft de standaardwaarschuwing dat de belofte van een centrale bank om een munt te plafonneren van de ene op de andere dag kan worden ingetrokken. Wie het paar als risicoloos behandelde, leerde het op één ochtend anders."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR naar PLN — actuele złoty-koers, omrekenaar en bedragtabellen",
        "description": "Euro naar Poolse złoty omrekenen met live koersen: de EUR/PLN-koers van vandaag, een gratis omrekenaar, bedragtabellen en wat de złoty beweegt.",
        "h1": "EUR naar PLN — euro naar Poolse złoty omrekenen",
        "intro": [
            "Polen is de zesde economie van de Europese Unie die nog met een eigen munt werkt, en de złoty is de meest verhandelde van de niet-euromunten van de unie. EUR/PLN handelt op de rentekloof met de Nationale Bank van Polen, op EU-middelen die naar het oosten stromen, op Duitse fabrieksorders voor de Poolse industrie en op het geopolitieke risico van de regio.",
            "Sinds Polen in 2004 tot de EU toetrad, won de złoty in boomperiodes en verloor hij hard in crises — 2008 en 2022 duwden het paar naar historische extremen. Nu de uiteindelijke invoering van de euro in Polen nog onbeslist is, blijft het paar nog jaren een structureel kenmerk van het Europese financiële stelsel.",
        ],
        "faq": [
            ("Zal Polen de euro invoeren en de złoty afschaffen?",
             "Polen is wettelijk verplicht uiteindelijk de euro in te voeren, maar heeft geen streefdatum, en de publieke opinie is sceptisch. Zolang er geen geloofwaardige tijdlijn bestaat, blijft EUR/PLN een actief verhandeld paar — politieke uitspraken over de planning kunnen hem al bewegen."),
            ("Waarom spoot EUR/PLN uit in 2022?",
             "De oorlog in buurland Oekraïne maakte Polen van de ene op de andere dag tot een fronteconomie: vluchtelingenstromen, defensie-uitgaven en energieschokken troffen de munt hard. De Nationale Bank van Polen greep in om de złoty te steunen — de scherpste bewegingen van het paar in twee decennia."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP naar JPY — wisselkoers van vandaag en omrekenaar voor dit volatiele paar",
        "description": "Brits pond naar Japanse yen omrekenen met live koersen: de GBP/JPY-koers van vandaag, een gratis omrekenaar en wat dit volatiele paar beweegt.",
        "h1": "GBP naar JPY — Brits pond naar Japanse yen omrekenen",
        "intro": [
            "GBP/JPY — oudere handelaren noemden het ‘het beest’ of ‘de draak’ — behoort tot de meest volatiele grote valutaparen. Het stapelt twee risicomotoren op elkaar: de gevoeligheid van sterling voor Brits politiek en begrotingsnieuws, en de rol van de yen als financieringsmunt van de wereld, die hem bij elke ommezwaai in het sentiment hard laat uithalen.",
            "Het paar is een lieveling van de carry trade: yen lenen tegen bijna nul rente om hoger renderende ponden te kopen. Dat werkt totdat een crisis iedereen dwingt tegelijk af te rollen — daarom klimt GBP/JPY jarenlang gestaag op en valt hij in weken gewelddadig. Positiegrootte en timing tellen hier meer dan bij vrijwel elk ander groot paar.",
        ],
        "faq": [
            ("Waarom is GBP/JPY volatieler dan USD/JPY?",
             "Omdat hij twee volatiliteiten vermenigvuldigt. Sterling legt het Britse politieke en economische risico bovenop het mondiale risicosentiment dat USD/JPY al aandrijft. Het paar heeft geen gedeelde ankereconomie en handelt daarom vrijwel puur op rentekloven en sentiment — ingrediënten voor grote bewegingen."),
            ("Wat is de carry trade in GBP/JPY?",
             "Yen lenen tegen de bijna-nulrente van Japan en beleggen in ponden tegen hogere Britse rente, om het verschil op te strijken. Het rendeert zolang de markten rustig zijn en bestraft hard wanneer dat niet zo: in risicoperiodes springt de yen omhoog wanneer carry-posities worden afgerold — vaak 10 procent of meer tegenover het pond in maanden."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD naar JPY — wisselkoers van vandaag, gratis omrekenaar en risicobarometer",
        "description": "Australische dollar naar yen omrekenen met live koersen: de AUD/JPY-koers van vandaag, een gratis omrekenaar, tabellen en risicouitleg.",
        "h1": "AUD naar JPY — Australische dollar naar Japanse yen omrekenen",
        "intro": [
            "AUD/JPY is de zuiverste risicobarometer van de valutamarkt. De Australische dollar staat voor mondiale groei en grondstoffenvraag — boven alles Chinese industriële vraag — terwijl de yen voor veiligheid staat. Draait de wereldeconomie, dan klimt het paar; bij paniek valt het sneller dan vrijwel elke andere grote cross.",
            "Het is tegelijk het klassieke carry trade-paar: decennia lang leenden beleggers goedkope yen om de hoger renderende Aussie te kopen. Die stroom vormt de lange, taaie opwaartse trends van het paar en zijn gewelddadige afwikkelingen — 2008 blijft het waarschuwende voorbeeld, toen AUD/JPY in enkele maanden ongeveer de helft van zijn waarde verloor.",
        ],
        "faq": [
            ("Waarom noemen handelaren AUD/JPY een risicobarometer?",
             "Omdat elke munt aan een tegenovergestelde pool zit: de Aussie stijgt met mondiale groei en grondstoffenvraag, de yen met angst. Het paar beweegt daardoor mee met de wereldbeurzen op een manier die weinig andere crossen evenaren — als het hard valt, is de risicoafkeer echt."),
            ("Wat gebeurde er met AUD/JPY in de crisis van 2008?",
             "Hij werd ongeveer gehalveerd. Toen het wereldwijde krediet bevroor, werd de carry trade afgerold: beleggers verkochten Australische dollars om geleende yen terug te betalen, en het paar stortte binnen enkele maanden van boven de 100 naar het lage bereik van 50. Het blijft het standaardvoorbeeld van hoe snel carry-strategieën omslaan."),
        ],
    },
}
