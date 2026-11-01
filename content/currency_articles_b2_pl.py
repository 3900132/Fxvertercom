# -*- coding: utf-8 -*-
"""Polish (pl) translations of the second batch of long-form currency articles —
emerging-market and pegged currencies promoted in site_config.INDEXED_CURRENCIES.

Mirrors content/currency_articles_b2_en.py: one entry per ISO code with
"sections" — ("h", heading), ("p", paragraph) or ("li", bullet) — and "faq" —
(question, answer) pairs. This file covers (alphabetical): AZN BDT ETB GEL GHS
KES KWD KZT LKR MAD QAR TZS UAH XAF XOF.
"""

ARTICLES_B2 = {}

# ─────────────────────────── AZN ───────────────────────────
ARTICLES_B2["AZN"] = {
    "sections": [
        ("h", "Krótka historia manata azerbejdżańskiego"),
        ("p", "Manat to nazwa, którą Azerowie nadali rublowi sowieckiemu, więc gdy przyszła niepodległość, nowa waluta po prostu przejęła stare, codzienne słowo. Pierwszy manat pojawił się w 1992 roku, a w 1994 roku stał się jedynym prawnym środkiem płatniczym; 1 stycznia 2006 roku dokonano denominacji w stosunku 5000 starych manatów do jednego nowego, a przeprojektowane banknoty nadały walucie obecny, wyraźnie europejski wygląd."),
        ("p", "Przez pierwszą dekadę nowy manat był sztywno powiązany z dolarem amerykańskim na stałym poziomie, podczas gdy rozwijały się kaspijskie pola naftowe, a rurociąg Baku–Tbilisi–Ceyhan otworzył drogę do rynków śródziemnomorskich. Ropa błyskawicznie wzbogaciła Azerbejdżan: w 1999 roku utworzono Państwowy Fundusz Naftowy (SOFAZ), by oszczędzać ten nagły zysk, a Baku wypełniło się dźwigami budowlanymi."),
        ("p", "Krach naftowy z lat 2014–2015 złamał powiązanie. Bank centralny zdewaluował manata dwoma ostrymi krokami w 2015 roku, po czym przeszedł do silnie zarządzanego pływania osadzonego na dolarze. Ten reżim utrzymuje się do dziś, podparty rezerwami funduszu naftowego — choć wojna o Górski Karabach w 2020 roku i powojenne wydatki na odbudowę wciąż utrzymują wysokie potrzeby fiskalne."),
        ("h", "Co wpływa na kurs walutowy AZN"),
        ("p", "Manat to jedno z najsilniej zarządzanych pływań na świecie: bank centralny wyznacza ton, a ropa wyznacza ton bankowi centralnemu."),
        ("li", "Ceny ropy i gazu: eksport ropy i gazu to baza dochodów państwa, więc światowe ceny energii napędzają fundamenty manata"),
        ("li", "SOFAZ i budżet: ile pieniędzy z ropy płynie z funduszu państwowego do wydatków rządowych, tyle kształtuje podaż dolarów na rynku"),
        ("li", "Polityka banku centralnego: zarządzane pływanie broni się interwencjami i rezerwami, a dolar pozostaje operacyjną kotwicą"),
        ("li", "Powiązania z Turcją i Rosją: handel, inwestycje i miliony podróżnych regionalnych wiążą otoczenie manata z lirą i rublem"),
        ("h", "Manat azerbejdżański w praktyce"),
        ("p", "Baku sprawia wrażenie miasta kartowego: płatności zbliżeniowe działają w taksówkach, restauracjach i sklepach, a miejska karta transportowa obsługuje metro. Aplikacje do zamawiania przejazdów i usługi dostaw też przyjmują karty. Poza stolicą gotówka znaczy więcej, a małe targi chcą manatów. Manat jest w praktyce niewymienialny za granicą — wymień pieniądze po przybyciu i przelicz resztki przed opuszczeniem kraju."),
        ("p", "Azerbejdżan leży w środku kilku przepływów pieniężnych naraz: przyjmuje inwestycje i opłaty tranzytowe, wysyła przekazy do partnerów w Gruzji i Turcji, a jednocześnie obsługuje duży sezonowy ruch z Rosji, Turcji, Iranu i Zatoki. Firmy handlujące z Azerbejdżanem powinny zakładać fakturowanie dużych kontraktów w dolarach i planować się na lokalne przepisy o wymianie walut. Podróżni znajdą w Baku porządek i ceny rozsądne na tle europejskim, a stabilność manata ułatwia pilnowanie budżetu."),
        ("h", "Popularne konwersje manata"),
        ("p", "USD/AZN to para kotwica i kurs, do którego ostatecznie odwołuje się każdy lokalny kontrakt. EUR/AZN i GBP/AZN obsługują europejski biznes i gości, TRY/AZN to ruchliwa para tureckiego handlu i turystyki, a RUB/AZN odzwierciedla intensywny ruch między Baku a Rosją."),
    ],
    "faq": [
        ("Co stało się z manatem w 2015 roku?",
         "Spadające ceny ropy uczyniły powiązanie z dolarem nie do utrzymania, więc bank centralny zdewaluował manata dwoma dużymi krokami w 2015 roku, po czym przyjął silnie zarządzane pływanie. Ten reżim, podparty rezerwami państwowego funduszu naftowego, trwa do dziś."),
        ("Czy manat azerbejdżański jest powiązany z dolarem?",
         "Był, na stałym poziomie, od 2006 roku aż do dewaluacji z 2015 roku. Dziś to zarządzane pływanie osadzone na dolarze — kurs porusza się niewiele, ale to polityka, a nie formalne powiązanie."),
        ("Czy można używać manatów poza Azerbejdżanem?",
         "Praktycznie nie. Manatów niemal nigdy nie ma w ofercie zagranicznych kantorów. Wymień pieniądze po przybyciu, a pozostałą gotówkę oddaj w banku lub licencjonowanym punkcie przed wyjazdem."),
    ],
}

# ─────────────────────────── BDT ───────────────────────────
ARTICLES_B2["BDT"] = {
    "sections": [
        ("h", "Krótka historia taki bengalskiej"),
        ("p", "Bangladesz uzyskał niepodległość w marcu 1971 roku po wojnie o oderwanie się od Pakistanu, a na początku 1972 roku młode państwo zastąpiło rupię pakistańską taką — nazwą zapożyczoną od tanki, dawnej srebrnej monety Bengalu — po kursie równym względem waluty zastępowanej. Bangladesz Bank, bank centralny, rozpoczął działalność w tym samym okresie."),
        ("p", "Współczesne dzieje taki to jedna z wielkich opowieści rozwojowych: eksport gotowej odzieży uczynił z Bangladeszu jednego z największych na świecie eksporterów ubrań, przekazy od milionów pracowników za granicą wyrosły na filar gospodarki, a rezerwy walutowe rosły przez lata, podczas gdy kraj budował mosty, linie metra i elektrownie."),
        ("p", "Presja przyszła w latach 2022–2023, gdy globalny skok dolara, boom importowy i drogie źródła energii wyczerpywały rezerwy. Takę dewaluowano etapami od długiego zarządzanego kursu, nałożono ograniczenia importowe, a Bangladesz przystąpił w 2023 roku do programu MFW. Od tego czasu waluta zmierza ku bardziej elastycznemu reżimowi w stylu pełzającego powiązania."),
        ("h", "Co wpływa na kurs walutowy BDT"),
        ("p", "Taka jest zarządzana, a jej głównymi siłami są dwa silniki dochodów zewnętrznych Bangladeszu plus rachunek importowy, który je konsumuje."),
        ("li", "Przekazy pieniężne: Bangladesz konsekwentnie należy do największych na świecie odbiorców przekazów, z pieniędzmi płynącymi z Zatoki, Malezji, Stanów Zjednoczonych i Wielkiej Brytanii"),
        ("li", "Eksport odzieży: gotowa konfekcja to zdecydowana większość przychodów z eksportu, więc zachodni popyt detaliczny porusza fundamentami waluty"),
        ("li", "Rachunek importowy: paliwo, bawełna, żywność i maszyny trzeba opłacać w dolarach, a ceny energii potrafią szybko ogołocić rezerwy"),
        ("li", "Polityka i rezerwy: zarządzanie stopami przez Bangladesz Bank, kontrola kapitału i program MFW wyznaczają, jak szybko taka może się dostosowywać"),
        ("h", "Taka bengalska w praktyce"),
        ("p", "Bangladesz to gospodarka gotówki i pieniądza mobilnego. Karty działają w dhakskich galeriach, hotelach i lepszych restauracjach, ale prawdziwa rewolucja płatnicza to mobilne usługi finansowe — bKash i jego konkurenci pozwalają dziesiątkom milionów ludzi wysyłać, otrzymywać i płacić telefonem. Odwiedzający powinni mieć takę gotówką na transport, jedzenie z ulicznych straganów i targi oraz odrzucać każdy terminal, który proponuje rozliczenie w walucie domowej."),
        ("p", "Taka jest w praktyce walutą zamkniętą: wymieniaj ją w Bangladeszu i przelicz resztę przed wyjazdem, bo zagraniczne kantory rzadko się nią zajmują. Po stronie odbiorczej przekazy to pieniądze na życie — rząd okresowo wypłacał zachęty gotówkowe, by kierować transfery oficjalnymi kanałami, a luka między kursami bankowymi a nieformalnymi kursami ulicznymi (dawne kanały hundi) potrafi rozstrzygnąć, z którego ścieżki korzystają rodziny. Porównuj łączną kwotę taków, razem z opłatami i marżą walutową, zanim wybierzesz dostawcę."),
        ("h", "Popularne konwersje taki bengalskiej"),
        ("p", "USD/BDT to para odniesienia dla handlu i rezerw. AED/BDT i SAR/BDT to robocze pary przekazowe milionów pracowników z Bangladeszu w ZEA i Arabii Saudyjskiej, MYR/BDT i GBP/BDT obsługują korytarze Malezji i Wielkiej Brytanii, a EUR/BDT ma znaczenie dla kupujących odzież i pracowników mieszkających w UE."),
    ],
    "faq": [
        ("Dlaczego Bangladesz to jeden z największych rynków przekazów na świecie?",
         "Miliony pracowników z Bangladeszu mieszkają w Zatoce, Malezji, Wielkiej Brytanii i Stanach Zjednoczonych i regularnie wysyłają pieniądze do domu. Transfery te dorównują eksportowi towarowemu jako źródło dewiz i utrzymują miliony gospodarstw domowych."),
        ("Czy takę można dostać poza Bangladeszem?",
         "Prawie nigdy. Taka jest w praktyce walutą zamkniętą i ma ją w ofercie tylko garstka zagranicznych kantorów. Wymieniaj pieniądze w bankach lub licencjonowanych punktach w Bangladeszu i przelicz niewydaną takę przed wyjazdem."),
        ("Czym jest bKash?",
         "bKash to dominująca bangladeska usługa pieniądza mobilnego, uruchomiona w 2011 roku. Przeniosła płatności kraju na telefony — korzystają z niej odbiorcy przekazów, uliczni sprzedawcy i spółki użyteczności publicznej — i bywa najszybszą drogą, jaką rodziny otrzymują transfery."),
    ],
}

