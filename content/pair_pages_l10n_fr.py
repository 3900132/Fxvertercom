# -*- coding: utf-8 -*-
"""Contenus français pour les pages de paires de devises (« USD vers EUR »).

PAIR_UI_L10N reprend les chaînes de pair_pages.PAIR_UI["en"] (les
emplacements {f} {t} {d} restent inchangés). PAIR_CONTENT_L10N reprend les
15 paires de PAIR_CONTENT["en"], avec des clés identiques à la version
anglaise. build-lang-pages.py fusionne le tout dans PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Convertisseur en direct",
    "pairRateHead": "Taux de change actuel",
    "pairAsOf": "Taux de référence au {d}. Le convertisseur en direct ci-dessus récupère toujours le taux le plus récent — les tableaux ci-dessous sont un instantané pris à la génération de la page, à titre indicatif.",
    "pairAmounts": "Montants courants : {f} vers {t}",
    "pairReverse": "Montants courants : {t} vers {f}",
    "pairMore": "Autres conversions en {f}",
    "pairMorePairs": "Autres paires de devises",
    "pairIntroHead": "À propos du taux de change {f}/{t}",
    "pairCurLinks": "Pages des devises",
    "pairMetaTmpl": ("Convertir {f} en {t} avec des taux en direct : le taux {f}/{t} du jour, une calculatrice gratuite, "
                     "des tableaux de montants courants et ce qui fait bouger cette paire de devises."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD vers EUR — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en euros avec des taux en direct : le taux USD/EUR du jour, une calculatrice gratuite, des tableaux de montants courants et ce qui fait bouger la paire.",
        "h1": "USD vers EUR — convertir des dollars US en euros",
        "intro": [
            "USD/EUR est la paire de devises la plus échangée au monde — environ un quart de l'ensemble des transactions de change — d'où les écarts les plus serrés et le marché le plus profond de toutes les conversions. Le taux n'est rien d'autre que le prix d'un dollar US en euros, fixé en continu par le commerce mondial, les flux d'investissement et l'écart de taux d'intérêt entre la Réserve fédérale américaine et la Banque centrale européenne.",
            "Pour les conversions du quotidien, la question pratique est la marge que vous payez par rapport au taux du marché interbancaire affiché ici. Les banques ajoutent typiquement 1 à 4 % ; les services de carte et de transfert varient beaucoup. Vérifier le taux en direct avant un achat ou un transfert vous dit instantanément si une offre est honnête.",
        ],
        "faq": [
            ("Comment le taux de change USD vers EUR est-il déterminé ?",
             "Il flotte librement — l'offre et la demande des deux monnaies fixent le prix en continu, principalement sous l'influence de la politique de taux de la Fed et de la BCE, de l'inflation des deux côtés de l'Atlantique et de l'appétit pour le risque mondial. Il n'existe aucun objectif fixe ni administré."),
            ("Quel est le meilleur moment pour convertir des USD en EUR ?",
             "La liquidité est la plus profonde et les écarts les plus serrés pendant le chevauchement des séances européennes et américaines (environ 13 h à 17 h UTC). Personne ne peut prévoir de façon fiable la direction à court terme ; pour les gros montants, il est donc plus sûr de convertir en plusieurs tranches que d'attendre un meilleur jour."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD vers GBP — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en livres sterling avec des taux en direct : le taux USD/GBP du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger la livre.",
        "h1": "USD vers GBP — convertir des dollars US en livres sterling",
        "intro": [
            "Le taux dollar–livre, surnommé « cable » d'après le câble télégraphique transatlantique qui l'a transmis pour la première fois dans les années 1860, est l'un des plus anciens taux de change cotés en continu au monde. Il reflète aujourd'hui l'écart de taux entre la Réserve fédérale et la Banque d'Angleterre, l'inflation britannique et la santé du commerce et des finances publiques du Royaume-Uni.",
            "La sterling s'échange le plus activement pendant les heures londoniennes, et la paire est sujette à des mouvements vifs autour des données économiques et des annonces budgétaires britanniques. Comparer chaque offre au taux du marché interbancaire ci-dessous est le moyen le plus rapide de voir la marge prise par un prestataire.",
        ],
        "faq": [
            ("Pourquoi la livre sterling vaut-elle plus que le dollar américain ?",
             "Un prix unitaire plus élevé ne signifie pas une économie plus forte — cela reflète l'histoire et les dénominations. La livre était la monnaie dominante du monde quand le dollar n'existait pas encore ; le chiffre ne dit rien de la force économique relative ni du pouvoir d'achat."),
            ("Qu'est-ce qui fait le plus bouger USD/GBP ?",
             "Les décisions de taux de la Fed et de la Banque d'Angleterre, les chiffres d'inflation britanniques et les nouvelles politiques ou budgétaires de Westminster. Lors du vote sur le Brexit en 2016, la livre a perdu environ 10 % en une journée — preuve que la sterling porte un risque politique que la plupart des grandes monnaies ne connaissent pas."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD vers JPY — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en yens japonais avec des taux en direct : le taux USD/JPY du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger le yen.",
        "h1": "USD vers JPY — convertir des dollars US en yens japonais",
        "intro": [
            "USD/JPY est la deuxième paire de devises la plus échangée au monde et le baromètre classique de l'écart de taux entre les États-Unis et le Japon. Les taux japonais étant restés proches de zéro pendant des décennies, le yen est devenu la grande monnaie de financement mondiale — il faiblit quand les marchés sont confiants et se renforce brutalement quand les crises défont ces positions.",
            "La paire est aussi surveillée pour les interventions officielles japonaises : le ministère des Finances a racheté des yens à plusieurs reprises quand celui-ci faiblissait trop vite et trop fort. Les grosses conversions méritent d'être vérifiées contre le taux du marché interbancaire, car les marges de détail sur le JPY peuvent être trompeusement larges.",
        ],
        "faq": [
            ("Pourquoi le yen chute-t-il parfois autant face au dollar ?",
             "Principalement à cause de l'écart de taux. Quand les taux américains sont élevés et les taux japonais proches de zéro, les investisseurs vendent des yens pour acheter des actifs en dollars mieux rémunérés — le carry trade. Le yen peut glisser pendant des mois, puis bondir violemment quand ces positions se défont."),
            ("Le gouvernement japonais peut-il changer le taux USD/JPY ?",
             "Il peut s'opposer au marché, pas l'inverser. Le Japon est intervenu en achetant ou en vendant des yens quand les mouvements devenaient désordonnés, parfois avec des dizaines de milliards de dollars en une seule opération. L'intervention lisse la trajectoire ; elle change rarement la direction de long terme fixée par les fondamentaux."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD vers CNY — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en yuans chinois avec des taux en direct : le taux USD/CNY du jour, une calculatrice gratuite, des tableaux de montants et le fonctionnement du taux administré.",
        "h1": "USD vers CNY — convertir des dollars US en yuans chinois",
        "intro": [
            "Le taux dollar–yuan est la plus grande paire de devises administrée par une banque centrale. Chaque matin, la Banque populaire de Chine fixe un cours de référence quotidien, et le taux onshore (CNY) ne peut évoluer que dans une bande autour de celui-ci — voilà pourquoi USD/CNY bouge bien moins au jour le jour que son importance économique ne le laisserait croire.",
            "L'excédent commercial chinois, les contrôles de capitaux et les objectifs politiques façonnent tous le taux. Pour vos conversions, notez que le CNY onshore et le CNH offshore peuvent différer légèrement, et que la conversion de devises des particuliers en Chine est soumise aux règles de contrôle des capitaux. Comparez toujours les offres au taux de référence ci-dessous.",
        ],
        "faq": [
            ("Le yuan chinois est-il librement convertible ?",
             "Pas totalement. La conversion liée au commerce est aisée, mais les flux d'investissement transfrontaliers sont encadrés par des quotas et des approbations. Voilà pourquoi la version offshore (CNH) se négocie à un prix légèrement différent du CNY onshore — l'écart reflète le coût de faire traverser l'argent à la frontière."),
            ("Pourquoi USD/CNY bouge-t-il si peu par rapport aux autres paires ?",
             "Parce que la banque centrale l'administre. Le fixing quotidien et la bande de négociation maintiennent le taux stable par rapport au dollar, conformément à la préférence chinoise pour la prévisibilité du commerce. Administré ne veut pas dire fixe : le taux suit quand même les fondamentaux sur des mois et des années."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD vers INR — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en roupies indiennes avec des taux en direct : le taux USD/INR du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger la roupie.",
        "h1": "USD vers INR — convertir des dollars US en roupies indiennes",
        "intro": [
            "USD/INR est l'un des plus grands corridors de transferts d'argent au monde — l'Inde reçoit plus de transferts que tout autre pays — et une paire émergente très échangée. La Reserve Bank of India gère la volatilité plutôt que le niveau : elle lisse les mouvements brusques avec ses réserves, mais laisse la roupie trouver sa tendance de long terme.",
            "L'histoire de fond de la roupie est une dépréciation graduelle face au dollar, portée par les différentiels d'inflation et la balance courante de l'Inde, entrecoupée d'épisodes de risque mondial. Pour qui envoie de l'argent en Inde, l'écart entre le taux du marché interbancaire et le taux proposé est là que se cache le vrai coût.",
        ],
        "faq": [
            ("Pourquoi la roupie indienne se déprécie-t-elle avec le temps ?",
             "Principalement les différentiels d'inflation et le déficit commercial : l'Inde importe bien plus qu'elle n'exporte, la différence étant financée par des entrées de capitaux. La RBI lisse la trajectoire, mais sur des décennies la roupie a dérivé régulièrement vers le bas face au dollar — ce qui est normal pour une économie en développement."),
            ("Comment obtenir le meilleur taux pour envoyer de l'argent en Inde ?",
             "Comparez le taux proposé au taux du marché interbancaire avant d'envoyer, et pas seulement les frais. Les services de transfert spécialisés battent généralement les virements bancaires sur ce corridor, et une différence d'à peine 1 % est significative sur des transferts familiaux réguliers étalés sur une année."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD vers CAD — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en dollars canadiens avec des taux en direct : le taux USD/CAD du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger le huard.",
        "h1": "USD vers CAD — convertir des dollars US en dollars canadiens",
        "intro": [
            "USD/CAD — surnommée « loonie » — est une paire du top cinq mondial, bâtie sur l'une des plus grandes relations commerciales de la planète. Le Canada envoie environ les trois quarts de ses exportations vers les États-Unis, si bien que la paire s'échange fortement sur la croissance américaine, les prix de l'énergie (le Canada est un grand exportateur de pétrole) et l'écart de taux entre la Fed et la Banque du Canada.",
            "Quand le pétrole monte, le CAD se renforce en général ; quand les craintes pour la croissance mondiale frappent, il faiblit avec les monnaies de matières premières. La paire est liquide 24 heures sur 24, et des offres à une fraction de pour cent du taux du marché interbancaire sont faciles à trouver — les marges larges méritent donc toujours d'être questionnées.",
        ],
        "faq": [
            ("Pourquoi le dollar canadien est-il appelé « loonie » ?",
             "D'après le loon — le huard représenté sur la pièce d'un dollar introduite en 1987. Le surnom est resté et désigne aujourd'hui la monnaie elle-même dans l'argot des marchés des changes."),
            ("Le prix du pétrole influence-t-il vraiment USD/CAD ?",
             "Oui, visiblement. Le pétrole brut et ses produits dérivés sont la première catégorie d'exportations du Canada, si bien que la hausse du baril apporte davantage de dollars au pays et soutient le CAD. Les traders traitent la paire comme un pari approximatif sur les marchés de l'énergie autant que sur les taux des deux pays."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD vers AUD — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en dollars australiens avec des taux en direct : le taux USD/AUD du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger l'Aussie.",
        "h1": "USD vers AUD — convertir des dollars US en dollars australiens",
        "intro": [
            "Le dollar australien est la monnaie de matières premières classique : ses destins suivent le minerai de fer, le charbon et le gaz, et surtout la demande chinoise pour ces derniers. USD/AUD est donc l'un des indicateurs en temps réel les plus lisibles de l'appétit mondial pour le risque — l'Aussie se renforce quand le commerce mondial tourne à plein régime et faiblit dans les épisodes de fuite vers la sécurité.",
            "La politique de taux de la Reserve Bank of Australia et de la Fed pilote les oscillations plus courtes. Les populations en visa vacances-travail et en études font de USD vers AUD (et inversement) une conversion récurrente, où même une marge de 1 % sur le taux s'accumule vite.",
        ],
        "faq": [
            ("Pourquoi le dollar australien est-il si sensible à la Chine ?",
             "La Chine est de loin le premier marché d'exportation de l'Australie, notamment pour le minerai de fer destiné à l'acier. Quand la construction chinoise ralentit, les prix des matières premières et l'AUD tombent généralement ensemble — la monnaie agit comme un baromètre en temps réel de l'industrie lourde chinoise."),
            ("L'AUD est-il une valeur refuge ?",
             "Tout l'inverse : les traders le qualifient de monnaie de risque. Dans les paniques mondiales — 2008, 2020 — l'argent afflue vers le dollar américain et l'Aussie tend à être la grande monnaie qui chute le plus fort. Cette cyclicité explique précisément pourquoi les amateurs de carry et les observateurs de croissance le surveillent tant."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD vers CHF — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en francs suisses avec des taux en direct : le taux USD/CHF du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger le franc.",
        "h1": "USD vers CHF — convertir des dollars US en francs suisses",
        "intro": [
            "Le franc suisse est la grande valeur refuge mondiale : quand la guerre, le stress bancaire ou la panique des marchés frappent, l'argent afflue vers la Suisse et le CHF se renforce. USD/CHF tend donc à baisser dans les crises mondiales, même quand le dollar est lui-même un refuge — le franc est simplement l'abri le plus solide.",
            "La Banque nationale suisse façonne activement le taux, du célèbre plancher face à l'euro de 2011–2015 aux interventions massives depuis. Pour les conversions, la Suisse rappelle aussi qu'une paire de pays riches peut encore porter de larges marges de détail, surtout aux aéroports et dans les hôtels — vérifiez toujours la référence du marché interbancaire.",
        ],
        "faq": [
            ("Pourquoi le franc suisse est-il considéré comme une valeur refuge ?",
             "Un siècle de neutralité, une dette faible, un excédent de balance courante et une banque centrale crédible font du franc le parking par défaut de l'argent qui fuit le risque. L'inflation suisse est aussi restée bien en dessous de celle des États-Unis et de la zone euro pendant des décennies, préservant le pouvoir d'achat de la monnaie."),
            ("Qu'a fait la BNS en janvier 2015 ?",
             "Elle a brutalement abandonné son plafond sur la force du franc face à l'euro. USD/CHF et EUR/CHF se sont effondrés d'environ 20 à 30 % en quelques minutes — l'un des plus grands mouvements intrajournaliers jamais vus sur une grande paire, et la raison pour laquelle les traders respectent encore l'expression « risque BNS »."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD vers MXN — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en pesos mexicains avec des taux en direct : le taux USD/MXN du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger le peso.",
        "h1": "USD vers MXN — convertir des dollars US en pesos mexicains",
        "intro": [
            "USD/MXN est la paire émergente la plus échangée des Amériques et l'une des plus liquides du monde. Le peso réagit à tout ce qui bouge l'économie américaine — politique commerciale, croissance, écarts de taux entre la Fed et Banxico — plus les prix du pétrole et l'énorme corridor de transferts en provenance des États-Unis.",
            "Sa grande liquidité fait que la paire réagit vite à l'appétit mondial pour le risque : cible classique du carry trade, elle se renforce dans les marchés calmes et fait des bonds violents dans les paniques. Pour les voyageurs et les expéditeurs, des marges de 3 à 6 % sont courantes dans les aéroports — le taux du marché interbancaire ci-dessous est la référence à laquelle comparer.",
        ],
        "faq": [
            ("Pourquoi USD/MXN est-elle si volatile ?",
             "Des taux d'intérêt élevés au Mexique attirent de l'argent de carry à court terme qui fuit dès que le stress arrive ; le peso est aussi l'actif de référence de tout le commerce et de toute l'actualité politique américano-mexicains. La combinaison le rend liquide mais nerveux — des mouvements quotidiens importants sont normaux, pas une panne."),
            ("Quel est le moyen le moins cher d'envoyer des dollars au Mexique ?",
             "Les services de transfert spécialisés battent régulièrement les banques et les boutiques de transfert en espèces sur ce corridor. Comparez le montant livré au taux du marché interbancaire : sur un transfert de 300 dollars, la différence entre une offre honnête et une marge de 5 % peut représenter une journée entière de salaire local."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD vers PHP — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars US en pesos philippins avec des taux en direct : le taux USD/PHP du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger le peso.",
        "h1": "USD vers PHP — convertir des dollars US en pesos philippins",
        "intro": [
            "Le peso philippin est adossé à l'un des plus grands flux de transferts au monde : des millions de travailleurs philippins expatriés envoient de l'argent au pays, et ces entrées de dollars sont un pilier de l'économie. USD/PHP s'échange donc sur l'appétit mondial pour le risque, les prix du pétrole (les Philippines sont importatrices nettes) et la politique de la Bangko Sentral ng Pilipinas.",
            "Le taux officiel est administré avec légèreté — la banque centrale laisse un ajustement graduel tout en lissant les pics. Pour les familles des travailleurs expatriés et les voyageurs, l'écart entre prestataires sur ce corridor est large : vérifier le taux du marché interbancaire avant d'envoyer est le moyen le plus simple d'économiser.",
        ],
        "faq": [
            ("Comment les transferts d'argent affectent-ils le peso philippin ?",
             "Les entrées régulières de dollars des travailleurs expatriés soutiennent le peso et la balance des paiements du pays — plusieurs pour cent du PIB chaque année. Quand le risque mondial monte ou que les économies d'accueil faiblissent, les transferts s'adoucissent et le peso suit."),
            ("Vaut-il mieux convertir des USD en PHP aux États-Unis ou aux Philippines ?",
             "Cela dépend du prestataire, pas du pays. Les deux bouts du corridor ont des options bon marché et chères ; le chiffre décisif est le nombre de pesos que le destinataire reçoit réellement. Comparez les offres au taux du marché interbancaire plutôt que de faire confiance à la boutique la plus proche."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR vers GBP — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des euros en livres sterling avec des taux en direct : le taux EUR/GBP du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger cette paire.",
        "h1": "EUR vers GBP — convertir des euros en livres sterling",
        "intro": [
            "EUR/GBP est la croisée européenne classique : deux économies qui s'envoient environ la moitié de leur commerce, séparées par une seule frontière monétaire. S'agissant de deux monnaies développées à faible inflation, la paire bouge bien moins que les croisées du dollar — c'est en réalité un pari sur les destins relatifs de la zone euro et du Royaume-Uni.",
            "L'écart de taux entre la BCE et la Banque d'Angleterre pilote l'essentiel de la tendance, tandis que les nouvelles politiques et budgétaires britanniques provoquent les pics. Pour les travailleurs transmanche, les retraités et les entreprises, la stabilité de la paire rend les petits écarts de taux encore plus importants : une marge de 1 % représente une grande part du mouvement annuel total.",
        ],
        "faq": [
            ("Pourquoi EUR/GBP est-elle plus calme qu'EUR/USD ?",
             "Ni l'euro ni la livre n'est une monnaie de risque mondiale, si bien que les grands flux de fuite vers la sécurité les contournent. La paire reflète surtout l'économie relative Royaume-Uni–UE et les différentiels de taux, qui évoluent lentement — mais elle peut s'emballer sur une nouvelle politique britannique, comme 2016 l'a montré."),
            ("Comment le Brexit affecte-t-il encore EUR/GBP ?",
             "Structurellement. Les nouvelles frictions commerciales depuis 2021 ont rendu l'économie britannique un peu moins ouverte à l'UE, ce que la plupart des économistes relient à une sterling structurellement plus faible. Chaque cycle de négociations commerciales Royaume-Uni–UE fait encore bouger la paire."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR vers CHF — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des euros en francs suisses avec des taux en direct : le taux EUR/CHF du jour, une calculatrice gratuite, des tableaux de montants et le rôle de la BNS dans cette paire.",
        "h1": "EUR vers CHF — convertir des euros en francs suisses",
        "intro": [
            "EUR/CHF est le test de la valeur refuge de l'Europe : chaque fois que le stress de la zone euro monte — crise de la dette de 2011, alertes bancaires, guerre sur le continent — l'argent franchit la frontière suisse et la paire baisse. La Banque nationale suisse surveille ce taux plus que tout autre et est intervenue à plusieurs reprises pour empêcher le franc d'étouffer les exportations suisses.",
            "L'histoire moderne de la paire est spectaculaire : un plancher à 1,20 à partir de 2011, puis le décrochage de janvier 2015 qui a produit un krach éclair de 20 à 30 % en quelques minutes. Depuis, le franc se négocie comme un refuge propre, parfois trop fort — et la BNS reste un acteur actif de ce marché.",
        ],
        "faq": [
            ("Pourquoi la Banque nationale suisse se soucie-t-elle tant d'EUR/CHF ?",
             "Parce que l'économie suisse vend à l'Europe. Un franc trop fort rend les exportations suisses non compétitives et tire l'inflation sous la cible ; la BNS achète donc des devises (et a imposé des taux négatifs) pour plafonner la force du franc. Elle intervient sur cette paire plus que presque toute autre banque centrale d'un grand marché."),
            ("EUR/CHF est-elle une paire stable à détenir ?",
             "Stable en temps calme, explosive en crise — tout l'inverse d'une diversification. Le décrochage de 2015 reste l'avertissement classique : la promesse d'une banque centrale de plafonner une monnaie peut être retirée du jour au lendemain. Ceux qui traitaient la paire comme sans risque l'ont appris en une matinée."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR vers PLN — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des euros en zlotys polonais avec des taux en direct : le taux EUR/PLN du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger le zloty.",
        "h1": "EUR vers PLN — convertir des euros en zlotys polonais",
        "intro": [
            "La Pologne est la sixième économie de l'Union européenne à avoir conservé sa monnaie, et le zloty est la plus échangée des monnaies non euro de l'UE. EUR/PLN s'échange sur l'écart de taux avec la Banque nationale de Pologne, les fonds européens qui affluent vers l'est, les commandes allemandes pour l'industrie polonaise et le risque géopolitique régional.",
            "Depuis l'adhésion de la Pologne à l'UE en 2004, le zloty s'est renforcé dans les booms et chuté durement dans les crises — 2008 et 2022 ont poussé la paire à des extrêmes historiques. L'adoption éventuelle de l'euro restant indécise, la paire demeure une donnée structurelle de la finance européenne pour des années.",
        ],
        "faq": [
            ("La Pologne adoptera-t-elle l'euro et abandonnera-t-elle le zloty ?",
             "La Pologne est légalement tenue d'adopter l'euro à terme, mais sans date cible et avec un scepticisme public large. Tant qu'aucun calendrier crédible n'existe, EUR/PLN reste une paire activement échangée — les simples déclarations politiques sur le calendrier peuvent à elles seules la faire bouger."),
            ("Pourquoi EUR/PLN a-t-elle explosé en 2022 ?",
             "La guerre dans l'Ukraine voisine a fait de la Pologne une économie de première ligne du jour au lendemain : afflux de réfugiés, dépenses de défense et chocs énergétiques ont durement frappé la monnaie. La Banque nationale de Pologne est intervenue pour soutenir le zloty — les mouvements les plus violents de la paire en deux décennies."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP vers JPY — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des livres sterling en yens japonais avec des taux en direct : le taux GBP/JPY du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger cette paire volatile.",
        "h1": "GBP vers JPY — convertir des livres sterling en yens japonais",
        "intro": [
            "GBP/JPY — que les anciens traders appelaient « la bête » ou « le dragon » — est l'une des grandes paires les plus volatiles. Elle empile deux moteurs de risque : la sensibilité de la sterling aux nouvelles politiques et budgétaires britanniques, et le rôle du yen comme grande monnaie de financement mondiale, qui la fait osciller durement dès que le sentiment mondial tourne.",
            "La paire est un favori du carry trade : emprunter des yens à taux quasi nul pour acheter des livres mieux rémunérées. Cela fonctionne jusqu'à ce qu'une crise force tout le monde à se dégager en même temps — voilà pourquoi GBP/JPY monte en pente douce pendant des années et chute violemment en quelques semaines. Le dimensionnement et le timing comptent ici plus que sur presque toute autre grande paire.",
        ],
        "faq": [
            ("Pourquoi GBP/JPY est-elle plus volatile qu'USD/JPY ?",
             "Parce qu'elle multiplie deux volatilités. La sterling ajoute le risque politique et économique britannique au sentiment mondial de risque qui pilote déjà USD/JPY. La paire n'a aucune économie commune pour ancre, si bien qu'elle s'échange presque uniquement sur les écarts de taux et le sentiment — des ingrédients à grands mouvements."),
            ("Qu'est-ce que le carry trade sur GBP/JPY ?",
             "Emprunter des yens à taux japonais quasi nul pour investir en livres à taux britanniques plus élevés, en empochant la différence. C'est profitable tant que les marchés sont calmes, et punitif quand ils ne le sont pas : dans les épisodes de fuite vers la sécurité, le yen bondit quand les positions de carry se défont, souvent de 10 % ou plus face à la livre en quelques mois."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD vers JPY — Taux de change, convertisseur et tableaux",
        "description": "Convertissez des dollars australiens en yens japonais avec des taux en direct : le taux AUD/JPY du jour, une calculatrice gratuite, des tableaux de montants et ce qui fait bouger ce baromètre du risque.",
        "h1": "AUD vers JPY — convertir des dollars australiens en yens japonais",
        "intro": [
            "AUD/JPY est le baromètre de risque le plus pur du marché des changes. Le dollar australien incarne la croissance mondiale et la demande de matières premières — surtout la demande industrielle chinoise — tandis que le yen incarne la sécurité. Quand l'économie mondiale s'étend, la paire grimpe ; quand la panique frappe, elle chute plus vite que presque toute autre grande croisée.",
            "C'est aussi la paire classique du carry trade : pendant des décennies, les investisseurs ont emprunté des yens bon marché pour acheter l'Aussie mieux rémunéré. Ce flux façonne les longues tendances haussières de la paire et ses épisodes de dénouement violents — 2008 reste l'avertissement, quand AUD/JPY a perdu environ la moitié de sa valeur en quelques mois.",
        ],
        "faq": [
            ("Pourquoi les traders appellent-ils AUD/JPY un baromètre du risque ?",
             "Parce que chaque monnaie occupe un pôle opposé : l'Aussie monte avec la croissance mondiale et la demande de matières premières, le yen monte avec la peur. La paire évolue donc avec les marchés d'actions mondiaux à un degré que peu de croisées égalent — quand elle chute durement, le risque-off est réel."),
            ("Que s'est-il passé pour AUD/JPY pendant la crise de 2008 ?",
             "Elle a été environ divisée par deux. Le carry trade s'est dénoué quand le crédit mondial s'est gelé : les investisseurs ont vendu des dollars australiens pour rembourser leurs yens empruntés, et la paire s'est effondrée d'au-dessus de 100 vers le bas des 50 en quelques mois. Elle demeure l'exemple standard de la rapidité avec laquelle les stratégies de carry s'inversent."),
        ],
    },
}
