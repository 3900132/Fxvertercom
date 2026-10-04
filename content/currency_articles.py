# -*- coding: utf-8 -*-
"""Long-form articles for flagship currency pages (English, rendered on the
EN pages at /currencies/<code>/).

Each entry: "sections" — ("h", heading), ("p", paragraph) or ("li", bullet);
and "faq" — (question, answer) pairs, rendered as details + FAQPage JSON-LD.
Only currencies with a complete entry get the article; the rest keep the
short profile until written. Target 600-800 words per currency, written for
a general reader (travel, remittance, business) — not filler text.
"""

CURRENCY_ARTICLES = {}

# ─────────────────────────── USD ───────────────────────────
CURRENCY_ARTICLES["USD"] = {
    "sections": [
        ("h", "A short history of the US Dollar"),
        ("p", "The US Dollar dates back to the Coinage Act of 1792, but its global role is a 20th-century story. The Bretton Woods agreement of 1944 made the dollar the anchor of the post-war monetary system: other currencies were pegged to it, and it alone was convertible to gold. When that link ended in 1971, the dollar kept its central place — oil was priced in dollars, trade was invoiced in dollars, and central banks stored their savings in dollars."),
        ("p", "Today the USD is the world's primary reserve currency, making up roughly 58% of official foreign-exchange reserves, and it sits on one side of nearly 90% of all foreign-exchange transactions. About half of global trade is invoiced in dollars, as is the majority of international debt."),
        ("p", "For anyone converting money this has one practical consequence: even a pair that doesn't involve the dollar is often priced through it behind the scenes. That is why USD-based reference rates are the benchmark for everything else."),
        ("h", "What moves the USD exchange rate"),
        ("p", "The dollar reacts to the same forces as any major currency — interest rates, inflation and growth — but at a scale no other currency matches."),
        ("li", "Federal Reserve policy: the world watches every Fed meeting, and higher US rates tend to strengthen the dollar as investors move money toward US yields"),
        ("li", "Inflation data: US CPI prints move currency markets within seconds of release"),
        ("li", "Safe-haven demand: in global crises (2008, 2020) money flows into dollars and US Treasuries, pushing the USD up"),
        ("li", "The global cycle: the dollar often strengthens when the US economy outperforms and eases when the rest of the world catches up"),
        ("h", "The US Dollar in practice"),
        ("p", "Traveling with dollars is easy almost everywhere: US cash is exchangeable in nearly every country, and where local currencies are unstable, prices are sometimes quoted in USD outright. Even so, paying or exchanging in the local currency is usually cheaper — dollar price tags abroad tend to hide an unfavorable rate."),
        ("p", "For remittances, the dollar is the measuring stick. Corridors are quoted as local currency per USD, so checking the mid-market USD rate before sending money tells you instantly how much margin a provider is taking."),
        ("p", "In business, dollar invoicing is about stability. A weaker dollar helps US exporters and squeezes importers, while the reverse applies to every company selling into the United States."),
        ("h", "Popular US Dollar conversions"),
        ("p", "USD/EUR is the most traded currency pair in the world, with the tightest spreads and the deepest market. USD/JPY dominates Asian flows and is highly sensitive to the interest-rate gap between the Fed and the Bank of Japan. USD/CNY is managed within a band set by China's central bank, so it moves less day to day than its trading volume would suggest. USD/MXN is one of the most liquid emerging-market pairs, watched closely by markets across the Americas."),
    ],
    "faq": [
        ("Is the US Dollar accepted everywhere?",
         "Dollars are exchangeable almost everywhere and are often informally accepted in economies with unstable local currencies. You will still almost always get a better effective rate paying in the local currency."),
        ("Why is the rate I'm offered worse than the mid-market rate?",
         "Banks and transfer services typically build a 1–4% margin into the rate they quote, sometimes more. Comparing the offer against the mid-market reference rate shows exactly how much you are paying."),
        ("Is the US Dollar a safe haven?",
         "Traditionally yes: deep markets, Treasury demand and the dollar's reserve role draw money in during crises. The dollar can still wobble at the peak of a panic, as in March 2008, but over decades it has been the standard refuge."),
    ],
}

# ─────────────────────────── EUR ───────────────────────────
CURRENCY_ARTICLES["EUR"] = {
    "sections": [
        ("h", "A short history of the Euro"),
        ("p", "The euro is the youngest of the major currencies and the boldest monetary experiment in history. It launched for electronic payments on 1 January 1999 and reached wallets as cash in 2002, replacing the Deutsche Mark, the French franc, the Italian lira, the Dutch guilder and more than a dozen other national currencies."),
        ("p", "It is the official currency of 20 EU members — the eurozone — plus several micro-states, and it is used daily by around 350 million people. The EUR is the second most traded currency in the world and the second largest reserve currency, at roughly 20% of global reserves."),
        ("p", "Monetary policy is set for the whole zone by the European Central Bank in Frankfurt: one interest rate serves Germany's industry, France's services and Italy's finances at the same time — which is exactly what makes euro politics interesting."),
        ("h", "What moves the EUR exchange rate"),
        ("p", "The euro trades on both economics and cohesion — markets constantly price in how well the currency union holds together."),
        ("li", "ECB policy and eurozone inflation, the same rate cycle story as the Fed but with twenty governments watching"),
        ("li", "The health of the big members: German industry, French services and Italian public finances all register in the EUR rate"),
        ("li", "Energy prices: Europe imports most of its energy, and the 2022 gas crisis famously pushed EUR/USD to parity for the first time in twenty years"),
        ("li", "Political stability of the bloc: elections and fiscal disputes in large members move the euro immediately"),
        ("h", "The Euro in practice"),
        ("p", "For travel, the euro's big advantage is simplicity: the same cash works from Lisbon to Helsinki. Payment habits differ — cash is still king in Germany and Austria, cards dominate the Nordics — but the currency itself never changes at an internal border."),
        ("p", "Within the eurozone, SEPA bank transfers are near-instant and essentially free, which makes the euro area one of the cheapest places in the world to move money. Cross-border payments leaving the zone are a different story and worth comparing carefully."),
        ("p", "For neighboring countries — Switzerland, the UK, Central and Eastern Europe — the euro acts as a pricing anchor for everything from rents to cars, so EUR reference rates matter well beyond the eurozone itself."),
        ("h", "Popular Euro conversions"),
        ("p", "EUR/USD is the world's most traded pair and usually has the tightest spreads of any conversion. EUR/GBP is the classic European cross, driven by trade and the interest-rate gap between Frankfurt and London. EUR/CHF is watched by the Swiss National Bank, which has intervened in it before. EUR/CNY has grown with EU–China trade and is increasingly quoted directly."),
    ],
    "faq": [
        ("Which countries use the euro?",
         "Twenty EU members form the eurozone, including Germany, France, Italy, Spain and the Netherlands. Andorra, Monaco, San Marino and Vatican City use it through agreements, and Kosovo and Montenegro use it unilaterally."),
        ("Is the euro stronger than the dollar?",
         "A higher unit price does not mean a stronger currency — it reflects denominations and history, not economic power. EUR/USD traded above 1.40 before the 2008 crisis, fell to parity in 2022, and neither move said much on its own about European purchasing power."),
        ("Will more countries adopt the euro?",
         "Every EU member is obliged to adopt the euro eventually once it meets the criteria, apart from Denmark which has an opt-out. Several members in Central and Eastern Europe are in the queue, joining Croatia, which adopted the euro in 2023."),
    ],
}

# ─────────────────────────── JPY ───────────────────────────
CURRENCY_ARTICLES["JPY"] = {
    "sections": [
        ("h", "A short history of the Japanese Yen"),
        ("p", "The yen was adopted in 1871 with the New Currency Act, replacing the tangled patchwork of Edo-period domain notes. It became a hard currency with the gold standard, went through wartime turmoil, and floated after 1971. The Plaza Accord of 1985 roughly doubled its value against the dollar within a few years, resetting Japan's export economy."),
        ("p", "Today the JPY is the third most traded currency in the world and a major reserve currency. Decades of near-zero interest rates gave it a second job: the world's favorite funding currency. Investors borrowed cheap yen to buy higher-yielding assets elsewhere — the famous carry trade — which makes the yen fall when markets are confident and surge when crises force those positions to unwind."),
        ("h", "What moves the JPY exchange rate"),
        ("p", "USD/JPY is essentially a two-country interest-rate story wrapped around a risk barometer."),
        ("li", "Bank of Japan policy: the last major central bank to leave negative rates behind (2024), after a long era of yield-curve control and bond buying"),
        ("li", "The US–Japan rate gap: the single biggest driver of USD/JPY — a wider gap favors the dollar, a narrowing one favors the yen"),
        ("li", "Risk sentiment: despite low rates, the yen strengthens in global crises as offshore positions unwind and money comes home"),
        ("li", "Intervention: Japan's Ministry of Finance has stepped into the market directly when moves turned disorderly, most notably in 2022"),
        ("h", "The Yen in practice"),
        ("p", "Japan was famously a cash-first country, and cash still matters at small restaurants, shrines and rural inns — but IC cards like Suica and card payments are now accepted almost everywhere in cities. The standard traveler trick remains withdrawing yen from 7-Eleven ATMs, which take foreign cards reliably."),
        ("p", "For Japan itself, a weak yen is a double-edged sword: it lifts exporters and record inbound tourism, while squeezing households through the import bill for energy and food. That domestic tension is exactly why yen moves get political attention faster than most currencies."),
        ("h", "Popular Yen conversions"),
        ("p", "USD/JPY is the most traded pair in Asia and a global benchmark. EUR/JPY and GBP/JPY are popular with trend traders for their volatility. CNY/JPY reflects the enormous trade relationship between Japan and China, and KRW and other Asian currencies are often quoted against the yen as regional benchmarks."),
    ],
    "faq": [
        ("Why has the yen been so weak recently?",
         "Mostly the interest-rate gap: when US rates stayed high while the Bank of Japan kept rates near zero, money moved toward the dollar. The yen tends to recover when the gap narrows, either through BOJ hikes or Fed cuts."),
        ("Do I need cash in Japan?",
         "Less than before — cards and IC cards work in most places now — but you should still carry cash for small restaurants, shrines and rural areas. 7-Eleven and Japan Post ATMs accept foreign cards."),
        ("Why are yen prices such big numbers?",
         "The yen has no widely used minor unit (sen are obsolete), and it was historically quoted against the dollar at over 100 yen per USD. The big numbers are just how the currency is denominated, not a sign of weakness."),
    ],
}

# ─────────────────────────── GBP ───────────────────────────
CURRENCY_ARTICLES["GBP"] = {
    "sections": [
        ("h", "A short history of the Pound Sterling"),
        ("p", "The pound is the oldest living currency: silver pennies called sterlings circulated in Anglo-Saxon England twelve centuries ago, and twelve of them made a shilling — twenty shillings made the pound. Britain stayed on that duodecimal system until 1971, when the currency finally went decimal."),
        ("p", "The UK invented the gold standard, anchored world trade during the empire era, and then managed a long, orderly decline from it — including the 1992 Black Wednesday, when speculators forced the pound out of the European exchange-rate mechanism in a single day. That episode is why Britain never adopted the euro, and why the Bank of England's independence, granted in 1997, matters so much to the currency's credibility today."),
        ("h", "What moves the GBP exchange rate"),
        ("p", "Sterling trades on monetary policy, real-economy data and politics — with politics punching above the weight other currencies are used to."),
        ("li", "Bank of England policy and UK inflation: rate expectations move sterling immediately"),
        ("li", "Gilt yields and fiscal credibility: budgets that unsettle bond markets unsettle the pound too (see the mini-budget of September 2022)"),
        ("li", "Political shocks: Brexit showed that structural news can re-rate the pound by double digits over a few years"),
        ("li", "The London financial industry: the UK runs a structural surplus in financial services, which supports sterling demand"),
        ("h", "The Pound in practice"),
        ("p", "The UK is one of the easiest places to travel cash-light: contactless cards and phones work nearly everywhere, from London taxis to village pubs. Cash still helps at markets and some small cafés, and note that Scotland and Northern Ireland issue their own banknotes — perfectly legal, but sometimes refused back in England, so spend them before leaving."),
        ("p", "For money moving between the UK and the EU, post-Brexit corridors no longer benefit from SEPA-like simplicity, so comparing providers genuinely pays. London remains the world's largest foreign-exchange trading hub — over a third of global FX volume is traded there."),
        ("h", "Popular Pound conversions"),
        ("p", "GBP/USD is nicknamed cable, after the transatlantic telegraph cable that first carried its price between London and New York in the 1860s. EUR/GBP is the day-to-day pair for European trade and travel. GBP/JPY — the beast among traders — is one of the most volatile majors, and GBP/INR and GBP/AED serve some of the largest remittance corridors in the world."),
    ],
    "faq": [
        ("Why is it called sterling? And cable?",
         "Sterling comes from the old silver pennies (easterlings); the currency's full name is pound sterling. Cable is the GBP/USD nickname from the 19th-century transatlantic telegraph cable that quoted the rate."),
        ("Will the UK ever join the euro?",
         "There is no current political plan to adopt the euro. The 1992 ERM exit and the 2016 Brexit vote pushed the question off the agenda for the foreseeable future."),
        ("Are Scottish banknotes valid in England?",
         "Yes — Scottish and Northern Ireland notes are legal currency across the UK, though some English shops are unfamiliar with them and refuse them. They exchange at par at any bank."),
    ],
}

# ─────────────────────────── CNY ───────────────────────────
CURRENCY_ARTICLES["CNY"] = {
    "sections": [
        ("h", "A short history of the Renminbi"),
        ("p", "The renminbi, China's official currency, was issued by the newly founded People's Bank of China in 1948, before the PRC itself was proclaimed; the yuan is its basic unit. Through the planned-economy decades it was an internal accounting unit; the 1978 reform era turned it into a real currency again."),
        ("p", "The modern story is a gradual internationalization: the 1994 unification of exchange rates, the 2005 move to a managed float, the 2015 surprise devaluation that shook global markets, and 2016, when the IMF added the yuan to its Special Drawing Rights basket — formal recognition as a reserve currency. The digital yuan (e-CNY) is the newest chapter and one of the first major central bank digital currencies."),
        ("h", "What moves the USD/CNY exchange rate"),
        ("p", "The yuan is not a free-floating currency, and that shapes everything: the People's Bank of China sets a daily central parity (the fixing) and lets the market rate move only within a band around it (currently ±2%)."),
        ("li", "The PBOC fixing: the single most important number, published every morning at 9:15 Beijing time"),
        ("li", "Trade flows: China's surplus puts structural upward pressure on the currency; capital controls hold it back"),
        ("li", "Policy signals: devaluations (2005, 2015) tend to come in clusters during trade tensions"),
        ("li", "Offshore sentiment: the freely traded CNH in Hong Kong often moves ahead of the onshore rate when tension builds"),
        ("h", "The Renminbi in practice"),
        ("p", "China is close to a cashless society: Alipay and WeChat Pay dominate everything from metro rides to street dumplings. Foreign visitors can now link international cards (Visa, Mastercard) to Alipay or WeChat Pay directly, which has transformed travel in China since 2023. Cash still works everywhere but is increasingly rare in daily use."),
        ("p", "The yuan is not freely convertible: residents face a $50,000 annual quota, and cross-border transfers need documentation. For remittance corridors into China, licensed services handle the conversion legally; sums above the quotas require bank paperwork."),
        ("h", "Popular Renminbi conversions"),
        ("p", "USD/CNY is the pair the whole world watches — a barometer of trade relations. EUR/CNY and JPY/CNY track Europe's and Japan's trade with China. Traders distinguish onshore CNY from offshore CNH, and the small gap between them is itself a market signal."),
    ],
    "faq": [
        ("What is the difference between CNY and RMB?",
         "None in practice: RMB (renminbi, 人民币) is the currency's official name — the people's currency — and CNY is its ISO code. The yuan is the base unit, like the dollar in USD."),
        ("Why does USD/CNY barely move some months?",
         "Because it is managed. The PBOC's daily fixing and the ±2% band mean the rate follows policy as much as markets — sharp moves usually signal a deliberate shift."),
        ("What is CNH?",
         "CNH is the offshore yuan, traded freely in Hong Kong and other financial centers outside mainland capital controls. It can diverge slightly from onshore CNY, and the gap widens when capital-flow tension builds."),
    ],
}