# ─────────────────────────── ETB ───────────────────────────
ARTICLES_B2["ETB"] = {
    "sections": [
        ("h", "Krótka historia birra etiopskiego"),
        ("p", "Słowo birr znaczy po amharsku srebro i tak nazywano monety — potomków talara Marii Teresy — które krążyły po etiopskiej wyżynie przez pokolenia. Współczesna Etiopia dość wcześnie zorganizowała formalną bankowość: Bank of Abyssinia powstał w 1905 roku, a kraj używał waluty birr, aż włoska okupacja lat 30. przerwała wszystko."),
        ("p", "Po wyzwoleniu Etiopia wprowadziła w 1945 roku dolara etiopskiego, a w 1976 roku przemianowała go na birr. Waluta przeszła przez erę imperialną, socjalistyczne lata dergu ze znacjonalizowanymi bankami i liberalizację po 1991 roku — zawsze jako mocno kontrolowana waluta, przy czym Bank Narodowy Etiopii racjonował dewizy, a birr przez dziesięciolecia stopniowo osuwał się wobec dolara."),
        ("p", "Przełomową reformą okazał się lipiec 2024 roku, gdy Etiopia uwolniła birra w ramach programu wspieranego przez MFW, pozwalając rynkowi wyznaczać kurs. Korekta była dramatyczna — waluta niemal od razu straciła około połowy oficjalnej wartości w dolarach — ale reforma miała zakończyć przewlekły niedobór dewiz, domknąć lukę między kursem oficjalnym a czarnorynkowym i przywrócić konkurencyjność eksportu."),
        ("h", "Co wpływa na kurs walutowy ETB"),
        ("p", "Birr jest dziś co do zasady kształtowany przez rynek, ale etiopski rynek dewizowy pozostaje płytki, więc wszystko rozstrzyga bilans między przychodami eksportowymi a rachunkiem importowym."),
        ("li", "Kawa, złoto i kwiaty: Etiopia to kolebka kawy i jeden z największych producentów Afryki, a złoto i kwiaty cięte dopełniają wielkich pozycji eksportowych"),
        ("li", "Rachunek importowy: paliwo, pszenica, maszyny i leki muszą być opłacane w dewizach, a niedobory definiowały tę gospodarkę przez lata"),
        ("li", "Inflacja: Etiopia w ostatnich latach należała do światowej czołówki inflacyjnej, która nieustannie podważa siłę nabywczą birra"),
        ("li", "Program reform i przekazy: wsparcie MFW, kroki liberalizacyjne i duże transfery od etiopskiej diaspory w Zatoce, USA i Europie kształtują ścieżkę waluty"),
        ("h", "Birr etiopski w praktyce"),
        ("p", "Etiopia pozostaje w duchu gospodarką gotówkową: banknotami birra płaci się za taksówki, targi i większość restauracji, choć pieniądz mobilny — telebirr i konkurenci — rozprzestrzenił się w ostatnich latach szybko. Karty przyjmują hotele i większe firmy w Addis Abebie, ale gdzie indziej znacznie rzadziej. Przy bankomatach zawsze wybieraj rozliczenie w birrach zamiast przyjmować konwersję terminala."),
        ("p", "Birr to jedna z najczyściej zamkniętych walut świata: przywóz i wywóz banknotów jest ograniczony, a zagraniczne kantory praktycznie w ogóle się nimi nie zajmują. Wymieniaj po przybyciu i przelicz resztę przed wyjazdem. W przekazach etiopska diaspora jest ogromna, a przez lata szeroka luka między kursem oficjalnym a równoległym pchała transfery do kanałów nieformalnych — uwolnienie kursu w 2024 roku zawęziło tę lukę i uczyniło oficjalne ścieżki znacznie atrakcyjniejszymi, co było właśnie celem reformy."),
        ("h", "Popularne konwersje birra"),
        ("p", "USD/ETB to jedyna para odniesienia dla handlu, pomocy rozwojowej i wyceny. AED/ETB i SAR/ETB to robocze pary przekazowe ogromnej etiopskiej siły roboczej w ZEA i Arabii Saudyjskiej, a EUR/ETB obsługuje europejską pomoc, handel i transfery diaspory."),
    ],
    "faq": [
        ("Czy birr etiopski jest wymienialny?",
         "Nie — w praktyce to waluta zamknięta. Banknotów birra nie można swobodnie przywozić ani wywozić, a zagraniczne punkty rzadko je notują. Wymieniaj wewnątrz Etiopii i przelicz resztki przed wyjazdem."),
        ("Dlaczego Etiopia uwolniła birra w 2024 roku?",
         "Lata niedoborów dewiz, szeroka luka między kursem oficjalnym a czarnorynkowym i ciężka inflacja uczyniły stary reżim kontroli nie do utrzymania. Uwolnienie birra było trzonem reformy wspieranej przez MFW, która miała ożywić eksport i wyprowadzić rynek na światło dzienne."),
        ("Jaka jest historia birra?",
         "Nazwa sięga monet srebrnych — birr znaczy po amharsku srebro. Współczesna Etiopia wprowadziła dolara etiopskiego w 1945 roku, a w 1976 roku przemianowała walutę na birr; emituje go Bank Narodowy Etiopii od lat 60."),
    ],
}

# ─────────────────────────── GEL ───────────────────────────
ARTICLES_B2["GEL"] = {
    "sections": [
        ("h", "Krótka historia lari gruzińskiego"),
        ("p", "Po rozpadzie ZSRR Gruzja przeszła przez rubla rosyjskiego, a potem przez tymczasową walutę kuponową, znosząc po drodze groźną inflację. Lari pojawiło się 2 października 1995 roku, zastępując kupony w stosunku milion do jednego i dając młodej republice walutę o głębokich korzeniach historycznych: lari to stare gruzińskie słowo oznaczające pieniądze i majątek, a jednostka podrzędna, tetri, bierze nazwę od średniowiecznej srebrnej monety."),
        ("p", "Lari to waluta płynna. Bank Narodowy Gruzji wygładza wahania, zamiast sztywno ustalać poziom — reżim testowany wielokrotnie: przez wojnę z Rosją w 2008 roku, przez wyprzedaż na rynkach wschodzących w latach 2014–2015, która mocno przycięła lari, i przez pandemiczne zamrożenie turystyki. Dolaryzacja, spadek po burzliwych latach 90., pozostaje wysoka: część gruzińskich oszczędności i kredytów nadal denominowana jest w dolarach."),
        ("p", "Lata po 2020 roku przyniosły niezwykłą odmianę. Turystyka odbudowała się, a po lutym 2022 roku Gruzja przyjęła duże fale ludzi, firm i przekazów z regionu, co pomogło lari przeżyć jeden z najmocniejszych okresów umocnienia od lat, zanim bank centralny go ostudził."),
        ("h", "Co wpływa na kurs walutowy GEL"),
        ("p", "Lari to waluta małej, otwartej gospodarki usługowej, więc przepływy znaczą tu tyle, co fundamenty."),
        ("li", "Turystyka: goście Tbilisi, wybrzeża Morza Czarnego, gór i kraju wina to ważne źródło dewiz, mocno sezonowe"),
        ("li", "Przekazy i napływy: transfery od Gruzinów za granicą — i fale pieniędzy, które przyszły po 2022 roku — potrafią realnie poruszyć walutą"),
        ("li", "Bilans handlowy: Gruzja importuje znacznie więcej, niż eksportuje, kupując w Turcji, UE i u sąsiadów, a sprzedając wino, orzechy i reeksportowane samochody"),
        ("li", "Polityka Banku Narodowego: interwencje i stopa procentowa bronią lari, a dolaryzacja kredytów krajowych czyni ze stabilności priorytet polityki"),
        ("h", "Lari gruzińskie w praktyce"),
        ("p", "Gruzja to jeden z łatwiejszych krajów Kaukazu do podróżowania bez gotówki: karty zbliżeniowe działają niemal wszędzie w Tbilisi i Batumi, od przejazdów metrem po górskie pensjonaty, choć gotówka wciąż przydaje się we wsiach i na targach. Bankomaty są niezawodne, a krajowa kultura przekazów — punkty obsługi w witrynach kamienic, prowadzące transfery transgraniczne — należy do najgęstszych na świecie."),
        ("p", "Lari nie jest realnie wymienialne za granicą: wymień pieniądze po przybyciu i przelicz resztę przed wyjazdem. W przekazach główne korytarze prowadzą do i z Rosji, UE, Turcji, Izraela i Stanów Zjednoczonych, a konkurencja między bankami i operatorami przekazów trzyma marże w ryzach — mimo to porównuj kwotę lari, którą faktycznie otrzymujesz. Dla firm dolaryzacja czynszów i kredytów oznacza, że osłabiające się lari po cichu podnosi koszty powiązane z dolarem — dlatego miejscowi śledzą USD/GEL równie uważnie jak każdy wskaźnik makroekonomiczny."),
        ("h", "Popularne konwersje lari"),
        ("p", "USD/GEL to para odniesienia dla oszczędności, kredytów i przekazów. EUR/GEL ma znaczenie dla handlu z UE i europejskich gości, TRY/GEL jest ruchliwą parą dzięki tureckiemu handlowi i turystyce, RUB/GEL odzwierciedla intensywny ruch regionalny z Rosją, a GBP/GEL obsługuje rosnące powiązania turystyczne i inwestycyjne z Wielką Brytanią."),
    ],
    "faq": [
        ("Czego Gruzja używała przed lari?",
         "Po niepodległości Gruzja używała rubla rosyjskiego, a od 1993 roku emitowała tymczasową walutę kuponową w warunkach wysokiej inflacji. Lari zastąpiło kupony w październiku 1995 roku w stosunku milion kuponów za jedno lari."),
        ("Czy lari gruzińskie jest do czegoś powiązane?",
         "Nie. Lari pływa, a Bank Narodowy Gruzji interweniuje tylko po to, by wygładzać nadmierne wahania. Dolar amerykański wciąż odgrywa dużą rolę, bo część gruzińskich kredytów i oszczędności jest zdolaryzowana."),
        ("Czy Gruzja to kraj gotówki czy kart?",
         "Oboje, i to z wygodą. Karty i płatności zbliżeniowe przyjmowane są niemal wszędzie w miastach i regionach turystycznych; miej lari gotówką na wsie, targi i starsze taksówki."),
    ],
}

