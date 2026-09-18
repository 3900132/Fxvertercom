# -*- coding: utf-8 -*-
"""Localized <title> / <meta description> templates for secondary pages.

Merged into CONTENT_UI by build-lang-pages.py, so every secondary page
(currency pages, /currencies/ index, /support/) gets a title and description
in its own language instead of the shared English one.

curTitle / curDesc are templates for per-currency pages; build-lang-pages.py
fills the {name} (English currency name) and {code} (ISO code) placeholders.
curIdxDesc is the meta description of the /currencies/ index page,
supportDesc the one of /support/.

Keep every string free of double quotes (") and ampersands (&): the values
are injected verbatim into HTML attributes and JSON-LD blocks."""

PAGE_META = {
 "en": {
        "curTitle":"{name} ({code}) — Live Exchange Rates and Currency Converter | Fxverter",
        "curDesc":"{name} ({code}) live exchange rates: convert {code} to USD, EUR, GBP and 140 other currencies with the free Fxverter currency converter. Rates, facts and calculator.",
        "curIdxDesc":"Fxverter supports 141 world currencies — US Dollar, Euro, Turkish Lira, Japanese Yen and more. Live reference rates and a dedicated page for each currency.",
        "supportDesc":"Fxverter is free, with no ads and no tracking. If you find it useful, support its development — every contribution keeps it free for everyone.",
 },
 "tr": {
        "curTitle":"{name} ({code}) — Canlı Döviz Kurları ve Çevirici | Fxverter",
        "curDesc":"{name} ({code}) canlı kurları: Ücretsiz Fxverter çeviricisiyle {code} için USD, EUR, GBP ve 140+ para birimine dönüştürme. Kurlar, bilgiler ve hesaplayıcı.",
        "curIdxDesc":"Fxverter 141 dünya para birimini destekler — ABD Doları, Euro, Türk Lirası, Japon Yeni ve daha fazlası. Her para birimi için canlı kurlar ve özel sayfa.",
        "supportDesc":"Fxverter ücretsizdir; reklam ve takip yoktur. Faydalı buluyorsanız gelişimini destekleyin — her katkı, herkes için ücretsiz kalmasını sağlar.",
 },
 "zh": {
        "curTitle":"{name}（{code}）— 实时汇率与货币换算 | Fxverter",
        "curDesc":"免费使用 Fxverter 在线换算器查看 {name}（{code}）实时汇率，将 {code} 与美元、欧元、英镑等 140 多种货币互相换算。含汇率、币种资料与计算器。",
        "curIdxDesc":"Fxverter 支持 141 种世界货币——美元、欧元、土耳其里拉、日元等。提供实时参考汇率和每个币种的专属页面。",
        "supportDesc":"Fxverter 完全免费，无广告、无追踪。如果它对你有帮助，欢迎支持它的开发——每一份贡献都能让它继续免费开放。",
 },
 "ja": {
        "curTitle":"{name}（{code}）— リアルタイム為替レート・通貨コンバーター | Fxverter",
        "curDesc":"無料のオンライン通貨コンバーター Fxverter で {name}（{code}）のリアルタイム為替レートを確認。{code} から USD・EUR・GBP など 140 以上の通貨へ換算できます。",
        "curIdxDesc":"Fxverter は米ドル、ユーロ、トルコリラ、日本円など 141 の世界通貨に対応。各通貨のリアルタイム参考レートと専用ページを提供します。",
        "supportDesc":"Fxverter は無料で、広告もトラッキングもありません。役に立ったら開発をご支援ください。すべての寄付が無料で使い続ける力になります。",
 },
 "de": {
        "curTitle":"{name} ({code}) — Aktuelle Wechselkurse und Währungsrechner | Fxverter",
        "curDesc":"Aktuelle Wechselkurse für {name} ({code}): {code} mit dem kostenlosen Fxverter-Konverter in USD, EUR, GBP und über 140 weitere Währungen umrechnen. Kurse, Fakten, Rechner.",
        "curIdxDesc":"Fxverter unterstützt 141 Weltwährungen — US-Dollar, Euro, Türkische Lira, Japanischer Yen und mehr. Aktuelle Referenzkurse und eine eigene Seite pro Währung.",
        "supportDesc":"Fxverter ist kostenlos, ohne Werbung und Tracking. Wenn es dir hilft, unterstütze die Weiterentwicklung — jeder Beitrag hält es für alle kostenlos.",
 },
 "fr": {
        "curTitle":"{name} ({code}) — Taux de change en direct et convertisseur | Fxverter",
        "curDesc":"Taux de change en direct de {name} ({code}) : convertissez {code} en USD, EUR, GBP et plus de 140 devises avec le convertisseur gratuit Fxverter. Taux, fiches et calculateur.",
        "curIdxDesc":"Fxverter prend en charge 141 devises — dollar américain, euro, livre turque, yen japonais et plus. Taux de référence en direct et une page par devise.",
        "supportDesc":"Fxverter est gratuit, sans publicité ni suivi. S'il vous est utile, soutenez son développement — chaque contribution le garde gratuit pour tous.",
 },
 "es": {
        "curTitle":"{name} ({code}) — Tipos de cambio en vivo y conversor | Fxverter",
        "curDesc":"Tipos de cambio en vivo de {name} ({code}): convierte {code} a USD, EUR, GBP y más de 140 monedas con el conversor gratuito de Fxverter. Tipos, datos y calculadora.",
        "curIdxDesc":"Fxverter admite 141 monedas del mundo: dólar estadounidense, euro, lira turca, yen japonés y más. Tipos de referencia en vivo y una página por moneda.",
        "supportDesc":"Fxverter es gratis, sin anuncios ni seguimiento. Si te resulta útil, apoya su desarrollo: cada contribución lo mantiene gratis para todos.",
 },
 "pt": {
        "curTitle":"{name} ({code}) — Taxas de câmbio ao vivo e conversor | Fxverter",
        "curDesc":"Taxas de câmbio ao vivo do {name} ({code}): converta {code} em USD, EUR, GBP e mais de 140 moedas com o conversor gratuito da Fxverter. Taxas, fatos e calculadora.",
        "curIdxDesc":"A Fxverter suporta 141 moedas do mundo — dólar americano, euro, lira turca, iene japonês e mais. Taxas de referência ao vivo e uma página por moeda.",
        "supportDesc":"A Fxverter é gratuita, sem anúncios e sem rastreamento. Se for útil para você, apoie o desenvolvimento — cada contribuição a mantém gratuita para todos.",
 },
 "ru": {
        "curTitle":"{name} ({code}) — Актуальный курс и конвертер валют | Fxverter",
        "curDesc":"Актуальный курс {name} ({code}): конвертируйте {code} в USD, EUR, GBP и ещё 140+ валют с бесплатным конвертером Fxverter. Курс, факты, калькулятор.",
        "curIdxDesc":"Fxverter поддерживает 141 мировую валюту — доллар США, евро, турецкую лиру, японскую иену и другие. Актуальные курсы и отдельная страница для каждой.",
        "supportDesc":"Fxverter бесплатен — без рекламы и отслеживания. Если сервис полезен, поддержите его разработку: каждый вклад сохраняет его бесплатным для всех.",
 },
 "ar": {
        "curTitle":"{name} ({code}) — أسعار الصرف المباشرة ومحوّل العملات | Fxverter",
        "curDesc":"أسعار الصرف المباشرة لـ {name} ({code}): حوّل {code} إلى الدولار الأمريكي واليورو والجنيه الإسترليني وأكثر من 140 عملة بمحوّل Fxverter المجاني. أسعار ومعلومات وحاسبة.",
        "curIdxDesc":"يدعم Fxverter 141 عملة عالمية — الدولار الأمريكي واليورو والليرة التركية والين الياباني وغيرها. أسعار مرجعية مباشرة وصفحة خاصة لكل عملة.",
        "supportDesc":"Fxverter مجاني وبدون إعلانات أو تتبع. إذا وجدته مفيدًا، ادعم تطويره — كل مساهمة تُبقيه مجانيًا للجميع.",
 },
 "hi": {
        "curTitle":"{name} ({code}) — लाइव विनिमय दरें और मुद्रा परिवर्तक | Fxverter",
        "curDesc":"{name} ({code}) की लाइव विनिमय दरें: मुफ़्त Fxverter कन्वर्टर से {code} को USD, EUR, GBP और 140+ अन्य मुद्राओं में बदलें। दरें, जानकारी और कैलकुलेटर।",
        "curIdxDesc":"Fxverter 141 विश्व मुद्राओं को सपोर्ट करता है — अमेरिकी डॉलर, यूरो, तुर्की लीरा, जापानी येन और भी बहुत कुछ। हर मुद्रा के लिए लाइव दरें और समर्पित पेज।",
        "supportDesc":"Fxverter मुफ़्त है — कोई विज्ञापन नहीं, कोई ट्रैकिंग नहीं। अगर यह आपके काम आता है, तो इसके विकास को सपोर्ट करें — हर योगदान इसे सबके लिए मुफ़्त रखता है।",
 },
 "id": {
        "curTitle":"{name} ({code}) — Kurs Real-time dan Konverter Mata Uang | Fxverter",
        "curDesc":"Kurs real-time {name} ({code}): konversi {code} ke USD, EUR, GBP dan 140+ mata uang lain dengan konverter Fxverter gratis. Kurs, fakta, dan kalkulator.",
        "curIdxDesc":"Fxverter mendukung 141 mata uang dunia — Dolar AS, Euro, Lira Turki, Yen Jepang, dan lainnya. Kurs referensi real-time dan halaman khusus per mata uang.",
        "supportDesc":"Fxverter gratis, tanpa iklan dan pelacakan. Jika bermanfaat, dukung pengembangannya — setiap kontribusi menjaganya tetap gratis untuk semua.",
 },
 "ms": {
        "curTitle":"{name} ({code}) — Kadar Semasa dan Penukar Mata Wang | Fxverter",
        "curDesc":"Kadar semasa {name} ({code}): tukar {code} kepada USD, EUR, GBP dan 140+ mata wang lain dengan penukar Fxverter percuma. Kadar, fakta dan kalkulator.",
        "curIdxDesc":"Fxverter menyokong 141 mata wang dunia — Dolar AS, Euro, Lira Turki, Yen Jepun dan banyak lagi. Kadar rujukan semasa dan halaman khusus setiap mata wang.",
        "supportDesc":"Fxverter percuma, tanpa iklan dan penjejakan. Jika ia berguna, sokong pembangunannya — setiap sumbangan mengekalkannya percuma untuk semua.",
 },
 "ko": {
        "curTitle":"{name}({code}) — 실시간 환율 및 통화 변환기 | Fxverter",
        "curDesc":"{name}({code}) 실시간 환율: 무료 Fxverter 변환기로 {code}을(를) USD, EUR, GBP 등 140개 이상 통화로 변환하세요. 환율, 정보, 계산기 제공.",
        "curIdxDesc":"Fxverter는 미국 달러, 유로, 튀르키예 리라, 일본 엔 등 141개 세계 통화를 지원합니다. 각 통화의 실시간 참조 환율과 전용 페이지를 제공합니다.",
        "supportDesc":"Fxverter는 무료이며 광고와 추적이 없습니다. 유용하다면 개발을 지원해 주세요. 모든 후원이 모두를 위한 무료 서비스를 유지합니다.",
 },
 "vi": {
        "curTitle":"{name} ({code}) — Tỷ giá trực tuyến và chuyển đổi tiền tệ | Fxverter",
        "curDesc":"Tỷ giá trực tuyến của {name} ({code}): đổi {code} sang USD, EUR, GBP và hơn 140 loại tiền với bộ chuyển đổi Fxverter miễn phí. Tỷ giá, thông tin, máy tính.",
        "curIdxDesc":"Fxverter hỗ trợ 141 loại tiền tệ thế giới — Đô la Mỹ, Euro, Lira Thổ Nhĩ Kỳ, Yên Nhật và hơn thế. Tỷ giá tham chiếu trực tuyến và trang riêng cho từng loại.",
        "supportDesc":"Fxverter miễn phí, không quảng cáo và không theo dõi. Nếu hữu ích, hãy ủng hộ phát triển — mỗi đóng góp giúp nó miễn phí cho mọi người.",
 },
 "th": {
        "curTitle":"{name} ({code}) — อัตราแลกเปลี่ยนสดและตัวแปลงสกุลเงิน | Fxverter",
        "curDesc":"อัตราแลกเปลี่ยนสดของ {name} ({code}): แปลง {code} เป็น USD, EUR, GBP และอีก 140+ สกุล ด้วยตัวแปลงสกุลเงิน Fxverter ฟรี พร้อมข้อมูลและเครื่องคำนวณ",
        "curIdxDesc":"Fxverter รองรับ 141 สกุลเงินทั่วโลก — ดอลลาร์สหรัฐ ยูโร ลีราตุรกี เยนญี่ปุ่น และอื่น ๆ พร้อมอัตราอ้างอิงสดและหน้าเฉพาะสำหรับแต่ละสกุลเงิน",
        "supportDesc":"Fxverter ใช้ฟรี ไม่มีโฆษณาและไม่ติดตามข้อมูล หากเป็นประโยชน์ สนับสนุนการพัฒนาได้ — ทุกการสนับสนุนช่วยให้ฟรีต่อไปสำหรับทุกคน",
 },
 "fa": {
        "curTitle":"{name} ({code}) — نرخ ارز لحظه‌ای و مبدل ارز | Fxverter",
        "curDesc":"نرخ ارز لحظه‌ای {name} ({code}): با مبدل رایگان Fxverter، {code} را به دلار، یورو، پوند و بیش از ۱۴۰ ارز دیگر تبدیل کنید. نرخ، اطلاعات و ماشین‌حساب.",
        "curIdxDesc":"Fxverter از ۱۴۱ ارز جهانی پشتیبانی می‌کند — دلار آمریکا، یورو، لیر ترکیه، ین ژاپن و بیشتر. نرخ مرجع لحظه‌ای و صفحه اختصاصی برای هر ارز.",
        "supportDesc":"Fxverter رایگان است، بدون تبلیغ و ردیابی. اگر برایتان مفید است، از توسعه‌اش حمایت کنید — هر مشارکتی آن را برای همه رایگان نگه می‌دارد.",
 },
 "uk": {
        "curTitle":"{name} ({code}) — Актуальний курс і конвертер валют | Fxverter",
        "curDesc":"Актуальний курс {name} ({code}): конвертуйте {code} в USD, EUR, GBP та ще 140+ валют із безкоштовним конвертером Fxverter. Курс, факти, калькулятор.",
        "curIdxDesc":"Fxverter підтримує 141 світову валюту — долар США, євро, турецьку ліру, японську єну та інші. Актуальні курси та окрема сторінка для кожної.",
        "supportDesc":"Fxverter безкоштовний — без реклами та відстеження. Якщо сервіс корисний, підтримайте його розробку: кожен внесок зберігає його безкоштовним.",
 },
 "el": {
        "curTitle":"{name} ({code}) — Ζωντανές ισοτιμίες και μετατροπέας νομισμάτων | Fxverter",
        "curDesc":"Ζωντανές ισοτιμίες για {name} ({code}): μετατρέψτε {code} σε USD, EUR, GBP και 140+ νομίσματα με τον δωρεάν μετατροπέα Fxverter. Ισοτιμίες, στοιχεία, αριθμομηχανή.",
        "curIdxDesc":"Το Fxverter υποστηρίζει 141 νομίσματα — δολάριο ΗΠΑ, ευρώ, τουρκική λίρα, ιαπωνικό γεν και άλλα. Ζωντανές ισοτιμίες και σελίδα για κάθε νόμισμα.",
        "supportDesc":"Το Fxverter είναι δωρεάν, χωρίς διαφημίσεις και παρακολούθηση. Αν σας φανεί χρήσιμο, υποστηρίξτε την ανάπτυξή του — κάθε συνεισφορά το κρατά δωρεάν.",
 },
 "bn": {
        "curTitle":"{name} ({code}) — লাইভ বিনিময় হার এবং মুদ্রা রূপান্তরকারী | Fxverter",
        "curDesc":"{name} ({code}) লাইভ বিনিময় হার: ফ্রি Fxverter কনভার্টার দিয়ে {code} থেকে USD, EUR, GBP সহ ১৪০+ মুদ্রায় রূপান্তর করুন। হার, তথ্য ও ক্যালকুলেটর।",
        "curIdxDesc":"Fxverter ১৪১টি বিশ্ব মুদ্রা সমর্থন করে — মার্কিন ডলার, ইউরো, তুর্কি লিরা, জাপানি ইয়েন সহ আরও অনেক। প্রতিটি মুদ্রার জন্য লাইভ হার ও আলাদা পেজ।",
        "supportDesc":"Fxverter ফ্রি — কোনো বিজ্ঞাপন নেই, ট্র্যাকিং নেই। কাজে লাগলে এর উন্নয়নে সহযোগিতা করুন — প্রতিটি অনুদান এটি সবার জন্য ফ্রি রাখে।",
 },
 "pl": {
        "curTitle":"{name} ({code}) — Aktualne kursy walut i przelicznik | Fxverter",
        "curDesc":"Aktualne kursy {name} ({code}): przelicz {code} na USD, EUR, GBP i ponad 140 innych walut dzięki darmowemu przelicznikowi Fxverter. Kursy, fakty, kalkulator.",
        "curIdxDesc":"Fxverter obsługuje 141 walut świata — dolar amerykański, euro, lira turecka, jen japoński i więcej. Aktualne kursy referencyjne i osobna strona każdej waluty.",
        "supportDesc":"Fxverter jest darmowy — bez reklam i śledzenia. Jeśli jest pomocny, wesprzyj jego rozwój — każdy wkład pozwala mu pozostać darmowym dla wszystkich.",
 },
 "nl": {
        "curTitle":"{name} ({code}) — Actuele wisselkoersen en valutaomrekenner | Fxverter",
        "curDesc":"Actuele wisselkoersen van {name} ({code}): reken {code} om naar USD, EUR, GBP en 140+ andere valuta met de gratis Fxverter-omrekenner. Koersen, feiten, rekenmachine.",
        "curIdxDesc":"Fxverter ondersteunt 141 wereldvaluta's — Amerikaanse dollar, euro, Turkse lira, Japanse yen en meer. Actuele referentiekoersen en een eigen pagina per valuta.",
        "supportDesc":"Fxverter is gratis, zonder advertenties en tracking. Vind je het handig, steun dan de ontwikkeling — elke bijdrage houdt het voor iedereen gratis.",
 },
 "it": {
        "curTitle":"{name} ({code}) — Tassi di cambio in tempo reale e convertitore | Fxverter",
        "curDesc":"Tassi di cambio in tempo reale di {name} ({code}): converti {code} in USD, EUR, GBP e oltre 140 valute con il convertitore gratuito Fxverter. Tassi, schede, calcolatrice.",
        "curIdxDesc":"Fxverter supporta 141 valute del mondo — dollaro USA, euro, lira turca, yen giapponese e altro. Tassi di riferimento in tempo reale e una pagina per valuta.",
        "supportDesc":"Fxverter è gratuito, senza pubblicità né tracciamento. Se lo trovi utile, sostieni lo sviluppo — ogni contributo lo mantiene gratuito per tutti.",
 },
 "ro": {
        "curTitle":"{name} ({code}) — Cursuri de schimb în timp real și convertor | Fxverter",
        "curDesc":"Cursuri de schimb în timp real pentru {name} ({code}): transformă {code} în USD, EUR, GBP și peste 140 de valute cu convertorul gratuit Fxverter. Cursuri, date, calculator.",
        "curIdxDesc":"Fxverter suportă 141 de valute mondiale — dolar american, euro, liră turcească, yen japonez și altele. Cursuri de referință în timp real și o pagină pentru fiecare.",
        "supportDesc":"Fxverter este gratuit, fără reclame și fără urmărire. Dacă îți este util, susține dezvoltarea — fiecare contribuție îl menține gratuit pentru toți.",
 },
 "cs": {
        "curTitle":"{name} ({code}) — Aktuální kurzy měn a převodník | Fxverter",
        "curDesc":"Aktuální kurzy {name} ({code}): převeďte {code} na USD, EUR, GBP a více než 140 dalších měn s bezplatným převodníkem Fxverter. Kurzy, fakty, kalkulačka.",
        "curIdxDesc":"Fxverter podporuje 141 světových měn — americký dolar, euro, tureckou liru, japonský jen a další. Aktuální referenční kurzy a samostatná stránka pro každou měnu.",
        "supportDesc":"Fxverter je zdarma — bez reklam a sledování. Pomáhá vám? Podpořte jeho vývoj — každý příspěvek ho udrží zdarma pro všechny.",
 },
 "da": {
        "curTitle":"{name} ({code}) — Aktuelle valutakurser og valutaberegner | Fxverter",
        "curDesc":"Aktuelle valutakurser for {name} ({code}): omregn {code} til USD, EUR, GBP og 140+ andre valutaer med den gratis Fxverter-omregner. Kurser, fakta, beregner.",
        "curIdxDesc":"Fxverter understøtter 141 verdensvalutaer — amerikanske dollar, euro, tyrkisk lira, japanske yen og flere. Aktuelle referencerekurser og en egen side for hver valuta.",
        "supportDesc":"Fxverter er gratis — uden reklamer og sporing. Hjælper det dig, så støt udviklingen — hvert bidrag holder det gratis for alle.",
 },
 "sv": {
        "curTitle":"{name} ({code}) — Aktuella växelkurser och valutakonverterare | Fxverter",
        "curDesc":"Aktuella växelkurser för {name} ({code}): konvertera {code} till USD, EUR, GBP och 140+ andra valutor med den gratis Fxverter-omvandlaren. Kurser, fakta, kalkylator.",
        "curIdxDesc":"Fxverter stödjer 141 världsvalutor — amerikanska dollar, euro, turkisk lira, japansk yen med flera. Aktuella referenskurser och en egen sida per valuta.",
        "supportDesc":"Fxverter är gratis — utan reklam och spårning. Hjälper det dig, stöd utvecklingen — varje bidrag håller det gratis för alla.",
 },
 "lo": {
        "curTitle":"{name} ({code}) — ອັດຕາແລກປ່ຽນສົດ ແລະ ຕົວແປງສະກຸນເງິນ | Fxverter",
        "curDesc":"ອັດຕາແລກປ່ຽນສົດຂອງ {name} ({code}): ແປງ {code} ເປັນ USD, EUR, GBP ແລະ 140+ ສະກຸນເງິນ ດ້ວຍຕົວແປງເງິນ Fxverter ຟຣີ ພ້ອມຂໍ້ມູນ ແລະ ເຄື່ອງຄິດໄລ່.",
        "curIdxDesc":"Fxverter ຮອງຮັບ 141 ສະກຸນເງິນທົ່ວໂລກ — ໂດລາສະຫະລັດ, ເອີໂຣ, ລີຣາຕວກກີ, ເຢນຍີ່ປຸ່ນ ແລະ ອື່ນໆ. ອັດຕາອ້າງອີງສົດ ແລະ ໜ້າສະເພາະສຳລັບແຕ່ລະສະກຸນ.",
        "supportDesc":"Fxverter ຟຣີ ບໍ່ມີໂຄສະນາ ແລະ ບໍ່ຕິດຕາມ. ຖ້າເປັນປະໂຫຍດ, ສະໜັບສະໜູນການພັດທະນາ — ທຸກການສະໜັບສະໜູນຊ່ວຍໃຫ້ຟຣີສຳລັບທຸກຄົນ.",
 },
 "tl": {
        "curTitle":"{name} ({code}) — Live na Exchange Rates at Tagapagpalit ng Pera | Fxverter",
        "curDesc":"Live na exchange rates ng {name} ({code}): i-convert ang {code} sa USD, EUR, GBP at 140+ iba pang pera gamit ang libreng Fxverter converter. Rates, facts, calculator.",
        "curIdxDesc":"Sinusuportahan ng Fxverter ang 141 world currency — US Dollar, Euro, Turkish Lira, Japanese Yen at marami pa. Live reference rates at nakalaang pahina bawat pera.",
        "supportDesc":"Libre ang Fxverter — walang ads at walang tracking. Kapaki-pakinabang ba? Suportahan ang pagpapaunlad nito — bawat ambag panatilihing libre para sa lahat.",
 },
}