# ─────────────────────────── CHF ───────────────────────────
CURRENCY_ARTICLES["CHF"] = {
    "sections": [
        ("h", "A short history of the Swiss Franc"),
        ("p", "The Swiss franc dates to 1850, when the young federal state standardized the coins that cantons had minted separately for centuries. Switzerland's formula for the currency was always the same: political neutrality, hard money and a central bank legally obliged to keep price stability first."),
        ("p", "That formula made the franc the world's classic safe haven — it strengthened through the oil shocks, the eurozone debt crisis and the 2008 crash. The most dramatic chapter came on 15 January 2015, when the Swiss National Bank abruptly abandoned its 1.20 floor against the euro; EUR/CHF collapsed about 20% in minutes, one of the largest currency moves in modern history."),
        ("h", "What moves the CHF exchange rate"),
        ("p", "The franc trades less on Swiss growth (the economy is famously steady) and more on fear and the Swiss National Bank."),
        ("li", "Global risk sentiment: European crises in particular push money into francs — geographically close, politically neutral"),
        ("li", "SNB policy: the bank uses both interest rates and direct currency interventions, and it does not hesitate to act against unwanted strength"),
        ("li", "Inflation: Swiss inflation has been the lowest in Europe through the recent cycle, reinforcing the hard-money reputation"),
        ("li", "The eurozone: because half of Swiss trade is with the EU, EUR/CHF is the pair the SNB watches most closely"),
        ("h", "The Swiss Franc in practice"),
        ("p", "Switzerland is expensive, and the franc is why. Cards and contactless work everywhere; cash still circulates more than in the Nordics, and the banknotes are famously durable and recently redesigned. Travelers from eurozone neighbors often pay in euros at the border regions, but the exchange rate offered is rarely favorable — always choose the local currency."),
        ("p", "For salaries and savings, the franc is what it has always been: the region's storage of value. For remittance, Switzerland is one of the most expensive corridors in Europe — the markup gap between banks and specialist services is unusually wide, so comparing providers is especially important."),
        ("h", "Popular Swiss Franc conversions"),
        ("p", "EUR/CHF is the structurally most important pair — the SNB has repeatedly shaped it, from the 2011–2015 floor to the interventions since. USD/CHF is the global risk gauge for the franc, and GBP/CHF and CHF/AED serve wealthy corridors and expat salaries."),
    ],
    "faq": [
        ("Why is the Swiss Franc a safe haven?",
         "Neutrality, deep and stable financial markets, low inflation, a current-account surplus and a central bank with a legal mandate for stability. In a crisis, capital goes where it expects to be left alone."),
        ("What happened in January 2015?",
         "The SNB had capped the franc at 1.20 per euro since 2011, buying unlimited foreign currency to defend it. When keeping the cap became too expensive, it scrapped the floor without warning — the franc jumped about 20% in minutes, bankrupting brokers and funds worldwide."),
        ("Why does the SNB intervene in currency markets?",
         "Switzerland is a small, open, exporting economy. An overly strong franc crushes exporters and pulls inflation below zero, so the SNB buys foreign currency to smooth the moves — one of the few major banks that intervenes against its own currency's strength."),
    ],
}

# ─────────────────────────── CAD ───────────────────────────
CURRENCY_ARTICLES["CAD"] = {
    "sections": [
        ("h", "A short history of the Canadian Dollar"),
        ("p", "Canada adopted its dollar in 1858, decimalized alongside the US to keep cross-border trade simple, and floated the currency in 1970 after decades of pegs. Canadians call the $1 coin the loonie (after the loon on its back) and the $2 coin the toonie — names that stuck so well that exchange desks worldwide use them."),
        ("p", "The modern Canadian dollar is a classic commodity currency: what happens to Canadian resources — above all oil, but also lumber, grain, metals and potash — is what happens to the CAD."),
        ("h", "What moves the CAD exchange rate"),
        ("p", "Three forces dominate, and they usually point the same way."),
        ("li", "Oil prices: Canada is a top-tier crude exporter, and USD/CAD has tracked WTI for years — rising oil generally means a stronger loonie"),
        ("li", "The US economy: about three quarters of Canadian exports go to the United States, so US demand is Canadian income"),
        ("li", "Bank of Canada policy: inflation targeting since 1991, with rate decisions moving the pair alongside the Fed's cycle"),
        ("h", "The Canadian Dollar in practice"),
        ("p", "Travelers find Canada entirely card-first — credit and debit work everywhere, tips are expected (15–20%), and cash is mostly for small markets. Prices are displayed without sales tax, which is added at checkout, a recurring surprise for visitors."),
        ("p", "The US–Canada corridor is one of the cheapest remittance routes in the world thanks to fierce competition, while corridors beyond North America cost more and deserve comparison. For businesses, the CAD's oil-and-US linkage makes it a natural hedge for anyone buying Canadian resources or selling into Canada."),
        ("h", "Popular Canadian Dollar conversions"),
        ("p", "USD/CAD is one of the most liquid pairs in the world. CAD/JPY is a favorite oil-linked cross. EUR/CAD and GBP/CAD serve European travel and trade, and CNY/CAD has grown with Chinese demand for Canadian commodities."),
    ],
    "faq": [
        ("Why does the Canadian Dollar follow oil prices?",
         "Crude oil is Canada's largest single export, and export earnings flow into the currency. When oil rises, Canada's terms of trade improve and the loonie tends to strengthen against currencies of oil importers."),
        ("What are loonies and toonies?",
         "Nicknames: the loonie is the $1 coin (a loon appears on it, since 1987) and the toonie is the $2 coin (introduced 1996). Both replaced paper notes that wore out too fast."),
        ("Is Canada expensive to visit?",
         "By US standards, mid-range costs are similar, but the sales tax (5–15% depending on province) is added at the register, and tips of 15–20% are expected — budget with both in mind."),
    ],
}

# ─────────────────────────── AUD ───────────────────────────
CURRENCY_ARTICLES["AUD"] = {
    "sections": [
        ("h", "A short history of the Australian Dollar"),
        ("p", "Australia replaced pounds, shillings and pence with the decimal dollar on 14 February 1966, and floated the currency in 1983. Since then the Aussie has become the most traded commodity currency on earth — and a case study in how a mid-sized economy's money can become a global instrument."),
        ("p", "The engine is Asia's industrialization: Australia sells iron ore, coal, gold and gas to the region, above all to China, its largest trading partner. The AUD accordingly became the market's preferred way to trade Chinese growth without touching Chinese capital controls."),
        ("h", "What moves the AUD exchange rate"),
        ("p", "The Aussie is a risk-on currency: it strengthens when the world economy looks healthy and weakens when fear rises."),
        ("li", "China's demand: iron ore and coal prices are the AUD's daily heartbeat — Chinese stimulus lifts it, property slumps dent it"),
        ("li", "Risk sentiment: AUD/JPY is the classic barometer — it rises in calm markets and plunges in panics"),
        ("li", "Reserve Bank of Australia policy: rate decisions and the terms-of-trade boom of 2011 (AUD above USD) or the 2020 COVID plunge show the range"),
        ("li", "Gold: a significant export, adding a second commodity leg to the currency"),
        ("h", "The Australian Dollar in practice"),
        ("p", "Australia runs one of the most cashless economies on the planet — contactless payments are accepted almost everywhere, and even buskers take cards. Travelers barely need cash outside remote areas. Prices include GST (10%) by law, so the displayed price is the price you pay."),
        ("p", "For remittances, Australia's corridors are competitive and well served by specialist providers. For businesses, the AUD's China linkage makes it the hedge of choice for anyone exposed to Australian commodities or Asian demand."),
        ("h", "Popular Australian Dollar conversions"),
        ("p", "AUD/USD is the most traded commodity-currency pair in the world. AUD/JPY is the risk barometer traders watch in every scare. AUD/CNY tracks the trade relationship with China, and AUD/NZD is the trans-Tasman pair that moves on the two economies' relative strength."),
    ],
    "faq": [
        ("Why is the AUD called a commodity currency?",
         "Because its value moves with the commodities Australia exports — above all iron ore and coal. When world commodity demand rises, export income rises, and the currency follows."),
        ("Is the AUD a risk-on currency?",
         "Yes. Its yield and its exposure to Asian growth make it the market's favorite expression of global optimism; in crises (2008, 2020) it fell faster than almost any major currency, then recovered with trade."),
        ("Why does the AUD fall when China slows?",
         "China buys about a third of Australian exports. Slower Chinese industry means lower commodity demand and prices, which feeds directly into Australia's income and the currency."),
    ],
}

# ─────────────────────────── TRY ───────────────────────────
CURRENCY_ARTICLES["TRY"] = {
    "sections": [
        ("h", "A short history of the Turkish Lira"),
        ("p", "The lira has been the currency of the Republic of Turkey since 1923, inheriting the Ottoman pound. Its modern history is a chronicle of chronic inflation: prices rose so persistently that in 2005 Turkey knocked six zeros off, creating the New Turkish Lira (the New was dropped in 2009). A middle-class savings habit in foreign currency — dollars under mattresses and gold at home — grew out of those decades."),
        ("p", "The 2018 currency crisis and the 2021–2023 experiment of cutting interest rates despite inflation (which peaked above 80%) pushed the lira to historic lows, and dollarization climbed to record levels. Since 2023, a return to orthodox monetary policy has begun rebuilding credibility — the single most important variable for the currency's future."),
        ("h", "What moves the TRY exchange rate"),
        ("p", "The lira's drivers are less about trade and more about trust."),
        ("li", "Central bank credibility: real interest rates (policy rate minus inflation) are the number to watch; negative real rates have meant depreciation"),
        ("li", "Political influence over policy: markets price the risk of interference in monetary decisions"),
        ("li", "Dollarization: when locals convert savings into dollars and gold, the lira weakens — and the reverse rebuilds it"),
        ("li", "External balances: Turkey imports energy and runs structural deficits, financed by tourism, exports and hot money"),
        ("h", "The Lira in practice"),
        ("p", "For travelers, Turkey is rewarding and cheap in lira terms, and the country's exchange offices (döviz bürosu) in tourist areas quote genuinely competitive rates — often better than banks, with low or no commission. Cards are accepted broadly, but carrying cash is normal, and prices for hotels are sometimes quoted in euros or dollars to escape volatility."),
        ("p", "For remittances, volatility is the enemy: what the recipient receives can change noticeably between sending and settling, so sending promptly and comparing the total received matters more than for stable currencies. Contracts and rents inside Turkey are increasingly indexed to dollars or euros."),
        ("h", "Popular Lira conversions"),
        ("p", "USD/TRY and EUR/TRY are the pairs that matter for everything from imports to tourism. EUR/TRY matters even more for European visitors and exporters, and GBP/TRY serves one of Turkey's biggest tourism markets."),
    ],
    "faq": [
        ("Why does the Turkish Lira keep losing value?",
         "A mix of structurally high inflation, negative real interest rates during unorthodox policy episodes, and episodes of political pressure on the central bank. Money seeks positive real returns, and the lira often lacked them."),
        ("What is the difference between TL and TRY?",
         "TL is the Turkish abbreviation (Türk Lirası) and TRY is the ISO code — same currency. The 2005 reform removed six zeros, so today's lira equals one million old lira."),
        ("Should I exchange money before traveling to Turkey?",
         "No need to exchange much at home: exchange offices in Turkey are competitive and abundant. Bring euros, dollars or pounds in clean notes and change locally — or simply withdraw and pay by card; just avoid airport desks for large amounts."),
    ],
}

# ─────────────────────────── INR ───────────────────────────
CURRENCY_ARTICLES["INR"] = {
    "sections": [
        ("h", "A short history of the Indian Rupee"),
        ("p", "The rupee's lineage goes back to the silver rupiya minted in the 16th century under Sher Shah Suri, standardized through the Mughal era and inherited by British India. After independence in 1947 the rupee was pegged and tightly controlled; crises in 1966 and 1991 forced devaluations, and the 1991 balance-of-payments crisis famously airlifted India's gold as collateral — the moment the economy opened up."),
        ("p", "Two modern episodes stand out: the 2016 demonetization, which withdrew the largest banknotes overnight, and the UPI revolution — a public digital-payment rail launched that same year that now processes billions of transactions a month, making India one of the world's most cashless major economies by volume."),
        ("h", "What moves the INR exchange rate"),
        ("p", "The rupee is managed by the Reserve Bank of India with a light touch — it floats, but with smoothing against disorderly moves."),
        ("li", "Oil: India imports the bulk of its crude, so oil spikes are the classic rupee stress test"),
        ("li", "Trade deficit vs inflows: the deficit is structurally offset by the world's largest remittance inflows (over $100 billion a year) and services exports"),
        ("li", "RBI policy and inflation: rate differentials with the Fed drive capital flows in and out"),
        ("li", "Foreign portfolio flows: Indian equities' popularity with global funds swings the currency month to month"),
        ("h", "The Rupee in practice"),
        ("p", "India runs on UPI: QR codes at every stall, auto-rickshaw and temple donation box. Foreign visitors can now link international cards to UPI-enabled apps in India, and cards work in cities — but cash still rules in rural areas and small towns, so carry some. ATMs are everywhere; withdrawal limits per transaction are modest."),
        ("p", "For remittances, India is the world's number-one recipient country, and the corridor is ferociously competitive — specialist services undercut banks by wide margins, so comparing the total received is worth real money on every transfer."),
        ("h", "Popular Rupee conversions"),
        ("p", "USD/INR is the reference pair, with a deep forward market. EUR/INR and GBP/INR serve Europe's trade and travel, and AED/INR is one of the highest-volume remittance pairs on earth, connecting millions of workers in the Gulf to home."),
    ],
    "faq": [
        ("Why does the rupee weaken over the long term?",
         "A structural trade deficit (oil above all) plus India's higher inflation than its main partners. The depreciation is gradual, and remittances plus services exports keep it orderly."),
        ("What is UPI?",
         "Unified Payments Interface — India's public, instant, free digital-payment system, launched in 2016. It processes more real-time transactions than any comparable system in the world, and foreign visitors can now use it with international cards."),
        ("What was demonetization in 2016?",
         "Overnight withdrawal of the two largest banknotes (₹500 and ₹1000), about 86% of cash in circulation, to fight untaxed wealth. It caused months of cash queues and permanently accelerated India's shift to digital payments."),
    ],
}