# ─────────────────────────── GHS ───────────────────────────
ARTICLES_B2["GHS"] = {
    "sections": [
        ("h", "Krótka historia cedi ghańskiego"),
        ("p", "Cedi bierze nazwę od słowa z języka Akan oznaczającego muszlę kauri — pieniądza handlu Afryką Zachodnią przez stulecia — podczas gdy jednostka podrzędna, pesewa, przypomina dawną miedzianą monetę. Pierwsze cedi Gany pojawiło się w 1965 roku, zastępując funta ghańskiego dwa lata po niepodległości; drugie cedi przyszło w 1967 roku po zmianie rządów, otwierając długi bój z inflacją."),
        ("p", "W połowie lat 2000. banknoty cedi nosiły więcej zer, niż ktokolwiek chciał liczyć. W lipcu 2007 roku Ghana dokonała denominacji, ścinając cztery zera — 10 000 starych cedi za jedno nowe — i przywróciła do obiegu monety wyparte wcześniej przez drożyznę. Ruch ten stał się jednym z najczęściej przywoływanych afrykańskich przykładów udanej denominacji."),
        ("p", "Lata 20. XXI wieku przyniosły trudniejszy sprawdzian. W 2022 roku cedi trafiło do grona najgorzej radzących sobie walut świata, inflacja przekroczyła pięćdziesiąt procent, a Ghana zawiesiła spłatę znacznej części długu zagranicznego, po czym w 2023 roku przystąpiła do programu MFW i przeprowadziła restrukturyzację obligacji. Stabilizacja postępuje powoli, a w naprawie najwięcej pracują rezerwy złota i dyscyplina fiskalna."),
        ("h", "Co wpływa na kurs walutowy GHS"),
        ("p", "Cedi pływa, a jego kierunek rozstrzygają dochody surowcowe, kalendarz fiskalny i zaufanie, że dług Gany daje się obsługiwać."),
        ("li", "Złoto i kakao: Ghana to czołowy światowy producent obu towarów, a przychody z ich eksportu kotwiczą krajową podaż dolarów — bank centralny kupował nawet złoto, by budować rezerwy"),
        ("li", "Ropa: wydobycie ze złoża Jubilee, eksploatowanego od końca 2010 roku, dodało trzecią wielką pozycję zarobkową eksportu"),
        ("li", "Wiarygodność fiskalna: wydatki w latach wyborczych i poziom długu niejednokrotnie stoją za najgorszymi epizodami cedi"),
        ("li", "Inflacja i polityka pieniężna: stopa procentowa Banku Ghany i pozycja rezerwowa przesądzają, jak skutecznie waluta jest broniona"),
        ("h", "Cedi ghańskie w praktyce"),
        ("p", "Ghana to jeden z afrykańskich pionierów pieniądza mobilnego: MTN MoMo i konkurenci obsługują płatności ulicznych sprzedawców, taksówek i szkół, a podróżny z lokalną gotówką i chętnym sprzedawcą radzi sobie zaskakująco dobrze bez karty. Galerie i hotele Akry przyjmują karty, ale targi i tro-tro chcą banknotów cedi — najlepiej drobnych."),
        ("p", "Cedi wymienisz w dużych centrach finansowych, ale gdzie indziej rynek jest płytki; przelicz resztki przed wyjazdem, bo zagraniczne kantory rzadko je mają w ofercie. W przekazach diaspora Gany w Stanach Zjednoczonych i Wielkiej Brytanii wysyła solidne strumienie, a szyny pieniądza mobilnego dostarczają dziś transfery wprost na telefon odbiorcy — porównuj kwotę cedi, którą faktycznie otrzymujesz, zamiast wierzyć nagłówkom o zerowej opłacie. Dla firm zmienność cedi w słabych latach czyni z nawet krótkoterminowego fakturowania pytanie o zabezpieczenie kursowe."),
        ("h", "Popularne konwersje cedi"),
        ("p", "USD/GHS to para odniesienia i liczba stojąca za każdą fakturą importową. GBP/GHS i EUR/GHS obsługują brytyjskie i europejskie powiązania handlowe oraz diaspory, a NGN/GHS ma znaczenie dla handlu transgranicznego z Nigerią, olbrzymim sąsiadem Gany — i przypomina, że historia cedi jest nierozerwalna z handlem Afryki Zachodniej."),
    ],
    "faq": [
        ("Dlaczego cedi poddano denominacji w 2007 roku?",
         "Lata inflacji zostawiły staremu cedi gigantyczne nominały. W lipcu 2007 roku Ghana usunęła cztery zera — 10 000 starych cedi stało się jednym nowym cedi — upraszczając ceny i przywracając praktyczne monety."),
        ("Dlaczego cedi mocno spadło w 2022 roku?",
         "Kombinacja wysokiego długu publicznego, popandemicznego stresu fiskalnego, globalnej siły dolara i rosnących kosztów importu wypchnęła inwestorów z aktywów w cedi. Ghana zawiesiła spłatę długu zagranicznego, inflacja przekroczyła pięćdziesiąt procent, a w 2023 roku przyszedł program MFW."),
        ("Czy Ghana to gospodarka gotówkowa czy pieniądza mobilnego?",
         "Obie rzeczy współistnieją w zgodzie. Pieniądz mobilny dominuje w codziennych płatnościach i sięga głęboko na prowincję, gotówka pozostaje niezbędna na targach i w transporcie, a karty obsługują głównie hotele, galerie i miejskie firmy."),
    ],
}

# ─────────────────────────── KES ───────────────────────────
ARTICLES_B2["KES"] = {
    "sections": [
        ("h", "Krótka historia szylinga kenijskiego"),
        ("p", "Kenia uzyskała niepodległość w 1963 roku, a w 1966 roku świeżo powołany Bank Centralny Kenii wyemitował szylinga kenijskiego, zastępując szylinga wschodnioafrykańskiego, który służył Kenii, Ugandzie i Tanzanii jako wspólna społeczność walutowa. Trzej sąsiedzi poszli potem własnymi drogami monetarnymi, choć ich waluty pozostały bliskimi krewnymi."),
        ("p", "Szyling przeszedł od reżimów sztywnych przez kontrolę dewizową do zliberalizowanego, zarządzanego pływania w latach 90. Nairobi wyrosło na biznesową i finansową stolicę Afryki Wschodniej, a w 2007 roku start M-Pesa — sposobu na przenoszenie pieniędzy telefonem — uczynił z Kenii najsłynniejsze laboratorium płatnicze świata."),
        ("p", "Najnowsza historia szylinga była kręta: mocno osunął się w 2011 roku, a presja narastała znów przez 2023 rok, gdy zbliżała się duża rata Euroobligacji. Operacja zadłużeniowa z początku 2024 roku kupiła krajowi czas, wsparcie MFW trwało, a waluta odzyskała grunt — przypomnienie, że na rynkach wschodzących kalendarze długu poruszają kursem równie mocno jak handel."),
        ("h", "Co wpływa na kurs walutowy KES"),
        ("p", "Szyling kenijski pływa w sposób zarządzany, a jego siłami napędowymi jest klasyczna wschodnioafrykańska mieszanka: eksport, turystyka, pieniądze diaspory i dług."),
        ("li", "Herbata, kawa i ogrodnictwo: klasyczny eksport Kenii — w tym kwiaty lecące świeże do europejskich supermarketów — dostarcza stabilnego strumienia dolarów"),
        ("li", "Turystyka: safari i wybrzeże przyciągają gości z Europy, obu Ameryk i coraz bardziej z Azji"),
        ("li", "Przekazy: pieniądze od Kenijczyków w Stanach Zjednoczonych, Europie i Zatoce to jedno z największych pojedynczych źródeł dewiz kraju"),
        ("li", "Dług i globalne stopy: raty Euroobligacji, programy MFW i cykl stóp amerykańskich kształtują presję na szylinga"),
        ("h", "Szyling kenijski w praktyce"),
        ("p", "Kenia to najbardziej przyjazna płatnościom bezgotówkowym gospodarka Afryki Wschodniej: M-Pesa przyjmują wszędzie, od nairobskich supermarketów po przydrożne stragany z warzywami, a wielu Kenijczyków ledwo używa gotówki. W miastach i hotelach zapłacisz kartą, ale trzymaj banknoty szylingów do matatu, targów i terenów wiejskich — taksówki z aplikacji coraz częściej przyjmują płatności w aplikacji, a minibus obsługuje wyłącznie gotówkę albo pieniądz mobilny. Jak zwykle, odrzucaj każdy terminal oferujący rozliczenie w Twojej walucie domowej."),
        ("p", "Szyling jest wymienialny w regionie Afryki Wschodniej i dostępny w głównych centrach międzynarodowych, choć płynność cienieje szybko poza Londynem i Nairobi. W przekazach korytarze do USA i Wielkiej Brytanii są głębokie i konkurencyjne, a szyny pieniądza mobilnego wpłacają środki wprost do portfeli M-Pesa — sprawdzaj kwotę szylingów, którą dostaje odbiorca, bo marketing o zerowej opłacie potrafi kryć szeroką marżę. Konta diaspory, zakup ziemi i obligacje skarbowe oferowane Kenijczykom za granicą przyciągają też stały strumień inwestycji. Dla firm rola Nairobi jako regionalnego huba sprawia, że szyling działa jak barometr całej Wspólnoty Afryki Wschodniej."),
        ("h", "Popularne konwersje szylinga kenijskiego"),
        ("p", "USD/KES to para odniesienia dla handlu, długu i przekazów. GBP/KES i EUR/KES obsługują brytyjskie i europejskie powiązania turystyczne, handlowe i diasporowe, a UGX/KES i TZS/KES to praktyczne pary regionalne dla handlu i podróży wewnątrz Wspólnoty Afryki Wschodniej."),
    ],
    "faq": [
        ("Czym jest M-Pesa?",
         "M-Pesa to kenijska usługa pieniądza mobilnego, uruchomiona w 2007 roku przez Safaricom. Pozwala przechowywać, wysyłać i otrzymywać pieniądze telefonem i korzysta z niej niemal każdy dorosły Kenijczyk — od opłacania czesnego po odbieranie transferów międzynarodowych."),
        ("Czy szyling kenijski jest powiązany z dolarem?",
         "Nie. Szyling pływa w reżimie zarządzanym pod okiem Banku Centralnego Kenii, który interweniuje, by wygładzać wahania, ale nie broni sztywnego kursu."),
        ("Kiedy Kenia dostała własną walutę?",
         "W 1966 roku, gdy Bank Centralny Kenii wyemitował szylinga kenijskiego, zastępując szylinga wschodnioafrykańskiego, który krążył w Kenii, Ugandzie i Tanzanii."),
    ],
}

