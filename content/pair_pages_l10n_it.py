# -*- coding: utf-8 -*-
"""Contenuti italiani per le pagine delle coppie di valute ("Da USD a EUR").

PAIR_UI_L10N corrisponde alle stringhe di pair_pages.PAIR_UI["en"] (i
segnaposto {f} {t} {d} restano invariati). PAIR_CONTENT_L10N corrisponde alle
15 coppie di PAIR_CONTENT["en"], con le stesse chiavi della versione inglese.
build-lang-pages.py unisce il tutto in PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Convertitore live",
    "pairRateHead": "Tasso di cambio attuale",
    "pairAsOf": "Tasso di riferimento al {d}. Il convertitore live qui sopra recupera sempre il tasso più recente — le tabelle qui sotto sono un'istantanea al momento della build, a solo scopo di orientamento.",
    "pairAmounts": "Importi comuni: {f} in {t}",
    "pairReverse": "Importi comuni: {t} in {f}",
    "pairMore": "Altre conversioni da {f}",
    "pairMorePairs": "Altre coppie di valute",
    "pairIntroHead": "Il tasso di cambio da {f} a {t}",
    "pairCurLinks": "Pagine delle valute",
    "pairMetaTmpl": ("Converti {f} in {t} con tassi di cambio live: il tasso {f}/{t} di oggi, una calcolatrice gratuita, "
                     "tabelle degli importi comuni e cosa muove questa coppia di valute."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "Da USD a EUR — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in euro con tassi live: il tasso di cambio USD/EUR di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove la coppia.",
        "h1": "Da USD a EUR — convertire dollari statunitensi in euro",
        "intro": [
            "USD/EUR è la coppia di valute più scambiata al mondo — circa un quarto di tutto il volume degli scambi valutari — ed è per questo che ha gli spread più stretti e il mercato più profondo di qualsiasi conversione. Il tasso è semplicemente il prezzo di un dollaro statunitense in euro, fissato di continuo dal commercio globale, dai flussi di investimento e dal differenziale dei tassi di interesse tra la Federal Reserve e la Banca Centrale Europea.",
            "Per le conversioni quotidiane la domanda pratica è quanto margine stai pagando oltre il tasso medio di mercato mostrato qui. Le banche aggiungono tipicamente l'1–4%; le carte e i servizi di trasferimento variano molto. Controllare il tasso live prima di un acquisto o di un trasferimento ti dice all'istante se una quotazione è equa.",
        ],
        "faq": [
            ("Come viene determinato il tasso di cambio da USD a EUR?",
             "Fluttua liberamente — domanda e offerta delle due valute fissano il prezzo giorno e notte, influenzate soprattutto dalla politica dei tassi della Fed e della BCE, dall'inflazione su entrambe le sponde dell'Atlantico e dal sentiment globale sul rischio. Non esiste un obiettivo fisso o amministrato."),
            ("Qual è il momento migliore per convertire da USD a EUR?",
             "La liquidità è più profonda e gli spread più stretti durante la sovrapposizione delle ore di negoziazione europee e americane (indicativamente 13:00–17:00 UTC). Nessuno può prevedere in modo affidabile la direzione a breve termine, quindi per importi elevati è più sicuro convertire in tranche che aspettare un giorno migliore."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "Da USD a GBP — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in sterline britanniche con tassi live: il tasso di cambio USD/GBP di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove la sterlina.",
        "h1": "Da USD a GBP — convertire dollari statunitensi in sterline britanniche",
        "intro": [
            "Il tasso tra dollaro e sterlina, soprannominato «cable» dal cavo telegrafico transatlantico che lo trasmise per la prima volta negli anni Sessanta dell'Ottocento, è una delle quotazioni di cambio più antiche ancora in uso continuo. Oggi riflette il differenziale dei tassi tra la Federal Reserve e la Bank of England, l'inflazione britannica e la salute del commercio e delle finanze pubbliche del Regno Unito.",
            "La sterlina si negozia più attivamente durante le ore londinesi, e la coppia è incline a bruschi movimenti in corrispondenza dei dati economici e degli annunci di politica fiscale britannici. Confrontare qualsiasi quotazione con il tasso medio di mercato qui sotto è il modo più rapido per vedere quanto margine trattiene un operatore.",
        ],
        "faq": [
            ("Perché la sterlina britannica vale più del dollaro statunitense?",
             "Un prezzo unitario più alto non significa un'economia più forte — riflette storia e tagli delle banconote. La sterlina era la valuta dominante del mondo quando il dollaro non esisteva ancora; il numero in sé non dice nulla sulla forza economica relativa o sul potere d'acquisto."),
            ("Cosa muove più di tutto USD/GBP?",
             "Le decisioni sui tassi della Fed e della Bank of England, i dati sull'inflazione britannica e le notizie politiche e fiscali da Westminster. Al referendum sulla Brexit del 2016 la sterlina cadde di circa il 10% in un giorno — un promemoria che la sterlina porta con sé un rischio politico che la maggior parte delle valute principali non ha."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "Da USD a JPY — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in yen giapponesi con tassi live: il tasso di cambio USD/JPY di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove lo yen.",
        "h1": "Da USD a JPY — convertire dollari statunitensi in yen giapponesi",
        "intro": [
            "USD/JPY è la seconda coppia di valute più scambiata al mondo e il classico barometro del differenziale dei tassi di interesse tra Stati Uniti e Giappone. Poiché i tassi giapponesi sono rimasti vicino allo zero per decenni, lo yen è diventato la valuta di finanziamento preferita del mondo — si indebolisce quando i mercati sono fiduciosi e si rafforza bruscamente quando le crisi smontano quelle posizioni.",
            "La coppia è osservata anche per gli interventi ufficiali giapponesi: il Ministero delle Finanze ha comprato ripetutamente yen quando si indeboliva troppo, troppo in fretta. Le conversioni importanti vanno verificate contro il tasso medio di mercato, perché i margini al dettaglio sul JPY possono essere ingannevolmente ampi.",
        ],
        "faq": [
            ("Perché a volte lo yen cade così tanto contro il dollaro?",
             "Soprattutto per il differenziale dei tassi. Quando i tassi americani sono alti e quelli giapponesi restano vicino allo zero, gli investitori vendono yen per comprare attività in dollari a rendimento più alto — è il carry trade. Lo yen può scivolare per mesi, poi saltare violentemente quando quelle posizioni si smontano."),
            ("Il governo giapponese può cambiare il tasso USD/JPY?",
             "Può opporsi al mercato, non invertirlo. Il Giappone è intervenuto comprando o vendendo yen quando i movimenti sono diventati disordinati, a volte con decine di miliardi di dollari in un'unica operazione. L'intervento smorza il percorso; raramente cambia la direzione di lungo periodo decisa dai fondamentali."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "Da USD a CNY — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in yuan cinesi con tassi live: il tasso di cambio USD/CNY di oggi, una calcolatrice gratuita, tabelle degli importi comuni e come funziona il tasso amministrato.",
        "h1": "Da USD a CNY — convertire dollari statunitensi in yuan cinesi",
        "intro": [
            "Il tasso tra dollaro e yuan è la più grande coppia di valute amministrata da una banca centrale. Ogni mattina la Banca Popolare Cinese fissa un fixing giornaliero, e il tasso onshore (CNY) può muoversi solo entro una fascia attorno a esso — per questo USD/CNY si muove molto meno giorno per giorno di quanto suggerirebbe la sua importanza economica.",
            "Il surplus commerciale della Cina, i controlli sui capitali e gli obiettivi di politica economica modellano tutti il tasso. Per le conversioni, ricorda che il CNY onshore e il CNH offshore possono differire leggermente, e che la conversione individuale di valuta in Cina è soggetta alle regole sui capitali. Confronta sempre le quotazioni con il tasso di riferimento qui sotto.",
        ],
        "faq": [
            ("Lo yuan cinese è liberamente convertibile?",
             "Non del tutto. La conversione legata al commercio è semplice, ma i flussi di investimento oltre confine sono controllati da quote e approvazioni. Per questo la versione offshore (CNH) si negozia a un prezzo leggermente diverso dal CNY onshore — il divario riflette quanto costa muovere denaro attraverso la frontiera."),
            ("Perché USD/CNY si muove pochissimo rispetto alle altre coppie?",
             "Perché lo amministra la banca centrale. Il fixing giornaliero e la fascia di negoziazione tengono il tasso stabile rispetto al dollaro, in linea con la preferenza cinese per la prevedibilità nel commercio. Amministrato non significa fisso: nei mesi e negli anni il tasso segue comunque i fondamentali."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "Da USD a INR — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in rupie indiane con tassi live: il tasso di cambio USD/INR di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove la rupia.",
        "h1": "Da USD a INR — convertire dollari statunitensi in rupie indiane",
        "intro": [
            "USD/INR è uno dei più importanti corridoi di rimesse al mondo — l'India riceve più rimesse di qualsiasi altro paese — e una coppia di mercato emergente molto scambiata. La Reserve Bank of India amministra la volatilità, non il livello: smorza i movimenti bruschi con le sue riserve ma lascia alla rupia trovare il suo trend di lungo periodo.",
            "La storia secolare della rupia è un graduale deprezzamento contro il dollaro, guidato dai differenziali di inflazione e dalla bilancia dei conti correnti dell'India, punteggiato da eventi di rischio globale. Per chi invia denaro in India, il vero costo si nasconde nel divario tra il tasso medio di mercato e il tasso offerto.",
        ],
        "faq": [
            ("Perché la rupia indiana si deprezza nel tempo?",
             "Soprattutto per i differenziali di inflazione e il deficit commerciale: l'India importa molto più di quanto esporti, e la differenza è finanziata dai flussi di capitale. La RBI smorza il percorso, ma nel corso dei decenni la rupia si è indebolita costantemente contro il dollaro — la norma per un'economia in via di sviluppo."),
            ("Come si ottiene il miglior tasso inviando denaro in India?",
             "Confronta il tasso offerto con il tasso medio di mercato prima di inviare, non solo le commissioni. I servizi di rimessa specializzati battono di solito i bonifici bancari su questo corridoio, e persino una differenza dell'1% è significativa sui trasferimenti familiari regolari nell'arco di un anno."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "Da USD a CAD — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in dollari canadesi con tassi live: il tasso di cambio USD/CAD di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove la Loonie.",
        "h1": "Da USD a CAD — convertire dollari statunitensi in dollari canadesi",
        "intro": [
            "USD/CAD — la «Loonie» — è una delle cinque coppie più scambiate al mondo, costruita su una delle più grandi relazioni commerciali della terra. Il Canada invia circa tre quarti delle sue esportazioni negli Stati Uniti, quindi la coppia si negozia pesantemente sulla crescita americana, sui prezzi dell'energia (il Canada è un grande esportatore di petrolio) e sul differenziale dei tassi tra la Fed e la Bank of Canada.",
            "Quando il petrolio sale, il CAD tipicamente si rafforza; quando colpiscono le paure per la crescita globale, si indebolisce con le valute legate alle materie prime in generale. La coppia è liquida giorno e notte, e quotazioni a una frazione di punto percentuale dal tasso medio di mercato sono facili da trovare — quindi i margini ampi sono sempre da mettere in discussione.",
        ],
        "faq": [
            ("Perché il dollaro canadese si chiama Loonie?",
             "Dallo loon — l'uccello raffigurato sulla moneta da un dollaro introdotta nel 1987. Il soprannome è rimasto e oggi nel gergo valutario indica la valuta stessa, come in «la Loonie oggi ha guadagnato terreno»."),
            ("Il prezzo del petrolio influenza davvero USD/CAD?",
             "Sì, in modo visibile. Il greggio e i prodotti correlati sono la più grande categoria di esportazione del Canada, quindi il petrolio in rialzo tende a portare più dollari in Canada e a sollevare il CAD. I trader trattano la coppia come un gioco approssimativo sui mercati dell'energia oltre che sui tassi dei due paesi."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "Da USD a AUD — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in dollari australiani con tassi live: il tasso di cambio USD/AUD di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove l'Aussie.",
        "h1": "Da USD a AUD — convertire dollari statunitensi in dollari australiani",
        "intro": [
            "Il dollaro australiano è la valuta legata alle materie prime per eccellenza: le sue fortune seguono le esportazioni di minerale di ferro, carbone e gas, e soprattutto la domanda cinese di questi beni. USD/AUD è quindi uno degli indicatori in tempo reale più puliti dell'appetito di rischio globale — l'Aussie si rafforza quando il commercio mondiale va a tutta velocità e si indebolisce nelle fasi di avversione al rischio.",
            "La politica dei tassi della Reserve Bank of Australia e della Fed guida le oscillazioni più brevi. Le popolazioni di working holiday e studenti dell'Australia rendono USD→AUD (e viceversa) una conversione ricorrente comune, dove persino un margine dell'1% sul tasso si accumula in fretta.",
        ],
        "faq": [
            ("Perché il dollaro australiano è così sensibile alla Cina?",
             "La Cina è il più grande mercato di esportazione dell'Australia con ampio margine, soprattutto per il minerale di ferro usato nella siderurgia. Quando l'edilizia cinese rallenta, i prezzi delle materie prime e l'AUD di solito cadono insieme — la valuta funziona da barometro in tempo reale dell'industria pesante cinese."),
            ("L'AUD è un rifugio sicuro?",
             "Il contrario: i trader la chiamano valuta risk-on. Nei panichi globali — 2008, 2020 — il denaro fluisce nei dollari statunitensi e l'Aussie tende a cadere più di tutte le valute principali. È proprio questa ciclicità il motivo per cui carry trader e osservatori della crescita la tengono d'occhio così da vicino."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "Da USD a CHF — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in franchi svizzeri con tassi live: il tasso di cambio USD/CHF di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove il franco.",
        "h1": "Da USD a CHF — convertire dollari statunitensi in franchi svizzeri",
        "intro": [
            "Il franco svizzero è il rifugio sicuro per eccellenza del mondo: quando colpiscono guerra, stress bancario o panico di mercato, il denaro fluisce in Svizzera e il CHF si rafforza. USD/CHF tende quindi a scendere nelle crisi globali persino quando il dollaro stesso è un rifugio — il franco è semplicemente il rifugio più forte.",
            "La Banca Nazionale Svizzera modella attivamente il tasso, dal famoso pavimento sull'euro del 2011–2015 agli interventi massicci di allora in poi. Per le conversioni, la Svizzera ricorda anche che una coppia di valute di un paese ricco può comunque portare ampi margini al dettaglio, soprattutto in aeroporti e hotel — controlla sempre il riferimento al tasso medio di mercato.",
        ],
        "faq": [
            ("Perché il franco svizzero è considerato un rifugio sicuro?",
             "Un secolo di neutralità, un debito basso, un surplus dei conti correnti e una banca centrale credibile fanno del franco il parcheggio predefinito per il denaro in fuga dal rischio. L'inflazione svizzera è inoltre rimasta per decenni ben al di sotto di quella americana ed eurozona, preservando il potere d'acquisto della valuta."),
            ("Che cosa ha fatto la SNB nel gennaio 2015?",
             "Ha abbandonato di colpo il tetto alla forza del franco contro l'euro. USD/CHF ed EUR/CHF sono crollati di circa il 20–30% nel giro di minuti — uno dei maggiori movimenti intraday mai visti su una coppia principale, e il motivo per cui i trader rispettano ancora l'espressione «rischio SNB»."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "Da USD a MXN — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in pesos messicani con tassi live: il tasso di cambio USD/MXN di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove il peso.",
        "h1": "Da USD a MXN — convertire dollari statunitensi in pesos messicani",
        "intro": [
            "USD/MXN è la coppia di mercato emergente più scambiata delle Americhe e una delle più liquide al mondo. Il peso si negozia su tutto ciò che muove l'economia statunitense — politica commerciale, crescita, differenziali dei tassi tra la Fed e Banxico — oltre ai prezzi del petrolio e all'enorme corridoio di rimesse dagli Stati Uniti.",
            "Essendo così liquida, la coppia reagisce in fretta al sentiment di rischio globale: è un classico obiettivo del carry trade che si rafforza nei mercati calmi e salta violentemente nei panichi. Per viaggiatori e chi invia rimesse, margini del 3–6% sono comuni negli aeroporti — il tasso medio di mercato qui sotto è il parametro di riferimento.",
        ],
        "faq": [
            ("Perché USD/MXN è così volatile?",
             "I tassi elevati in Messico attraggono denaro a breve termine del carry trade che lascia il paese rapidamente nello stress; il peso è anche l'attività di riferimento per tutto il commercio e le notizie politiche tra USA e Messico. La combinazione lo rende liquido ma nervoso — grandi movimenti giornalieri sono la norma, non un malfunzionamento."),
            ("Qual è il modo più economico di inviare dollari in Messico?",
             "I servizi di rimessa specializzati battono costantemente banche e sportelli di trasferimento in contanti su questo corridoio. Confronta l'importo consegnato con il tasso medio di mercato: su un trasferimento di 300 dollari, la differenza tra una quotazione equa e un margine del 5% può valere l'intero salario locale di un giorno."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "Da USD a PHP — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari statunitensi in pesos filippini con tassi live: il tasso di cambio USD/PHP di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove il peso.",
        "h1": "Da USD a PHP — convertire dollari statunitensi in pesos filippini",
        "intro": [
            "Il peso filippino è ancorato da uno dei maggiori flussi di rimesse del mondo: milioni di lavoratori filippini all'estero inviano denaro a casa, e quei flussi in dollari sono un pilastro dell'economia. USD/PHP di conseguenza si negozia sull'appetito di rischio globale, sui prezzi del petrolio (le Filippine sono importatori netti) e sulla politica della Bangko Sentral ng Pilipinas.",
            "Il tasso ufficiale è amministrato con mano leggera — la banca centrale consente un aggiustamento graduale smorzando i picchi. Per le famiglie degli OFW (i lavoratori filippini all'estero) e per i viaggiatori, lo spread tra operatori su questo corridoio è ampio, quindi controllare il tasso medio di mercato prima di inviare è il modo più semplice di risparmiare.",
        ],
        "faq": [
            ("Come incidono le rimesse sul peso filippino?",
             "I flussi costanti in dollari dei lavoratori all'estero sostengono il peso e la bilancia dei pagamenti del paese — parecchi punti percentuali del PIL ogni anno. Quando sale il rischio globale o si indeboliscono le economie ospiti, le rimesse si riducono e il peso tende a seguirle."),
            ("Conviene convertire da USD a PHP negli Stati Uniti o nelle Filippine?",
             "Dipende dall'operatore, non dal paese. Entrambe le sponde del corridoio hanno opzioni economiche e costose; il numero decisivo è quanti pesos riceve davvero il destinatario. Confronta le quotazioni con il tasso medio di mercato invece di fidarti dello sportello più vicino."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "Da EUR a GBP — Tasso di cambio, convertitore e tabelle",
        "description": "Converti euro in sterline britanniche con tassi live: il tasso di cambio EUR/GBP di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove questa coppia.",
        "h1": "Da EUR a GBP — convertire euro in sterline britanniche",
        "intro": [
            "EUR/GBP è il cross europeo classico: due economie che si scambiano circa metà del proprio commercio, separate da una sola frontiera valutaria. Poiché entrambe sono valute sviluppate a bassa inflazione, la coppia si muove molto meno dei cross sul dollaro — in realtà è una scommessa sulle fortune relative dell'eurozona e del Regno Unito.",
            "Il differenziale dei tassi tra BCE e Bank of England guida la maggior parte del trend, mentre le notizie politiche e fiscali britanniche provocano i picchi. Per i pendolari tra le due sponde della Manica, i pensionati e le imprese, la stabilità della coppia rende le piccole differenze di tasso ancora più importanti: un margine dell'1% è una gran parte dell'intero movimento annuale.",
        ],
        "faq": [
            ("Perché EUR/GBP è più tranquilla di EUR/USD?",
             "Né l'euro né la sterlina sono valute di rischio globale, quindi i grandi flussi verso la sicurezza le aggirano. La coppia riflette soprattutto l'economia relativa Regno Unito–UE e i differenziali dei tassi, che cambiano lentamente — anche se può dare picchi violenti sulle notizie politiche britanniche, come ha mostrato il 2016."),
            ("Come influisce ancora la Brexit su EUR/GBP?",
             "Strutturalmente. Le nuove frizioni commerciali dal 2021 hanno reso l'economia britannica un po' meno aperta all'UE, cosa che molti economisti collegano a una sterlina strutturalmente più debole. Ogni round di trattative Regno Unito–UE sulle regole commerciali muove comunque la coppia."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "Da EUR a CHF — Tasso di cambio, convertitore e tabelle",
        "description": "Converti euro in franchi svizzeri con tassi live: il tasso di cambio EUR/CHF di oggi, una calcolatrice gratuita, tabelle degli importi comuni e il ruolo della SNB.",
        "h1": "Da EUR a CHF — convertire euro in franchi svizzeri",
        "intro": [
            "EUR/CHF è la cartina al tornasole del rischio europeo: ogni volta che sale lo stress nell'eurozona — la crisi del debito del 2011, gli allarmi bancari, la guerra nel continente — il denaro attraversa la frontiera svizzera e la coppia scende. La Banca Nazionale Svizzera la osserva più da vicino di qualsiasi altro tasso, ed è intervenuta ripetutamente per impedire al franco di soffocare le esportazioni svizzere.",
            "La storia moderna della coppia è drammatica: un pavimento a 1,20 dal 2011, poi il depeg di gennaio 2015 che ha prodotto un flash crash del 20–30% in pochi minuti. Da allora il franco si negozia come un rifugio pulito, se a volte troppo forte — e la SNB resta un partecipante attivo di questo mercato.",
        ],
        "faq": [
            ("Perché la Banca Nazionale Svizzera tiene così tanto a EUR/CHF?",
             "Perché l'economia svizzera vende in Europa. Un franco troppo forte rende le esportazioni svizzere non competitive e trascina l'inflazione sotto obiettivo, quindi la SNB compra valuta estera (e un tempo ha impostato tassi negativi) per limitare la forza del franco. Interviene su questa coppia più di quasi qualsiasi altra banca centrale in un grande mercato."),
            ("EUR/CHF è una coppia stabile da tenere?",
             "È stabile nei tempi calmi ed esplosiva nelle crisi — l'opposto di un portafoglio diversificato. Il depeg del 2015 resta l'avvertimento da manuale che la promessa di una banca centrale di limitare una valuta può essere ritirata dall'oggi al domani. Chiunque la trattasse come priva di rischio ha imparato il contrario in una sola mattina."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "Da EUR a PLN — Tasso di cambio, convertitore e tabelle",
        "description": "Converti euro in zloty polacchi con tassi live: il tasso di cambio EUR/PLN di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove lo zloty.",
        "h1": "Da EUR a PLN — convertire euro in zloty polacchi",
        "intro": [
            "La Polonia è la sesta economia dell'Unione europea che usa ancora la propria valuta, e lo zloty è la più scambiata delle valute dell'UE fuori dall'euro. EUR/PLN si negozia sul differenziale dei tassi con la Banca Nazionale di Polonia, sui fondi UE che fluiscono verso est, sugli ordini delle fabbriche tedesche per l'industria polacca e sul rischio geopolitico regionale.",
            "Dal 2004, anno dell'adesione polacca all'UE, lo zloty si è rafforzato nei boom ed è caduto duramente nelle crisi — il 2008 e il 2022 hanno spinto la coppia a estremi storici. Con l'eventuale adozione dell'euro da parte della Polonia ancora indecisa, la coppia resterà una caratteristica strutturale della finanza europea per anni.",
        ],
        "faq": [
            ("La Polonia adotterà l'euro eliminando lo zloty?",
             "La Polonia è obbligata per legge ad aderire all'euro prima o poi, ma non ha una data obiettivo e il pubblico è molto scettico. Finché non esiste un calendario credibile di adozione, EUR/PLN resta una coppia attivamente scambiata — le dichiarazioni politiche sui tempi possono muoverla da sole."),
            ("Perché EUR/PLN è salita così bruscamente nel 2022?",
             "La guerra nell'Ucraina vicina ha reso la Polonia un'economia di prima linea dall'oggi al domani: afflussi di rifugiati, spese per la difesa e shock energetici hanno colpito duramente la valuta. La Banca Nazionale di Polonia è intervenuta a sostegno dello zloty — i movimenti più bruschi della coppia in due decenni."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "Da GBP a JPY — Tasso di cambio, convertitore e tabelle",
        "description": "Converti sterline britanniche in yen giapponesi con tassi live: il tasso di cambio GBP/JPY di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove questa coppia volatile.",
        "h1": "Da GBP a JPY — convertire sterline britanniche in yen giapponesi",
        "intro": [
            "GBP/JPY — i vecchi trader la chiamavano «la bestia» o «il drago» — è una delle coppie principali più volatili. Sovrappone due motori di rischio l'uno sull'altro: la sensibilità della sterlina alle notizie politiche e fiscali britanniche, e il ruolo dello yen come valuta di finanziamento del mondo, che la fa oscillare duramente ogni volta che il sentiment globale si gira.",
            "La coppia è la favorita del carry trade: prendere a prestito yen a tassi vicini allo zero per comprare sterline a rendimento più alto. Funziona finché una crisi non costringe tutti a smontare le posizioni insieme, ed è per questo che GBP/JPY tende a salire a fatica per anni e a cadere violentemente in settimane. Dimensioni e tempistiche contano qui più che in quasi qualsiasi altra coppia principale.",
        ],
        "faq": [
            ("Perché GBP/JPY è più volatile di USD/JPY?",
             "Perché moltiplica due volatilità. La sterlina aggiunge il rischio politico ed economico britannico al sentiment di rischio globale che già guida USD/JPY. La coppia non condivide un'ancora economica, quindi si negozia quasi solo su differenziali di tassi e sentiment — ingredienti per grandi movimenti."),
            ("Che cos'è il carry trade su GBP/JPY?",
             "Prendere a prestito yen ai tassi giapponesi vicini allo zero e investire in sterline a tassi britannici più alti, intascando la differenza. È redditizio finché i mercati sono calmi e punitivo quando non lo sono: nelle fasi di avversione al rischio lo yen aumenta mentre le posizioni carry si smontano, spesso del 10% o più contro la sterlina nel giro di mesi."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "Da AUD a JPY — Tasso di cambio, convertitore e tabelle",
        "description": "Converti dollari australiani in yen giapponesi con tassi live: il tasso di cambio AUD/JPY di oggi, una calcolatrice gratuita, tabelle degli importi comuni e cosa muove questo barometro del rischio.",
        "h1": "Da AUD a JPY — convertire dollari australiani in yen giapponesi",
        "intro": [
            "AUD/JPY è il barometro del rischio più puro del mercato valutario. Il dollaro australiano rappresenta la crescita globale e la domanda di materie prime — prima di tutto quella industriale cinese — mentre lo yen rappresenta la sicurezza. Quando l'economia mondiale si espande, la coppia sale; quando arriva il panico, cade più in fretta di quasi qualsiasi altro cross principale.",
            "È anche la coppia classica del carry trade: per decenni gli investitori hanno preso a prestito yen a basso costo per comprare l'Aussie, che rende di più. Quel flusso modella i lunghi trend ascendenti della coppia e i suoi episodi di smontaggio violento — il 2008 resta la storia ammonitiva, quando AUD/JPY perse circa metà del suo valore in pochi mesi.",
        ],
        "faq": [
            ("Perché i trader chiamano AUD/JPY un barometro del rischio?",
             "Perché ogni valuta sta a un polo opposto: l'Aussie sale con la crescita globale e la domanda di materie prime, lo yen sale con la paura. La coppia si muove quindi con i mercati azionari mondiali in misura che pochi altri cross eguagliano — quando cade duramente, il risk-off è reale."),
            ("Che cosa è successo ad AUD/JPY nella crisi del 2008?",
             "Ha perso circa la metà. Il carry trade si smontò mentre il credito globale si congelava: gli investitori vendettero dollari australiani per ripagare gli yen presi a prestito, e la coppia crollò da sopra 100 fino ai primi 50 nel giro di pochi mesi. Resta l'esempio standard di quanto rapidamente si invertano le strategie carry."),
        ],
    },
}