# ─────────────────────────── MXN ───────────────────────────
CURRENCY_ARTICLES["MXN"] = {
    "sections": [
        ("h", "A short history of the Mexican Peso"),
        ("p", "The peso is the direct descendant of the Spanish colonial real — the original global trade coin — and Mexico has issued its own since 1823. The 1980s debt and inflation crises ended in 1993 with the Nuevo Peso, which removed three zeros; the Nuevo was dropped from the name in 1996. The 1994 Tequila crisis then forced the peso to float, and it has been freely traded ever since."),
        ("p", "Today the Mexican peso is the most traded currency in Latin America and one of the top emerging-market pairs globally, with a new tailwind: nearshoring, as factories relocate closer to the US market."),
        ("h", "What moves the MXN exchange rate"),
        ("p", "The peso trades on its own central bank and on America's economy at the same time — a double exposure no other currency has quite so strongly."),
        ("li", "Banxico policy: an independent, orthodox inflation targeter, often holding rates higher than the Fed for long stretches"),
        ("li", "The US economy: about 80% of Mexican exports go north, and US recessions hit the peso first"),
        ("li", "Remittances: over $60 billion a year flows in from the US — one of the world's largest corridors and a steady dollar supply"),
        ("li", "Risk appetite and carry: high Mexican rates make the peso a favorite carry-trade currency — strong in calm times, sharp drops in panics"),
        ("h", "The Peso in practice"),
        ("p", "Travelers find Mexico comfortably card-friendly in cities and resorts, with cash still essential at markets, taxis and small eateries — the OXXO convenience-store cash culture is real. ATMs are widespread; use bank-affiliated ones, decline the machine's conversion offer, and note tips of 10–15% are customary."),
        ("p", "For remittances, the US–Mexico corridor is the largest on earth and among the cheapest — competition has pushed fees to a few percent or less. Beyond the Americas, compare providers carefully; the spread differences are significant."),
        ("h", "Popular Peso conversions"),
        ("p", "USD/MXN is one of the most liquid emerging-market pairs in the world and a favorite of traders for its volatility. EUR/MXN and GBP/MXN serve European travel and trade, and MXN/JPY appears in carry strategies."),
    ],
    "faq": [
        ("Why is USD/MXN so volatile?",
         "The peso combines emerging-market risk with a huge carry trade: global funds borrow cheap currencies and hold pesos for the rate gap. When fear spikes, those positions unwind fast and the peso falls sharply — the reverse is true in calm markets."),
        ("What was the 1993 revaluation?",
         "After the 1980s inflation crises, Mexico replaced 1,000 old pesos with 1 new peso (the Nuevo Peso) in 1993. Today's peso equals one thousand pre-1993 pesos."),
        ("Should I use cash or card in Mexico?",
         "Both: cards work in cities, malls and resorts, but carry pesos in cash for markets, street food, taxis and small towns. Pay in pesos, never accept the terminal's offer to charge in dollars."),
    ],
}

# ─────────────────────────── BRL ───────────────────────────
CURRENCY_ARTICLES["BRL"] = {
    "sections": [
        ("h", "A short history of the Brazilian Real"),
        ("p", "The real arrived in July 1994 with the Plano Real, one of the most successful stabilization programs ever run: Brazil had lived through generations of runaway inflation — peaking near 2,500% a year — and the new currency, backed by fiscal reform and a pegged start, ended it almost overnight."),
        ("p", "The peg broke in 1999 and the real floated, beginning its modern life as a high-yield commodity currency: soy, iron ore, sugar, coffee and oil flow out, and global risk appetite flows in. The real has traded through commodity supercycles, the 2015–16 recession and repeated political cycles, staying free-floating and deeply liquid throughout."),
        ("h", "What moves the BRL exchange rate"),
        ("p", "Brazil offers among the highest real interest rates in the world, and everything about the currency follows from that plus commodities."),
        ("li", "The Selic rate: Brazil's central bank (Copom) hikes hard against inflation, attracting carry flows that support the real"),
        ("li", "Commodities: soybeans, iron ore and crude oil are the big export earners — their prices lift or sink the currency"),
        ("li", "Risk appetite: as a classic carry currency, the real strengthens in calm markets and drops sharply in global panics"),
        ("li", "Fiscal credibility: budgets and elections move the real faster than in inflation-targeting veterans"),
        ("h", "The Real in practice"),
        ("p", "Brazil runs on PIX — the central bank's instant-payment system, launched in 2020, used by nearly the entire adult population for everything from beach vendors to rent. Foreign visitors can now pay some merchants via international cards linked to PIX-accepting wallets, and contactless cards work widely; cash still suits markets and smaller beach towns."),
        ("p", "For remittances into Brazil, costs are above emerging-market averages and the tax treatment of incoming money is strict, so comparing licensed services matters. For businesses, the real is the hedge for anyone buying Brazilian commodities — and one of the highest-yield currencies in any diversified portfolio."),
        ("h", "Popular Real conversions"),
        ("p", "USD/BRL is the reference pair and one of the most liquid emerging-market rates in the world. EUR/BRL serves European trade and travel, and BRL/JPY is a classic carry cross watched for its yield spread."),
    ],
    "faq": [
        ("Why is the Brazilian Real so volatile?",
         "High interest rates attract short-term global money, and Brazil's exports are commodity-priced. Both flows reverse quickly on global scares and domestic political news, so the real swings more than G7 currencies."),
        ("What was the Plano Real?",
         "The 1994 stabilization plan: a new currency (the real), fiscal reform and an initial peg. It ended decades of hyperinflation — annual inflation collapsed from roughly 2,500% to single digits within two years."),
        ("Can foreigners use PIX in Brazil?",
         "PIX is domestic, but it is opening up: major international cards and wallets can now be used at PIX-accepting merchants through partner apps. For most visitors, contactless cards plus some cash remains the simplest setup."),
    ],
}

# ─────────────────────────── SGD ───────────────────────────
CURRENCY_ARTICLES["SGD"] = {
    "sections": [
        ("h", "A short history of the Singapore Dollar"),
        ("p", "Singapore introduced the dollar in 1967, two years after independence, replacing the Malaya and British Borneo dollar. The new currency was initially interchangeable with the Malaysian ringgit, but that arrangement ended in 1973. Since then the Singapore dollar has grown with the city-state's transformation from trading port into a major financial, shipping and technology hub."),
        ("p", "Unlike most central banks, the Monetary Authority of Singapore (MAS) uses the exchange rate as its main monetary-policy tool. It manages the Singapore dollar against a trade-weighted basket within an undisclosed band, adjusting the band when inflation or growth conditions change. That framework has made the SGD one of Asia's most stable currencies."),
        ("h", "What moves the SGD exchange rate"),
        ("p", "Singapore is a small, exceptionally open economy, so the currency reflects both regional trade and global capital flows."),
        ("li", "MAS policy: the slope, width and center of the trade-weighted band matter more than a conventional overnight-rate target"),
        ("li", "Global trade: electronics, pharmaceuticals, shipping and finance make Singapore sensitive to the world business cycle"),
        ("li", "China and regional demand: mainland China and ASEAN are crucial trading partners, so Asian growth expectations feed into SGD"),
        ("li", "Inflation and imported costs: food, energy and housing costs matter greatly in an economy that imports most of what it consumes"),
        ("h", "The Singapore Dollar in practice"),
        ("p", "Singapore is one of the world's easiest places to pay by card or phone. Contactless cards, PayNow and QR payments are common, although small hawker stalls may still prefer cash or a local wallet. The currency is divided into 100 cents, and Malaysian ringgit may be accepted near the border, but the quoted rate is rarely as good as paying in SGD."),
        ("p", "For remittances, Singapore is a major regional hub for workers from Malaysia, Indonesia, the Philippines and India. Bank transfers are reliable, but specialist services can offer a materially better total received. Businesses use SGD as a relatively stable invoicing and treasury currency for Southeast Asian operations."),
        ("h", "Popular Singapore Dollar conversions"),
        ("p", "USD/SGD is the primary global reference pair and responds to both US rates and MAS settings. SGD/MYR is the natural cross-border pair for the tightly connected Singaporean and Malaysian economies. SGD/IDR and SGD/INR serve large worker and business corridors, while SGD/CNY tracks one of the region's most important trade relationships."),
    ],
    "faq": [
        ("How does Singapore manage the Singapore Dollar?",
         "MAS manages the SGD against a secret trade-weighted basket inside a policy band. It changes the band’s slope, width or center rather than relying mainly on a short-term interest-rate target."),
        ("Is the Singapore Dollar a safe currency?",
         "It is regarded as one of Asia's more stable currencies because Singapore has strong institutions, substantial reserves, low inflation historically and a credible exchange-rate framework. Stability does not mean the rate never moves."),
        ("Can I use Malaysian ringgit in Singapore?",
         "Some businesses near the Malaysian border accept ringgit, but acceptance is not universal and the exchange rate may include a large margin. Paying in SGD or using a card is normally better."),
    ],
}

# ─────────────────────────── HKD ───────────────────────────
CURRENCY_ARTICLES["HKD"] = {
    "sections": [
        ("h", "A short history of the Hong Kong Dollar"),
        ("p", "The Hong Kong dollar emerged in the nineteenth century as Hong Kong became a British trading port. It was linked at different times to silver, sterling and the US dollar before the modern linked exchange-rate system began in 1983. After the severe market pressure of the 1997 Asian financial crisis, the system was strengthened with clearer convertibility rules and a more formal currency-board discipline."),
        ("p", "Under the current system, the Hong Kong Monetary Authority keeps the currency within HK$7.75 to HK$7.85 per US dollar. When the rate reaches either side, the authority buys or sells Hong Kong dollars against its foreign reserves. The arrangement gives Hong Kong monetary stability while leaving local interest rates to move with US conditions."),
        ("h", "What moves the HKD exchange rate"),
        ("p", "The HKD is unusual because the exchange rate is largely engineered; market pressure appears more clearly in liquidity and interest-rate differences than in a large change in the peg."),
        ("li", "US Federal Reserve policy: Hong Kong rates generally follow US rates to protect the linked system"),
        ("li", "Capital flows: money moving into or out of Hong Kong changes banking liquidity and can push the rate toward a band boundary"),
        ("li", "Mainland China: trade, tourism, listings and policy links with the mainland affect the territory's economy and demand for HKD"),
        ("li", "Property and financial markets: Hong Kong's asset cycle can amplify liquidity conditions even when the exchange rate barely moves"),
        ("h", "The Hong Kong Dollar in practice"),
        ("p", "Hong Kong is highly card-friendly, and Octopus cards remain useful for transit, convenience stores and small purchases. Cash is still common at traditional restaurants and markets. Macau patacas may be accepted in Macau but are not a substitute for HKD in Hong Kong, and mainland yuan is accepted in some tourist businesses at an often-unfavorable rate."),
        ("p", "The HKD is important for cross-border trade, investment and remittances, especially between Hong Kong and mainland China. Transfers involving CNY may use separate onshore and offshore markets, so compare the final amount rather than assuming a quoted bank rate is the market rate."),
        ("h", "Popular Hong Kong Dollar conversions"),
        ("p", "USD/HKD is the defining pair and normally trades inside the 7.75–7.85 convertibility zone. HKD/CNY and HKD/CNH reflect Hong Kong's role as an offshore renminbi center. HKD/JPY and HKD/GBP are common travel and investment crosses, while HKD/SGD connects two major Asian financial hubs."),
    ],
    "faq": [
        ("Is the Hong Kong Dollar pegged to the US Dollar?",
         "Yes. The Linked Exchange Rate System keeps HKD within HK$7.75 to HK$7.85 per US dollar through automatic convertibility and the HKMA's currency-board operations."),
        ("Can the Hong Kong Dollar break its peg?",
         "A peg is a policy arrangement, not a law of nature, but Hong Kong holds substantial reserves and has defended the system through major crises. A change would require a major policy decision rather than an ordinary daily fluctuation."),
        ("Can I pay with yuan in Hong Kong?",
         "Some shops accept mainland yuan, especially in tourist areas, but acceptance and rates vary. HKD, a card or an Octopus card is usually the most predictable way to pay."),
    ],
}

# ─────────────────────────── NZD ───────────────────────────
CURRENCY_ARTICLES["NZD"] = {
    "sections": [
        ("h", "A short history of the New Zealand Dollar"),
        ("p", "New Zealand decimalized on 10 July 1967, replacing pounds, shillings and pence with the dollar. The country moved from a fixed exchange rate to a freely floating dollar in 1985, an early example of a modern inflation-targeting economy. The New Zealand dollar is often called the kiwi, after the native bird shown on the one-dollar coin."),
        ("p", "The NZD became a global market currency because New Zealand combines an independent central bank, liquid financial markets and a small economy exposed to agricultural prices. It is not a reserve currency on the scale of the dollar or euro, but it is widely traded and often used to express a view on Asia-Pacific growth and global risk appetite."),
        ("h", "What moves the NZD exchange rate"),
        ("p", "The kiwi is both a yield currency and a commodity currency, with domestic dairy prices especially important."),
        ("li", "Reserve Bank of New Zealand policy: rate expectations move NZD quickly because global investors compare New Zealand yields with those abroad"),
        ("li", "Dairy and agricultural exports: milk powder, meat, wool and wood products are major sources of foreign income"),
        ("li", "China and Australia: China is a major buyer of New Zealand goods, while Australia is its largest nearby economic partner"),
        ("li", "Risk sentiment: NZD usually benefits from confidence and falls when investors seek the dollar, yen or Swiss franc"),
        ("h", "The New Zealand Dollar in practice"),
        ("p", "Visitors can usually travel through New Zealand using contactless cards and mobile wallets. Cash remains useful for small markets, rural operators and occasional public-transport top-ups. Prices generally include GST, unlike in some other English-speaking countries, and tips are not routinely expected."),
        ("p", "New Zealand sends substantial export and education income abroad, while migrants and expatriates create steady remittance corridors. Banks are convenient but not always cheapest; check the exchange margin and fixed fee separately. Businesses exposed to dairy, tourism or imported fuel often manage NZD risk because its moves can be sharp."),
        ("h", "Popular New Zealand Dollar conversions"),
        ("p", "NZD/USD is the main reference pair and a proxy for the country’s rate outlook. NZD/AUD tracks the relative fortunes of two closely connected economies. NZD/JPY is a classic risk-sensitive cross, while NZD/CNY and NZD/SGD matter for Asia-Pacific trade and travel."),
    ],
    "faq": [
        ("Why is the New Zealand Dollar called the kiwi?",
         "Kiwi is the market nickname for NZD, taken from New Zealand's distinctive flightless bird. The bird appears on the one-dollar coin, although the currency's formal name is the New Zealand dollar."),
        ("Is NZD a commodity currency?",
         "Yes, in part. Dairy, meat, wood and other exports are important, so global food and agricultural prices influence income and the exchange rate. Interest rates and risk appetite can be just as important."),
        ("Do I need cash in New Zealand?",
         "Usually not much. Cards and contactless payments are accepted widely, but a little cash helps at small markets, remote businesses and places with unreliable connectivity."),
    ],
}