# ─────────────────────────── KWD ───────────────────────────
ARTICLES_B2["KWD"] = {
    "sections": [
        ("h", "Krótka historia dinara kuwejckiego"),
        ("p", "Kuwejt wprowadził dinara w 1961 roku, zastępując nim rupię Zatoki w stosunku około trzynastu rupii za dinara — mniej więcej tyle, ile wtedy wart był funt brytyjski. To dziedzictwo sprawia, że dinar jest w przeliczeniu na pojedynczą jednostkę najwyżej wycenianą walutą świata: to opowieść o nominałach, nie o sile gospodarki. Start nadzorowała Kuwejcka Rada Walutowa, a Bank Centralny Kuwejtu przejął stery w 1968 roku."),
        ("p", "Najbardziej dramatyczny rozdział dinara przyszedł w 1990 roku. Gdy Irak najechał Kuwejt, siły okupacyjne obrabowały bank centralny i wywiozły banknoty. Po wyzwoleniu na początku 1991 roku rząd unieważnił banknoty będące w obiegu pod okupacją i wyemitował nową serię — jeden z niewielu przypadków, gdy współczesną walutę chirurgicznie wyemitowano na nowo, by zneutralizować skradzioną gotówkę."),
        ("p", "Dinar był powiązany z dolarem amerykańskim od 2003 do 2007 roku, po czym przeszedł na niejawną koszykówkę walut — powszechnie uważaną za silnie dolarową — co pozwala mu delikatnie dryfować zarówno wobec dolara, jak i euro. Kuwejt od lat dyskutuje o powrocie do powiązania albo nawet o unii monetarnej Zatoki, ale reżim koszykowy się utrzymał."),
        ("h", "Co wpływa na kurs walutowy KWD"),
        ("p", "Jak sąsiedzi z Zatoki, Kuwejt prowadzi reżim sztywny, więc los dinara związany jest z wiarygodnością powiązania i zdrowiem naftowej gospodarki, które za nim stoi."),
        ("li", "Powiązanie koszykowe: od 2007 roku dinar podąża za niejawną koszykówką, więc delikatnie porusza się wobec dolara, gdy poruszają się inne waluty koszyka"),
        ("li", "Dochody naftowe: eksport ropy finansuje budżet państwa i rezerwy, które gwarantują powiązanie"),
        ("li", "Kuwejcka Organizacja Inwestycyjna: jeden z najstarszych i największych funduszy majątkowych świata, sięgający lat 50., to strukturalne źródło narodowego bogactwa"),
        ("li", "Praca ekspatów i odpływy: większość mieszkańców to pracownicy z zagranicy, więc repatriacja zarobków to stały odpływ, który powiązanie musi wchłonąć"),
        ("h", "Dinar kuwejcki w praktyce"),
        ("p", "Kuwejt to kraj kartowy z wysokimi kosztami życia, a gotówka wciąż pomaga na targach i w małych jadłodajniach. Dla gości praktyczna wskazówka jest taka jak wszędzie przy sztywnym kursie: nie ma dnia, w którym wymiana dolarów wychodzi korzystniej, więc zamiast łapać moment, ograniczaj opłaty."),
        ("p", "Dinar jest niemal niemożliwy do wymiany poza Kuwejtem — nawet regionalne kantory trzymają go niechętnie — więc przelicz gotówkę przed wyjazdem. Dla milionów ekspatów pracujących w Kuwejcie ten kraj to jeden z największych na świecie nadawców przekazów względem swojej wielkości: korytarze do Indii, Filipin, Egiptu i Bangladeszu są ogromne, a różnica między marżami KWD u różnych dostawców jest naprawdę odczuwalna na miesięcznej pensji."),
        ("h", "Popularne konwersje dinara kuwejckiego"),
        ("p", "USD/KWD to para odniesienia, choć powiązanie biegnie przez koszykówkę, i to ten kurs każdy ekspat w myślach dzieli przez swoją pensję. INR/KWD to największy pojedynczy korytarz przekazowy, tuż za nim plasują się PHP/KWD, EGP/KWD i BDT/KWD. GBP/KWD i EUR/KWD mają znaczenie dla zachodnich ekspatów i firm."),
    ],
    "faq": [
        ("Dlaczego dinar kuwejcki to najwyżej wyceniana waluta świata?",
         "Dinar zastąpił rupię Zatoki w 1961 roku w stosunku około trzynastu rupii za jednego dinara, blisko ówczesnej wartości funta. Wielka wartość jednostki to historia nominałów — nie mówi nic o sile nabywczej ani wielkości gospodarki."),
        ("Czy dinar kuwejcki jest powiązany z dolarem amerykańskim?",
         "Już nie bezpośrednio. Był powiązany z dolarem od 2003 do 2007 roku, po czym przeszedł na niejawną koszykówkę walut. Jej skład jest tajny, ale większość analityków zakłada dominację dolara."),
        ("Czy dinary kuwejckie da się wymienić za granicą?",
         "Bardzo trudno. Niewiele kantorów poza Kuwejtem ma dinary w ofercie. Wymień pozostałą gotówkę w kuwejckim banku lub domu wymiany przed opuszczeniem kraju."),
    ],
}

# ─────────────────────────── KZT ───────────────────────────
ARTICLES_B2["KZT"] = {
    "sections": [
        ("h", "Krótka historia tenge kazachskiego"),
        ("p", "Kazachstan był pierwszą republiką Azji Środkowej byłego ZSRR, która uruchomiła własną walutę, wprowadzając tenge 15 listopada 1993 roku w miejsce rubla rosyjskiego. Nazwa dzieli dawnego tureckiego rdzenia z rosyjskim słowem oznaczającym same pieniądze — przypominka, jak głębokie są tutejsze tradycje handlowe."),
        ("p", "Pierwsze dwie dekady tenge zbiegły się z boomem naftowym: Kazachstan wyrosł na jednego ze znaczących światowych eksporterów ropy, Bank Narodowy gromadził rezerwy, a przez lata tenge handlowano w zarządzanych przedziałach wobec dolara. Koniec z tym przyniosło załamanie cen ropy w latach 2014–2015: po dewaluacji tenge uwolniono w sierpniu 2015 roku, a bank centralny przeszedł do targetowania inflacji."),
        ("p", "Ostatnie lata były burzliwe — zamieszki styczniowe 2022 roku, przelot skutków wojny w Ukrainie i skok inflacji, który zmusił Bank Narodowy do agresywnych podwyżek stóp. Przez wszystko tenge pozostaje najpłynniejszą walutą regionu, z działającym rynkiem i głębokimi rezerwami w tle."),
        ("h", "Co wpływa na kurs walutowy KZT"),
        ("p", "Tenge to pływająca waluta surowcowa wciśnięta między dwóch wielkich sąsiadów, a jej siły napędowe odzwierciedlają tę geografię."),
        ("li", "Ceny ropy i surowców: ropa, uran i metale dominują kazachski eksport, więc ich ceny napędzają podaż dewiz"),
        ("li", "Polityka Banku Narodowego: interwencje, stopa procentowa i akumulacja rezerw kształtują ścieżkę tenge w zarządzanym pływaniu"),
        ("li", "Handel z Rosją i Chinami: wahania rubla, rozliczenia w juanach i przekierowania regionalnego handlu trafiają wprost do kazachskich rynków"),
        ("li", "Inflacja i geopolityka: regionalna premia za ryzyko i krajowa presja cenowa poruszają i walutę, i stopy, które ją bronią"),
        ("h", "Tenge kazachskie w praktyce"),
        ("p", "Kazachstan zaskakuje cyfryzacją: superaplikacja Kaspi rządzi płatnościami i zakupami, karty działają niemal wszędzie w Ałmaty i Astanie, a gotówka ma znaczenie głównie na wsi i na bazarach. Podróżni wypłacą tenge z bankomatów bankowych i zawsze powinni wybierać rozliczenie w KZT zamiast przyjmować konwersję terminala."),
        ("p", "Tenge trudno wymienić poza byłym obszarem sowieckim — zachodnich kantorów, które je mają w ofercie, jest niewiele — więc przelicz pozostałą gotówkę przed wyjazdem. Jeśli ruszasz dalej do sąsiadów, zaplanuj gotówkę z wyprzedzeniem: wymiana tenge na kirgiskie somy czy inne waluty regionu w praktyce często biegnie przez dolary, a bazarkowe kursy zwykle biją tablice bankowe. W biznesie eksporterzy zarabiają w dolarach, a pensje płacą w tenge, więc uwolnienie kursu w 2015 roku uczyniło z zabezpieczania kursowego codzienność kazachskich firm. Przekazy z Rosji, Kirgistanu i Uzbekistanu są istotne, a dziesiątki tysięcy ludzi, którzy w 2022 roku przenieśli się do Kazachstanu, niemal z dnia na dzień dodały nowe korytarze."),
        ("h", "Popularne konwersje tenge"),
        ("p", "USD/KZT to para odniesienia i główny barometr zdrowia waluty. EUR/KZT i GBP/KZT obsługują europejski handel i podróżnych, RUB/KZT to para kluczowa dla ogromnego handlu transgranicznego z Rosją, a CNY/KZT rośnie razem z chińskimi inwestycjami i korytarzami Nowego Jedwabnego Szlaku."),
    ],
    "faq": [
        ("Czy tenge kazachskie jest powiązane z dolarem?",
         "Nie. Kazachstan powiązał kurs na lata, ale uwolnił tenge w sierpniu 2015 roku po załamaniu cen ropy. Bank Narodowy nadal wygładza wahania, więc to pływanie zarządzane, nie wolne."),
        ("Dlaczego tenge tak mocno spadło w 2015 roku?",
         "Spadające ceny ropy przecięły dolarowe dochody kraju, a obrona starego powiązania stała się nie do utrzymania. Po dewaluacji bank centralny pozwolił rynkowi wyznaczać kurs i przeszedł do targetowania inflacji."),
        ("Kiedy wprowadzono tenge?",
         "15 listopada 1993 roku, w miejsce rubla rosyjskiego — Kazachstan był pierwszą byłą republiką radziecką w Azji Środkowej, która wydała własną walutę."),
    ],
}

