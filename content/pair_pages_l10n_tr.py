# -*- coding: utf-8 -*-
"""Türkçe içerikler — döviz çifti sayfaları (USD/EUR ve ötekileri).

PAIR_UI_L10N, pair_pages.PAIR_UI["en"] içindeki 10 arayüz dizesini karşılıklar;
{f} {t} {d} yer tutucuları olduğu gibi korunur. PAIR_CONTENT_L10N ise
PAIR_CONTENT["en"] içindeki 15 çifti karşılıklar; anahtarlar İngilizce sürümle
aynıdır (USD-EUR vb.). Kardeş dosyalarda (pair_pages_l10n_de.py vb.) olduğu
gibi iki dict de düzdür — build-lang-pages.py ikisini PAIR_UI["tr"] ile
PAIR_CONTENT["tr"] içine birleştirir.
"""

PAIR_UI_L10N = {
    "pairConvert": "Canlı çevirici",
    "pairRateHead": "Güncel döviz kuru",
    "pairAsOf": "{d} tarihli referans kur. Yukarıdaki canlı çevirici her zaman en güncel kuru getirir — aşağıdaki tablolar yalnızca yol göstermesi için derleme anında alınmış bir anlık görüntüdür.",
    "pairAmounts": "Sık kullanılan tutarlar: {f} → {t}",
    "pairReverse": "Sık kullanılan tutarlar: {t} → {f}",
    "pairMore": "Diğer {f} çevirileri",
    "pairMorePairs": "Diğer döviz çiftleri",
    "pairIntroHead": "{f}/{t} döviz kuru hakkında",
    "pairCurLinks": "Para birimi sayfaları",
    "pairMetaTmpl": ("{f} birimini {t} birimine canlı döviz kurlarıyla çevirin: günün {f}/{t} kuru, ücretsiz bir hesaplayıcı, "
                     "sık kullanılan tutar tabloları ve bu döviz çiftini etkileyen faktörler."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD'den EUR'a — günün kuru, ücretsiz çevirici ve tutar tabloları",
        "description": "ABD dolarını euroya canlı kurlarla çevirin: günün USD/EUR kuru, ücretsiz hesaplayıcı, tutar tabloları ve dünyanın en likit çiftini etkileyen faktörler.",
        "h1": "USD'den EUR'a — ABD dolarını euroya çevirin",
        "intro": [
            "USD/EUR, dünyada en çok işlem gören döviz çiftidir — tüm döviz işlem hacminin yaklaşık dörtte biri — bu yüzden tüm çevrimler arasında en dar spread'lere ve en derin pazara sahiptir. Kur, tek bir ABD dolarının euro cinsinden fiyatından ibarettir; küresel ticaret, yatırım akımları ve Federal Reserve ile Avrupa Merkez Bankası arasındaki faiz farkı tarafından sürekli biçimde belirlenir.",
            "Günlük çevrimlerde pratik soru, burada gösterilen orta piyasa kurunun üzerine ne kadar marj ödediğinizdir. Bankalar tipik olarak yüzde 1–4 ekler; kart ve havale hizmetleri geniş ölçüde değişkenlik gösterir. Bir alışveriş ya da havaleden önce canlı kura bakmak, elinize sunulan teklifin adil olup olmadığını anında söyler.",
        ],
        "faq": [
            ("USD/EUR döviz kuru nasıl belirlenir?",
             "Kur serbestçe dalgalanır — iki para birimine duyulan arz ve talep, fiyatı gündüz gece belirler; bunu başlıca Fed ile ECB'nin faiz politikası, Atlantik'in iki yakasındaki enflasyon ve küresel risk iştahı şekillendirir. Sabit ya da yönetilen bir hedef yoktur."),
            ("USD'yi EUR'ya çevirmek için en uygun zaman hangisidir?",
             "Likidite en derin ve spread'ler en dar, Avrupa ile ABD işlem saatlerinin çakıştığı dönemdedir (yaklaşık 13:00–17:00 UTC). Kısa vadeli yönü kimsenin güvenilir biçimde öngöremeyeceği için, büyük tutarlarda daha iyi bir gün bekleme yerine parça parça çevirmek daha güvenlidir."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD'den GBP'ye — canlı sterlin kuru, çevirici ve tutar tabloları",
        "description": "ABD dolarını İngiliz sterlinine canlı kurlarla çevirin: günün USD/GBP kuru, ücretsiz hesaplayıcı, tutar tabloları ve sterlini hareket ettiren faktörler.",
        "h1": "USD'den GBP'ye — ABD dolarını İngiliz sterlinine çevirin",
        "intro": [
            "Dolar-sterlin kuru, onu 1860'larda ilk kez taşıyan transatlantik telgraf kablosundan ötürü “kablo” (cable) lakabını taşır ve dünyanın kesintisiz kote edilen en eski döviz kurlarından biridir. Bugün Fed ile İngiltere Merkez Bankası arasındaki faiz farkını, Birleşik Krallık enflasyonunu ve Britanya'nın ticaret ile mali durumunun sağlığını yansıtır.",
            "Sterlin, Londra saatlerinde en aktif işlem görür; çift, Birleşik Krallık ekonomik verileri ve mali açıklamalar çevresinde sert hareketlere yatkındır. Herhangi bir teklifi aşağıdaki orta piyasa kuruyla karşılaştırmak, sağlayıcının ne kadar marj aldığını görmenin en hızlı yoludur.",
        ],
        "faq": [
            ("İngiliz sterlini neden ABD dolarından daha değerlidir?",
             "Daha yüksek birim fiyat, daha güçlü bir ekonomi anlamına gelmez — tarihi ve para birimlerinin bölünüşünü yansıtır. Sterlin, dolar daha var olmadan dünyanın hâkim para birimiydi; sayının kendisi göreli ekonomik güç ya da satın alma gücü hakkında bir şey söylemez."),
            ("USD/GBP'yi en çok ne hareket ettirir?",
             "Fed ve İngiltere Merkez Bankası'nın faiz kararları, Birleşik Krallık enflasyon verileri ile Westminster'dan gelen siyasi ve mali haberler. 2016 Brexit oylamasında sterlin tek günde yaklaşık yüzde 10 düştü — bu, sterlinin çoğu büyük para biriminin taşımadığı bir siyasi risk taşıdığını hatırlatır."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD'den JPY'ye — güncel yen kuru, ücretsiz hesaplayıcı ve tablolar",
        "description": "ABD dolarını Japon yenine canlı kurlarla çevirin: günün USD/JPY kuru, ücretsiz hesaplayıcı, tutar tabloları ve yenin yönünü belirleyen faktörler.",
        "h1": "USD'den JPY'ye — ABD dolarını Japon yenine çevirin",
        "intro": [
            "USD/JPY, dünyada en çok işlem gören ikinci döviz çifti ve ABD ile Japonya arasındaki faiz farkının klasik barometresidir. Japon faizleri onlarca yıl sıfıra yakın durduğu için yen, dünyanın gözde finansman para birimine dönüştü — piyasalar kendine güvenerken zayıflar, krizler bu pozisyonları kapatmaya zorladığında sertçe güçlenir.",
            "Çift, resmi Japonya müdahaleleri yüzünden de izlenir: Maliye Bakanlığı, yen çok uzağa ve çok hızlı zayıfladığında defalarca yen satın aldı. Büyük çevrimleri en sağlıklısı orta piyasa kuruna karşı kontrol etmektir; JPY'de perakende marjları yanıltıcı ölçüde geniş olabiliyor.",
        ],
        "faq": [
            ("Yen, dollara karşı bazen neden bu kadar sert düşer?",
             "Başlıca neden faiz farkıdır. ABD faizleri yüksek, Japon faizleri sıfıra yakınken yatırımcılar, daha yüksek getiri dolu dolar varlıkları almak için yen satar — carry trade. Yen aylarca sürebilen bir gerileme yaşayabilir; bu işlemler kapatıldığında da şiddetle sıçrar."),
            ("Japonya hükümeti USD/JPY kurunu değiştirebilir mi?",
             "Pazara karşı durabilir, onu tersine çeviremez. Japonya, hareketler düzensizleştiğinde yen alarak ya da satarak müdahale etti — tek bir epizotta bazen on milyarlarca dolar tutarında. Müdahale yolu yumuşatır; temellerin çizdiği uzun vadeli yönü ise nadiren değiştirir."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD'den CNY'ye — yönetilen yuan kuru, çevirici ve tutar tabloları",
        "description": "ABD dolarını Çin yuanına canlı kurlarla çevirin: günün USD/CNY kuru, ücretsiz hesaplayıcı, tutar tabloları ve yönetilen kur sisteminin işleyişi.",
        "h1": "USD'den CNY'ye — ABD dolarını Çin yuanına çevirin",
        "intro": [
            "Dolar-yuan kuru, bir merkez bankasınca yönetilen en büyük döviz çiftidir. Her sabah Çin Halk Bankası günlük bir sabitleme (fixing) açıklar ve kıyı içi kur (CNY) yalnızca bunun çevresindeki bir bandın içinde oynayabilir — USD/CNY'nin gün gün, ekonomik öneminin çağrıştırdığından çok daha az hareket etmesinin nedeni budur.",
            "Çin'in ticaret fazlası, sermaye kontrolleri ve politika hedefleri — hepsi kurda rol oynar. Çevrimler için iki not: Kıyı içi CNY ile kıyı dışı CNH hafif farklılaşabilir ve Çin'de bireysel döviz çevrimi sermaye kontrolü kurallarına tabidir. Teklifleri daima aşağıdaki referans kur ile karşılaştırın.",
        ],
        "faq": [
            ("Çin yuanı serbestçe çevrilebilir mi?",
             "Tam olarak hayır. Ticarete dayalı çevrim kolaydır; sınır ötesi yatırım akımları ise kotalara ve onaylara bağlıdır. Bu yüzden kıyı dışı sürüm (CNH), kıyı içi CNY'den hafif farklı bir fiyattan işlem görür — aradaki fark, parayı sınırın ötesine taşımanın maliyetini gösterir."),
            ("Diğer çiftlerle kıyaslandığında USD/CNY neden neredeyse oynamaz?",
             "Çünkü merkez bankası onu yönetir. Günlük sabitleme ve işlem bandı, kuru dollara göre istikrarlı tutar — Çin'in ticarette öngörülebilirlik tercihiyle uyumlu şekilde. Yönetilmek sabit olmak değildir: Kur, aylar ve yıllar ölçeğinde yine temellere göre yön bulur."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD'den INR'ya — bugünkü rupi kuru, hesaplayıcı ve havale notları",
        "description": "ABD dolarını Hint rupisine canlı kurlarla çevirin: günün USD/INR kuru, ücretsiz hesaplayıcı, tutar tabloları ve dünyanın en büyük havale koridorundan notlar.",
        "h1": "USD'den INR'ya — ABD dolarını Hint rupisine çevirin",
        "intro": [
            "USD/INR, dünyanın en önemli havale koridorlarından biridir — Hindistan, dünyanın diğer hiçbir ülkesinin almadığı kadar havale alır — ve yoğun işlem gören bir yükselen piyasa çiftidir. Hindistan Merkez Bankası (RBI) düzeyi değil oynaklığı yönetir: Rezervleriyle sert hareketleri yumuşatır ama rupiye uzun vadeli trendini bulma özgürlüğü tanır.",
            "Rupinin yapısal öyküsü, enflasyon farklılıkları ile Hindistan'ın cari işlemler dengesinin sürüklediği ve küresel risk olaylarıyla kesilen, dollara karşı kademeli bir değer kaybıdır. Hindistan'a para gönderen herkes için gerçek maliyet, orta piyasa kuru ile sunulan kur arasındaki farka gizlenmiştir.",
        ],
        "faq": [
            ("Hint rupisi zaman içinde neden değer kaybeder?",
             "Başlıca nedenler enflasyon farklılıkları ve ticaret açığıdır: Hindistan, sattığından çok daha fazlasını ithal eder ve farkı sermaye girişleriyle finanse eder. RBI yolu yumuşatır; yine de on yıllar boyunca rupi dollara karşı istikrarlı biçimde zayıfladı — gelişen bir ekonomi için bu normaldir."),
            ("Hindistan'a para gönderirken en iyi kuru nasıl yakalarım?",
             "Göndermeden önce yalnız ücretlere değil, sunulan kur ile orta piyasa kuru arasındaki farka da bakın. Bu koridorda uzmanlaşmış havale hizmetleri genellikle banka transferini geride bırakır; düzenli aile havalelerinde yüzde 1'lik fark bile bir yılın içinde kayda değer bir tutara dönüşür."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD'den CAD'e — canlı loonie kuru, ücretsiz çevirici ve tablolar",
        "description": "ABD dolarını Kanada dolarına canlı kurlarla çevirin: günün USD/CAD kuru, ücretsiz hesaplayıcı, tutar tabloları ve loonie'yi etkileyen petrol ile faizler.",
        "h1": "USD'den CAD'e — ABD dolarını Kanada dolarına çevirin",
        "intro": [
            "USD/CAD — “loonie” — dünyanın ilk beş döviz çiftinden biridir ve yeryüzündeki en büyük ticaret ilişkilerinden birinin üzerine kuruludur. Kanada ihracatının kabaca dörtte üçünü ABD'ye gönderir; bu yüzden çift, ABD büyümesine, enerji fiyatlarına (Kanada önemli bir petrol ihracatçısıdır) ve Fed ile Kanada Merkez Bankası arasındaki faiz farkına göre yoğun biçimde fiyatlanır.",
            "Petrol yükseldiğinde CAD genellikle güçlenir; küresel büyüme korkuları bastırınca emtia para birimleriyle birlikte zayıflar. Çift gündüz gece likittir ve orta piyasa kurundan yüzde birin çok altında farkla teklif bulmak kolaydır — geniş marjlar bu yüzden daima sorgulanmayı hak eder.",
        ],
        "faq": [
            ("Kanada dolarına neden loonie denir?",
             "1987'de tedavüle giren bir dolarlık madeni paranın üzerindeki kuzey dalgıç kuşundan (loon) sonra. Lakap yerleşti ve bugün FX argosunda para biriminin kendisini anlatır — tıpkı “loonie bugün yükseldi” denmesi gibi."),
            ("Petrol fiyatı gerçekten USD/CAD'yi etkiler mi?",
             "Evet, gözle görülür ölçüde. Ham petrol ve ilgili ürünler Kanada'nın en büyük ihracat kalemidir; yükselen petrol Kanada'ya daha çok dolar taşır ve CAD'i yukarı çeker. Tüccarlar bu çifti, iki ülkenin faizlerinin yanında enerji piyasalarına kaba bir bahis olarak da okur."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD'den AUD'ye — güncel Aussie kuru, hesaplayıcı ve tutar tabloları",
        "description": "ABD dolarını Avustralya dolarına canlı kurlarla çevirin: günün USD/AUD kuru, ücretsiz hesaplayıcı, tutar tabloları ve emtia parası Aussie'nin dinamikleri.",
        "h1": "USD'den AUD'ye — ABD dolarını Avustralya dolarına çevirin",
        "intro": [
            "Avustralya doları klasik emtia para birimidir: Kaderi demir cevheri, kömür ve gaz ihracatının, her şeyden önce de Çin'in bunlara duyduğu talebin izinde ilerler. USD/AUD bu yüzden küresel risk iştahının en temiz gerçek zamanlı göstergelerinden biridir — dünya ticareti canlanırken Aussie güçlenir, riskten kaçış dönemlerinde zayıflar.",
            "Daha kısa vadeli salınımları Avustralya Merkez Bankası'nın (RBA) ve Fed'in faiz politikası sürükler. Avustralya'nın çalışma-tatil ve öğrenci nüfusu, USD→AUD (ve geri dönüşünü) sıkça tekrarlanan bir çevrim haline getirir; yüzde 1'lik bir kur marjı bile burada hızla birikir.",
        ],
        "faq": [
            ("Avustralya doları Çin'e neden bu kadar hassastır?",
             "Çin, açık ara Avustralya'nın en büyük ihracat pazarıdır; özellikle çelik üretimi için gereken demir cevherinde. Çin inşaatı yavaşladığında emtia fiyatları ile AUD çoğu zaman birlikte düşer — para birimi, Çin ağır sanayisinin gerçek zamanlı barometresi gibi davranır."),
            ("AUD güvenli liman mıdır?",
             "Tam tersi: Tüccarlar buna risk iştahı para birimi der. Küresel panik anlarında — 2008, 2020 — para ABD dolarına akar ve Aussie büyük para birimleri arasında genellikle en sert düşendir. Tam da bu döngüselliktir, carry tüccarlarının ve büyüme gözlemcilerinin onu bu denli yakından izlemesinin nedeni."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD'den CHF'ye — günün frangı kuru, ücretsiz çevirici ve tablolar",
        "description": "ABD dolarını İsviçre frangına canlı kurlarla çevirin: günün USD/CHF kuru, ücretsiz hesaplayıcı, tutar tabloları ve frangıyı hareket ettiren faktörler.",
        "h1": "USD'den CHF'ye — ABD dolarını İsviçre frangına çevirin",
        "intro": [
            "İsviçre frangı, dünyanın başta gelen güvenli liman para birimidir: Savaş, bankacılık stresi ya da pazar panisi vurduğunda para İsviçre'ye akar ve CHF güçlenir. Bu yüzden USD/CHF, dollanın kendisi bir sığınakken bile küresel krizlerde düşme eğilimindedir — frangı, yalnızca daha güçlü sığınaaktır.",
            "İsviçre Merkez Bankası (SNB) kurun şeklini aktif biçimde belirler: 2011–2015 arasındaki ünlü euro tabanından bugüne kadarki yoğun müdahalelere kadar. Çevrimler açısından İsviçre başka bir gerçeği de hatırlatır: Zengin bir ülkenin para çifti bile geniş perakende marjları taşıyabilir; özellikle havalimanlarında ve otellerde — orta piyasa referansını her zaman kontrol edin.",
        ],
        "faq": [
            ("İsviçre frangı neden güvenli liman olarak görülür?",
             "Bir asırlık tarafsızlık, düşük borç, cari işlemler fazlası ve inandırıcı bir merkez bankası, frangı riskten kaçan paranın varsayılan park yeri yapar. İsviçre enflasyonu ayrıca on yıllardır ABD'nin ve euro bölgesinin çok altında seyrederek para biriminin satın alma gücünü korudu."),
            ("SNB Ocak 2015'te ne yaptı?",
             "Frangının euro karşısındaki gücüne koyduğu sınırı ani biçimde kaldırdı. USD/CHF ile EUR/CHF dakikalar içinde kabaca yüzde 20–30 çöktü — bir büyük çiftte görülmüş en sert gün içi hareketlerden biri; tüccarların “SNB riski” ifadesine bugün de saygı duymasının nedeni."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD'den MXN'ye — canlı peso kuru, hesaplayıcı ve havale ipuçları",
        "description": "ABD dolarını Meksika pesosuna canlı kurlarla çevirin: günün USD/MXN kuru, ücretsiz hesaplayıcı, tutar tabloları ve en likit yükselen çiftin dinamikleri.",
        "h1": "USD'den MXN'ye — ABD dolarını Meksika pesosuna çevirin",
        "intro": [
            "USD/MXN, Amerika kıtasının en çok işlem gören yükselen piyasa çifti ve dünyanın en likit çiftleri arasındadır. Peso, ABD ekonomisini hareket ettiren her şeye göre fiyatlanır — ticaret politikası, büyüme, Fed ile Banxico arasındaki faiz farkı — üstüne petrol fiyatları ve ABD'den gelen devasa havale koridoru eklenir.",
            "Bu kadar likit olduğu için çift, küresel risk iştahına çabuk yanıt verir: Sakin piyasalarda güçlenen, paniklerde şiddetle boşlanan klasik bir carry trade hedefidir. Gezginler ve havale gönderenler için havalimanlarında yüzde 3–6'lık marjlar olağandır — aşağıdaki orta piyasa kuru kıyaslama ölçütüdür.",
        ],
        "faq": [
            ("USD/MXN neden bu kadar oynaktır?",
             "Meksika'daki yüksek faizler, stres anlarında hızla kaçan kısa vadeli carry parasını çeker; pesoyu ayrıca ABD-Meksika ticareti ve siyasi haberlerinin referans varlığı yapar. İkisinin birleşimi çifti likit ama sıçrak kılar — büyük günlük hareketler normaldir, arıza değil."),
            ("Doları Meksika'ya göndermenin en ucuz yolu nedir?",
             "Bu koridorda uzmanlaşmış havale hizmetleri, bankaları ve nakit transfer dükkanlarını düzenli olarak geride bırakır. Ulaşılan tutarı orta piyasa kuruyla karşılaştırın: 300 dolarlık bir havalede adil bir teklif ile yüzde 5'lik bir marj arasındaki fark, yerelde tam bir günlük ücrete denk düşebilir."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD'den PHP'ye — güncel peso kuru, ücretsiz çevirici ve havale rehberi",
        "description": "ABD dolarını Filipinler pesosine canlı kurlarla çevirin: günün USD/PHP kuru, ücretsiz hesaplayıcı, tutar tabloları ve havale odaklı çiftin dinamikleri.",
        "h1": "USD'den PHP'ye — ABD dolarını Filipinler pesosine çevirin",
        "intro": [
            "Filipinler pesosu, dünyanın en büyük havale akışlarından birinin üzerine kuruludur: Milyonlarca yurt dışındaki Filipinli işçi (OFW) yuvaya para gönderir ve bu dolar girişleri ekonominin bir sütunudur. USD/PHP buna uygun olarak küresel risk iştahına, petrol fiyatlarına (Filipinler net ithalatçıdır) ve Bangko Sentral ng Pilipinas'ın politikasına göre fiyatlanır.",
            "Resmi kur hafif bir elle yönetilir — merkez bankası, kademeli ayarlanmaya izin verirken sivrilikleri yumuşatır. OFW aileleri ile gezginler için bu koridorda sağlayıcılar arasındaki fark geniştir; göndermeden önce orta piyasa kuruna bakmak, tasarrufun en kolay tek yoludur.",
        ],
        "faq": [
            ("Havaleler Filipinler pesosunu nasıl etkiler?",
             "Yurt dışındaki işçilerden gelen istikrarlı dolar akışı, pesoyu ve ülkenin ödemeler dengesini destekler — her yıl GSYH'nin birkaç yüzde biri. Küresel risk yükseldiğinde ya da varılan ekonomiler zayıfladığında havaleler yumuşar ve peso çoğu kez onları izler."),
            ("USD'yi PHP'ye ABD'de mi yoksa Filipinler'de mi çevirmek daha iyidir?",
             "Belirleyici olan ülke değil sağlayıcıdır. Koridorun iki yakasında da ucuz ve pahalı seçenekler vardır; asıl sayı, alıcının eline gerçekten kaç peso geçtiğidir. En yakın dükkanına güvenmek yerine teklifleri orta piyasa kuruyla kıyaslayın."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR'dan GBP'ye — euro-sterlin kuru, çevirici ve tutar tabloları",
        "description": "Euroyu İngiliz sterlinine canlı kurlarla çevirin: günün EUR/GBP kuru, ücretsiz hesaplayıcı, tutar tabloları ve Avrupa'nın sakin çiftini etkileyen faktörler.",
        "h1": "EUR'dan GBP'ye — euroyu İngiliz sterlinine çevirin",
        "intro": [
            "EUR/GBP, klasik Avrupa çaprazıdır: Ticaretlerinin kabaca yarısını birbirine yapan iki ekonomi, yalnızca bir para sınırıyla ayrılır. İkisi de gelişmiş, düşük enflasyonlu para birimleri olduğundan çift, dolar çaprazlarından çok daha az kıpırdar — özünde euro bölgesi ile Birleşik Krallığın göreli kaderine atılan bir bahstir.",
            "ECB ile İngiltere Merkez Bankası arasındaki faiz farkı trendin büyük bölümünü taşır; sivrilikleri ise Birleşik Krallık siyaseti ve maliye haberleri üretir. İki yaka arasında çalışanlar, emekliler ve işletmeler için çiftin istikrarı küçük kur farklarını daha da önemli kılar: Yüzde 1'lik bir marj, toplam yıllık hareketin büyük bir dilimidir.",
        ],
        "faq": [
            ("EUR/GBP, EUR/USD'den neden daha sakindir?",
             "Ne euro ne de sterlin küresel bir risk para birimidir; dünya çapındaki güvenli limana kaçış akımları bu ikiliyi yanıdan geçer. Çift, ağırlıkla Birleşik Krallık-AB göreli ekonomisini ve yavaş değişen faiz farklarını yansıtır — 2016'nın gösterdiği gibi Britanya siyasi haberlerinde sert biçimde sivrilenebilir."),
            ("Brexit hâlâ EUR/GBP'yi nasıl etkiliyor?",
             "Yapısal olarak. 2021'den bu yana yeni ticaret sürtünmeleri Birleşik Krallık ekonomisini AB'ye karşı biraz daha kapalı hale getirdi; çoğu ekonomist bunu yapısal olarak daha zayıf bir sterline bağlar. Ticaret kurallarına dair her Birleşik Krallık-AB müzakere turu çifti bugün de oynatıyor."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR'dan CHF'ye — canlı kur, hesaplayıcı ve SNB'nin çiftteki rolü",
        "description": "Euroyu İsviçre frangına canlı kurlarla çevirin: günün EUR/CHF kuru, ücretsiz hesaplayıcı, tutar tabloları ve İsviçre Merkez Bankası'nın çiftteki rolü.",
        "h1": "EUR'dan CHF'ye — euroyu İsviçre frangına çevirin",
        "intro": [
            "EUR/CHF, Avrupa'nın güvenli liman kıyas taşıdır: Euro bölgesi gerilimi yükseldiğinde — 2011 borç krizi, bankacılık korkuları, kıtada savaş — para İsviçre sınırını geçer ve çift düşer. İsviçre Merkez Bankası bu kuru diğer her kurdan yakından izler ve frangının İsviçre ihracatını boğmasını önlemek için defalarca müdahale etti.",
            "Çiftin modern tarihi dramatiktir: 2011'den itibaren 1,20 seviyesinde bir taban; ardından Ocak 2015'te bu bağın kopması, dakikalar içinde yüzde 20–30'luk bir flaş çöküşe yol açtı. O günden beri frangı, kimi zaman fazla güçlü olsa da temiz bir sığınak olarak işlem görüyor; SNB de bu pazarın aktif bir katılımcısı olmayı sürdürüyor.",
        ],
        "faq": [
            ("İsviçre Merkez Bankası EUR/CHF'ye neden bu kadar önem verir?",
             "Çünkü İsviçre ekonomisi Avrupa'ya satar. Fazla güçlü bir frangı İsviçre ihracatını rekabet dışı bırakır ve enflasyonu hedefin altına çeker; bu yüzden SNB yabancı para alır (ve bir dönem negatif faiz uyguladı) ve frangının gücünü sınırlamaya çalışır. Bu çiftte, büyük bir piyasada işlem gören neredeyse hiçbir başka merkez bankasından daha sık müdahale eder."),
            ("EUR/CHF tutmak için istikrarlı bir çift midir?",
             "Sakin zamanlarda stabil, krizde patlayıcıdır — çeşitlendirmenin tam karşıtı. 2015'teki bağın kopması, bir merkez bankasının para birimini sınırlama sözünün bir gecede geri çekilebileceğinin ders kitabı uyarısıdır. Çifti risksiz sananlar, tek bir sabahla aksini öğrendi."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR'dan PLN'ye — günün zloti kuru, ücretsiz çevirici ve tablolar",
        "description": "Euroyu Polonya zlotisine canlı kurlarla çevirin: günün EUR/PLN kuru, ücretsiz hesaplayıcı, tutar tabloları ve zlotiyi hareket ettiren faktörler.",
        "h1": "EUR'dan PLN'ye — euroyu Polonya zlotisine çevirin",
        "intro": [
            "Polonya, kendi para birimini hâlâ kullanan AB'nin altıncı büyük ekonomisidir ve zloti, AB'nin euro dışı para birimleri arasında en çok işlem görendir. EUR/PLN, Polonya Merkez Bankası (NBP) ile faiz farkına, doğuya akan AB fonlarına, Polonya sanayisine gelen Alman fabrika siparişlerine ve bölgesel jeopolitik riske göre fiyatlanır.",
            "Polonya'nın 2004'te AB'ye girmesinden bu yana zloti hem canlanmalarda güçlendi hem de krizlerde sert düştü — 2008 ile 2022, çifti tarihi uçlara taşıdı. Polonya'nın nihai euro geçişi hâlâ karara bağlanmadığı için çift, önümüzdeki yıllarda da Avrupa finansının yapısal bir parçası olmaya devam edecek.",
        ],
        "faq": [
            ("Polonya euroyu benimseyip zlotiyi bırakacak mı?",
             "Polonya hukuken er ya da geç euroyu benimsemekle yükümlü; ancak bir hedef tarihi yok ve kamuoyunda geniş bir şüphecilik sürüyor. İnanılır bir geçiş takvimi belirene dek EUR/PLN aktif işlem gören bir çift olarak kalır — takvime dair siyasi açıklamalar tek başına çifti oynatabilir."),
            ("EUR/PLN 2022'de neden fırladı?",
             "Komşu Ukrayna'daki savaş, Polonya'yı bir gecede cephe hattındaki bir ekonomiye dönüştürdü: Mülteci akınları, savunma harcamaları ve enerji şokları para birimini sert biçimde vurdu. Polonya Merkez Bankası zlotiyi desteklemek için müdahale etti — çift, yirmi yılın en keskin hareketlerini yaşadı."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP'den JPY'ye — oynak sterlin-yen kuru, çevirici ve tutar tabloları",
        "description": "İngiliz sterlinini Japon yenine canlı kurlarla çevirin: günün GBP/JPY kuru, ücretsiz hesaplayıcı, tutar tabloları ve en oynak büyük çifti etkileyen faktörler.",
        "h1": "GBP'den JPY'ye — İngiliz sterlinini Japon yenine çevirin",
        "intro": [
            "GBP/JPY — eski tüccarlar ona “canavar” (the beast) ya da “ejder” (the dragon) derdi — en oynak büyük döviz çiftlerinden biridir. İki risk motorunu üst üste dizer: Sterlinin Birleşik Krallık siyaset ve maliye haberlerine duyarlılığı ile yenin dünyanın finansman para birimi rolü; küresel iştah her döndüğünde ikisi birlikte çifti sert biçimde sallar.",
            "Çift, carry trade'in gözdesidir: Sıfıra yakın faizli yen borçlanıp daha yüksek getiri sunan sterlini almak. Bu düzen, bir kriz herkesi aynı anda pozisyon kapatmaya zorlayana dek işler; GBP/JPY'nin yıllarca tırmanıp haftalar içinde şiddetle düşmesinin nedeni budur. Pozisyon boyutu ve zamanlama, burada hemen her başka büyük çiftten daha çok belirleyicidir.",
        ],
        "faq": [
            ("GBP/JPY, USD/JPY'den neden daha oynaktır?",
             "Çünkü iki oynaklığı çarpar. Sterlin, USD/JPY'yi zaten süren küresel risk iştahının üzerine Birleşik Krallık'a özgü siyasi ve ekonomik risk ekler. Çiftin ortak bir çapa ekonomisi yoktur; neredeyse tamamen faiz farkları ve iştaha göre işlem görür — büyük hareketlere hazır bir malzeme."),
            ("GBP/JPY'de carry trade nedir?",
             "Japonya'nın sıfıra yakın faizleriyle yen borçlanıp, Birleşik Krallık'ın daha yüksek faizlerinde sterlin yatırımına girmek ve aradaki farkı cebe indirmek. Piyasalar sakinken kârlıdır, olmadıklarında acı verir: Riskten kaçış dönemlerinde carry pozisyonları kapanırken yen fırlar — aylar ölçeğinde sterline karşı sık sık yüzde 10 ve üzeri."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD'den JPY'ye — risk barometresi kuru, hesaplayıcı ve tablolar",
        "description": "Avustralya dolarını Japon yenine canlı kurlarla çevirin: günün AUD/JPY kuru, ücretsiz hesaplayıcı, tutar tabloları ve piyasanın risk barometresinin dinamikleri.",
        "h1": "AUD'den JPY'ye — Avustralya dolarını Japon yenine çevirin",
        "intro": [
            "AUD/JPY, döviz piyasasının en saf risk barometresidir. Avustralya doları küresel büyümeyi ve emtia talebini — her şeyden önce Çin'in sanayi talebini — temsil eder; yen ise güvenliği. Dünya ekonomisi büyürken çift tırmanır; panik vurduğunda neredeyse her başka büyük çaprazdan çabuk düşer.",
            "Aynı zamanda klasik carry trade çiftidir: Onlarca yıl boyunca yatırımcılar, ucuz yen borçlanıp daha yüksek getiri sunan Aussie'yi aldı. Bu akım, çiftin uzun ve inatçı yükseliş trendlerini de şiddetli kapanma epizotlarını da biçimlendirir — 2008 ders niteliğindeki örnek olarak durur: AUD/JPY birkaç ay içinde değerinin kabaca yarısını yitirdi.",
        ],
        "faq": [
            ("Tüccarlar AUD/JPY'ye neden risk barometresi der?",
             "Çünkü her para birimi karşıt bir kutupta durur: Aussie küresel büyüme ve emtia talebiyle yükselir, yen korkuyla. Çift bu yüzden dünya hisse piyasalarıyla, az çaprazın erişebildiği ölçüde birlikte hareket eder — sert düştüğünde riskten kaçış gerçektir."),
            ("2008 krizinde AUD/JPY'ye ne oldu?",
             "Kabaca yarıya indi. Küresel kredi donduğu için carry trade kapandı: Yatırımcılar borçlandıkları yenleri geri ödemek için Avustralya doları sattı ve çift, aylar içinde 100'ün üzerinden 50'nin hemen üstündeki seviyelere çöktü. Carry stratejilerinin ne kadar çabuk ters dönebildiğinin standart örneği olarak kalır."),
        ],
    },
}
