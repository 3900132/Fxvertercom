# -*- coding: utf-8 -*-
"""Currency-pair pages ("USD to EUR") — pair list, English content, and UI
scaffold strings.

Structure:
  PAIRS          — (from, to) tuples, one page per pair per indexed language.
                   Page URL: /currencies/<from>-to-<to>/ (lowercase codes).
  PAIR_UI        — per-language scaffold strings shared by all pair pages.
  PAIR_CONTENT   — per-language, per-pair copy. Key "USD-EUR" = (from, to).
                   Every language that has a complete entry gets pair pages
                   rendered; languages without entries get none (same policy
                   as guide translations).

Translations live in content/pair_pages_l10n_<lang>.py, each defining
PAIR_CONTENT_L10N and PAIR_UI_L10N; build-lang-pages.py merges them here.
"""

PAIRS = [
    ("USD", "EUR"), ("USD", "GBP"), ("USD", "JPY"), ("USD", "CNY"), ("USD", "INR"),
    ("USD", "CAD"), ("USD", "AUD"), ("USD", "CHF"), ("USD", "MXN"), ("USD", "PHP"),
    ("EUR", "GBP"), ("EUR", "CHF"), ("EUR", "PLN"), ("GBP", "JPY"), ("AUD", "JPY"),
]

# Scaffold strings, shared by every pair page in a language.
PAIR_UI = {
    "en": {
        "pairConvert": "Live converter",
        "pairRateHead": "Current exchange rate",
        "pairAsOf": "Reference rate as of {d}. The live converter above always fetches the latest rate — the tables below are a build-time snapshot for orientation.",
        "pairAmounts": "Common amounts: {f} to {t}",
        "pairReverse": "Common amounts: {t} to {f}",
        "pairMore": "More {f} conversions",
        "pairMorePairs": "More currency pairs",
        "pairIntroHead": "About the {f} to {t} exchange rate",
        "pairCurLinks": "Currency pages",
        "pairMetaTmpl": ("Convert {f} to {t} with live exchange rates: today's {f}/{t} rate, a free calculator, "
                         "common amount tables and what moves this currency pair."),
    },
}