# ─────────────────────────── LKR ───────────────────────────
ARTICLES_B2["LKR"] = {
    "sections": [
        ("h", "Krótka historia rupii lankijskiej"),
        ("p", "Cejlon przyjął dziesiętną rupię po 100 centach w latach 70. XIX wieku, zastępując starszą monetę riks dolarów i pieniędzy epoki brytyjskiej. Po niepodległości w 1948 roku w 1949 roku powołano Bank Centralny Cejlonu, który przejął emisję banknotów; w 1972 roku kraj zmienił nazwę na Sri Lankę, a waluta działała dalej."),
        ("p", "Rupia przez dekady siedziała w reżimach sztywnych i zarządzanych, zanim na początku lat 90. zliberalizowano ją do zarządzanego pływania. Długa wojna domowa od 1983 do 2009 roku przyhamowała gospodarkę, a pokój, który nadszedł potem, uwolnił boom turystyczny — plaże, kraina wzgórz i antyczne miasta ciągnęły gości z Europy, Indii i Azji Wschodniej."),
        ("p", "Potem przyszedł 2022 rok, najgorszy kryzys od niepodległości: rezerwy wyczerpała obsługa długu, rząd zawiesił spłaty zadłużenia zagranicznego, a w marcu 2022 roku rupię gwałtownie uwolniono po latach utrzymywania na sztucznym poziomie. Nadeszły niedobory paliwa, leków i żywności, a program MFW ułożony w 2023 roku rozpoczął długi proces restrukturyzacji długu i odbudowy rezerw."),
        ("h", "Co wpływa na kurs walutowy LKR"),
        ("p", "Rupia Sri Lanki to zarządzane pływanie, którego los rozstrzyga zdolność kraju do zarabiania dewiz i obsługi długów."),
        ("li", "Turystyka: przyjazdy to jedna z czołowych pozycji zarobkowych, a wstrząsy jak zamachy wielkanocne z 2019 roku i pandemia pokazały, jak szybko ten dochód potrafi zniknąć"),
        ("li", "Przekazy: lankijscy pracownicy w Zatoce i gdzie indziej wysyłają pieniądze do domu, a udział kanałów oficjalnych faluje razem z oferowanym kursem"),
        ("li", "Herbata, odzież i kauczuk: klasyczna eksportowa trójka finansuje sporą część importu"),
        ("li", "Dług i rezerwy: spłaty długu publicznego, przeglądy programu MFW i poziomy rezerw napędzają oczekiwania rynku mocniej niż jakiekolwiek dane dzienne"),
        ("h", "Rupia lankijska w praktyce"),
        ("p", "Sri Lanka pozostaje gospodarką mocno gotówkową: tuk-tuki, autobusy, targi i małe restauracje chcą rupii, podczas gdy karty działają w kolombojskich galeriach i hotelach turystycznych. Rupia jest walutą zamkniętą za granicą — wymieniaj po przybyciu i przelicz resztę przed wylotem, bo niemal żaden zagraniczny bank nie przyjmie jej z powrotem."),
        ("p", "W przekazach lata kryzysu dały bolesną lekcję: gdy kurs oficjalny odstawał od ulicznego, transfery uciekały do kanałów nieformalnych, a oficjalne napływy się załamywały. Po uwolnieniu kursu kanały oficjalne znacznie podniosły konkurencyjność, a banki i operatorzy przekazów aktywnie zabiegają o korytarz pracowników z Zatoki. Jak zawsze, porównuj łączną liczbę rupii otrzymanych za każdą wysłaną jednostkę — oferta bez opłat z kiepskim kursem to nie okazja. Podróżni: ceny ostro dostosowały się po dewaluacji, więc weryfikuj koszty od nowa, zamiast ufać starszym przewodnikom."),
        ("h", "Popularne konwersje rupii lankijskiej"),
        ("p", "USD/LKR to para odniesienia i liczba, na którą patrzy każdy importer i nadawca przekazów. GBP/LKR i AUD/LKR obsługują duże diaspory w Wielkiej Brytanii i Australii, AED/LKR i SAR/LKR niosą korytarz pracowników z Zatoki, a EUR/LKR dopełnia europejską stronę podróży i handlu."),
    ],
    "faq": [
        ("Dlaczego rupia lankijska runęła w 2022 roku?",
         "Rezerwy wyczerpała obsługa długu, podczas gdy turystyka i przekazy słabły, więc kraj nie mógł opłacić importu. Rząd zawiesił spłaty zadłużenia zagranicznego i uwolnił rupię, którą wcześniej trzymano na przewartościowanym, zarządzanym poziomie — korekta była surowa."),
        ("Czy rupia lankijska jest powiązana z dolarem?",
         "Nie. Po latach ścisłej kontroli rupię uwolniono w marcu 2022 roku i handluje się nią dziś w zarządzanym pływaniu pod okiem Banku Centralnego Sri Lanki, z programem MFW w tle."),
        ("Czy rupie lankijskie da się wymienić poza Sri Lanką?",
         "Rzadko. Rupia za granicą to waluta zamknięta, z prawie zerową płynnością. Wymień pieniądze na rupie po przybyciu i przelicz pozostałą gotówkę przed opuszczeniem kraju."),
    ],
}

# ─────────────────────────── MAD ───────────────────────────
ARTICLES_B2["MAD"] = {
    "sections": [
        ("h", "Krótka historia dirhama marokańskiego"),
        ("p", "Nazwa dirhama jest starożytna — wędrowała z greckiej drachmy do arabskiego i stała się jedną ze standardowych monet wczesnego świata islamu. Współczesny dirham Maroka wprowadzono w 1960 roku, zastępując nim franka marokańskiego pozostałego po epoce protektoratu; emituje go Bank al-Maghrib, bank centralny utworzony w 1959 roku."),
        ("p", "Dirham zawsze był walutą zarządzaną. Przez dekady był związany z frankiem francuskim i przez to powiązanie z euro; w 2015 roku Maroko przeszło na koszykówkę euro i dolarów amerykańskich, a bank centralny etapami rozszerza pas wahań w ramach stopniowej liberalizacji. Transakcje rachunku bieżącego są w większości wymienialne, ale przepływy rachunku kapitałowego pozostają kontrolowane."),
        ("p", "Taka konstrukcja pasuje gospodarce rozciąganej między Europą a resztą świata: Francja i Hiszpania dominują w handlu, z UE przyjeżdżają miliony turystów, a marokańska diaspora we Francji, Hiszpanii, we Włoszech i w krajach Beneluksu wysyła do domu jedne z największych strumieni przekazów w Afryce."),
        ("h", "Co wpływa na kurs walutowy MAD"),
        ("p", "Dirham nie pływa swobodnie, więc jego siłami napędowymi jest ekonomia stojąca za powiązaniem i tempo marokańskiej liberalizacji."),
        ("li", "Powiązanie z euro: Europa to dominujący partner handlowy Maroka, więc udział euro w koszykówce najbardziej trafia eksporterom i importerom"),
        ("li", "Turystyka i przekazy: miliony gości i wielka diaspora dostarczają dewiz, które finansują rachunek importowy"),
        ("li", "Fosforyty i przemysł: Maroko to jeden z czołowych światowych eksporterów fosforytów, który zbudował poważną produkcję motoryzacyjną i lotniczą dla europejskich klientów"),
        ("li", "Susza i rolnictwo: zbiory zależne od deszczu huśtają dochody wsi i import żywności, a lata z mało deszczu zawodnie obciążają gospodarkę"),
        ("h", "Dirham marokański w praktyce"),
        ("p", "Maroko działa na gotówce dokładnie tam, gdzie kochają je podróżni — medyny, suki, grand taxi i przydrożne kawiarnie — podczas gdy karty i płatności zbliżeniowe działają sprawnie w miastach, hotelach i większych restauracjach. Miej drobne banknoty: targowanie się na suku z dużym nominałem to otwarcie przegrywającego, a sprzedawcy rzadko mają resztę."),
        ("p", "Dirham to oficjalnie waluta zamknięta: obowiązują limity przywozu i wywozu, a strona wywozowa jest szczelna. Wymień pozostałe dirhamy w licencjonowanym biurze przed wyjazdem — kantor lotniskowy je przyjmie, ale uliczny nawoływacz nie da kursu wartego zachodu. Przekazy od diaspory są ogromne i konkurencyjne: banki, wyspecjalizowani operatorzy i sieci gotówkowe kwotują różne efektywne kursy, więc porównuj kwotę dirhamów faktycznie otrzymanych."),
        ("h", "Popularne konwersje dirhama marokańskiego"),
        ("p", "EUR/MAD to para, która naprawdę się liczy — większość marokańskiego handlu, turystyki i pieniędzy diaspory porusza się wobec euro. USD/MAD i GBP/MAD obsługują amerykańskich i brytyjskich gości oraz firmy, a CAD/MAD odzwierciedla rosnącą społeczność marokańską w Kanadzie. W samym Maroku sprawdzaj zawsze, czy cena podana w euro nie wykorzystuje własnego, korzystnego dla sprzedawcy kursu."),
    ],
    "faq": [
        ("Czy dirham marokański jest powiązany kursowo?",
         "Tak. Dirham jest zarządzany wobec koszykówki euro i dolarów amerykańskich (od 2015 roku, wcześniej faktycznie euro i frank francuski), a pas wahań jest stopniowo rozszerzany, gdy Bank al-Maghrib liberalizuje reżim."),
        ("Czy można wywieźć dirhamy marokańskie z kraju?",
         "Tylko w limitach — dirham to oficjalnie waluta zamknięta, a jej wywóz jest ograniczony. Wymień pozostałe banknoty w licencjonowanym biurze wymiany przed wyjazdem i zachowaj paragony, jeśli planujesz zamienić niewykorzystane dirhamy z powrotem."),
        ("Czy w Maroku opłaca się płacić w euro?",
         "Nie. Niektóre hotele i sklepy turystyczne kwotują w euro, ale ich kursy konwersji bywają zwykle kiepskie. Płać w dirhamach albo kartą w dirhamach i odrzucaj każdą propozycję terminala, by przeliczyć Twoją walutę domową przy kasie."),
    ],
}

