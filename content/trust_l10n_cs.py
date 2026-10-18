# -*- coding: utf-8 -*-
"""Czech (cs) trust pages (About / Privacy / Terms / Contact / Feedback).

Same shape as TRUST["en"] in trust_l10n.py: each entry has title, meta
description and a list of sections rendered in order — ["h", heading],
["p", paragraph] or ["li", list item]. LABELS holds the short nav chip
labels; it includes "feedback" because the site renders trust links for
all five TRUST_PAGES.
"""

TRUST_LANG = {
    "about": {
        "title": "O Fxverteru – bezplatný open-source převodník měn",
        "desc": "Kdo stojí za Fxverterem, proč existuje a čím se liší: převodník měn s důrazem na soukromí a otevřeným zdrojovým kódem, poctivými referenčními kurzy a srozumitelnými průvodci.",
        "sections": [
            ["p", "Fxverter je bezplatný online převodník měn s otevřeným zdrojovým kódem, který běží celý ve vašem prohlížeči. Zobrazuje referenční kurzy více než 140 světových měn, nevyžaduje žádný API klíč, žádnou registraci ani instalaci – otevřete web a rovnou převádíte."],
            ["h", "Proč jsme ho vytvořili"],
            ["p", "Většina převodnických webů zahrává skutečný kurz pod vyskakovací okna, zdi registrací a dotírání s instalací aplikace. My jsme chtěli opak: rychlý a soukromí respektující nástroj, který jako první ukazuje poctivý referenční střední kurz a pak se stáhne z cesty. Celý produkt je jedna statická stránka, která funguje na jakémkoli zařízení, v sedmi jazycích a po instalaci i offline."],
            ["h", "Čím se liší"],
            ["li", "Žádný účet, žádné sledování – převody běží lokálně ve vašem prohlížeči"],
            ["li", "Tři veřejné zdroje dat, mezi nimiž lze přepínat: Frankfurter (referenční kurzy Evropské centrální banky), ExchangeRate-API a Fawaz Currency API"],
            ["li", "40 hlavních měn se samostatnými stránkami: převodní tabulky v reálném čase, grafy trendů za 30/90 dní a profily měn"],
            ["li", "Srozumitelní průvodci, kteří vysvětlují, jak směnné kurzy doopravdy fungují"],
            ["li", "Lze nainstalovat jako aplikaci (PWA), která i offline pokračuje s posledními známými kurzy"],
            ["h", "O datech"],
            ["p", "Kurzy jsou orientační referenční kurzy z veřejných zdrojů centrálních bank a trhů, aktualizované denně. Jde o stejný srovnávací měřítkový kurz, který vidíte v Googlu nebo ve finančních zprávách – hodí se pro srovnávání a plánování, nejde ale o smluvní nabídku pro konkrétní převod."],
            ["h", "Kdo stojí za ním"],
            ["p", "Fxverter vytváří a udržuje nezávislý vývojář a podporují ho uživatelé. Kompletní zdrojový kód je veřejný na GitHubu – každý si ho může projít, hostovat sám nebo přispět vylepšeními."],
            ["p", "Máte dotazy, opravy nebo nápady? Napište na <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> – všechno si přečteme."],
        ],
    },
    "privacy": {
        "title": "Ochrana osobních údajů | Fxverter",
        "desc": "Co Fxverter sbírá a nesbírá: žádné vyžadované cookies, žádné účty, jen anonymní statistiky – a jak jsou řešeny reklama a služby třetích stran.",
        "sections": [
            ["p", "Fxverter je navržen tak, aby se dal používat bez předání jakýchkoli osobních údajů. Tyto zásady vysvětlují, co web sbírá a nesbírá, a jak jsou řešeny reklama a služby třetích stran. Naposledy aktualizováno: září 2026."],
            ["h", "Co nesbíráme"],
            ["p", "Účet není potřeba a web sám nenastavuje žádné reklamní cookies. Převody běží lokálně ve vašem prohlížeči – částky ani měnové páry, které převádíte, nikdy nevidíme."],
            ["h", "Informace sbírané automaticky"],
            ["p", "K pochopení celkového využití a vylepšení nástroje mohou být sbírány anonymní souhrnné statistiky návštěvnosti (zobrazení stránek a země, bez cookies). Tyto statistiky neumožňují vaši identifikaci."],
            ["h", "Informace, které sami odešlete"],
            ["p", "Použijete-li formulář zpětné vazby, jméno, e-mailová adresa a zpráva, které odešlete, slouží jen ke čtení a zodpovězení vaší zpětné vazby. Podpoříte-li projekt, platbu zpracovává Creem.io jako merchant of record – vaše kompletní platební údaje nikdy nedostaneme. Podporovatelé jsou jmenovitě uvedeni jen s jejich výslovným souhlasem."],
            ["h", "Služby třetích stran"],
            ["p", "Směnné kurzy si váš prohlížeč stahuje přímo z veřejných API (Frankfurter/ECB, ExchangeRate-API, Fawaz Currency API) – tyto požadavky přicházejí z vašeho zařízení, ne přes naše servery. Web je hostován jako statické soubory a anonymní analytika může běžet přes Cloudflare."],
            ["h", "Reklama"],
            ["p", "Tento web může zobrazovat reklamu zprostředkovanou přes Google AdSense. Dodavatelé třetích stran, včetně Googlu, používají cookies a podobné technologie k zobrazování reklam na základě vašich předchozích návštěv tohoto nebo jiných webů. Používání reklamních cookies umožňuje Googlu a jeho partnerům zobrazovat vám reklamy na základě návštěv našeho webu a/nebo dalších webů na internetu."],
            ["p", "Personalizovanou reklamu můžete vypnout v <a href=\"https://adssettings.google.com\" rel=\"noopener\">nastavení reklam Google</a> a cookies dodavatelů třetích stran odmítnout na <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Kde to vyžaduje zákon – například v EHP a ve Spojeném království – se personalizovaná reklama zobrazuje jen s vaším souhlasem, jinak se používá reklama nepersonalizovaná. Podrobnosti: <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">jak Google využívá informace z webů, které používají jeho služby</a>."],
            ["h", "Místní úložiště"],
            ["p", "Volba motivu, velikost písma, uložené měnové páry a načasování instalačního banneru se ukládají do místního úložiště vašeho prohlížeče. Tato data nikdy neopustí vaše zařízení a kdykoli je můžete vymazat v nastavení prohlížeče."],
            ["h", "Uchovávání a vaše práva"],
            ["p", "Zprávy zpětné vazby se uchovávají jen tak dlouho, jak je potřeba k odpovědi. Vymazání jakékoli odeslané zpětné vazby si můžete vyžádat napsáním na <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
            ["h", "Změny těchto zásad"],
            ["p", "Změní-li se postupy webu s daty, bude tato stránka aktualizována a výše uvedené datum revidováno. Pokračování v používání webu po změně znamená, že aktualizované zásady přijímáte."],
        ],
    },
    "terms": {
        "title": "Podmínky užívání | Fxverter",
        "desc": "Základní pravidla používání Fxverteru: kurzy jsou orientační referenční hodnoty, ne nabídky; služba je poskytována tak, jak je; a jak jsou řešeny odpovědnost, duševní vlastnictví a přijatelné používání.",
        "sections": [
            ["p", "Používáním fxverter.com s těmito podmínkami souhlasíte. Pokud nesouhlasíte, web prosím nepoužívejte. Naposledy aktualizováno: září 2026."],
            ["h", "Služba"],
            ["p", "Fxverter je bezplatný online převodník měn s otevřeným zdrojovým kódem, poskytovaný „tak, jak je“ a „tak, jak je k dispozici“, bez záruk jakéhokoli druhu, výslovných i mlčky předpokládaných – včetně přesnosti, dostupnosti nebo vhodnosti pro určitý účel."],
            ["h", "Směnné kurzy jsou pouze orientační"],
            ["p", "Všechny zobrazené kurzy jsou referenční kurzy sesbírané z veřejných zdrojů, jako jsou centrální banky a otevřená měnová API, obvykle aktualizované jednou denně. Jde o srovnávací měřítka – nejde o nabídky, o finanční poradenství ani o cenu, kterou vám jakýkoli poskytovatel skutečně nabídne. Nepoužívejte je pro finanční transakce, bankovní převody, fakturaci ani oficiální účetnictví; před transakcí si kurz vždy ověřte u své banky nebo finanční instituce."],
            ["h", "Omezení odpovědnosti"],
            ["p", "V maximálním rozsahu povoleném zákonem nenese udržovatelé Fxverteru odpovědnost za žádné ztráty ani škody vzniklé používáním webu či jeho dat, nebo nemožností je používat – včetně rozhodnutí učiněných na základě zobrazených kurzů."],
            ["h", "Duševní vlastnictví"],
            ["p", "Zdrojový kód je open source pod licencí MIT a je k dispozici na GitHubu. Texty, design a značka webu zůstávají majetkem projektu Fxverter; obsah webu nesmíte bez povolení zveřejňovat vcelku."],
            ["h", "Služby třetích stran a odkazy"],
            ["p", "Web spoléhá na veřejná API třetích stran a může odkazovat na weby třetích stran. Neovládáme je a neneseme odpovědnost za jejich obsah, dostupnost ani postupy."],
            ["h", "Přijatelné používání"],
            ["p", "Souhlasíte, že službu nebudete narušovat, nepokusíte ji přetížit a nebudete automatizované nástroje používat tak, aby se zhoršila pro ostatní návštěvníky."],
            ["h", "Změny těchto podmínek"],
            ["p", "Tyto podmínky mohou být občas aktualizovány; aktuální verzí je vždy tato stránka. Máte otázky? Napište na <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
        ],
    },
    "contact": {
        "title": "Kontakt | Fxverter",
        "desc": "Jak se dostat k týmu Fxverteru: zpětná vazba, opravy kurzů, licence a média – hello@fxverter.com nebo online formulář zpětné vazby.",
        "sections": [
            ["p", "Nejrychlejší cestou k nám je e-mail: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Každou zprávu si přečteme a obvykle odpovídáme během pár dní."],
            ["h", "O čem psát"],
            ["li", "Zpětná vazba a nápady na funkce – co funguje, co ne a co chybí"],
            ["li", "Opravy – vypadá-li něco na stránce špatně, řekněte nám, o kterou jde"],
            ["li", "Dotazy k licencím a opětovnému zveřejňování"],
            ["li", "Dotazy od médií a ohledně partnerství"],
            ["h", "Rychlejší cesta"],
            ["p", "Nechce se vám psát e-mail? Použijte <a href=\"../feedback/\">online formulář zpětné vazby</a> – dojde do stejné schránky a vyplnění zabere zhruba třicet sekund."],
            ["h", "Poznámka ke kurzům"],
            ["p", "Všechny kurzy jsou orientační referenční hodnoty z veřejných zdrojů, aktualizované denně – co to znamená v praxi, vysvětlují <a href=\"../guides/\">průvodci</a>. Než napíšete ohledně „špatného“ kurzu, porovnejte prosím s druhým zdrojem ve stejnou denní dobu: malé rozdíly mezi referenčními kurzy a nabídkami poskytovatelů jsou normální."],
            ["h", "Soukromí"],
            ["p", "Vaše e-mailová adresa slouží jen k zodpovězení – žádné newslettery, žádný marketing. Podrobnosti najdete v <a href=\"../privacy/\">zásadách ochrany osobních údajů</a>."],
        ],
    },
    "feedback": {
        "title": "Odeslat zpětnou vazbu | Fxverter",
        "desc": "Řekněte nám, co funguje, co nefunguje a co chybí – formulář zpětné vazby Fxverteru dojde přímo do schránky týmu, bez nutnosti mít účet.",
        "sections": [
            ["p", "Našli jste chybu, kurz, který vypadá zvláštně, nebo máte nápad, jak by Fxverter mohl být užitečnější? Níže uvedený formulář dojde přímo do naší schránky – bez nutnosti mít účet a vyplnění zabere zhruba třicet sekund."],
            ["h", "Co nám pomůže nejvíc"],
            ["li", "Kterou stránku nebo funkci jste používali"],
            ["li", "Co jste očekávali a co se doopravdy stalo"],
            ["li", "Váš prohlížeč nebo zařízení, je-li problém vizuální"],
            ["h", "Radši e-mail?"],
            ["p", "Napište na <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> – nebo prostě použijte níže uvedený formulář, dojde na stejné místo."],
        ],
        "form": {
            "name": "Jméno (nepovinné)",
            "email": "E-mail (nepovinný – jen pokud chcete odpověď)",
            "message": "Vaše zpráva",
            "send": "Odeslat zpětnou vazbu",
            "ok": "✓ Zpětná vazba odeslána – děkujeme!",
            "empty": "Nejprve napište zprávu.",
            "fail": "Odeslání selhalo – napište prosím přímo na hello@fxverter.com.",
        },
    },
}

LABELS = {
    "about": "O nás",
    "privacy": "Ochrana osobních údajů",
    "terms": "Podmínky užívání",
    "contact": "Kontakt",
    "feedback": "Zpětná vazba",
}
