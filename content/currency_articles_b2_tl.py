# -*- coding: utf-8 -*-
"""Filipino (tl) translations of the second batch of long-form currency articles
— emerging-market and pegged currencies promoted in site_config.INDEXED_CURRENCIES.

Mirrors content/currency_articles_b2_en.py: one entry per ISO code with
'sections' — ("h", heading), ("p", paragraph) or ("li", bullet) — and 'faq' —
(question, answer) pairs. This file covers (alphabetical): AZN BDT ETB GEL GHS
KES KWD KZT LKR MAD QAR TZS UAH XAF XOF.
"""

ARTICLES_B2 = {}

# ─────────────────────────── AZN ───────────────────────────
ARTICLES_B2["AZN"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng manat ng Azerbaijan"),
        ("p", "Ang manat ang pangalan na ibinigay ng mga Azerbaijani sa ruble ng Sobyet, kaya nang dumating ang kasarinlan, kinuha lang ng bagong currency ang lumang pang-araw-araw na salita. Lumitaw ang unang manat noong 1992 at naging tanging legal tender noong 1994; noong 1 Enero 2006, na-redenominate ito sa 5,000 lumang manat bawat isang bagong manat, kasama ang mga muling dinisenyong banknote na nagbigay sa currency ng kasalukuyan nitong malinaw na anyong Europeo."),
        ("p", "Sa unang dekada nito, nakakandado ang bagong manat sa dolyar ng US sa nakapirming antas habang ini-develop ang mga oil field ng Caspian at binuksan ng Baku–Tbilisi–Ceyhan pipeline ang ruta patungo sa mga merkado ng Mediterranean. Ginawang mabilis na mayaman ang Azerbaijan ng langis: itinatag ang State Oil Fund (SOFAZ) noong 1999 para i-ipon ang windfall, at napuno ng mga construction crane ang Baku."),
        ("p", "Nabasag ang peg ng pagbagsak ng presyo ng langis noong 2014–2015. Ibinaba ng bangko sentral ang manat sa dalawang matalim na hakbang noong 2015, at pagkatapos ay lumipat sa heavily managed float na nakasentro sa dolyar. Nananatiling buhay ang regime mula noon, sinusuportahan ng reserba ng oil fund — bagama't nanatiling mataas ang demands sa piskal ng digmaan sa Nagorno-Karabakh noong 2020 at ng gastos sa post-war reconstruction."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng AZN"),
        ("p", "Isa sa pinakamahigpit na managed float sa mundo ang manat: nagtatakda ng tono ang bangko sentral, at nagtatakda ng tono para sa bangko sentral ang langis."),
        ("li", "Presyo ng langis at gas: ang eksport ng crude at gas ang base ng kita ng estado, kaya ang mga world energy price ang nagtutulak sa fundamentals ng manat"),
        ("li", "SOFAZ at ang badyet: kung gaano karaming pera ng langis ang dumadaloy mula sa state fund papunta sa gastos ng gobyerno ang humuhubog sa supply ng dolyar sa merkado"),
        ("li", "Patakaran ng bangko sentral: ipinagtatanggol ang managed float gamit ang interbensyon at reserba, at nananatiling operational anchor ang dolyar"),
        ("li", "Ugnayan sa Turkey at Russia: ang kalakalan, pamumuhunan at milyun-milyong regional na biyahero ang nag-uugnay ng paligid ng manat sa lira at ruble"),
        ("h", "Ang manat ng Azerbaijan sa praktika"),
        ("p", "Card-first ang pakiramdam ng Baku: gumagana ang contactless payments sa taxi, restaurant at tindahan, at hina-handle ng transport card ng lungsod ang metro. Tumatanggap din ng card payment ang mga ride-hailing app at delivery service. Sa labas ng kabesera, mas mahalaga ang cash, at gusto ng maliliit na palengke ang manat. Sa praktika, halos hindi ma-convert ang manat sa abroad — magpalit ng pera pagdating at i-convert ang natira bago umalis ng bansa."),
        ("p", "Nasa gitna ng ilang daloy ng pera nang sabay-sabay ang Azerbaijan: tumatanggap ito ng investment at transit fee, nagpapadala ng remittance sa mga partner sa Georgia at Turkey, at nag-o-host ng malaking seasonal na trapiko mula sa Russia, Turkey, Iran at Golpo. Dapat ipagpalagay ng mga negosyong nakikitungo sa Azerbaijan ang dollar invoicing para sa malalaking kontrata at magplano para sa mga lokal na regulasyon sa conversion. Madali at makatwirang presyo ang matatagpuan ng mga manlalakbay sa Baku ayon sa mga pamantayan ng Europa, at ginagawang madali ang pagbabadyet ng katatagan ng manat."),
        ("h", "Mga popular na conversion ng manat ng Azerbaijan"),
        ("p", "Ang USD/AZN ang anchor pair at ang rate na huling tinutukoy ng bawat lokal na kontrata. Sinisilbihan ng EUR/AZN at GBP/AZN ang mga negosyo at bisita ng Europa, habang ang TRY/AZN ay abalang pair para sa kalakalan at turismo ng Turkey, at sinusubaybayan ng RUB/AZN ang mabigat na trapiko sa pagitan ng Baku at Russia."),
    ],
    "faq": [
        ("Ano ang nangyari sa manat noong 2015?",
         "Ginawang hindi sustainable ng pagbaba ng presyo ng langis ang peg sa dolyar, at ibinaba ng bangko sentral ang manat sa dalawang malaking hakbang noong 2015 bago lumipat sa heavily managed float. Nananatiling buhay ang regime mula noon, sinusuportahan ng reserba ng state oil fund."),
        ("Nakakandado ba ang manat ng Azerbaijan sa dolyar?",
         "Oo, sa nakapirming antas, mula 2006 hanggang sa mga devaluation noong 2015. Ngayon, managed float itong nakasentro sa dolyar — bahagya lang gumalaw ang rate, ngunit patakaran iyan, hindi pormal na peg."),
        ("Magagamit ba ang manat ng Azerbaijan sa labas ng Azerbaijan?",
         "Sa praktika, hindi. Halos hindi kailanman sinasalamin ng mga foreign exchange desk ang manat. Mag-convert pagdating at palitan ang natitirang cash sa bangko o lisensyadong opisina bago umalis ng bansa."),
    ],
}

# ─────────────────────────── BDT ───────────────────────────
ARTICLES_B2["BDT"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng taka ng Bangladesh"),
        ("p", "Nakamit ng Bangladesh ang kasarinlan noong Marso 1971 matapos ang digmaan ng paghihiwalay sa Pakistan, at sa unang bahagi ng 1972 pinalitan ng bagong estado ang rupee ng Pakistan ng taka — pangalang hiniram mula sa tanka, ang lumang silver coinage ng Bengal — sa par ng pinalitan nitong currency. Nagsimulang mag-operate ang Bangladesh Bank, ang bangko sentral, sa parehong panahon."),
        ("p", "Isa sa mga pinakadakilang development run ang modernong kuwento ng taka: ginawang isa sa pinakamalalaking apparel exporter ng mundo ang Bangladesh ang mga eksport ng ready-made garment, naging haligi ng ekonomiya ang remittance ng milyun-milyong manggagawa sa abroad, at pumaitaas nang maraming taon ang foreign reserves habang nagtatayo ang bansa ng mga tulay, metro line at power plant."),
        ("p", "Dumating ang presyon noong 2022–2023, nang ubusin ng global dollar surge, import boom at mamahaling enerhiya ang reserba. Ibinaba ang taka nang paunti-unti mula sa matagal nitong managed rate, ipinataw ang mga restriksyon sa import, at pumasok sa IMF program ang Bangladesh noong 2023. Mula noon, papunta sa mas flexible, crawling-peg style na regime ang currency."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng BDT"),
        ("p", "Pinamamahalaan ang taka, at ang dalawang makina ng external na kita ng Bangladesh kasama ng import bill na kumakain dito ang malalaking driver nito."),
        ("li", "Remittance: laging kabilang ang Bangladesh sa pinakamalalaking recipient ng remittance sa mundo, na may perang dumadaloy mula sa Golpo, Malaysia, Estados Unidos at United Kingdom"),
        ("li", "Garment exports: ang ready-made clothing ang nakararami sa export earnings, kaya ang Western retail demand ang gumagalaw sa fundamentals ng currency"),
        ("li", "Ang import bill: dapat bayaran sa dolyar ang langis, cotton, pagkain at makinarya, at maaaring mabilis na ubusin ng presyo ng enerhiya ang reserba"),
        ("li", "Patakaran at reserba: ang rate management, capital control at IMF program ng Bangladesh Bank ang nagtatakda kung gaano kabilis maaaring makaangkop ang taka"),
        ("h", "Ang taka ng Bangladesh sa praktika"),
        ("p", "Cash-and-mobile-money economy ang Bangladesh. Gumagana ang card sa mga mall, hotel at mas mahusay na restaurant ng Dhaka, ngunit ang tunay na payment revolution ay ang mga mobile financial service — pinapayagan ng bKash at mga kalaban nito ang sampu-sampung milyong tao na magpadala, tumanggap at magbayad gamit ang telepono. Dapat magdala ng taka cash ang mga bisita para sa transportasyon, street food at mga palengke, at tanggihan ang bawat card terminal na nag-aalok ng singil sa sarili mong currency."),
        ("p", "Sa praktika, sarado ang taka: palitan ito sa Bangladesh at i-convert ang natira bago umalis, dahil bihirang hawakan ng mga desk sa abroad. Sa side ng pagtanggap, perang pang-buhay ang remittance — minsang nagbayad pa ang gobyerno ng cash incentive para i-channel ang mga transfer sa mga opisyal na ruta, at ang agwat sa pagitan ng bank rate at ng impormal na street rate (ang lumang hundi channel) ang maaaring magpasya kung alin ang gagamitin ng mga pamilya. Ihambing ang kabuuang taka na matatanggap, kasama ang fee at exchange margin, bago kumitil sa isang provider."),
        ("h", "Mga popular na conversion ng taka ng Bangladesh"),
        ("p", "Ang USD/BDT ang reference pair para sa kalakalan at reserba. Ang AED/BDT at SAR/BDT ang workhorse remittance pair para sa milyun-milyong manggagawang Bangladeshi sa UAE at Saudi Arabia, habang sinisilbihan ng MYR/BDT at GBP/BDT ang mga corridor ng Malaysia at United Kingdom. Mahalaga ang EUR/BDT para sa mga garment buyer at manggagawang nakabase sa EU."),
    ],
    "faq": [
        ("Bakit isa sa pinakamalalaking remittance market sa mundo ang Bangladesh?",
         "Milyun-milyong manggagawang Bangladeshi ang nakatira sa Golpo, Malaysia, UK at US, at regular nilang pinapadalhan ng pera ang tahanan. Kahalintulad ng mga merchandise export ng bansa ang mga transfer na ito bilang pinagkukunan ng foreign currency, at sumusuporta sa milyun-milyong sambahayan."),
        ("Makakakuha ba ng taka sa labas ng Bangladesh?",
         "Halos hindi kailanman. Sa praktika, saradong currency ang taka at iilang foreign exchange desk lang ang nagsa-stock nito. Magpalit ng pera sa mga bangko o lisensyadong counter sa Bangladesh, at i-convert ang hindi nagamit na taka bago bumiyahe."),
        ("Ano ang bKash?",
         "Ang bKash ang nananaig na mobile-money service ng Bangladesh, inilunsad noong 2011. Inilipat nito sa mga telepono ang payments ng bansa — mga recipient ng remittance, street vendor at kumpanya ng utility ang gumagamit nito — at madalas ito ang pinakamabilis na paraan para makatanggap ng transfer ang mga pamilya."),
    ],
}