# ─────────────────────────── QAR ───────────────────────────
ARTICLES_B2["QAR"] = {
    "sections": [
        ("h", "Krótka historia riala katarskiego"),
        ("p", "Przed rialem Katar używał rupii indyjskiej, a potem rupii Zatoki wspólnie z sąsiadami. W 1966 roku Katar i sąsiedni emirat Dubaj utworzyły wspólną radę walutową i wyemitowały riala na użytek obojga; gdy Dubaj w 1971 roku dołączył do Zjednoczonych Emiratów Arabskich, Katar poszedł własną drogą, a rial katarski od 1973 roku emituje Katarska Agencja Monetarna — dzisiejszy Katarski Bank Centralny, utworzony w 1993 roku."),
        ("p", "Jak większość walut Zatoki, rial to waluta o sztywnym kursie. Po wcześniejszych powiązaniach ze specjalnymi prawami ciągnienia i koszykówką walut Katar od 2001 roku powiązał riala z dolarem amerykańskim po około 3,64 riala za dolara. Powiązanie przeszło próbę podczas blokady dyplomatycznej w Zatoce w latach 2017–2021, gdy część kontrahentów przez chwilę wątpiła, czy się utrzyma — utrzymało się, podparte ogromnymi rezerwami i dochodami ze skroplonego gazu ziemnego."),
        ("p", "Katar to jeden z czołowych światowych eksporterów LNG, a dochody z węglowodorów obracają budżetem państwa, Katarską Organizacją Inwestycyjną i systemem bankowym, które razem stanowią główne centra popytu na walutę. Dzięki tym dochodom mały półwysep może trzymać sztywny kurs przez naftowe cykle, które zatapiają inne waluty."),
        ("h", "Co wpływa na kurs walutowy QAR"),
        ("p", "Przy powiązaniu z dolarem rial jest w gruncie rzeczy pochodną dolara amerykańskiego — ciekawym pytaniem jest zawsze wiarygodność powiązania, nie kurs dzienny."),
        ("li", "Powiązanie z dolarem: Katarski Bank Centralny trzyma riala na poziomie około 3,64 za dolara, więc QAR porusza się tylko wtedy, gdy inne waluty poruszają się wobec dolara"),
        ("li", "Dochody z węglowodorów: zyski z LNG i ropy finansują budżet, rezerwy i fundusz majątkowy, które stoją za powiązaniem"),
        ("li", "Siła rezerw i wiarygodność: głębokie rezerwy zagraniczne i zdrowy system bankowy to to, co pozwala powiązaniu przetrwać szoki polityczne"),
        ("li", "Polityka regionalna: blokada z lat 2017–2021 pokazała, że nastroje inwestorów wobec Kataru, nie tylko ekonomia, potrafią na chwilę docisnąć walutę"),
        ("h", "Rial katarski w praktyce"),
        ("p", "Doha jest w pełni przyjazna kartom — hotele, galerie, taksówki i większość restauracji przyjmuje płatności zbliżeniowe — ale miej riale gotówką do suków, małych bufetów i starszych taksówkarzy. Katar jest drogi na tle regionu, a sztywne powiązanie oznacza, że z dolarem nie ma żadnej gry na terminy: kurs po prostu jest taki, jaki jest."),
        ("p", "Poza Zatoką rial trudno wymienić. Kantory w Europie czy Azji rzadko go mają w ofercie, więc przelicz pozostałe banknoty przed wylotem do domu. W samym Katarze zdecydowana większość mieszkańców to ekspaci, a kraj wysyła jedne z największych na świecie strumieni przekazów na osobę — korytarze do Indii, Filipin, Nepalu, Bangladeszu i Egiptu są głębokie i konkurencyjne, więc porównywanie łącznej kwoty otrzymanej naprawdę się opłaca."),
        ("h", "Popularne konwersje riala katarskiego"),
        ("p", "USD/QAR jest sztywny na poziomie około 3,64 i stanowi nudną, ale niezbędną referencję wszystkiego wycenianego w dolarach. INR/QAR i PHP/QAR obsługują dwa z największych ekspackich korytarzy przekazowych, a BDT/QAR i NPR/QAR to ważne południowoazjatyckie trasy. EUR/QAR i GBP/QAR to praktyczne pary europejskich podróżnych i firm."),
    ],
    "faq": [
        ("Czy rial katarski jest powiązany z dolarem?",
         "Tak. Katar powiązał riala z dolarem amerykańskim po około 3,64 za dolara od 2001 roku, po wcześniejszych powiązaniach ze specjalnymi prawami ciągnienia i koszykówką. Powiązanie przetrwało regionalną blokadę z lat 2017–2021."),
        ("Czy w Katarze można płacić dolarami amerykańskimi?",
         "Niektóre hotele i duże sklepy mogą kwotować w dolarach, ale reszta zwykle wraca w rialach, a ukryty w tym kurs rzadko jest po Twojej stronie. Płać w rialach albo kartą i pozwól sieci kartowej prowadzić konwersję."),
        ("Dlaczego rial ma tak stabilny kurs?",
         "Sztywne powiązanie, gigantyczne rezerwy i czołowe dochody z LNG czynią QAR jedną z najstabilniejszych walut świata. Stabilny kurs to wybór polityczny, nie znak, że rynek śpi."),
    ],
}

