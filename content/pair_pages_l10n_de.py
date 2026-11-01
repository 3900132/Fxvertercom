# -*- coding: utf-8 -*-
"""Deutsche Inhalte für die Währungspaar-Seiten ("USD in EUR").

PAIR_UI_L10N entspricht den Strings aus pair_pages.PAIR_UI["en"] ({f} {t} {d}
Platzhalter bleiben unverändert). PAIR_CONTENT_L10N entspricht den 15 Paaren
aus PAIR_CONTENT["en"], die Schlüssel sind identisch mit der englischen
Version. build-lang-pages.py führt beides in PAIR_UI / PAIR_CONTENT zusammen.
"""

PAIR_UI_L10N = {
    "pairConvert": "Live-Umrechner",
    "pairRateHead": "Aktueller Wechselkurs",
    "pairAsOf": "Referenzkurs vom {d}. Der Live-Umrechner oben ruft stets den neuesten Kurs ab — die Tabellen unten sind eine Momentaufnahme zum Erstellungszeitpunkt zur Orientierung.",
    "pairAmounts": "Gängige Beträge: {f} in {t}",
    "pairReverse": "Gängige Beträge: {t} in {f}",
    "pairMore": "Weitere {f}-Umrechnungen",
    "pairMorePairs": "Weitere Währungspaare",
    "pairIntroHead": "Über den {f}/{t}-Wechselkurs",
    "pairCurLinks": "Währungsseiten",
    "pairMetaTmpl": ("{f} in {t} umrechnen mit Live-Wechselkursen: der heutige {f}/{t}-Kurs, ein kostenloser Rechner, "
                     "Tabellen gängiger Beträge und was dieses Währungspaar bewegt."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD in EUR — Wechselkurs, Umrechner & Tabellen",
        "description": "US-Dollar in Euro umrechnen mit Live-Kursen: der heutige USD/EUR-Wechselkurs, ein kostenloser Rechner, Tabellen gängiger Beträge und was dieses Paar bewegt.",
        "h1": "USD in EUR — US-Dollar in Euro umrechnen",
        "intro": [
            "USD/EUR ist das meistgehandelte Währungspaar der Welt — rund ein Viertel des gesamten Devisenumsatzes —, weshalb es die engsten Spreads und den tiefsten Markt aller Umrechnungen hat. Der Kurs ist schlicht der Preis eines US-Dollars in Euro, fortlaufend bestimmt durch globalen Handel, Investitionsströme und den Zinsabstand zwischen Federal Reserve und Europäischer Zentralbank.",
            "Bei alltäglichen Umrechnungen ist die praktische Frage, welche Marge Sie über den hier gezeigten Mittelkurs zahlen. Banken schlagen typischerweise 1–4 % auf; Karten- und Überweisungsdienste variieren stark. Wer vor einem Kauf oder einer Überweisung den Live-Kurs prüft, erkennt sofort, ob ein Angebot fair ist.",
        ],
        "faq": [
            ("Wie wird der USD-zu-EUR-Wechselkurs bestimmt?",
             "Er schwankt frei — Angebot und Nachfrage nach den beiden Währungen setzen rund um die Uhr den Preis, beeinflusst vor allem von der Zinspolitik von Fed und EZB, der Inflation auf beiden Seiten des Atlantiks und der globalen Risikostimmung. Ein festes oder gesteuertes Ziel gibt es nicht."),
            ("Wann ist der beste Zeitpunkt, USD in EUR umzurechnen?",
             "Die Liquidität ist am tiefsten und die Spreads am engsten, wenn sich die europäischen und die US-Handelszeiten überschneiden (etwa 13:00–17:00 UTC). Niemand kann die kurzfristige Richtung zuverlässig vorhersagen; bei großen Beträgen ist es daher sicherer, in Teilen umzurechnen, als auf einen besseren Tag zu warten."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD in GBP — Wechselkurs, Umrechner & was das Pfund bewegt",
        "description": "US-Dollar in britische Pfund umrechnen mit Live-Kursen: der heutige USD/GBP-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was das Pfund bewegt.",
        "h1": "USD in GBP — US-Dollar in britische Pfund umrechnen",
        "intro": [
            "Der Kurs zwischen Dollar und Pfund, unter Händlern „Kabel“ (cable) genannt nach dem transatlantischen Telegrafenkabel, das ihn erstmals in den 1860er-Jahren übertrug, gehört zu den ältesten fortlaufend notierten Wechselkursen der Welt. Heute spiegelt er den Zinsabstand zwischen Federal Reserve und Bank of England, die britische Inflation und den Zustand von Großbritanniens Handel und Staatsfinanzen.",
            "Sterling handelt sich am aktivsten während der Londoner Stunden, und das Paar neigt zu scharfen Bewegungen rund um britische Konjunkturdaten und Finanzankündigungen. Jedes Angebot mit dem Mittelkurs unten zu vergleichen ist der schnellste Weg zu sehen, wie viel Marge ein Anbieter nimmt.",
        ],
        "faq": [
            ("Warum ist das britische Pfund mehr wert als der US-Dollar?",
             "Ein höherer Stückpreis bedeutet keine stärkere Wirtschaft — er spiegelt Geschichte und Stückelung wider. Das Pfund war die dominierende Währung der Welt, als der Dollar noch gar nicht existierte; die Zahl selbst sagt nichts über relative Wirtschaftskraft oder Kaufkraft."),
            ("Was bewegt USD/GBP am stärksten?",
             "Zinsentscheidungen von Fed und Bank of England, britische Inflationszahlen sowie politische und fiskalische Nachrichten aus Westminster. Beim Brexit-Votum 2016 fiel das Pfund an einem Tag um rund 10 % — eine Erinnerung daran, dass Sterling ein politisches Risiko trägt, das die meisten großen Währungen nicht kennen."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD in JPY — Wechselkurs, Umrechner & was den Yen bewegt",
        "description": "US-Dollar in japanische Yen umrechnen mit Live-Kursen: der heutige USD/JPY-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Yen bewegt.",
        "h1": "USD in JPY — US-Dollar in japanische Yen umrechnen",
        "intro": [
            "USD/JPY ist das zweitmeistgehandelte Währungspaar der Welt und der klassische Gradmesser für den Zinsabstand zwischen den USA und Japan. Da die japanischen Zinsen jahrzehntelang nahe null lagen, wurde der Yen zur beliebtesten Finanzierungswährung der Welt — er schwächelt, wenn die Märkte zuversichtlich sind, und zieht scharf an, wenn Krisen diese Positionen abwickeln.",
            "Beobachtet wird das Paar auch wegen offizieller japanischer Interventionen: Das Finanzministerium hat wiederholt Yen gekauft, wenn er zu weit und zu schnell fiel. Große Umrechnungen prüfen Sie am besten gegen den Mittelkurs, denn Einzelhandelsmargen beim JPY können täuschend breit sein.",
        ],
        "faq": [
            ("Warum fällt der Yen manchmal so stark gegenüber dem Dollar?",
             "Vor allem wegen des Zinsabstands. Sind die US-Zinsen hoch und die japanischen nahe null, verkaufen Anleger Yen, um höher verzinsliche Dollaranlagen zu kaufen — der Carry Trade. Der Yen kann monatelang rutschen und dann heftig springen, wenn diese Geschäfte abgewickelt werden."),
            ("Kann die japanische Regierung den USD/JPY-Kurs ändern?",
             "Sie kann dem Markt entgegenwirken, ihn nicht umkehren. Japan hat interveniert, indem es Yen kaufte oder verkaufte, wenn die Bewegungen ungeordnet wurden — mitunter mit zweistelligen Milliardenbeträgen in Dollar in einer einzigen Episode. Interventionen glätten den Weg; die langfristige Richtung der Fundamentaldaten ändern sie selten."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD in CNY — Wechselkurs, Umrechner & der gesteuerte Kurs",
        "description": "US-Dollar in chinesische Yuan umrechnen mit Live-Kursen: der heutige USD/CNY-Wechselkurs, ein kostenloser Rechner, Betragstabellen und wie der gesteuerte Kurs funktioniert.",
        "h1": "USD in CNY — US-Dollar in chinesische Yuan umrechnen",
        "intro": [
            "Der Kurs zwischen Dollar und Yuan ist das größte Währungspaar, das von einer Zentralbank gesteuert wird. Jeden Morgen setzt die Chinesische Volksbank einen offiziellen Leitkurs fest, und der Onshore-Kurs (CNY) darf sich nur in einer Bandbreite darum bewegen — deshalb bewegt sich USD/CNY von Tag zu Tag weit weniger, als seine wirtschaftliche Bedeutung vermuten ließe.",
            "Chinas Handelsüberschuss, die Kapitalkontrollen und die politischen Ziele prägen alle den Kurs. Bei Umrechnungen gilt: Der Onshore-CNY und der Offshore-CNH können leicht abweichen, und private Währungsumrechnung in China unterliegt den Kapitalverkehrsregeln. Vergleichen Sie Angebote stets mit dem Referenzkurs unten.",
        ],
        "faq": [
            ("Ist der chinesische Yuan frei konvertierbar?",
             "Nicht vollständig. Handelsbezogene Umrechnung ist unkompliziert, doch Investitionsströme über die Grenze unterliegen Quoten und Genehmigungen. Deshalb notiert die Offshore-Variante (CNH) etwas anders als der Onshore-CNY — die Lücke zeigt, wie teuer es ist, Geld über die Grenze zu bewegen."),
            ("Warum bewegt sich USD/CNY kaum im Vergleich zu anderen Paaren?",
             "Weil die Zentralbank ihn steuert. Der tägliche Leitkurs und die Handelsbandbreite halten den Kurs relativ zum Dollar stabil, entsprechend Chinas Präferenz für Berechenbarkeit im Handel. Gesteuert heißt nicht fix: Über Monate und Jahre zieht der Kurs trotzdem mit den Fundamentaldaten."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD in INR — Wechselkurs, Umrechner & was die Rupie bewegt",
        "description": "US-Dollar in indische Rupien umrechnen mit Live-Kursen: der heutige USD/INR-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was die Rupie bewegt.",
        "h1": "USD in INR — US-Dollar in indische Rupien umrechnen",
        "intro": [
            "USD/INR ist einer der wichtigsten Überweisungskorridore der Welt — Indien erhält mehr Rücküberweisungen als jedes andere Land — und ein stark gehandeltes Schwellenwährungspaar. Die Reserve Bank of India steuert die Volatilität, nicht das Niveau: Sie glättet scharfe Bewegungen mit ihren Reserven, lässt die Rupie aber ihren langfristigen Trend finden.",
            "Die säkulare Geschichte der Rupie ist eine allmähliche Abwertung gegenüber dem Dollar, getrieben von Inflationsunterschieden und Indiens Leistungsbilanz, unterbrochen von globalen Risikoereignissen. Wer Geld nach Indien sendet, findet die wahren Kosten in der Lücke zwischen Mittelkurs und gebotenem Kurs.",
        ],
        "faq": [
            ("Warum verliert die indische Rupie über Zeit an Wert?",
             "Vor allem wegen der Inflationsunterschiede und des Handelsdefizits: Indien importiert weit mehr, als es exportiert, und die Differenz wird über Kapitalzuflüsse finanziert. Die RBI glättet den Weg, doch über Jahrzehnte ist die Rupie gegenüber dem Dollar stetig schwächer geworden — für eine aufstrebende Wirtschaft ist das normal."),
            ("Wie bekommt man den besten Kurs beim Geldsenden nach Indien?",
             "Vergleichen Sie vor dem Senden den gebotenen Kurs mit dem Mittelkurs, nicht nur die Gebühren. Spezialisierte Überweisungsdienste schlagen auf diesem Korridor meist die Banküberweisung, und schon 1 % Unterschied macht sich bei regelmäßigen Familienüberweisungen über ein Jahr deutlich bemerkbar."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD in CAD — Wechselkurs, Umrechner & was den Loonie bewegt",
        "description": "US-Dollar in kanadische Dollar umrechnen mit Live-Kursen: der heutige USD/CAD-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Loonie bewegt.",
        "h1": "USD in CAD — US-Dollar in kanadische Dollar umrechnen",
        "intro": [
            "USD/CAD — im FX-Jargon „Loonie“ — ist eines der fünf meistgehandelten Paare der Welt und beruht auf einer der größten Handelsbeziehungen der Erde. Kanada schickt rund drei Viertel seiner Exporte in die USA, daher handelt das Paar stark auf US-Wachstum, Energiepreise (Kanada ist ein bedeutender Ölexporteur) und den Zinsabstand zwischen Fed und Bank of Canada.",
            "Steigt das Öl, wird der CAD meist stärker; treffen globale Wachstumssorgen ein, schwächelt er mit den Rohstoffwährungen insgesamt. Das Paar ist rund um die Uhr liquide, und Angebote innerhalb eines Bruchteils eines Prozents vom Mittelkurs sind leicht zu finden — breite Margen sind also immer ein Warnsignal.",
        ],
        "faq": [
            ("Warum heißt der kanadische Dollar Loonie?",
             "Nach dem Eistaucher — dem Vogel auf der 1987 eingeführten Ein-Dollar-Münze. Der Spitzname blieb und bezeichnet heute in FX-Kreisen die Währung selbst, etwa in „der Loonie hat heute zugelegt“."),
            ("Wirkt sich der Ölpreis wirklich auf USD/CAD aus?",
             "Ja, sichtbar. Rohöl und verwandte Produkte sind Kanadas größte Exportkategorie, steigende Ölpreise bringen also tendenziell mehr Dollar nach Kanada und stützen den CAD. Händler behandeln das Paar als grobes Spiel auf die Energiemärkte — neben den Zinsen der beiden Länder."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD in AUD — Wechselkurs, Umrechner & was den Aussie bewegt",
        "description": "US-Dollar in australische Dollar umrechnen mit Live-Kursen: der heutige USD/AUD-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Aussie bewegt.",
        "h1": "USD in AUD — US-Dollar in australische Dollar umrechnen",
        "intro": [
            "Der australische Dollar ist die klassische Rohstoffwährung: Sein Glück hängt an Eisenerz-, Kohle- und Gasexporten und vor allem an der chinesischen Nachfrage danach. USD/AUD ist damit einer der saubersten Echtzeit-Indikatoren für die globale Risikofreude — der Aussie stärkt sich, wenn der Welthandel boomt, und schwächelt in Risikophasen.",
            "Die Zinspolitik der Reserve Bank of Australia und der Fed treibt die kürzeren Schwankungen. Australiens Working-Holiday- und Studierendenpopulationen machen USD→AUD (und zurück) zu einer häufigen, wiederkehrenden Umrechnung, bei der sich schon eine Kursmarge von 1 % schnell summiert.",
        ],
        "faq": [
            ("Warum reagiert der australische Dollar so empfindlich auf China?",
             "China ist mit großem Abstand Australiens wichtigster Exportmarkt, vor allem für Eisenerz für die Stahlproduktion. Wenn die chinesische Bauwirtschaft abkühlt, fallen Rohstoffpreise und AUD meist zusammen — die Währung wirkt als Echtzeit-Barometer der chinesischen Schwerindustrie."),
            ("Ist der AUD ein sicherer Hafen?",
             "Ganz im Gegenteil: Trader nennen ihn eine Risikowährung. In globalen Paniken — 2008, 2020 — fließt Geld in US-Dollar, und der Aussie fällt unter den großen Währungen meist am härtesten. Genau diese Zyklik ist der Grund, warum Carry-Trader und Wachstumsbeobachter ihn so genau im Blick haben."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD in CHF — Wechselkurs, Umrechner & was den Franken bewegt",
        "description": "US-Dollar in Schweizer Franken umrechnen mit Live-Kursen: der heutige USD/CHF-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Franken bewegt.",
        "h1": "USD in CHF — US-Dollar in Schweizer Franken umrechnen",
        "intro": [
            "Der Schweizer Franken ist der wichtigste sichere Hafen der Welt: Bei Krieg, Bankenstress oder Marktpanik fließt Geld in die Schweiz, und der CHF stärkt sich. USD/CHF fällt daher in globalen Krisen oft, selbst wenn der Dollar selbst Zuflucht ist — der Franken ist schlicht der stärkere Schutzraum.",
            "Die Schweizerische Nationalbank gestaltet den Kurs aktiv — von der berühmten Euro-Untergrenze 2011–2015 bis zu umfangreichen Interventionen seither. Für Umrechnungen erinnert die Schweiz auch daran, dass ein reiches Land keine engen Einzelhandelsmargen garantiert, besonders an Flughäfen und in Hotels — prüfen Sie immer den Mittelkurs als Referenz.",
        ],
        "faq": [
            ("Warum gilt der Schweizer Franken als sicherer Hafen?",
             "Ein Jahrhundert Neutralität, niedrige Schulden, ein Leistungsbilanzüberschuss und eine glaubwürdige Zentralbank machen den Franken zur Standardstation für Geld auf der Flucht vor Risiko. Die Schweizer Inflation lag zudem Jahrzehnte weit unter der der USA und der Eurozone und erhielt so die Kaufkraft der Währung."),
            ("Was hat die SNB im Januar 2015 getan?",
             "Sie gab ihre Obergrenze für die Frankenstärke gegenüber dem Euro abrupt auf. USD/CHF und EUR/CHF brachen binnen Minuten um etwa 20–30 % ein — eine der größten Intraday-Bewegungen, die es bei einem großen Paar je gab, und der Grund, warum Trader den Begriff „SNB-Risiko“ bis heute respektieren."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD in MXN — Wechselkurs, Umrechner & was den Peso bewegt",
        "description": "US-Dollar in mexikanische Pesos umrechnen mit Live-Kursen: der heutige USD/MXN-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Peso bewegt.",
        "h1": "USD in MXN — US-Dollar in mexikanische Pesos umrechnen",
        "intro": [
            "USD/MXN ist das meistgehandelte Schwellenwährungspaar Amerikas und eines der liquidesten der Welt. Der Peso handelt auf allem, was die US-Wirtschaft bewegt — Handelspolitik, Wachstum, der Zinsabstand zwischen Fed und Banxico —, dazu auf Ölpreise und den gewaltigen Überweisungskorridor aus den Vereinigten Staaten.",
            "Weil er so liquide ist, reagiert das Paar schnell auf die globale Risikostimmung: ein klassisches Carry-Trade-Ziel, das sich in ruhigen Märkten stärkt und in Paniken ruckartig einbricht. Reisende und Überweisungssender finden am Flughafen häufig Margen von 3–6 % — der Mittelkurs unten ist der Maßstab für den Vergleich.",
        ],
        "faq": [
            ("Warum ist USD/MXN so volatil?",
             "Hohe Zinsen in Mexiko locken kurzfristiges Carry-Geld an, das im Stress schnell wieder abzieht; zugleich ist der Peso das Referenzasset für den gesamten Handel und die politischen Nachrichten zwischen den USA und Mexiko. Zusammen macht das ihn liquide, aber sprungfreudig — große Tagesschwankungen sind normal, keine Fehlfunktion."),
            ("Was ist der günstigste Weg, Dollar nach Mexiko zu senden?",
             "Spezialisierte Überweisungsdienste schlagen Banken und Bargeldtransfer-Läden auf diesem Korridor regelmäßig. Vergleichen Sie den ankommenden Betrag mit dem Mittelkurs: Bei einer 300-Dollar-Überweisung kann die Differenz zwischen einem fairen Angebot und einer 5-%-Marge einem vollen Tageslohn vor Ort entsprechen."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD in PHP — Wechselkurs, Umrechner & was den Peso bewegt",
        "description": "US-Dollar in philippinische Pesos umrechnen mit Live-Kursen: der heutige USD/PHP-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Peso bewegt.",
        "h1": "USD in PHP — US-Dollar in philippinische Pesos umrechnen",
        "intro": [
            "Der philippinische Peso stützt sich auf einen der größten Überweisungsströme der Welt: Millionen Filipinos im Ausland schicken Geld nach Hause, und diese Dollarzuflüsse sind eine Säule der Wirtschaft. USD/PHP handelt entsprechend auf der globalen Risikostimmung, den Ölpreisen (die Philippinen sind Nettoimporteur) und der Politik der Bangko Sentral ng Pilipinas.",
            "Der offizielle Kurs wird mit leichter Hand gesteuert — die Zentralbank erlaubt allmähliche Anpassung und glättet Spitzen. Für OFW-Familien und Reisende sind die Spread-Unterschiede auf diesem Korridor breit, daher ist der Blick auf den Mittelkurs vor dem Senden die einfachste Ersparnis überhaupt.",
        ],
        "faq": [
            ("Wie wirken sich Überweisungen auf den philippinischen Peso aus?",
             "Stete Dollarzuflüsse von Arbeitnehmern im Ausland stützen Peso und Zahlungsbilanz — jedes Jahr mehrere Prozent des BIP. Steigt das globale Risiko oder schwächeln die Gastländer, lassen die Überweisungen nach, und der Peso folgt meist."),
            ("Ist es besser, USD in PHP in den USA oder auf den Philippinen umzutauschen?",
             "Es hängt vom Anbieter ab, nicht vom Land. Auf beiden Seiten des Korridors gibt es günstige und teure Optionen; entscheidend ist, wie viele Pesos beim Empfänger tatsächlich ankommen. Vergleichen Sie Angebote mit dem Mittelkurs, statt dem nächstgelegenen Laden zu vertrauen."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR in GBP — Wechselkurs, Umrechner & was dieses Paar bewegt",
        "description": "Euro in britische Pfund umrechnen mit Live-Kursen: der heutige EUR/GBP-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was dieses Paar bewegt.",
        "h1": "EUR in GBP — Euro in britische Pfund umrechnen",
        "intro": [
            "EUR/GBP ist der klassische europäische Kreuzkurs: zwei Volkswirtschaften, die rund die Hälfte ihres Handels miteinander abwickeln, getrennt nur durch eine Währungsgrenze. Da beide entwickelte Niedriginflationswährungen sind, bewegt sich das Paar weit weniger als Dollarkreuze — im Kern ist es eine Wette auf das relative Schicksal von Eurozone und Vereinigtem Königreich.",
            "Der Zinsabstand zwischen EZB und Bank of England treibt den größten Teil des Trends, während britische politische und fiskalische Nachrichten die Ausschläge liefern. Für Grenzgänger, Rentner und Unternehmen macht die Stabilität des Paares kleine Kursunterschiede noch wichtiger: Eine Marge von 1 % ist ein großer Anteil an der gesamten Jahresbewegung.",
        ],
        "faq": [
            ("Warum ist EUR/GBP ruhiger als EUR/USD?",
             "Weder Euro noch Pfund sind globale Risikowährungen, daher ziehen weltweite Flucht-in-Sicherheit-Bewegungen an ihnen vorbei. Das Paar spiegelt vor allem die relative Ökonomie von Großbritannien und der EU sowie Zinsdifferenzen, die sich langsam ändern — auch wenn es bei britischen Politiknachrichten hart ausschlagen kann, wie 2016 zeigte."),
            ("Wie wirkt sich der Brexit weiterhin auf EUR/GBP aus?",
             "Strukturell. Neue Handelshürden seit 2021 machten die britische Wirtschaft etwas weniger offen gegenüber der EU, was die meisten Ökonomen mit einem strukturell schwächeren Pfund verbinden. Jede Runde der britisch-europäischen Verhandlungen über Handelsregeln bewegt das Paar bis heute."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR in CHF — Wechselkurs, Umrechner & die Rolle der SNB",
        "description": "Euro in Schweizer Franken umrechnen mit Live-Kursen: der heutige EUR/CHF-Wechselkurs, ein kostenloser Rechner, Betragstabellen und die Rolle der SNB bei diesem Paar.",
        "h1": "EUR in CHF — Euro in Schweizer Franken umrechnen",
        "intro": [
            "EUR/CHF ist der Lackmustest für den sicheren Hafen Europa: Sobald der Stress in der Eurozone steigt — die Schuldenkrise 2011, Bankenpaniken, Krieg auf dem Kontinent — fließt Geld über die Schweizer Grenze, und das Paar fällt. Die Schweizerische Nationalbank beobachtet diesen Kurs genauer als jeden anderen und hat wiederholt interveniert, damit der Franken die Schweizer Exporte nicht erstickt.",
            "Die moderne Geschichte des Paares ist dramatisch: eine Untergrenze bei 1,20 ab 2011, dann das abrupte Aufgeben dieser Grenze im Januar 2015, das einen Flash-Crash von 20–30 % in Minuten produzierte. Seither handelt der Franken als sauberer, wenn mitunter zu starker Zufluchtsort — und die SNB bleibt ein aktiver Teilnehmer an diesem Markt.",
        ],
        "faq": [
            ("Warum interessiert sich die SNB so sehr für EUR/CHF?",
             "Weil die Schweizer Wirtschaft nach Europa verkauft. Ein zu starker Franken macht Schweizer Exporte unattraktiv und drückt die Inflation unter das Ziel, daher kauft die SNB Fremdwährung (und verhängte einmal Negativzinsen), um die Frankenstärke zu deckeln. Sie interveniert in diesem Paar mehr als fast jede andere Notenbank in einem großen Markt."),
            ("Ist EUR/CHF ein stabiles Paar zum Halten?",
             "In ruhigen Zeiten stabil, in Krisen explosiv — das Gegenteil von diversifiziert. Das Aufgeben der Untergrenze 2015 bleibt die Lehrbuchwarnung, dass die Zusage einer Zentralbank, eine Währung zu deckeln, über Nacht zurückgezogen werden kann. Wer das Paar für risikofrei hielt, lernte es an einem einzigen Morgen anders."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR in PLN — Wechselkurs, Umrechner & was den Złoty bewegt",
        "description": "Euro in polnische Złoty umrechnen mit Live-Kursen: der heutige EUR/PLN-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was den Złoty bewegt.",
        "h1": "EUR in PLN — Euro in polnische Złoty umrechnen",
        "intro": [
            "Polen ist die sechstgrößte Volkswirtschaft der EU mit einer eigenen Währung, und der Złoty ist die am meisten gehandelte der Nicht-Euro-Währungen der Union. EUR/PLN handelt auf dem Zinsabstand zur Nationalbank Polens, auf EU-Mitteln, die nach Osten fließen, auf deutschen Fabrikaufträgen für die polnische Industrie und auf dem geopolitischen Risiko der Region.",
            "Seit Polens EU-Beitritt 2004 hat der Złoty in Boomphasen zugelegt und in Krisen hart verloren — 2008 und 2022 trieben das Paar an historische Extreme. Da Polens künftige Euro-Einführung weiter offen ist, bleibt das Paar für Jahre ein struktureller Bestandteil des europäischen Finanzsystems.",
        ],
        "faq": [
            ("Wird Polen den Euro einführen und den Złoty abschaffen?",
             "Polen ist rechtlich verpflichtet, irgendwann den Euro einzuführen, hat aber keinen Zieltermin, und die Öffentlichkeit ist skeptisch. Solange es keinen glaubwürdigen Zeitplan gibt, bleibt EUR/PLN ein aktiv gehandeltes Paar — schon politische Aussagen zur Zeitschiene können es allein bewegen."),
            ("Warum ist EUR/PLN 2022 ausgeschlagen?",
             "Der Krieg im Nachbarland Ukraine machte Polen über Nacht zu einer Frontökonomie: Flüchtlingszustrome, Verteidigungsausgaben und Energieschocks trafen die Währung hart. Die Nationalbank Polens intervenierte zur Unterstützung des Złoty — die schärfsten Bewegungen des Paares seit zwei Jahrzehnten."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP in JPY — Wechselkurs, Umrechner & dieses volatile Paar",
        "description": "Britische Pfund in japanische Yen umrechnen mit Live-Kursen: der heutige GBP/JPY-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was dieses volatile Paar bewegt.",
        "h1": "GBP in JPY — britische Pfund in japanische Yen umrechnen",
        "intro": [
            "GBP/JPY — alte Trader nannten es „das Biest“ oder „den Drachen“ — ist eines der volatilsten großen Währungspaare. Es stapelt zwei Risikomotoren übereinander: Sterlings Empfindlichkeit für britische Politik- und Fiskalnachrichten und die Rolle des Yen als Finanzierungswährung der Welt, die es bei jeder Kehrtwende der Stimmung heftig ausschlagen lässt.",
            "Das Paar ist ein Liebling des Carry Trades: nahe null verzinste Yen leihen, um höher verzinsliche Pfund zu kaufen. Das funktioniert, bis eine Krise alle zwingt, gleichzeitig abzuwickeln — deshalb klettert GBP/JPY über Jahre dahin und fällt in Wochen gewaltsam. Positionsgröße und Timing zählen hier mehr als bei fast jedem anderen großen Paar.",
        ],
        "faq": [
            ("Warum ist GBP/JPY volatiler als USD/JPY?",
             "Weil es zwei Volatilitäten multipliziert. Sterling legt das britische Politik- und Konjunkturrisiko oben auf die globale Risikostimmung, die ohnehin USD/JPY treibt. Das Paar hat keine gemeinsame Ankerökonomie und handelt daher fast nur auf Zinsabstände und Stimmung — Zutaten für große Bewegungen."),
            ("Was ist der Carry Trade in GBP/JPY?",
             "Yen zu nahe null japanischen Zinsen leihen und in höher verzinsliche Pfund investieren, um die Differenz einzustreichen. Es rentiert sich, solange die Märkte ruhig sind, und bestraft hart, wenn sie es nicht sind: In Risikophasen springt der Yen, wenn Carry-Positionen abgewickelt werden — oft 10 % und mehr gegenüber dem Pfund in Monaten."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD in JPY — Wechselkurs, Umrechner & Risiko-Barometer",
        "description": "Australische Dollar in japanische Yen umrechnen mit Live-Kursen: der heutige AUD/JPY-Wechselkurs, ein kostenloser Rechner, Betragstabellen und was dieses Risiko-Barometer bewegt.",
        "h1": "AUD in JPY — australische Dollar in japanische Yen umrechnen",
        "intro": [
            "AUD/JPY ist der reinsten Form nach das Risiko-Barometer im Devisenmarkt. Der australische Dollar steht für globales Wachstum und Rohstoffnachfrage — vor allem chinesische Industrieanfrage —, während der Yen für Sicherheit steht. Läuft die Weltwirtschaft, klettert das Paar; bei Panik fällt es schneller als fast jeder andere große Kreuzkurs.",
            "Es ist zugleich das klassische Carry-Trade-Paar: Über Jahrzehnte liehen sich Anleger billige Yen, um den höher verzinsten Aussie zu kaufen. Dieser Fluss prägt die langen, zähen Aufwärtstrends des Paares und seine gewaltsamen Abwicklungen — 2008 bleibt das warnende Beispiel, als AUD/JPY in wenigen Monaten rund die Hälfte verlor.",
        ],
        "faq": [
            ("Warum nennen Trader AUD/JPY ein Risiko-Barometer?",
             "Weil jede Währung an einem entgegengesetzten Pol sitzt: Der Aussie steigt mit globalem Wachstum und Rohstoffnachfrage, der Yen mit Angst. Das Paar bewegt sich daher mit den Weltaktienmärkten, wie es kaum ein anderer Kreuzkurs tut — wenn es hart fällt, ist die Risikoabkehr real."),
            ("Was geschah mit AUD/JPY in der Krise 2008?",
             "Es wurde rund halbiert. Als der globale Kredit einfroren, wurde der Carry Trade abgewickelt: Anleger verkauften australische Dollar, um geliehene Yen zurückzuzahlen, und das Paar stürzte von über 100 auf die unteren 50er binnen Monaten. Es bleibt das Standardbeispiel dafür, wie schnell Carry-Strategien umkippen."),
        ],
    },
}