# ─────────────────────────── ETB ───────────────────────────
ARTICLES_B2["ETB"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng birr ng Ethiopia"),
        ("p", "Ang ibig sabihin ng birr ay pilak sa wikang Amharic, at ito ang pumangalan sa mga barya — mga inapo ng Maria Theresa thaler — na umikot sa mga highland ng Ethiopia sa loob ng maraming henerasyon. Maagang inayos ng modernong Ethiopia ang pormal na banking para sa rehiyon, itinatag ang Bank of Abyssinia noong 1905, at gumamit ng currency na birr hanggang ginambala ng Italyanong pananakop noong dekada 1930 ang lahat."),
        ("p", "Matapos ang paglaya, ipinakilala ng Ethiopia ang Ethiopian dollar noong 1945 at pinalitan ang pangalan nito ng birr noong 1976. Dumaan ang currency sa panahon ng imperyo, sa mga sosyalistang taon ng Derg na nasyonalisado ang mga bangko, at sa liberalisasyon pagkatapos ng 1991 — laging isang mahigpit na kinokontrol na currency, na nag-rasyon ng foreign exchange ang National Bank of Ethiopia at dahan-dahang lumulusot na birr laban sa dolyar sa loob ng mga dekada."),
        ("p", "Ang repormang nagtakda ng landas nito ay dumating noong Hulyo 2024, nang i-float ng Ethiopia ang birr sa ilalim ng IMF-backed program, pinayagan ang merkado na magtakda ng rate. Dramatiko ang pag-aangkop — halos agad nawalan ang currency ng mga kalahati ng opisyal na halaga nito sa dolyar — ngunit nilalayon ng reporma na tapusin ang chronic na kakulangan sa foreign currency, isara ang agwat sa pagitan ng opisyal at black-market rate, at gawing competitive muli ang mga eksport."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng ETB"),
        ("p", "Sa prinsipyo, market-determined na ngayon ang birr, ngunit nananatiling manipis ang forex market ng Ethiopia, kaya ang balanse sa pagitan ng export earnings at ng import bill ang lahat."),
        ("li", "Kape, ginto at bulaklak: pinagmulan ng kape ang Ethiopia at isa sa pinakamalalaking producer ng Africa, kumpleto ng ginto at cut flowers ang malalaking export earner"),
        ("li", "Ang import bill: dapat bayaran sa hard currency ang langis, trigo, makinarya at gamot, at tinukoy ng mga shortage ang ekonomiya sa loob ng maraming taon"),
        ("li", "Implasyon: kabilang ang Ethiopia sa pinakamataas na implasyon sa mundo sa mga nakaraang taon, na patuloy na sumisira sa kapangyarihang bumili ng birr"),
        ("li", "Reform program at remittance: suporta ng IMF, mga hakbang sa liberalisasyon at malalaking transfer mula sa malaking diaspora ng Ethiopia sa Golpo, US at Europa ang humuhubog sa landas ng currency"),
        ("h", "Ang birr ng Ethiopia sa praktika"),
        ("p", "Nasa puso pa rin ng Ethiopia ang cash economy: binabayaran ng birr note ang taxi, palengke at karamihan sa mga restaurant, bagama't mabilis na kumalat ang mobile money — telebirr at mga kalaban nito — sa mga nakaraang taon. Tinatanggap ang card sa mga hotel at mas malalaking negosyo ng Addis Ababa ngunit mas kaunti sa iba pang lugar. Sa mga ATM, piliing singilin ka sa birr sa halip na tanggapin ang conversion ng terminal."),
        ("p", "Isa sa pinakamalinaw na saradong currency sa mundo ang birr: restriktibo ang pag-import at pag-export ng mga note, at halos walang exchange desk sa abroad ang hahawak nito. Mag-convert pagdating at palitan ang natira bago umalis. Para sa remittance, napakalaki ng diaspora ng Ethiopia, at sa loob ng maraming taon, itinulak ng malawak na agwat sa pagitan ng opisyal at parallel rate ang mga transfer sa mga impormal na channel — pinakipot ng float noong 2024 ang agwat na iyon at ginawang mas kaakit-akit ang mga opisyal na ruta, na eksaktong layunin ng reporma."),
        ("h", "Mga popular na conversion ng birr ng Ethiopia"),
        ("p", "Ang USD/ETB ang nag-iisang reference pair para sa kalakalan, tulong at pricing. Ang AED/ETB at SAR/ETB ang workhorse remittance pair para sa napakalaking Ethiopian workforce sa UAE at Saudi Arabia, habang sinisilbihan ng EUR/ETB ang European na tulong, kalakalan at diaspora transfer."),
    ],
    "faq": [
        ("Naco-convert ba ang birr ng Ethiopia?",
         "Hindi — sarado itong currency sa praktika. Hindi malayang mai-import o mai-export ang birr note, at bihirang mag-quote ang mga foreign desk. Magpalit sa loob ng Ethiopia at i-convert ang mga natira bago bumiyahe."),
        ("Bakit ni-float ng Ethiopia ang birr noong 2024?",
         "Maraming taon ng forex shortage, malawak na agwat sa pagitan ng opisyal at black-market rate at mabigat na implasyon ang gumawa sa lumang controlled regime na hindi na sustainable. Ang pag-float ng birr ang sentro ng IMF-backed repormang layong buhayin muli ang mga eksport at dalhin ang merkado sa liwanag."),
        ("Ano ang kasaysayan ng birr?",
         "Bumabalik ang pangalan sa silver coinage — ibig sabihin ng birr ay pilak sa wikang Amharic. Ipinakilala ng modernong Ethiopia ang Ethiopian dollar noong 1945 at pinalitan ang pangalan ng currency ng birr noong 1976; inilalabas ito ng National Bank of Ethiopia mula pa noong dekada 1960."),
    ],
}

# ─────────────────────────── GEL ───────────────────────────
ARTICLES_B2["GEL"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng lari ng Georgia"),
        ("p", "Matapos ang pagbagsak ng Sobyet, dumaan ang Georgia sa ruble ng Russia at pagkatapos sa pansamantalang coupon currency, na nakaranas ng matinding implasyon sa daan. Dumating ang lari noong 2 Oktubre 1995, pumalit sa mga coupon sa isang milyon bawat isa, at nagbigay sa batang estado ng currency na may malalim na makasaysayang alingawngaw: lumang terminong Georgian ang lari para sa pera at ari-arian, at hiram ang pangalan ng subunit nitong tetri mula sa isang medieval silver coin."),
        ("p", "Lumulutang na currency ang lari. Pinapakinis ng National Bank of Georgia ang volatility sa halip na magtakda ng antas, isang regime na nasubok nang paulit-ulit — ng digmaan sa Russia noong 2008, ng emerging-market selloff noong 2014–2015 na bumagsak nang husto sa lari, at ng tourism shutdown ng pandemya. Nanatiling mataas ang dollarization, isang legacy ng magulong dekada 1990: marami pa ring savings at loan sa Georgia ang naka-denominate sa dolyar."),
        ("p", "Nagdala ang mga taon pagkatapos ng 2020 ng kahanga-hangang baliktad. Nakabawi ang turismo, at pagkatapos ng Pebrero 2022, sinalsal ng Georgia ang malalaking inflow ng mga tao, kompanya at money transfer mula sa rehiyon, tinulungan ang lari na magsagawa ng isa sa pinakamalalakas nitong run sa loob ng maraming taon bago dahan-dahang inilabas muli ng bangko sentral."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng GEL"),
        ("p", "Currency ng maliit, bukas at serbisyong pinapatakbo na ekonomiya ang lari, kaya kasinghalaga ng fundamentals ang mga daloy."),
        ("li", "Turismo: ang mga bisita sa Tbilisi, Black Sea coast, mga bundok at wine country ay pangunahing pinagkukunan ng foreign currency, napakaseasonal"),
        ("li", "Remittance at inflow: mga transfer mula sa mga Georgian sa abroad — at ang mga along pera na dumating pagkatapos ng 2022 — ay maaaring gumalaw sa currency nang makabuluhan"),
        ("li", "Trade balance: mas malaki ang ini-import ng Georgia kaysa ini-export, bumibili mula sa Turkey, EU at mga kapitbahay habang nagbebenta ng alak, mani at re-exported na kotse"),
        ("li", "Patakaran ng National Bank: ipinagtatanggol ng interbensyon at policy rate ang lari, habang ginagawang pryoridad ng patakaran ang katatagan dahil sa dollarization ng lokal na lending"),
        ("h", "Ang lari ng Georgia sa praktika"),
        ("p", "Isa sa mga mas madaling bansa sa Caucasus para sa cashless na paglalakbay ang Georgia: gumagana ang contactless card sa halos lahat ng dako sa Tbilisi at Batumi, mula sa mga biyahe sa metro hanggang mountain guesthouse, bagama't nakakatulong pa rin ang cash sa mga nayon at palengke. Maaasahan ang mga ATM, at ang money-transfer culture ng bansa — mga storefront operator na humahawak ng cross-border remittance — isa sa pinakamakapal sa mundo."),
        ("p", "Hindi makabuluhang naco-convert ang lari sa abroad: magpalit ng pera pagdating at i-convert ang natira bago umalis. Para sa remittance, ang mga malalaking corridor ay papunta at mula sa Russia, EU, Turkey, Israel at Estados Unidos, at pinapanatili ng kompetisyon sa pagitan ng mga bangko at transfer operator ang makatwirang margen — gayunpaman, ihambing pa rin ang halagang lari na matatanggap. Para sa mga negosyo, ang dollarization ng renta at loan ay nangangahulugang tahimik na pinapamaga ng humihinang lari ang mga gastos na naka-link sa dolyar — ang dahilan kung bakit kasing-higpit na tinitingnan ng mga lokal ang USD/GEL ng anumang macro indicator."),
        ("h", "Mga popular na conversion ng lari ng Georgia"),
        ("p", "Ang USD/GEL ang reference pair para sa savings, loan at remittance. Mahalaga ang EUR/GEL para sa kalakalan ng EU at mga bisitang Europeo, habang abalang pair ang TRY/GEL salamat sa kalakalan at turismo ng Turkey, at sinusubaybayan ng RUB/GEL ang mabigat na regional na trapiko sa Russia. Sinisilbihan ng GBP/GEL ang lumalaking ugnayan sa UK sa paglalakbay at pamumuhunan."),
    ],
    "faq": [
        ("Ano ang ginamit ng Georgia bago ang lari?",
         "Matapos ang kasarinlan, gumamit ang Georgia ng ruble ng Russia, pagkatapos naglabas ng pansamantalang coupon currency mula noong 1993 sa gitna ng mataas na implasyon. Pinalitan ng lari ang mga coupon noong Oktubre 1995 sa isang milyong coupon bawat lari."),
        ("Nakakandado ba ang lari ng Georgia sa anuman?",
         "Hindi. Lumulutang ang lari, at nakikialam lamang ang National Bank of Georgia para pinisin ang labis na volatility. Nanatiling malaki ang anino ng dolyar ng US dahil marami sa mga loan at savings sa Georgia ang dollarized."),
        ("Cash o card ba ang Georgia?",
         "Pareho, nang komportable. Tinatanggap ang card at contactless payment sa halos lahat ng dako sa mga lungsod at pook panturista; magdala ng lari cash para sa mga nayon, palengke at lumang taxi."),
    ],
}

