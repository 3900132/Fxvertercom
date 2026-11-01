# -*- coding: utf-8 -*-
"""Polskie treści dla stron par walutowych („USD na EUR").

PAIR_UI_L10N odpowiada ciągom z pair_pages.PAIR_UI["en"] (znaczniki {f} {t} {d}
pozostają nieprzetłumaczone), a PAIR_CONTENT_L10N — 15 parom z
PAIR_CONTENT["en"]; klucze są identyczne jak w wersji angielskiej.
build-lang-pages.py scala oba słowniki z PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Przelicznik na żywo",
    "pairRateHead": "Aktualny kurs wymiany",
    "pairAsOf": "Kurs referencyjny na {d}. Przelicznik na żywo powyżej zawsze pobiera najświeższy kurs — tabele poniżej to migawka z momentu budowy strony, służąca orientacji.",
    "pairAmounts": "Popularne kwoty: {f} na {t}",
    "pairReverse": "Popularne kwoty: {t} na {f}",
    "pairMore": "Więcej konwersji {f}",
    "pairMorePairs": "Więcej par walutowych",
    "pairIntroHead": "O kursie {f}/{t}",
    "pairCurLinks": "Strony walut",
    "pairMetaTmpl": ("Przelicz {f} na {t} według kursów na żywo: dzisiejszy kurs {f}/{t}, darmowy kalkulator, "
                     "tabele popularnych kwot i czynniki, które poruszają tą parą walutową."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD na EUR — dzisiejszy kurs, darmowy przelicznik i tabele kwot",
        "description": "Przelicz dolary amerykańskie na euro według kursów na żywo: dzisiejszy kurs USD/EUR, darmowy kalkulator, tabele popularnych kwot i co porusza tą parą.",
        "h1": "USD na EUR — przelicz dolary amerykańskie na euro",
        "intro": [
            "USD/EUR to najczęściej handlowana para walutowa świata — około jednej czwartej całego obrotu walutowego — dzięki czemu ma najwęższe spready i najgłębszy rynek ze wszystkich konwersji. Kurs to po prostu cena jednego dolara amerykańskiego w euro, wyznaczana w sposób ciągły przez handel światowy, przepływy inwestycyjne i lukę stóp procentowych między Fed a Europejskim Bankiem Centralnym.",
            "Przy codziennych przewalutowaniach praktyczne pytanie brzmi, jaką marżę płacisz ponad kurs średni pokazany tutaj. Banki typowo doliczają 1–4 procent; usługi kartowe i transferowe różnią się bardzo. Sprawdzenie kursu na żywo przed zakupem lub przelewem mówi natychmiast, czy oferta jest uczciwa.",
        ],
        "faq": [
            ("Jak wyznaczany jest kurs USD na EUR?",
             "Pływa swobodnie — podaż i popyt na obie waluty ustalają cenę całą dobę, pod wpływem głównie polityki stóp Fed i EBC, inflacji po obu stronach Atlantyku i globalnych nastrojów ryzyka. Nie ma żadnego sztywnego ani zarządzanego celu."),
            ("Kiedy najlepiej przeliczać USD na EUR?",
             "Płynność jest największa, a spready najwęższe, gdy nakładają się sesje europejska i amerykańska (w przybliżeniu 13:00–17:00 UTC). Nikt nie potrafi wiarygodnie przewidzieć krótkoterminowego kierunku, więc przy dużych kwotach bezpieczniej jest przeliczać transzami, niż czekać na lepszy dzień."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD na GBP — kurs dolara do funta, przelicznik i tabele kwot",
        "description": "Przelicz dolary amerykańskie na funty brytyjskie według kursów na żywo: dzisiejszy kurs USD/GBP, darmowy kalkulator, tabele kwot i co porusza funtem.",
        "h1": "USD na GBP — przelicz dolary amerykańskie na funty brytyjskie",
        "intro": [
            "Kurs dolara do funta, noszący przydomek „cable” od transatlantyckiego kabla telegraficznego, który po raz pierwszy przeniósł go w latach 60. XIX wieku, należy do najstarszych nieprzerwanie notowanych kursów wymiany na świecie. Dziś odzwierciedla lukę stóp między Fed a Bankiem Anglii, brytyjską inflację oraz stan handlu i finansów publicznych Wielkiej Brytanii.",
            "Sterling handlowany jest najaktywniej w godzinach londyńskich, a para ma skłonność do ostrych ruchów wokół brytyjskich danych gospodarczych i ogłoszeń fiskalnych. Porównanie każdej oferty z kursem średnim poniżej to najszybszy sposób, by zobaczyć, ile marży bierze dostawca.",
        ],
        "faq": [
            ("Dlaczego funt brytyjski jest wart więcej niż dolar amerykański?",
             "Wyższa cena jednostki nie oznacza silniejszej gospodarki — odzwierciedla historię i nominały. Funt był dominującą walutą świata, gdy dolara jeszcze nie było; sama liczba nie mówi nic o względnej sile gospodarczej ani o sile nabywczej."),
            ("Co porusza USD/GBP najmocniej?",
             "Decyzje o stopach Fed i Banku Anglii, brytyjskie odczyty inflacji oraz polityczne i fiskalne wieści z Westminsteru. Głosowanie o brexicie w 2016 roku zgoliło funta o około 10 procent w jeden dzień — przypomnienie, że sterling niesie ryzyko polityczne, którego nie znosi większość głównych walut."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD na JPY — dzisiejszy kurs dolara i jena, darmowy przelicznik i tabele",
        "description": "Przelicz dolary amerykańskie na jeny według kursów na żywo: dzisiejszy kurs USD/JPY, darmowy kalkulator, tabele kwot i co porusza jenem.",
        "h1": "USD na JPY — przelicz dolary amerykańskie na jeny japońskie",
        "intro": [
            "USD/JPY to druga najczęściej handlowana para świata i klasyczny barometr luki stóp procentowych między Stanami Zjednoczonymi a Japonią. Ponieważ japońskie stopy przez dekady siedziały blisko zera, jen stał się ulubioną walutą finansowania świata — słabnie, gdy rynki są pewne siebie, i gwałtownie mocnieje, gdy kryzysy domykają te pozycje.",
            "Parą wstrząsa też oficjalna japońska interwencja: Ministerstwo Finansów wielokrotnie kupowało jeny, gdy ten spadał zbyt daleko i zbyt szybko. Duże przewalutowania najlepiej weryfikować względem kursu średniego, bo detaliczne marże przy JPY potrafią być zaskakująco szerokie.",
        ],
        "faq": [
            ("Dlaczego jen czasem tak mocno spada wobec dolara?",
             "Głównie przez lukę stóp procentowych. Gdy stopy amerykańskie są wysokie, a japońskie bliskie zera, inwestorzy sprzedają jeny, by kupować wyżej oprocentowane aktywa w dolarach — to carry trade. Jen może sunąć w dół miesiącami, po czym skoczyć gwałtownie, gdy te transakcje się domykają."),
            ("Czy japoński rząd może zmienić kurs USD/JPY?",
             "Może działać przeciw rynkowi, ale go nie odwróci. Japonia interweniowała, kupując albo sprzedając jeny, gdy ruchy stawały się nieuporządkowane — czasem z dziesiątkami miliardów dolarów w pojedynczym epizodzie. Interwencja wygładza ścieżkę; rzadko zmienia długoterminowy kierunek wyznaczany przez fundamenty."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD na CNY — kurs dolara do juana, przelicznik online i tabele kwot",
        "description": "Przelicz dolary amerykańskie na juany według kursów na żywo: dzisiejszy kurs USD/CNY, darmowy kalkulator, tabele kwot i jak działa zarządzany kurs.",
        "h1": "USD na CNY — przelicz dolary amerykańskie na juany chińskie",
        "intro": [
            "Kurs dolara do juana to największa para walutowa zarządzana przez bank centralny. Każdego ranka Ludowy Bank Chin ustala dzienny kurs centralny (fixing), a kurs krajowy (CNY) może poruszać się tylko w pasie wokół niego — dlatego USD/CNY porusza się z dnia na dzień znacznie mniej, niż sugerowałaby jego waga gospodarcza.",
            "Kształtują go chińska nadwyżka handlowa, kontrola kapitału i cele polityki. Przy przewalutowaniach pamiętaj, że krajowy CNY i offshore'owy CNH mogą się lekko różnić, a prywatna wymiana walut w Chinach podlega zasadom kontroli kapitału. Zawsze porównuj oferty z kursem referencyjnym poniżej.",
        ],
        "faq": [
            ("Czy juan chiński jest w pełni wymienialny?",
             "Nie w całości. Przewalutowanie związane z handlem jest łatwe, ale przepływy inwestycyjne przez granicę podlegają kwotom i zezwoleniom. Dlatego offshore'owy CNH notowany jest lekko inaczej niż krajowy CNY — luka pokazuje, jak drogo kosztuje przenoszenie pieniędzy przez granicę."),
            ("Dlaczego USD/CNY prawie się nie porusza w porównaniu z innymi parami?",
             "Bo zarządza nim bank centralny. Dzienny fixing i pas handlowy utrzymują kurs stabilny względem dolara, zgodnie z chińską preferencją przewidywalności w handlu. Zarządzanie nie znaczy sztywność: przez miesiące i lata kurs i tak dryfuje razem z fundamentami."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD na INR — dzisiejszy kurs, darmowy przelicznik i tabele przekazów",
        "description": "Przelicz dolary amerykańskie na rupie indyjskie według kursów na żywo: dzisiejszy kurs USD/INR, darmowy kalkulator, tabele kwot i co porusza rupią.",
        "h1": "USD na INR — przelicz dolary amerykańskie na rupie indyjskie",
        "intro": [
            "USD/INR to jeden z najważniejszych korytarzy przekazowych świata — Indie otrzymują więcej przekazów niż jakikolwiek inny kraj — i mocno handlowana para rynku wschodzącego. Bank Rezerw Indii zarządza zmiennością, nie poziomem: wygładza ostre ruchy rezerwami, ale pozwala rupii znaleźć długoterminowy trend.",
            "Strukturalna historia rupii to stopniowa deprecjacja wobec dolara, napędzana różnicami inflacji i bilansem bieżącym Indii, przerywana globalnymi wstrząsami ryzyka. Dla każdego, kto wysyła pieniądze do Indii, luka między kursem średnim a oferowanym kursem to miejsce, gdzie kryje się prawdziwy koszt.",
        ],
        "faq": [
            ("Dlaczego rupia indyjska traci na wartości z czasem?",
             "Głównie przez różnice inflacyjne i deficyt handlowy: Indie importują znacznie więcej, niż eksportują, a różnicę finansują napływy kapitału. RBI wygładza ścieżkę, ale przez dekady rupia dryfowała stabilnie ku osłabieniu wobec dolara — co dla rozwijającej się gospodarki jest normalne."),
            ("Jak dostać najlepszy kurs przy wysyłce pieniędzy do Indii?",
             "Porównuj oferowany kurs z kursem średnim przed wysyłką, a nie tylko opłaty. Wyspecjalizowane usługi przekazowe zwykle biją przelewy bankowe na tym korytarzu, a różnica nawet 1 procent jest znacząca przy regularnych przelewach rodzinnych przez rok."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD na CAD — kurs dolara do loonie, przelicznik i tabele kwot",
        "description": "Przelicz dolary amerykańskie na dolary kanadyjskie według kursów na żywo: dzisiejszy kurs USD/CAD, kalkulator, tabele kwot i co porusza loonie.",
        "h1": "USD na CAD — przelicz dolary amerykańskie na dolary kanadyjskie",
        "intro": [
            "USD/CAD — „loonie” — to para z czołowej piątki świata, oparta na jednej z największych relacji handlowych na Ziemi. Kanada wysyła około trzech czwartych eksportu do Stanów Zjednoczonych, więc para handluje mocno na amerykańskim wzroście, cenach energii (Kanada to ważny eksporter ropy) i luce stóp między Fed a Bankiem Kanady.",
            "Gdy ropa rośnie, CAD zwykle mocnieje; gdy uderzają obawy o globalny wzrost, słabnie razem z walutami surowcowymi. Para jest płynna całą dobę, a oferty w ułamku procenta od kursu średniego łatwo znaleźć — szerokie marże zawsze warto zakwestionować.",
        ],
        "faq": [
            ("Dlaczego dolar kanadyjski nazywa się loonie?",
             "Od nurka (loon) — ptaka na 1-dolarowej monecie wprowadzonej w 1987 roku. Przydomek się przyjął i dziś w slangu walutowym oznacza samą walutę, jak w zdaniu „loonie dziś zyskał”."),
            ("Czy cena ropy naprawdę wpływa na USD/CAD?",
             "Tak, widocznie. Ropa i produkty powiązane to największa kategoria eksportu Kanady, więc rosnąca ropa przynosi do kraju więcej dolarów i podnosi CAD. Traderzy traktują tę parę jako zgrubny zakład na rynki energii, obok stóp obu krajów."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD na AUD — kurs dolara australijskiego dziś, przelicznik i tabele kwot",
        "description": "Przelicz dolary amerykańskie na dolary australijskie według kursów na żywo: dzisiejszy kurs USD/AUD, kalkulator, tabele kwot i co porusza Aussie.",
        "h1": "USD na AUD — przelicz dolary amerykańskie na dolary australijskie",
        "intro": [
            "Dolar australijski to klasyczna waluta surowcowa: jego losy śledzą eksport rudy żelaza, węgla i gazu, a przede wszystkim chiński popyt na te towary. USD/AUD jest dlatego jednym z najczystszych wskaźników czasu rzeczywistego globalnego apetytu na ryzyko — Aussie mocnieje, gdy światowy handel pędzi, i słabnie w epizodach ucieczki od ryzyka.",
            "Krótsze wahania napędza polityka stóp Reserve Bank of Australia i Fed. Populacje studenckie i pracujące wakacyjnie czynią z USD→AUD (i z powrotem) częste, powtarzalne przewalutowanie, gdzie nawet marża kursowa 1 procent szybko się kumuluje.",
        ],
        "faq": [
            ("Dlaczego dolar australijski jest tak wrażliwy na Chiny?",
             "Chiny to zdecydowanie największy rynek eksportowy Australii, zwłaszcza rudy żelaza do produkcji stali. Gdy chińskie budownictwo zwalnia, ceny surowców i AUD zwykle spadają razem — waluta działa jak barometr czasu rzeczywistego chińskiego przemysłu ciężkiego."),
            ("Czy AUD to bezpieczna przystań?",
             "Wręcz przeciwnie: traderzy nazywają go walutą risk-on. W globalnych panikach — 2008, 2020 — pieniądze płyną do dolarów amerykańskich, a Aussie spada zwykle najmocniej z głównych walut. Ta cykliczność to właśnie powód, dla którego traderzy carry i obserwatorzy wzrostu śledzą go tak uważnie."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD na CHF — kurs dolara do franka, darmowy przelicznik i tabele",
        "description": "Przelicz dolary amerykańskie na franki szwajcarskie według kursów na żywo: dzisiejszy kurs USD/CHF, kalkulator, tabele kwot i co porusza frankiem.",
        "h1": "USD na CHF — przelicz dolary amerykańskie na franki szwajcarskie",
        "intro": [
            "Frank szwajcarski to najlepsza bezpieczna przystań świata: gdy wybucha wojna, stres bankowy albo panika rynkowa, pieniądze płyną do Szwajcarii, a CHF mocnieje. USD/CHF dlatego zwykle spada w globalnych kryzysach, nawet gdy sam dolar jest schronieniem — frank jest po prostu silniejszą osłoną.",
            "Szwajcarski Bank Narodowy aktywnie kształtuje kurs — od słynnej podłogi 1,20 wobec euro z lat 2011–2015 po ciężkie interwencje od tamtej pory. Szwajcaria przypomina też, że para bogatego kraju wciąż może nosić szerokie detaliczne marże, zwłaszcza na lotniskach i w hotelach — zawsze sprawdzaj referencję kursu średniego.",
        ],
        "faq": [
            ("Dlaczego frank szwajcarski uchodzi za bezpieczną przystań?",
             "Wiek neutralności, niski dług, nadwyżka na rachunku bieżącym i wiarygodny bank centralny czynią z franka domyślne miejsce parkowania pieniędzy uciekających przed ryzykiem. Szwajcarska inflacja przez dekady biegała też znacznie poniżej amerykańskiej i strefy euro, chroniąc siłę nabywczą waluty."),
            ("Co SNB zrobił w styczniu 2015 roku?",
             "Nagle porzucił limit siły franka wobec euro. USD/CHF i EUR/CHF runęły o około 20–30 procent w kilka minut — jeden z największych ruchów intraday w historii głównej pary i powód, dla którego traderzy do dziś szanują hasło „ryzyko SNB”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD na MXN — dzisiejszy kurs peso, darmowy przelicznik i tabele kwot",
        "description": "Przelicz dolary amerykańskie na peso meksykańskie według kursów na żywo: dzisiejszy kurs USD/MXN, kalkulator, tabele kwot i co porusza peso.",
        "h1": "USD na MXN — przelicz dolary amerykańskie na peso meksykańskie",
        "intro": [
            "USD/MXN to najbardziej handlowana para rynku wschodzącego w obu Amerykach i jedna z najbardziej płynnych na świecie. Peso reaguje na wszystko, co porusza gospodarką USA — politykę handlową, wzrost, lukę stóp między Fed a Banxico — do tego ceny ropy i ogromny korytarz przekazowy ze Stanów Zjednoczonych.",
            "Ponieważ para jest tak płynna, szybko reaguje na globalne nastroje ryzyka: to klasyczny cel carry trade, który mocnieje na spokojnych rynkach i raptownie spada w panikach. Dla podróżnych i nadawców przekazów marże 3–6 procent są częste na lotniskach — kurs średni poniżej to punkt odniesienia do porównań.",
        ],
        "faq": [
            ("Dlaczego USD/MXN jest tak zmienny?",
             "Wysokie stopy w Meksyku przyciągają krótkoterminowy pieniądz carry, który w stresie szybko ucieka; peso to też aktywo referencyjne całego handlu i politycznych wieści między USA a Meksykiem. Razem to czyni je płynnym, ale nerwowym — duże ruchy dzienne są normą, nie usterką."),
            ("Jaki jest najtańszy sposób przesłania dolarów do Meksyku?",
             "Wyspecjalizowane usługi przekazowe regularnie biją banki i punkty transferów gotówkowych na tym korytarzu. Porównuj dostarczoną kwotę z kursem średnim: przy przekazie 300 dolarów różnica między uczciwą ofertą a marżą 5 procent może równać się całemu dziennemu zarobkowi na miejscu."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD na PHP — kurs dolara do peso filipińskiego, przelicznik i tabele",
        "description": "Przelicz dolary amerykańskie na peso filipińskie według kursów na żywo: dzisiejszy kurs USD/PHP, kalkulator, tabele kwot i co porusza peso.",
        "h1": "USD na PHP — przelicz dolary amerykańskie na peso filipińskie",
        "intro": [
            "Peso filipińskie trzymają jeden z największych strumieni przekazów na świecie: miliony Filipińczyków pracujących za granicą wysyłają pieniądze do domu, a te napływy dolarów to filar gospodarki. USD/PHP handluje odpowiednio na globalnym apetycie na ryzyko, cenach ropy (Filipiny to netto importer) i polityce Bangko Sentral ng Pilipinas.",
            "Kurs oficjalny jest zarządzany lekką ręką — bank centralny pozwala na stopniowe dostosowania, wygładzając szczyty. Dla rodzin OFW i podróżnych rozrzut marż między dostawcami na tym korytarzu jest szeroki, więc sprawdzenie kursu średniego przed wysyłką to najprostsza oszczędność ze wszystkich.",
        ],
        "faq": [
            ("Jak przekazy wpływają na peso filipińskie?",
             "Stabilne napływy dolarów od pracowników za granicą podtrzymują peso i bilans płatniczy kraju — co roku kilka procent PKB. Gdy rośnie globalne ryzyko albo słabną gospodarki przyjmujące, przekazy słabną, a peso zwykle podąża."),
            ("Czy lepiej przeliczyć USD na PHP w USA czy na Filipinach?",
             "Zależy to od dostawcy, nie od kraju. Po obu stronach korytarza są tanie i drogie opcje; rozstrzyga liczba peso, które odbiorca faktycznie dostaje. Porównuj oferty z kursem średnim, zamiast ufać najbliższemu punktowi."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR na GBP — dzisiejszy kurs euro do funta, darmowy przelicznik i tabele",
        "description": "Przelicz euro na funty brytyjskie według kursów na żywo: dzisiejszy kurs EUR/GBP, darmowy kalkulator, tabele kwot i co porusza tą parą.",
        "h1": "EUR na GBP — przelicz euro na funty brytyjskie",
        "intro": [
            "EUR/GBP to klasyczny kros europejski: dwie gospodarki, które wysyłają do siebie około połowy handlu, rozdzielone tylko granicą walutową. Ponieważ obie to rozwinięte, niskoinflacyjne waluty, para porusza się znacznie mniej niż krosy dolarowe — to naprawdę zakład na względne losy strefy euro i Wielkiej Brytanii.",
            "Luka stóp między EBC a Bankiem Anglii napędza większość trendu, a brytyjskie wieści polityczne i fiskalne dają skoki. Dla pracowników za kanałem, emerytów i firm stabilność pary sprawia, że drobne różnice kursowe znaczą jeszcze więcej: marża 1 procent to duża część całego rocznego ruchu.",
        ],
        "faq": [
            ("Dlaczego EUR/GBP jest spokojniejszy niż EUR/USD?",
             "Ani euro, ani funt nie są globalnymi walutami ryzyka, więc światowe ucieczki do bezpieczeństwa je omijają. Para odzwierciedla głównie względną ekonomię Wielkiej Brytanii i UE oraz różnice stóp, które zmieniają się powoli — choć potrafi ostro skoczyć przy brytyjskich wieściach politycznych, jak pokazał rok 2016."),
            ("Jak brexit wciąż wpływa na EUR/GBP?",
             "Strukturalnie. Nowe tarcia handlowe od 2021 roku zrobiły gospodarkę Wielkiej Brytanii nieco mniej otwartą na UE, co większość ekonomistów wiąże ze strukturalnie słabszym funtem. Każda runda negocjacji brytyjsko-unijnych o reguły handlowe do dziś porusza tą parą."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR na CHF — kurs euro do franka szwajcarskiego, przelicznik i tabele",
        "description": "Przelicz euro na franki szwajcarskie według kursów na żywo: dzisiejszy kurs EUR/CHF, darmowy kalkulator, tabele kwot i rola SNB przy tej parze.",
        "h1": "EUR na CHF — przelicz euro na franki szwajcarskie",
        "intro": [
            "EUR/CHF to europejski papier lakmusowy bezpiecznej przystani: gdy rośnie stres w strefie euro — kryzys zadłużeniowy 2011 roku, strach bankowy, wojna na kontynencie — pieniądze płyną przez szwajcarską granicę, a para spada. Szwajcarski Bank Narodowy patrzy na ten kurs uważniej niż na żaden inny i wielokrotnie interweniował, by frank nie zdusił szwajcarskiego eksportu.",
            "Nowoczesna historia pary jest dramatyczna: podłoga na 1,20 od 2011 roku, potem porzucenie podłogi w styczniu 2015 roku, które w kilka minut wywołało flash crash o 20–30 procent. Od tamtej pory frank handlowany jest jako czysta, choć czasem zbyt silna, przystań — a SNB pozostaje aktywnym uczestnikiem tego rynku.",
        ],
        "faq": [
            ("Dlaczego Szwajcarski Bank Narodowy tak bardzo troszczy się o EUR/CHF?",
             "Bo szwajcarska gospodarka sprzedaje do Europy. Zbyt mocny frank czyni szwajcarski eksport niekonkurencyjnym i ściąga inflację poniżej celu, więc SNB kupuje waluty zagraniczne (i raz wprowadził stopy ujemne), by przycinać siłę franka. Interweniuje w tej parze mocniej niż niemal każdy inny bank centralny dużego rynku."),
            ("Czy EUR/CHF to stabilna para do trzymania?",
             "Na spokojnie stabilna, w kryzysach wybuchowa — przeciwieństwo dywersyfikacji. Porzucenie podłogi w 2015 roku pozostaje podręcznikowym ostrzeżeniem, że obietnica banku centralnego dotycząca przycięcia waluty może zniknąć z dnia na dzień. Każdy, kto traktował tę parę jako pozbawioną ryzyka, nauczył się inaczej w jednym poranku."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR na PLN — dzisiejszy kurs euro do złotego, darmowy przelicznik i tabele",
        "description": "Przelicz euro na złote według kursów na żywo: dzisiejszy kurs EUR/PLN, darmowy kalkulator, tabele popularnych kwot i co porusza złotym.",
        "h1": "EUR na PLN — przelicz euro na złote polskie",
        "intro": [
            "Polska to szósta gospodarka UE, która wciąż używa własnej waluty, a złoty jest najbardziej handlowaną spośród walut unijnych spoza strefy euro. EUR/PLN handluje na luce stóp z Narodowym Bankiem Polskim, na funduszach UE płynących na wschód, na niemieckich zamówieniach dla polskiego przemysłu i na geopolitycznym ryzyku regionu.",
            "Od wejścia Polski do UE w 2004 roku złoty zarówno mocniał w boomach, jak i ciężko spadał w kryzysach — 2008 i 2022 rok doprowadziły parę do historycznych ekstremów. Przy nadal nierozstrzygniętej przyszłej adopcji euro para pozostanie strukturalnym elementem europejskich finansów na lata.",
        ],
        "faq": [
            ("Czy Polska przyjmie euro i zdejmie złotego?",
             "Polska jest prawnie zobowiązana do ostatecznego przyjęcia euro, ale nie ma daty docelowej, a sceptycyzm społeczny jest szeroki. Dopóki nie będzie wiarygodnego harmonogramu adopcji, EUR/PLN pozostaje aktywnie handlowaną parą — same polityczne wypowiedzi o kalendarzu potrafią nią poruszyć."),
            ("Dlaczego EUR/PLN skoczył w 2022 roku?",
             "Wojna w sąsiedniej Ukrainie zrobiła z Polski z dnia na dzień gospodarkę frontową: napływy uchodźców, wydatki obronne i szoki energetyczne mocno uderzyły w walutę. Narodowy Bank Polski interweniował, by wspierać złotego — to były najostrzejsze ruchy tej pary od dwóch dekad."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP na JPY — kurs funta do jena, darmowy przelicznik i tabele kwot",
        "description": "Przelicz funty brytyjskie na jeny według kursów na żywo: dzisiejszy kurs GBP/JPY, darmowy kalkulator, tabele kwot i co porusza tą zmienną parą.",
        "h1": "GBP na JPY — przelicz funty brytyjskie na jeny japońskie",
        "intro": [
            "GBP/JPY — dawni traderzy nazywali go „bestią” albo „smokiem” — to jedna z najbardziej zmiennych głównych par. Nakłada na siebie dwa silniki ryzyka: wrażliwość sterlinga na brytyjskie wieści polityczne i fiskalne oraz rolę jena jako waluty finansowania świata, która sprawia, że para ostro buja przy każdej odmianie nastrojów.",
            "To ulubiona para carry trade: pożyczasz jeny o stopach bliskich zeru, by kupować wyżej oprocentowane funty. Działa to aż do kryzysu, który zmusza wszystkich do domknięcia naraz — dlatego GBP/JPY potrafi tlić się w górę latami, a spaść gwałtownie w tygodnie. Wielkość pozycji i timing znaczą tu więcej niż przy prawie każdej innej dużej parze.",
        ],
        "faq": [
            ("Dlaczego GBP/JPY jest bardziej zmienny niż USD/JPY?",
             "Bo mnoży dwie zmienności. Sterling dokłada brytyjskie ryzyko polityczne i gospodarcze do globalnych nastrojów ryzyka, które i tak napędzają USD/JPY. Para nie ma wspólnej gospodarki-kotwicy, więc handluje się nią niemal czysto na lukach stóp i nastrojach — składnikach wielkich ruchów."),
            ("Czym jest carry trade w GBP/JPY?",
             "Pożyczaniem jenów po japońskich stopach bliskich zeru i inwestowaniem w funty po wyższych stopach brytyjskich, z inkasowaniem różnicy. Opłaca się, dopóki rynki są spokojne, i karze, gdy przestają być: w epizodach ucieczki od ryzyka jen eksploduje, gdy pozycje carry się domykają — często 10 procent i więcej wobec funta w ciągu miesięcy."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD na JPY — kurs dolara australijskiego do jena, przelicznik i tabele",
        "description": "Przelicz dolary australijskie na jeny według kursów na żywo: dzisiejszy kurs AUD/JPY, kalkulator, tabele kwot i co porusza tym barometrem ryzyka.",
        "h1": "AUD na JPY — przelicz dolary australijskie na jeny japońskie",
        "intro": [
            "AUD/JPY to najczystszy barometr ryzyka na rynku walutowym. Dolar australijski reprezentuje globalny wzrost i popyt surowcowy — przede wszystkim chiński popyt przemysłowy — podczas gdy jen reprezentuje bezpieczeństwo. Gdy światowa gospodarka się rozpędza, para wspina się; gdy przychodzi panika, spada szybciej niż niemal każdy inny główny kros.",
            "To też klasyczna para carry trade: przez dekady inwestorzy pożyczali tanie jeny, by kupować wyżej oprocentowanego Aussie. Ten strumień kształtuje długie, uparte trend wzrostowe pary i jej gwałtowne odwinięcia — 2008 rok pozostaje przestrogą, gdy AUD/JPY stracił w kilka miesięcy około połowy wartości.",
        ],
        "faq": [
            ("Dlaczego traderzy nazywają AUD/JPY barometrem ryzyka?",
             "Bo każda waluta siedzi na przeciwległym biegunie: Aussie rośnie z globalnym wzrostem i popytem surowcowym, jen rośnie ze strachem. Para porusza się dlatego z rynkami akcji świata w stopniu, którego mało który kros dorównuje — gdy twardo spada, ucieczka od ryzyka jest prawdziwa."),
            ("Co stało się z AUD/JPY w kryzysie 2008 roku?",
             "Został mniej więcej przepołowiony. Carry trade się odwinięło, gdy światowy kredyt zamarzł: inwestorzy sprzedawali dolary australijskie, by spłacić pożyczone jeny, a para runęła z ponad 100 do niskich 50 w kilka miesięcy. To do dziś standardowy przykład, jak szybko strategie carry się odwracają."),
        ],
    },
}
