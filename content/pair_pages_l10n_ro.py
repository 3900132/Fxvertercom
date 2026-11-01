# -*- coding: utf-8 -*-
"""Conținut românesc (ro) pentru paginile de perechi valutare („USD în EUR”).

PAIR_UI_L10N corespunde șirurilor de schelet din pair_pages.PAIR_UI pentru
limba engleză (placeholder-ele {f} {t} {d} rămân nemodificate).
PAIR_CONTENT_L10N corespunde celor 15 perechi din PAIR_CONTENT pentru engleză,
cu chei identice. build-lang-pages.py le îmbină în PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Convertor live",
    "pairRateHead": "Cursul valutar actual",
    "pairAsOf": "Curs de referință la data de {d}. Convertorul live de mai sus preia mereu cel mai nou curs — tabelele de mai jos sunt o imagine la momentul generării, pentru orientare.",
    "pairAmounts": "Sume uzuale: {f} în {t}",
    "pairReverse": "Sume uzuale: {t} în {f}",
    "pairMore": "Mai multe conversii {f}",
    "pairMorePairs": "Mai multe perechi valutare",
    "pairIntroHead": "Despre cursul {f}/{t}",
    "pairCurLinks": "Pagini ale valutelor",
    "pairMetaTmpl": ("Convertește {f} în {t} cu cursuri valutare live: cursul {f}/{t} de azi, un calculator gratuit, "
                     "tabele de sume uzuale și ce mișcă această pereche valutară."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD în EUR — cursul de schimb dolar american–euro și convertor",
        "description": "Convertește dolari americani în euro cu cursuri live: cursul USD/EUR de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă această pereche.",
        "h1": "USD în EUR — convertește dolari americani în euro",
        "intro": [
            "USD/EUR este cea mai tranzacționată pereche valutară din lume — aproximativ un sfert din totalul cifrei de afaceri valutare — de aceea are cele mai strânse spread-uri și cea mai adâncă piață dintre toate conversiile. Cursul este pur și simplu prețul unui dolar american în euro, stabilit continuu de comerțul global, de fluxurile de investiții și de diferența de dobândă dintre Rezerva Federală și Banca Centrală Europeană.",
            "La conversiile de zi cu zi, întrebarea practică este ce marjă plătești peste cursul mid-market afișat aici. Băncile adaugă de obicei 1–4%; serviciile de card și de transfer variază mult. Verificarea cursului live înaintea unei achiziții sau a unui transfer îți spune imediat dacă o ofertă este corectă.",
        ],
        "faq": [
            ("Cum se stabilește cursul USD în EUR?",
             "Flotează liber — cererea și oferta celor două monede stabilesc prețul non-stop, influențate mai ales de politica de dobânzi a Fed și a BCE, de inflația de ambele părți ale Atlanticului și de sentimentul global de risc. Nu există niciun obiectiv fix sau administrat."),
            ("Care este cel mai bun moment pentru a converti USD în EUR?",
             "Lichiditatea este cea mai adâncă, iar spread-urile cele mai strânse în suprapunerea orelor de tranzacționare europene și americane (aproximativ 13:00–17:00 UTC). Nimeni nu poate prezice în mod credibil direcția pe termen scurt, deci pentru sume mari este mai sigur să convertești în tranșe decât să aștepți o zi mai bună."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD în GBP — cursul de schimb dolar american–liră sterlină și convertor",
        "description": "Convertește dolari americani în lire sterline cu cursuri live: cursul USD/GBP de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă lira.",
        "h1": "USD în GBP — convertește dolari americani în lire sterline",
        "intro": [
            "Cursul dolar–liră, poreclit „cable” după cablul telegrafic transatlantic care l-a purtat prima dată în anii 1860, este unul dintre cele mai vechi cursuri cotate continuu din lume. Astăzi reflectă diferența de dobândă dintre Rezerva Federală și Bank of England, inflația britanică și starea comerțului și a finanțelor publice ale Regatului Unit.",
            "Sterlina se tranzacționează cel mai activ în orele londoneze, iar perechea e predispusă la mișcări bruște în jurul datelor economice și al anunțurilor fiscale britanice. Compararea oricărei oferte cu cursul mid-market de mai jos este calea cea mai rapidă de a vedea cât de multă marjă ia un furnizor.",
        ],
        "faq": [
            ("De ce lira sterlină valorează mai mult decât dolarul american?",
             "Un preț unitar mai mare nu înseamnă o economie mai puternică — reflectă istoria și denominațiile. Lira era moneda dominantă a lumii când dolarul nici nu exista; cifra în sine nu spune nimic despre forța economică relativă sau despre puterea de cumpărare."),
            ("Ce mișcă USD/GBP cel mai mult?",
             "Deciziile de dobândă ale Fed și ale Bank of England, datele de inflație britanice și știrile politice și fiscale de la Westminster. La votul pentru Brexit din 2016, lira a căzut cu circa 10% într-o zi — un memento că sterlina poartă un risc politic pe care majoritatea valutelor majore nu-l poartă."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD în JPY — cursul de schimb dolar american–yen japonez și convertor",
        "description": "Convertește dolari americani în yeni japonezi cu cursuri live: cursul USD/JPY de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă yenul.",
        "h1": "USD în JPY — convertește dolari americani în yeni japonezi",
        "intro": [
            "USD/JPY este a doua pereche valutară ca tranzacționare din lume și barometrul clasic al diferenței de dobândă dintre Statele Unite și Japonia. Cum ratele japoneze au stat decenii aproape de zero, yenul a devenit moneda de finanțare favorită a lumii — se slăbește când piețele sunt încrezătoare și se întărește abrupt când crizele demontează aceste poziții.",
            "Perechea este urmărită și pentru intervențiile oficiale japoneze: Ministerul de Finanțe a cumpărat de repetate ori yeni când aceștia se slăbeau prea mult, prea repede. Conversiile mari se verifică cel mai bine împotriva cursului mid-market, deoarece marjele de retail pe JPY pot fi înșelător de late.",
        ],
        "faq": [
            ("De ce cade yenul uneori atât de mult față de dolar?",
             "În principal din cauza diferenței de dobândă. Când ratele americane sunt ridicate, iar cele japoneze rămân aproape de zero, investitorii vinde yeni ca să cumpere active în dolari cu randament mai mare — carry trade-ul. Yenul poate aluneca luni de zile, apoi să sară violent când aceste poziții se demontează."),
            ("Poate guvernul japonez să schimbe cursul USD/JPY?",
             "Poate să reziste pieței, nu să-l inverseze. Japonia a intervenit cumpărând sau vânzând yeni când mișcările deveneau dezordonate, uneori cu zeci de miliarde de dolari într-un singur episod. Intervenția netezește traiectoria; direcția pe termen lung, stabilită de fundamente, o schimbă rar."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD în CNY — cursul de schimb dolar american–yuan chinezesc și convertor",
        "description": "Convertește dolari americani în yuani chinezești cu cursuri live: cursul USD/CNY de azi, un calculator gratuit, tabele de sume uzuale și cursul administrat.",
        "h1": "USD în CNY — convertește dolari americani în yuani chinezești",
        "intro": [
            "Cursul dolar–yuan este cea mai mare pereche valutară administrată de o bancă centrală. În fiecare dimineață, Banca Populară a Chinei stabilește o paritate centrală zilnică, iar cursul onshore (CNY) se poate mișca doar într-o bandă în jurul ei — de aceea USD/CNY se mișcă mult mai puțin de la o zi la alta decât ar sugera importanța sa economică.",
            "Excedentul comercial al Chinei, controalele de capital și obiectivele de politică modelează toate cursul. La conversii, reține că CNY onshore și CNH offshore pot diferi ușor și că conversia valutară a persoanelor fizice în China se supune regulilor de control al capitalului. Compară întotdeauna ofertele cu cursul de referință de mai jos.",
        ],
        "faq": [
            ("Yuanul chinezesc este liber convertibil?",
             "Nu complet. Conversia legată de comerț este simplă, dar fluxurile de investiții peste graniță sunt controlate prin cote și aprobări. De aceea varianta offshore (CNH) se tranzacționează la un preț ușor diferit de CNY onshore — decalajul arată cât costă mutarea banilor peste graniță."),
            ("De ce abia se mișcă USD/CNY în comparație cu alte perechi?",
             "Pentru că banca centrală îl administrează. Paritatea zilnică și banda de tranzacționare mențin cursul stabil față de dolar, în acord cu preferința Chinei de previzibilitate în comerț. Administrat nu înseamnă fix: cursul urmează totuși fundamentele pe parcursul lunilor și anilor."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD în INR — cursul de schimb dolar american–rupie indiană și convertor",
        "description": "Convertește dolari americani în rupii indiene cu cursuri live: cursul USD/INR de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă rupia.",
        "h1": "USD în INR — convertește dolari americani în rupii indiene",
        "intro": [
            "USD/INR este unul dintre cele mai importante coridoare de transferuri din lume — India primește mai multe transferuri decât orice altă țară — și o pereche puternic tranzacționată de piață emergentă. Reserve Bank of India administrează volatilitatea, nu nivelul: netezește mișcările bruște cu rezervele sale, dar lasă rupia să-și găsească trendul pe termen lung.",
            "Povestea seculară a rupiei este deprecierea treptată față de dolar, condusă de diferențele de inflație și de balanța de cont curent a Indiei, întreruptă de evenimentele globale de risc. Pentru oricine trimite bani în India, decalajul dintre cursul mid-market și cursul oferit este locul unde se ascunde costul real.",
        ],
        "faq": [
            ("De ce se depreciază rupia indiană în timp?",
             "În principal din cauza diferențelor de inflație și a deficitului comercial: India importă mult mai mult decât exportă, iar diferența se finanțează din afluxuri de capital. RBI netezește drumul, dar de-a lungul deceniilor rupia s-a slăbit constant față de dolar — un fenomen normal pentru o economie în dezvoltare."),
            ("Cum obții cel mai bun curs când trimiți bani în India?",
             "Compară cursul oferit cu cel mid-market înainte de a trimite, nu doar comisioanele. Serviciile specializate de transfer bat de regulă transferul bancar pe acest coridor, iar o diferență de chiar 1% contează mult la transferuri familiale regulate, pe un an."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD în CAD — cursul de schimb dolar american–dolar canadian și convertor",
        "description": "Convertește dolari americani în dolari canadieni cu cursuri live: cursul USD/CAD de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă loonie-ul.",
        "h1": "USD în CAD — convertește dolari americani în dolari canadieni",
        "intro": [
            "USD/CAD — „loonie” — se află printre primele cinci perechi valutare din lume și se sprijină pe una dintre cele mai mari relații comerciale de pe planetă. Canada trimite circa trei sferturi din exporturile sale în Statele Unite, deci perechea se tranzacționează puternic pe creșterea americană, pe prețurile energiei (Canada este un exportator major de petrol) și pe diferența de dobândă dintre Fed și Bank of Canada.",
            "Când petrolul urcă, CAD se întărește de regulă; când teama de încetinire globală lovește, se slăbește odată cu monedele de materii prime în general. Perechea este lichidă non-stop, iar oferte aflate la o fracțiune de procent de cursul mid-market se găsesc ușor — deci o marjă lată merită întotdeauna pusă la îndoială.",
        ],
        "faq": [
            ("De ce dolarul canadian se numește loonie?",
             "După loon — pasărea de pe moneda de un dolar introdusă în 1987. Porecla a prins și se referă astăzi la moneda în sine în argoul valutar, precum în „loonie-ul s-a întărit azi”."),
            ("Prețul petrolului influențează într-adevăr USD/CAD?",
             "Da, vizibil. Țițeiul și produsele conexe sunt cea mai mare categorie de export a Canadei, deci petrolul în creștere aduce de regulă mai mulți dolari în Canada și ridică CAD. Traderii tratează perechea și ca un pariu aproximativ pe piețele energetice, nu doar pe ratele celor două țări."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD în AUD — cursul de schimb dolar american–dolar australian și convertor",
        "description": "Convertește dolari americani în dolari australieni cu cursuri live: cursul USD/AUD de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă aussie-ul.",
        "h1": "USD în AUD — convertește dolari americani în dolari australieni",
        "intro": [
            "Dolarul australian este moneda clasică de materii prime: soarta sa urmărește exporturile de minereu de fier, cărbune și gaz și, mai ales, cererea chineză pentru ele. USD/AUD este deci unul dintre cei mai curați indicatori în timp real ai apetitului global pentru risc — aussie-ul se întărește când comerțul mondial merge bine și se slăbește în episoadele de evitare a riscului.",
            "Politica de dobânzi a Reserve Bank of Australia și a Fed conduce oscilațiile pe termen mai scurt. Populațiile de tineri în working holiday și de studenți fac USD→AUD (și înapoi) o conversie recurentă frecventă, unde chiar o marjă de curs de 1% se compune repede.",
        ],
        "faq": [
            ("De ce dolarul australian e atât de sensibil la China?",
             "China este de departe cel mai mare piață de export a Australiei, mai ales pentru minereul de fier folosit în siderurgie. Când construcțiile chineze încetinesc, prețurile materiilor prime și AUD cad de obicei împreună — moneda funcționează ca barometru în timp real al industriei grele chineze."),
            ("AUD este un refugiu sigur?",
             "Dimpotrivă: traderii îl numesc monedă risk-on. În panici globale — 2008, 2020 — banii curg spre dolari americani, iar aussie-ul tinde să cadă cel mai puternic dintre valutele majore. Exact această ciclicită face ca traderii de carry și cei care urmăresc creșterea să-l țină atent sub observație."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD în CHF — cursul de schimb dolar american–franc elvețian și convertor",
        "description": "Convertește dolari americani în franci elvețieni cu cursuri live: cursul USD/CHF de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă francul.",
        "h1": "USD în CHF — convertește dolari americani în franci elvețieni",
        "intro": [
            "Francul elvețian este primul refugiu sigur al lumii: când lovesc războiul, stresul bancar sau panica pieței, banii curg spre Elveția și CHF se întărește. USD/CHF tinde deci să scadă în crizele globale chiar și atunci când dolarul însuși e un adăpost — francul este pur și simplu adăpostul mai puternic.",
            "Banca Națională Elvețiană modelează activ cursul, de la celebrul podea de 1,20 față de euro din 2011–2015 până la intervențiile masive de după. La conversii, Elveția amintește și că o pereche a unei țări bogate poate totuși avea marje de retail late, mai ales la aeroporturi și hoteluri — verifică întotdeauna referința mid-market.",
        ],
        "faq": [
            ("De ce francul elvețian e considerat refugiu sigur?",
             "Un secol de neutralitate, datorie mică, excedent de cont curent și o bancă centrală credibilă fac din franc locul implicit de parcare pentru banii care fug de risc. Inflația elvețiană a rămas, de asemenea, cu mult sub cea din SUA și din zona euro decenii la rând, păstrând puterea de cumpărare a monedei."),
            ("Ce a făcut SNB în ianuarie 2015?",
             "A abandonat brusc plafonul asupra forței francului față de euro. USD/CHF și EUR/CHF s-au prăbușit cu aproximativ 20–30% în câteva minute — una dintre cele mai mari mișcări intraday ale unei perechi majore, și motivul pentru care traderii respectă și astăzi expresia „risc SNB”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD în MXN — cursul de schimb dolar american–peso mexican și convertor",
        "description": "Convertește dolari americani în pesos mexicani cu cursuri live: cursul USD/MXN de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă peso-ul.",
        "h1": "USD în MXN — convertește dolari americani în pesos mexicani",
        "intro": [
            "USD/MXN este cea mai tranzacționată pereche de piață emergentă din Americi și una dintre cele mai lichide din lume. Peso-ul se tranzacționează pe orice mișcă economia americană — politica comercială, creșterea, diferența de dobândă dintre Fed și Banxico — plus prețurile petrolului și coridorul uriaș de transferuri din Statele Unite.",
            "Fiind atât de lichidă, perechea se mișcă repede pe sentimentul global de risc: țintă clasică de carry trade, se întărește în piețe calme și cade brusc în panici. Pentru călători și expeditori de transferuri, marje de 3–6% sunt frecvente la aeroporturi — cursul mid-market de mai jos este reperul cu care se compară.",
        ],
        "faq": [
            ("De ce este USD/MXN atât de volatil?",
             "Ratele ridicate din Mexic atrag bani de carry pe termen scurt, care pleacă repede în perioade de stres; peso-ul este și activul de referință pentru tot comerțul și știrile politice SUA–Mexic. Combinația îl face lichid, dar nervos — mișcările zilnice mari sunt normale, nu o defecțiune."),
            ("Care este cel mai ieftin mod de a trimite dolari în Mexic?",
             "Serviciile specializate de transfer bat constant băncile și ghișeele de transfer în numerar pe acest coridor. Compară suma livrată cu cursul mid-market: la un transfer de 300 de dolari, diferența dintre o ofertă corectă și o marjă de 5% poate fi un salariu zilnic local întreg."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD în PHP — cursul de schimb dolar american–peso filipinez și convertor",
        "description": "Convertește dolari americani în pesos filipinezi cu cursuri live: cursul USD/PHP de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă peso-ul.",
        "h1": "USD în PHP — convertește dolari americani în pesos filipinezi",
        "intro": [
            "Peso-ul filipinez e ancorat de unul dintre cele mai mari fluxuri de transferuri din lume: milioane de lucrători filipinezi de peste hotare trimit bani acasă, iar aceste afluxuri în dolari sunt un pilon al economiei. USD/PHP se tranzacționează în consecință pe apetitul global de risc, pe prețurile petrolului (Filipinele sunt importator net) și pe politica Bangko Sentral ng Pilipinas.",
            "Cursul oficial e administrat cu mâna ușoară — banca centrală permite ajustare treptată, netezind vârfurile. Pentru familiile OFW și pentru călători, spread-ul dintre furnizori pe acest coridor e lat, deci verificarea cursului mid-market înainte de trimitere este cel mai simplu mod de a economisi.",
        ],
        "faq": [
            ("Cum afectează transferurile de bani peso-ul filipinez?",
             "Afluxurile constante de dolari de la lucrătorii din străinătate susțin peso-ul și balanța de plăți a țării — câteva procente din PIB în fiecare an. Când riscul global crește sau economiile gazdă slăbesc, transferurile se reduc, iar peso-ul tinde să le urmeze."),
            ("Este mai bine să convertești USD în PHP în SUA sau în Filipine?",
             "Depinde de furnizor, nu de țară. Ambele capete ale coridorului au opțiuni ieftine și scumpe; cifra decisivă e câți pesos primește efectiv destinatarul. Compară ofertele cu cursul mid-market în loc să ai încredere în ghișeul cel mai aproape."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR în GBP — cursul de schimb euro–liră sterlină și convertor",
        "description": "Convertește euro în lire sterline cu cursuri live: cursul EUR/GBP de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă această pereche.",
        "h1": "EUR în GBP — convertește euro în lire sterline",
        "intro": [
            "EUR/GBP este cross-ul european clasic: două economii care își trimit reciproc circa jumătate din comerț, despărțite de o singură graniță valutară. Fiind ambele valute dezvoltate, cu inflație mică, perechea se mișcă mult mai puțin decât cross-urile dolarului — este, în esență, un pariu pe sorțile relative ale zonei euro și ale Regatului Unit.",
            "Diferența de dobândă dintre BCE și Bank of England conduce cea mai mare parte a trendului, în timp ce știrile politice și fiscale britanice produc vârfurile. Pentru navetiștii transmaneci, pensionari și afaceri, stabilitatea perechii face ca diferențele mici de curs să conteze și mai mult: o marjă de 1% reprezintă o mare parte din mișcarea totală anuală.",
        ],
        "faq": [
            ("De ce este EUR/GBP mai liniștit decât EUR/USD?",
             "Nici euro, nici lira nu sunt valute globale de risc, deci fluxurile mondiale de refugiu în siguranță le ocolesc. Perechea reflectă mai ales economiile relative Marea Britanie–UE și diferențele de dobânzi, care se schimbă încet — deși poate sări puternic pe știri politice britanice, cum a arătat 2016."),
            ("Cum afectează Brexitul EUR/GBP și acum?",
             "Structural. Noile fricțiuni comerciale din 2021 au făcut economia britanică puțin mai puțin deschisă față de UE, ceea ce majoritatea economiștilor leagă de o sterlină structural mai slabă. Fiecare rundă de negocieri Marea Britanie–UE pe regulile comerciale mai mișcă perechea și astăzi."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR în CHF — cursul de schimb euro–franc elvețian și convertor",
        "description": "Convertește euro în franci elvețieni cu cursuri live: cursul EUR/CHF de azi, un calculator gratuit, tabele de sume uzuale și rolul SNB în această pereche.",
        "h1": "EUR în CHF — convertește euro în franci elvețieni",
        "intro": [
            "EUR/CHF este testul litmus al refugiului european: ori de câte ori crește stresul din zona euro — criza datoriei din 2011, panici bancare, război pe continent — banii trec granița elvețiană, iar perechea scade. Banca Națională Elvețiană o urmărește mai atent decât orice alt curs și a intervenit de repetate ori ca francul să nu sufoce exporturile elvețiene.",
            "Istoria modernă a perechii e dramatică: o podea la 1,20 din 2011, apoi abandonarea ei în ianuarie 2015, care a produs o prăbușire-fulger de 20–30% în câteva minute. De atunci, francul se tranzacționează ca un adăpost curat, uneori prea puternic — iar SNB rămâne participant activ pe această piață.",
        ],
        "faq": [
            ("De ce interesează SNB atât de mult EUR/CHF?",
             "Pentru că economia elvețiană vinde în Europa. Un franc prea puternic face exporturile elvețiene necompetitive și trage inflația sub țintă, deci SNB cumpără valută străină (și a impus odată rate negative) ca să plafoneze forța francului. Intervine pe această pereche mai mult decât aproape orice altă bancă centrală pe o piață majoră."),
            ("EUR/CHF este o pereche stabilă de deținut?",
             "Este stabilă în vremuri calme și explozivă în crize — opusul diversificării. Abandonarea podelei din 2015 rămâne avertizarea de manual că promisiunea unei bănci centrale de a plafona o monedă poate fi retrasă peste noapte. Cine a considerat perechea fără risc a învățat altfel într-o singură dimineață."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR în PLN — cursul de schimb euro–złoty polonez și convertor",
        "description": "Convertește euro în złoty polonez cu cursuri live: cursul EUR/PLN de azi, un calculator gratuit, tabele de sume uzuale și ce mișcă zloty-ul.",
        "h1": "EUR în PLN — convertește euro în złoty polonez",
        "intro": [
            "Polonia este a șasea economie a Uniunii Europene care încă își folosește propria monedă, iar złoty-ul este cel mai tranzacționat dintre valutele non-euro ale UE. EUR/PLN se tranzacționează pe diferența de dobândă față de National Bank of Poland, pe fondurile UE care curg spre est, pe comenzile fabricilor germane pentru industria poloneză și pe riscul geopolitic regional.",
            "Din momentul aderării Poloniei la UE în 2004, złoty-ul s-a întărit în boom-uri și a căzut puternic în crize — 2008 și 2022 au împins perechea la extreme istorice. Cu adoptarea eventuală a euro de către Polonia încă nedecisă, perechea rămâne un element structural al finanțelor europene pentru anii care vin.",
        ],
        "faq": [
            ("Va adopta Polonia euro și va renunța la złoty?",
             "Polonia este obligată prin lege să adopte euro în cele din urmă, dar nu are o dată-țintă, iar publicul e sceptic. Cât timp nu există un calendar credibil de adoptare, EUR/PLN rămâne o pereche activ tranzacționată — simplele declarații politice despre calendar o pot mișca de unele singure."),
            ("De ce a sărit EUR/PLN în 2022?",
             "Războiul din Ucraina vecină a făcut din Polonia peste noapte o economie de linia întâi: afluxurile de refugiați, cheltuielile de apărare și șocurile energetice au lovit moneda dur. National Bank of Poland a intervenit să susțină złoty-ul — cele mai puternice mișcări ale perechii în două decenii."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP în JPY — cursul de schimb liră sterlină–yen japonez și convertor",
        "description": "Convertește lire sterline în yeni japonezi cu cursuri live: cursul GBP/JPY de azi, un calculator gratuit, tabele de sume și ce mișcă perechea volatilă.",
        "h1": "GBP în JPY — convertește lire sterline în yeni japonezi",
        "intro": [
            "GBP/JPY — traderii de altădată îl numeau „bestia” sau „dragonul” — este una dintre cele mai volatile perechi majore. Suprapune două motoare de risc: sensibilitatea sterlinei la știrile politice și fiscale britanice și rolul yenului de monedă de finanțare a lumii, care îl face să se balanseze puternic ori de câte ori sentimentul global se răstâlnește.",
            "Perechea e favorita carry trade-ului: împrumuti yeni la rate aproape de zero ca să cumperi lire cu randament mai mare. Funcționează până când o criză îi obligă pe toți să demonteze odată, de aceea GBP/JPY tinde să urmeze anii întregi și să cadă violent în săptămâni. Dimensiunea poziției și momentul contează aici mai mult decât la aproape orice altă pereche majoră.",
        ],
        "faq": [
            ("De ce este GBP/JPY mai volatil decât USD/JPY?",
             "Pentru că înmulțește două volatilități. Sterlina adaugă riscul politic și economic specific britanic peste sentimentul global care conduce deja USD/JPY. Perechea nu are nicio economie-ancoră comună, deci se tranzacționează aproape pur pe diferențe de rate și pe sentiment — ingrediente pentru mișcări mari."),
            ("Ce este carry trade-ul în GBP/JPY?",
             "Împrumutul de yeni la rate japoneze aproape de zero și investiția în lire la rate britanice mai mari, încasând diferența. Este profitabil cât timp piețele sunt calme și punitiv când nu sunt: în episoadele de evitare a riscului, yenul sare pe măsură ce pozițiile de carry se demontează — frecvent cu 10% sau mai mult față de liră în câteva luni."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD în JPY — cursul de schimb dolar australian–yen japonez și convertor",
        "description": "Convertește dolari australieni în yeni japonezi cu cursuri live: cursul AUD/JPY de azi, un calculator gratuit, tabele de sume și ce mișcă barometrul de risc.",
        "h1": "AUD în JPY — convertește dolari australieni în yeni japonezi",
        "intro": [
            "AUD/JPY este cel mai pur barometru de risc al pieței valutare. Dolarul australian reprezintă creșterea globală și cererea de materii prime — mai ales cererea industrială chineză — în timp ce yenul reprezintă siguranța. Când economia mondială se extinde, perechea urcă; când lovește panica, cade mai repede decât aproape orice alt cross major.",
            "Este și perechea clasică a carry trade-ului: decenii la rând, investitorii au împrumutat yeni ieftini ca să cumpere aussie-ul mai bine plătit. Acest flux modelează trendurile ascendente lungi și dure ale perechii și episoadele ei violente de demontare — 2008 rămâne lecția, când AUD/JPY a pierdut aproximativ jumătate din valoare în câteva luni.",
        ],
        "faq": [
            ("De ce numesc traderii AUD/JPY barometru de risc?",
             "Pentru că fiecare monedă stă la un pol opus: aussie-ul urcă odată cu creșterea globală și cererea de materii prime, yenul urcă odată cu frica. Perechea se mișcă deci odată cu piețele de acțiuni mondiale într-o măsură pe care puțini cross-uri o egalează — când cade puternic, evitarea riscului e reală."),
            ("Ce s-a întâmplat cu AUD/JPY în criza din 2008?",
             "A fost aproximativ înjumătățit. Carry trade-ul s-a demontat odată cu înghețarea creditului global: investitorii au vândut dolari australieni ca să returneze yeni împrumutați, iar perechea s-a prăbușit de la peste 100 la puțin peste 50 în câteva luni. Rămâne exemplul standard al rapidității cu care se inversează strategiile de carry."),
        ],
    },
}
