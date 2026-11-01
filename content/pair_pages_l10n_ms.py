# -*- coding: utf-8 -*-
"""Kandungan bahasa Melayu (ms) untuk halaman pasangan mata wang (USD ke EUR).

PAIR_UI_L10N sepadan dengan rentetan daripada pair_pages.PAIR_UI["en"]
(pemegang tempat {f} {t} {d} dikekalkan). PAIR_CONTENT_L10N sepadan dengan
15 pasangan daripada PAIR_CONTENT["en"], kekuncinya sama dengan versi Inggeris.
build-lang-pages.py menggabungkan kedua-duanya ke dalam PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Penukar langsung",
    "pairRateHead": "Kadar pertukaran semasa",
    "pairAsOf": "Kadar rujukan pada {d}. Penukar langsung di atas sentiasa mendapatkan kadar terkini — jadual di bawah ialah tangkapan semasa pembinaan untuk panduan.",
    "pairAmounts": "Jumlah lazim: {f} kepada {t}",
    "pairReverse": "Jumlah lazim: {t} kepada {f}",
    "pairMore": "Penukaran {f} yang lain",
    "pairMorePairs": "Pasangan mata wang lain",
    "pairIntroHead": "Tentang kadar pertukaran {f} kepada {t}",
    "pairCurLinks": "Halaman mata wang",
    "pairMetaTmpl": ("Tukar {f} kepada {t} dengan kadar pertukaran langsung: kadar {f}/{t} hari ini, kalkulator percuma, "
                     "jadual jumlah lazim dan apa yang menggerakkan pasangan ini."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD ke EUR — kadar hari ini, penukar percuma dan jadual jumlah",
        "description": "Tukar dolar AS kepada euro dengan kadar langsung: kadar USD/EUR hari ini, kalkulator percuma, jadual jumlah lazim dan apa yang menggerakkan pasangan ini.",
        "h1": "USD ke EUR — tukar dolar AS kepada euro",
        "intro": [
            "USD/EUR ialah pasangan mata wang paling banyak didagangkan di dunia — kira-kira suku daripada keseluruhan perolehan dagangan pertukaran asing — dan itulah sebabnya ia mempunyai spread paling sempit serta pasaran paling dalam antara semua penukaran. Kadarnya semudah harga satu dolar AS dalam euro, ditetapkan secara berterusan oleh perdagangan global, aliran pelaburan dan jurang kadar faiz antara The Fed dengan Bank Pusat Eropa.",
            "Bagi penukaran harian, soalan praktikalnya ialah berapa margin yang anda bayar melebihi kadar tengah pasaran yang dipaparkan di sini. Bank lazimnya menambah 1–4 peratus; perkhidmatan kad dan pemindahan berbeza-beza jauh. Menyemak kadar langsung sebelum pembelian atau pemindahan memberitahu anda serta-merta sama ada sebut harga itu adil.",
        ],
        "faq": [
            ("Bagaimana kadar USD ke EUR ditentukan?",
             "Ia terapung secara bebas — bekalan dan permintaan kedua-dua mata wang menetapkan harga sepanjang masa, dipengaruhi terutamanya oleh dasar kadar faiz Fed dan ECB, inflasi di kedua-dua belah Atlantik serta sentimen risiko global. Tiada sasaran tetap atau terkawal."),
            ("Bilakah masa terbaik untuk menukar USD kepada EUR?",
             "Likuiditi paling dalam dan spread paling sempit berlaku semasa pertindihan waktu dagangan Eropah dan AS (kira-kira 13:00–17:00 UTC). Tiada siapa boleh meramalkan arah jangka pendek dengan boleh harap, maka bagi jumlah besar lebih selamat menukar secara berperingkat berbanding menunggu hari yang lebih baik."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD ke GBP — kadar hari ini, penukar percuma dan apa yang menggerakkan pound",
        "description": "Tukar dolar AS kepada pound British dengan kadar langsung: kadar USD/GBP hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan pound.",
        "h1": "USD ke GBP — tukar dolar AS kepada pound British",
        "intro": [
            "Kadar dolar–pound, digelarkan cable sempena kabel telegraf merentasi Atlantik yang pertama kali membawanya pada 1860-an, antara kadar pertukaran tertua yang terus dikutip di dunia. Hari ini ia mencerminkan jurang kadar faiz antara The Fed dengan Bank of England, inflasi United Kingdom serta kesihatan kedudukan perdagangan dan fiskal Britain.",
            "Sterling berdagang paling aktif semasa waktu London, dan pasangan ini mudah mengalami pergerakan tajam sekitar data ekonomi UK serta pengumuman fiskal. Membandingkan sebarang sebut harga dengan kadar tengah pasaran di bawah ialah cara terpantas melihat berapa besar margin yang diambil penyedia.",
        ],
        "faq": [
            ("Mengapa pound British lebih bernilai daripada dolar AS?",
             "Harga seunit yang lebih tinggi tidak bermakna ekonomi yang lebih kuat — ia mencerminkan sejarah dan pecahan. Pound ialah mata wang dominan dunia ketika dolar belum lagi wujud; angka itu sendiri tidak memberitahu apa-apa tentang kekuatan ekonomi relatif atau kuasa beli."),
            ("Apakah yang paling menggerakkan USD/GBP?",
             "Keputusan kadar faiz daripada Fed dan Bank of England, data inflasi UK serta berita politik dan fiskal dari Westminster. Semasa undian Brexit 2016 pound jatuh kira-kira 10 peratus dalam sehari — peringatan bahawa sterling membawa risiko politik yang tidak dialami kebanyakan mata wang utama."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD ke JPY — kadar hari ini, penukar percuma dan jadual kadar yen",
        "description": "Tukar dolar AS kepada yen Jepun dengan kadar langsung: kadar USD/JPY hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan yen.",
        "h1": "USD ke JPY — tukar dolar AS kepada yen Jepun",
        "intro": [
            "USD/JPY ialah pasangan mata wang kedua paling banyak didagangkan di dunia dan barometer klasik jurang kadar faiz antara Amerika Syarikat dengan Jepun. Oleh sebab kadar faiz Jepun berada hampir sifar selama dekad-dekad, yen menjadi mata wang pembiayaan kegemaran dunia — ia melemah apabila pasaran yakin dan menguat dengan tajam apabila krisis melupuskan kedudukan tersebut.",
            "Pasangan ini juga dipantau kerana campur tangan rasmi Jepun: Kementerian Kewangan berulang kali membeli yen apabila ia melemah terlalu jauh dan terlalu pantas. Penukaran besar patut disemak terhadap kadar tengah pasaran, kerana margin runcit atas JPY boleh mengelirukan lebarnya.",
        ],
        "faq": [
            ("Mengapa yen kadangkala jatuh begitu banyak terhadap dolar?",
             "Terutamanya kerana jurang kadar faiz. Apabila kadar AS tinggi dan kadar Jepun kekal hampir sifar, pelabur menjual yen untuk membeli aset dolar berpulangan lebih tinggi — niaga cadangan (carry trade). Yen boleh meluncur berbulan-bulan, kemudian melonjak dengan ganas apabila kedudukan itu dilupuskan."),
            ("Bolehkah kerajaan Jepun mengubah kadar USD/JPY?",
             "Ia boleh menentang pasaran, bukan membalikkannya. Jepun telah campur tangan dengan membeli atau menjual yen apabila pergerakan menjadi tidak terkawal, kadangkala dengan puluhan bilion dolar dalam satu episod. Campur tangan melicinkan laluan; ia jarang mengubah arah jangka panjang yang ditetapkan oleh asas ekonomi."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD ke CNY — kadar hari ini, penukar percuma dan cara kadar terkawal berfungsi",
        "description": "Tukar dolar AS kepada yuan China dengan kadar langsung: kadar USD/CNY hari ini, kalkulator percuma, jadual jumlah dan cara kadar terkawal berfungsi.",
        "h1": "USD ke CNY — tukar dolar AS kepada yuan China",
        "intro": [
            "Kadar dolar–yuan ialah pasangan mata wang terbesar yang dikuruskan oleh bank pusat. Setiap pagi Bank Rakyat China menetapkan kadar tengah harian, dan kadar dalam negeri (CNY) hanya dibenarkan bergerak dalam jalur di sekelilingnya — itulah sebab USD/CNY bergerak jauh lebih sedikit dari hari ke hari berbanding kepentingan ekonominya.",
            "Lebihan perdagangan China, kawalan modal dan matlamat dasar semuanya membentuk kadar. Bagi penukaran, ingat bahawa CNY dalam negeri dan CNH luar pesisir boleh berbeza sedikit, dan penukaran mata wang oleh individu di China tertakluk kepada peraturan kawalan modal. Sentiasa bandingkan sebut harga dengan kadar rujukan di bawah.",
        ],
        "faq": [
            ("Adakah yuan China boleh ditukar secara bebas?",
             "Tidak sepenuhnya. Penukaran berkaitan perdagangan mudah, tetapi aliran pelaburan merentasi sempadan dikawal oleh kuota dan kelulusan. Itulah sebab versi luar pesisir (CNH) berdagang pada harga sedikit berbeza daripada CNY dalam negeri — jurang itu mencerminkan seberapa mahal untuk menggerakkan wang merentasi sempadan."),
            ("Mengapa USD/CNY hampir tidak bergerak berbanding pasangan lain?",
             "Kerana bank pusat mengurusnya. Kadar tengah harian dan jalur dagangan mengekalkan kadar stabil terhadap dolar, selari dengan keutamaan dasar China untuk kebolehramalan dalam perdagangan. Terkawal tidak bermakna tetap: kadar masih menjejak asas ekonomi dari bulan ke bulan dan dari tahun ke tahun."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD ke INR — kadar hari ini, penukar percuma dan panduan wang kiriman",
        "description": "Tukar dolar AS kepada rupee India dengan kadar langsung: kadar USD/INR hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan rupee.",
        "h1": "USD ke INR — tukar dolar AS kepada rupee India",
        "intro": [
            "USD/INR antara koridor wang kiriman terpenting di dunia — India menerima lebih banyak wang kiriman daripada mana-mana negara lain — dan pasangan pasaran berkembang yang banyak didagangkan. Bank Rizab India menguruskan kemeruapan, bukan paras: ia melicinkan pergerakan tajam menggunakan rizabnya tetapi membiarkan rupee mencari trend jangka panjangnya.",
            "Kisah jangka panjang rupee ialah penyusutan beransur terhadap dolar, didorong oleh perbezaan inflasi dan baki akaun semasa India, diselangi peristiwa risiko global. Bagi sesiapa yang menghantar wang ke India, jurang antara kadar tengah pasaran dengan kadar yang ditawarkan itulah tempat kos sebenar bersembunyi.",
        ],
        "faq": [
            ("Mengapa rupee India menyusut nilai dari masa ke masa?",
             "Terutamanya perbezaan inflasi dan defisit perdagangan: India mengimport jauh lebih daripada yang dieksport, dan perbezaan itu dibiayai oleh aliran modal masuk. RBI melicinkan laluan itu, tetapi sepanjang dekad-dekad rupee telah beransur lebih lemah terhadap dolar — perkara biasa bagi ekonomi membangun."),
            ("Bagaimana saya mendapat kadar terbaik menghantar wang ke India?",
             "Bandingkan kadar yang ditawarkan dengan kadar tengah pasaran sebelum menghantar, bukan sekadar yurannya. Perkhidmatan wang kiriman khusus biasanya mengatasi wayar bank pada koridor ini, dan perbezaan walaupun 1 peratus signifikan bagi pemindahan keluarga berjadual sepanjang setahun."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD ke CAD — kadar hari ini, penukar percuma dan pengaruh harga minyak",
        "description": "Tukar dolar AS kepada dolar Kanada dengan kadar langsung: kadar USD/CAD hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan loonie.",
        "h1": "USD ke CAD — tukar dolar AS kepada dolar Kanada",
        "intro": [
            "USD/CAD — loonie — ialah pasangan global lima teratas yang dibina di atas salah satu hubungan perdagangan terbesar di dunia. Kanada menghantar kira-kira tiga perempat eksportnya ke Amerika Syarikat, maka pasangan ini berdagang berat mengikut pertumbuhan AS, harga tenaga (Kanada pengeksport minyak utama) dan jurang kadar antara Fed dengan Bank of Canada.",
            "Apabila minyak naik, CAD lazimnya menguat; apabila kebimbangan pertumbuhan global melanda, ia melemah bersama mata wang komoditi amnya. Pasangan ini likuid sepanjang masa, dan sebut harga dalam pecahan satu peratus daripada kadar tengah pasaran mudah dicari — maka margin yang lebar sentiasa patut dipersoalkan.",
        ],
        "faq": [
            ("Mengapa dolar Kanada digelar loonie?",
             "Sempena burung loon — burung pada syiling satu dolar yang diperkenalkan pada 1987. Nama gelaran itu melekat dan kini merujuk kepada mata wang itu sendiri dalam slanga pertukaran asing, seperti dalam ayat loonie menguat hari ini."),
            ("Adakah harga minyak benar-benar mempengaruhi USD/CAD?",
             "Ya, dengan jelas. Minyak mentah dan produk berkaitan ialah kategori eksport terbesar Kanada, maka minyak yang menaik membawa lebih banyak dolar ke Kanada dan mengangkat CAD. Peniaga melihat pasangan ini sebagai taruhan kasar pada pasaran tenaga serta kadar faiz kedua-dua negara."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD ke AUD — kadar hari ini, penukar percuma dan penunjuk komoditi",
        "description": "Tukar dolar AS kepada dolar Australia dengan kadar langsung: kadar USD/AUD hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan Aussie.",
        "h1": "USD ke AUD — tukar dolar AS kepada dolar Australia",
        "intro": [
            "Dolar Australia ialah mata wang komoditi klasik: nasibnya menjejak eksport bijih besi, arang batu dan gas, dan terutamanya permintaan China terhadapnya. USD/AUD dengan itu antara penunjuk masa nyata paling bersih bagi selera risiko global — Aussie menguat apabila perdagangan dunia membangun dan melemah dalam episod menjauhi risiko.",
            "Dasar kadar faiz daripada Bank Rizab Australia dan Fed menggerakkan ayunan jangka pendek. Populasi cuti kerja dan pelajar Australia menjadikan USD ke AUD (dan sebaliknya) penukaran berulang yang lazim, di mana margin kadar walaupun 1 peratus terkumpul dengan pantas.",
        ],
        "faq": [
            ("Mengapa dolar Australia begitu sensitif kepada China?",
             "China ialah pasaran eksport terbesar Australia dengan jurang jauh, terutamanya bagi bijih besi untuk pembuatan keluli. Apabila pembinaan China melambatkan, harga komoditi dan AUD lazimnya jatuh bersama — mata wang ini bertindak sebagai barometer masa nyata industri berat China."),
            ("Adakah AUD pelabuhan selamat?",
             "Sebaliknya: peniaga menggelarnya mata wang pro-risiko. Dalam panik global — 2008, 2020 — wang mengalir ke dolar AS dan Aussie lazimnya jatuh paling teruk antara mata wang utama. Kitaran itulah tepat sebab peniaga cadangan dan pemerhati pertumbuhan memantauinya begitu rapat."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD ke CHF — kadar hari ini, penukar percuma dan kisah pelabuhan selamat",
        "description": "Tukar dolar AS kepada franc Switzerland dengan kadar langsung: kadar USD/CHF hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan franc.",
        "h1": "USD ke CHF — tukar dolar AS kepada franc Switzerland",
        "intro": [
            "Franc Switzerland ialah mata wang pelabuhan selamat utama dunia: apabila perang, tekanan perbankan atau panik pasaran melanda, wang mengalir ke Switzerland dan CHF menguat. USD/CHF dengan itu cenderung jatuh dalam krisis global walaupun dolar itu sendiri tempat perlindungan — franc semudahnya tempat perlindungan yang lebih kuat.",
            "Bank Nasional Switzerland secara aktif membentuk kadar, daripada lantai euro termasyhur 2011–2015 sehingga campur tangan berat selepas itu. Bagi penukaran, Switzerland turut mengingatkan bahawa pasangan mata wang negara kaya masih boleh membawa margin runcit yang lebar, terutamanya di lapangan terbang dan hotel — sentiasa semak rujukan kadar tengah pasaran.",
        ],
        "faq": [
            ("Mengapa franc Switzerland dianggap pelabuhan selamat?",
             "Abad berkecuali, hutang rendah, lebihan akaun semasa dan bank pusat yang berwibawa menjadikan franc tempat letak lalai bagi wang yang melarikan diri daripada risiko. Inflasi Switzerland juga jauh lebih rendah daripada AS dan zon euro selama dekad-dekad, memelihara kuasa beli mata wang itu."),
            ("Apakah yang dilakukan SNB pada Januari 2015?",
             "Ia meninggalkan had kekuatan franc terhadap euro secara tiba-tiba. USD/CHF dan EUR/CHF runtuh sekitar 20–30 peratus dalam beberapa minit — antara pergerakan intrahari terbesar yang pernah berlaku bagi pasangan utama, dan sebab peniaga masih menghormati frasa risiko SNB."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD ke MXN — kadar hari ini, penukar percuma dan jadual untuk pengembara",
        "description": "Tukar dolar AS kepada peso Mexico dengan kadar langsung: kadar USD/MXN hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan peso.",
        "h1": "USD ke MXN — tukar dolar AS kepada peso Mexico",
        "intro": [
            "USD/MXN ialah pasangan pasaran berkembang paling banyak didagangkan di benua Amerika dan antara paling likuid di dunia. Peso berdagang mengikut segala-galanya yang menggerakkan ekonomi AS — dasar perdagangan, pertumbuhan, jurang kadar faiz antara Fed dengan Banxico — ditambah harga minyak serta koridor wang kiriman gergasi dari Amerika Syarikat.",
            "Kerana sangat likuid, pasangan ini bergerak pantas mengikut sentimen risiko global: ia sasaran niaga cadangan klasik yang menguat dalam pasaran tenang dan terjunam dengan ganas dalam panik. Bagi pengembara dan pengirim wang kiriman, margin 3–6 peratus lazim di lapangan terbang — kadar tengah pasaran di bawah ialah penanda aras untuk dibandingkan.",
        ],
        "faq": [
            ("Mengapa USD/MXN begitu meruap?",
             "Kadar faiz tinggi di Mexico menarik wang cadangan jangka pendek yang pergi pantas ketika tekanan; peso juga aset rujukan bagi semua perdagangan dan berita politik AS–Mexico. Gabungan itu menjadikannya likuid tetapi mudah terlompat — pergerakan harian besar adalah normal, bukan kerosakan."),
            ("Apakah cara termurah menghantar dolar ke Mexico?",
             "Perkhidmatan wang kiriman khusus konsisten mengatasi bank dan kedai pemindahan tunai pada koridor ini. Bandingkan jumlah yang sampai dengan kadar tengah pasaran: bagi pemindahan 300 dolar, perbezaan antara sebut harga yang adil dengan margin 5 peratus boleh menyamai upah sehari di tempat itu."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD ke PHP — kadar hari ini, penukar percuma dan tip wang kiriman OFW",
        "description": "Tukar dolar AS kepada peso Filipina dengan kadar langsung: kadar USD/PHP hari ini, kalkulator percuma, jadual jumlah dan tip untuk wang kiriman OFW.",
        "h1": "USD ke PHP — tukar dolar AS kepada peso Filipina",
        "intro": [
            "Peso Filipina disauhkan oleh salah satu aliran wang kiriman terbesar dunia: jutaan pekerja Filipina di luar negara menghantar wang pulang, dan aliran masuk dolar itu ialah tunjang ekonomi. USD/PHP dengan itu berdagang mengikut selera risiko global, harga minyak (Filipina pengimport bersih) dan dasar Bangko Sentral ng Pilipinas.",
            "Kadar rasmi dikuruskan dengan tangan ringan — bank pusat membenarkan penyesuaian beransur sambil melicinkan lonjakan. Bagi keluarga OFW dan pengembara, jurang antara penyedia pada koridor ini lebar, maka menyemak kadar tengah pasaran sebelum menghantar ialah cara paling mudah untuk menjimatkan.",
        ],
        "faq": [
            ("Bagaimana wang kiriman mempengaruhi peso Filipina?",
             "Aliran masuk dolar yang konsisten daripada pekerja di luar negara menyokong peso dan imbangan pembayaran negara — beberapa peratus daripada KDNK setiap tahun. Apabila risiko global meningkat atau ekonomi negara tuan rumah melemah, wang kiriman merosot dan peso lazimnya mengikut."),
            ("Adakah lebih baik menukar USD kepada PHP di Amerika Syarikat atau di Filipina?",
             "Ia bergantung kepada penyedia, bukan negara. Kedua-dua belah koridor mempunyai pilihan murah dan mahal; angka penentunya ialah berapa peso yang benar-benar diterima oleh penerima. Bandingkan sebut harga dengan kadar tengah pasaran berbanding mempercayai kedai yang paling dekat."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR ke GBP — kadar hari ini, penukar percuma dan silang Eropah klasik",
        "description": "Tukar euro kepada pound British dengan kadar langsung: kadar EUR/GBP hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan silang ini.",
        "h1": "EUR ke GBP — tukar euro kepada pound British",
        "intro": [
            "EUR/GBP ialah silang Eropah klasik: dua ekonomi yang menghantar kira-kira separuh perdagangan mereka antara satu sama lain, dipisahkan oleh satu sempadan mata wang. Oleh sebab kedua-duanya mata wang maju berinflasi rendah, pasangan ini bergerak jauh lebih kurang daripada silang dolar — ia sebenarnya pertaruhan pada nasib relatif zon euro dengan United Kingdom.",
            "Jurang kadar faiz antara ECB dengan Bank of England menggerakkan kebanyakan trend, manakala berita politik dan fiskal UK menyebabkan lonjakan. Bagi pekerja rentas Selat, pesara dan perniagaan, kestabilan pasangan ini menjadikan perbezaan kadar kecil lebih penting lagi: margin 1 peratus ialah bahagian besar daripada jumlah pergerakan tahunan.",
        ],
        "faq": [
            ("Mengapa EUR/GBP lebih tenang daripada EUR/USD?",
             "Bukan euro mahupun pound ialah mata wang risiko global, maka aliran melarikan diri ke keselamatan sedunia melaluinya. Pasangan ini kebanyakannya mencerminkan ekonomi relatif UK–EU dan perbezaan kadar yang berubah perlahan — walaupun ia boleh melonjak keras atas berita politik British, seperti yang ditunjukkan pada 2016."),
            ("Bagaimana Brexit masih mempengaruhi EUR/GBP?",
             "Secara berstruktur. Gesekan perdagangan baharu sejak 2021 menjadikan ekonomi UK sedikit kurang terbuka kepada EU, yang dikaitkan oleh kebanyakan ahli ekonomi dengan sterling yang secara struktur lebih lemah. Setiap pusingan rundingan UK–EU mengenai peraturan perdagangan masih menggerakkan pasangan ini."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR ke CHF — kadar hari ini, penukar percuma dan peranan SNB",
        "description": "Tukar euro kepada franc Switzerland dengan kadar langsung: kadar EUR/CHF hari ini, kalkulator percuma, jadual jumlah dan peranan SNB dalam pasangan ini.",
        "h1": "EUR ke CHF — tukar euro kepada franc Switzerland",
        "intro": [
            "EUR/CHF ialah ujian pelabuhan selamat Eropah: setiap kali tekanan zon euro meningkat — krisis hutang 2011, kebimbangan perbankan, perang di benua ini — wang mengalir merentasi sempadan Swiss dan pasangan ini jatuh. Bank Nasional Switzerland memantau kadar ini lebih rapat daripada kadar lain mana pun, dan telah berulang kali campur tangan agar franc tidak mencekik eksport Swiss.",
            "Sejarah moden pasangan ini dramatik: lantai 1.20 dari 2011, kemudian pelepasan tambatan pada Januari 2015 yang menghasilkan kejatuhan kilat 20–30 peratus dalam beberapa minit. Sejak itu franc berdagang sebagai perlindungan yang bersih, walaupun kadangkala terlalu kuat — dan SNB kekal peserta aktif dalam pasaran ini.",
        ],
        "faq": [
            ("Mengapa SNB begitu mengambil berat tentang EUR/CHF?",
             "Kerana ekonomi Switzerland menjual ke Eropah. Franc yang terlalu kuat menjadikan eksport Swiss tidak berdaya saing dan menarik inflasi di bawah sasaran, maka SNB membeli mata wang asing (dan pernah mengenakan kadar negatif) untuk mengehad kekuatan franc. Ia campur tangan dalam pasangan ini lebih daripada hampir mana-mana bank pusat lain dalam pasaran utama."),
            ("Adakah EUR/CHF pasangan yang stabil untuk dipegang?",
             "Stabil ketika tenang dan meletup ketika krisis — kebalikan daripada pelbagai. Pelepasan tambatan 2015 kekal amaran buku teks bahawa janji bank pusat untuk mengehad mata wang boleh ditarik balik semalaman. Sesiapa yang menganggap pasangan ini bebas risiko belajar sebaliknya dalam satu pagi."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR ke PLN — kadar hari ini, penukar percuma dan jadual jumlah zloty",
        "description": "Tukar euro kepada zloty Poland dengan kadar langsung: kadar EUR/PLN hari ini, kalkulator percuma, jadual jumlah dan apa yang menggerakkan zloty.",
        "h1": "EUR ke PLN — tukar euro kepada zloty Poland",
        "intro": [
            "Poland ialah ekonomi keenam terbesar Kesatuan Eropah yang masih menggunakan mata wangnya sendiri, dan zloty ialah antara mata wang bukan euro EU yang paling banyak didagangkan. EUR/PLN berdagang mengikut jurang kadar faiz dengan Bank Negara Poland, dana EU yang mengalir ke timur, pesanan kilang Jerman bagi industri Poland serta risiko geopolitik serantau.",
            "Sejak Poland menyertai EU pada 2004, zloty pernah menguat dalam ledakan dan jatuh teruk dalam krisis — 2008 dan 2022 menolak pasangan ini ke ekstrem bersejarah. Dengan penerimaan euro Poland yang masih belum diputuskan, pasangan ini kekal menjadi ciri struktur kewangan Eropah untuk tahun-tahun akan datang.",
        ],
        "faq": [
            ("Adakah Poland akan menerima euro dan menghapuskan zloty?",
             "Poland terikat secara undang-undang untuk menyertai euro suatu hari nanti tetapi tiada tarikh sasaran dan keraguan awam meluas. Selagi tiada garis masa penerimaan yang boleh dipercayai, EUR/PLN kekal pasangan yang aktif didagangkan — kenyataan politik tentang jadual itu sahaja boleh menggerakkannya."),
            ("Mengapa EUR/PLN melonjak pada 2022?",
             "Perang di Ukraine yang berjiran menjadikan Poland ekonomi barisan depan semalaman: aliran masuk pelarian, perbelanjaan pertahanan dan kejutan tenaga menghentam mata wang dengan berat. Bank Negara Poland campur tangan untuk menyokong zloty — pergerakan paling tajam pasangan ini dalam dua dekad."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP ke JPY — kadar hari ini, penukar percuma dan panduan pasangan meruap",
        "description": "Tukar pound British kepada yen Jepun dengan kadar langsung: kadar GBP/JPY hari ini, kalkulator percuma, jadual jumlah dan panduan bagi pasangan meruap ini.",
        "h1": "GBP ke JPY — tukar pound British kepada yen Jepun",
        "intro": [
            "GBP/JPY — peniaga lama menggelarnya binatang buas atau naga — antara pasangan mata wang utama paling meruap. Ia menumpuk dua enjin risiko: kepekaan sterling terhadap berita politik dan fiskal UK, serta peranan yen sebagai mata wang pembiayaan dunia, yang menjadikannya berayun dengan keras setiap kali sentimen global berpusing.",
            "Pasangan ini kegemaran niaga cadangan: meminjam yen berkadar hampir sifar untuk membeli pound berpulangan lebih tinggi. Itu berjalan sehingga krisis memaksa semua orang melupuskan kedudukan serentak, itulah sebab GBP/JPY cenderung memanjat bertahun-tahun dan jatuh dengan ganas dalam beberapa minggu. Saiz kedudukan dan masa lebih penting di sini berbanding hampir mana-mana pasangan utama lain.",
        ],
        "faq": [
            ("Mengapa GBP/JPY lebih meruap daripada USD/JPY?",
             "Kerana ia mendarab dua kemeruapan. Sterling menambah risiko politik dan ekonomi khusus UK di atas sentimen risiko global yang sudah menggerakkan USD/JPY. Pasangan ini tiada ekonomi sauh bersama, maka ia berdagang hampir tulen atas jurang kadar dan sentimen — bahan bagi pergerakan besar."),
            ("Apakah itu niaga cadangan dalam GBP/JPY?",
             "Meminjam yen pada kadar Jepun hampir sifar dan melabur dalam pound pada kadar UK lebih tinggi, menggapai perbezaannya. Ia menguntungkan selagi pasaran tenang dan menghukum apabila tidak: dalam episod menjauhi risiko, yen melonjak apabila kedudukan cadangan dilupuskan, kerap 10 peratus atau lebih terhadap pound dalam beberapa bulan."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD ke JPY — kadar hari ini, penukar percuma dan barometer risiko",
        "description": "Tukar dolar Australia kepada yen Jepun dengan kadar langsung: kadar AUD/JPY hari ini, kalkulator percuma, jadual jumlah dan barometer risiko global ini.",
        "h1": "AUD ke JPY — tukar dolar Australia kepada yen Jepun",
        "intro": [
            "AUD/JPY ialah barometer risiko paling tulen dalam pasaran mata wang. Dolar Australia mewakili pertumbuhan global dan permintaan komoditi — terutamanya permintaan industri China — manakala yen mewakili keselamatan. Apabila ekonomi dunia berkembang, pasangan ini mendaki; apabila panik melanda, ia jatuh lebih pantas daripada hampir mana-mana silang utama yang lain.",
            "Ia juga pasangan niaga cadangan klasik: selama dekad-dekad pelabur meminjam yen murah untuk membeli Aussie berpulangan lebih tinggi. Aliran itu membentuk trend menaik yang panjang dan perlahan serta episod pelupusan yang ganas — 2008 kekal kisah pengajaran, apabila AUD/JPY kehilangan kira-kira separuh nilainya dalam beberapa bulan.",
        ],
        "faq": [
            ("Mengapa peniaga menggelar AUD/JPY barometer risiko?",
             "Kerana setiap mata wang berada di kutub bertentangan: Aussie naik bersama pertumbuhan global dan permintaan komoditi, yen naik bersama ketakutan. Pasangan ini dengan itu bergerak bersama pasaran ekuiti dunia pada tahap yang jarang dipadankan oleh silang lain — apabila ia jatuh dengan keras, pelarian daripada risiko itu nyata."),
            ("Apakah yang berlaku kepada AUD/JPY dalam krisis 2008?",
             "Ia hampir separuh. Niaga cadangan dilupuskan apabila kredit global membeku: pelabur menjual dolar Australia untuk membayar balik yen yang dipinjam, dan pasangan ini runtuh daripada atas 100 ke paras awal 50-an dalam beberapa bulan. Ia kekal contoh piawai betapa pantas strategi cadangan berpatah balik."),
        ],
    },
}