# ─────────────────────────── SEK ───────────────────────────
CURRENCY_ARTICLES["SEK"] = {
    "sections": [
        ("h", "A short history of the Swedish Krona"),
        ("p", "Sweden created the krona in 1873 as part of the Scandinavian Monetary Union with Denmark and Norway. The union shared a gold standard but allowed each country to issue its own notes and coins. It ended after the First World War, yet the krona name survived. Sweden eventually abandoned its fixed exchange-rate policy during the 1992 European currency crisis and has allowed the krona to float ever since."),
        ("p", "The Riksbank, founded in 1668, is one of the world's oldest central banks. Sweden has not adopted the euro, despite being an EU member, so the SEK remains a liquid regional currency whose value reflects both Nordic fundamentals and global appetite for risk."),
        ("h", "What moves the SEK exchange rate"),
        ("p", "The krona is sensitive to interest rates, European growth and investors' willingness to hold smaller currencies."),
        ("li", "Riksbank policy and Swedish inflation: changing expectations for the policy rate are quickly reflected in SEK"),
        ("li", "European demand: Germany and the wider EU are important trading partners for Swedish manufacturers"),
        ("li", "Global risk: the krona often weakens when investors retreat into larger reserve currencies"),
        ("li", "Industrial and housing cycles: Sweden's export sector and highly leveraged households make domestic data relevant to the rate"),
        ("h", "The Swedish Krona in practice"),
        ("p", "Sweden is close to cashless. Cards, contactless payments and the Swish mobile system are normal, while some businesses no longer accept notes or coins. Visitors should keep a card with a PIN and a backup payment method; cash machines exist but are less useful than in many countries. Prices include VAT, and tipping is discretionary rather than compulsory."),
        ("p", "For Nordic businesses, SEK exposure can matter even when the contract is in euros, because supplier costs and wages may be denominated in kronor. Remittance providers serve Swedish residents sending money abroad, but a low advertised fee can conceal a wide exchange spread."),
        ("h", "Popular Swedish Krona conversions"),
        ("p", "EUR/SEK is the key pair for Swedish trade and monetary-policy expectations. USD/SEK reflects global dollar and risk cycles, NOK/SEK compares two closely linked Scandinavian economies, and GBP/SEK is common for travel and services trade."),
    ],
    "faq": [
        ("Does Sweden use the euro?",
         "No. Sweden is an EU member but currently uses the Swedish krona and has no active timetable for joining the euro. Some tourist businesses may quote euros, but SEK is the local currency."),
        ("Can I pay cash in Sweden?",
         "Cash is legal tender but not accepted everywhere. Cards and mobile payments are much more practical, so visitors should arrange a reliable card rather than depending on banknotes."),
        ("Why is SEK sometimes volatile?",
         "Sweden is a small open economy with a floating currency. Global risk, European industrial demand, domestic housing conditions and Riksbank expectations can all move SEK at once."),
    ],
}

# ─────────────────────────── NOK ───────────────────────────
CURRENCY_ARTICLES["NOK"] = {
    "sections": [
        ("h", "A short history of the Norwegian Krone"),
        ("p", "Norway introduced the krone in 1875 when it joined the Scandinavian Monetary Union with Sweden and Denmark. The monetary union ended after the First World War, but Norway retained the currency name. The krone moved through several fixed and managed arrangements before Norway adopted a floating exchange rate in 1992."),
        ("p", "The modern NOK story is inseparable from petroleum. North Sea oil turned Norway into a wealthy exporter, but the country placed much of that income in its sovereign wealth fund rather than spending it all at home. The arrangement cushions the economy, yet the krone still reacts to oil prices, European growth and global risk."),
        ("h", "What moves the NOK exchange rate"),
        ("p", "NOK is a small, liquid currency with unusually clear links to energy and European conditions."),
        ("li", "Oil and gas prices: export revenue and Norway's terms of trade generally improve when energy prices rise"),
        ("li", "Norges Bank policy: rate expectations affect the yield available on NOK assets and the currency's carry appeal"),
        ("li", "European growth: the EU is Norway's main trading area, so manufacturing and energy demand abroad matter"),
        ("li", "Risk appetite and market liquidity: NOK can weaken during global stress even when Norway's public finances remain strong"),
        ("h", "The Norwegian Krone in practice"),
        ("p", "Norway is highly card-oriented. Contactless payments are accepted almost everywhere, and Vipps is a major domestic mobile-payment service. Cash is useful for a few small operators but is no longer the default. Travelers should choose NOK rather than accepting a foreign-currency conversion at a terminal, and remember that Norway is outside the euro area."),
        ("p", "For businesses, the krone creates a natural currency exposure for energy, seafood, shipping and tourism. Remittance services are reliable, but compare the rate as well as the fee. Norway's high cost of living means even a small exchange-rate margin can make a noticeable difference on rent, wages or travel spending."),
        ("h", "Popular Norwegian Krone conversions"),
        ("p", "EUR/NOK is the principal trade and travel pair, while USD/NOK combines energy prices with the global dollar cycle. NOK/SEK compares the two Scandinavian neighbors, and GBP/NOK is useful for UK–Norway energy and tourism flows."),
    ],
    "faq": [
        ("Does Norway use the euro?",
         "No. Norway is not an EU member and uses the Norwegian krone. Euros may be accepted in a few tourist locations, but the rate is usually better when paying in NOK."),
        ("Why does NOK follow oil prices?",
         "Oil and gas are major Norwegian exports, so energy prices affect export income and the country's terms of trade. The relationship is not one-for-one because interest rates, fund flows and global risk also matter."),
        ("Is Norway's currency stable because of its oil fund?",
         "The sovereign wealth fund and strong public finances provide a major buffer, but NOK still floats and can move substantially. Fiscal strength reduces some risks; it does not eliminate market volatility."),
    ],
}

# ─────────────────────────── DKK ───────────────────────────
CURRENCY_ARTICLES["DKK"] = {
    "sections": [
        ("h", "A short history of the Danish Krone"),
        ("p", "Denmark introduced the krone in 1875 as part of the Scandinavian Monetary Union, replacing the rigsdaler. The union's shared gold standard ended during the First World War, but Denmark kept the krone. After several exchange-rate regimes, Denmark chose to keep its currency closely tied to the European monetary system rather than adopt the euro."),
        ("p", "Today the krone participates in ERM II with a central rate of DKK 7.46038 per euro and a formal fluctuation band of 2.25% on either side. Danmarks Nationalbank normally keeps the actual movement much narrower through interest-rate adjustments and foreign-exchange intervention. Denmark has a treaty opt-out from the euro."),
        ("h", "What moves the DKK exchange rate"),
        ("p", "The krone is a managed European currency, so its main story is the defense of the euro peg rather than a free market view on Denmark."),
        ("li", "ECB policy: Danish rates are set with the euro relationship in mind, often tracking the ECB with a small spread"),
        ("li", "Danmarks Nationalbank operations: intervention and certificates of deposit rates keep DKK close to its central rate"),
        ("li", "Danish inflation and wages: domestic pressures influence how much tightening is needed to preserve the peg"),
        ("li", "European trade: Germany and the EU are central to Denmark's exports, shipping and supply chains"),
        ("h", "The Danish Krone in practice"),
        ("p", "Denmark is almost cashless in everyday life. Cards, contactless payments and MobilePay are widely accepted, although cash remains legal and useful in a few small businesses. Denmark is in the EU but not the euro area, so travelers should check whether a terminal is charging DKK or offering an expensive home-currency conversion."),
        ("p", "Because the krone is closely tied to the euro, DKK conversion costs are often modest for euro-area transfers. The exchange margin can still matter for salaries, invoices and large property payments. Businesses with Danish revenue but euro costs have less currency uncertainty than they would with a freely floating Nordic currency."),
        ("h", "Popular Danish Krone conversions"),
        ("p", "EUR/DKK is the anchor pair and normally stays close to 7.46. USD/DKK reflects the dollar's movement against the euro, while SEK/DKK and NOK/DKK are useful for Nordic trade and travel. GBP/DKK is common in shipping, tourism and services transactions."),
    ],
    "faq": [
        ("Is the Danish Krone pegged to the euro?",
         "Yes. Denmark participates in ERM II with a central rate of 7.46038 kroner per euro and a narrow practical trading range maintained by Danmarks Nationalbank."),
        ("Why does Denmark not use the euro?",
         "A referendum in 2000 rejected euro adoption, and Denmark has a formal opt-out. The country keeps monetary independence in name while maintaining a very close exchange-rate link to the euro."),
        ("Do I need Danish cash?",
         "Usually not. Cards and mobile payments are accepted almost everywhere, but a small amount of kroner is sensible for markets, donations or a business that does not accept cards."),
    ],
}

# ─────────────────────────── PLN ───────────────────────────
CURRENCY_ARTICLES["PLN"] = {
    "sections": [
        ("h", "A short history of the Polish Zloty"),
        ("p", "The zloty means golden and has been used in Polish monetary history for centuries. The modern zloty was introduced after the Second World War and underwent a major redenomination in 1995: 10,000 old zlotys became one new zloty. Poland gradually moved from a managed rate to a freely floating currency around the turn of the millennium."),
        ("p", "Poland joined the European Union in 2004 but has not adopted the euro. Its large domestic economy, growing manufacturing base and deepening financial markets make PLN the most traded currency in Central Europe. The floating rate gives Poland a shock absorber when demand, energy prices or regional risk change."),
        ("h", "What moves the PLN exchange rate"),
        ("p", "The zloty responds to both Polish fundamentals and the broader mood toward emerging Europe."),
        ("li", "National Bank of Poland policy: interest-rate expectations and inflation reports are central to PLN pricing"),
        ("li", "German and EU demand: Poland is deeply integrated into European manufacturing and supply chains"),
        ("li", "Energy and trade balances: imported fuel costs can weigh on PLN, while exports and EU investment support it"),
        ("li", "Regional risk: wars, elections and shifts in global risk appetite can move Central European currencies together"),
        ("h", "The Polish Zloty in practice"),
        ("p", "Poland is convenient for visitors: cards and contactless payments are widespread, while cash in zlotys remains useful at markets, small towns and some transit machines. Poland uses the zloty, not the euro, even though euros may be quoted in tourist areas. Dynamic currency conversion at a terminal or ATM is normally more expensive than letting the card issuer convert."),
        ("p", "The country is a major destination for workers and a growing source of cross-border business payments. For remittances, compare the total PLN received because bank fees, intermediary charges and the exchange spread can all apply. Companies importing from the euro area often hedge PLN because a relatively small rate move can change margins."),
        ("h", "Popular Polish Zloty conversions"),
        ("p", "EUR/PLN is the key pair for Polish trade and European investment. USD/PLN reflects global dollar and risk cycles, while GBP/PLN supports UK–Poland worker and business corridors. CZK/PLN and HUF/PLN are useful Central European crosses."),
    ],
    "faq": [
        ("Will Poland adopt the euro?",
         "Poland is committed in principle as an EU member, but it has no announced adoption date. Joining requires meeting economic and legal criteria and a domestic political decision."),
        ("Why was the zloty redenominated?",
         "In 1995 Poland removed four zeros to make prices and accounting practical after decades of inflation. Ten thousand old zlotys became one new zloty; it was a change of units, not an overnight increase in purchasing power."),
        ("Can I pay with euros in Poland?",
         "Some hotels and tourist businesses accept euros, but coverage and rates vary. Paying in PLN with a card is usually more predictable, especially outside major tourist centers."),
    ],
}

# ─────────────────────────── ZAR ───────────────────────────
CURRENCY_ARTICLES["ZAR"] = {
    "sections": [
        ("h", "A short history of the South African Rand"),
        ("p", "South Africa introduced the rand in 1961 when it became a republic and left the sterling area. The name comes from the Witwatersrand, the gold-bearing ridge on which Johannesburg was built. The rand replaced the South African pound at two rand to one pound and has since developed into the most actively traded currency in Africa."),
        ("p", "The rand has been floating since the 1980s, with periods of controls and managed intervention. Its market history reflects apartheid-era sanctions, the democratic transition of 1994, commodity booms and domestic electricity and fiscal pressures. It is a sophisticated but high-volatility emerging-market currency."),
        ("h", "What moves the ZAR exchange rate"),
        ("p", "ZAR is unusually sensitive to the global risk cycle because South Africa is an open emerging market with a large, liquid financial market."),
        ("li", "Commodities: platinum, gold, coal, iron ore and other mineral exports affect the trade balance and foreign income"),
        ("li", "South African Reserve Bank policy: inflation and real yields influence global demand for rand assets"),
        ("li", "Electricity and infrastructure: power shortages, logistics constraints and reform progress affect growth expectations"),
        ("li", "Global risk appetite: investors often sell rand assets in a crisis, regardless of South Africa's local data"),
        ("h", "The South African Rand in practice"),
        ("p", "Cards are accepted widely in South African cities, malls and hotels, but cash remains useful for markets, tips, minibus taxis and smaller businesses. ATMs are common; use a bank-owned machine, protect your PIN and decline dynamic currency conversion when offered. Prices are in rand and tipping is customary in restaurants and for many services."),
        ("p", "The rand is central to regional commerce, with South Africa serving as a financial and trading hub for neighboring economies. Remittance costs differ sharply by corridor. Travelers and businesses should allow for volatility: a rate that looks favorable can change quickly after commodity data, political news or a global risk shock."),
        ("h", "Popular South African Rand conversions"),
        ("p", "USD/ZAR is the main global reference pair and a barometer of emerging-market risk. EUR/ZAR and GBP/ZAR serve important trade and diaspora corridors, while ZAR/JPY is a classic risk-sensitive cross. ZAR/NAD links the rand with Namibia's currency, which is pegged one-for-one to it."),
    ],
    "faq": [
        ("Why is the rand so volatile?",
         "South Africa combines a floating currency, commodity exposure, domestic infrastructure and fiscal concerns, and a large market for international investors. Global risk-off episodes can therefore produce large ZAR moves."),
        ("Is the rand linked to gold?",
         "Gold is an important export and a historical part of the rand's identity, but the modern rate is driven by the whole commodity basket, interest rates, capital flows and risk sentiment rather than gold alone."),
        ("Should I carry cash in South Africa?",
         "Yes, a modest amount is useful for tips, markets and smaller operators, although cards work widely in formal businesses. Use sensible security precautions and avoid carrying more cash than needed."),
    ],
}

# ─────────────────────────── RUB ───────────────────────────
CURRENCY_ARTICLES["RUB"] = {
    "sections": [
        ("h", "A short history of the Russian Ruble"),
        ("p", "The ruble is one of Europe's oldest currency names, with roots in medieval Rus and a modern decimal system established under Peter the Great in the early eighteenth century. The post-Soviet ruble replaced the Soviet currency in 1993, and Russia redenominated it in 1998 at 1,000 old rubles to one new ruble after the financial crisis."),
        ("p", "The ruble was gradually made more market-based through the 2000s, but the 2014 sanctions and the 2022 invasion of Ukraine brought capital controls, restricted trading and major changes in payment channels. As a result, a published RUB quote may not represent a freely accessible rate for every person or transaction."),
        ("h", "What moves the RUB exchange rate"),
        ("p", "Ruble pricing now reflects policy controls and sanctions as much as ordinary market economics."),
        ("li", "Energy exports: oil and gas receipts are important sources of foreign currency, though sanctions and price restrictions alter the flows"),
        ("li", "Central Bank of Russia policy: interest rates and capital controls influence demand for rubles and foreign currency"),
        ("li", "Trade and settlement rules: export-revenue requirements, import demand and the shift toward yuan settlement affect liquidity"),
        ("li", "Geopolitical restrictions: sanctions, blocked reserves and limited access to international finance can cause large discontinuities"),
        ("h", "The Russian Ruble in practice"),
        ("p", "Travel and transfers involving RUB require more planning than for a freely convertible major currency. International cards issued outside Russia may not work there, and cards issued by Russian banks may not work abroad. Access to cash or bank transfers depends on the corridor and current regulations. Check official guidance and use licensed providers; do not assume that an online quote can be executed."),
        ("p", "Within Russia, domestic bank cards and instant-transfer systems are widely used, while cash rubles remain familiar. For businesses, invoices may be settled in rubles or another currency under applicable law, but sanctions screening, correspondent-bank availability and compliance checks can determine whether a payment is possible."),
        ("h", "Popular Russian Ruble conversions"),
        ("p", "USD/RUB and EUR/RUB are traditional reference pairs, although access and liquidity vary by venue. CNY/RUB has become more important as trade and settlement shift toward China. RUB/KZT and RUB/TRY are relevant regional crosses, but their practical rate depends heavily on the payment route."),
    ],
    "faq": [
        ("Is the Russian Ruble freely convertible?",
         "Not in the practical sense it was before the major sanctions and capital controls. Convertibility, settlement and access depend on residency, the banks involved, current rules and the specific corridor."),
        ("Why can RUB rates differ so much between sources?",
         "Sanctions, capital controls, thin offshore liquidity, different trading venues and transfer restrictions can separate an indicative market quote from the rate a person can actually obtain."),
        ("Can foreign cards be used in Russia?",
         "Many foreign-issued cards and payment networks have limited or no functionality there. Check current official travel and banking guidance before relying on a card, cash withdrawal or transfer route."),
    ],
}