# ─────────────────────────── GHS ───────────────────────────
ARTICLES_B2["GHS"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng cedi ng Ghana"),
        ("p", "Kinuha ng cedi ang pangalan nito mula sa salitang Akan para sa cowrie shell — pera ng kalakalan sa West Africa sa loob ng mga siglo — habang ang minor unit nitong pesewa ay nag-alaala sa lumang copper coin. Dumating ang unang cedi ng Ghana noong 1965, pumalit sa Ghanaian pound dalawang taon matapos ang kasarinlan; sinundan ito ng ikalawang cedi noong 1967 pagkatapos ng pagbabago ng gobyerno, simula ng mahabang pakikibaka sa implasyon."),
        ("p", "Pagdating ng gitna ng dekada 2000, mas marami nang zero sa mga note ng cedi kaysa gustong bilangin ng sinuman. Noong Hulyo 2007, na-redenominate ng Ghana ang currency, pinutol ang apat na zero — 10,000 lumang cedi para sa isang bagong cedi — at ibinalik ang mga coin na tinaboy ng presyo mula sa paggamit. Naging isa sa pinakasinusumbing halimbawa ng malinis na redenomination sa Africa ang hakbang."),
        ("p", "Nagdala ang dekada 2020 ng mas mahirap na pagsubok. Noong 2022, kabilang ang cedi sa pinakamasasamang performing currency sa mundo, umakyat ang implasyon sa lampas limampung porsyento, at sinuspende ng Ghana ang pagbabayad sa malaking bahagi ng foreign debt nito bago pumasok sa IMF program noong 2023 at i-restructure ang mga bond. Dahan-dahan ang stabilisasyon, na ang gold reserves at fiscal discipline ang gumagawa ng karamihan sa repair."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng GHS"),
        ("p", "Lumulutang ang cedi, at ang commodity earnings, fiscal calendar at kumpiyansang manageable pa ang mga utang ng Ghana ang nagpapasya ng direksyon nito."),
        ("li", "Ginto at cocoa: isa sa mga nangungunang producer ng mundo ang Ghana sa dalawa, at ang export earnings mula rito ang nag-a-anchor sa dollar supply ng bansa — bumili pa ng ginto ang bangko sentral para magtayo ng reserba"),
        ("li", "Langis: nagdagdag ng ikatlong pangunahing export earner ang produksyon mula sa Jubilee field, naka-onstream mula noong huling bahagi ng 2010"),
        ("li", "Fiscal credibility: paulit-ulit na nagtulak sa pinakamasasamang episyode ng cedi ang spending sa election year at mga antas ng utang"),
        ("li", "Implasyon at monetary policy: ang policy rate at posisyon ng reserba ng Bank of Ghana ang nagpapasya kung gaano kalaking depensa ang nakukuha ng currency"),
        ("h", "Ang cedi ng Ghana sa praktika"),
        ("p", "Isa sa mga mobile-money pioneer ng Africa ang Ghana: hina-handle ng MTN MoMo at mga kalaban nito ang payments para sa mga street vendor, taxi at paaralan, at kaya ng bisitang may lokal na cash at may pasyang vendor na makauwi nang medyo malayo nang walang card. Tumatanggap ng card ang mga mall at hotel ng Accra, ngunit gusto ng mga palengke at tro-tro ang cedi note — maliliit ang dapat."),
        ("p", "Nae-exchange ang cedi sa mga pangunahing financial center ngunit manipis sa lahat ng iba pa; i-convert ang mga natira bago umalis, dahil bihirang mag-stock ang mga desk sa abroad. Para sa remittance, malalaki ang daloy mula sa diaspora ng Ghana sa Estados Unidos at United Kingdom, at ngayon ay inihahatid ng mga mobile-money rail ang mga transfer nang direkta sa telepono ng recipient — ihambing ang halagang cedi na matatanggap sa halip na maniwala sa zero-fee headline. Para sa mga negosyo, ginagawang hedging question ang kahit panandaliang invoicing ang volatility ng cedi sa masasamang taon."),
        ("h", "Mga popular na conversion ng cedi ng Ghana"),
        ("p", "Ang USD/GHS ang reference pair at ang numero sa likod ng bawat import invoice. Sinisilbihan ng GBP/GHS at EUR/GHS ang mga ugnayan ng kalakalan at diaspora ng Britain at Europa, habang mahalaga ang NGN/GHS para sa cross-border trade sa Nigeria, ang higanteng kapitbahay ng Ghana — at paalala na hindi maihihiwalay ng kuwento ng cedi ang kalakalan ng West Africa."),
    ],
    "faq": [
        ("Bakit na-redenominate ang cedi noong 2007?",
         "Naiwan ng mga taon ng implasyon ang lumang cedi na may napakalalaking denominasyon. Noong Hulyo 2007, tinanggal ng Ghana ang apat na zero — 10,000 lumang cedi ang naging isang bagong cedi — pinasimple ang mga presyo at ibinalik ang praktikal na coinage."),
        ("Bakit bumagsak nang husto ang cedi noong 2022?",
         "Kombinasyon ng mabigat na government debt, post-pandemic fiscal stress, lakas ng global dollar at tumataas na import cost ang nagtulak sa mga investor palabas ng cedi assets. Sinuspende ng Ghana ang external debt payments, lumampas ang implasyon sa limampung porsyento, at sinundan ng IMF program noong 2023."),
        ("Cash o mobile-money economy ba ang Ghana?",
         "Pareho, magkasamang masaya. Pangunahin ang mobile money sa pang-araw-araw na payments at umaabot nang malalim sa kanayunan, habang nananatiling mahalaga ang cash sa mga palengke at transportasyon. Pangunahing nagsisilbi ang card sa mga hotel, mall at urban na negosyo."),
    ],
}

# ─────────────────────────── KES ───────────────────────────
ARTICLES_B2["KES"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng shilling ng Kenya"),
        ("p", "Nakamit ng Kenya ang kasarinlan noong 1963, at noong 1966 inilabas ng bagong itinatag na Central Bank of Kenya ang shilling ng Kenya, pumalit sa East African shilling na nagsilbi sa Kenya, Uganda at Tanzania bilang shared currency community. Nagpatuloy nang mag-isa ang mga kapitbahay sa monetary affairs, bagama't malalapit na kamag-anak pa rin ang kanilang mga currency."),
        ("p", "Dumaan ang shilling sa mga fixed regime at exchange control papunta sa liberalized, managed float noong dekada 1990. Lumago ang Nairobi bilang business at financial hub ng East Africa, at noong 2007, ginawa ng paglulunsad ng M-Pesa — paraan ng paggalaw ng pera gamit ang mobile phone — ang Kenya bilang pinakasikat na payments laboratory sa mundo."),
        ("p", "Magulo ang kamakailang kasaysayan ng shilling: mabilis itong lumusot noong 2011, at nag-ipon muli ang presyon sa buong 2023 habang papalapit ang malaking Eurobond maturity. Bumili ng oras para sa bansa ang debt operation noong unang bahagi ng 2024, nagpatuloy ang suporta ng IMF, at nakahanap ng pagtatayuan ang currency — paalala na sa mga emerging market, kasinghalaga ng kalakalan ang debt calendar sa paggalaw ng exchange rate."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng KES"),
        ("p", "Lumulutang nang pinamamahalaan ang shilling ng Kenya, at ang klasikong East African mix ng mga eksport, turismo, pera ng diaspora at utang ang mga driver nito."),
        ("li", "Tsa, kape at horticulture: ang mga klasikong eksport ng Kenya — kabilang ang mga bulaklak na sariwang inililipad sa mga supermarket ng Europa — ang naghahatid ng tuloy-tuloy na daloy ng dolyar"),
        ("li", "Turismo: dinadala ng mga safari at ang coast ang mga bisita mula sa Europa, Americas at papalapit nang papalapit sa Asya"),
        ("li", "Remittance: ang pera mula sa mga Kenyan sa Estados Unidos, Europa at Golpo ay isa sa pinakamalalaking isahang pinagkukunan ng foreign currency ng bansa"),
        ("li", "Utang at global rates: ang mga Eurobond maturity, IMF program at US rate cycle ang humuhubog sa presyon sa shilling"),
        ("h", "Ang shilling ng Kenya sa praktika"),
        ("p", "Ang Kenya ang pinakacashless-friendly na ekonomiya sa East Africa: tinatanggap ang M-Pesa kahit saan mula sa mga supermarket ng Nairobi hanggang roadside produce stall, at halos hindi na gumagamit ng cash ang maraming Kenyan. Maaaring magbayad ng card ang mga bisita sa lungsod at hotel, ngunit mag-ingat ng shilling note para sa matatu, palengke at kanayunan — lalong tumatanggap ng app payment ang mga ride-hailing taxi, ngunit cash o mobile money lang ang minibus. Gaya ng lagi, tanggihan ang bawat card terminal na nag-aalok ng singil sa sarili mong currency."),
        ("p", "Naco-convert ang shilling sa rehiyon ng East Africa at nae-exchange sa mga pangunahing international center, bagama't mabilis na manipis ang liquidity sa labas ng London at Nairobi. Para sa remittance, malalim at kompetitibo ang mga corridor ng US at UK, at direkta sa M-Pesa wallet dumadaloy ang pera sa mga mobile-money rail — tingnan ang halagang shilling na matatanggap, dahil maaaring magtago ng malawak na margen ang zero-fee marketing. Nakakaakit pa rin ng tuloy-tuloy na investment money pabalik sa tahanan ang mga diaspora account, pagbili ng lupa at government bond na iniaalok sa mga Kenyan sa abroad. Para sa mga negosyo, ang papel ng Nairobi bilang regional hub ay ginagawang barometro ng buong East African Community ang shilling."),
        ("h", "Mga popular na conversion ng shilling ng Kenya"),
        ("p", "Ang USD/KES ang reference pair para sa kalakalan, utang at remittance. Sinisilbihan ng GBP/KES at EUR/KES ang mga ugnayan sa UK at Europa sa paglalakbay, kalakalan at diaspora, habang ang UGX/KES at TZS/KES ang praktikal na mga regional pair para sa kalakalan at paglalakbay sa loob ng East African Community."),
    ],
    "faq": [
        ("Ano ang M-Pesa?",
         "Ang M-Pesa ang mobile-money service ng Kenya, inilunsad noong 2007 ng Safaricom. Pinapayagan nitong i-store, ipadala at tanggapin ang pera gamit ang telepono, at ginagamit ito ng halos bawat Kenyan adult — mula sa pagbabayad ng matrikula hanggang sa pagtanggap ng international transfer."),
        ("Nakakandado ba ang shilling ng Kenya sa dolyar?",
         "Hindi. Lumulutang ang shilling sa pinamamahalaang regime sa ilalim ng Central Bank of Kenya, na nakikialam para pinisin ang volatility ngunit hindi nagtatanggol sa nakapirming rate."),
        ("Kailan nakuha ng Kenya ang sariling currency?",
         "Noong 1966, nang inilabas ng Central Bank of Kenya ang shilling ng Kenya para pumalit sa East African shilling na umikot sa buong Kenya, Uganda at Tanzania."),
    ],
}

