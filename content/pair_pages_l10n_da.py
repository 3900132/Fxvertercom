# -*- coding: utf-8 -*-
"""Danish (da) currency-pair page copy — flat structure like the other l10n files."""

PAIR_UI_L10N = {'pairConvert': 'Live-omregner',
 'pairRateHead': 'Aktuel valutakurs',
 'pairAsOf': 'Referencekurs pr. {d}. Live-omregneren ovenfor henter altid den nyeste kurs – '
             'tabellerne nedenfor er et øjebliksbillede fra oprettelsestidspunktet til '
             'orientering.',
 'pairAmounts': 'Almindelige beløb: {f} til {t}',
 'pairReverse': 'Almindelige beløb: {t} til {f}',
 'pairMore': 'Flere {f}-konverteringer',
 'pairMorePairs': 'Flere valutapar',
 'pairIntroHead': 'Om valutakursen fra {f} til {t}',
 'pairCurLinks': 'Valutasider',
 'pairMetaTmpl': 'Omregn {f} til {t} med live-valutakurser: dagens {f}/{t}-kurs, en gratis '
                 'omregner, tabeller over almindelige beløb og hvad der flytter dette valutapar.'}

PAIR_CONTENT_L10N = {'USD-EUR': {'title': 'USD til EUR — valutakurs, omregner & tabeller',
             'description': 'Omregn amerikanske dollar til euro med live-kurser: dagens '
                            'USD/EUR-valutakurs, en gratis omregner, tabeller over almindelige '
                            'beløb og hvad der flytter paret.',
             'h1': 'USD til EUR — omregn amerikanske dollar til euro',
             'intro': ['USD/EUR er verdens mest handlede valutapar – omkring en fjerdedel af al '
                       'valutaomsætning – og har derfor de snævreste spread og det dybeste marked '
                       'af alle omregninger. Kursen er ganske enkelt prisen på én amerikansk '
                       'dollar i euro, fastsat løbende af global handel, investeringsstrømme og '
                       'rentespændet mellem Federal Reserve og Den Europæiske Centralbank.',
                       'Ved hverdagsomregninger er det praktiske spørgsmål, hvilken margen du '
                       'betaler over den viste midtkurs. Banker lægger typisk 1–4 % oveni; kort- '
                       'og overførselstjenester varierer meget. Tjekker du live-kursen, før du '
                       'køber eller overfører, ser du straks, om et tilbud er fair.'],
             'faq': [('Hvordan fastsættes USD/EUR-kursen?',
                      'Den flyder frit – udbud og efterspørgsel efter de to valutaer fastsætter '
                      "prisen døgnet rundt, påvirket først og fremmest af Fed's og ECB's "
                      'rentepolitik, inflationen på hver side af Atlanterhavet og den globale '
                      'risikostemning. Der findes ikke noget fast eller styret mål.'),
                     ('Hvornår er det bedste tidspunkt at omregne USD til EUR?',
                      'Likviditeten er størst og spreadene snævrest, når de europæiske og '
                      'amerikanske handelstider overlapper (ca. 13:00–17:00 UTC). Ingen kan '
                      'forudsige den kortsigtede retning pålideligt, så ved store beløb er det '
                      'sikrere at omregne i portioner end at vente på en bedre dag.')]},
 'USD-GBP': {'title': 'USD til GBP — valutakurs, omregner & pundet i bevægelse',
             'description': 'Omregn amerikanske dollar til britiske pund med live-kurser: dagens '
                            'USD/GBP-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter pundet.',
             'h1': 'USD til GBP — omregn amerikanske dollar til britiske pund',
             'intro': ['Kursen mellem dollar og pund, hos handlende kendt som ”cable” efter den '
                       "transatlantiske telegrafkabel, der første gang overførte den i 1860'erne, "
                       'hører til verdens ældste løbende noterede valutakurser. I dag afspejler '
                       'den rentespændet mellem Federal Reserve og Bank of England, den britiske '
                       'inflation og tilstanden i Storbritanniens handel og offentlige finanser.',
                       'Sterling handles mest aktivt i London-tiderne, og paret tenderer skarpe '
                       'bevægelser omkring britiske konjunkturtal og finanspolitiske meddelelser. '
                       'At sammenligne ethvert tilbud med midtkursen nedenfor er den hurtigste '
                       'måde at se, hvor stor en margen en udbyder tager.'],
             'faq': [('Hvorfor er det britiske pund mere værd end den amerikanske dollar?',
                      'En højere enhedspris betyder ikke en stærkere økonomi – den afspejler '
                      'historie og enhedsstørrelse. Pundet var verdens dominerende valuta, længe '
                      'før dollaren eksisterede; tallet selv siger intet om relativ økonomisk '
                      'styrke eller købekraft.'),
                     ('Hvad flytter USD/GBP mest?',
                      'Rentebeslutninger fra Fed og Bank of England, britiske inflationstal samt '
                      'politiske og finanspolitiske nyheder fra Westminster. Ved '
                      'Brexit-afstemningen i 2016 faldt pundet omkring 10 % på én dag – en '
                      'påmindelse om, at sterling bærer en politisk risiko, som de fleste store '
                      'valutaer ikke kender.')]},
 'USD-JPY': {'title': 'USD til JPY — valutakurs, omregner & yenen i bevægelse',
             'description': 'Omregn amerikanske dollar til japanske yen med live-kurser: dagens '
                            'USD/JPY-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter yenen.',
             'h1': 'USD til JPY — omregn amerikanske dollar til japanske yen',
             'intro': ['USD/JPY er verdens næstmest handlede valutapar og det klassiske mål for '
                       'rentespændet mellem USA og Japan. Da de japanske renter lå nær nul i '
                       'årtier, blev yenen verdens foretrukne finansieringsvaluta – den vakler, '
                       'når markederne er optimistiske, og rykker skarpt, når kriser ruller disse '
                       'positioner tilbage.',
                       'Paret følges også på grund af officielle japanske interventioner: '
                       'finansministeriet har gentagne gange købt yen, når den faldt for langt og '
                       'for hurtigt. Ved større omregninger gælder, at detailmarginerne på yen kan '
                       'være forbløffende brede, så sammenlign altid med midtkursen.'],
             'faq': [('Hvorfor falder yenen nogle gange så kraftigt mod dollaren?',
                      'Først og fremmest på grund af rentespændet. Er de amerikanske renter høje '
                      'og de japanske nær nul, sælger investorer yen for at købe højere afkastende '
                      'dollaraktiver – carry-traden. Yenen kan glide i måneder og derefter springe '
                      'voldsomt, når disse positioner lukkes.'),
                     ('Kan den japanske regering ændre USD/JPY-kursen?',
                      'Den kan modvirke markedet, ikke vende det. Japan har grebet ind ved at købe '
                      'eller sælge yen, når bevægelserne blev uordnede – sommetider for tocifrede '
                      'milliardbeløb i dollar i én enkelt episode. Interventioner udjævner vejen; '
                      'de ændrer sjældent fundamentets langsigtede retning.')]},
 'USD-CNY': {'title': 'USD til CNY — valutakurs, omregner & den styrede kurs',
             'description': 'Omregn amerikanske dollar til kinesiske yuan med live-kurser: dagens '
                            'USD/CNY-valutakurs, en gratis omregner, beløbstabeller og sådan '
                            'fungerer den styrede kurs.',
             'h1': 'USD til CNY — omregn amerikanske dollar til kinesiske yuan',
             'intro': ['Kursen mellem dollar og yuan er det største valutapar, en centralbank '
                       'styrer. Hver morgen fastsætter Kinas Folkebank en officiel referencekurs, '
                       'og den indenlandske kurs (CNY) må kun bevæge sig inden for et bånd omkring '
                       'den – derfor bevæger USD/CNY sig fra dag til dag langt mindre, end dets '
                       'økonomiske vægt kunne tyde på.',
                       'Kinas handelsoverskud, kapitalkontrollerne og politiske mål former alle '
                       'kursen. Ved omregninger gælder: den indenlandske CNY og den '
                       'offshore-handlede CNH kan afvige let, og privat valutaomregning i Kina '
                       'følger kapitalreglerne. Sammenlign altid tilbud med referencekursen '
                       'nedenfor.'],
             'faq': [('Er den kinesiske yuan frit konvertibel?',
                      'Ikke fuldt ud. Handelstilknyttet omregning er ukompliceret, men '
                      'investeringsstrømme over grænsen følger kvoter og godkendelser. Derfor '
                      'noterer den offshore-registrerede variant (CNH) sig lidt anderledes end den '
                      'indenlandske CNY – afstanden viser, hvor dyrt det er at flytte penge over '
                      'grænsen.'),
                     ('Hvorfor bevæger USD/CNY sig så lidt sammenlignet med andre par?',
                      'Fordi centralbanken styrer den. Den daglige referencekurs og handelsbåndet '
                      'holder kursen stabil mod dollaren, i tråd med Kinas præference for '
                      'forudsigelighed i handelen. Styret betyder ikke frossen: over måneder og år '
                      'følger kursen stadig fundamentet.')]},
 'USD-INR': {'title': 'USD til INR — valutakurs, omregner & rupien i bevægelse',
             'description': 'Omregn amerikanske dollar til indiske rupier med live-kurser: dagens '
                            'USD/INR-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter rupien.',
             'h1': 'USD til INR — omregn amerikanske dollar til indiske rupier',
             'intro': ['USD/INR er en af verdens vigtigste overførselskorridorer – Indien modtager '
                       'flere pengeoverførsler end noget andet land – og et stærkt handlet par på '
                       'fremvoksende markeder. Reserve Bank of India styrer volatiliteten, ikke '
                       'niveauet: den udjævner skarpe bevægelser med sine reserver men lader '
                       'rupien finde sin langsigtede retning.',
                       'Rupiens langsigtede historie er en gradvis svækkelse mod dollaren, drevet '
                       'af inflationsforskelle og Indiens handelsbalance, afbrudt af globale '
                       'risikohændelser. Den, der sender penge til Indien, finder de reelle '
                       'omkostninger i afstanden mellem midtkurs og tilbudskurs.'],
             'faq': [('Hvorfor mister den indiske rupee værdi over tid?',
                      'Først og fremmest på grund af inflationsforskelle og handelsunderskuddet: '
                      'Indien importerer langt mere, end det eksporterer, og forskellen '
                      'finansieres af kapitaltilstrømninger. RBI udjævner vejen, men over årtier '
                      'er rupien blevet støt svagere mod dollaren – normalt for en fremvoksende '
                      'økonomi.'),
                     ('Hvordan får man den bedste kurs, når man sender penge til Indien?',
                      'Sammenlign tilbudskursen med midtkursen, før du sender – ikke kun '
                      'gebyrerne. Specialiserede overførselstjenester slår typisk bankoverførslen '
                      'på denne korridor, og bare 1 % forskel gør sig mærkbar over et år med '
                      'tilbagevendende familieoverførsler.')]},
 'USD-CAD': {'title': 'USD til CAD — valutakurs, omregner & loonien i bevægelse',
             'description': 'Omregn amerikanske dollar til canadiske dollar med live-kurser: '
                            'dagens USD/CAD-valutakurs, en gratis omregner, beløbstabeller og hvad '
                            'der flytter loonien.',
             'h1': 'USD til CAD — omregn amerikanske dollar til canadiske dollar',
             'intro': ['USD/CAD – i FX-jargon ”loonie” – er et af verdens fem mest handlede par og '
                       'bygger på en af verdens største handelsrelationer. Canada sender omkring '
                       'tre fjerdedele af sin eksport til USA, så paret handler stærkt på '
                       'amerikansk vækst, energipriser (Canada er en betydelig olieeksportør) og '
                       'rentespændet mellem Fed og Bank of Canada.',
                       'Stiger olien, bliver CAD som regel stærkere; rammer globale '
                       'vækstbekymringer, vakler den sammen med råvarevalutaerne i deres helhed. '
                       'Paret er likvidt døgnet rundt, og tilbud inden for en brøkdel af en '
                       'procent fra midtkursen er lette at finde – brede marginer er derfor altid '
                       'et varsel.'],
             'faq': [('Hvorfor hedder den canadiske dollar loonie?',
                      'Efter islommen – fuglen på 1-dollar-mønten, der blev indført i 1987. '
                      'Kælenavnet blev hængende og betegner i FX-kredse i dag valutaen selv, som i '
                      '”loonien steg i dag”.'),
                     ('Påvirker olieprisen reelt USD/CAD?',
                      'Ja, mærkbart. Råolie og beslægtede produkter er Canadas største '
                      'eksportkategori, så stigende oliepriser bringer normalt flere dollars til '
                      'Canada og støtter CAD. Handlende behandler paret som et groft væddemål på '
                      'energimarkederne – oveni de to landes renter.')]},
 'USD-AUD': {'title': 'USD til AUD — valutakurs, omregner & aussien i bevægelse',
             'description': 'Omregn amerikanske dollar til australske dollar med live-kurser: '
                            'dagens USD/AUD-valutakurs, en gratis omregner, beløbstabeller og hvad '
                            'der flytter aussien.',
             'h1': 'USD til AUD — omregn amerikanske dollar til australske dollar',
             'intro': ['Den australske dollar er den klassiske råvarevaluta: dens skæbne hænger på '
                       'eksport af jernmalm, kul og gas og først og fremmest på Kinas '
                       'efterspørgsel efter dem. USD/AUD er dermed et af de reneste '
                       'realtidsbarometre for global risikovilje – aussien styrkes, når '
                       'verdenshandelen blomstrer, og svækkes i risikofaser.',
                       "Reserve Bank of Australia's og Fed's rentepolitik driver de kortere sving. "
                       'Australiens arbejds- og studiepopulationer gør USD→AUD (og tilbage) til en '
                       'hyppig, tilbagevendende omregning, hvor allerede 1 % kursmarge hurtigt '
                       'lægges sammen.'],
             'faq': [('Hvorfor reagerer den australske dollar så følsomt på Kina?',
                      'Kina er med god margin Australiens vigtigste eksportmarked, især for '
                      'jernmalm til stålproduktion. Køler den kinesiske byggebranche ned, falder '
                      'råvarepriser og AUD som regel sammen – valutaen fungerer som '
                      'realtidsbarometer for kinesisk tung industri.'),
                     ('Er AUD en sikker havn?',
                      'Tværtimod: handlende kalder den en risikovaluta. I globale panikker – 2008, '
                      '2020 – flyder penge ind i amerikanske dollar, og aussien falder typisk '
                      'hårdst blandt de store valutaer. Netop denne cyklik er grunden til, at '
                      'carry-handlende og vækstobservatører følger den så tæt.')]},
 'USD-CHF': {'title': 'USD til CHF — valutakurs, omregner & franken i bevægelse',
             'description': 'Omregn amerikanske dollar til schweiziske franc med live-kurser: '
                            'dagens USD/CHF-valutakurs, en gratis omregner, beløbstabeller og hvad '
                            'der flytter franken.',
             'h1': 'USD til CHF — omregn amerikanske dollar til schweiziske franc',
             'intro': ['Den schweiziske franc er verdens vigtigste sikre havn: ved krig, '
                       'bankstress eller markedspanik flyder penge ind i Schweiz, og CHF styrkes. '
                       'USD/CHF falder derfor ofte i globale kriser, selvom dollaren selv er et '
                       'tilflugtssted – franken er simpelthen det stærkere beskyttelsesrum.',
                       'Schweizerische Nationalbank former kursen aktivt – fra det berømte gulv på '
                       '1,20 mod euroen 2011–2015 til omfattende interventioner siden. Ved '
                       'omregninger minder Schweiz også om, at et rigt land ikke garanterer snævre '
                       'detailmarginer, især i lufthavne og på hoteller – brug altid midtkursen '
                       'som reference.'],
             'faq': [('Hvorfor anses den schweiziske franc for en sikker havn?',
                      'Et århundrede neutralitet, lav gæld, et overskud på betalingsbalancen og en '
                      'troværdig centralbank gør franken til standardstationen for penge på flugt '
                      "fra risiko. Den schweiziske inflation lå desuden i årtier langt under USA's "
                      'og euroområdets og bevarede valutaens købekraft.'),
                     ('Hvad gjorde SNB i januar 2015?',
                      'Den opgav brat sit gulv for francens styrke mod euroen. USD/CHF og EUR/CHF '
                      'brød sammen omkring 20–30 % på minutter – en af de største '
                      'intradag-bevægelser nogensinde på et stort par, og grunden til, at '
                      'handlende respekterer begrebet ”SNB-risiko” den dag i dag.')]},
 'USD-MXN': {'title': 'USD til MXN — valutakurs, omregner & pesoen i bevægelse',
             'description': 'Omregn amerikanske dollar til mexicanske pesos med live-kurser: '
                            'dagens USD/MXN-valutakurs, en gratis omregner, beløbstabeller og hvad '
                            'der flytter pesoen.',
             'h1': 'USD til MXN — omregn amerikanske dollar til mexicanske pesos',
             'intro': ['USD/MXN er Amerikas mest handlede par på fremvoksende markeder og et af '
                       "verdens mest likvide. Pesoen handler på alt, hvad USA's økonomi gør – "
                       'handelspolitik, vækst, rentespændet mellem Fed og Banxico – plus '
                       'oliepriser og den enorme overførselskorridor fra USA.',
                       'Fordi den er så likvid, reagerer paret hurtigt på den globale '
                       'risikostemning: et klassisk carry-trade-mål, der styrkes i rolige markeder '
                       'og bryder sammen brat i panikker. Rejsende og overførselsafsendere finder '
                       'ofte marginer på 3–6 % i lufthavnene – midtkursen nedenfor er målestokken '
                       'for sammenligning.'],
             'faq': [('Hvorfor er USD/MXN så volatil?',
                      'Høje renter i Mexico lokker kortvarige carry-penge til, der trækker sig '
                      'hurtigt ud i stress; samtidig er pesoen referenceaktivet for al handel og '
                      'politik mellem USA og Mexico. Tilsammen gør det den likvid, men hoppeparat '
                      '– store daglige sving er normalen, ikke en fejl.'),
                     ('Hvad er den billigste måde at sende dollars til Mexico på?',
                      'Specialiserede overførselstjenester slår regelmæssigt banker og '
                      'kontantoverførselsbutikker på denne korridor. Sammenlign det ankomne beløb '
                      'med midtkursen: ved en overførsel på 300 dollars kan forskellen mellem et '
                      'fair tilbud og en margen på 5 % svare til en hel dagsløn lokalt.')]},
 'USD-PHP': {'title': 'USD til PHP — valutakurs, omregner & pesoen i bevægelse',
             'description': 'Omregn amerikanske dollar til filippinske pesos med live-kurser: '
                            'dagens USD/PHP-valutakurs, en gratis omregner, beløbstabeller og hvad '
                            'der flytter pesoen.',
             'h1': 'USD til PHP — omregn amerikanske dollar til filippinske pesos',
             'intro': ['Den filippinske peso hviler på en af verdens største overførselsstrømme: '
                       'millioner af filippinere i udlandet sender penge hjem, og disse '
                       'dollarstrømme er en søjle i økonomien. USD/PHP handler derfor på den '
                       'globale risikostemning, oliepriserne (Filippinerne er nettoimportør) og '
                       "Bangko Sentral ng Pilipinas' politik.",
                       'Den officielle kurs styres med let hånd – centralbanken tillader gradvis '
                       'tilpasning og udjævner toppe. For OFW-familier og rejsende er '
                       'spread-forskellene på denne korridor brede, så et blik på midtkursen før '
                       'afsendelse er den nemmeste besparelse overhovedet.'],
             'faq': [('Hvordan påvirker pengeoverførsler den filippinske peso?',
                      'Jævne dollarstrømme fra arbejdere i udlandet støtter pesoen og '
                      'betalingsbalancen – hvert år flere procent af BNP. Stiger den globale '
                      'risiko eller vakler værtslandene, falder overførslerne, og pesoen følger '
                      'som regel med.'),
                     ('Er det bedre at veksle USD til PHP i USA eller på Filippinerne?',
                      'Det afhænger af udbyderen, ikke landet. På begge sider af korridoren findes '
                      'billige og dyre muligheder; afgørende er, hvor mange pesos der reelt '
                      'ankommer hos modtageren. Sammenlign tilbud med midtkursen i stedet for at '
                      'stole på den nærmeste butik.')]},
 'EUR-GBP': {'title': 'EUR til GBP — valutakurs, omregner & hvad der flytter paret',
             'description': 'Omregn euro til britiske pund med live-kurser: dagens '
                            'EUR/GBP-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter paret.',
             'h1': 'EUR til GBP — omregn euro til britiske pund',
             'intro': ['EUR/GBP er den klassiske europæiske krydskurs: to økonomier, der handler '
                       'omkring det halve af deres handel med hinanden, adskilt kun af en '
                       'valutagrænse. Da begge er udviklede lavinflationsvalutaer, bevæger paret '
                       'sig langt mindre end dollarkryds – i bund og grund er det et væddemål om '
                       'euroområdets og Storbritanniens relative skæbne.',
                       'Rentespændet mellem ECB og Bank of England driver størstedelen af trenden, '
                       'mens britiske politiske og finanspolitiske nyheder leverer udstikkene. For '
                       'grænsearbejdere, pensionister og virksomheder gør parets stabilitet selv '
                       'små kursforskelle vigtige: en margen på 1 % er en stor andel af hele '
                       'årsbevægelsen.'],
             'faq': [('Hvorfor er EUR/GBP roligere end EUR/USD?',
                      'Hverken euro eller pund er globale risikovalutaer, så verdensomspændende '
                      'flugt-til-sikkerhed-bevægelser passerer dem forbi. Paret afspejler først og '
                      "fremmest Storbritanniens og EU's relative økonomi samt renteforskelle, der "
                      'ændrer sig langsomt – selvom det kan udarte hårdt ved britiske '
                      'politinyheder, som 2016 viste.'),
                     ('Hvordan påvirker Brexit fortsat EUR/GBP?',
                      'Strukturelt. Nye handelshindringer siden 2021 gjorde den britiske økonomi '
                      'en anelse mindre åben over for EU, hvilket de fleste økonomer forbinder med '
                      'et strukturelt svagere pund. Hver runde af de britisk-europæiske '
                      'forhandlinger om handelsregler flytter paret den dag i dag.')]},
 'EUR-CHF': {'title': "EUR til CHF — valutakurs, omregner & SNB's rolle",
             'description': 'Omregn euro til schweiziske franc med live-kurser: dagens '
                            "EUR/CHF-valutakurs, en gratis omregner, beløbstabeller og SNB's rolle "
                            'ved dette par.',
             'h1': 'EUR til CHF — omregn euro til schweiziske franc',
             'intro': ['EUR/CHF er sikkerhavnen Europas lakmustest: Så snart stresset i '
                       'euroområdet stiger – gældskrisen 2011, bankpanik, krig på kontinentet – '
                       'flyder penge over den schweiziske grænse, og paret falder. Schweizerische '
                       'Nationalbank overvåger denne kurs nøjere end nogen anden og har grebet '
                       'gentagne gange ind, så franken ikke kvæler de schweiziske eksporter.',
                       'Parets moderne historie er dramatisk: et gulv ved 1,20 fra 2011, derefter '
                       'den bratte opgivelse af gulvet i januar 2015, der producerede et nedbrud '
                       'på 20–30 % på minutter. Siden har franken handlet som ren, om end til '
                       'tider for stærk tilflugt – og SNB forbliver en aktiv deltager på dette '
                       'marked.'],
             'faq': [('Hvorfor interesserer SNB sig så meget for EUR/CHF?',
                      'Fordi den schweiziske økonomi sælger til Europa. En alt for stærk frank gør '
                      'schweiziske eksporter uattraktive og trækker inflationen under målet, så '
                      'SNB køber fremmed valuta (og indførte engang negative renter) for at dæmpe '
                      'frankstyrken. Den griber ind i dette par oftere end næsten enhver anden '
                      'centralbank i et stort marked.'),
                     ('Er EUR/CHF et stabilt par at holde?',
                      'Stabilt i rolige tider, eksplosivt i kriser – det modsatte af '
                      'diversificeret. Opgivelsen af gulvet i 2015 forbliver lærebogsadvarslen om, '
                      'at en centralbanks løfte om at dæmpe en valuta kan trækkes tilbage natten '
                      'over. Den, der holdt paret for risikofrit, lærte det anderledes en enkelt '
                      'formiddag.')]},
 'EUR-PLN': {'title': 'EUR til PLN — valutakurs, omregner & zlotyen i bevægelse',
             'description': 'Omregn euro til polske zloty med live-kurser: dagens '
                            'EUR/PLN-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter zlotyen.',
             'h1': 'EUR til PLN — omregn euro til polske zloty',
             'intro': ["Polen er EU's sjette største økonomi med egen valuta, og zlotyen er den "
                       'mest handlede af unionens ikke-euro-valutaer. EUR/PLN handler på '
                       'rentespændet til National Bank of Poland, på EU-midler, der flyder østpå, '
                       'på tyske fabriksordrer til polsk industri og på regionens geopolitiske '
                       'risiko.',
                       'Siden Polens EU-indtræden i 2004 har zlotyen vundet i boomer og tabt hårdt '
                       'i kriser – 2008 og 2022 drev paret til historiske ekstremer. Eftersom '
                       'Polens kommende euroindførelse fortsat er åben, forbliver paret i årevis '
                       'en strukturel del af det europæiske finanssystem.'],
             'faq': [('Vil Polen indføre euroen og afskaffe zlotyen?',
                      'Polen er juridisk forpligtet til en skønne at indføre euroen, men har ingen '
                      'måldato, og befolkningen er skeptisk. Så længe der ikke findes en troværdig '
                      'tidsplan, forbliver EUR/PLN et aktivt handlet par – selv politiske '
                      'udtalelser om tidshorisonten kan flytte det alene.'),
                     ('Hvorfor udartede EUR/PLN sig i 2022?',
                      'Krigen i nabolandet Ukraine gjorde Polen til en grænseøkonomi fra den ene '
                      'dag til den anden: flygtningestrømme, forsvarsudgifter og energichok ramte '
                      'valutaen hårdt. National Bank of Poland greb ind for at støtte zlotyen – '
                      'parets skarpeste bevægelser i to årtier.')]},
 'GBP-JPY': {'title': 'GBP til JPY — valutakurs, omregner & det volatile par',
             'description': 'Omregn britiske pund til japanske yen med live-kurser: dagens '
                            'GBP/JPY-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter det volatile par.',
             'h1': 'GBP til JPY — omregn britiske pund til japanske yen',
             'intro': ['GBP/JPY – gamle handlende kaldte den ”bæstet” eller ”dragen” – er et af de '
                       'mest volatile store valutapar. Den stablet to risikomotorer oven på '
                       'hinanden: sterlings følsomhed over for britisk politik og finans, og '
                       'yenens rolle som verdens finansieringsvaluta, som får den til at udbryde '
                       'voldsomt ved hver stemningsvending.',
                       'Paret er en favorit i carry-traden: låne yen til renter nær nul for at '
                       'købe højere afkastende pund. Det virker, indtil en krise tvinger alle til '
                       'at lukke samtidig – derfor klatrer GBP/JPY i årevis og falder voldsomt på '
                       'uger. Positionsstørrelse og timing tæller her mere end ved næsten ethvert '
                       'andet stort par.'],
             'faq': [('Hvorfor er GBP/JPY mere volatil end USD/JPY?',
                      'Fordi den ganger to volatiliteter. Sterling lægger britisk politik og '
                      'konjunkturrisiko oven på den globale risikostemning, der i forvejen driver '
                      'USD/JPY. Paret har ingen fælles ankerøkonomi og handler derfor næsten '
                      'udelukkende på rentespænd og stemning – ingredienser til store bevægelser.'),
                     ('Hvad er carry-traden i GBP/JPY?',
                      'At låne yen til japanske renter nær nul og investere i højere afkastende '
                      'pund for at høste forskellen. Det betaler sig, så længe markederne er '
                      'rolige, og straffer hårdt, når de ikke er: i risikofaser springer yenen, '
                      'når carry-positioner lukkes – ofte 10 % og mere mod pundet på måneder.')]},
 'AUD-JPY': {'title': 'AUD til JPY — valutakurs, omregner & risikobarometer',
             'description': 'Omregn australske dollar til japanske yen med live-kurser: dagens '
                            'AUD/JPY-valutakurs, en gratis omregner, beløbstabeller og hvad der '
                            'flytter risikobarometeret.',
             'h1': 'AUD til JPY — omregn australske dollar til japanske yen',
             'intro': ['AUD/JPY er i sin reneste form FX-markedets risikobarometer. Den australske '
                       'dollar står for global vækst og råvareefterspørgsel – først og fremmest '
                       'kinesisk industri – mens yenen står for sikkerhed. Kører verdensøkonomien, '
                       'klatrer paret; ved panik falder det hurtigere end næsten ethvert andet '
                       'stort krydskurs.',
                       'Det er samtidig det klassiske carry-trade-par: i årtier lånte investorer '
                       'billige yen for at købe den højere afkastende aussie. Denne strøm former '
                       'parets lange, sejlivede opgangstrends og dets voldsomme afviklinger – 2008 '
                       'forbliver advarselseksemplet, da AUD/JPY mistede omkring det halve på få '
                       'måneder.'],
             'faq': [('Hvorfor kalder handlende AUD/JPY et risikobarometer?',
                      'Fordi hver valuta sidder ved en modsat pol: aussien stiger med global vækst '
                      'og råvareefterspørgsel, yenen med frygt. Paret bevæger sig derfor med '
                      'verdens aktiemarkeder som få andre krydskurser – falder det hårdt, er '
                      'risikoafvisningen reel.'),
                     ('Hvad skete der med AUD/JPY i krisen 2008?',
                      'Den blev næsten halveret. Da den globale kredit frøs, blev carry-traden '
                      'afviklet: investorer solgte australske dollar for at tilbagebetale lånte '
                      "yen, og paret styrtede fra over 100 til de lave 50'ere på måneder. Det "
                      'forbliver standardeksemplet på, hvor hurtigt carry-strategier vælter.')]}}