# ─────────────────────────── KRW ───────────────────────────
CURRENCY_ARTICLES["KRW"] = {
    "sections": [
        ("h", "A short history of the South Korean Won"),
        ("p", "South Korea adopted the won after liberation in 1945, replacing the yen-based currency used during the colonial period. A new won was introduced in 1962 after a redenomination, and the currency moved through fixed and managed regimes before becoming substantially more flexible after the Asian financial crisis of 1997–98."),
        ("p", "The modern won reflects South Korea's transformation from an aid-dependent economy into a major exporter of semiconductors, cars, ships, batteries and entertainment. It is not fully free of official influence: the Bank of Korea and authorities monitor disorderly moves, especially when trade, security or global funding conditions deteriorate."),
        ("h", "What moves the KRW exchange rate"),
        ("p", "KRW is an export and technology currency with strong links to the global manufacturing cycle."),
        ("li", "Semiconductors and electronics: chip prices and the technology investment cycle are crucial for export receipts"),
        ("li", "China and the United States: both are major trade and supply-chain partners, so their growth and policy affect KRW"),
        ("li", "Bank of Korea and Federal Reserve policy: the interest-rate gap influences portfolio flows and the cost of imported funding"),
        ("li", "Risk and geopolitics: global shocks and tensions on the Korean peninsula can prompt rapid moves into the dollar"),
        ("h", "The South Korean Won in practice"),
        ("p", "South Korea is highly digital for daily payments. Cards and mobile wallets work in cities, transit cards handle public transport, and cash is still useful at markets, small restaurants and some rural businesses. ATMs may charge foreign-card fees or impose local limits, so travelers should keep a backup payment method."),
        ("p", "For remittances, Korea is home to many foreign workers and students, and licensed banks and specialist providers serve corridors across Asia. Compare the amount received in the destination currency. Korean companies often hedge KRW because export prices may be in dollars while wages and operating costs are in won."),
        ("h", "Popular South Korean Won conversions"),
        ("p", "USD/KRW is the main reference pair and a closely watched Asian risk indicator. JPY/KRW reflects the competitive relationship between Japan and Korea, while CNY/KRW tracks trade with China. EUR/KRW and SGD/KRW are common for European and regional business flows."),
    ],
    "faq": [
        ("Why is the won sensitive to chip prices?",
         "Semiconductors are a major Korean export, so chip demand and prices affect the country's trade income, corporate profits and foreign-investor flows. The won can respond before the data appears in the trade figures."),
        ("Is the South Korean Won freely floating?",
         "It is market-determined but not ignored by authorities. The Bank of Korea and government can respond to disorderly moves, liquidity stress or exceptional volatility, so KRW is best described as a managed or monitored float."),
        ("Do I need cash in South Korea?",
         "Cards and mobile payments are excellent in cities, but cash remains useful at markets, smaller restaurants and a few transit or vending situations. Keep some won and a backup card."),
    ],
}

# ─────────────────────────── AED ───────────────────────────
CURRENCY_ARTICLES["AED"] = {
    "sections": [
        ("h", "A short history of the UAE Dirham"),
        ("p", "The United Arab Emirates introduced the dirham in 1973, shortly after the federation was formed, replacing the Qatar and Dubai riyal and the Abu Dhabi dinar. The currency's name recalls the ancient Greek drachma and is shared with several currencies in the region. The UAE later established the modern central-bank framework that supports its exchange-rate policy."),
        ("p", "The dirham has been fixed at AED 3.6725 per US dollar since 1980s-era policy arrangements. The Central Bank of the UAE maintains the peg with reserves and domestic liquidity tools. Because the UAE earns much of its foreign income in dollars or dollar-linked energy markets, the peg gives importers, expats and global businesses predictable pricing."),
        ("h", "What moves the AED exchange rate"),
        ("p", "The AED/USD rate itself is intentionally stable, but the dirham's wider purchasing power and financial conditions still change."),
        ("li", "US Federal Reserve policy: UAE rates generally follow US rates to protect the dollar peg"),
        ("li", "Oil and gas income: energy revenue supports fiscal capacity and the country's external balance, even as the economy diversifies"),
        ("li", "Trade, property and tourism: Dubai and Abu Dhabi attract global capital, making flows and real-estate cycles important"),
        ("li", "Imported inflation: because many goods are imported, global prices and the dollar's strength affect local costs"),
        ("h", "The UAE Dirham in practice"),
        ("p", "The UAE is highly card-friendly in malls, hotels, taxis and restaurants, while cash is still useful at souks, small shops and for tips. ATMs are common. The dirham is the official currency; US dollars may be accepted in tourist settings, but the exchange rate is usually less favorable than paying in AED."),
        ("p", "The UAE is a major remittance hub for workers from India, Pakistan, the Philippines, Bangladesh and elsewhere. The fixed dollar rate makes the currency leg predictable, but providers still compete on fees and destination-currency spreads. Compare the final amount received rather than only the advertised transfer fee."),
        ("h", "Popular UAE Dirham conversions"),
        ("p", "USD/AED is effectively fixed at about 3.6725. AED/INR and AED/PKR are among the most important worker-remittance corridors, while AED/PHP and AED/BDT connect the Gulf with large expatriate communities. EUR/AED and GBP/AED are widely used for tourism and property transactions."),
    ],
    "faq": [
        ("Is the UAE Dirham pegged to the dollar?",
         "Yes. The official rate is about AED 3.6725 for one US dollar, and the Central Bank of the UAE supports the peg through reserves and monetary operations."),
        ("Why do AED interest rates follow the Fed?",
         "A fixed exchange rate is easier to defend when domestic money-market conditions broadly match those in the United States. The UAE therefore generally adjusts policy rates alongside the Federal Reserve."),
        ("Is the UAE Dirham the same as the Saudi Riyal?",
         "No. They are separate currencies with separate pegs, although both are closely linked to the US dollar. Their exchange rate against each other is therefore usually stable but not identical."),
    ],
}

# ─────────────────────────── SAR ───────────────────────────
CURRENCY_ARTICLES["SAR"] = {
    "sections": [
        ("h", "A short history of the Saudi Riyal"),
        ("p", "Saudi Arabia established a national monetary authority in 1952 and introduced the modern Saudi riyal in 1961, replacing earlier silver riyal and foreign-coin arrangements. The currency developed alongside the kingdom's oil industry, which made Saudi Arabia a central energy exporter and gave the riyal a strong external anchor."),
        ("p", "The riyal has been fixed at SAR 3.75 per US dollar since 1986. The Saudi Central Bank, known as SAMA, maintains the peg with foreign reserves, interest-rate tools and regulation of the banking system. The stable rate simplifies oil contracts, imports and remittances, although domestic inflation and purchasing power can still change."),
        ("h", "What moves the SAR exchange rate"),
        ("p", "The dollar rate is deliberately steady; the meaningful questions concern Saudi growth, liquidity and the purchasing power of a dollar-linked currency."),
        ("li", "US Federal Reserve policy: Saudi rates generally follow US rates to preserve the peg"),
        ("li", "Oil revenue: crude exports fund public spending, the external balance and a large share of foreign-currency earnings"),
        ("li", "Vision 2030 investment: diversification, tourism and infrastructure spending are changing the economy's non-oil demand"),
        ("li", "Imports and remittances: food, machinery, construction materials and worker transfers affect domestic liquidity and inflation"),
        ("h", "The Saudi Riyal in practice"),
        ("p", "Cards and contactless payments are now common in Saudi cities, and mobile wallets are growing quickly. Cash remains useful for small vendors, markets and tips. Visitors should use SAR when a terminal asks whether to convert to their home currency; dynamic conversion commonly adds a margin. The official currency is the riyal, even when prices are discussed in dollars for large contracts."),
        ("p", "Saudi Arabia is a major destination for expatriate workers, making SAR remittances important across South and Southeast Asia. The dollar peg removes one layer of uncertainty, but fees and destination-currency rates still vary widely. Licensed exchange houses, banks and digital services should be compared by the amount received."),
        ("h", "Popular Saudi Riyal conversions"),
        ("p", "USD/SAR is fixed at about 3.75. SAR/INR, SAR/PKR, SAR/BDT and SAR/PHP are major remittance pairs, while EUR/SAR and GBP/SAR serve tourism, trade and investment. SAR/AED is a stable Gulf cross because both currencies are pegged to the dollar."),
    ],
    "faq": [
        ("Is the Saudi Riyal pegged to the US Dollar?",
         "Yes. The Saudi Central Bank maintains a long-standing rate of roughly SAR 3.75 per US dollar. Ordinary market trading does not normally move that rate materially."),
        ("Does the oil price change SAR immediately?",
         "Not usually through the exchange rate, because the peg is fixed. Oil prices do affect government revenue, fiscal policy, growth, reserves and domestic liquidity, so they matter to the economy even when USD/SAR stays unchanged."),
        ("What is SAMA?",
         "SAMA is the former name of the Saudi Central Bank, the institution responsible for monetary and banking policy, reserves and supporting the riyal's exchange-rate stability."),
    ],
}

# ─────────────────────────── THB ───────────────────────────
CURRENCY_ARTICLES["THB"] = {
    "sections": [
        ("h", "A short history of the Thai Baht"),
        ("p", "The baht began as a unit of weight for silver and later became Thailand's modern currency. The country standardized its monetary system in the nineteenth and early twentieth centuries, and the Bank of Thailand was established in 1942. Thailand moved through dollar-linked arrangements before adopting a managed float after the 1997 Asian financial crisis."),
        ("p", "The 1997 crisis began with pressure on the baht's former peg and spread across Asia. Since then, the currency has been market-determined but monitored by the central bank. Tourism, manufacturing and agriculture give THB a broad economic base, while political events and capital flows can still produce sharp moves."),
        ("h", "What moves the THB exchange rate"),
        ("p", "The baht balances tourism income, Asian trade and domestic monetary policy."),
        ("li", "Tourism: visitor receipts supply foreign currency and are vital to Thailand's external balance"),
        ("li", "Exports and China: electronics, automobiles, agriculture and trade with China connect THB to regional manufacturing"),
        ("li", "Bank of Thailand policy: rate expectations and measures on capital flows affect the currency"),
        ("li", "Political and global risk: domestic uncertainty and shifts into safe-haven currencies can weaken THB"),
        ("h", "The Thai Baht in practice"),
        ("p", "Thailand remains a cash-heavy travel destination even as cards and QR payments spread. Cards work in hotels, malls and larger restaurants, while cash is important for street food, markets, taxis and small islands. ATMs are plentiful but often charge a fixed foreign-card fee. The baht is divided into 100 satang, though satang coins are rarely used in everyday prices."),
        ("p", "For remittances, Thailand has large corridors with neighboring countries and overseas workers. Compare fees, exchange spreads and cash-pickup terms. Travelers should avoid exchanging large amounts at airports when possible, and businesses exposed to tourism or imported fuel may hedge THB around high-season demand."),
        ("h", "Popular Thai Baht conversions"),
        ("p", "USD/THB is the main reference pair and reacts to US rates, tourism and regional risk. CNY/THB reflects close trade with China, while JPY/THB is important for Japanese investment and visitors. EUR/THB and GBP/THB are common travel and tourism pairs."),
    ],
    "faq": [
        ("Why is tourism important to the Thai Baht?",
         "Visitors bring foreign currency and create demand for Thai goods and services. A tourism rebound improves the external balance, while a major travel slowdown can remove an important source of foreign income."),
        ("Is the Thai Baht pegged to the dollar?",
         "No. Thailand has used a managed float since the 1997 crisis. The rate is market-determined, but the Bank of Thailand can respond to excessive volatility or disorderly flows."),
        ("Should I use cash in Thailand?",
         "Yes, especially for street food, markets, taxis and smaller businesses. Cards and QR payments are excellent in formal businesses, but carry baht and use reputable ATMs for cash needs."),
    ],
}

# ─────────────────────────── MYR ───────────────────────────
CURRENCY_ARTICLES["MYR"] = {
    "sections": [
        ("h", "A short history of the Malaysian Ringgit"),
        ("p", "Malaysia introduced the Malaysian dollar in 1967, replacing the shared currency used by Malaya, Singapore and Borneo. After Singapore left the currency interchangeability arrangement in 1973, Malaysia continued with its own dollar and adopted the name ringgit in 1993. The word means jagged, referring to the Spanish silver dollars that circulated in the region."),
        ("p", "During the 1997–98 Asian financial crisis, Malaysia fixed the ringgit at RM3.80 per US dollar and imposed capital controls. The peg was removed in 2005, and MYR has since operated as a managed float. Malaysia's diversified exports — electronics, palm oil, petroleum, chemicals and manufactured goods — give the currency several competing drivers."),
        ("h", "What moves the MYR exchange rate"),
        ("p", "The ringgit is closely connected to Asian trade and to the prices of the commodities Malaysia exports."),
        ("li", "China and regional manufacturing: electronics supply chains and Chinese demand are major influences on trade income"),
        ("li", "Oil, gas and palm oil: commodity prices affect export receipts, government revenue and the current account"),
        ("li", "Bank Negara Malaysia policy: interest rates and measures affecting capital flows shape the yield appeal of MYR"),
        ("li", "US dollar strength: global funds and imported costs can move MYR even when Malaysian data is steady"),
        ("h", "The Malaysian Ringgit in practice"),
        ("p", "Malaysia is easy to navigate with cards in cities, malls and hotels, while cash remains useful at hawker stalls, markets and smaller towns. DuitNow QR and local wallets are common for residents. Visitors should pay in ringgit when offered a choice, because a shop's dollar or euro conversion usually includes a margin."),
        ("p", "The Singapore–Malaysia corridor is especially important for commuting, trade and family transfers, with additional remittance links to Indonesia, Bangladesh and the Philippines. Compare both fees and the rate. Businesses often invoice in dollars but pay Malaysian wages and suppliers in MYR, creating a natural need for hedging."),
        ("h", "Popular Malaysian Ringgit conversions"),
        ("p", "USD/MYR is the main reference pair, sensitive to the dollar, China and commodity cycles. SGD/MYR is the most visible regional cross because of close trade and daily border traffic. MYR/IDR and MYR/THB connect neighboring economies, while EUR/MYR supports European business and travel."),
    ],
    "faq": [
        ("Is the Malaysian Ringgit freely floating?",
         "MYR is market-determined within a managed framework. Bank Negara Malaysia monitors liquidity and disorderly conditions, and the currency is subject to rules that can affect offshore access and settlement."),
        ("What was the 1998 ringgit peg?",
         "Malaysia fixed the ringgit at RM3.80 per US dollar during the Asian financial crisis and used capital controls to stabilize the economy. The peg was removed in 2005, returning MYR to a managed float."),
        ("Is ringgit accepted in Singapore?",
         "Some businesses near the border may accept it, but this is not universal and the rate can be poor. Use SGD in Singapore and MYR in Malaysia whenever possible."),
    ],
}