# ─────────────────────────── KWD ───────────────────────────
ARTICLES_B2["KWD"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng dinar ng Kuwait"),
        ("p", "Ipinakilala ng Kuwait ang dinar noong 1961, pumalit sa Gulf rupee sa mga labintatlong rupee bawat dinar — humigit-kumulang katumbas ng halaga ng British pound noong panahong iyon. Ang minang iyan ang dahilan kung bakit, bawat isang unit, ang dinar ang pinakamataas na naka-value na currency sa mundo: kuwento ito ng denominasyon, hindi ng economic strength. Hina-handle ng Kuwaiti Currency Board ang paglulunsad, at pumalit ang Central Bank of Kuwait noong 1968."),
        ("p", "Ang pinakadramatikong kabanata ng dinar ay dumating noong 1990. Nang sakupin ng Iraq ang Kuwait, dinambong ng mga occupying force ang bangko sentral at dinala ang mga banknote. Matapos ang paglaya noong unang bahagi ng 1991, hindi pinansin ng gobyerno ang mga note na umikot sa ilalim ng occupation at naglabas ng bagong serye — isa sa mga bihirang pagkakataon na surgical na muling inilabas ang modernong currency para neutralize ang ninakaw na cash."),
        ("p", "Nakakandado ang dinar sa dolyar ng US mula 2003 hanggang 2007, pagkatapos lumipat sa hindi inihayag na basket ng mga currency — malawakang inaakalang mabigat sa dolyar — na nagpapahintulot dito na bahagyang lumutang laban sa dolyar at euro. Matagal nang tinatalakay ng Kuwait ang muling pag-peg o kahit isang Gulf monetary union, ngunit nanatili ang basket regime."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng KWD"),
        ("p", "Gaya ng mga kapitbahay nito sa Golpo, fixed regime ang pinatakbo ng Kuwait, kaya nakakabit ang kapalaran ng dinar sa kredibilidad ng peg at kalusugan ng oil economy sa likod nito."),
        ("li", "Ang currency-basket peg: mula noong 2007, sinusundan ng dinar ang hindi inihayag na basket, kaya bahagya itong gumagalaw laban sa dolyar habang gumagalaw ang iba pang basket currency"),
        ("li", "Kita sa langis: pinopondohan ng crude exports ang state budget at ang mga reserbang gumagarantiya sa peg"),
        ("li", "Ang Kuwait Investment Authority: isa sa pinakalumang at pinakamalaking sovereign wealth fund sa mundo, nagbabalik sa dekada 1950, ay structural na pinagkukunan ng national wealth"),
        ("li", "Expat labor at outflow: karamihan sa populasyon ay mga dayuhang manggagawa, kaya constant na outflow ang wage repatriation na dapat sipsipin ng peg"),
        ("h", "Ang dinar ng Kuwait sa praktika"),
        ("p", "Card-first na bansa ang Kuwait na may mataas na cost of living, at nakakatulong pa rin ang cash sa mga palengke at maliliit na carinderia. Para sa mga bisita, pareho ang praktikal na trick sa kahit saang pegged: walang kanais-nais na araw para i-convert ang dolyar, kaya mag-focus sa pagpapanatiling mababa ang fee sa halip na pag-timing sa merkado."),
        ("p", "Halos imposible ang pag-exchange ng dinar sa labas ng Kuwait — kahit mga regional desk ay magagalaw na mag-stock nito — kaya i-convert ang cash bago umalis. Para sa milyun-milyong expatriate na nagtatrabaho sa Kuwait, isa sa pinakamalalaking remittance sender sa mundo ang bansa kung ihahambing sa laki nito: napakalaki ng mga corridor sa India, Pilipinas, Egypt at Bangladesh, at tunay na makabuluhan ang pagkakaiba ng KWD margin ng mga provider sa buwanang sahod."),
        ("h", "Mga popular na conversion ng dinar ng Kuwait"),
        ("p", "Ang USD/KWD ang reference pair kahit dumadaan sa basket ang peg, at ito ang rate na mental na hinahati ng bawat expat salary. Ang INR/KWD ang pinakamalaking isahang remittance corridor, sinusundan nang malapit ng PHP/KWD, EGP/KWD at BDT/KWD. Mahalaga ang GBP/KWD at EUR/KWD para sa mga Western expatriate at negosyo."),
    ],
    "faq": [
        ("Bakit ang dinar ng Kuwait ang pinakamataas na naka-value na currency?",
         "Pinalitan ng dinar ang Gulf rupee noong 1961 sa mga labintatlong rupee bawat isang dinar, malapit sa halaga ng pound noong panahong iyon. Ang malaking unit value nito ay denominational history — walang sinasabi tungkol sa purchasing power o laki ng ekonomiya."),
        ("Nakakandado ba ang dinar ng Kuwait sa dolyar ng US?",
         "Hindi na nang direkta. Naka-dollar-peg ito mula 2003 hanggang 2007, pagkatapos lumipat sa hindi inihayag na currency basket. Lihim ang komposisyon, ngunit inaasahan ng karamihan sa mga analyst na dinodominate ng dolyar ang basket."),
        ("Nae-exchange ba ang mga dinar ng Kuwait sa abroad?",
         "Napakahirap. Iilang currency desk sa labas ng Kuwait ang nag-stock ng dinar. Palitan ang natitirang cash sa Kuwaiti bank o exchange house bago umalis ng bansa."),
    ],
}

