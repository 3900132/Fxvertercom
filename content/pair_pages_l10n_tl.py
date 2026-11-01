# -*- coding: utf-8 -*-
"""Filipino (tl) currency-pair page copy (flat structure, like the other l10n files)."""

PAIR_UI_L10N = {'pairConvert': 'Live na converter',
 'pairRateHead': 'Kasalukuyang exchange rate',
 'pairAsOf': 'Reference rate noong {d}. Laging pinakabagong rate ang kinukuha ng live converter sa '
             'itaas — ang mga tablea sa ibaba ay snapshot sa oras ng build para sa orientasyon.',
 'pairAmounts': 'Mga karaniwang halaga: {f} patungong {t}',
 'pairReverse': 'Mga karaniwang halaga: {t} patungong {f}',
 'pairMore': 'Iba pang conversion ng {f}',
 'pairMorePairs': 'Iba pang currency pair',
 'pairIntroHead': 'Tungkol sa exchange rate ng {f} patungong {t}',
 'pairCurLinks': 'Mga pahina ng currency',
 'pairMetaTmpl': 'I-convert ang {f} patungong {t} nang may live exchange rates: ang {f}/{t} rate '
                 'ngayon, libreng kalkulator, mga tablea ng karaniwang halaga at kung ano ang '
                 'nagpapagalaw sa currency pair na ito.'}

