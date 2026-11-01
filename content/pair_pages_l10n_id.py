# -*- coding: utf-8 -*-
"""Konten bahasa Indonesia untuk halaman pasangan mata uang ("USD ke EUR").

PAIR_UI_L10N berisi padanan string dari pair_pages.PAIR_UI["en"] (placeholder
{f} {t} {d} tetap dipertahankan). PAIR_CONTENT_L10N berisi 15 pasangan dari
PAIR_CONTENT["en"], kuncinya identik dengan versi Inggris. build-lang-pages.py
menggabungkan keduanya ke PAIR_UI / PAIR_CONTENT untuk bahasa id.
"""

PAIR_UI_L10N = {
    "pairConvert": "Konverter real-time",
    "pairRateHead": "Kurs saat ini",
    "pairAsOf": "Kurs referensi per {d}. Konverter real-time di atas selalu mengambil kurs terbaru — tabel di bawah adalah cuplikan saat halaman dibangun, untuk gambaran.",
    "pairAmounts": "Jumlah umum: {f} ke {t}",
    "pairReverse": "Jumlah umum: {t} ke {f}",
    "pairMore": "Konversi {f} lainnya",
    "pairMorePairs": "Pasangan mata uang lainnya",
    "pairIntroHead": "Tentang nilai tukar {f} ke {t}",
    "pairCurLinks": "Halaman mata uang",
    "pairMetaTmpl": ("Konversi {f} ke {t} dengan kurs real-time: kurs {f}/{t} hari ini, kalkulator gratis, "
                     "tabel jumlah umum dan apa yang memengaruhi pasangan mata uang ini."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD ke EUR — kurs hari ini, konverter gratis dan tabel jumlah",
        "description": "Konversi dolar AS ke euro dengan kurs real-time: nilai tukar USD/EUR hari ini, kalkulator gratis, tabel jumlah umum dan faktor yang memengaruhi pasangan ini.",
        "h1": "USD ke EUR — konversi dolar AS ke euro",
        "intro": [
            "USD/EUR adalah pasangan mata uang yang paling banyak diperdagangkan di dunia — sekitar seperempat seluruh perputaran pasar valas — itulah sebabnya pasangan ini memiliki spread paling rapat dan pasar terdalam dari segala konversi. Kursnya semata harga satu dolar AS dalam euro, ditentukan terus-menerus oleh perdagangan global, arus investasi, dan selisih suku bunga antara Federal Reserve dan Bank Sentral Eropa.",
            "Untuk konversi sehari-hari, pertanyaan praktisnya adalah berapa margin yang Anda bayarkan di atas kurs tengah pasar yang ditampilkan di sini. Bank biasanya menambahkan 1–4 persen; layanan kartu dan transfer bervariasi lebar. Memeriksa kurs real-time sebelum pembelian atau transfer langsung memberi tahu apakah sebuah penawaran adil.",
        ],
        "faq": [
            ("Bagaimana nilai tukar USD ke EUR ditentukan?",
             "Kurs ini mengambang bebas — penawaran dan permintaan atas kedua mata uang menetapkan harganya sepanjang waktu, dipengaruhi terutama oleh kebijakan suku bunga Fed dan ECB, inflasi di kedua sisi Atlantik, serta sentimen risiko global. Tidak ada target tetap atau terkelola."),
            ("Kapan waktu terbaik mengonversi USD ke EUR?",
             "Likuiditas terdalam dan spread paling rapat terjadi saat jam perdagangan Eropa dan AS saling tumpang tindih (kira-kira 13:00–17:00 UTC). Tidak ada yang dapat memprediksi arah jangka pendek dengan andal, sehingga untuk jumlah besar lebih aman mengonversi bertahap daripada menunggu hari yang lebih baik."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD ke GBP — kurs hari ini, konverter gratis dan pendorong utama pound",
        "description": "Konversi dolar AS ke pound sterling dengan kurs real-time: kurs USD/GBP hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan pound.",
        "h1": "USD ke GBP — konversi dolar AS ke pound sterling",
        "intro": [
            "Kurs dolar–pound, dijuluki “cable” merujuk pada kabel telegraf transatlantik yang pertama kali mengantarnya pada 1860-an, adalah salah satu kurs yang paling lama terus dikutip di dunia. Kini kurs ini mencerminkan selisih suku bunga antara Federal Reserve dan Bank of England, inflasi Inggris, serta kondisi perdagangan dan fiskal Britania.",
            "Sterling paling aktif diperdagangkan pada jam London, dan pasangan ini rawan bergerak tajam di sekitar data ekonomi serta pengumuman fiskal Inggris. Membandingkan setiap penawaran dengan kurs tengah pasar di bawah adalah cara tercepat melihat berapa besar margin yang diambil penyedia layanan.",
        ],
        "faq": [
            ("Mengapa pound sterling lebih bernilai daripada dolar AS?",
             "Harga per satuan yang lebih tinggi tidak berarti ekonomi lebih kuat — itu cerminan sejarah dan penomoran. Pound adalah mata uang dominan dunia ketika dolar belum ada; angkanya sendiri tidak berkata apa-apa tentang kekuatan ekonomi relatif atau daya beli."),
            ("Apa yang paling menggerakkan USD/GBP?",
             "Keputusan suku bunga Fed dan Bank of England, data inflasi Inggris, serta berita politik dan fiskal dari Westminster. Pada hasil suara Brexit 2016 pound jatuh sekitar 10 persen dalam sehari — pengingat bahwa sterling membawa risiko politik yang tak dimiliki kebanyakan mata uang besar."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD ke JPY — kurs hari ini, kalkulator gratis dan tabel nilai tukar",
        "description": "Konversi dolar AS ke yen Jepang dengan kurs real-time: kurs USD/JPY hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan yen.",
        "h1": "USD ke JPY — konversi dolar AS ke yen Jepang",
        "intro": [
            "USD/JPY adalah pasangan mata uang paling banyak diperdagangkan kedua di dunia dan barometer klasik selisih suku bunga Amerika–Jepang. Karena suku bunga Jepang bertahun-tahun bertahan dekat nol, yen menjadi mata uang pendanaan favorit dunia — ia melemah saat pasar percaya diri dan menguat tajam saat krisis membongkar posisi-posisi itu.",
            "Pasangan ini juga dipantau karena intervensi resmi Jepang: Kementerian Keuangan berulang kali membeli yen saat yen melemah terlalu jauh, terlalu cepat. Konversi besar sebaiknya diperiksa terhadap kurs tengah pasar, karena margin ritel pada JPY bisa mengejutkan lebarnya.",
        ],
        "faq": [
            ("Mengapa yen terkadang jatuh jauh terhadap dolar?",
             "Terutama karena selisih suku bunga. Saat suku bunga AS tinggi dan suku bunga Jepang dekat nol, investor menjual yen untuk membeli aset dolar berimbal hasil lebih tinggi — carry trade. Yen bisa melorot berbulan-bulan, lalu melompat keras ketika posisi itu dibongkar."),
            ("Bisakah pemerintah Jepang mengubah kurs USD/JPY?",
             "Ia bisa melawan arah pasar, bukan membalikkannya. Jepang pernah berintervensi dengan membeli atau menjual yen saat pergerakan menjadi kacau, terkadang dengan puluhan miliar dolar dalam satu episode. Intervensi menghaluskan lintasan; arah jangka panjang yang ditetapkan fundamental jarang berubah karenanya."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD ke CNY — kurs hari ini, konverter gratis dan cara kerja kurs terkelola",
        "description": "Konversi dolar AS ke yuan Tiongkok dengan kurs real-time: kurs USD/CNY hari ini, kalkulator gratis, tabel jumlah dan cara kerja kurs terkelola.",
        "h1": "USD ke CNY — konversi dolar AS ke yuan Tiongkok",
        "intro": [
            "Kurs dolar–yuan adalah pasangan mata uang terbesar yang dikelola oleh bank sentral. Setiap pagi People’s Bank of China menetapkan fixing harian, dan kurs onshore (CNY) hanya boleh bergerak dalam koridor di sekitarnya — alasan USD/CNY bergerak jauh lebih kecil dari hari ke hari dibanding bobot ekonominya.",
            "Surplus perdagangan Tiongkok, kontrol modal, dan sasaran kebijakan semuanya membentuk kurs. Untuk konversi, ingat bahwa CNY onshore dan CNH offshore bisa sedikit berbeda, dan konversi mata uang perorangan di Tiongkok tunduk pada aturan kontrol modal. Selalu bandingkan penawaran dengan kurs referensi di bawah.",
        ],
        "faq": [
            ("Apakah yuan Tiongkok dapat dikonversi bebas?",
             "Belum sepenuhnya. Konversi terkait perdagangan mudah, tetapi arus investasi lintas batas dikendalikan lewat kuota dan izin. Karena itu versi offshore (CNH) diperdagangkan sedikit berbeda dari CNY onshore — selisihnya mencerminkan seberapa mahal memindahkan uang melewati perbatasan."),
            ("Mengapa USD/CNY nyaris tidak bergerak dibanding pasangan lain?",
             "Karena dikelola oleh bank sentral. Fixing harian dan koridor perdagangan menjaga kurs stabil terhadap dolar, sejalan dengan preferensi kebijakan Tiongkok akan keteraturan dalam perdagangan. Terkelola bukan berarti tetap: dalam hitungan bulan dan tahun kurs tetap bergerak mengikuti fundamental."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD ke INR — kurs hari ini, konverter gratis dan koridor remitansi",
        "description": "Konversi dolar AS ke rupee India dengan kurs real-time: kurs USD/INR hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan rupee.",
        "h1": "USD ke INR — konversi dolar AS ke rupee India",
        "intro": [
            "USD/INR adalah salah satu koridor remitansi terpenting di dunia — India menerima remitansi lebih banyak daripada negara mana pun — dan pasangan pasar berkembang yang ramai diperdagangkan. Reserve Bank of India mengendalikan volatilitas, bukan level: ia menghaluskan pergerakan tajam dengan cadangannya tetapi membiarkan rupee menemukan tren jangka panjangnya.",
            "Kisah struktural rupee adalah depresiasi bertahap terhadap dolar, didorong diferensial inflasi dan neraca berjalan India, diselingi peristiwa risiko global. Bagi siapa pun yang mengirim uang ke India, selisih antara kurs tengah pasar dan kurs yang ditawarkan adalah tempat biaya sesungguhnya bersembunyi.",
        ],
        "faq": [
            ("Mengapa rupee India terdepresiasi dari waktu ke waktu?",
             "Terutama karena diferensial inflasi dan defisit perdagangan: India mengimpor jauh lebih banyak daripada mengekspor, dan selisihnya dibiayai masuknya modal. RBI menghaluskan lintasannya, tetapi selama puluhan tahun rupee perlahan melemah terhadap dolar — hal yang wajar bagi ekonomi berkembang."),
            ("Bagaimana mendapatkan kurs terbaik saat mengirim uang ke India?",
             "Bandingkan kurs yang ditawarkan dengan kurs tengah pasar sebelum mengirim, bukan hanya biayanya. Layanan remitansi khusus biasanya mengungguli transfer bank pada koridor ini, dan selisih 1 persen pun berarti besar untuk transfer keluarga rutin selama setahun."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD ke CAD — kurs hari ini, konverter gratis dan penggerak loonie",
        "description": "Konversi dolar AS ke dolar Kanada dengan kurs real-time: kurs USD/CAD hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan loonie.",
        "h1": "USD ke CAD — konversi dolar AS ke dolar Kanada",
        "intro": [
            "USD/CAD — “loonie” — adalah pasangan lima besar dunia yang dibangun di atas salah satu hubungan dagang terbesar di bumi. Kanada mengirim kira-kira tiga perempat ekspornya ke Amerika Serikat, sehingga pasangan ini diperdagangkan kuat pada pertumbuhan AS, harga energi (Kanada pengekspor minyak utama), dan selisih suku bunga antara Fed dan Bank of Canada.",
            "Saat minyak naik, CAD biasanya menguat; ketika kekhawatiran pertumbuhan global menghantam, ia melemah bersama mata uang komoditas pada umumnya. Pasangan ini likuid sepanjang waktu, dan penawaran dengan selisih pecahan persen dari kurs tengah pasar mudah ditemukan — margin lebar selalu patut dipertanyakan.",
        ],
        "faq": [
            ("Mengapa dolar Kanada disebut loonie?",
             "Merujuk pada burung loon — burung yang tertera pada koin satu dolar yang diperkenalkan 1987. Julukan itu melekat dan kini merujuk mata uangnya sendiri dalam slang valas, seperti “loonie menguat hari ini”."),
            ("Apakah harga minyak benar-benar memengaruhi USD/CAD?",
             "Ya, terlihat jelas. Minyak mentah dan produk terkait adalah kategori ekspor terbesar Kanada, sehingga minyak yang naik cenderung membawa lebih banyak dolar ke Kanada dan mengangkat CAD. Pedagang memperlakukan pasangan ini sebagai tarikan kasar pada pasar energi sekaligus suku bunga kedua negara."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD ke AUD — kurs hari ini, kalkulator gratis dan tabel konversi",
        "description": "Konversi dolar AS ke dolar Australia dengan kurs real-time: kurs USD/AUD hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan Aussie.",
        "h1": "USD ke AUD — konversi dolar AS ke dolar Australia",
        "intro": [
            "Dolar Australia adalah mata uang komoditas klasik: nasibnya mengikuti ekspor bijih besi, batu bara, dan gas, dan terutama permintaan Tiongkok atas semuanya. USD/AUD dengan demikian menjadi salah satu indikator waktu-nyata paling bersih untuk nafsu risiko global — Aussie menguat saat perdagangan dunia membludak dan melemah pada episode penghindaran risiko.",
            "Kebijakan suku bunga Reserve Bank of Australia dan Fed menggerakkan ayunan jangka pendek. Populasi kerja-liburan dan pelajar di Australia menjadikan USD→AUD (dan sebaliknya) konversi rutin yang berulang, di mana margin kurs 1 persen pun terakumulasi dengan cepat.",
        ],
        "faq": [
            ("Mengapa dolar Australia begitu sensitif terhadap Tiongkok?",
             "Tiongkok adalah pasar ekspor terbesar Australia dengan selisih jauh, terutama untuk bijih besi pembuatan baja. Ketika konstruksi Tiongkok melambat, harga komoditas dan AUD biasanya jatuh bersama — mata uang ini bekerja seperti barometer waktu-nyata industri berat Tiongkok."),
            ("Apakah AUD mata uang tempat berlindung yang aman?",
             "Justru sebaliknya: pedagang menyebutnya mata uang risk-on. Dalam kepanikan global — 2008, 2020 — uang mengalir ke dolar AS dan Aussie cenderung jatuh paling keras di antara mata uang besar. Siklikalitas itulah alasan pedagang carry dan pengamat pertumbuhan memantau Aussie dengan ketat."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD ke CHF — kurs hari ini, konverter gratis dan peran SNB",
        "description": "Konversi dolar AS ke franc Swiss dengan kurs real-time: kurs USD/CHF hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan franc.",
        "h1": "USD ke CHF — konversi dolar AS ke franc Swiss",
        "intro": [
            "Franc Swiss adalah mata uang tempat berlindung aman utama dunia: ketika perang, tekanan perbankan, atau kepanikan pasar melanda, uang mengalir ke Swiss dan CHF menguat. USD/CHF karena itu cenderung turun dalam krisis global bahkan saat dolar sendiri menjadi tempat perlindungan — franc semata tempat berteduh yang lebih kuat.",
            "Bank Nasional Swiss (SNB) aktif membentuk kurs, dari batas bawah euro yang terkenal 2011–2015 hingga intervensi besar sejak itu. Untuk konversi, Swiss juga mengingatkan bahwa pasangan mata uang negara kaya tetap bisa membawa margin ritel lebar, terutama di bandara dan hotel — selalu periksa referensi kurs tengah pasar.",
        ],
        "faq": [
            ("Mengapa franc Swiss dianggap tempat berlindung aman?",
             "Satu abad netralitas, utang rendah, surplus neraca berjalan, dan bank sentral yang kredibel menjadikan franc tempat parkir bawaan bagi uang yang kabur dari risiko. Inflasi Swiss juga berjalan jauh di bawah AS dan kawasan euro selama puluhan tahun, memelihara daya beli mata uangnya."),
            ("Apa yang dilakukan SNB pada Januari 2015?",
             "Ia tiba-tiba meninggalkan batas atas kekuatan franc terhadap euro. USD/CHF dan EUR/CHF runtuh sekitar 20–30 persen dalam hitungan menit — salah satu pergerakan intraday terbesar yang pernah terjadi pada pasangan besar, dan alasan pedagang tetap menghormati istilah “risiko SNB”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD ke MXN — kurs hari ini, konverter gratis dan pasar paling likuid",
        "description": "Konversi dolar AS ke peso Meksiko dengan kurs real-time: kurs USD/MXN hari ini, kalkulator gratis, tabel jumlah dan pasangan paling likuid di benua Amerika.",
        "h1": "USD ke MXN — konversi dolar AS ke peso Meksiko",
        "intro": [
            "USD/MXN adalah pasangan mata uang pasar berkembang paling banyak diperdagangkan di benua Amerika dan salah satu yang paling likuid di dunia. Peso diperdagangkan pada segala hal yang menggerakkan ekonomi AS — kebijakan dagang, pertumbuhan, selisih suku bunga antara Fed dan Banxico — ditambah harga minyak dan koridor remitansi raksasa dari Amerika Serikat.",
            "Karena sangat likuid, pasangan ini bergerak cepat terhadap sentimen risiko global: target carry trade klasik yang menguat di pasar tenang dan melompat liar saat kepanikan. Bagi pelancong dan pengirim remitansi, margin 3–6 persen lazim di bandara — kurs tengah pasar di bawah adalah tolok ukur pembanding.",
        ],
        "faq": [
            ("Mengapa USD/MXN begitu volatil?",
             "Suku bunga tinggi di Meksiko menarik uang carry jangka pendek yang pergi cepat dalam situasi stres; peso juga aset referensi bagi seluruh perdagangan dan berita politik AS–Meksiko. Kombinasinya membuatnya likuid tetapi mudah tersentak — pergerakan harian besar adalah hal normal, bukan kerusakan."),
            ("Apa cara termurah mengirim dolar ke Meksiko?",
             "Layanan remitansi khusus secara konsisten mengungguli bank dan toko transfer tunai pada koridor ini. Bandingkan jumlah yang sampai dengan kurs tengah pasar: pada transfer 300 dolar, selisih antara penawaran yang adil dan margin 5 persen bisa setara upah harian penuh di sana."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD ke PHP — kurs hari ini, konverter gratis dan remitansi OFW",
        "description": "Konversi dolar AS ke peso Filipina dengan kurs real-time: kurs USD/PHP hari ini, kalkulator gratis, tabel jumlah dan koridor remitansi besar Filipina.",
        "h1": "USD ke PHP — konversi dolar AS ke peso Filipina",
        "intro": [
            "Peso Filipina ditopang salah satu arus remitansi terbesar dunia: jutaan pekerja Filipina di luar negeri (OFW) mengirim uang pulang, dan masuk dolar itu adalah pilar ekonomi. USD/PHP dengan demikian diperdagangkan pada nafsu risiko global, harga minyak (Filipina importir bersih), dan kebijakan Bangko Sentral ng Pilipinas.",
            "Kurs resminya dikelola dengan tangan ringan — bank sentral mengizinkan penyesuaian bertahap sambil menghaluskan lonjakan. Bagi keluarga OFW dan pelancong, selisih antarpenyedia pada koridor ini lebar, sehingga memeriksa kurs tengah pasar sebelum mengirim adalah cara paling mudah untuk berhemat.",
        ],
        "faq": [
            ("Bagaimana remitansi memengaruhi peso Filipina?",
             "Masuk dolar yang stabil dari pekerja di luar negeri menopang peso dan neraca pembayaran negara — beberapa persen dari PDB setiap tahun. Ketika risiko global naik atau ekonomi negara tujuan melemah, remitansi melunak dan peso biasanya mengikuti."),
            ("Lebih baik mengonversi USD ke PHP di AS atau di Filipina?",
             "Tergantung penyedianya, bukan negaranya. Kedua sisi koridor punya pilihan murah dan mahal; angka penentunya adalah berapa peso yang benar-benar diterima penerima. Bandingkan penawaran dengan kurs tengah pasar alih-alih percaya pada toko yang paling dekat."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR ke GBP — kurs hari ini, konverter gratis dan tabel jumlah",
        "description": "Konversi euro ke pound sterling dengan kurs real-time: kurs EUR/GBP hari ini, kalkulator gratis, tabel jumlah dan faktor yang memengaruhi pasangan ini.",
        "h1": "EUR ke GBP — konversi euro ke pound sterling",
        "intro": [
            "EUR/GBP adalah cross Eropa klasik: dua ekonomi yang mengirim kira-kira separuh perdagangannya satu sama lain, dipisahkan satu perbatasan mata uang. Karena keduanya mata uang negara maju berinflasi rendah, pasangan ini bergerak jauh lebih kecil daripada cross dolar — hakikatnya taruhan pada keberuntungan relatif kawasan euro dan Inggris.",
            "Selisih suku bunga antara ECB dan Bank of England menggerakkan sebagian besar tren, sementara berita politik dan fiskal Inggris menyumbang lonjakan. Bagi pekerja lintas selat, pensiunan, dan bisnis, stabilitas pasangan ini justru membuat perbedaan kurs kecil makin berarti: margin 1 persen adalah porsi besar dari total pergerakan tahunan.",
        ],
        "faq": [
            ("Mengapa EUR/GBP lebih tenang daripada EUR/USD?",
             "Baik euro maupun pound bukan mata uang risiko global, sehingga arus perlindungan dunia melewatinya. Pasangan ini sebagian besar mencerminkan ekonomi relatif Inggris–Uni Eropa dan diferensial suku bunga yang berubah lambat — meski bisa melonjak keras pada berita politik Inggris, seperti yang ditunjukkan 2016."),
            ("Bagaimana Brexit masih memengaruhi EUR/GBP?",
             "Secara struktural. Friksi dagang baru sejak 2021 membuat ekonomi Inggris sedikit lebih tertutup terhadap Uni Eropa, yang oleh sebagian besar ekonom dikaitkan dengan sterling yang struktural lebih lemah. Setiap putaran negosiasi aturan dagang Inggris–Uni Eropa masih menggerakkan pasangan ini."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR ke CHF — kurs hari ini, konverter gratis dan peran Bank Nasional Swiss",
        "description": "Konversi euro ke franc Swiss dengan kurs real-time: kurs EUR/CHF hari ini, kalkulator gratis, tabel jumlah dan peran SNB pada pasangan ini.",
        "h1": "EUR ke CHF — konversi euro ke franc Swiss",
        "intro": [
            "EUR/CHF adalah uji lakmus tempat berlindung aman Eropa: setiap kali tekanan kawasan euro meningkat — krisis utang 2011, kepanikan perbankan, perang di benua itu — uang mengalir ke Swiss dan pasangan ini turun. Bank Nasional Swiss memantau kurs ini lebih ketat daripada kurs mana pun, dan berulang kali berintervensi agar franc tidak mencekik ekspor Swiss.",
            "Sejarah modern pasangan ini dramatis: batas bawah 1,20 sejak 2011, lalu pelepasan patokan Januari 2015 yang menghasilkan kejatuhan kilat 20–30 persen dalam hitungan menit. Sejak itu franc diperdagangkan sebagai tempat berlindung yang bersih, meski kadang terlalu kuat — dan SNB tetap menjadi pemain aktif di pasar ini.",
        ],
        "faq": [
            ("Mengapa Bank Nasional Swiss begitu peduli pada EUR/CHF?",
             "Karena ekonomi Swiss menjual ke Eropa. Franc yang terlalu kuat membuat ekspor Swiss tak kompetitif dan menarik inflasi di bawah target, sehingga SNB membeli mata uang asing (dan pernah memberlakukan suku bunga negatif) untuk membatasi kekuatan franc. Ia berintervensi pada pasangan ini lebih dari hampir bank sentral mana pun di pasar besar."),
            ("Apakah EUR/CHF pasangan yang stabil untuk dimiliki?",
             "Stabil di masa tenang dan meledak di krisis — kebalikan dari terdiversifikasi. Pelepasan patokan 2015 tetap menjadi peringatan buku teks bahwa janji bank sentral untuk membatasi mata uang bisa ditarik seketika. Siapa pun yang menganggap pasangan ini bebas risiko belajar sebaliknya dalam satu pagi."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR ke PLN — kurs hari ini, konverter gratis dan prospek adopsi euro",
        "description": "Konversi euro ke zloty Polandia dengan kurs real-time: kurs EUR/PLN hari ini, kalkulator gratis, tabel jumlah dan faktor yang menggerakkan zloty.",
        "h1": "EUR ke PLN — konversi euro ke zloty Polandia",
        "intro": [
            "Polandia adalah ekonomi terbesar keenam Uni Eropa yang masih memakai mata uangnya sendiri, dan zloty adalah mata uang non-euro Uni Eropa yang paling banyak diperdagangkan. EUR/PLN diperdagangkan pada selisih suku bunga dengan Bank Nasional Polandia (NBP), dana Uni Eropa yang mengalir ke timur, pesanan pabrik Jerman bagi industri Polandia, dan risiko geopolitik kawasan.",
            "Sejak Polandia bergabung dengan Uni Eropa pada 2004, zloty menguat pada masa boom dan jatuh keras saat krisis — 2008 dan 2022 mendorong pasangan ini ke ekstrem historis. Dengan adopsi euro Polandia yang masih belum diputuskan, pasangan ini tetap menjadi ciri struktural keuangan Eropa untuk bertahun-tahun mendatang.",
        ],
        "faq": [
            ("Apakah Polandia akan mengadopsi euro dan menghapus zloty?",
             "Polandia secara hukum wajib bergabung ke euro suatu saat tetapi tidak memiliki tanggal target, dan skeptisisme publik luas. Selama belum ada lini masa adopsi yang kredibel, EUR/PLN tetap pasangan yang ramai diperdagangkan — pernyataan politik soal jadwalnya saja bisa menggerakkannya."),
            ("Mengapa EUR/PLN melonjak pada 2022?",
             "Perang di Ukraina tetangga menjadikan Polandia ekonomi garis depan seketika: arus pengungsi, belanja pertahanan, dan guncangan energi menghantam mata uang keras. Bank Nasional Polandia berintervensi menopang zloty — pergerakan paling tajam pasangan ini dalam dua dekade."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP ke JPY — kurs hari ini, konverter gratis dan pasangan paling volatil",
        "description": "Konversi pound sterling ke yen Jepang dengan kurs real-time: kurs GBP/JPY hari ini, kalkulator gratis, tabel jumlah pasangan yang paling volatil.",
        "h1": "GBP ke JPY — konversi pound sterling ke yen Jepang",
        "intro": [
            "GBP/JPY — pedagang lama menyebutnya “the beast” atau “the dragon” — adalah salah satu pasangan besar paling volatil. Ia menumpuk dua mesin risiko sekaligus: sensitivitas sterling terhadap berita politik dan fiskal Inggris, dan peran yen sebagai mata uang pendanaan dunia yang membuatnya berayun keras setiap sentimen global berbalik.",
            "Pasangan ini favorit carry trade: meminjam yen bersuku bunga mendekati nol untuk membeli pound berimbal hasil lebih tinggi. Cara itu bekerja sampai krisis memaksa semua orang membongkar posisi bersamaan — alasan GBP/JPY cenderung merambat naik bertahun-tahun lalu jatuh liar dalam hitungan minggu. Ukuran posisi dan waktu lebih menentukan di sini daripada di hampir semua pasangan besar lain.",
        ],
        "faq": [
            ("Mengapa GBP/JPY lebih volatil daripada USD/JPY?",
             "Karena mengalikan dua volatilitas. Sterling menambahkan risiko politik dan ekonomi khas Inggris di atas sentimen risiko global yang sudah menggerakkan USD/JPY. Pasangan ini tak punya ekonomi jangkar bersama, sehingga diperdagangkan hampir murni pada selisih suku bunga dan sentimen — bahan pergerakan besar."),
            ("Apa itu carry trade pada GBP/JPY?",
             "Meminjam yen pada suku bunga Jepang mendekati nol dan menginvestasikannya pada pound dengan suku bunga Inggris lebih tinggi, menyimpan selisihnya. Untung selama pasar tenang dan menghukum saat tidak: pada episode penghindaran risiko yen melonjak saat posisi carry dibongkar, sering kali 10 persen atau lebih terhadap pound dalam beberapa bulan."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD ke JPY — kurs hari ini, konverter gratis dan barometer risiko global",
        "description": "Konversi dolar Australia ke yen Jepang dengan kurs real-time: kurs AUD/JPY hari ini, kalkulator gratis, tabel jumlah barometer risiko ini.",
        "h1": "AUD ke JPY — konversi dolar Australia ke yen Jepang",
        "intro": [
            "AUD/JPY adalah barometer risiko termurni di pasar mata uang. Dolar Australia mewakili pertumbuhan global dan permintaan komoditas — terutama permintaan industri Tiongkok — sementara yen mewakili keamanan. Saat ekonomi dunia tumbuh, pasangan ini memanjat; saat kepanikan melanda, ia jatuh lebih cepat daripada hampir semua cross besar lain.",
            "Ia juga pasangan carry trade klasik: selama puluhan tahun investor meminjam yen yang murah untuk membeli Aussie berimbal hasil lebih tinggi. Arus itu membentuk tren naik panjang pasangan ini dan episode pembongkaran liarnya — 2008 tetap menjadi kisah peringatan, saat AUD/JPY kehilangan sekitar separuh nilainya dalam beberapa bulan.",
        ],
        "faq": [
            ("Mengapa pedagang menyebut AUD/JPY barometer risiko?",
             "Karena masing-masing mata uang berdiri di kutub berlawanan: Aussie naik bersama pertumbuhan global dan permintaan komoditas, yen naik bersama kecemasan. Pasangan ini karena itu bergerak bersama pasar saham dunia melebihi kebanyakan cross lain — saat ia jatuh keras, penghindaran risiko itu nyata."),
            ("Apa yang terjadi pada AUD/JPY dalam krisis 2008?",
             "Sekitar setengah nilainya hilang. Carry trade dibongkar saat kredit global membeku: investor menjual dolar Australia untuk melunasi yen pinjaman, dan pasangan ini runtuh dari di atas 100 ke angka 50-an rendah dalam beberapa bulan. Ia tetap contoh standar betapa cepat strategi carry berbalik."),
        ],
    },
}