# ─────────────────────────── KZT ───────────────────────────
ARTICLES_B2["KZT"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng tenge ng Kazakhstan"),
        ("p", "Unang Central Asian republic ng dating Soviet Union ang Kazakhstan na naglunsad ng sariling currency, ipinakilala ang tenge noong 15 Nobyembre 1993 para pumalit sa ruble ng Russia. Nagbabahagi ang pangalan ng sinaunang Turkic root sa mismong salitang Russian para sa pera — paalala kung gaano kalalim ang mga trading tradition ng rehiyon."),
        ("p", "Kasabay ng oil boom ang unang dalawang dekada ng tenge: lumago ang Kazakhstan bilang isa sa mga makabuluhang crude exporter sa mundo, naiipon ng National Bank ang reserba, at sa loob ng maraming taon, na-trade ang tenge sa managed range laban sa dolyar. Tinapos iyan ng pagbagsak ng presyo ng langis noong 2014–2015: matapos ang devaluation, ni-float ang tenge noong Agosto 2015 at lumipat ang bangko sentral sa inflation targeting."),
        ("p", "Magulo ang mga nakaraang taon — civil unrest noong Enero 2022, spillover mula sa digmaan sa Ukraine, at inflation spike na pumilit sa National Bank na agresibong magtaas. Sa kabuuan, nanatiling pinakaliquid na currency ng rehiyon ang tenge, may gumaganang merkado at malalim na reserba sa likod nito."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng KZT"),
        ("p", "Floating commodity currency ang tenge na naipit sa pagitan ng dalawang higanteng kapitbahay, at sinasalamin ng mga driver nito ang heograpiyang iyon."),
        ("li", "Presyo ng langis at commodity: dinodominate ng crude oil, uranium at metal ang mga eksport ng Kazakhstan, kaya ang presyo nila ang nagtutulak sa supply ng hard currency"),
        ("li", "Patakaran ng National Bank: hinuhubog ng interbensyon, policy rate at pag-iipon ng reserba ang landas ng tenge sa ilalim ng managed float"),
        ("li", "Kalakalan sa Russia at China: ang mga swing ng ruble, yuan settlement at re-routing ng regional trade ay dumadaloy nang direkta sa mga merkado ng Kazakh"),
        ("li", "Implasyon at geopolitics: gumagalaw sa currency at sa mga rate na nagtatanggol dito ang regional risk premium at domestic na presyon sa presyo"),
        ("h", "Ang tenge ng Kazakhstan sa praktika"),
        ("p", "Kapansin-pansing digital ang Kazakhstan: dinodominate ng Kaspi super-app ang payments at shopping, gumagana ang card sa halos lahat ng dako sa Almaty at Astana, at pinakamahalaga ang cash sa mga rural na lugar at bazaar. Maaaring mag-withdraw ng tenge ang mga bisita mula sa bank ATM at dapat palaging piliing singilin sa KZT sa halip na tanggapin ang conversion ng terminal."),
        ("p", "Mahirap i-exchange ang tenge sa labas ng dating Soviet space — iilang Western desk ang nag-stock nito — kaya i-convert ang natitirang cash bago umalis. Kung magpapatuloy ng biyahe sa mga kapitbahay na bansa, magplano nang maingat ng cash: madalas dumaan sa dolyar sa praktika ang pagpapalit ng tenge sa Kyrgyz som o iba pang regional currency, at karaniwang tatalo ng bazaar exchange rate ang mga board ng bangko. Para sa negosyo, kumikita ng dolyar ang mga exporter habang nagbabayad ng sahod sa tenge, kaya ginawang normal na bahagi ng Kazakh corporate life ang hedging ng float noong 2015. Makabuluhan ang remittance flow sa Russia, Kyrgyzstan at Uzbekistan, at halos gabing naidagdag ng sampu-sampung libong taong lumipat sa Kazakhstan noong 2022 ang mga bagong corridor."),
        ("h", "Mga popular na conversion ng tenge ng Kazakhstan"),
        ("p", "Ang USD/KZT ang reference pair at pangunahing gauge ng kalusugan ng currency. Sinisilbihan ng EUR/KZT at GBP/KZT ang European trade at mga biyahero, habang ang RUB/KZT ang pair na mahalaga sa napakalaking cross-border trade sa Russia, at lumaki ang CNY/KZT kasama ng Chinese investment at mga Belt-and-Road corridor."),
    ],
    "faq": [
        ("Nakakandado ba ang tenge ng Kazakhstan sa dolyar?",
         "Hindi. Matagal nang nakakandado ang Kazakhstan ngunit ni-float ang tenge noong Agosto 2015 matapos ang pagbagsak ng presyo ng langis. Pinapakinis pa rin ng National Bank ang volatility, kaya managed float ito sa halip na malaya."),
        ("Bakit bumagsak nang mabilis ang tenge noong 2015?",
         "Pinutol ng pagbaba ng presyo ng langis ang dollar income ng bansa, at naging unsustainable ang pagtatanggol sa lumang peg. Matapos ang devaluation, hinayaan ng bangko sentral na itakda ng merkado ang rate at lumipat sa inflation targeting."),
        ("Kailan ipinakilala ang tenge?",
         "Noong 15 Nobyembre 1993, pumalit sa ruble ng Russia — unang Central Asian na dating Soviet republic ang Kazakhstan na naglabas ng sariling currency."),
    ],
}

# ─────────────────────────── LKR ───────────────────────────
ARTICLES_B2["LKR"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng rupee ng Sri Lanka"),
        ("p", "Nagpatibay ang Ceylon ng desimal na rupee ng 100 sentimo noong dekada 1870, pumalit sa mas lumang coinage ng rixdollar at pera ng panahon ng British. Matapos ang kasarinlan noong 1948, itinatag ang Central Bank of Ceylon noong 1949 at kinuha nito ang paglalabas ng note; pinalitan ng bansa ang pangalan nito ng Sri Lanka noong 1972 at nagpatuloy ang currency."),
        ("p", "Gumugol ang rupee ng mga dekada sa fixed at managed regime bago ito nag-liberalize sa managed float noong unang bahagi ng dekada 1990. Pinigilan ng mahabang civil war mula 1983 hanggang 2009 ang ekonomiya, at pinalaya ng kapayapaan ang tourism boom — hinalaw ng mga beach, hill country at sinaunang lungsod ang mga bisita mula sa Europa, India at East Asia."),
        ("p", "Pagkatapos dumating ang 2022, pinakamasamang krisis mula noong kasarinlan: naubos ang reserba ng debt service, sinuspende ng gobyerno ang pagbabayad sa external debt nito, at mabilis na ni-float ang rupee noong Marso 2022 matapos ang mga taon ng paghawak sa artipisyal na antas. Sinundan ng mga shortage ng langis, gamot at pagkain, at sinimulan ng IMF program na inayos noong 2023 ang mahabang proseso ng debt restructuring at pagtatayo muli ng reserba."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng LKR"),
        ("p", "Managed float ang rupee ng Sri Lanka na pinapasya ng kakayahan ng bansa na kumita ng foreign currency at magbayad ng mga utang nito."),
        ("li", "Turismo: pangunahing earner ang arrivals ng bisita, at ipinakita ng mga shock tulad ng 2019 Easter attacks at pandemya kung gaano kabilis mawawala ang kita na iyon"),
        ("li", "Remittance: nagpapadala ng pera sa tahanan ang mga manggagawang Sri Lankan sa Golpo at iba pa, at umaangat-lumulubog ang bahaging dumadaan sa opisyal na channel kasama ng inalok na exchange rate"),
        ("li", "Tsa, garment at rubber: pondo ng klasikong export trio ang malaking bahagi ng mga import"),
        ("li", "Utang at reserba: higit sa anumang pang-araw-araw na data, ang mga sovereign debt payment, IMF review at antas ng reserba ang nagtutulak sa expectations ng merkado"),
        ("h", "Ang rupee ng Sri Lanka sa praktika"),
        ("p", "Nananatiling cash-heavy na ekonomiya ang Sri Lanka: gustong-gusto ng tuk-tuk, bus, palengke at maliliit na restaurant ang rupee, habang gumagana ang card sa mga mall ng Colombo at tourist hotel. Saradong currency ang rupee sa abroad — palitan ito pagdating at i-convert ang natira bago lumipad palabas, dahil halos walang foreign bank ang tatanggap nito pabalik."),
        ("p", "Para sa remittance, nagturo ng mahirap na aral ang mga taon ng krisis: nang maging napakahuli ng opisyal na rate sa street rate, lumipat ang mga transfer sa mga impormal na channel at bumagsak ang opisyal na inflow. Mula noong float, mas kompetitibo nang husto ang mga opisyal na channel, at aktibong nililigawan ng mga bangko at money-transfer operator ang Gulf corridor. Gaya ng lagi, ihambing ang kabuuang rupee na matatanggap bawat unit na naipadala — hindi kasunduan ang zero-fee offer na may masamang rate. Para sa mga manlalakbay, mabilis na inangkop ang mga presyo matapos ang devaluation, kaya muling suriin ang mga gastos sa halip na maniwala sa mas lumang guidebook."),
        ("h", "Mga popular na conversion ng rupee ng Sri Lanka"),
        ("p", "Ang USD/LKR ang reference pair at ang numero na tinitingnan ng bawat importer at remitter. Sinisilbihan ng GBP/LKR at AUD/LKR ang malalaking diaspora community sa United Kingdom at Australya, habang dinadala ng AED/LKR at SAR/LKR ang Gulf worker corridor. Kumpleto ng EUR/LKR ang European side ng paglalakbay at kalakalan."),
    ],
    "faq": [
        ("Bakit bumagsak ang rupee ng Sri Lanka noong 2022?",
         "Naubos ng debt service ang reserba habang lumubog ang turismo at remittance, naiwan ang bansang hindi makabayad sa mga import. Sinuspende ng gobyerno ang external debt payments at ni-float ang rupee na matagal nang hawak sa overvalued na managed rate — mabilis ang pag-aangkop."),
        ("Nakakandado ba ang rupee ng Sri Lanka sa dolyar?",
         "Hindi. Matapos ang mga taon ng mahigpit na pamamahala, ni-float ang rupee noong Marso 2022 at ngayon ay tinatrado sa managed float sa ilalim ng Central Bank of Sri Lanka, sinusuportahan ng IMF program."),
        ("Nae-exchange ba ang rupee ng Sri Lanka sa labas ng Sri Lanka?",
         "Bihira. Saradong currency ang rupee sa abroad na halos walang liquidity. Mag-convert sa rupee pagdating at palitan ang natitirang cash bago umalis ng bansa."),
    ],
}