# ─────────────────────────── IDR ───────────────────────────
CURRENCY_ARTICLES["IDR"] = {
    "sections": [
        ("h", "A short history of the Indonesian Rupiah"),
        ("p", "Indonesia introduced the rupiah in 1946, shortly after declaring independence, to replace a mixture of Japanese occupation money and Netherlands Indies currency. The currency went through several inflationary episodes and a major 1965 redenomination, when 1,000 old rupiah became one new rupiah. Large denominations remain a normal feature of everyday prices."),
        ("p", "The rupiah was heavily managed before the Asian financial crisis. After the 1997–98 collapse, Indonesia moved to a more flexible exchange rate and granted Bank Indonesia greater central-bank independence. Today IDR is still monitored closely because imported food, fuel and dollar debt make exchange-rate stability important to households and companies."),
        ("h", "What moves the IDR exchange rate"),
        ("p", "Indonesia's huge domestic market gives IDR resilience, but commodities and global funding remain powerful influences."),
        ("li", "Coal, palm oil, nickel and other commodities: export prices affect foreign-exchange earnings and the current account"),
        ("li", "US rates and global risk: higher dollar yields can pull capital away from Indonesian bonds and equities"),
        ("li", "Bank Indonesia policy: rate decisions and market operations aim to balance inflation, growth and rupiah stability"),
        ("li", "Imports and domestic demand: energy, food and machinery costs can increase pressure on the currency"),
        ("h", "The Indonesian Rupiah in practice"),
        ("p", "Indonesia is a mix of cash and digital payments. Cards work at hotels, malls and many urban businesses, while cash is essential at markets, small warungs and in much of the country outside major centers. QRIS, the national QR-payment standard, has made digital payments much easier for residents and visitors using supported services. Count notes carefully because denominations are large."),
        ("p", "Indonesia is a major destination for tourism, labor and investment, and remittance routes connect it with Malaysia, Singapore, Saudi Arabia and other countries. Compare the amount received rather than focusing only on a zero-fee label. Travelers should use licensed money changers and avoid unofficial exchange offers."),
        ("h", "Popular Indonesian Rupiah conversions"),
        ("p", "USD/IDR is the main reference pair and a broad gauge of emerging-market risk. SGD/IDR is important for the regional business and worker corridor, while MYR/IDR and AUD/IDR reflect nearby trade and commodity links. EUR/IDR and SAR/IDR serve travel and remittance flows."),
    ],
    "faq": [
        ("Why are Indonesian prices shown in such large numbers?",
         "The rupiah's historical inflation and the 1965 redenomination left the currency with large denominations. One thousand old rupiah became one new rupiah in 1965, but the unit was not repeatedly re-denominated afterward."),
        ("Is IDR a freely floating currency?",
         "The rate is market-determined but Bank Indonesia actively manages liquidity and volatility. Capital flows, commodity prices and imported costs can therefore produce intervention as well as ordinary market moves."),
        ("Should I exchange money before visiting Indonesia?",
         "Bring a reliable card and exchange or withdraw rupiah through reputable providers after arrival. Airport desks and unofficial street offers often have wider margins; cash is still important outside major tourist businesses."),
    ],
}

# ─────────────────────────── PHP ───────────────────────────
CURRENCY_ARTICLES["PHP"] = {
    "sections": [
        ("h", "A short history of the Philippine Peso"),
        ("p", "The Philippine peso inherited its name from the Spanish silver peso that circulated through the archipelago and the wider Pacific trade. The modern republic established the currency after independence in 1946, and the Central Bank of the Philippines began operations in 1949. The peso has moved from fixed and tightly managed arrangements toward a market-determined rate, with the central bank smoothing disorderly conditions."),
        ("p", "The Philippines' currency story is shaped by overseas workers and services as much as by goods trade. Remittances, business-process outsourcing, tourism and electronics exports bring in foreign currency, while imported fuel and food create regular demand for dollars. That mix can make PHP resilient in some shocks and vulnerable in others."),
        ("h", "What moves the PHP exchange rate"),
        ("p", "The peso is a liquid regional currency whose main drivers are external income, imports and US monetary policy."),
        ("li", "Remittances: millions of overseas Filipino workers send a steady flow of dollars and other currencies home"),
        ("li", "US rates and the dollar: Philippine borrowers and investors respond to the cost and availability of dollar funding"),
        ("li", "Imports and energy: the country imports much of its fuel, so oil prices can widen the trade deficit and pressure PHP"),
        ("li", "BPO, tourism and electronics: services exports and semiconductor shipments provide important foreign-exchange earnings"),
        ("h", "The Philippine Peso in practice"),
        ("p", "Cards and mobile wallets are common in Manila and other cities, but cash remains essential for jeepneys, markets, small islands and many neighborhood stores. GCash and other electronic wallets are widely used domestically, though visitors may not be able to register without a local number or identity documents. Keep smaller peso notes for transport and tips."),
        ("p", "The Philippines is one of the world's largest remittance markets, so consumers have many transfer options. Compare the total PHP received, including the exchange spread, cash-pickup fee and any local charge. Businesses receiving dollars and paying local wages may also use forward contracts to manage the peso value of their income."),
        ("h", "Popular Philippine Peso conversions"),
        ("p", "USD/PHP is the principal reference pair and reflects the dollar, remittances and imported energy costs. SGD/PHP and HKD/PHP serve major worker corridors, while AED/PHP and SAR/PHP connect Gulf-based Filipino workers with families at home. JPY/PHP and CNY/PHP are important Asian trade and travel crosses."),
    ],
    "faq": [
        ("Why are remittances important to the Philippine Peso?",
         "Overseas Filipino workers send large and relatively steady amounts home. Those inflows supply foreign currency, support household spending and can offset part of the country's goods-trade deficit."),
        ("Is the Philippine Peso pegged to the dollar?",
         "No. PHP floats and the Bangko Sentral ng Pilipinas may smooth excessive volatility or disorderly market conditions. The dollar remains influential because of trade, remittances, debt and imports."),
        ("Should visitors carry cash in the Philippines?",
         "Yes. Cards work well in formal urban businesses, but cash is necessary for local transport, markets, smaller islands and many independent vendors. Use reputable ATMs and keep smaller peso notes available."),
    ],
}

# ─────────────────────────── ARS ───────────────────────────
CURRENCY_ARTICLES["ARS"] = {
    "sections": [
        ("h", "A short history of the Argentine Peso"),
        ("p", "Argentina's peso replaced the austral in 1992 after years of inflation and currency instability. The Convertibility Plan then fixed one peso at one US dollar and temporarily restored confidence, but the rigid peg became impossible to maintain after recession, debt stress and capital flight. The peg collapsed in 2001–02, banks restricted withdrawals, and the peso began a new floating era after a sharp devaluation."),
        ("p", "The modern peso is shaped by repeated attempts to stabilize prices while financing a country with valuable agricultural, energy and mineral exports. Argentina has periodically used exchange controls, multiple official rates and import restrictions. For that reason, an online ARS quote may not equal the rate available for every transaction, and the gap between official and informal prices is itself a signal of policy credibility."),
        ("h", "What moves the ARS exchange rate"),
        ("p", "The peso responds less to one single commodity than to the public's confidence that inflation, public finances and access to foreign currency can be managed."),
        ("li", "Inflation and monetary policy: rapid price increases erode the peso's purchasing power and raise demand for dollars, while credible disinflation can support it"),
        ("li", "Fiscal and debt confidence: budget deficits, debt negotiations and expectations about government financing can trigger abrupt changes in the exchange rate"),
        ("li", "Export earnings and reserves: soy, grains, energy and mining bring in dollars, but harvests, commodity prices and reserve levels vary"),
        ("li", "Capital controls and the parallel market: restrictions on access to official dollars create different rates and can amplify expectations of devaluation"),
        ("h", "The Argentine Peso in practice"),
        ("p", "Argentina is a card-friendly country in large cities, but cash remains useful for taxis, small shops and everyday purchases. Visitors should understand which rate a card issuer, exchange house or merchant is using; dynamic conversion and informal offers can produce very different results. Prices can change quickly during periods of high inflation, so compare the final amount rather than relying on an old guidebook."),
        ("p", "Remittances and business payments require a licensed route and careful attention to local regulations. Families often think in dollars as a store of value even when they spend pesos, while exporters and importers manage the difference between invoicing currency and the rate at which funds can actually be settled. A low transfer fee does not compensate for a wide ARS spread."),
        ("h", "Popular Argentine Peso conversions"),
        ("p", "USD/ARS is the essential reference pair for savings, imports and inflation expectations. EUR/ARS and BRL/ARS serve tourism and regional trade, while CLP/ARS and UYU/ARS are useful for neighboring-country travel. Quotes should specify whether they refer to an official, card or cash-market rate."),
    ],
    "faq": [
        ("Why does the Argentine Peso have several exchange rates?", "Argentina has used foreign-exchange controls and limits on access to official dollars. Different legal channels, taxes and restrictions can therefore produce separate official, card and parallel-market rates."),
        ("Was the Argentine Peso ever equal to the US Dollar?", "Yes. The 1991 Convertibility Plan fixed one peso to one US dollar until the system broke down in 2001–02. The peg initially reduced inflation, but it ended with recession, debt stress and a major devaluation."),
        ("Is Argentina a cash or card economy?", "Both. Cards work widely in cities, but cash is important for small businesses and transport, and the effective exchange rate can differ by payment channel. Check the rate and fees before a large transaction."),
    ],
}

# ─────────────────────────── BGN ───────────────────────────
CURRENCY_ARTICLES["BGN"] = {
    "sections": [
        ("h", "A short history of the Bulgarian Lev"),
        ("p", "Bulgaria introduced the lev in 1881, taking its name from the word for lion. The currency passed through several difficult periods, including wartime inflation and post-communist instability. In 1997 Bulgaria adopted a currency board after a severe banking and inflation crisis. The lev was first fixed to the Deutsche Mark and then, when Germany adopted the euro, to the euro at BGN 1.95583 per EUR."),
        ("p", "The currency board means Bulgaria does not use an independent floating exchange rate in the usual sense. The Bulgarian National Bank must back the monetary base with foreign assets, and domestic interest conditions are strongly influenced by the euro area. Bulgaria joined the EU in 2007 and has worked toward eventual euro adoption, subject to the required economic and legal conditions."),
        ("h", "What moves the BGN exchange rate"),
        ("p", "The lev's euro rate is deliberately stable, so its important drivers are the economic conditions behind the peg and the credibility of Bulgaria's convergence path."),
        ("li", "The euro and ECB policy: Bulgarian money-market conditions follow the euro area because defending the fixed rate is the central monetary constraint"),
        ("li", "Fiscal and reserve credibility: disciplined public finances and ample foreign reserves reinforce confidence in the currency board"),
        ("li", "EU trade and investment: Germany and other EU economies drive manufacturing, tourism, supply chains and foreign direct investment"),
        ("li", "Inflation and euro-convergence expectations: local price growth, wages and the timetable for joining the euro affect real purchasing power and asset flows"),
        ("h", "The Bulgarian Lev in practice"),
        ("p", "Cards are accepted in Bulgarian cities, hotels and many restaurants, while lev cash remains useful in markets, rural areas and small businesses. Bulgaria is in the EU but currently uses the lev, so check whether an ATM or terminal is charging BGN or offering a home-currency conversion. Some tourist businesses quote euros, but paying in lev usually makes the exchange rate easier to verify."),
        ("p", "The fixed rate makes euro-to-lev transfers relatively predictable, but banks and exchange offices can still add a spread or fee. Businesses with euro-area suppliers generally face limited exchange-rate risk, whereas firms with dollar or other-currency costs still need to manage exposure. Compare the total received rather than assuming a fixed official rate means a free conversion."),
        ("h", "Popular Bulgarian Lev conversions"),
        ("p", "EUR/BGN is the defining pair and is fixed at 1.95583 lev per euro under the currency board. USD/BGN follows the dollar's movement against the euro, while RON/BGN, TRY/BGN and GBP/BGN serve regional trade, tourism and remittance flows."),
    ],
    "faq": [
        ("Is the Bulgarian Lev pegged to the euro?", "Yes. Bulgaria's currency board fixes one euro at BGN 1.95583. The lev can still vary against the dollar, pound and other currencies as those currencies move against the euro."),
        ("Does Bulgaria use the euro?", "Bulgaria currently uses the lev. It is an EU member committed to adopting the euro after meeting the required criteria, but the timing depends on formal assessments and policy decisions."),
        ("What is a currency board?", "A currency board commits the monetary authority to exchange the local currency at a fixed rate and back its monetary base with foreign assets. It limits discretionary money creation and makes the peg the core of monetary policy."),
    ],
}

# ─────────────────────────── CLP ───────────────────────────
CURRENCY_ARTICLES["CLP"] = {
    "sections": [
        ("h", "A short history of the Chilean Peso"),
        ("p", "Chile has used the peso since independence-era monetary reforms in the nineteenth century, although the currency was briefly replaced by the escudo in the 1960s. The modern peso returned in 1975 after a redenomination. Chile experimented with fixed and crawling exchange-rate arrangements, then moved to a freely floating peso in 1999, allowing the currency to absorb changes in commodity prices and global finance."),
        ("p", "The peso belongs to one of Latin America's most open and institutionally developed economies. Chile's central bank operates an inflation-targeting framework, while the country exports copper, lithium, fruit, wine, fish and other commodities. That combination gives CLP a clear connection to the world industrial cycle but also leaves it exposed to shifts in Chinese demand and global risk appetite."),
        ("h", "What moves the CLP exchange rate"),
        ("p", "The Chilean peso is a floating commodity currency, with copper and interest-rate expectations often setting the direction of the market."),
        ("li", "Copper and mining revenue: copper is Chile's flagship export, so prices, production and Chinese demand strongly affect foreign-currency income"),
        ("li", "Banco Central policy and inflation: changes in the policy rate and inflation expectations alter the return on peso assets"),
        ("li", "China and global manufacturing: Chile sells heavily into Asia, making CLP sensitive to industrial activity and construction demand abroad"),
        ("li", "Political and global risk: domestic constitutional debates, fiscal expectations and broad risk-off moves can increase the peso's volatility"),
        ("h", "The Chilean Peso in practice"),
        ("p", "Chile is relatively easy for travelers using cards in cities, hotels and supermarkets, but cash remains useful at markets, small restaurants and rural businesses. Prices are quoted in pesos and large numbers are normal. ATMs may charge a local fee in addition to the foreign-card fee, so make fewer, sensible withdrawals and decline dynamic currency conversion when offered."),
        ("p", "Chile's open economy creates active corridors for mining, agriculture, tourism, education and family transfers. Businesses often receive dollars for exports but pay wages and local suppliers in pesos, making hedging useful when copper or global rates move sharply. Remittance customers should compare the final CLP received, not just the advertised transfer fee."),
        ("h", "Popular Chilean Peso conversions"),
        ("p", "USD/CLP is the main reference rate and a widely followed gauge of copper and emerging-market sentiment. EUR/CLP serves European trade and tourism, while CLP/PEN, CLP/ARS and CLP/BRL connect Chile with its South American neighbors. CNY/CLP is increasingly relevant to mining and commodity trade."),
    ],
    "faq": [
        ("Why does copper affect the Chilean Peso?", "Copper is Chile's most important export, so its price influences export earnings, the current account and expectations for national income. CLP can weaken when copper falls, although interest rates and risk sentiment also matter."),
        ("Is the Chilean Peso pegged to the dollar?", "No. Chile has allowed CLP to float since 1999, with the central bank sometimes intervening in exceptional or disorderly conditions. Its exchange rate is therefore market-determined rather than fixed."),
        ("Is cash needed in Chile?", "Cards are widely accepted in urban Chile, but carry some pesos for markets, small businesses, transport and rural areas. Use bank ATMs and choose to be charged in CLP rather than accepting a terminal's conversion."),
    ],
}