# ─────────────────────────── TZS ───────────────────────────
ARTICLES_B2["TZS"] = {
    "sections": [
        ("h", "Krótka historia szylinga tanzańskiego"),
        ("p", "Tanzania narodziła się w 1964 roku z unii Tanganiki i Zanzibaru, a w 1966 roku Bank Tanzanii wyemitował szylinga tanzańskiego, zastępując szylinga wschodnioafrykańskiego współdzielonego z Kenią i Ugandą. Nowy kraj, nowa waluta — ale znajome oblicze dla każdego, kto handlował w Afryce Wschodniej."),
        ("p", "Pierwsze dekady szylinga ukształtował socjalistyczny eksperyment Ujamaa, zapowiedziany deklaracją z Aruszy z 1967 roku: banki znacjonalizowano, państwo prowadziło gospodarkę, a walutą administrowano ściśle. Liberalizacja od połowy lat 80. odbudowała gospodarkę rynkową, a szyling od lat 90. handlowany jest w zarządzanym pływaniu."),
        ("p", "Współczesna Tanzania opiera się na złocie — swoim największym eksporcie — obok nerkowców, kawy i kamienia szlachetnego tanzanitu, znajdowanego niemal nigdzie indziej na Ziemi. Filar stanowi turystyka: Serengeti, Kilimandżaro i plaże Zanzibaru ciągną gości z każdego kontynentu, a odkrycia gazu na morzu obiecują więcej. Przez 2023 i 2024 rok szyling był pod presją popytu importowego, a Bank Tanzanii zacieśniał politykę, by go ustabilizować."),
        ("h", "Co wpływa na kurs walutowy TZS"),
        ("p", "Szyling pływa pod nadzorem, a jego siłami napędowymi są eksport, turyści i import gospodarki, która wciąż buduje swoją bazę przemysłową."),
        ("li", "Eksport złota i płodów rolnych: złoto, nerkowce i kawa dominują przychody towarowe, więc światowe ceny surowców trafiają do waluty wprost"),
        ("li", "Turystyka: parki na stałym lądzie i Zanzibar przynoszą sezonowe dewizy, skoncentrowane w szczycie sezonu"),
        ("li", "Import i port: paliwo, maszyny i towary konsumpcyjne trzeba opłacać w dolarach, a port w Dar es Salaam obsługuje też śródlądowych sąsiadów, dodając popyt regionalny"),
        ("li", "Polityka Banku Tanzanii: decyzje o stopach, interwencje i zarządzanie rezerwami ustabilizowują szylinga w zarządzanym pływaniu"),
        ("h", "Szyling tanzański w praktyce"),
        ("p", "Tanzania poza miastami to gospodarka gotówki: targi, minibusy dala-dala, uliczne jedzenie i większość zanzibarskich pensjonatów żyje z banknotów szylingów. Pieniądz mobilny jest jednak wszędzie — M-Pesa od Vodacom i konkurenci powtarzają kenijski sukces — a karty działają w hotelach, safari lodge i miejskich restauracjach. W parkach narodowych i biurach promów płatności często idą przez terminale albo oficjalne aplikacje, ale ich niezawodność bywa różna, więc miej zapasową gotówkę. Noś też drobne banknoty — wydawanie reszty to przewlekły problem na straganach."),
        ("p", "Szyling jest w praktyce walutą zamkniętą: prawie żaden kantor za granicą go nie ma w ofercie, więc wymieniaj po przybyciu i przelicz resztę przed wyjazdem. W przekazach strumienie Tanzanii są mniejsze niż kenijskie, ale rosną, napływając ze Stanów Zjednoczonych, Europy i Zatoki, często prosto do portfeli mobilnych. Dla firm i operatorów safari ceny kwotuje się zwykle w dolarach, a koszty płaci w szylingach, więc kurs to żywy problem marży — i opłaty parkowe, wypisywane w dolarach, rozlicza się przez tę samą konwersję."),
        ("h", "Popularne konwersje szylinga tanzańskiego"),
        ("p", "USD/TZS to para odniesienia turystyki, importu i gospodarki portowej. EUR/TZS i GBP/TZS obsługują europejskich podróżnych i przepływy związane z pomocą rozwojową, a KES/TZS to kluczowa para regionalna dla handlu i podróży wewnątrz Wspólnoty Afryki Wschodniej."),
    ],
    "faq": [
        ("Kiedy wprowadzono szylinga tanzańskiego?",
         "W 1966 roku, gdy Bank Tanzanii wyemitował go w miejsce szylinga wschodnioafrykańskiego, dwa lata po połączeniu Tanganiki i Zanzibaru w Tanzanię."),
        ("Czy szyling tanzański jest powiązany kursowo?",
         "Nie. Szyling handlowany jest w zarządzanym pływaniu, a Bank Tanzanii wygładza wahania, zamiast bronić sztywnego poziomu."),
        ("Czy w Tanzanii można używać dolarów amerykańskich?",
         "Częściowo. Opłaty parkowe, safari i część cen lodge'ów kwotowane są w dolarach, ale codzienne płatności wymagają szylingów, a lokalne płacenie w dolarach zwykle oznacza kiepski kurs. Noś szylingi gotówką na targi i transport."),
    ],
}

# ─────────────────────────── UAH ───────────────────────────
ARTICLES_B2["UAH"] = {
    "sections": [
        ("h", "Krótka historia hrywny ukraińskiej"),
        ("p", "Hrywna bierze nazwę od waluty średniowiecznej Rusi Kijowskiej, gdzie hrywna była jednostką wagi i płatności wyliczaną w srebrze. Współczesna wersja nadeszła we wrześniu 1996 roku, gdy Bank Narodowy Ukrainy zastąpił tymczasowe kupony karbowanica w stosunku około 100 000 starych jednostek za jedną hrywnię, niemal z dnia na dzień kończąc jedną z najostrzejszych inflacji lat posowieckich."),
        ("p", "Młoda waluta przeszła próbę wcześnie. Konflikt z Rosją w latach 2014–2015 zaciął dolarową wartość hrywny o około dwie trzecie i zmusił Bank Narodowy do podniesienia stóp, ograniczenia przepływów kapitału i przyjęcia wsparcia MFW. Od tego czasu bank centralny przeszedł na targetowanie inflacji i bardziej elastyczny kurs, stopniowo odbudowując rezerwy i wiarygodność."),
        ("p", "Pełnoskalowa inwazja w 2022 roku przyniosła najtrudniejszy sprawdzian: Bank Narodowy utrzymał kurs na stałym poziomie, ograniczył wypłaty i transfery transgraniczne i pilnował, by system płatniczy działał mimo ataków na infrastrukturę. Gdy warunki pozwalały, bank rozluźniał kontrole i wracał do bardziej zarządzanego, elastycznego kursu, podparty kredytami MFW i dużymi transferami od Ukrainczyków za granicą."),
        ("h", "Co wpływa na kurs walutowy UAH"),
        ("p", "Hrywna to waluta zarządzana: to Bank Narodowy Ukrainy, nie rynek, ma ostatnie słowo o kursie — zwłaszcza na czas wojny."),
        ("li", "Wojna i bezpieczeństwo: wydarzenia wojskowe, ataki na infrastrukturę energetyczną i ogólny przebieg konfliktu przykrywają wszystko inne w tej walucie"),
        ("li", "Kontrola kapitału i polityka NBU: kluczowa stopa, limity przesyłania pieniędzy za granicę i bezpośrednie interwencje kształtują kurs oficjalny"),
        ("li", "Programy MFW i rezerwy: międzynarodowe finansowanie i poziom rezerw walutowych podpierają zaufanie do hrywny"),
        ("li", "Handel i przekazy: eksport zbóż, metali i żywności równoważy import paliwa i energii, a transfery od ukraińskich pracowników — zwłaszcza w UE — dostarczają dewiz"),
        ("h", "Hrywna ukraińska w praktyce"),
        ("p", "W Ukrainie karty i płatności telefonem są powszechne nawet u drobnych sprzedawców, a bankomaty w miastach działają niezawodnie, choć sieci mogą padać przy przerwach w dostawie prądu — gotówka to zapas, który trzyma każdy. Weź dolary lub euro w czystych banknotach, by w razie potrzeby wymienić je w licencjonowanych punktach, i zawsze płać w hrywnach: sprzedawca, który kwotuje w dolarach, nie robi Ci żadnej przysługi."),
        ("p", "Hrywna to w praktyce waluta zamknięta za granicą. Poza Ukrainą i garstką sąsiednich rynków wymiany niewiele punktów ją kwotuje, więc zaplanuj wydanie albo przeliczenie gotówki przed opuszczeniem kraju. Sprawdź aktualne zasady Banku Narodowego przed podróżą, bo limity przywozu i wywozu gotówki od 2022 roku zmieniały się wielokrotnie."),
        ("p", "W przekazach Ukraina była w ostatnich latach jednym z największych odbiorców w Europie: rodziny otrzymują pieniądze od pracowników w Polsce, Niemczech, Czechach i nie tylko. Dominują licencjonowane systemy przekazów i banki; porównuj kwotę hrywien otrzymanych od początku do końca, bo opłaty i marże walutowe różnią się mocno. Firmy muszą liczyć się z zasadami rozliczeń Banku Narodowego dla płatności handlowych, więc kontrakty eksportowe i importowe wymagają aktualnej porady regulacyjnej, a nie starych wzorców."),
        ("h", "Popularne konwersje hrywny"),
        ("p", "USD/UAH to para odniesienia i kotwica cen dla oszczędzających i importerów, a EUR/UAH ma znaczenie dla handlu z UE. PLN/UAH to jedna z najważniejszych par regionu: miliony Ukraińców żyje i pracuje w Polsce, a przemieszczenie ludności od 2022 roku uczyniło z niej rdzeniowy korytarz przekazowy. GBP/UAH i CAD/UAH obsługują szeroką ukraińską diasporę."),
    ],
    "faq": [
        ("Czy hrywnę ukraińską można wymienić poza Ukrainą?",
         "Tylko wyjątkowo. Płynność poza Ukrainą i garstką sąsiednich rynków jest szczupła, a banki gdzie indziej rzadko ją mają w ofercie. Wymień gotówkę na hrywny po przybyciu i z powrotem przed wyjazdem, sprawdzając aktualne limity Banku Narodowego Ukrainy."),
        ("Dlaczego kurs UAH jest kontrolowany?",
         "Bank Narodowy zarządza kursem, by chronić rezerwy oraz utrzymać stabilne ceny i działający system płatniczy — najpierw po 2014 roku, a od 2022 roku jeszcze ściślej. Ograniczenia luzowano etapami, gdy warunki pozwalały."),
        ("Czy warto mieć gotówkę na Ukrainie?",
         "Tak, miej trochę. Karty i płatności telefonem są szeroko przyjmowane w miastach, ale przerwy w prądzie, tereny wiejskie i małe rynki sprawiają, że rozsądnym zapasem są hrywny w gotówce — plus niewielka rezerwa dolarów albo euro."),
    ],
}