# ─────────────────────────── MAD ───────────────────────────
ARTICLES_B2["MAD"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng dirham ng Morocco"),
        ("p", "Sinauna ang pangalan ng dirham — naglakbay ito mula sa Greek drachma papunta sa Arabic at naging isa sa mga standard coin ng maagang Islamic world. Ipinakilala ang modernong dirham ng Morocco noong 1960, pumalit sa Moroccan franc na naiwan mula sa panahon ng protectorate, na inilalabas ng Bank al-Maghrib, ang bangko sentral na itinatag noong 1959."),
        ("p", "Laging pinamamahalaang currency ang dirham. Nakabat ito sa French franc sa loob ng mga dekada at, sa pamamagitan ng link na iyon, sa euro; noong 2015, lumipat ang Morocco sa basket ng euro at dolyar ng US, at pinalawak ng bangko sentral ang fluctuation band nang paunti-unti bilang bahagi ng dahan-dahang liberalisasyon. Malaking bahagi naco-convert ang mga current-account na transaksyon, ngunit kinokontrol pa rin ang mga capital-account flow."),
        ("p", "Angkop ang disenyo sa ekonomiyang hinihila sa pagitan ng Europa at ng natitirang bahagi ng mundo: dinodominate ng France at Spain ang kalakalan, dumarating ang milyun-milyong turista mula sa EU, at nagpapadala ng ilan sa pinakamalalaking remittance flow sa Africa ang Moroccan diaspora sa France, Spain, Italy at mga Benelux na bansa."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng MAD"),
        ("p", "Hindi malayang lumulutang ang dirham, kaya ang mga ekonomiya sa likod ng peg at ang bilis ng sariling liberalisasyon ng Morocco ang mga driver nito."),
        ("li", "Ang euro link: dinodominate ng Europa ang kalakalan ng Morocco, kaya ang EUR share ng basket ang pinakamahalaga para sa mga exporter at importer"),
        ("li", "Turismo at remittance: milyun-milyong bisita at malaking diaspora ang nagpapadala ng foreign currency na nagpopondo sa import bill"),
        ("li", "Phosphate at industriya: isa sa mga nangungunang phosphate exporter ng mundo ang Morocco at nagtayo ng seryosong automotive at aerospace manufacturing para sa mga kliyenteng Europeo"),
        ("li", "Drought at agrikultura: gumagalaw sa rural income at food import ang mga rain-fed anihan, at maaasahang bumigat sa ekonomiya ang mga taon ng kaunting ulan"),
        ("h", "Ang dirham ng Morocco sa praktika"),
        ("p", "Gumagana ang Morocco sa cash sa mga lugar na pinakamamahal ng mga manlalakbay — medina, souk, grand taxi at roadside café — habang maayos na gumagana ang card at contactless sa mga lungsod, hotel at mas malalaking restaurant. Magdala ng maliliit na note: pagtalo sa souk na may malaking denomination ang pagkalugiag na opening move, at bihirang may sukli ang mga vendor."),
        ("p", "Opisyal na saradong currency ang dirham: may mga limitasyon sa kung magkano ang mai-import o mai-export, at mahigpit ang export side. Palitan ang natitirang dirham sa lisensyadong opisina bago umalis — iko-convert ng airport desk ang mga ito, hindi ibibigay ng mga street tout ang rate na sulit kunin. Napakalaki at kompetitibo ng remittance flow mula sa diaspora: magkakaiba ang epektibong rate na naka-quote ng mga bangko, transfer specialist at cash network, kaya ihambing ang halagang dirham na talagang matatanggap."),
        ("h", "Mga popular na conversion ng dirham ng Morocco"),
        ("p", "Ang EUR/MAD ang pair na mahalaga — karamihan sa kalakalan, turismo at pera ng diaspora ng Morocco ang gumagalaw laban sa euro. Sinisilbihan ng USD/MAD at GBP/MAD ang mga manlalakbay at negosyo ng America at Britain, habang sinasalamin ng CAD/MAD ang lumalaking komunidad ng Morocco sa Canada. Sa loob ng Morocco, laging tingnan kung ginagamit ng euro price tag ang sariling kanais-nais na conversion ng merchant."),
    ],
    "faq": [
        ("Nakakandado ba ang dirham ng Morocco?",
         "Oo. Pinamamahalaan ang dirham laban sa basket ng euro at dolyar ng US (mula noong 2015; bago nito, epektibong euro at French franc), at dahan-dahang pinalalawak ang fluctuation band habang ginagawang mas malaya ng Bank al-Maghrib ang regime."),
        ("Maaari ba akong magdala ng dirham ng Morocco palabas ng bansa?",
         "Sa loob lang ng mga limitasyon — opisyal na saradong currency ang dirham at restriktibo ang pag-export nito. I-convert ang natitirang note sa lisensyadong exchange office bago bumiyahe, at mag-ingat ng resibo kung plano mong palitan pabalik ang anumang hindi nagamit na dirham."),
        ("Dapat ba akong magbayad ng euro sa Morocco?",
         "Hindi. Maaaring mag-quote ng euro ang ilang hotel at tourist shop, ngunit karaniwang masama ang mga conversion rate nila. Magbayad sa dirham, o sa card na naka-billing sa dirham, at tanggihan ang anumang terminal offer na i-convert sa sarili mong currency sa checkout."),
    ],
}

# ─────────────────────────── QAR ───────────────────────────
ARTICLES_B2["QAR"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng riyal ng Qatar"),
        ("p", "Bago ang riyal, gumamit ang Qatar ng rupee ng India at pagkatapos ng Gulf rupee kasama ng mga kapitbahay nito. Noong 1966, nagtatag ng joint currency board ang Qatar at ang katabing emirato ng Dubai at naglabas ng shared na riyal; nang sumali ang Dubai sa United Arab Emirates noong 1971, nagpatuloy nang mag-isa ang Qatar, at inilalabas ng Qatar Monetary Agency — ang Qatar Central Bank ngayon, itinatag noong 1993 — ang riyal ng Qatar mula noong 1973."),
        ("p", "Gaya ng karamihan sa mga currency sa Golpo, fixed-rate currency ang riyal. Matapos ang mas maagang mga peg sa special drawing right at currency basket, nakakandado ng Qatar ang riyal sa dolyar ng US sa mga 3.64 riyal bawat dolyar mula noong 2001. Sinubok ang peg sa panahon ng Gulf diplomatic blockade noong 2017–2021, nang maikling nagduda ang ilang counterparty na pananatilihin nito — nanatili ito, sinusuportahan ng napakalaking foreign reserve at kita ng liquefied natural gas."),
        ("p", "Isa sa mga nangungunang LNG exporter sa mundo ang Qatar, at ang hydrocarbon revenue ang nagpapagana sa state budget, Qatar Investment Authority at banking system bilang mga pangunahing demand center ng currency. Iyon ang dahilan kung bakit kayang patakbuhin ng maliit na peninsula ang fixed rate sa mga oil-price cycle na lumulubog sa iba pang currency."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng QAR"),
        ("p", "Sa naka-andar na dollar peg, epektibong derivative ng dolyar ng US ang riyal — ang kagiliw-giliw na tanong ay laging ang kredibilidad ng peg, hindi ang pang-araw-araw na rate."),
        ("li", "Ang dollar peg: pinapanatili ng Qatar Central Bank ang riyal sa mga 3.64 bawat dolyar ng US, kaya gumagalaw lang ang QAR kapag gumagalaw ang iba pang currency laban sa dolyar"),
        ("li", "Hydrocarbon revenue: nagpopondo sa budget, reserba at sovereign wealth fund ang kita ng LNG at langis na nakatayo sa likod ng peg"),
        ("li", "Lakas ng reserba at kredibilidad: ang malalim na foreign reserve at kalusugan ng banking system ang nagpapahintulot sa peg na makaligtas sa mga political shock"),
        ("li", "Regional politics: ipinakita ng blockade noong 2017–2021 na maaaring maikling pindutin ang currency ng sentiment ng investor sa Qatar, hindi lang ang ekonomiya"),
        ("h", "Ang riyal ng Qatar sa praktika"),
        ("p", "Napakacard-friendly ng Doha — tinatanggap ang contactless payment sa hotel, mall, taxi at karamihan sa mga restaurant — ngunit mag-ingat ng riyal cash para sa mga souq, maliit na cafeteria at mas lumang taxi driver. Mahal ang Qatar ayon sa mga regional na pamantayan, at walang hedging game na paglalaruan sa dolyar dahil sa nakapirming peg; kung ano ang rate, iyon ito."),
        ("p", "Sa labas ng Golpo, mahirap i-exchange ang riyal. Bihirang nag-stock ang mga currency desk sa Europa o Asia nito, kaya i-convert ang mga natitirang note bago lumipad pabalik sa tahanan. Sa loob ng Qatar, karamihan sa mga residente ay expatriate, at ilan sa pinakamalalaking remittance flow sa mundo kada tao ang ipinapadala ng bansa palabas — malalim at kompetitibo ang mga corridor sa India, Pilipinas, Nepal, Bangladesh at Egypt, kaya tunay na pera ang halaga ng paghahambing ng kabuuang matatanggap."),
        ("h", "Mga popular na conversion ng riyal ng Qatar"),
        ("p", "Naka-fix ang USD/QAR sa mga 3.64, ginagawa itong boring pero essential na reference ng lahat ng naka-price sa dolyar. Ang INR/QAR at PHP/QAR ang nagsisilbi sa dalawa sa pinakamalalaking expat remittance corridor, at ang BDT/QAR at NPR/QAR ay mga pangunahing ruta ng South Asia. Ang EUR/QAR at GBP/QAR ang praktikal na mga pair para sa mga manlalakbay at negosyong Europeo."),
    ],
    "faq": [
        ("Nakakandado ba ang riyal ng Qatar sa dolyar?",
         "Oo. Nakakandado ng Qatar ang riyal sa dolyar ng US sa mga 3.64 bawat dolyar mula noong 2001, matapos ang mas maagang mga peg sa special drawing right at currency basket. Nanatili ang peg sa buong regional blockade noong 2017–2021."),
        ("Maaari ba akong gumastos ng dolyar ng US sa Qatar?",
         "Maaaring mag-quote ng presyo sa dolyar ang ilang hotel at malalaking tindahan, ngunit karaniwang bumabalik ang sukli sa riyal at bihirang pabor sa iyo ang kinakaltas na rate. Magbayad sa riyal, o sa card, at hayaan ang network na hawakan ang anumang conversion."),
        ("Bakit napakastable ng rate ng riyal?",
         "Ang nakapirming peg, malalaking reserba at nangungunang kita sa LNG ang gumagawa sa QAR na isa sa pinakastable na currency sa mundo. Ang stable na rate ay pinili ng patakaran, hindi senyales na natutulog ang merkado."),
    ],
}