# ─────────────────────────── CZK ───────────────────────────
CURRENCY_ARTICLES["CZK"] = {
    "sections": [
        ("h", "A short history of the Czech Koruna"),
        ("p", "The Czech koruna became the currency of the Czech Republic after the peaceful dissolution of Czechoslovakia in 1993. It initially shared a short-lived monetary union with Slovakia, then separated as the two new states established independent notes and coins. The Czech National Bank managed the exchange rate for years before the koruna began floating in 1997."),
        ("p", "The Czech Republic joined the European Union in 2004 but has retained the koruna rather than adopting the euro. It is a highly integrated manufacturing economy, closely tied to Germany and the wider European supply chain. The CNB's inflation-targeting framework and the country's strong industrial base make CZK one of the more liquid Central European currencies."),
        ("h", "What moves the CZK exchange rate"),
        ("p", "Koruna pricing combines domestic monetary policy with the fortunes of German industry and investor appetite for Central Europe."),
        ("li", "Czech National Bank policy: rate decisions, inflation forecasts and the outlook for real yields are central to CZK valuation"),
        ("li", "German and euro-area demand: cars, machinery and electronics connect Czech exports to European manufacturing cycles"),
        ("li", "Inflation and wages: domestic price and wage growth influence competitiveness and expectations for future interest rates"),
        ("li", "Regional and global risk: political shocks, energy costs and shifts out of emerging Europe can move CZK even when local data is calm"),
        ("h", "The Czech Koruna in practice"),
        ("p", "Prague and other Czech cities are card-friendly, but koruna cash remains useful at markets, small pubs, rural businesses and some ticket machines. The Czech Republic is in the EU but not the euro area. Tourist businesses may quote euros, yet the exchange rate is often better and clearer when paying in CZK. At ATMs, reject dynamic currency conversion and let the card network handle the exchange."),
        ("p", "The Czech economy has dense trade and investment links with Germany, Slovakia and the rest of the EU. Companies often invoice in euros while paying Czech wages and suppliers in koruna, so even a modest move can affect margins. Cross-border workers and families should compare both the transfer fee and the CZK rate offered by the provider."),
        ("h", "Popular Czech Koruna conversions"),
        ("p", "EUR/CZK is the key pair for trade, tourism and CNB expectations. USD/CZK reflects the dollar and global risk cycle, while PLN/CZK, HUF/CZK and SKK-related legacy corridors are useful regional references. GBP/CZK serves UK travel, education and business payments."),
    ],
    "faq": [
        ("Does the Czech Republic use the euro?", "No. The Czech Republic uses the koruna and has no current adoption date. As an EU member it has a long-term obligation in principle, but entry requires meeting criteria and a domestic policy decision."),
        ("Why did the Czech koruna float?", "The Czech National Bank ended its exchange-rate commitment in April 2017 after using a weaker koruna to prevent excessively low inflation. Since then CZK has generally been market-determined, with the CNB able to respond to disorderly conditions."),
        ("Can I pay with euros in Prague?", "Some tourist businesses accept euros, but coverage and rates vary. Paying in koruna by card or with local cash is normally more transparent, especially outside central tourist areas."),
    ],
}

# ─────────────────────────── EGP ───────────────────────────
CURRENCY_ARTICLES["EGP"] = {
    "sections": [
        ("h", "A short history of the Egyptian Pound"),
        ("p", "Egypt introduced the pound in the nineteenth century as part of a move toward a modern national monetary system. The currency was once closely linked to sterling and later to the dollar, but economic shocks, wars and changing reserve conditions brought repeated adjustments. Since 2016 Egypt has experienced several major devaluations as authorities worked to unify exchange markets and secure external financing."),
        ("p", "The pound's value is closely tied to Egypt's ability to obtain foreign currency for imports and debt service. Tourism, Suez Canal receipts, remittances and exports supply dollars, while energy, food and machinery create large import needs. Because access rules and official rates can change, a published EGP rate should be treated as a reference until a bank or licensed provider confirms the executable rate."),
        ("h", "What moves the EGP exchange rate"),
        ("p", "The Egyptian pound is influenced by external funding and domestic inflation as much as by ordinary trade flows."),
        ("li", "Foreign-exchange liquidity and reserves: official availability of dollars affects importers, banks and confidence in the pound"),
        ("li", "Inflation and central-bank policy: high local inflation reduces purchasing power, while interest-rate decisions influence deposits and capital flows"),
        ("li", "Tourism, Suez and remittances: visitor spending, canal revenue and transfers from Egyptians abroad are vital sources of foreign currency"),
        ("li", "Energy, food and external debt: import bills, subsidy policy and scheduled repayments can increase demand for dollars and pressure EGP"),
        ("h", "The Egyptian Pound in practice"),
        ("p", "Cards are accepted in many Cairo hotels, malls and established restaurants, but cash in Egyptian pounds remains essential for taxis, markets, small shops and many local services. Travelers should use licensed exchange offices or bank ATMs and check notes carefully. Prices and exchange practices can change quickly, so avoid relying on an old quoted rate or exchanging a large amount at an airport desk."),
        ("p", "Egypt is a major remittance destination and a large tourism market. Families and businesses should confirm whether a transfer is settled through an official bank channel, a cash-pickup network or another authorized route. Comparing the total EGP received is especially important when restrictions, fees or different rate windows make the headline commission misleading."),
        ("h", "Popular Egyptian Pound conversions"),
        ("p", "USD/EGP is the principal reference pair for imports, savings and external debt. EUR/EGP and GBP/EGP are common in tourism and diaspora transfers, while SAR/EGP, AED/EGP and KWD/EGP connect Egypt with Gulf employers and investors. Rates can differ by channel, so quote terms matter."),
    ],
    "faq": [
        ("Why has the Egyptian Pound been devalued?", "Egypt has faced high import needs, inflation, foreign-exchange shortages and external financing pressures. Devaluations and a move toward a more flexible rate have been used to restore market access and attract foreign currency, though they also raise local prices."),
        ("Can I use US dollars in Egypt?", "Some hotels and tourist businesses quote or accept dollars, but the pound is the official currency and is needed for many everyday purchases. Paying in EGP and using licensed exchange channels usually gives clearer terms."),
        ("Where should visitors exchange money in Egypt?", "Use banks, licensed exchange offices or reputable ATMs, and keep receipts where required. Avoid unofficial street exchanges and check the provider's rate, commission and any withdrawal limit before committing funds."),
    ],
}

# ─────────────────────────── HUF ───────────────────────────
CURRENCY_ARTICLES["HUF"] = {
    "sections": [
        ("h", "A short history of the Hungarian Forint"),
        ("p", "Hungary introduced the forint in 1946 to replace the pengő after one of the worst episodes of hyperinflation ever recorded. The new currency restored a usable unit of account and was named after the Florentine fiorino. Under state socialism the exchange rate was controlled; after the transition to a market economy, HUF moved through managed arrangements and became a more flexible, market-traded currency."),
        ("p", "Hungary joined the European Union in 2004 but has kept the forint. Its economy is deeply integrated with German manufacturing and EU supply chains, while domestic inflation, energy imports and fiscal policy can produce large moves. The National Bank of Hungary has used interest rates and other tools to influence inflation and financial stability, particularly during recent periods of volatility."),
        ("h", "What moves the HUF exchange rate"),
        ("p", "The forint is a liquid but risk-sensitive Central European currency whose rate reflects both local policy and the regional cycle."),
        ("li", "National Bank policy and inflation: large changes in inflation or the policy-rate path alter the return on forint assets"),
        ("li", "EU funds and fiscal policy: access to European funding, budget credibility and public-sector measures affect investor confidence"),
        ("li", "Energy and trade balances: Hungary imports much of its energy, while manufacturing exports and German demand supply foreign income"),
        ("li", "Global risk and regional flows: investors often sell HUF alongside other emerging European currencies during dollar or geopolitical shocks"),
        ("h", "The Hungarian Forint in practice"),
        ("p", "Budapest is easy to navigate with cards and contactless payments, but forint cash remains useful at markets, small cafés, baths and rural businesses. Hungary does not use the euro, even though tourist prices may be shown in euros. Always check the terminal or ATM currency and decline dynamic conversion; a familiar home-currency amount can conceal a wide margin."),
        ("p", "Cross-border workers, students and manufacturers create regular HUF corridors with Austria, Germany, Slovakia and Romania. A company may sell in euros but pay Hungarian costs in forint, so budgeting at a reference rate and hedging larger invoices can protect margins. Remittance users should compare the HUF amount received, not merely the transfer fee."),
        ("h", "Popular Hungarian Forint conversions"),
        ("p", "EUR/HUF is the dominant pair for Hungarian trade, travel and monetary-policy expectations. USD/HUF reflects the global dollar cycle, while PLN/HUF, CZK/HUF and RON/HUF connect Central European markets. GBP/HUF is common for UK–Hungary travel, education and family transfers."),
    ],
    "faq": [
        ("Why are Hungarian prices shown in large numbers?", "The forint has a relatively low unit value against major currencies and has experienced historical inflation. Large nominal figures are a feature of its denomination, not a direct measure of current purchasing power."),
        ("Does Hungary use the euro?", "No. Hungary uses the forint and has no announced euro adoption date. EU membership creates a long-term commitment in principle, but meeting criteria and choosing a timetable remain matters for Hungarian policy."),
        ("Is the forint a freely floating currency?", "HUF is broadly market-determined, but the National Bank of Hungary can use interest rates, liquidity tools and communication to limit disorderly moves and protect financial stability."),
    ],
}

# ─────────────────────────── ILS ───────────────────────────
CURRENCY_ARTICLES["ILS"] = {
    "sections": [
        ("h", "A short history of the Israeli New Shekel"),
        ("p", "Israel's new shekel was introduced in 1985 as part of a stabilization program that replaced the old shekel at a ratio of 1,000 to one. It followed the earlier Israeli pound and a period of very high inflation. The program paired fiscal and monetary measures with a more disciplined exchange-rate framework, helping establish the currency used today."),
        ("p", "The Bank of Israel gradually moved the shekel toward a floating regime during the 1990s. Israel's economy now combines technology exports, services, manufacturing and a growing natural-gas industry, while maintaining substantial foreign-exchange reserves. The shekel can be liquid and resilient, but geopolitical risk can change its direction quickly and may prompt central-bank action."),
        ("h", "What moves the ILS exchange rate"),
        ("p", "The shekel is driven by the contrast between Israel's strong external sectors and the security and policy risks surrounding the economy."),
        ("li", "Bank of Israel and US policy: interest-rate expectations influence capital flows, mortgages and the relative return on shekel assets"),
        ("li", "Technology and services exports: foreign investment and high-value exports bring dollars into Israel and can support ILS"),
        ("li", "Geopolitical conditions: conflict, security uncertainty and fiscal demands can lead residents and investors to seek foreign currency"),
        ("li", "Energy, trade and reserves: gas exports, imports and the central bank's substantial reserves affect the external balance and confidence"),
        ("h", "The Israeli New Shekel in practice"),
        ("p", "Israel is highly card-oriented, with contactless payments common in cities, transport and restaurants. Shekel cash is still useful at markets, small vendors and some taxis. Travelers should confirm whether a terminal is charging ILS or offering dynamic conversion into a home currency. The shekel is the everyday legal tender even when hotels or tour operators display dollar or euro estimates."),
        ("p", "Israel has important corridors with North America, Europe and Jewish communities worldwide, alongside technology and defense trade. Businesses may earn dollars or euros while paying local wages and tax in shekels, so currency hedging can matter when geopolitical news drives rapid moves. Remittance customers should compare the final ILS received and the provider's settlement terms."),
        ("h", "Popular Israeli New Shekel conversions"),
        ("p", "USD/ILS is the main global reference pair and reacts to US rates, technology flows and security headlines. EUR/ILS and GBP/ILS serve European travel and trade, while ILS/JPY and ILS/CHF can reflect broader safe-haven and risk movements. ILS/AED and ILS/SAR are used in regional business corridors."),
    ],
    "faq": [
        ("What is the difference between the shekel and the new shekel?", "The new shekel replaced the old shekel in 1985 at 1,000 old shekels for one new shekel. ILS is the ISO code for the current currency; 'shekel' is the name commonly used in daily speech."),
        ("Is the Israeli Shekel pegged to the dollar?", "No. The shekel has floated since the 1990s. The Bank of Israel can intervene or adjust policy in exceptional circumstances, but ordinary USD/ILS pricing is determined by the market."),
        ("Can I pay with dollars in Israel?", "Some tourist businesses may accept dollars, but prices and change are usually clearer in shekels. Cards are widely accepted, and visitors should choose ILS at payment terminals to avoid dynamic-conversion markups."),
    ],
}

# ─────────────────────────── ISK ───────────────────────────
CURRENCY_ARTICLES["ISK"] = {
    "sections": [
        ("h", "A short history of the Icelandic Krona"),
        ("p", "Iceland's modern krona was introduced in 1981 after a redenomination in which 100 old kronur became one new krona. The currency inherited a history of exchange controls, inflation and close links to the Danish monetary system. Iceland eventually allowed the krona to float in 2001, giving it a market price that could adjust to the country's small and specialized economy."),
        ("p", "The 2008 global financial crisis brought an extraordinary test: the collapse of Iceland's oversized banking system caused a sharp fall in ISK and temporary capital controls. The currency later recovered as tourism, fisheries and an export-oriented recovery improved the external balance. ISK remains a small, volatile currency whose domestic price and seasonal flows deserve attention."),
        ("h", "What moves the ISK exchange rate"),
        ("p", "Iceland's currency responds to the country's narrow export base, tourism cycle and interest-rate decisions more dramatically than larger European currencies do."),
        ("li", "Tourism receipts: international visitors bring a large seasonal flow of foreign currency, supporting demand for ISK during strong travel years"),
        ("li", "Fisheries and aluminum: fish products and energy-intensive aluminum exports are key sources of external income"),
        ("li", "Central Bank policy and inflation: high domestic rates may support the krona, while inflation and wage pressures can weaken confidence"),
        ("li", "Global risk and capital flows: a small market can move sharply when investors reduce exposure or when funding conditions tighten"),
        ("h", "The Icelandic Krona in practice"),
        ("p", "Iceland is very card-friendly; contactless payments work at hotels, petrol stations, restaurants and many remote attractions. Cash is rarely essential, though a small amount of kronur can help at a few unattended facilities or small operators. Travelers should pay in ISK rather than accepting a terminal's conversion into euros, dollars or pounds, and remember that Iceland's prices can be high even when the exchange rate is favorable."),
        ("p", "Tourism companies and exporters may receive foreign currency while paying Icelandic wages and local costs in kronur. Because the currency is seasonal and thinly traded, businesses often budget conservatively and hedge larger obligations. For transfers, compare the rate and fixed fee carefully: a small spread matters when converting rent, salaries or travel budgets."),
        ("h", "Popular Icelandic Krona conversions"),
        ("p", "EUR/ISK is the most useful European reference pair, while USD/ISK reflects global risk and energy conditions. GBP/ISK is common for tourism, and NOK/ISK and DKK/ISK connect Iceland to its Nordic neighbors. CAD/ISK can matter for travel and fisheries-related trade."),
    ],
    "faq": [
        ("Why is the Icelandic Krona volatile?", "Iceland has a small economy, a narrow export base and a relatively small financial market. Tourism seasons, fisheries, interest rates and global risk flows can therefore move ISK more than they move larger currencies."),
        ("Does Iceland use the euro?", "No. Iceland uses the Icelandic krona. Cards are widely accepted, but visitors should select ISK at payment terminals and exchange only modest amounts of cash when needed."),
        ("What happened to ISK in 2008?", "Iceland's banking collapse triggered a severe loss of confidence and a sharp krona depreciation. Capital controls were introduced during the crisis and later relaxed as the financial system and external position stabilized."),
    ],
}