PAIR_CONTENT_L10N = {'USD-EUR': {'title': 'USD patungong EUR — exchange rate ngayon, libreng converter at tablea ng '
                      'halaga',
             'description': 'I-convert ang dolyar ng US sa euro nang may live rates: ang USD/EUR '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at kung ano ang '
                            'nagpapagalaw sa pair.',
             'h1': 'USD patungong EUR — i-convert ang dolyar ng US sa euro',
             'intro': ['Ang USD/EUR ang pinakamalakas nang tinatrabahong currency pair sa mundo — '
                       'humigit-kumulang isang-kaapat ng buong foreign-exchange turnover — kaya '
                       'ito ang may pinakamakipot na spread at pinakamalalim na merkado sa lahat '
                       'ng conversion. Ang rate ay simpleng presyo ng isang dolyar ng US sa euro, '
                       'patuloy na itinatakda ng global na kalakalan, mga daloy ng pamumuhunan at '
                       'interest-rate gap sa pagitan ng Federal Reserve at European Central Bank.',
                       'Para sa pang-araw-araw na conversion, ang praktikal na tanong ay kung '
                       'magkano ang margin na binabayaran mo sa itaas ng mid-market rate na '
                       'ipinapakita rito. Karaniwang nagdaragdag ang mga bangko ng 1–4 porsyento; '
                       'malawakang nag-iiba ang mga card at transfer service. Ang pag-check ng '
                       'live rate bago bumili o mag-transfer ay agad nagsasabi kung patas ang '
                       'quote.'],
             'faq': [('Paano tinutukoy ang USD papuntang EUR exchange rate?',
                      'Malayang lumulutang ito — ang supply at demand sa dalawang currency ang '
                      'nagtatakda ng presyo sa buong araw, naiimpluwensyahan pangunahin ng '
                      'interest-rate policy ng Fed at ECB, implasyon sa magkabilang panig ng '
                      'Atlantic at global na risk sentiment. Walang nakapirming o pinamamahalaang '
                      'target.'),
                     ('Kailan ang pinakamagandang panahon para i-convert ang USD sa EUR?',
                      'Pinakamalalim ang liquidity at pinakamakipot ang spread sa panahon ng '
                      'overlap ng European at US trading hours (mga 13:00–17:00 UTC). Walang '
                      'nakapagpapredict nang maaasahan sa panandaliang direksyon, kaya para sa '
                      'malalaking halaga, mas ligtas ang pag-convert nang paunti-unti kaysa '
                      'maghintay ng mas magandang araw.')]},
 'USD-GBP': {'title': 'USD patungong GBP — exchange rate ngayon, libreng converter at ang kwento '
                      'ng cable',
             'description': 'I-convert ang dolyar ng US sa pound sterling nang may live rates: ang '
                            'USD/GBP rate ngayon, libreng kalkulator, tablea ng halaga at ang '
                            'kwento ng cable.',
             'h1': 'USD patungong GBP — i-convert ang dolyar ng US sa pound sterling',
             'intro': ['Ang rate sa pagitan ng dolyar at pound, pinangalanan ng mga trader na '
                       '‘cable’ matapos ang transatlantic telegraph cable na unang nagdala nito '
                       'noong dekada 1860, isa sa pinakalumang patuloy na naka-quote na exchange '
                       'rate sa mundo. Ngayon, sinasalamin nito ang interest-rate gap sa pagitan '
                       'ng Federal Reserve at Bank of England, implasyon ng UK at kalusugan ng '
                       'kalakalan at piskal na posisyon ng Britain.',
                       'Pinakamabilis na tinatrado ang sterling sa panahon ng London, at may '
                       'tendensyang matalim gumalaw ang pair sa paligid ng UK economic data at '
                       'fiscal announcement. Ang paghahambing ng anumang quote sa mid-market rate '
                       'sa ibaba ang pinakamabilis na paraan para makita kung magkano ang margin '
                       'na kinukuha ng provider.'],
             'faq': [('Bakit mas mataas ang halaga ng pound sterling kaysa dolyar ng US?',
                      'Ang mas mataas na presyo kada unit ay hindi nangangahulugan ng mas malakas '
                      'na ekonomiya — kasaysayan at denominasyon ang salamin nito. Dominanteng '
                      'currency ang pound noong panahong wala pa ang dolyar; walang sinasabi ang '
                      'numero mismo tungkol sa relatibong lakas ng ekonomiya o purchasing power.'),
                     ('Ano ang pinakamalaking gumagalaw sa USD/GBP?',
                      'Mga desisyon sa interest rate mula sa Fed at Bank of England, mga ulat ng '
                      'implasyon ng UK, at mga balitang pampulitika o piskal mula sa Westminster. '
                      'Sa Brexit vote noong 2016, bumagsak ang pound ng mga 10 porsyento sa isang '
                      'araw — paalala na may political risk ang sterling na wala sa karamihan ng '
                      'pangunahing currency.')]},
 'USD-JPY': {'title': 'USD patungong JPY — exchange rate ngayon, libreng converter at gabay sa yen',
             'description': 'I-convert ang dolyar ng US sa yen ng Hapon nang live: ang USD/JPY '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at kung ano ang '
                            'nagpapagalaw sa yen.',
             'h1': 'USD patungong JPY — i-convert ang dolyar ng US sa yen ng Hapon',
             'intro': ['Ang USD/JPY ang pangalawang pinakamalakas nang tinatrabahong currency pair '
                       'sa mundo at klasikong barometro ng interest-rate gap sa pagitan ng Estados '
                       'Unidos at Hapon. Dahil ilang dekadang halos zero ang mga rate ng Hapon, '
                       'naging paboritong funding currency ng mundo ang yen — humihina ito kapag '
                       'kumpiyansa ang mga merkado at mabilis na lumalakas kapag iwinawasak ng mga '
                       'krisis ang mga posisyong iyon.',
                       'Tinitingnan din ang pair para sa opisyal na interbensyon ng Hapon: '
                       'paulit-ulit na bumili ng yen ang Ministry of Finance kapag masyado nang '
                       'mabilis humina ito. Ang pinakamabuting gawin sa malalaking conversion ay '
                       'i-check ito laban sa mid-market rate, dahil maaaring mapanlinlang ang '
                       'lapad ng retail margin sa JPY.'],
             'faq': [('Bakit minsan bumabagsak nang husto ang yen laban sa dolyar?',
                      'Pangunahin dahil sa interest-rate gap. Kapag mataas ang mga rate ng US at '
                      'halos zero ang mga rate ng Hapon, nagbebenta ang mga investor ng yen para '
                      'bumili ng mas mataas na yield na dollar asset — ang carry trade. Maaaring '
                      'lumusot ang yen nang mga buwan, pagkatapos mabilis na tumalon kapag '
                      'iniiwasak ang mga trade na iyon.'),
                     ('Maaari bang baguhin ng gobyerno ng Hapon ang USD/JPY rate?',
                      'Maaari itong umasa laban sa merkado, hindi ito baliktarin. Nakikialam ang '
                      'Hapon sa pagbili o pagbebenta ng yen kapag nagiging magulo ang mga galaw, '
                      'kung minsan na may sampu-sampung bilyong dolyar sa isang episyode. '
                      'Pinapakinis ng interbensyon ang daan; bihira nitong binabago ang '
                      'pangmatagalang direksyon na itinatakda ng fundamentals.')]},
 'USD-CNY': {'title': 'USD patungong CNY — exchange rate ngayon, libreng converter at ang managed '
                      'na rate',
             'description': 'I-convert ang dolyar ng US sa yuan ng Tsina nang may live rates: ang '
                            'USD/CNY rate ngayon, libreng kalkulator, tablea ng halaga at ang '
                            'managed na rate nito.',
             'h1': 'USD patungong CNY — i-convert ang dolyar ng US sa yuan ng Tsina',
             'intro': ['Ang rate sa pagitan ng dolyar at yuan ang pinakamalaking currency pair na '
                       "pinamamahalaan ng central bank. Tuwing umaga, nagtatakda ang People's Bank "
                       'of China ng araw-araw na fixing, at pinapayagan lang ang onshore rate '
                       "(CNY) na gumalaw sa loob ng band sa paligid nito — kaya't kakaunti lang "
                       'ang ginagalaw ng USD/CNY araw-araw kaysa sa ipinahihiwatig ng economic '
                       'importance nito.',
                       'Hinuhubog ng trade surplus ng Tsina, mga capital control at mga layunin ng '
                       'patakaran ang rate. Para sa mga conversion, tandaang maaaring bahagyang '
                       'magkaiba ang onshore CNY at offshore CNH, at napapailalim sa '
                       'capital-control rules ang indibidwal na currency conversion sa Tsina. '
                       'Laging ihambing ang mga quote sa reference rate sa ibaba.'],
             'faq': [('Malayang naco-convert ba ang yuan ng Tsina?',
                      'Hindi nang buo. Madali ang trade-related na conversion, ngunit kinokontrol '
                      'ng mga quota at approval ang mga investment flow sa ibayo ng hangganan. '
                      "Kaya't bahagyang magkaiba ang presyo ng offshore na bersyon (CNH) sa "
                      'onshore CNY — ang agwat ay sumasalamin kung magkano ang gastos ng paglipat '
                      'ng pera sa ibayo ng border.'),
                     ('Bakit bihira gumalaw ang USD/CNY kumpara sa ibang pair?',
                      'Dahil pinamamahalaan ito ng central bank. Pinapanatili ng araw-araw na '
                      'fixing at trading band ang rate nang stable laban sa dolyar, ayon sa '
                      'preferensya ng Tsina sa predictability sa kalakalan. Hindi nangangahulugang '
                      'naka-fix ang pinamamahalaan: nakasunod pa rin ang rate sa fundamentals sa '
                      'loob ng mga buwan at taon.')]},
 'USD-INR': {'title': 'USD patungong INR — exchange rate ngayon, libreng converter at gabay sa '
                      'rupee',
             'description': 'I-convert ang dolyar ng US sa rupee ng India nang live: ang USD/INR '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at ang galaw ng '
                            'rupee.',
             'h1': 'USD patungong INR — i-convert ang dolyar ng US sa rupee ng India',
             'intro': ['Ang USD/INR ay isa sa pinakamahahalagang remittance corridor sa mundo — '
                       'mas maraming remittance ang natatanggap ng India kaysa anumang bansa — at '
                       'isang mabigat na tinatrabahong emerging-market pair. Pinamamahalaan ng '
                       'Reserve Bank of India ang volatility sa halip na ang antas: pinapakinis '
                       'nito ang mga matalim na galaw gamit ang reserba nito ngunit hinahayaang '
                       'hanapin ng rupee ang pangmatagalang trend nito.',
                       'Ang pangmatagalang kuwento ng rupee ay dahan-dahang depreciation laban sa '
                       'dolyar, tinutulak ng inflation differential at current-account balance ng '
                       'India, napuputol ng mga global risk event. Para sa sinumang nagpapadala ng '
                       'pera sa India, sa agwat sa pagitan ng mid-market rate at inalok na rate '
                       'nakatago ang tunay na gastos.'],
             'faq': [('Bakit bumababa ang halaga ng rupee ng India sa paglipas ng panahon?',
                      'Pangunahin ang inflation differential at trade deficit: mas malaki ang '
                      'ini-import ng India kaysa ini-export, at pinopondohan ng capital inflow ang '
                      'pagkakaiba. Pinapakinis ng RBI ang daan, ngunit sa loob ng mga dekada, '
                      'dahan-dahang humina ang rupee laban sa dolyar — normal ito para sa umuunlad '
                      'na ekonomiya.'),
                     ('Paano ako makakakuha ng pinakamagandang rate sa pagpapadala ng pera sa '
                      'India?',
                      'Ihambing ang inalok na rate sa mid-market rate bago magpadala, hindi lang '
                      'ang mga fee. Karaniwang tatalo ng mga specialised remittance service ang '
                      'bank wire sa corridor na ito, at makabuluhan ang pagkakaiba na 1 porsyento '
                      'sa regular na pamilyang transfer sa loob ng isang taon.')]},
 'USD-CAD': {'title': 'USD patungong CAD — exchange rate ngayon, libreng converter at ang galaw ng '
                      'loonie',
             'description': 'I-convert ang dolyar ng US sa dolyar ng Canada nang live: ang USD/CAD '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at ang galaw ng '
                            'loonie.',
             'h1': 'USD patungong CAD — i-convert ang dolyar ng US sa dolyar ng Canada',
             'intro': ['Ang USD/CAD — ‘loonie’ — ay top-five na global currency pair na nakabatay '
                       'sa isa sa pinakamalalaking trading relationship sa mundo. Ipinapadala ng '
                       'Canada ang mga tatlong-kaapat ng mga eksport nito sa Estados Unidos, kaya '
                       'mabigat na tinatrado ang pair sa US growth, presyo ng enerhiya '
                       '(pangunahing oil exporter ang Canada) at rate gap sa pagitan ng Fed at '
                       'Bank of Canada.',
                       'Kapag tumataas ang langis, karaniwang lumalakas ang CAD; kapag tumatama '
                       'ang takot sa global growth, humihina ito kasama ng mga commodity currency '
                       'sa pangkalahatan. Liquid ang pair sa buong araw, at madaling makahanap ng '
                       'mga quote sa loob ng bahagi ng isang porsyento ng mid-market rate — kaya '
                       'laging sulit tanungin ang malawak na margin.'],
             'faq': [('Bakit loonie ang tawag sa dolyar ng Canada?',
                      'Mula sa loon — ang ibon sa barya ng isang dolyar na ipinakilala noong 1987. '
                      'Naidikit ang palayaw at ngayon ay tumutukoy na sa mismong currency sa FX '
                      'slang, tulad ng ‘lumakas ang loonie ngayong araw’.'),
                     ('Totoo bang nakakaapekto ang presyo ng langis sa USD/CAD?',
                      'Oo, kitang-kita. Ang crude oil at mga kaugnay na produkto ang '
                      'pinakamalaking export category ng Canada, kaya ang tumataas na langis ay '
                      'may tendensyang magdala ng mas maraming dolyar sa Canada at itaas ang CAD. '
                      'Itinatrato ng mga trader ang pair bilang magaspang na pagtaya sa energy '
                      'market pati na rin sa interest rate ng dalawang bansa.')]},
 'USD-AUD': {'title': 'USD patungong AUD — exchange rate ngayon, libreng converter at ang '
                      'commodity currency',
             'description': 'I-convert ang dolyar ng US sa dolyar ng Australya nang live: ang '
                            'USD/AUD rate ngayon, libreng kalkulator, tablea ng halaga at ang '
                            'commodity currency.',
             'h1': 'USD patungong AUD — i-convert ang dolyar ng US sa dolyar ng Australya',
             'intro': ['Ang dolyar ng Australya ang klasikong commodity currency: nakadikit sa '
                       'iron ore, coal at gas export ang kapalaran nito, at higit sa lahat sa '
                       "demand ng Tsina sa mga ito. Kaya't isa sa pinakamalinaw na real-time "
                       'indicator ng global risk appetite ang USD/AUD — lumalakas ang Aussie kapag '
                       'boom ang world trade at humihina sa mga risk-off na episyode.',
                       'Ang interest-rate policy ng Reserve Bank of Australia at ng Fed ang '
                       'nagtutulak sa mas maiikling swing. Ginagawang karaniwang paulit-ulit na '
                       'conversion ang USD→AUD (at pabalik) ng mga working-holiday at student '
                       'population ng Australya, kung saan mabilis na sumasama ang kahit 1 '
                       'porsyentong rate margin.'],
             'faq': [('Bakit napakasensitibo ng dolyar ng Australya sa Tsina?',
                      'Malayo ang pinakamalaking export market ng Australya — ang Tsina — lalo na '
                      'sa iron ore na ginagamit sa steelmaking. Kapag lumamig ang construction ng '
                      'Tsina, karaniwang sabay na bumabagsak ang commodity prices at AUD — '
                      'real-time barometro ng heavy industry ng Tsina ang currency.'),
                     ('Safe haven ba ang AUD?',
                      'Ang kabaliktaran: risk-on currency ang tawag ng mga trader dito. Sa mga '
                      'global paniko — 2008, 2020 — umaagos ang pera sa dolyar ng US at karaniwang '
                      'pinakamabilis na bumabagsak sa mga pangunahing currency ang Aussie. Ang '
                      'cyclicality na iyon ang eksaktong dahilan kung bakit sobrang bantay ng mga '
                      'carry trader at growth watcher dito.')]},
 'USD-CHF': {'title': 'USD patungong CHF — exchange rate ngayon, libreng converter at ang safe '
                      'haven na franko',
             'description': 'I-convert ang dolyar ng US sa franko ng Suwisa nang live: ang USD/CHF '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at ang galaw ng '
                            'franko.',
             'h1': 'USD patungong CHF — i-convert ang dolyar ng US sa franko ng Suwisa',
             'intro': ['Ang franko ng Suwisa ang premier safe-haven currency ng mundo: kapag '
                       'tumama ang digmaan, banking stress o market panic, umaagos ang pera sa '
                       "Suwisa at lumalakas ang CHF. Kaya't may tendensyang bumaba ang USD/CHF sa "
                       'mga global crisis kahit ang dolyar mismo ay kanlungan — simple, ang franko '
                       'ang mas malakas na kanlungan.',
                       'Aktibong huhubog ng Swiss National Bank ang rate, mula sa bantog na euro '
                       'floor noong 2011–2015 hanggang mabigat na interbensyon mula noon. Para sa '
                       'mga conversion, paalala rin ng Suwisa na maaari pa ring malawak ang retail '
                       'margin ng mayayamang bansang pair, lalo na sa airport at hotel — laging '
                       'tingnan ang mid-market reference.'],
             'faq': [('Bakit itinuturing na safe haven ang franko ng Suwisa?',
                      'Isang siglo ng neutralidad, mababang utang, current-account surplus at '
                      'kapani-paniwalang central bank ang gumagawa sa franko bilang default '
                      'parking place ng perang tumatakas sa risk. Napakababa rin ng implasyon ng '
                      'Suwisa kumpara sa US at eurozone sa loob ng mga dekada, pumipanatili ng '
                      'purchasing power ng currency.'),
                     ('Ano ang ginawa ng SNB noong Enero 2015?',
                      'Bigla nitong tinalikuran ang cap sa lakas ng franko laban sa euro. Bumagsak '
                      'ang USD/CHF at EUR/CHF ng mga 20–30 porsyento sa loob ng mga minuto — isa '
                      'sa pinakamalalaking intra-day move sa isang pangunahing pair — at ang '
                      'dahilan kung bakit iginagalang pa rin ng mga trader ang phrase na ‘SNB '
                      'risk’.')]},
 'USD-MXN': {'title': 'USD patungong MXN — exchange rate ngayon, libreng converter at gabay sa '
                      'peso ng Mexico',
             'description': 'I-convert ang dolyar ng US sa peso ng Mexico nang live: ang USD/MXN '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at kung ano ang '
                            'nagpapagalaw sa peso.',
             'h1': 'USD patungong MXN — i-convert ang dolyar ng US sa peso ng Mexico',
             'intro': ['Ang USD/MXN ang pinakamalakas nang tinatrabahong emerging-market currency '
                       'pair sa Americas at isa sa pinakaliquid sa mundo. Sa lahat ng gumagalaw sa '
                       'ekonomiya ng US tumitrado ang peso — trade policy, growth, interest-rate '
                       'gap sa pagitan ng Fed at Banxico — pati na rin ang presyo ng langis at ang '
                       'napakalaking remittance corridor mula sa Estados Unidos.',
                       'Dahil sobrang liquid nito, mabilis gumalaw ang pair sa global risk '
                       'sentiment: klasikong carry-trade target na lumalakas sa kalmadong merkado '
                       'at mabilis na bumabagsak sa mga paniko. Para sa mga manlalakbay at '
                       'remittance sender, karaniwan ang margin na 3–6 porsyento sa mga airport — '
                       'ang mid-market rate sa ibaba ang benchmark na ihahambing.'],
             'faq': [('Bakit napakavolatile ng USD/MXN?',
                      'Inaakit ng mataas na interest rate sa Mexico ang panandaliang carry money '
                      'na mabilis umalis sa stress; ang peso rin ang reference asset ng lahat ng '
                      'kalakalan at political news sa pagitan ng US at Mexico. Ginagawa ng '
                      'kombinasyon itong liquid ngunit madaling tumalon — normal ang malalaking '
                      'galaw kada araw, hindi malfunction.'),
                     ('Ano ang pinakamurang paraan ng pagpapadala ng dolyar sa Mexico?',
                      'Palaging tatalo ng mga specialised remittance service ang mga bangko at '
                      'cash-transfer storefront sa corridor na ito. Ihambing ang halagang '
                      'dumarating sa mid-market rate: sa 300-dolyar na transfer, ang pagkakaiba ng '
                      'patas na quote at 5 porsyentong margin ay maaaring isang buong araw na '
                      'sahod sa lugar.')]},
 'USD-PHP': {'title': 'USD patungong PHP — exchange rate ngayon, libreng converter at gabay sa '
                      'remittance ng OFW',
             'description': 'I-convert ang dolyar ng US sa piso ng Pilipinas nang live: ang '
                            'USD/PHP rate ngayon, libreng kalkulator, tablea ng halaga at ang '
                            'papel ng remittance ng OFW.',
             'h1': 'USD patungong PHP — i-convert ang dolyar ng US sa piso ng Pilipinas',
             'intro': ['Naka-angkla ang piso ng Pilipinas sa isa sa pinakamalalaking remittance '
                       'flow sa mundo: milyun-milyong overseas Filipino worker ang nagpapadala ng '
                       'pera sa tahanan, at ang mga dollar inflow na iyon ay haligi ng ekonomiya. '
                       'Tumitrado naman ang USD/PHP sa global risk appetite, presyo ng langis (net '
                       'importer ang Pilipinas) at patakaran ng Bangko Sentral ng Pilipinas.',
                       'Pinamamahalaan nang magaan ang opisyal na rate — pinapayagan ng central '
                       'bank ang dahan-dahang pag-aangkop habang pinipisin ang mga spike. Para sa '
                       'mga pamilyang OFW at manlalakbay, malawak ang spread ng mga provider sa '
                       'corridor na ito, kaya ang pag-check ng mid-market rate bago magpadala ang '
                       'pinakamadaling paraan para makatipid.'],
             'faq': [('Paano nakakaapekto ang remittance sa piso ng Pilipinas?',
                      'Sinusuportahan ng tuloy-tuloy na dollar inflow mula sa mga overseas worker '
                      'ang piso at balance of payments ng bansa — ilang porsyento ng GDP bawat '
                      'taon. Kapag tumataas ang global risk o humihina ang mga host economy, '
                      'lumalambot ang remittance at sinasamahan ito ng piso.'),
                     ('Mas mabuti bang mag-convert ng USD sa PHP sa US o sa Pilipinas?',
                      'Nakadepende sa provider, hindi sa bansa. May mga murang at mamahaling '
                      'opsyon sa magkabilang panig ng corridor; ang napagpasyahang numero ay kung '
                      'ilang piso ang talagang matatanggap ng recipient. Ihambing ang mga quote sa '
                      'mid-market rate sa halip na maniwala sa pinakamalapit na tindahan.')]},
 'EUR-GBP': {'title': 'EUR patungong GBP — exchange rate ngayon, libreng converter at ang European '
                      'cross',
             'description': 'I-convert ang euro sa pound sterling nang may live rates: ang EUR/GBP '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at ang European '
                            'cross.',
             'h1': 'EUR patungong GBP — i-convert ang euro sa pound sterling',
             'intro': ['Ang EUR/GBP ang klasikong European cross: dalawang ekonomiyang nagpapadala '
                       "ng mga kalahati ng kalakalan nila sa isa't isa, pinaghihiwalay lang ng "
                       'isang currency border. Dahil pareho silang developed at mababang-implasyon '
                       'na currency, mas malayo ang ginagalaw ng pair kaysa mga dollar cross — '
                       'talagang pagtaya sa relatibong kapalaran ng eurozone at UK.',
                       'Karamihan sa trend ay tinutulak ng interest-rate gap sa pagitan ng ECB at '
                       'Bank of England, habang nagbibigay ng mga spike ang UK political at fiscal '
                       'news. Para sa mga cross-channel worker, pensioner at negosyo, ginagawang '
                       'mas mahalaga ang maliliit na pagkakaiba ng rate ng katatagan ng pair: '
                       'malaking bahagi ng kabuuang taunang galaw ang 1 porsyentong margin.'],
             'faq': [('Bakit mas tahimik ang EUR/GBP kaysa EUR/USD?',
                      'Wala sa dalawa ang global risk currency, kaya binabalewala ng worldwide '
                      'flight-to-safety flow ang mga ito. Karamihan sa pair ay sumasalamin sa '
                      'UK–EU relatibong ekonomiya at rate differential na mabagal magbago — '
                      "bagama't maaari itong tumalon nang mabilis sa British political news, gaya "
                      'ng ipinakita noong 2016.'),
                     ('Paano nakakaapekto pa rin ng Brexit ang EUR/GBP?',
                      'Istraktural. Ginawang bahagyang mas sarado ng mga bagong trade friction '
                      'mula noong 2021 ang ekonomiya ng UK sa EU, na ikinokonekta ng karamihan sa '
                      'mga economist sa istraktural na mas mahinang sterling. Bawat round ng UK–EU '
                      'negotiation sa trade rules ay gumagalaw pa rin sa pair hanggang ngayon.')]},
 'EUR-CHF': {'title': 'EUR patungong CHF — exchange rate ngayon, libreng converter at ang papel ng '
                      'SNB',
             'description': 'I-convert ang euro sa franko ng Suwisa nang may live rates: ang '
                            'EUR/CHF rate ngayon, libreng kalkulator, tablea ng halaga at ang '
                            'papel ng SNB sa pair na ito.',
             'h1': 'EUR patungong CHF — i-convert ang euro sa franko ng Suwisa',
             'intro': ['Ang EUR/CHF ang safe-haven litmus test ng Europa: sa tuwing tumataas ang '
                       'stress sa eurozone — debt crisis noong 2011, mga banking scare, digmaan sa '
                       'kontinente — tumatawid ang pera sa Swiss border at bumabagsak ang pair. '
                       'Mas mahigpit na tinitingnan ng Swiss National Bank ang rate na ito kaysa '
                       'kahit anong iba, at paulit-ulit na nakikialam para hindi magula ang Swiss '
                       'exports.',
                       'Dramatiko ang modernong kasaysayan ng pair: isang floor sa 1.20 mula noong '
                       '2011, pagkatapos ang Enero 2015 na depeg na gumawa ng 20–30 porsyentong '
                       'flash crash sa loob ng mga minuto. Mula noon, tinatrado ang franko bilang '
                       'malinis, kung minsan sobrang lakas, na kanlungan — at aktibo pa ring '
                       'participant sa merkado ang SNB.'],
             'faq': [('Bakit napakahalaga sa SNB ang EUR/CHF?',
                      'Dahil sa Europa nagbebenta ang ekonomiya ng Suwisa. Ginagawang hindi '
                      'kompetitibo ng sobrang lakas na franko ang mga Swiss export at hinihila ang '
                      'implasyon sa ibaba ng target, kaya bumibili ng foreign currency ang SNB (at '
                      'minsang nagpatupad ng negative rates) para i-cap sa lakas ng franko. Mas '
                      'marami itong nakikialam sa pair na ito kaysa halos anumang ibang central '
                      'bank sa malaking merkado.'),
                     ('Stable na pair ba ang EUR/CHF para hawakan?',
                      'Stable sa kalmadong panahon at sumasabog sa mga krisis — kabaliktaran ng '
                      'diversified. Nanatiling textbook na babala ang depeg noong 2015 na maaaring '
                      'bawiin overnight ang pangako ng central bank na i-cap ang isang currency. '
                      'Natuto nang iba sa isang umaga ang sinumang itinuring na walang panganib '
                      'ang pair.')]},
 'EUR-PLN': {'title': 'EUR patungong PLN — exchange rate ngayon, libreng converter at ang zloty ng '
                      'Poland',
             'description': 'I-convert ang euro sa zloty ng Poland nang may live rates: ang '
                            'EUR/PLN rate ngayon, libreng kalkulator, tablea ng halaga at kung ano '
                            'ang nagpapagalaw sa zloty.',
             'h1': 'EUR patungong PLN — i-convert ang euro sa zloty ng Poland',
             'intro': ['Ang Poland ang ikaanim na pinakamalaking ekonomiya ng European Union na '
                       'gumagamit pa rin ng sariling currency, at ang zloty ang pinakamalakas nang '
                       'tinatrabaho sa mga non-euro currency ng EU. Tumitrado ang EUR/PLN sa '
                       'interest-rate gap sa National Bank of Poland, EU fund na umaagos papuntang '
                       'silangan, German factory order para sa Polish industry at regional '
                       'geopolitical risk.',
                       'Mula noong sumali ang Poland sa EU noong 2004, lumakas ang zloty sa mga '
                       'boom at bumagsak nang mabilis sa mga krisis — itinulak ng 2008 at 2022 ang '
                       'pair sa mga historic na ekstremo. Habang hindi pa napagpapasyahan ang '
                       'eventual na euro adoption ng Poland, nananatiling structural na feature ng '
                       'European finance ang pair sa mga darating na taon.'],
             'faq': [('Papalitan ba ng Poland ang euro at tatanggalin ang zloty?',
                      'May legal na obligasyon ang Poland na sumali sa euro sa kalaunan ngunit '
                      'walang target na petsa at malawak ang skepticismo ng publiko. Hanggang may '
                      'kapani-paniwalang adoption timeline, aktibo pa ring tinatrado ang EUR/PLN — '
                      'kaya nitong gumalaw ang pair ang mga political statement tungkol sa '
                      'timetable.'),
                     ('Bakit tumalon ang EUR/PLN noong 2022?',
                      'Ginawang frontline economy ang Poland nang gabing-gabi ng digmaan sa '
                      'katabing Ukraine: tinama nang mabilis ang currency ng refugee inflow, '
                      'defense spending at energy shock. Nakialam ang National Bank of Poland para '
                      'suportahan ang zloty — ang pinakamatalim na galaw ng pair sa loob ng '
                      'dalawang dekada.')]},
 'GBP-JPY': {'title': 'GBP patungong JPY — exchange rate ngayon, libreng converter at ang volatile '
                      'na pair',
             'description': 'I-convert ang pound sterling sa yen ng Hapon nang live: ang GBP/JPY '
                            'rate ngayon, libreng kalkulator, tablea ng halaga at ang volatile na '
                            'pair na ito.',
             'h1': 'GBP patungong JPY — i-convert ang pound sterling sa yen ng Hapon',
             'intro': ['Ang GBP/JPY — tawag ng mga matatandang trader dito ay ‘ang halimaw’ o ‘ang '
                       'dragon’ — isa sa pinakavolatile na pangunahing currency pair. Nagpapatong '
                       'ito ng dalawang risk engine: ang sensitivity ng sterling sa UK political '
                       'at fiscal news, at ang papel ng yen bilang funding currency ng mundo, '
                       'ginagawa itong mabilis humampas sa bawat liko ng global sentiment.',
                       'Paborito ng carry trade ang pair: nanghihiram ng halos zero-rate na yen '
                       'para bumili ng mas mataas na yield na pound. Gumagana ito hanggang sapitin '
                       "ng krisis na sabay-sabay silang mag-unwind — kaya't ilang taong "
                       'unti-unting paitaas ang GBP/JPY at mabilis na pagbagsak sa loob ng mga '
                       'linggo. Mas mahalaga rito ang sizing at timing kaysa halos anumang ibang '
                       'pangunahing pair.'],
             'faq': [('Bakit mas volatile ang GBP/JPY kaysa USD/JPY?',
                      'Dahil dinodoble nito ang dalawang volatility. Nagdaragdag ang sterling ng '
                      'UK-specific na political at economic risk sa itaas ng global risk sentiment '
                      'na tumutulak na sa USD/JPY. Walang anchor economy na pareho ang pair, kaya '
                      'halos purong rate gap at sentiment lang ang tinatrado nito — sangkap ng '
                      'malalaking galaw.'),
                     ('Ano ang carry trade sa GBP/JPY?',
                      'Pamumuhiram ng yen sa halos zero na Japanese rate at pamumuhunan sa pound '
                      'sa mas mataas na UK rate, kinikita ang pagkakaiba. Kumikita ito habang '
                      'kalmado ang mga merkado at parusang mabilis kapag hindi: sa risk-off na '
                      'episyode, tumatalon ang yen habang nage-unwind ang mga carry position, '
                      'madalas 10 porsyento o higit pa laban sa pound sa loob ng mga buwan.')]},
 'AUD-JPY': {'title': 'AUD patungong JPY — exchange rate ngayon, libreng converter at ang risk '
                      'barometro',
             'description': 'I-convert ang dolyar ng Australya sa yen ng Hapon nang live: ang '
                            'AUD/JPY rate ngayon, libreng kalkulator, tablea ng halaga at ang risk '
                            'barometro.',
             'h1': 'AUD patungong JPY — i-convert ang dolyar ng Australya sa yen ng Hapon',
             'intro': ['Ang AUD/JPY ang pinakamalinaw na risk barometro sa currency market. '
                       'Kumakatawan sa global growth at commodity demand — higit sa lahat ang '
                       'industrial demand ng Tsina — ang dolyar ng Australya, habang kumakatawan '
                       'sa kaligtasan ang yen. Kapag lumalago ang world economy, umaakyat ang '
                       'pair; kapag tumama ang paniko, bumabagsak ito nang mas mabilis kaysa halos '
                       'anumang ibang pangunahing cross.',
                       'Ito rin ang klasikong carry-trade currency pair: sa loob ng mga dekada, '
                       'nanghiram ng murang yen ang mga investor para bumili ng mas mataas na '
                       'yield na Aussie. Hinuhubog ng flow na iyon ang mahaba, mabigat na uptrend '
                       'ng pair at ng mga mabilis na unwind episode nito — nanatiling babala ang '
                       '2008, nang mawalan ng mga kalahati ng halaga nito ang AUD/JPY sa loob ng '
                       'ilang buwan.'],
             'faq': [('Bakit sinasabing risk barometro ang AUD/JPY ng mga trader?',
                      'Dahil magkabaliktaran ang kinatatayuan ng bawat currency: umaangat ang '
                      'Aussie kasama ng global growth at commodity demand, umaangat ang yen sa '
                      'takot. Kaya gumagalaw ang pair kasama ng world equity market nang hindi '
                      'maitatapatan ng iilang cross — kapag bumagsak ito nang mabilis, totoong '
                      'risk-off iyon.'),
                     ('Ano ang nangyari sa AUD/JPY sa krisis noong 2008?',
                      'Halos nahati sa dalawa. Nage-unwind ang carry trade habang nagyelo ang '
                      'global credit: nagbenta ang mga investor ng Australian dollar para bayaran '
                      'ang hiram na yen, at bumagsak ang pair mula sa itaas ng 100 hanggang low '
                      '50s sa loob ng mga buwan. Nanatiling standard na halimbawa ito ng kung '
                      'gaano kabilis bumaliktad ang mga carry strategy.')]}}