# ─────────────────────────── TZS ───────────────────────────
ARTICLES_B2["TZS"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng shilling ng Tanzania"),
        ("p", "Ipinanganak ang Tanzania noong 1964 mula sa union ng Tanganyika at Zanzibar, at noong 1966 inilabas ng Bank of Tanzania ang shilling ng Tanzania, pumalit sa East African shilling na binabahagi sa Kenya at Uganda. Bagong bansa, bagong currency — ngunit pamilyar na mukha para sa sinumang nangalakal sa East Africa."),
        ("p", "Hinubog ng sosyalistang Ujamaa experiment na inilunsad kasama ang Arusha Declaration noong 1967 ang mga unang dekada ng shilling: nasyonalisado ang mga bangko, pinatakbo ng estado ang ekonomiya, at mahigpit na pinamahalaan ang currency. Itinayong muli ng liberalisasyon mula gitna ng dekada 1980 ang market economy, at tinatrado ang shilling sa managed float mula noong dekada 1990."),
        ("p", "Nakasandal ang modernong Tanzania sa ginto — pinakamalaking export nito — kasama ng cashew, kape at gemstone na tanzanite, na halos hindi matatagpuan sa ibang lugar sa mundo. Haligi ang turismo: hinihila ng Serengeti, Kilimanjaro at mga beach ng Zanzibar ang mga bisita mula sa bawat kontinente, at nangangako pa ang mga offshore gas discovery. Sa buong 2023 at 2024, pinindot ang shilling ng import demand, at pinahigpit ng Bank of Tanzania ang patakaran para ito ay pumatag."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng TZS"),
        ("p", "Lumulutang ang shilling sa ilalim ng pamamahala, at ang mga eksport, turista at import ng ekonomiyang bumubuo pa ng industrial base nito ang mga driver."),
        ("li", "Export ng ginto at agrikultura: dinodominate ng ginto, cashew at kape ang merchandise earnings, kaya direkta ang pagpasok ng world commodity price sa currency"),
        ("li", "Turismo: nagdadala ng seasonal foreign exchange ang mga park sa mainland at Zanzibar, nakakumpol sa high season"),
        ("li", "Import at ang port: dapat bayaran sa dolyar ang langis, makinarya at consumer goods, at nagsisilbi rin sa mga landlocked na kapitbahay ang port ng Dar es Salaam, nagdaragdag ng regional demand"),
        ("li", "Patakaran ng Bank of Tanzania: pumatag sa shilling sa loob ng managed float nito ang mga desisyon sa rate, interbensyon at reserve management"),
        ("h", "Ang shilling ng Tanzania sa praktika"),
        ("p", "Cash-first ang Tanzania sa labas ng mga lungsod nito: gumagana sa shilling note ang mga palengke, dala-dala minibus, street food at karamihan sa guesthouse ng Zanzibar. Gayunpaman, nasa lahat ng dako ang mobile money — sinasalamin ng M-Pesa ng Vodacom at mga kalaban nito ang tagumpay ng Kenya — at gumagana ang card sa mga hotel, lodge at urban na restaurant. Sa mga national park at ferry office, madalas dumaan sa card machine o opisyal na app ang payments, ngunit nag-iiba ang pagiging maaasahan, kaya magdala ng backup cash. Magdala din ng mas maliliit na note; chronic na problema ang sukli sa mga stall ng palengke."),
        ("p", "Sa praktika, saradong currency ang shilling: halos walang exchange desk sa abroad ang nag-stock nito, kaya mag-convert pagdating at palitan ang natira bago umalis. Para sa remittance, mas maliit ang mga flow ng Tanzania kaysa sa Kenya ngunit lumalago, dumarating mula sa Estados Unidos, Europa at Golpo, madalas direkta sa mobile wallet. Para sa mga negosyo at safari operator, karaniwang naka-quote sa dolyar ang pricing habang sa shilling binabayaran ang mga gastos, kaya live na isyu ng margen ang exchange rate — at ang mga park fee, kitang-kita na naka-lista sa dolyar, naaayos sa pamamagitan ng parehong conversion."),
        ("h", "Mga popular na conversion ng shilling ng Tanzania"),
        ("p", "Ang USD/TZS ang reference pair para sa turismo, import at port economy. Sinisilbihan ng EUR/TZS at GBP/TZS ang mga manlalakbay na Europeo at aid-linked flow, habang ang KES/TZS ang pangunahing regional pair para sa kalakalan at paglalakbay sa loob ng East African Community."),
    ],
    "faq": [
        ("Kailan ipinakilala ang shilling ng Tanzania?",
         "Noong 1966, nang inilabas ito ng Bank of Tanzania para pumalit sa East African shilling, dalawang taon matapos pagsamahin ng Tanganyika at Zanzibar ang kanilang sarili upang mabuo ang Tanzania."),
        ("Nakakandado ba ang shilling ng Tanzania?",
         "Hindi. Tinatrado ang shilling sa managed float, na pinapakinis ng Bank of Tanzania ang volatility sa halip na ipagtanggol ang nakapirming antas."),
        ("Maaari ba akong gumamit ng dolyar ng US sa Tanzania?",
         "Bahagya. Naka-quote sa dolyar ang mga park fee, safari at ilang presyo ng lodge, ngunit kailangan ng shilling ang pang-araw-araw na pagbabayad, at karaniwang masamang conversion rate ang pagbabayad nang lokal sa dolyar. Magdala ng shilling cash para sa mga palengke at transportasyon."),
    ],
}

# ─────────────────────────── UAH ───────────────────────────
ARTICLES_B2["UAH"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng hryvnia ng Ukraine"),
        ("p", "Kinukuha ng hryvnia ang pangalan nito mula sa currency ng medieval Kyivan Rus, kung saan ang hryvnia ay unit ng timbang at pagbabayad sa pilak. Dumating ang modernong bersyon noong Setyembre 1996, nang pinalitan ng National Bank of Ukraine ang pansamantalang karbovanets coupon sa mga humigit-kumulang 100,000 lumang unit bawat isang hryvnia, tinapos ang isa sa pinakamatalim na implasyon ng mga post-Soviet na taon sa halos isang gabi."),
        ("p", "Maagang nasubok ang batang currency. Pinutol ng conflict sa Russia noong 2014–2015 ang halaga ng hryvnia sa dolyar nang humigit-kumulang dalawang-katlo at pumilit sa National Bank na itaas ang interest rate, higpitan ang capital flow at tanggapin ang suporta ng IMF. Mula noon, lumipat na ang National Bank sa inflation targeting at mas flexible na exchange rate, dahan-dahang muling binubuo ang reserves at kredibilidad."),
        ("p", "Nagdala ng pinakamahirap na pagsubok ang full-scale invasion noong 2022: hawak ng National Bank ang exchange rate sa nakapirming antas, may cap sa mga withdrawal at cross-border transfer, at pinanatiling gumagana ang payment system sa gitna ng mga strike sa infrastructure. Habang pinahihintulutan ng mga kondisyon, nagluluwang ang bangko sa mga kontrol at bumalik sa mas pinamamahalaang flexible na rate, sinusuportahan ng IMF lending at malalaking transfer mula sa mga Ukrainian sa abroad."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng UAH"),
        ("p", "Pinamamahalaang currency ang hryvnia: ang National Bank of Ukraine, hindi ang merkado, ang huling salita sa rate, lalo na sa panahon ng digmaan."),
        ("li", "Digmaan at seguridad: dinodominate ng mga military development, strike sa energy infrastructure at kabuuang kurso ng conflict ang lahat ng iba pa tungkol sa currency"),
        ("li", "Capital control at patakaran ng NBU: humuhubog sa opisyal na rate ang key policy rate, mga limitasyon sa paglipat ng pera sa abroad at direkta na interbensyon"),
        ("li", "IMF program at reserba: sinusuportahan ng international financing at antas ng foreign reserve ang kumpiyansa sa hryvnia"),
        ("li", "Kalakalan at remittance: sinasalamin ng mga export ng grain, metal at pagkain ang import ng langis at enerhiya, habang nagpapadala ng hard currency ang mga transfer mula sa mga manggagawang Ukrainian — lalo na sa EU"),
        ("h", "Ang hryvnia ng Ukraine sa praktika"),
        ("p", "Sa loob ng Ukraine, karaniwan ang card at phone payment kahit sa mga maliliit na merchant, at maaasahan ang mga ATM sa mga lungsod, bagama't maaaring mabigo ang mga network sa power outage — backup na cash ang dala ng lahat. Magdala ng dolyar o euro sa malilinis na note para i-exchange sa lisensyadong desk kung kinakailangan, at laging magbayad sa hryvnia: walang tinutulungan ang merchant na nag-quote ng dolyar."),
        ("p", "Sa praktika, saradong currency ang hryvnia sa abroad. Sa labas ng Ukraine at iilang kapitbahay na exchange market, iilang desk ang mag-quote nito, kaya planuhing gastusin o i-convert ang cash bago umalis ng bansa. Tingnan ang mga kasalukuyang patakaran ng National Bank bago maglakbay, dahil paulit-ulit na nagbago ang mga limitasyon sa pag-import at pag-export ng cash mula noong 2022."),
        ("p", "Para sa remittance, isa sa pinakamalalaking recipient sa Europa ang Ukraine sa mga nakaraang taon, na tumatanggap ng pera mula sa mga manggagawa sa Poland, Germany, Czech Republic at iba pa. Dinodominate ng mga lisensyadong transfer system at bangko; ihambing ang kabuuang halagang hryvnia na matatanggap, dahil malawakang nag-iiba ang fee at exchange margin. Nakaharap sa mga settlement rule ng National Bank ang mga negosyo para sa mga trade payment, kaya kailangan ng mga export at import contract ang kasalukuyang regulatory advice sa halip na mga lumang template."),
        ("h", "Mga popular na conversion ng hryvnia ng Ukraine"),
        ("p", "Ang USD/UAH ang reference pair at price anchor ng mga nag-iipon at importer, habang mahalaga ang EUR/UAH para sa kalakalan sa EU. Ang PLN/UAH ang isa sa pinakamahahalagang pair sa rehiyon: milyun-milyong Ukrainian ang naninirahan at nagtatrabaho sa Poland, at ginawa ng displacement mula noong 2022 ang core remittance corridor nito. Sinisilbihan ng GBP/UAH at CAD/UAH ang mas malawak na Ukrainian diaspora."),
    ],
    "faq": [
        ("Nae-exchange ba ang hryvnia ng Ukraine sa labas ng Ukraine?",
         "Bihira lang. Manipis ang liquidity sa labas ng Ukraine at iilang kapitbahay na merkado, at bihirang nag-stock ang mga bangko sa iba pa. I-convert ang cash sa hryvnia pagdating at pabalik bago umalis, sinusuri ang mga kasalukuyang limitasyon ng National Bank of Ukraine."),
        ("Bakit kinokontrol ang exchange rate ng UAH?",
         "Pinamamahalaan ng National Bank ang rate para iprotektahan ang reserba at panatilihing stable ang mga presyo at payment system — una matapos ang 2014 at mas mahigpit pa mula noong 2022. Nailuwag ang mga restriksyon nang paunti-unti habang pinahihintulutan ng mga kondisyon."),
        ("Dapat ba akong magdala ng cash sa Ukraine?",
         "Magdala ng kaunti. Malawakang tinatanggap ang card at phone payment sa mga lungsod, ngunit ginagawang makatuwirang backup ang hryvnia cash — kasama ang maliit na reserba ng dolyar o euro — ang power outage, rural na lugar at maliliit na palengke."),
    ],
}