PAIR_CONTENT = {
    "en": {
        # ───────────────────────── USD → EUR ─────────────────────────
        "USD-EUR": {
            "title": "USD to EUR — US Dollar to Euro Exchange Rate & Converter",
            "description": "Convert US Dollars to Euros with live rates: today's USD/EUR exchange rate, a free calculator, common amount tables and what moves the pair.",
            "h1": "USD to EUR — convert US Dollars to Euros",
            "intro": [
                "USD/EUR is the most traded currency pair in the world — roughly a quarter of all foreign-exchange turnover — which is why it has the tightest spreads and the deepest market of any conversion. The rate is simply the price of one US Dollar in Euros, set continuously by global trade, investment flows and the interest-rate gap between the Federal Reserve and the European Central Bank.",
                "For everyday conversions the practical question is what margin you are paying over the mid-market rate shown here. Banks typically add 1–4%; card and transfer services vary widely. Checking the live rate before a purchase or transfer tells you instantly whether a quote is fair.",
            ],
            "faq": [
                ("How is the USD to EUR exchange rate determined?",
                 "It floats freely — supply and demand for the two currencies set the price around the clock, influenced mainly by Fed and ECB interest-rate policy, inflation on both sides of the Atlantic, and global risk sentiment. There is no fixed or managed target."),
                ("When is the best time to convert USD to EUR?",
                 "Liquidity is deepest and spreads are tightest during the overlap of European and US trading hours (roughly 13:00–17:00 UTC). No one can reliably predict short-term direction, so for large amounts it is safer to convert in tranches than to wait for a better day."),
            ],
        },
        # ───────────────────────── USD → GBP ─────────────────────────
        "USD-GBP": {
            "title": "USD to GBP — US Dollar to British Pound Exchange Rate & Converter",
            "description": "Convert US Dollars to British Pounds with live rates: the USD/GBP exchange rate today, a free calculator, amount tables and what moves the pound.",
            "h1": "USD to GBP — convert US Dollars to British Pounds",
            "intro": [
                "The dollar–pound rate, nicknamed \"cable\" after the transatlantic telegraph cable that first carried it in the 1860s, is one of the oldest continuously quoted exchange rates in the world. Today it reflects the interest-rate gap between the Federal Reserve and the Bank of England, UK inflation, and the health of Britain's trade and fiscal position.",
                "Sterling trades most actively during London hours, and the pair is prone to sharp moves around UK economic data and fiscal announcements. Comparing any quote against the mid-market rate below is the fastest way to see how much margin a provider is taking.",
            ],
            "faq": [
                ("Why is the British Pound worth more than the US Dollar?",
                 "A higher unit price does not mean a stronger economy — it reflects history and denominations. The pound was the world's dominant currency when the dollar did not yet exist; the number itself says nothing about relative economic strength or purchasing power."),
                ("What moves USD/GBP most?",
                 "Interest-rate decisions from the Fed and the Bank of England, UK inflation prints, and political or fiscal news from Westminster. During the 2016 Brexit vote the pound fell roughly 10% in a day — a reminder that sterling carries political risk most major currencies do not."),
            ],
        },
        # ───────────────────────── USD → JPY ─────────────────────────
        "USD-JPY": {
            "title": "USD to JPY — US Dollar to Japanese Yen Exchange Rate & Converter",
            "description": "Convert US Dollars to Japanese Yen with live rates: the USD/JPY exchange rate today, a free calculator, amount tables and what moves the yen.",
            "h1": "USD to JPY — convert US Dollars to Japanese Yen",
            "intro": [
                "USD/JPY is the second most traded currency pair in the world and the classic barometer of the interest-rate gap between the United States and Japan. Because Japanese rates sat near zero for decades, the yen became the world's favourite funding currency — it weakens when markets are confident and strengthens sharply when crises unwind those positions.",
                "The pair is also watched for official Japanese intervention: the Ministry of Finance has repeatedly bought yen when it weakens too far, too fast. Large conversions are best checked against the mid-market rate, since retail margins on JPY can be deceptively wide.",
            ],
            "faq": [
                ("Why does the yen sometimes fall so much against the dollar?",
                 "Mainly because of the interest-rate gap. When US rates are high and Japanese rates stay near zero, investors sell yen to buy higher-yielding dollar assets — the carry trade. The yen can slide for months, then jump violently when those trades unwind."),
                ("Can the Japanese government change the USD/JPY rate?",
                 "It can lean against the market, not reverse it. Japan has intervened by buying or selling yen when moves became disorderly, sometimes with tens of billions of dollars in a single episode. Intervention smooths the path; it rarely changes the long-term direction set by fundamentals."),
            ],
        },
        # ───────────────────────── USD → CNY ─────────────────────────
        "USD-CNY": {
            "title": "USD to CNY — US Dollar to Chinese Yuan (RMB) Exchange Rate & Converter",
            "description": "Convert US Dollars to Chinese Yuan with live rates: the USD/CNY exchange rate today, a free calculator, amount tables and how the managed rate works.",
            "h1": "USD to CNY — convert US Dollars to Chinese Yuan",
            "intro": [
                "The dollar–yuan rate is the largest currency pair managed by a central bank. Each morning the People's Bank of China sets a daily fixing, and the onshore rate (CNY) is allowed to move only within a band around it — which is why USD/CNY moves far less day to day than its economic importance would suggest.",
                "China's trade surplus, capital controls and policy goals all shape the rate. For conversions, note that onshore CNY and offshore CNH can differ slightly, and that individual currency conversion in China is subject to capital-control rules. Always compare quotes against the reference rate below.",
            ],
            "faq": [
                ("Is the Chinese Yuan freely convertible?",
                 "Not fully. Trade-related conversion is easy, but investment flows across the border are controlled by quotas and approvals. That is why the offshore version (CNH) trades at a slightly different price from the onshore CNY — the gap reflects how expensive it is to move money across the border."),
                ("Why does USD/CNY barely move compared with other pairs?",
                 "Because the central bank manages it. The daily fixing and the trading band keep the rate stable relative to the dollar, in line with China's policy preference for predictability in trade. Managed does not mean fixed: the rate still trends with fundamentals over months and years."),
            ],
        },
        # ───────────────────────── USD → INR ─────────────────────────
        "USD-INR": {
            "title": "USD to INR — US Dollar to Indian Rupee Exchange Rate & Converter",
            "description": "Convert US Dollars to Indian Rupees with live rates: the USD/INR exchange rate today, a free calculator, amount tables and what moves the rupee.",
            "h1": "USD to INR — convert US Dollars to Indian Rupees",
            "intro": [
                "USD/INR is one of the world's most important remittance corridors — India receives more remittances than any other country — and a heavily traded emerging-market pair. The Reserve Bank of India manages volatility rather than the level: it smooths sharp moves using its reserves but lets the rupee find its long-term trend.",
                "The rupee's secular story is gradual depreciation against the dollar, driven by inflation differentials and India's current-account balance, punctuated by global risk events. For anyone sending money to India, the gap between the mid-market rate and the offered rate is where the real cost hides.",
            ],
            "faq": [
                ("Why does the Indian Rupee depreciate over time?",
                 "Mainly inflation differentials and the trade deficit: India imports far more than it exports, and the difference is financed by capital inflows. The RBI smooths the path, but over decades the rupee has drifted steadily weaker against the dollar — which is normal for a developing economy."),
                ("How do I get the best rate sending money to India?",
                 "Compare the offered rate against the mid-market rate before sending, not just the fees. Specialised remittance services usually beat bank wires on this corridor, and a difference of even 1% is significant on regular family transfers over a year."),
            ],
        },
        # ───────────────────────── USD → CAD ─────────────────────────
        "USD-CAD": {
            "title": "USD to CAD — US Dollar to Canadian Dollar Exchange Rate & Converter",
            "description": "Convert US Dollars to Canadian Dollars with live rates: the USD/CAD exchange rate today, a free calculator, amount tables and what moves the loonie.",
            "h1": "USD to CAD — convert US Dollars to Canadian Dollars",
            "intro": [
                "USD/CAD — \"loonie\" — is a top-five global currency pair built on one of the largest trading relationships on earth. Canada sends roughly three-quarters of its exports to the United States, so the pair trades heavily on US growth, energy prices (Canada is a major oil exporter) and the rate gap between the Fed and the Bank of Canada.",
                "When oil rises, CAD typically strengthens; when global growth fears hit, it weakens with commodity currencies in general. The pair is liquid around the clock, and quotes within a fraction of a percent of the mid-market rate are easy to find — so wide margins are always worth questioning.",
            ],
            "faq": [
                ("Why is the Canadian Dollar called the loonie?",
                 "After the loon — the bird on the one-dollar coin introduced in 1987. The nickname stuck and now refers to the currency itself in FX slang, as in \"the loonie rallied today\"."),
                ("Does the oil price really affect USD/CAD?",
                 "Yes, visibly. Crude oil and related products are Canada's largest export category, so rising oil tends to bring more dollars into Canada and lift the CAD. Traders treat the pair as a rough play on energy markets as well as on the two countries' interest rates."),
            ],
        },
        # ───────────────────────── USD → AUD ─────────────────────────
        "USD-AUD": {
            "title": "USD to AUD — US Dollar to Australian Dollar Exchange Rate & Converter",
            "description": "Convert US Dollars to Australian Dollars with live rates: the USD/AUD exchange rate today, a free calculator, amount tables and what moves the Aussie.",
            "h1": "USD to AUD — convert US Dollars to Australian Dollars",
            "intro": [
                "The Australian dollar is the classic commodity currency: its fortunes track iron ore, coal and gas exports, and above all Chinese demand for them. USD/AUD is therefore one of the cleanest real-time indicators of global risk appetite — the Aussie strengthens when world trade is booming and weakens in risk-off episodes.",
                "Interest-rate policy from the Reserve Bank of Australia and the Fed drives the shorter-term swings. Australia's working-holiday and student populations make USD→AUD (and back) a common recurring conversion, where even a 1% rate margin compounds quickly.",
            ],
            "faq": [
                ("Why is the Australian Dollar so sensitive to China?",
                 "China is Australia's largest export market by a wide margin, especially for iron ore used in steelmaking. When Chinese construction slows, commodity prices and the AUD usually fall together — the currency acts as a real-time barometer of Chinese heavy industry."),
                ("Is AUD a safe haven?",
                 "The opposite: traders call it a risk-on currency. In global panics — 2008, 2020 — money flows into US dollars and the Aussie tends to fall hardest among major currencies. That cyclicality is precisely why carry traders and growth watchers watch it so closely."),
            ],
        },
        # ───────────────────────── USD → CHF ─────────────────────────
        "USD-CHF": {
            "title": "USD to CHF — US Dollar to Swiss Franc Exchange Rate & Converter",
            "description": "Convert US Dollars to Swiss Francs with live rates: the USD/CHF exchange rate today, a free calculator, amount tables and what moves the franc.",
            "h1": "USD to CHF — convert US Dollars to Swiss Francs",
            "intro": [
                "The Swiss franc is the world's premier safe-haven currency: when war, banking stress or market panic strikes, money flows into Switzerland and CHF strengthens. USD/CHF therefore tends to fall in global crises even when the dollar itself is a refuge — the franc is simply the stronger shelter.",
                "The Swiss National Bank actively shapes the rate, from the famous euro floor of 2011–2015 to heavy intervention since. For conversions, Switzerland is also a reminder that a rich-country currency pair can still carry wide retail margins, especially at airports and hotels — always check the mid-market reference.",
            ],
            "faq": [
                ("Why is the Swiss Franc considered a safe haven?",
                 "A century of neutrality, low debt, a current-account surplus and a credible central bank make the franc the default parking place for money fleeing risk. Swiss inflation has also run far below the US and eurozone for decades, preserving the currency's purchasing power."),
                ("What did the SNB do in January 2015?",
                 "It abruptly abandoned its cap on the franc's strength against the euro. USD/CHF and EUR/CHF collapsed about 20–30% within minutes — one of the largest intra-day moves ever in a major pair, and the reason traders still respect the phrase \"SNB risk\"."),
            ],
        },
        # ───────────────────────── USD → MXN ─────────────────────────
        "USD-MXN": {
            "title": "USD to MXN — US Dollar to Mexican Peso Exchange Rate & Converter",
            "description": "Convert US Dollars to Mexican Pesos with live rates: the USD/MXN exchange rate today, a free calculator, amount tables and what moves the peso.",
            "h1": "USD to MXN — convert US Dollars to Mexican Pesos",
            "intro": [
                "USD/MXN is the most traded emerging-market currency pair in the Americas and one of the most liquid in the world. The peso trades on everything that moves the US economy — trade policy, growth, interest-rate gaps between the Fed and Banxico — plus oil prices and the enormous remittance corridor from the United States.",
                "Because it is so liquid, the pair moves fast on global risk sentiment: it is a classic carry-trade target that strengthens in calm markets and gaps violently in panics. For travellers and remittance senders, margins of 3–6% are common at airports — the mid-market rate below is the benchmark to compare against.",
            ],
            "faq": [
                ("Why is USD/MXN so volatile?",
                 "High interest rates in Mexico attract short-term carry money that leaves quickly in stress; the peso is also the reference asset for all US–Mexico trade and political news. The combination makes it liquid but jumpy — big daily moves are normal, not a malfunction."),
                ("What is the cheapest way to send dollars to Mexico?",
                 "Specialised remittance services consistently beat banks and cash-transfer storefronts on this corridor. Compare the amount delivered against the mid-market rate: on a 300-dollar transfer, the difference between a fair quote and a 5% margin can be a full day's local wage."),
            ],
        },
        # ───────────────────────── USD → PHP ─────────────────────────
        "USD-PHP": {
            "title": "USD to PHP — US Dollar to Philippine Peso Exchange Rate & Converter",
            "description": "Convert US Dollars to Philippine Pesos with live rates: the USD/PHP exchange rate today, a free calculator, amount tables and what moves the peso.",
            "h1": "USD to PHP — convert US Dollars to Philippine Pesos",
            "intro": [
                "The Philippine peso is anchored by one of the world's largest remittance flows: millions of overseas Filipino workers send money home, and those dollar inflows are a pillar of the economy. USD/PHP accordingly trades on global risk appetite, oil prices (the Philippines is a net importer) and policy from Bangko Sentral ng Pilipinas.",
                "The official rate is managed with a light hand — the central bank allows gradual adjustment while smoothing spikes. For OFW families and travellers, the spread between providers on this corridor is wide, so checking the mid-market rate before sending is the single easiest way to save.",
            ],
            "faq": [
                ("How do remittances affect the Philippine Peso?",
                 "Steady dollar inflows from overseas workers support the peso and the country's balance of payments — several percent of GDP every year. When global risk rises or host economies weaken, remittances soften and the peso tends to follow."),
                ("Is it better to convert USD to PHP in the US or in the Philippines?",
                 "It depends on the provider, not the country. Both sides of the corridor have cheap and expensive options; the deciding number is how many pesos the recipient actually receives. Compare quotes against the mid-market rate rather than trusting whichever storefront is closest."),
            ],
        },
        # ───────────────────────── EUR → GBP ────────────────────────
        "EUR-GBP": {
            "title": "EUR to GBP — Euro to British Pound Exchange Rate & Converter",
            "description": "Convert Euros to British Pounds with live rates: the EUR/GBP exchange rate today, a free calculator, amount tables and what moves this pair.",
            "h1": "EUR to GBP — convert Euros to British Pounds",
            "intro": [
                "EUR/GBP is the classic European cross: two economies that send roughly half their trade to each other, separated by one currency border. Because both are developed, low-inflation currencies, the pair moves far less than dollar crosses — it is really a bet on the relative fortunes of the eurozone and the UK.",
                "The interest-rate gap between the ECB and the Bank of England drives most of the trend, while UK political and fiscal news causes the spikes. For cross-channel workers, pensioners and businesses, the pair's stability makes small rate differences matter even more: a 1% margin is a large share of the total annual move.",
            ],
            "faq": [
                ("Why is EUR/GBP quieter than EUR/USD?",
                 "Neither the euro nor the pound is a global risk currency, so worldwide flight-to-safety flows pass them by. The pair mostly reflects UK–EU relative economics and rate differentials, which change slowly — though it can spike hard on British political news, as 2016 showed."),
                ("How does Brexit still affect EUR/GBP?",
                 "Structurally. New trade frictions since 2021 made the UK economy slightly less open to the EU, which most economists link to a structurally weaker sterling. Every round of UK–EU negotiations on trade rules still moves the pair."),
            ],
        },
        # ───────────────────────── EUR → CHF ────────────────────────
        "EUR-CHF": {
            "title": "EUR to CHF — Euro to Swiss Franc Exchange Rate & Converter",
            "description": "Convert Euros to Swiss Francs with live rates: the EUR/CHF exchange rate today, a free calculator, amount tables and the SNB's role in this pair.",
            "h1": "EUR to CHF — convert Euros to Swiss Francs",
            "intro": [
                "EUR/CHF is the safe-haven litmus test of Europe: whenever eurozone stress rises — the debt crisis of 2011, banking scares, war on the continent — money flows across the Swiss border and the pair falls. The Swiss National Bank watches it more closely than any other rate, and has repeatedly intervened to keep the franc from suffocating Swiss exports.",
                "The pair's modern history is dramatic: a floor at 1.20 from 2011, then the January 2015 depeg that produced a 20–30% flash crash in minutes. Since then the franc has traded as a clean, if sometimes too strong, refuge — and the SNB remains an active participant in this market.",
            ],
            "faq": [
                ("Why does the Swiss National Bank care so much about EUR/CHF?",
                 "Because Switzerland's economy sells to Europe. A franc that is too strong makes Swiss exports uncompetitive and drags inflation below target, so the SNB buys foreign currency (and once imposed negative rates) to cap the franc's strength. It intervenes in this pair more than almost any other central bank in a major market."),
                ("Is EUR/CHF a stable pair to hold?",
                 "It is stable in calm times and explosive in crises — the opposite of diversified. The 2015 depeg remains the textbook warning that a central bank's promise to cap a currency can be withdrawn overnight. Anyone treating the pair as riskless learned otherwise in one morning."),
            ],
        },
        # ───────────────────────── EUR → PLN ────────────────────────
        "EUR-PLN": {
            "title": "EUR to PLN — Euro to Polish Złoty Exchange Rate & Converter",
            "description": "Convert Euros to Polish Złoty with live rates: the EUR/PLN exchange rate today, a free calculator, amount tables and what moves the zloty.",
            "h1": "EUR to PLN — convert Euros to Polish Złoty",
            "intro": [
                "Poland is the European Union's sixth-largest economy that still uses its own currency, and the złoty is the most traded of the EU's non-euro currencies. EUR/PLN trades on the interest-rate gap with the National Bank of Poland, EU funds flowing east, German factory orders for Polish industry, and regional geopolitical risk.",
                "Since Poland joined the EU in 2004, the złoty has both strengthened in booms and fallen hard in crises — 2008 and 2022 pushed the pair to historic extremes. With Poland's eventual euro adoption still undecided, the pair remains a structural feature of European finance for years to come.",
            ],
            "faq": [
                ("Will Poland adopt the Euro and remove the złoty?",
                 "Poland is legally obliged to join the euro eventually but has no target date and wide public scepticism. Until a credible adoption timeline exists, EUR/PLN remains an actively traded pair — political statements about the timetable can move it by themselves."),
                ("Why did EUR/PLN spike in 2022?",
                 "The war in neighbouring Ukraine made Poland a frontline economy overnight: refugee inflows, defence spending and energy shocks hit the currency hard. The National Bank of Poland intervened to support the złoty — the pair's sharpest moves in two decades."),
            ],
        },
        # ───────────────────────── GBP → JPY ────────────────────────
        "GBP-JPY": {
            "title": "GBP to JPY — British Pound to Japanese Yen Exchange Rate & Converter",
            "description": "Convert British Pounds to Japanese Yen with live rates: the GBP/JPY exchange rate today, a free calculator, amount tables and what moves this volatile pair.",
            "h1": "GBP to JPY — convert British Pounds to Japanese Yen",
            "intro": [
                "GBP/JPY — old traders called it \"the beast\" or \"the dragon\" — is one of the most volatile major currency pairs. It stacks two risk engines on top of each other: sterling's sensitivity to UK political and fiscal news, and the yen's role as the world's funding currency, which makes it swing hard whenever global sentiment turns.",
                "The pair is a favourite of the carry trade: borrowing near-zero-rate yen to buy higher-yielding pounds. That works until a crisis forces everyone to unwind at once, which is why GBP/JPY tends to grind up for years and fall violently in weeks. Sizing and timing matter more here than in almost any other major pair.",
            ],
            "faq": [
                ("Why is GBP/JPY more volatile than USD/JPY?",
                 "Because it multiplies two volatilities. Sterling adds UK-specific political and economic risk on top of the global risk sentiment that already drives USD/JPY. The pair has no anchor economy in common, so it trades almost purely on rate gaps and sentiment — ingredients for big moves."),
                ("What is the carry trade in GBP/JPY?",
                 "Borrowing yen at near-zero Japanese rates and investing in pounds at higher UK rates, pocketing the difference. It is profitable while markets are calm and punishing when they are not: in risk-off episodes the yen surges as carry positions unwind, frequently 10% or more against the pound in months."),
            ],
        },
        # ───────────────────────── AUD → JPY ────────────────────────
        "AUD-JPY": {
            "title": "AUD to JPY — Australian Dollar to Japanese Yen Exchange Rate & Converter",
            "description": "Convert Australian Dollars to Japanese Yen with live rates: the AUD/JPY exchange rate today, a free calculator, amount tables and what moves this risk barometer.",
            "h1": "AUD to JPY — convert Australian Dollars to Japanese Yen",
            "intro": [
                "AUD/JPY is the purest risk barometer in the currency market. The Australian dollar represents global growth and commodity demand — above all Chinese industrial demand — while the yen represents safety. When the world economy is expanding, the pair climbs; when panic strikes, it falls faster than almost any other major cross.",
                "It is also the classic carry-trade currency pair: for decades investors borrowed cheap yen to buy the higher-yielding Aussie. That flow shapes the pair's long grinding uptrends and its violent unwind episodes — 2008 remains the cautionary tale, when AUD/JPY lost roughly half its value in a few months.",
            ],
            "faq": [
                ("Why do traders call AUD/JPY a risk barometer?",
                 "Because each currency sits at an opposite pole: the Aussie rises with global growth and commodity demand, the yen rises with fear. The pair therefore moves with world equity markets to a degree few other crosses match — when it falls hard, risk-off is real."),
                ("What happened to AUD/JPY in the 2008 crisis?",
                 "It roughly halved. The carry trade unwound as global credit froze: investors sold Australian dollars to repay borrowed yen, and the pair collapsed from above 100 to the low 50s within months. It remains the standard example of how quickly carry strategies reverse."),
            ],
        },
    },
}
