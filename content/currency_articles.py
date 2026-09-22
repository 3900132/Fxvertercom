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
        ("li", "ECB policy and eurozone inflation, the same rate cycle story as the Fed but with nineteen governments watching"),
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
        ("p", "The UK invented the gold standard, anchored world trade during the empire era, and then managed a long, orderly decline from it — including the 1992 Black Wednesday, when speculators forced the pound out of the European exchange-rate mechanism in a single day. That episode is why Britain never adopted the euro, and why Bank of Independence (1997) matters so much to the currency's credibility today."),
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
        ("p", "The renminbi (officially, the currency; the yuan is its unit) was issued by the newly founded People's Bank of China in 1948, before the PRC itself was proclaimed. Through the planned-economy decades it was an internal accounting unit; the 1978 reform era turned it into a real currency again."),
        ("p", "The modern story is a gradual internationalization: the 1994 unification of exchange rates, the 2005 move to a managed float, the 2015 surprise devaluation that shook global markets, and 2016, when the IMF added the yuan to its Special Drawing Rights basket — formal recognition as a world reserve currency. The digital yuan (e-CNY) is the newest chapter, one of the first major central-bank digital currencies."),
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
        ("p", "For salaries and savings, the franc is what it has always been: the region's storage of value. For remittance, Switzerland is one of the most expensive corridors in Europe — the markup gap between banks and specialist services is unusually wide, so comparison matters more than usual."),
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
        ("p", "Australia runs one of the most cashless economies on the planet — contactless everywhere, and even buskers take cards. Travelers barely need cash outside remote areas. Note that prices shown typically exclude GST (10%), which is already included in shelf prices by law, making sticker prices honest."),
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
        ("p", "The lira is the currency of the Republic of Turkey since 1923, inheriting the Ottoman pound. Its modern history is a chronicle of chronic inflation: prices rose so persistently that in 2005 Turkey knocked six zeros off, creating the New Turkish Lira (the New was dropped in 2009). A middle-class savings habit in foreign currency — dollars under mattresses and gold at home — grew out of those decades."),
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