# ─────────────────────────── XAF ───────────────────────────
ARTICLES_B2["XAF"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng CFA franc ng Central Africa"),
        ("p", "Ipinanganak ang CFA franc ng Central Africa kasabay ng kanluraning kambal nito: nilikha noong 26 Disyembre 1945, ang araw na iniratipika ng France ang mga Bretton Woods agreement, bilang bahagi ng colonial currency architecture. Sinilbihan ng sangang ito ang French Equatorial Africa at Cameroon, at mula noong unang bahagi ng dekada 1970, inilalabas ito ng Bank of Central African States (BEAC), nakahimpil sa Yaoundé."),
        ("p", "Anim na bansa ang gumagamit nito: Cameroon, Central African Republic, Chad, Republic of the Congo, Equatorial Guinea at Gabon. Sumali ang Equatorial Guinea, dating kolonya ng Spain, noong 1985. Nag-ebolb mula sa French franc papunta sa euro ang peg na nagtatakda ng currency, sa parehong nakapirming rate ng kanluraning bersyon — 655.957 CFA franc bawat euro — at magkasamang gumagalaw ang dalawang sangang ito mula noon, kasama ang overnight na 50 porsyentong devaluation noong 1994."),
        ("p", "Ang ginagawang natatangi ng Central African zone ay ang economic base nito: dinodominate ng langis, mga producer ang Gabon, Congo, Chad at Equatorial Guinea habang pinapatakbo ng Cameroon ang pinakamalaking diversified economy ng rehiyon at gateway port nito. Simbolo ng katotohanan ng zone ang Chad–Cameroon pipeline na binuksan noong 2003 — umaagos ang hydrocarbon, at madalas dadaan sa Douala ang lahat ng iba pa."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng XAF"),
        ("p", "Gaya ng kanluraning franc, inaayos ng euro peg ang headline rate; ang totoong kuwento ay ang oil-and-timber economy sa likod nito."),
        ("li", "Presyo ng langis: dinodominate ng crude export mula sa Gabon, Congo, Chad at Equatorial Guinea ang foreign-exchange earnings ng zone, kaya mas mahalaga ang energy market kaysa sa anuman"),
        ("li", "Ang euro peg: sinusundan ng XAF ang euro laban sa dolyar at lahat ng iba pa nang eksaktong 655.957 bawat euro"),
        ("li", "BEAC at reserve framework: sinusuportahan ng pooled reserve at operations-account arrangement sa French Treasury ang kredibilidad ng peg"),
        ("li", "Regional corridor: nakadepende sa mga ruta sa pamamagitan ng Cameroon ang landlocked na Chad at Central African Republic, kaya kasinghalaga ng produksyon ang trade logistics sa paghubog sa dollar supply ng zone"),
        ("h", "Ang CFA franc ng Central Africa sa praktika"),
        ("p", "Parehong note at coin ang umiikot sa lahat ng anim na bansa, ginagawang kapwa-simple ang paglalakbay sa pagitan ng Yaoundé, Libreville at Brazzaville — walang internal na exchange, walang paghahanap ng rate sa mga border. Gumagana ang card sa mga bangko, hotel at supermarket ng mga lungsod, ngunit cash-heavy pa rin ang rehiyon: magdala ng maliliit na denominasyon para sa mga palengke, taxi at mas maliliit na bayan."),
        ("p", "Limitado ang convertibility sa labas ng rehiyon, kaya palitan ang natitirang franc bago umalis — halos hindi kailanman nag-stock ang mga desk sa abroad ng XAF. Isang praktikal na pagkakaiba: sa ilang member state, maaaring harapin ng mga bangko ang periodic shortage ng foreign currency, kaya ang malalaking dollar payment ay madalas nangangailangan ng planning at pasensya. Para sa remittance, pangunahing corridor ang mga flow mula sa France, bagama't mas maliit kaysa sa mga kanluraning Africa; sulit pa rin ang paghahambing ng halagang CFA na matatanggap, dahil malawakang nag-iiba ang bank margin sa zone. Para sa mga negosyo, tinatanggal ng fixed euro link ang currency risk sa mga European contract ngunit nagdadala ng lakas o kahinaan ng euro sa lahat ng naka-price sa dolyar."),
        ("h", "Mga popular na conversion ng CFA franc ng Central Africa"),
        ("p", "Ang EUR/XAF ang defining pair, naka-fix ng peg sa 655.957. Ang USD/XAF ang aktwal na tinitingnan ng mga oil company at commodity trader, sinisilbihan ng GBP/XAF ang mga British at international business link, at ang XAF/XOF — parity sa disenyo — mahalaga kapag gumagalaw ang pera sa pagitan ng dalawang CFA zone."),
    ],
    "faq": [
        ("Ano ang pagkakaiba ng XAF at XOF?",
         "Dalawang sangang bahagi ng parehong sistema ang mga ito, inilalabas ng iba't ibang bangko sentral para sa iba't ibang rehiyon: XAF ng BEAC para sa anim na bansa ng Central Africa, XOF ng BCEAO para sa walong bansa ng West Africa. Parehong nakakandado sa euro sa parehong rate at may parehong halaga, ngunit magkahiwalay ang mga banknote."),
        ("Maaari ba akong gumamit ng CFA franc ng West Africa sa Central Africa?",
         "Magkaiba ang mga note at magkahiwalay ang mga zone sa legal, kaya huwag umasa dito — maaaring tanggapin ng mga bangko ang note ng ibang zone sa par ngunit walang obligasyon. Direkta ang exchange sa pagitan ng dalawa sa loob ng rehiyon."),
        ("Nakakandado ba ang CFA franc ng Central Africa sa euro?",
         "Oo, sa 655.957 CFA franc bawat euro — parehong nakapirming rate ng CFA franc ng West Africa. Bago ang euro, parehong nakakandado sa French franc ang dalawang sangang ito, at nakaligtas ang parity sa ilang muling pagdidisenyo ng sistema."),
    ],
}

# ─────────────────────────── XOF ───────────────────────────
ARTICLES_B2["XOF"] = {
    "sections": [
        ("h", "Maikling kasaysayan ng CFA franc ng West Africa"),
        ("p", "Ipinanganak ang CFA franc noong 26 Disyembre 1945 — ang araw na iniratipika ng France ang mga Bretton Woods agreement — bilang franc ng mga kolonyang Africa ng France, currency na nilikha para ihiwalay ang mga colonial economy mula sa sariling postwar devaluation ng France. Muling ginamit ang pangalan nang may diplomasya para mangahulugang franc ng Financial Community of Africa, ngunit mas matatanda ang buto ng sistema kaysa sa karamihan ng member state nito."),
        ("p", "Ngayon, inilalabas ang CFA franc ng West Africa ng Central Bank of West African States (BCEAO), nakahimpil sa Dakar, para sa walong bansa: Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Senegal at Togo. Sumali ang Guinea-Bissau, dating kolonya ng Portugal, noong 1997. Nakakandado ang currency sa euro — at bago nito sa French franc — sa nakapirming rate na 655.957 CFA franc bawat euro mula noong 1999, nakaligtas kahit sa 1994 na desisyon na hatiin overnight ang halaga nito laban sa French franc."),
        ("p", "May kasamang French connection ang arrangement na nagtatakda ng politika nito: pinagsasama ng mga member state ang reserba at kasaysayang nagpanatili ng operations account sa French Treasury. Nilalayon ng mga repormang inanunsyo sa huling bahagi ng 2019 na tapusin ang centralization ng reserba sa France at muling i-brand ang currency bilang eco, at inaprubahan ng mga member state ang mga pagbabago noong 2020 — ngunit paulit-ulit na lumusot ang transisyon, at higit sa isang beses nang naipagpaliban ang mas malawak na single-currency project ng ECOWAS, naiiwan ang CFA franc na matibay na umiikot."),
        ("h", "Ano ang nagpapagalaw sa exchange rate ng XOF"),
        ("p", "Laban sa euro, walang gumagalaw — iyon ang layunin ng peg. Ang mga pwersang pumipindot sa mismong peg ang kagiliw-giliw na ekonomiya."),
        ("li", "Ang euro peg: eksaktong 655.957 CFA franc ang binibili ng isang euro, kaya umaangat-lumulubog ang XOF kasama ng euro laban sa dolyar at iba pang currency"),
        ("li", "Cocoa at commodity export: pinakamalaking cocoa producer sa mundo ang Côte d'Ivoire, at ang ginto, cotton at langis mula sa rehiyon ang nagtutulak sa foreign-exchange supply"),
        ("li", "Ang garantiya ng French Treasury: nagbibigay sa peg ng bihirang kredibilidad ang pooled reserve at garantiya — sa halaga ng monetary flexibility, ang core ng matagalang debate tungkol sa currency"),
        ("li", "Mga regional reform plan: hinuhubog ng eco project at mga reporma noong 2019–2020 ang mga expectation tungkol sa tawag sa currency na ito sa loob ng sampung taon"),
        ("h", "Ang CFA franc ng West Africa sa praktika"),
        ("p", "Para sa mga manlalakbay, napakakombenyente ng eight-country zone: gumagana ang parehong banknote mula Dakar hanggang Cotonou hanggang Abidjan, walang exchange sa mga internal na border at walang exchange-rate risk sa pagitan ng mga member. Stable ang mga presyo ayon sa mga regional na pamantayan — ini-import ng peg ang European-style price discipline, at kasaysayang mas mababa ang inflation sa zone kaysa sa mga kapitbahay na may floating currency."),
        ("p", "Naco-convert ang CFA franc laban sa euro sa pamamagitan ng banking system ngunit manipis ang trading sa iba pa, kaya i-convert ang mga natira bago umalis sa rehiyon. Mabilis na digital ang pang-araw-araw na buhay: dinodominate ng mga mobile money service tulad ng Orange Money at Wave ang pang-araw-araw na payments sa Senegal at Côte d'Ivoire. Para sa remittance, ang mga malalaking corridor ay mula sa France, na may malaking West African diaspora, at pinapanatili ng kompetisyon sa pagitan ng mga bangko at transfer operator ang presyon sa fee — ihambing ang halagang CFA na matatanggap, hindi ang ina-advertise na komisyon."),
        ("h", "Mga popular na conversion ng CFA franc ng West Africa"),
        ("p", "Naka-fix ang EUR/XOF — ang peg — at ang numero na nakasulat sa paligid ng bawat regional na kontrata. Mahalaga ang USD/XOF para sa mga commodity buyer at dollar invoicing, sinisilbihan ng GBP/XOF ang British connection, at ang NGN/XOF ang praktikal na pair para sa kalakalan sa Nigerian border, kung saan nagtatagpo ang dalawang napakaibang monetary philosophy."),
    ],
    "faq": [
        ("Nakakandado ba ang CFA franc ng West Africa sa euro?",
         "Oo, sa nakapirming rate na 655.957 CFA franc bawat euro, parity na minana mula sa peg sa French franc noong 1999. Nakaligtas ang peg sa maraming krisis, sinusuportahan ng pooled reserve at garantiya ng French Treasury."),
        ("Aling mga bansa ang gumagamit ng XOF?",
         "Walong bansa sa West Africa: Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Senegal at Togo. Gumagamit ang anim na bansa ng Central Africa ng magkahiwalay ngunit kaparehong halagang XAF, inilalabas ng ibang bangko sentral."),
        ("Ano ang eco?",
         "Ang eco ang planadong currency na dapat magpatuloy mula sa CFA franc bilang bahagi ng mga monetary reform ng West Africa. Inanunsyo noong 2019 at inaprubahan ng mga member state noong 2020, paulit-ulit na naipagpaliban ang transisyon, at nananatiling ginagamit ang CFA franc habang umuunlad ang single-currency project ng rehiyon."),
    ],
}
