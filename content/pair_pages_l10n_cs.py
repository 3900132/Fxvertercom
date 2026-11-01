# -*- coding: utf-8 -*-
"""České (cs) obsahy pro stránky měnových párů („USD na EUR“).

PAIR_UI_L10N odpovídá řetězcům z pair_pages.PAIR_UI["en"] (zástupné znaky
{f} {t} {d} zůstávají beze změny). PAIR_CONTENT_L10N odpovídá 15 párům z
PAIR_CONTENT["en"], klíče jsou shodné s anglickou verzí.
build-lang-pages.py obojí sloučí do PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Živý převodník",
    "pairRateHead": "Aktuální směnný kurz",
    "pairAsOf": "Referenční kurz ke dni {d}. Živý převodník výše vždy načítá nejnovější kurz – tabulky níže jsou snímkem z okamžiku sestavení stránky pro orientaci.",
    "pairAmounts": "Běžné částky: {f} na {t}",
    "pairReverse": "Běžné částky: {t} na {f}",
    "pairMore": "Další převody {f}",
    "pairMorePairs": "Další měnové páry",
    "pairIntroHead": "O směnném kurzu {f}/{t}",
    "pairCurLinks": "Stránky měn",
    "pairMetaTmpl": ("Převod {f} na {t} s živými kurzy: dnešní kurz {f}/{t}, bezplatná kalkulačka, "
                     "tabulky běžných částek a co hýbe tímto měnovým párem."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD na EUR — směnný kurz, převodník a tabulky",
        "description": "Převádějte americké dolary na eura s živými kurzy: dnešní kurz USD/EUR, bezplatná kalkulačka, tabulky běžných částek a co hýbe tímto párem.",
        "h1": "USD na EUR — převod amerických dolarů na eura",
        "intro": [
            "USD/EUR je nejvíce obchodovaný měnový pár světa – zhruba čtvrtina veškerého devizového obratu – a proto má nejužší spready a nejhlubší trh ze všech převodů. Kurz je prostě cena jednoho amerického dolaru v eurech, nepřetržitě stanovovaná globálním obchodem, investičními toky a úrokovou mezerou mezi Fedem a Evropskou centrální bankou.",
            "U běžných převodů je praktickou otázkou, jakou marži platíte nad středním kurzem zobrazeným zde. Banky typicky připočítávají 1–4 %; kartové a převodní služby se výrazně liší. Kontrola živého kurzu před nákupem či převodem okamžitě prozradí, zda je nabídka férová.",
        ],
        "faq": [
            ("Jak je určován kurz USD na EUR?",
             "Plove volně – nabídku a poptávku po obou měnách stanovuje cenu nepřetržitě, ovlivňují je především úrokové politiky Fedu a ECB, inflace na obou stranách Atlantiku a globální nálada rizika. Žádný fixní ani řízený cíl neexistuje."),
            ("Kdy je nejlepší čas převést USD na EUR?",
             "Likvidita je nejhlubší a spready nejužší při překryvu evropských a amerických obchodních hodin (zhruba 13:00–17:00 UTC). Nikdo nedokáže spolehlivě předpovědět krátkodobý směr, proto je u velkých částek bezpečnější převádět po částech, než čekat na lepší den."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD na GBP — směnný kurz, převodník a co hýbe librou",
        "description": "Převádějte americké dolary na britské libry s živými kurzy: dnešní kurz USD/GBP, bezplatná kalkulačka, tabulky částek a co hýbe librou.",
        "h1": "USD na GBP — převod amerických dolarů na britské libry",
        "intro": [
            "Kurz dolaru a libry, přezdívaný „cable” podle transatlantického telegrafního kabelu, který jej v 60. letech 19. století přenášel jako první, patří k nejstarším nepřetržitě uváděným kurzům světa. Dnes odráží úrokovou mezeru mezi Fedem a Bank of England, britskou inflaci i stav britského obchodu a veřejných financí.",
            "Sterling se nejaktivněji obchoduje během londýnských hodin a pár má sklon k prudkým pohybům kolem britských ekonomických dat a rozpočtových oznámení. Srovnání jakékoli nabídky se středním kurzem níže je nejrychlejší způsob, jak zjistit, jak velkou marži si poskytovatel bere.",
        ],
        "faq": [
            ("Proč je britská libra hodnotnější než americký dolar?",
             "Vyšší jednotková cena neznamená silnější ekonomiku – odráží historii a nominace. Libra byla dominantní měnou světa, když dolar ještě neexistoval; samotné číslo nic nevypovídá o relativní ekonomické síle ani kupní síle."),
            ("Co hýbe USD/GBP nejvíc?",
             "Rozhodnutí o sazbách Fedu a Bank of England, britské inflační čísla i politické a rozpočtové zprávy z Westminstru. Při hlasování o brexitu v roce 2016 libra za jediný den klesla zhruba o 10 % – připomínka, že sterling nese politické riziko, jaké většina hlavních měn nezná."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD na JPY — směnný kurz, převodník a co hýbe jenem",
        "description": "Převádějte americké dolary na japonské jeny s živými kurzy: dnešní kurz USD/JPY, bezplatná kalkulačka, tabulky částek a co hýbe jenem.",
        "h1": "USD na JPY — převod amerických dolarů na japonské jeny",
        "intro": [
            "USD/JPY je druhý nejvíce obchodovaný měnový pár světa a klasický barometr úrokové mezery mezi USA a Japonskem. Protože japonské sazby desetiletí seděly blízko nuly, stal se jen světovou oblíbenou financovací měnou – oslabuje, když jsou trhy sebevědomé, a prudce sílí, když krize tyto pozice rozvíjejí.",
            "Pár se sleduje i kvůli oficiálním japonským intervencím: ministerstvo financí opakovaně kupovalo jeny, když padaly příliš daleko a příliš rychle. Velké převody ověřujte proti střednímu kurzu, protože maloobchodní marže u JPY mohou být klamavě široké.",
        ],
        "faq": [
            ("Proč jen někdy vůči dolaru tolik klesá?",
             "Především kvůli úrokové mezeře. Jsou-li americké sazby vysoké a japonské blízko nuly, prodávají investoři jeny a kupují výnosnější dolarová aktiva – carry trade. Jen může klouzat měsíce a poté prudce skočit, když se tyto obchody rozvíjejí."),
            ("Může japonská vláda změnit kurz USD/JPY?",
             "Může trhu vzdorovat, nikoli jej obrátit. Japonsko zasahovalo nákupem či prodejem jenů, když se pohyby staly chaotickými, někdy s desítkami miliard dolarů v jedné epizodě. Intervence vyhlazují cestu; dlouhodobý směr daný fundamenty mění jen zřídka."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD na CNY — směnný kurz, převodník a řízený kurz",
        "description": "Převádějte americké dolary na čínské juany s živými kurzy: dnešní kurz USD/CNY, bezplatná kalkulačka, tabulky částek a jak řízený kurz funguje.",
        "h1": "USD na CNY — převod amerických dolarů na čínské juany",
        "intro": [
            "Kurz dolaru a juanu je největší měnový pár řízený centrální bankou. Lidová banka Číny každé ráno stanovuje denní fixing a onshore kurz (CNY) se smí pohybovat jen v pásmu kolem něj – proto se USD/CNY den od dne hýbe podstatně méně, než by naznačovala jeho ekonomická váha.",
            "Čínský obchodní přebytek, kapitálové kontroly i politické cíle všechny formují kurz. Při převodech počítejte s tím, že onshore CNY a offshore CNH se mohou mírně lišit a že individuální převod měny v Číně podléhá pravidlům kapitálových kontrol. Nabídky vždy porovnávejte s referenčním kurzem níže.",
        ],
        "faq": [
            ("Je čínský juan volně konvertibilní?",
             "Ne zcela. Převody vázané na obchod jsou snadné, toky investic přes hranice ale řídí kvóty a schválení. Proto offshore verze (CNH) obchoduje za mírně odlišnou cenu než onshore CNY – rozdíl ukazuje, kolik stojí přesun peněz přes hranici."),
            ("Proč se USD/CNY hýbe méně než jiné páry?",
             "Protože jej centrální banka řídí. Denní fixing a obchodní pásmo drží kurz vůči dolaru stabilní, v souladu s čínskou preferencí předvídatelnosti v obchodu. Řízený neznamená fixní: během měsíců a let kurz stále sleduje fundamenty."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD na INR — směnný kurz, převodník a co hýbe rupií",
        "description": "Převádějte americké dolary na indické rupie s živými kurzy: dnešní kurz USD/INR, bezplatná kalkulačka, tabulky částek a co hýbe rupií.",
        "h1": "USD na INR — převod amerických dolarů na indické rupie",
        "intro": [
            "USD/INR je jedním z nejdůležitějších převodních koridorů světa – Indie přijímá více převodů než kterákoliv jiná země – a výrazně obchodovaný pár rozvíjejícího se trhu. Rezervní banka Indie řídí volatilitu, nikoli úroveň: prudké pohyby vyhlazuje rezervami, ale nechá rupii najít dlouhodobý trend.",
            "Sekulárním příběhem rupie je pozvolná depreciace vůči dolaru, poháněná inflačními rozdíly a běžným účtem Indie, s přestávkami při globálních rizikových událostech. Pro každého, kdo posílá peníze do Indie, je skutečné náklady skryté v mezeře mezi středním kurzem a nabízeným kurzem.",
        ],
        "faq": [
            ("Proč indická rupie časem oslabuje?",
             "Především kvůli inflačním rozdílům a obchodnímu deficitu: Indie dováží podstatně víc, než vyváží, a rozdíl financují kapitálové přítoky. RBI cestu vyhlazuje, ale během desetiletí rupie vůči dolaru pozvolna oslabovala – což je pro rozvíjející se ekonomiku normální."),
            ("Jak dostat nejlepší kurz při posílání peněz do Indie?",
             "Před odesláním porovnejte nabízený kurz se středním kurzem, ne jen poplatky. Specializované převodní služby na tomto koridoru obvykle porazí bankovní převody a rozdíl už 1 % je u pravidelných rodinných převodů během roku významný."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD na CAD — směnný kurz, převodník a co hýbe loonie",
        "description": "Převádějte americké dolary na kanadské dolary s živými kurzy: dnešní kurz USD/CAD, bezplatná kalkulačka, tabulky částek a co hýbe loonie.",
        "h1": "USD na CAD — převod amerických dolarů na kanadské dolary",
        "intro": [
            "USD/CAD – „loonie” – patří k pěti nejvíce obchodovaným párům světa a stojí na jednom z největších obchodních vztahů planety. Kanada odesílá zhruba tři čtvrtiny vývozu do USA, takže pár silně obchoduje podle amerického růstu, cen energií (Kanada je významný vývozce ropy) a mezery sazeb mezi Fedem a Bank of Canada.",
            "Když ropa roste, CAD typicky sílí; když se rozpoutají obavy z globálního růstu, oslabuje spolu se surovinovými měnami. Pár je likvidní nepřetržitě a nabídky v zlomku procenta od středního kurzu jsou snadno dostupné – široké marže proto vždy stojí za zpochybnění.",
        ],
        "faq": [
            ("Proč se kanadský dolar nazývá loonie?",
             "Podle loona – ptáka na jednodolarové minci zavedené v roce 1987. Přezdívka se vžila a dnes ve slangu devizového trhu označuje samotnou měnu, například „loonie dnes posílil”."),
            ("Ovlivňuje cena ropy skutečně USD/CAD?",
             "Ano, nápadně. Surová ropa a související produkty jsou největší kanadskou vývozní kategorií, takže rostoucí ropa přivádí do Kanady víc dolarů a CAD zvedá. Traderi na pár nahlížejí jako na hrubou sázku na energetické trhy i sazby obou zemí."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD na AUD — směnný kurz, převodník a co hýbe aussie",
        "description": "Převádějte americké dolary na australské dolary s živými kurzy: dnešní kurz USD/AUD, bezplatná kalkulačka, tabulky částek a co hýbe aussie.",
        "h1": "USD na AUD — převod amerických dolarů na australské dolary",
        "intro": [
            "Australský dolar je klasická surovinová měna: jeho osudy sledují vývoz železné rudy, uhlí a plynu a především čínská poptávka po nich. USD/AUD je tak jedním z nejčistších indikátorů globální chuti k riziku v reálném čase – Aussie sílí, když světový obchod kvete, a slábne v rizikových fázích.",
            "Kratší výkyvy řídí měnová politika Reserve Bank of Australia a Fedu. Australská komunita pracovních a studijních pobytů dělá z USD→AUD (a zpět) častý opakovaný převod, kde se už 1% kurzová marže rychle nasčítá.",
        ],
        "faq": [
            ("Proč je australský dolar tak citlivý na Čínu?",
             "Čína je s velkým odstupem největším australským exportním trhem, především pro železnou rudu do oceláren. Když čínské stavebnictví zpomalí, surovinové ceny i AUD obvykle padají spolu – měna působí jako barometr čínského těžkého průmyslu v reálném čase."),
            ("Je AUD bezpečným přístavem?",
             "Právě naopak: traderi mu říkají risk-on měna. V globálních panikách (2008, 2020) peníze proudí do amerických dolarů a Aussie z hlavních měn padá obvykle nejvíc. Právě tato cyklicita je důvodem, proč ho carry traderi i pozorovatelé růstu sledují tak pozorně."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD na CHF — směnný kurz, převodník a co hýbe frankem",
        "description": "Převádějte americké dolary na švýcarské franky s živými kurzy: dnešní kurz USD/CHF, bezplatná kalkulačka, tabulky částek a co hýbe frankem.",
        "h1": "USD na CHF — převod amerických dolarů na švýcarské franky",
        "intro": [
            "Švýcarský frank je prvním bezpečným přístavem světa: když udeří válka, bankovní stres či panika na trzích, peníze proudí do Švýcarska a CHF sílí. USD/CHF proto v globálních krizích typicky klesá, i když sám dolar je útočištěm – frank je prostě silnějším přístavem.",
            "Švýcarská národní banka kurz aktivně formuje, od slavné euroní podlahy 1,20 v letech 2011–2015 po rozsáhlé intervence od té doby. Při převodech je Švýcarsko zároveň připomínkou, že i pár bohaté země může nést široké maloobchodní marže, zejména na letištích a v hotelech – vždy kontrolujte střední kurz.",
        ],
        "faq": [
            ("Proč je švýcarský frank považován za bezpečný přístav?",
             "Staletí neutrality, nízký dluh, přebytek běžného účtu a důvěryhodná centrální banka dělají z franku výchozí parkoviště pro peníze prchající před rizikem. Švýcarská inflace navíc desetiletí běžela výrazně pod americkou a eurozónskou, čímž zachovala kupní sílu měny."),
            ("Co provedla SNB v lednu 2015?",
             "Náhle opustila strop síly franku vůči euru. USD/CHF i EUR/CHF se během minut propadly asi o 20–30 % – jeden z největších intradenních pohybů hlavního páru vůbec – a proto traderi dodnes respektují pojem „riziko SNB”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD na MXN — směnný kurz, převodník a co hýbe pesem",
        "description": "Převádějte americké dolary na mexická pesa s živými kurzy: dnešní kurz USD/MXN, bezplatná kalkulačka, tabulky částek a co hýbe pesem.",
        "h1": "USD na MXN — převod amerických dolarů na mexická pesa",
        "intro": [
            "USD/MXN je nejvíce obchodovaný pár rozvíjejícího se trhu v Americe a jeden z nejlikvidnějších na světě. Peso obchoduje podle všeho, co hýbe americkou ekonomikou – obchodních politik, růstu, úrokové mezery mezi Fedem a Banxico – a navíc podle cen ropy a obrovského převodního koridoru z USA.",
            "Protože je tak likvidní, reaguje pár rychle na globální náladu rizika: je klasickým cílem carry trade, který sílí v klidných trzích a prudce propadá v panikách. Cestovatelé i odesílatelé převodů na letištích běžně narazí na marže 3–6 % – střední kurz níže je měřítkem pro srovnání.",
        ],
        "faq": [
            ("Proč je USD/MXN tak volatilní?",
             "Vysoké sazby v Mexiku přitahují krátkodobé carry peníze, které v obtížných časech rychle odtékají; peso je zároveň referenčním aktivem veškerého obchodu a politických zpráv mezi USA a Mexikem. Kombinace z něj dělá likvidní, ale skákavou měnu – velké denní pohyby jsou normální, ne porucha."),
            ("Jak nejlevněji poslat dolary do Mexika?",
             "Specializované převodní služby na tomto koridoru pravidelně poráží banky i pobočky hotovostních převodů. Porovnejte doručenou částku se středním kurzem: u převodu 300 dolarů může rozdíl mezi férovou nabídkou a 5% marží odpovídat celodenní místní mzdě."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD na PHP — směnný kurz, převodník a co hýbe pesem",
        "description": "Převádějte americké dolary na filipínská pesa s živými kurzy: dnešní kurz USD/PHP, bezplatná kalkulačka, tabulky částek a co hýbe pesem.",
        "h1": "USD na PHP — převod amerických dolarů na filipínská pesa",
        "intro": [
            "Filipínské peso ukotvuje jeden z největších převodních toků světa: miliony filipínských pracovníků v zahraničí posílají peníze domů a tyto dolarové přítoky jsou pilířem ekonomiky. USD/PHP proto obchoduje podle globální chuti k riziku, cen ropy (Filipíny jsou netto dovozce) a politiky Bangko Sentral ng Pilipinas.",
            "Oficiální kurz je řízen s lehkou rukou – centrální banka dovoluje pozvolné přizpůsobení a vyhlazuje špičky. Pro rodiny OFW i cestovatele jsou na tomto koridoru rozdíly mezi poskytovateli široké, takže kontrola středního kurzu před odesláním je nejjednodušší úsporou vůbec.",
        ],
        "faq": [
            ("Jak převody ovlivňují filipínské peso?",
             "Stálé dolarové přítoky od pracovníků v zahraničí podpírají peso i platební bilanci země – každý rok několik procent HDP. Když roste globální riziko či oslabují hostitelské ekonomiky, převody ochabují a peso většinou následuje."),
            ("Je lepší převést USD na PHP v USA nebo na Filipínách?",
             "Záleží na poskytovateli, ne na zemi. Na obou stranách koridoru najdete levné i drahé možnosti; rozhodující je, kolik pes reálně přijme příjemce. Porovnávejte nabídky se středním kurzem, místo abyste věřili nejbližší pobočce."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR na GBP — směnný kurz, převodník a co hýbe párem",
        "description": "Převádějte eura na britské libry s živými kurzy: dnešní kurz EUR/GBP, bezplatná kalkulačka, tabulky částek a co hýbe tímto párem.",
        "h1": "EUR na GBP — převod eur na britské libry",
        "intro": [
            "EUR/GBP je klasický evropský kříž: dvě ekonomiky, které směrují zhruba polovinu svého obchodu jedna k druhé, oddělené jedinou měnovou hranicí. Protože obě jsou rozvinuté měny s nízkou inflací, hýbe se pár mnohem méně než dolarové kříže – ve skutečnosti jde o sázku na vzájemné osudy eurozóny a Británie.",
            "Úroková mezera mezi ECB a Bank of England řídí většinu trendu, zatímco britské politické a rozpočtové zprávy dodávají výkyvy. Pro pracovníky přes Lamanšský průliv, důchodce i firmy znamená stabilita páru, že i malé kurzové rozdíly váží víc: 1% marže je velkou částí celoročního pohybu.",
        ],
        "faq": [
            ("Proč je EUR/GBP klidnější než EUR/USD?",
             "Ani euro, ani libra nejsou globální rizikové měny, takže celosvětové úniky do bezpečí je míjejí. Pár odráží hlavně vzájemnou ekonomiku Británie a EU a úrokové rozdíly, které se mění pomalu – i když na britské politické zprávy může prudce vyrazit, jak ukázal rok 2016."),
            ("Jak brexit stále ovlivňuje EUR/GBP?",
             "Strukturálně. Nové obchodní tření od roku 2021 učinilo britskou ekonomiku mírně méně otevřenou vůči EU, což většina ekonomů spojuje se strukturálně slabší librou. Každé kolo britsko-evropských jednání o obchodních pravidlech pár hýbe dodnes."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR na CHF — směnný kurz, převodník a role SNB",
        "description": "Převádějte eura na švýcarské franky s živými kurzy: dnešní kurz EUR/CHF, bezplatná kalkulačka, tabulky částek a role SNB u tohoto páru.",
        "h1": "EUR na CHF — převod eur na švýcarské franky",
        "intro": [
            "EUR/CHF je lakmusovým papírkem bezpečného přístavu Evropy: kdykoli vzroste stres v eurozóně – dluhová krize 2011, bankovní panika, válka na kontinentu – peníze přetékají přes švýcarskou hranici a pár klesá. Švýcarská národní banka jej sleduje pozorněji než jakýkoli jiný kurz a opakovaně zasahovala, aby frank neutopil švýcarské vývozce.",
            "Moderní historie páru je dramatická: podlaha na 1,20 od roku 2011 a poté odvázání v lednu 2015, které během minut způsobilo zhroucení o 20–30 %. Od té doby frank obchoduje jako čisté – byť občas příliš silné – útočiště a SNB zůstává aktivním účastníkem tohoto trhu.",
        ],
        "faq": [
            ("Proč SNB tolik záleží na EUR/CHF?",
             "Protože švýcarská ekonomika prodává do Evropy. Příliš silný frank činí švýcarský vývoz nekonkurenceschopným a táhne inflaci pod cíl, proto SNB kupuje cizí měnu (a jednou zavedla záporné sazby), aby sílu franku zbrzdila. V tomto páru zasahuje víc než téměř jakákoli jiná centrální banka ve velkém trhu."),
            ("Je EUR/CHF stabilní pár k držení?",
             "V klidných časech stabilní, v krizích výbušný – opak diverzifikace. Odvázání z roku 2015 zůstává učebnicovým varováním, že slib centrální banky stropovat měnu lze přes noc odvolat. Kdo pár považoval za bezrizikový, naučil se to jinak jediným ránem."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR na PLN — směnný kurz, převodník a co hýbe złotym",
        "description": "Převádějte eura na polské złoté s živými kurzy: dnešní kurz EUR/PLN, bezplatná kalkulačka, tabulky částek a co hýbe złotym.",
        "h1": "EUR na PLN — převod eur na polské złoté",
        "intro": [
            "Polsko je šestou největší ekonomikou EU, která stále užívá vlastní měnu, a złoty je nejvíce obchodovanou měnou mezi ne-eurovými měnami unie. EUR/PLN obchoduje podle úrokové mezery vůči Národní bance Polska, fondů EU proudících na východ, německých zakázek pro polský průmysl i regionálního geopolitického rizika.",
            "Od vstupu Polska do EU v roce 2004 złoty v konjunkturách sílil i v krizích tvrdě padal – roky 2008 a 2022 přivedly pár k historickým extrémům. S případným zavedením eura stále nerozhodnuto zůstává pár strukturální součástí evropských financí i v následujících letech.",
        ],
        "faq": [
            ("Přijme Polsko euro a zruší złoty?",
             "Polsko je právně povinno euro nakonec přijmout, nemá ale žádné cílové datum a veřejnost je skeptická. Dokud nebude existovat důvěryhodný harmonogram, zůstává EUR/PLN aktivně obchodovaným párem – už jen politická prohlášení o harmonogramu jej dokáží sama pohýt."),
            ("Proč EUR/PLN v roce 2022 vyrazilo?",
             "Válka v sousední Ukrajině proměnila Polsko přes noc v hraniční ekonomiku: příliv uprchlíků, obranné výdaje i energetické šoky měnu tvrdě zasáhly. Národní banka Polska zasáhla na podporu złotého – nejsilnější pohyby páru za dvě dekády."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP na JPY — směnný kurz, převodník a tento volatilní pár",
        "description": "Převádějte britské libry na japonské jeny s živými kurzy: dnešní kurz GBP/JPY, bezplatná kalkulačka, tabulky částek a co hýbe tímto volatilním párem.",
        "h1": "GBP na JPY — převod britských liber na japonské jeny",
        "intro": [
            "GBP/JPY – starší traderi mu říkali „bestie” či „drak” – patří k nejvolatilnějším hlavním párům. Kladie na sebe dva rizikové motory: citlivost libry na britské politické a rozpočtové zprávy a roli jenu jako světové financovací měny, díky níž prudce skáče při každém obratu nálady.",
            "Pár je oblíbený u carry trade: půjčení jenu téměř na nulové sazby k nákupu výnosnějších liber. To funguje, dokud krize nedonutí všechny rozvinout pozice najednou – proto GBP/JPY roky tvrdošíjně stoupá a v týdnech prudce padá. Velikost pozice a načasování tu váží víc než u téměř jakéhokoli jiného hlavního páru.",
        ],
        "faq": [
            ("Proč je GBP/JPY volatilnější než USD/JPY?",
             "Protože násobí dvě volatility. Libra přidává britské politické a ekonomické riziko k globální náladě, která už řídí USD/JPY. Pár nemá společnou kotvící ekonomiku, takže obchoduje téměř čistě podle úrokových mezer a nálady – příslib velkých pohybů."),
            ("Co je carry trade v GBP/JPY?",
             "Půjčení jenů na téměř nulových japonských sazbách a investice do výnosnějších liber s kapsou rozdílu. Výnosné, dokud jsou trhy klidné, a krutě trestající, když nejsou: v rizikových fázích jen vystřelí, když se carry pozice rozvíjejí, často o 10 % a víc vůči libře během měsíců."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD na JPY — směnný kurz, převodník a barometr rizika",
        "description": "Převádějte australské dolary na japonské jeny s živými kurzy: dnešní kurz AUD/JPY, bezplatná kalkulačka, tabulky částek a co hýbe tímto barometrem rizika.",
        "h1": "AUD na JPY — převod australských dolarů na japonské jeny",
        "intro": [
            "AUD/JPY je nejčistším barometrem rizika na devizovém trhu. Australský dolar představuje globální růst a surovinovou poptávku – především čínský průmysl – zatímco jen představuje bezpečí. Když světová ekonomika roste, pár stoupá; při panice padá rychleji než téměř jakýkoli jiný hlavní kříž.",
            "Zároveň jde o klasický carry trade pár: desetiletí si investoři půjčovali levné jeny k nákupu výnosnějšího Aussie. Tento tok formuje dlouhé vytrvalé vzestupné trendy páru i jeho násilná rozvinutí – rok 2008 zůstává výstrahou, kdy AUD/JPY za několik měsíců ztratilo zhruba polovinu hodnoty.",
        ],
        "faq": [
            ("Proč traderi nazývají AUD/JPY barometrem rizika?",
             "Protože každá měna stojí na opačném pólu: Aussie roste s globálním růstem a poptávkou po surovinách, jen se strachem. Pár se proto pohybuje se světovými akciemi v míře, které se málokterý kříž rovná – když tvrdě padá, riziková averze je skutečná."),
            ("Co se stalo s AUD/JPY v krizi 2008?",
             "Zhruba se zpolovilo. Když ztuhl globální úvěr, carry trade se rozvinul: investoři prodávali australské dolary k zaplacení vypůjčených jenů a pár se během měsíců zřítil z hodnot nad 100 na nízko padesátky. Zůstává standardním příkladem rychlosti obratu carry strategií."),
        ],
    },
}