# ─────────────────────────── NGN ───────────────────────────
CURRENCY_ARTICLES["NGN"] = {
    "sections": [
        ("h", "A short history of the Nigerian Naira"),
        ("p", "Nigeria introduced the naira in 1973, replacing the Nigerian pound after independence and decimalizing the monetary system. The Central Bank of Nigeria initially managed the currency closely, but oil-price shocks, fiscal pressures and changing foreign-exchange policy produced repeated devaluations. The naira's modern history is therefore tied to the challenge of converting large oil receipts into stable domestic purchasing power."),
        ("p", "Nigeria has periodically operated more than one exchange-rate window, especially when official foreign-currency supply could not meet demand. In 2023 authorities moved toward a more market-led system, followed by substantial volatility and further policy changes. Remittance recipients and businesses should distinguish an indicative quote from the rate available through a licensed settlement channel."),
        ("h", "What moves the NGN exchange rate"),
        ("p", "The naira is shaped by oil income and dollar liquidity, while inflation and exchange-market policy determine how quickly those forces reach households."),
        ("li", "Oil production and prices: crude exports provide most of Nigeria's foreign-exchange earnings, so outages, prices and production targets matter greatly"),
        ("li", "Central-bank policy and liquidity: intervention, interest rates, reserve management and the structure of FX windows influence the executable rate"),
        ("li", "Inflation and imports: food, fuel, machinery and other imports create persistent demand for dollars and can weaken the naira when prices rise"),
        ("li", "Remittances and investment flows: diaspora transfers, portfolio money and foreign direct investment supply dollars but can change with confidence"),
        ("h", "The Nigerian Naira in practice"),
        ("p", "Nigeria uses a mix of cards, mobile transfers and cash. Cards and bank apps work in many cities, but cash remains important for transport, markets, smaller merchants and areas with unreliable connectivity. Visitors and residents should use regulated banks, bureaux de change or licensed payment providers, keep transaction records and be cautious of unofficial exchange offers."),
        ("p", "Nigeria is a major remittance destination and a regional commercial hub. Because rates and liquidity can vary by provider and settlement route, the amount finally received matters more than a zero-fee advertisement. Businesses often invoice in dollars but pay local wages and suppliers in naira, creating a need to manage both conversion risk and the rules governing access to foreign currency."),
        ("h", "Popular Nigerian Naira conversions"),
        ("p", "USD/NGN is the principal reference pair for oil, imports, remittances and investor confidence. GBP/NGN and EUR/NGN serve large diaspora and trade corridors, while AED/NGN connects Nigeria with Gulf-based workers and businesses. GHS/NGN and XOF/NGN are relevant West African regional crosses."),
    ],
    "faq": [
        ("Why has the Nigerian Naira weakened?", "Pressure has come from high inflation, strong demand for imported goods and dollars, constrained oil production, fiscal needs and periods when official FX supply did not meet demand. Policy changes can also cause abrupt repricing between exchange-rate windows."),
        ("Is there one Nigerian Naira exchange rate?", "The market has moved toward a more unified, market-led framework, but rates can still differ by venue, timing, fees and access rules. Confirm the rate and settlement method with a licensed provider before sending money."),
        ("Can visitors use cards in Nigeria?", "Cards and mobile payments work at many formal businesses, especially in cities, but outages, limits and connectivity issues make cash a useful backup. Use reputable ATMs and follow current banking and travel guidance."),
    ],
}

# ─────────────────────────── PKR ───────────────────────────
CURRENCY_ARTICLES["PKR"] = {
    "sections": [
        ("h", "A short history of the Pakistani Rupee"),
        ("p", "Pakistan continued to use the rupee after independence in 1947 and established the State Bank of Pakistan in 1948. The currency moved through fixed and managed arrangements before a more flexible regime emerged around the turn of the century. Devaluations have often followed periods in which imports and external debt payments outpaced the country's supply of dollars."),
        ("p", "The rupee's value is closely connected to Pakistan's balance of payments. Textile and agricultural exports, overseas-worker remittances and official financing bring in foreign currency, while energy, machinery and debt service create demand for it. Inflation, political uncertainty and negotiations with international lenders can therefore move PKR as quickly as ordinary trade data."),
        ("h", "What moves the PKR exchange rate"),
        ("p", "The Pakistani rupee trades on external financing, import demand and confidence in the country's stabilization program."),
        ("li", "Reserves and external financing: IMF programs, bilateral support, debt rollovers and official inflows affect the supply of dollars"),
        ("li", "Energy and the import bill: Pakistan imports much of its fuel and machinery, so oil prices and industrial demand pressure the rupee"),
        ("li", "Remittances and exports: transfers from overseas Pakistanis and textile, rice and other exports provide crucial foreign exchange"),
        ("li", "Inflation, interest rates and political risk: domestic prices, monetary tightening and confidence in policy determine demand for PKR assets"),
        ("h", "The Pakistani Rupee in practice"),
        ("p", "Cash remains important in Pakistan, although cards, bank transfers and mobile wallets are increasingly common in cities. Travelers should carry smaller rupee notes for transport, markets and local shops, use bank-affiliated ATMs and keep a backup payment method. A quoted dollar or euro price may be convenient for a hotel, but paying in PKR usually makes the applied rate easier to inspect."),
        ("p", "Pakistan is one of the world's largest remittance destinations, with major corridors from the Gulf, the United Kingdom, North America and Europe. Licensed banks and money-transfer services compete on fees and rates, while documentation and settlement rules can affect delivery. Compare the amount received and the delivery method rather than choosing solely by headline commission."),
        ("h", "Popular Pakistani Rupee conversions"),
        ("p", "USD/PKR is the main reference pair for imports, debt and remittances. AED/PKR and SAR/PKR are especially important Gulf-worker corridors, while GBP/PKR and EUR/PKR serve diaspora communities. INR/PKR reflects regional interest but is less central to ordinary public transactions than the dollar pairs."),
    ],
    "faq": [
        ("Why is the Pakistani Rupee under pressure?", "Large import and debt-service needs, high inflation, limited reserves, political uncertainty and changing external financing can all increase demand for dollars. Remittances and policy support can ease that pressure but do not remove it permanently."),
        ("What role does the IMF play in PKR?", "IMF programs can provide financing and a policy framework for rebuilding reserves, reducing fiscal imbalances and improving the foreign-exchange market. Reviews and conditions can therefore affect confidence in PKR and the availability of dollars."),
        ("Should I carry cash in Pakistan?", "Yes. Cards and mobile payments work in many formal businesses, but cash is still needed for transport, markets and smaller towns. Use reputable exchange providers and avoid carrying more cash than necessary."),
    ],
}

# ─────────────────────────── RON ───────────────────────────
CURRENCY_ARTICLES["RON"] = {
    "sections": [
        ("h", "A short history of the Romanian Leu"),
        ("p", "Romania's leu has roots in the nineteenth-century monetary system and takes its name from the lion. The current leu was introduced in 2005 in a redenomination that removed four zeros: 10,000 old lei became one new leu. Romania joined the European Union in 2007 but has retained RON while its economy and institutions converge with the euro area."),
        ("p", "The National Bank of Romania generally manages the leu against a broad set of economic conditions rather than allowing the kind of free fluctuation seen in some neighboring markets. EU trade, foreign investment, migrant remittances and sizeable domestic inflation all matter. Romania has a long-term euro objective, but adoption requires meeting the relevant convergence criteria and making a political decision on timing."),
        ("h", "What moves the RON exchange rate"),
        ("p", "The leu balances a managed exchange-rate approach with a fast-changing economy exposed to European trade, inflation and fiscal policy."),
        ("li", "National Bank policy and inflation: interest rates, liquidity operations and the inflation outlook influence demand for RON"),
        ("li", "EU trade and investment: Germany, Italy and other EU partners drive manufacturing, services, supply chains and investment flows"),
        ("li", "Fiscal and external balances: public spending, the current-account deficit and energy imports affect confidence and financing needs"),
        ("li", "Remittances and regional risk: money sent by Romanians abroad supports foreign-currency supply, while shocks in Central Europe can weaken RON"),
        ("h", "The Romanian Leu in practice"),
        ("p", "Cards and contactless payments are common in Romanian cities, while cash in lei remains useful for markets, small villages, tips and some transport. Romania is in the EU but does not use the euro. Tourist businesses may quote euros, yet a card transaction in RON is usually more transparent. At an ATM or terminal, reject dynamic currency conversion unless there is a clear reason to choose it."),
        ("p", "Romania has large corridors with Italy, Spain, Germany and the United Kingdom because of trade, migration and family transfers. A worker sending money home should compare the RON received after all fees, while an importer should account for euro invoices against leu revenue. Companies often manage this exposure through euro pricing or simple forward contracts."),
        ("h", "Popular Romanian Leu conversions"),
        ("p", "EUR/RON is the central pair for trade, investment and Romanian households. USD/RON reflects the global dollar cycle, while GBP/RON and CHF/RON serve important diaspora, savings and travel corridors. HUF/RON, PLN/RON and BGN/RON are useful regional crosses."),
    ],
    "faq": [
        ("Will Romania adopt the euro?", "Romania has a long-term commitment as an EU member, but it has no fixed adoption date. It must meet economic and legal convergence conditions and decide when joining best suits the country."),
        ("What was the 2005 Romanian redenomination?", "Romania removed four zeros from the currency: 10,000 old lei became one new leu. It simplified prices and accounting but did not by itself change people's real purchasing power."),
        ("Is the Romanian Leu pegged to the euro?", "No. RON is not fixed to the euro, although the National Bank of Romania manages volatility and pays close attention to euro-area conditions because Europe dominates Romanian trade."),
    ],
}

# ─────────────────────────── TWD ───────────────────────────
CURRENCY_ARTICLES["TWD"] = {
    "sections": [
        ("h", "A short history of the New Taiwan Dollar"),
        ("p", "The New Taiwan dollar was issued in 1949 during a period of monetary reform and post-war instability. It replaced the old Taiwan dollar at 40,000 old dollars for one new dollar, restoring a workable unit after severe inflation. Taiwan's central bank later guided the currency through export-led industrialization, moving from tighter management toward a more flexible market rate."),
        ("p", "Today TWD is the money of a major technology and manufacturing economy. Taiwan is central to global semiconductor supply chains and also exports electronics, machinery and chemical products. The Central Bank of the Republic of China (Taiwan) monitors the exchange rate closely, seeking to limit disorderly movements while allowing economic fundamentals and trade flows to influence it."),
        ("h", "What moves the TWD exchange rate"),
        ("p", "The Taiwan dollar is an export currency whose direction often reflects chip demand, regional geopolitics and the balance between foreign investment and local savings."),
        ("li", "Semiconductors and electronics: chip cycles, technology investment and export orders affect Taiwan's trade surplus and dollar supply"),
        ("li", "US and China trade: Taiwan's supply-chain links with both markets make their growth, tariffs and technology policies important to TWD"),
        ("li", "Central-bank policy: domestic rates, liquidity and the CBC's approach to smoothing volatility influence the currency's trading range"),
        ("li", "Geopolitical and global risk: security tensions or a broad flight to safety can increase demand for dollars and pressure TWD"),
        ("h", "The New Taiwan Dollar in practice"),
        ("p", "Taiwan is highly convenient for digital payments, with cards and mobile wallets common in cities, while cash remains useful at night markets, small eateries, temples and some taxis. The EasyCard and other stored-value cards are practical for public transport. Visitors should choose TWD at card terminals and ATMs rather than accepting dynamic conversion into a home currency."),
        ("p", "Taiwanese manufacturers often earn US dollars but pay local wages and suppliers in TWD, so the exchange rate is an important margin variable. Remittances and business transfers with the United States, Japan, mainland China and Southeast Asia are well established, but the final amount depends on fees, bank spreads and the permitted settlement route."),
        ("h", "Popular New Taiwan Dollar conversions"),
        ("p", "USD/TWD is the principal reference pair and a close watch on the technology cycle. JPY/TWD and CNY/TWD reflect regional trade and tourism, while EUR/TWD serves European technology and machinery links. SGD/TWD and KRW/TWD are useful Asian manufacturing crosses."),
    ],
    "faq": [
        ("What is the difference between TWD and the Taiwan dollar?", "TWD is the ISO currency code for the New Taiwan dollar, the currency issued and managed by Taiwan's central bank. People commonly call it the Taiwan dollar or simply NT dollar in English."),
        ("Is the New Taiwan Dollar pegged to the US Dollar?", "No. TWD is market-determined within a managed framework. Taiwan's central bank can smooth excessive volatility, but the rate responds to trade, technology flows, interest rates and global risk."),
        ("Do I need cash in Taiwan?", "Cards and mobile payments work widely in cities, but cash is still important at night markets, small food stalls, temples and some local transport situations. Keep some TWD and a backup payment method."),
    ],
}

# ─────────────────────────── VND ───────────────────────────
CURRENCY_ARTICLES["VND"] = {
    "sections": [
        ("h", "A short history of the Vietnamese Dong"),
        ("p", "Vietnam introduced the dong in 1946 for the Democratic Republic of Vietnam, and a separate southern dong circulated before reunification. The State Bank later unified the currency, and a 1985 redenomination attempted to simplify the unit after severe inflation. The reform era that began with Doi Moi in 1986 gradually opened Vietnam to trade, investment and a more market-oriented exchange system."),
        ("p", "The dong is not a freely floating currency: the State Bank of Vietnam manages the central rate and permits market movement around it. Vietnam's transformation into an export and manufacturing hub has brought large foreign-investment inflows, while electronics, textiles, footwear, agriculture and tourism supply foreign currency. Large denominations are normal, and digital payments are expanding rapidly alongside cash."),
        ("h", "What moves the VND exchange rate"),
        ("p", "Dong pricing reflects Vietnam's managed exchange-rate framework as well as the country's trade surplus, imported costs and global dollar conditions."),
        ("li", "State Bank policy: the daily reference rate, trading band, liquidity tools and intervention shape how quickly VND can adjust"),
        ("li", "Exports and foreign investment: electronics, garments, footwear and manufacturing inflows bring dollars and other currencies into Vietnam"),
        ("li", "China, the United States and regional supply chains: trade demand, imported components and shifting production locations affect the balance"),
        ("li", "Inflation, energy and remittances: imported fuel and materials raise dollar demand, while overseas Vietnamese transfers support foreign-currency supply"),
        ("h", "The Vietnamese Dong in practice"),
        ("p", "Vietnam is a mix of cash and fast-growing digital payments. Cards work at hotels, malls and established restaurants, while dong cash is essential for street food, markets, taxis and many small businesses. Prices commonly use large numbers, so check the number of zeros carefully. At ATMs and terminals, choose VND rather than accepting a foreign-currency conversion with an unknown margin."),
        ("p", "Vietnam receives remittances from workers and diaspora communities and is a major destination for manufacturing investment and tourism. Licensed banks and transfer providers can differ substantially in fees, limits and the rate applied. Companies with dollar export revenue and dong payroll costs may hedge or match receipts and expenses to reduce exchange-rate uncertainty."),
        ("h", "Popular Vietnamese Dong conversions"),
        ("p", "USD/VND is the principal reference pair and is closely watched by importers, exporters and travelers. CNY/VND reflects the deep supply-chain relationship with China, while JPY/VND, KRW/VND and SGD/VND serve major Asian investment and trade corridors. EUR/VND and AUD/VND are common for tourism, education and remittances."),
    ],
    "faq": [
        ("Why are Vietnamese prices shown in large numbers?", "The dong has a low unit value and Vietnam has retained its large denominations rather than repeatedly removing zeros. The numbers are normal; count the zeros carefully and check whether a price is quoted in thousands or millions."),
        ("Is the Vietnamese Dong freely floating?", "No. The State Bank of Vietnam manages VND through a reference rate, a trading band and market operations. Supply and demand matter, but the official framework limits the speed and size of ordinary moves."),
        ("Should I use cash or cards in Vietnam?", "Use both. Cards are convenient at formal businesses in larger cities, but dong cash remains essential for street vendors, markets, local transport and smaller towns. Use reputable ATMs and decline dynamic currency conversion."),
    ],
}