# ─────────────────────────── XAF ───────────────────────────
ARTICLES_B2["XAF"] = {
    "sections": [
        ("h", "Krótka historia franka CFA Afryki Środkowej"),
        ("p", "Frank CFA Afryki Środkowej dzieli urodziny ze swoim zachodnim bliźniakiem: powstał 26 grudnia 1945 roku, w dniu ratyfikacji układów z Bretton Woods przez Francję, jako część kolonialnej architektury walutowej. Ta gałąź obsługiwała Francuską Afrykę Równikową i Kamerun, a od wczesnych lat 70. emituje ją Bank Państw Afryki Środkowej (BEAC) z siedzibą w Jaunde."),
        ("p", "Używa go sześć krajów: Kamerun, Republika Środkowoafrykańska, Czad, Republika Konga, Gwinea Równikowa i Gabon. Gwinea Równikowa, była kolonia hiszpańska, dołączyła w 1985 roku. Powiązanie definiujące tę walutę ewoluowało od franka francuskiego do euro, po tej samej sztywnej stawce co wersja zachodnia — 655,957 franka CFA za euro — i obie gałęzie poruszają się razem od tamtej pory, włącznie z jednodniową dewaluacją o 50 procent w 1994 roku."),
        ("p", "To, co odróżnia strefę środkowoafrykańską, to baza gospodarcza: dominuje ropa — Gabon, Kongo, Czad i Gwinea Równikowa to producenci, a Kamerun prowadzi największą, zdywersyfikowaną gospodarkę regionu i jego port bramy. Rurociąg Czad–Kamerun, otwarty w 2003 roku, symbolizuje rzeczywistość strefy — węglowodory płyną, a wszystko inne często podróżuje przez Dualę."),
        ("h", "Co wpływa na kurs walutowy XAF"),
        ("p", "Jak przy zachodnim franku, powiązanie z euro przybija kurs w nagłówkach; prawdziwa historia to gospodarka ropy i drewna za nim."),
        ("li", "Ceny ropy: eksport ropy z Gabonu, Konga, Czadu i Gwinei Równikowej dominuje przychody dewizowe strefy, więc rynki energii znaczą więcej niż cokolwiek innego"),
        ("li", "Powiązanie z euro: XAF podąża za euro wobec dolara i wszystkiego innego dokładnie po 655,957 za euro"),
        ("li", "BEAC i system rezerw: wspólne rezerwy i układ konta operacyjnego z francuskim skarbem państwa podpierają wiarygodność powiązania"),
        ("li", "Korytarze regionalne: śródlądowy Czad i Republika Środkowoafrykańska zależą od tras przez Kamerun, więc logistyka handlu kształtuje podaż dolarów strefy równie mocno jak sama produkcja"),
        ("h", "Frank CFA Afryki Środkowej w praktyce"),
        ("p", "Te same banknoty i monety krążą we wszystkich sześciu krajach, co czyni podróże między Jaunde, Libreville a Brazzaville orzeźwiająco proste — żadnej wewnętrznej wymiany, żadnego łapania kursu na granicach. Karty działają w miejskich bankach, hotelach i supermarketach, ale region pozostaje mocno gotówkowy: noś banknoty w drobnych nominałach na targi, taksówki i mniejsze miasteczka."),
        ("p", "Wymienialność poza regionem jest ograniczona, więc wymień pozostałe franki przed wylotem — kantory zagraniczne niemal nigdy nie mają XAF w ofercie. Jedna praktyczna osobliwość: w części państw członkowskich banki potrafią zderzać się z okresowymi niedoborami dewiz, więc duże płatności w dolarach bywają kwestią planowania i cierpliwości. W przekazach główny korytarz prowadzi z Francji, choć strumienie są mniejsze niż zachodnioafrykańskie; porównywanie kwoty CFA otrzymanej nadal się opłaca, bo marże bankowe w strefie różnią się mocno. Dla firm sztywne powiązanie z euro usuwa ryzyko walutowe kontraktów europejskich, ale wprowadza siłę albo słabość euro w wszystko wyceniane w dolarach."),
        ("h", "Popularne konwersje franka CFA Afryki Środkowej"),
        ("p", "EUR/XAF to para definiująca, sztywna przez powiązanie na poziomie 655,957. USD/XAF to to, na co naprawdę patrzą firmy naftowe i traderzy surowców, GBP/XAF obsługuje brytyjskie i międzynarodowe powiązania biznesowe, a XAF/XOF — parytet z założenia — ma znaczenie, gdy pieniądze wędrują między dwiema strefami CFA."),
    ],
    "faq": [
        ("Czym różni się XAF od XOF?",
         "To dwie gałęzie tego samego systemu, emitowane przez różne banki centralne dla różnych regionów: XAF przez BEAC dla sześciu państw Afryki Środkowej, XOF przez BCEAO dla ośmiu państw Afryki Zachodniej. Oba są powiązane z euro po tej samej stawce i mają równą wartość, ale banknoty są odmienne."),
        ("Czy franki CFA Afryki Zachodniej działają w Afryce Środkowej?",
         "Banknoty są inne, a strefy prawnie rozdzielone, więc nie polegaj na tym — banki mogą przyjąć banknoty drugiej strefy po wartości nominalnej, ale nie mają takiego obowiązku. Wymiana między nimi wewnątrz regionu jest prosta."),
        ("Czy frank CFA Afryki Środkowej jest powiązany z euro?",
         "Tak, po 655,957 franka CFA za euro — tej samej sztywnej stawce co frank CFA Afryki Zachodniej. Przed euro obie gałęzie były powiązane z frankiem francuskim, a parytet przetrwał kilka przebudów systemu."),
    ],
}

# ─────────────────────────── XOF ───────────────────────────
ARTICLES_B2["XOF"] = {
    "sections": [
        ("h", "Krótka historia franka CFA Afryki Zachodniej"),
        ("p", "Frank CFA narodził się 26 grudnia 1945 roku — w dniu, gdy Francja ratyfikowała układy z Bretton Woods — jako frank francuskich kolonii Afryki, waluta stworzona po to, by osłaniać gospodarki kolonialne przed powojenną dewaluacją samej Francji. Nazwę dyplomatycznie przebrano później na frank Wspólnoty Finansowej Afryki, ale kości tego systemu są starsze niż większość jego państw członkowskich."),
        ("p", "Dziś frank CFA Afryki Zachodniej emituje Bank Centralny Państw Afryki Zachodniej (BCEAO) z siedzibą w Dakarze dla ośmiu krajów: Beninu, Burkina Faso, Wybrzeża Kości Słoniowej, Gwinei Bissau, Mali, Nigru, Senegalu i Togo. Gwinea Bissau, dawna kolonia portugalska, dołączyła w 1997 roku. Waluta jest powiązana z euro — wcześniej z frankiem francuskim — po sztywnej stawce 655,957 franka CFA za euro od 1999 roku i przetrwała nawet decyzję z 1994 roku o jednodniowym przecięciu jej wartości wobec franka francuskiego na pół."),
        ("p", "Układ wiąże się z francuską koneksją, która zdefiniowała jego politykę: państwa członkowskie łączą rezerwy i historycznie prowadziły konto operacyjne we francuskim skarbie państwa. Reformy ogłoszone pod koniec 2019 roku miały skończyć centralizację rezerw we Francji i przemianować walutę na eco, a państwa członkowskie zatwierdziły zmiany w 2020 roku — ale przejście wielokrotnie się opóźniało, a szerszy projekt wspólnej waluty ECOWAS przekładano nie raz, więc frank CFA krąży nadal w pełni sił."),
        ("h", "Co wpływa na kurs walutowy XOF"),
        ("p", "Wobec euro nic się nie porusza — w tym celu powiązanie istnieje. Ciekawa ekonomia to siły naciskające na samo powiązanie."),
        ("li", "Powiązanie z euro: jedno euro kupuje dokładnie 655,957 franka CFA, więc XOF rośnie i spada razem z euro wobec dolara i innych walut"),
        ("li", "Eksport kakao i surowców: Wybrzeże Kości Słoniowej to największy światowy producent kakao, a złoto, bawełna i ropa regionu napędzają podaż dewiz"),
        ("li", "Gwarancja francuskiego skarbu państwa: wspólne rezerwy i gwarancja dają powiązaniu rzadką wiarygodność — kosztem swobody monetarnej, rdzenia wieloletniej debaty o tej walucie"),
        ("li", "Regionalne plany reform: projekt eco i reformy z lat 2019–2020 kształtują oczekiwania, jak ta waluta będzie się nawet nazywać za dziesięć lat"),
        ("h", "Frank CFA Afryki Zachodniej w praktyce"),
        ("p", "Dla podróżnych ośmiokrajowa strefa jest wygodna wspaniale: te same banknoty działają od Dakaru przez Kotonu po Abidżan, bez wymiany na wewnętrznych granicach i bez ryzyka kursowego między członkami. Ceny są stabilne na tle regionu — powiązanie importuje europejską dyscyplinę cenową, a inflacja w strefie historycznie biegała znacznie poniżej sąsiadów z pływającymi walutami."),
        ("p", "Frank CFA jest wymienialny wobec euro przez system bankowy, ale gdzie indziej handluje się nim płytko, więc przelicz resztki przed opuszczeniem regionu. Codzienność szybko się cyfryzuje: usługi pieniądza mobilnego jak Orange Money i Wave dominują płatności w Senegalu i na Wybrzeżu Kości Słoniowej. W przekazach główne korytarze biegną z Francji, gdzie mieszka duża zachodnioafrykańska diaspora, a konkurencja między bankami i operatorami trzyma presję na opłaty — porównuj kwotę CFA otrzymaną, nie reklamowaną prowizję."),
        ("h", "Popularne konwersje franka CFA Afryki Zachodniej"),
        ("p", "EUR/XOF to para sztywna — samo powiązanie — i liczba, wokół której pisane są kontrakty regionalne. USD/XOF ma znaczenie dla kupujących surowce i fakturowania w dolarach, GBP/XOF obsługuje powiązania brytyjskie, a NGN/XOF to praktyczna para dla handlu przez nigeryjską granicę, gdzie spotykają się dwie bardzo różne filozofie monetarne."),
    ],
    "faq": [
        ("Czy frank CFA Afryki Zachodniej jest powiązany z euro?",
         "Tak, po sztywnej stawce 655,957 franka CFA za euro — parytecie odziedziczonym po powiązaniu z frankiem francuskim w 1999 roku. Powiązanie przetrwało wiele kryzysów, podparte wspólnymi rezerwami i gwarancją francuskiego skarbu państwa."),
        ("Które kraje używają XOF?",
         "Osiem państw Afryki Zachodniej: Benin, Burkina Faso, Wybrzeże Kości Słoniowej, Gwinea Bissau, Mali, Niger, Senegal i Togo. Sześć państw Afryki Środkowej używa odrębnego, lecz równowartościowego XAF, emitowanego przez inny bank centralny."),
        ("Czym jest eco?",
         "Eco to planowana waluta, która ma zastąpić franka CFA w ramach zachodnioafrykańskich reform monetarnych. Ogłoszona w 2019 roku i zatwierdzona przez państwa członkowskie w 2020 roku, zmiana była wielokrotnie przekładana, a frank CFA pozostaje w użyciu, podczas gdy regionalny projekt wspólnej waluty dojrzewa."),
    ],
}
