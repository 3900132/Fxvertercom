# -*- coding: utf-8 -*-
"""Halaman kepercayaan (Tentang / Dasar Privasi / Terma / Hubungi / Maklum Balas).

Terjemahan Bahasa Melayu (ms) bagi kandungan English dalam
content/trust_l10n.py (TRUST["en"] dan FEEDBACK["en"], termasuk
seksyen contact yang telah dibetulkan kepada borang maklum balas).
Setiap entri: title, desc dan senarai seksyen yang dipaparkan
mengikut susunan — ["h", tajuk], ["p", perenggan] atau ["li", item senarai].
"""

TRUST_LANG = {
    "about": {
        "title": "Tentang Fxverter — Penukar Mata Wang Percuma dan Sumber Terbuka",
        "desc": "Siapa di sebalik Fxverter, mengapa ia wujud dan apa yang menjadikannya berbeza: penukar mata wang sumber terbuka yang mengutamakan privasi, dengan kadar rujukan yang jujur dan panduan berbahasa mudah.",
        "sections": [
            ["p", "Fxverter ialah penukar mata wang dalam talian yang percuma dan sumber terbuka, berjalan sepenuhnya dalam pelayar anda. Ia memaparkan kadar pertukaran rujukan bagi lebih 140 mata wang dunia, tidak memerlukan kunci API, pendaftaran mahupun pemasangan — anda buka laman webnya dan terus menukar."],
            ["h", "Mengapa kami membina ia"],
            ["p", "Kebanyakan tapak penukar mengebumikan kadar sebenar di sebalik pop-ups, halangan pendaftaran dan desakan memasang aplikasi. Kami mahukan sebaliknya: alat yang pantas dan peribadi yang memaparkan kadar rujukan pertengahan pasaran yang jujur lebih dahulu, kemudian tidak mengganggu. Keseluruhan produk hanyalah satu halaman statik yang berfungsi pada mana-mana peranti, dalam tujuh bahasa, malah luar talian selepas pemasangan."],
            ["h", "Apakah yang menjadikannya berbeza"],
            ["li", "Tiada akaun, tiada penjejakan — penukaran berjalan setempat dalam pelayar anda"],
            ["li", "Tiga sumber data awam yang boleh ditukar: Frankfurter (kadar rujukan Bank Pusat Eropah), ExchangeRate-API dan Fawaz Currency API"],
            ["li", "40 mata wang utama dengan halaman tersendiri: jadual penukaran segera, carta trend 30/90 hari dan profil mata wang"],
            ["li", "Panduan berbahasa mudah yang menerangkan bagaimana kadar pertukaran sebenarnya berfungsi"],
            ["li", "Boleh dipasang sebagai aplikasi (PWA) yang terus berfungsi luar talian dengan kadar terakhir yang diketahui"],
            ["h", "Mengenai data"],
            ["p", "Kadar-kadar ini ialah kadar rujukan indikatif daripada sumber bank pusat dan pasaran awam, dikemas kini setiap hari. Ia penanda aras yang sama seperti yang anda lihat di Google atau dalam berita kewangan — berguna untuk perbandingan dan perancangan, bukan sebut harga kontrak untuk pemindahan tertentu."],
            ["h", "Siapa di sebaliknya"],
            ["p", "Fxverter dibina dan diselenggara oleh seorang pembangun bebas dan disokong oleh penggunanya. Kod sumber yang lengkap adalah awam di GitHub — sesiapa sahaja boleh mengauditnya, mengehoskannya sendiri atau menyumbang penambahbaikan."],
            ["p", "Ada soalan, pembetulan atau idea? Tulis ke <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — kami membaca semuanya."],
        ],
    },
    "privacy": {
        "title": "Dasar Privasi | Fxverter",
        "desc": "Apa yang Fxverter kumpul dan tidak kumpul: tanpa cookie, tanpa akaun, statistik tanpa nama sahaja — serta bagaimana pengiklanan dan perkhidmatan pihak ketiga dikendalikan.",
        "sections": [
            ["p", "Fxverter direka bentuk supaya boleh digunakan tanpa menyerahkan sebarang maklumat peribadi. Dasar ini menerangkan apa yang dikumpul dan tidak dikumpul oleh laman ini, serta bagaimana pengiklanan dan perkhidmatan pihak ketiga dikendalikan. Kemas kini terakhir: September 2026."],
            ["h", "Apa yang kami tidak kumpul"],
            ["p", "Tiada akaun diperlukan dan tiada cookie pengiklanan ditetapkan oleh laman itu sendiri. Penukaran berjalan setempat dalam pelayar anda — kami tidak pernah melihat jumlah atau pasangan mata wang yang anda tukar."],
            ["h", "Maklumat yang dikumpul secara automatik"],
            ["p", "Statistik lawatan tanpa nama dan agregat (pandangan halaman dan negara, tanpa cookie) mungkin dikumpul untuk memahami penggunaan keseluruhan dan menambah baik alat ini. Statistik ini tidak boleh digunakan untuk mengenal pasti anda."],
            ["h", "Maklumat yang anda pilih untuk hantar"],
            ["p", "Jika anda menggunakan borang maklum balas, nama, alamat e-mel dan mesej yang anda hantar digunakan hanya untuk membaca dan membalas maklum balas anda. Jika anda menyokong projek ini, bayaran diproses oleh Creem.io sebagai peniaga rekod (merchant of record) — kami tidak pernah menerima butiran bayaran penuh anda. Penyokong disenaraikan mengikut nama hanya dengan kebenaran jelas mereka."],
            ["h", "Perkhidmatan pihak ketiga"],
            ["p", "Kadar pertukaran diambil oleh pelayar anda secara terus daripada API awam (Frankfurter/ECB, ExchangeRate-API, Fawaz Currency API) — permintaan itu datang daripada peranti anda, bukan melalui pelayan kami. Laman ini dihoskan sebagai fail statik, dan analitik tanpa nama mungkin berjalan melalui Cloudflare."],
            ["h", "Pengiklanan"],
            ["p", "Laman ini mungkin memaparkan pengiklanan yang disampaikan melalui Google AdSense. Pembekal pihak ketiga, termasuk Google, menggunakan cookie dan teknologi serupa untuk menyampaikan iklan berdasarkan lawatan anda sebelum ini ke laman ini atau laman web lain. Penggunaan cookie pengiklanan oleh Google membolehkan Google dan rakan kongsinya menyampaikan iklan kepada anda berdasarkan lawatan anda ke laman kami dan/atau tapak lain di internet."],
            ["p", "Anda boleh menarik diri daripada pengiklanan diperibadikan di <a href=\"https://adssettings.google.com\" rel=\"noopener\">Tetapan Iklan Google</a>, atau menarik diri daripada cookie pembekal pihak ketiga di <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Di tempat yang diwajibkan oleh undang-undang — contohnya di EEA dan United Kingdom — pengiklanan diperibadikan hanya dipaparkan dengan kebenaran anda, dan pengiklanan tidak diperibadikan digunakan sebaliknya. Untuk butiran, lihat <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">bagaimana Google menggunakan maklumat daripada tapak yang menggunakan perkhidmatannya</a>."],
            ["h", "Storan setempat"],
            ["p", "Pilihan tema anda, saiz fon, pasangan mata wang yang disimpan dan masa paparan sepanduk pemasangan disimpan dalam storan setempat pelayar anda. Data ini tidak pernah meninggalkan peranti anda dan boleh dibersihkan pada bila-bila masa melalui tetapan pelayar anda."],
            ["h", "Penyimpanan dan hak anda"],
            ["p", "Mesej maklum balas disimpan hanya selama yang diperlukan untuk membalas. Anda boleh meminta kami memadamkan sebarang maklum balas yang anda hantar dengan menulis ke <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
            ["h", "Perubahan kepada dasar ini"],
            ["p", "Jika amalan data laman ini berubah, halaman ini akan dikemas kini dan tarikh di atas direvisi. Penggunaan berterusan laman ini selepas perubahan bermakna anda menerima dasar yang dikemas kini."],
        ],
    },
    "terms": {
        "title": "Terma Penggunaan | Fxverter",
        "desc": "Peraturan asas penggunaan Fxverter: kadar adalah nilai rujukan indikatif, bukan sebut harga; perkhidmatan disediakan seadanya; serta bagaimana liabiliti, harta intelek dan penggunaan boleh diterima dikendalikan.",
        "sections": [
            ["p", "Dengan menggunakan fxverter.com, anda bersetuju dengan terma ini. Jika anda tidak bersetuju, sila jangan gunakan laman ini. Kemas kini terakhir: September 2026."],
            ["h", "Perkhidmatan"],
            ["p", "Fxverter ialah penukar mata wang dalam talian yang percuma dan sumber terbuka, disediakan \"seadanya\" dan \"seperti tersedia\" tanpa jaminan apa jua jenis, tersurat mahupun tersirat — termasuk ketepatan, ketersediaan atau kesesuaian untuk tujuan tertentu."],
            ["h", "Kadar pertukaran hanya indikatif"],
            ["p", "Semua kadar yang dipaparkan ialah kadar rujukan yang dikumpul daripada sumber awam seperti bank pusat dan API mata wang terbuka, biasanya dikemas kini sekali sehari. Ia penanda aras untuk perbandingan — bukan sebut harga, bukan nasihat kewangan, dan bukan harga yang mana-mana pembekal akan beri kepada anda. Jangan gunakannya untuk transaksi kewangan, pemindahan bank, penginvoisan atau perakaunan rasmi; sentiasa sahkan kadar dengan bank atau institusi kewangan anda sebelum berurusan."],
            ["h", "Had liabiliti"],
            ["p", "Setakat maksimum yang dibenarkan oleh undang-undang, penyelenggara Fxverter tidak bertanggungjawab atas sebarang kerugian atau kerosakan yang timbul daripada penggunaan, atau ketidakupayaan menggunakan, laman ini atau datanya — termasuk keputusan yang dibuat berdasarkan kadar yang dipaparkan."],
            ["h", "Harta intelek"],
            ["p", "Kod sumber adalah sumber terbuka di bawah lesen MIT dan tersedia di GitHub. Teks, reka bentuk dan jenama laman ini kekal menjadi hak milik projek Fxverter; anda tidak boleh menerbitkan semula kandungan laman ini secara keseluruhan tanpa kebenaran."],
            ["h", "Perkhidmatan dan pautan pihak ketiga"],
            ["p", "Laman ini bergantung pada API awam pihak ketiga dan mungkin memaut ke laman web pihak ketiga. Kami tidak mengawalnya dan tidak bertanggungjawab atas kandungan, ketersediaan atau amalan mereka."],
            ["h", "Penggunaan boleh diterima"],
            ["p", "Anda bersetuju untuk tidak mengganggu perkhidmatan ini, cuba membebankannya, atau menggunakan alat automatik dengan cara yang merosakkannya bagi pengunjung lain."],
            ["h", "Perubahan kepada terma ini"],
            ["p", "Terma ini mungkin dikemas kini dari semasa ke semasa; versi semasa sentiasa halaman ini. Ada soalan? Tulis ke <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
        ],
    },
    "contact": {
        "title": "Hubungi Kami | Fxverter",
        "desc": "Cara menghubungi pasukan Fxverter: maklum balas, pembetulan kadar, pelesenan dan media — hello@fxverter.com atau borang maklum balas dalam talian.",
        "sections": [
            ["p", "Cara paling pantas menghubungi kami ialah e-mel: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Kami membaca setiap mesej dan biasanya membalas dalam beberapa hari."],
            ["h", "Apa yang boleh ditulis"],
            ["li", "Maklum balas dan idea ciri — apa yang berfungsi, apa yang tidak, apa yang tiada"],
            ["li", "Pembetulan — jika ada yang kelihatan salah pada sesuatu halaman, beritahu kami halaman yang mana"],
            ["li", "Soalan pelesenan dan penerbitan semula"],
            ["li", "Pertanyaan media dan perkongsian"],
            ["h", "Cara paling pantas"],
            ["p", "Tidak berminat menulis e-mel? Guna <a href=\"../feedback/\">borang maklum balas dalam talian</a> — ia sampai ke peti masuk yang sama dan hanya mengambil masa kira-kira tiga puluh saat."],
            ["h", "Nota tentang kadar"],
            ["p", "Semua kadar ialah nilai rujukan indikatif daripada sumber awam, dikemas kini setiap hari — lihat <a href=\"../guides/\">panduan</a> untuk memahami maksudnya dalam praktik. Sebelum anda menulis tentang kadar yang \"salah\", sila bandingkan dengan sumber kedua pada waktu yang sama dalam sehari: perbezaan kecil antara kadar rujukan dan sebut harga pembekal adalah normal."],
            ["h", "Privasi"],
            ["p", "Alamat e-mel anda digunakan hanya untuk membalas anda — tiada surat berita, tiada pemasaran. Lihat <a href=\"../privacy/\">Dasar Privasi</a> untuk butiran."],
        ],
    },
    "feedback": {
        "title": "Hantar Maklum Balas | Fxverter",
        "desc": "Beritahu kami apa yang berfungsi, apa yang rosak dan apa yang tiada — borang maklum balas Fxverter sampai terus ke peti masuk pasukan, tanpa perlu akaun.",
        "sections": [
            ["p", "Menjumpai pepijat, kadar yang kelihatan janggal, atau idea yang menjadikan Fxverter lebih berguna? Borang di bawah sampai terus ke peti masuk kami — tanpa perlu akaun, dan hanya mengambil masa kira-kira tiga puluh saat."],
            ["h", "Apa yang paling membantu kami"],
            ["li", "Halaman atau ciri mana yang anda gunakan"],
            ["li", "Apa yang anda jangkakan dan apa yang sebenarnya berlaku"],
            ["li", "Pelayar atau peranti anda, jika masalahnya berkaitan paparan"],
            ["h", "Lebih suka e-mel?"],
            ["p", "Tulis ke <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — atau sahaja guna borang di bawah, kedua-duanya sampai ke tempat yang sama."],
        ],
        "form": {
            "name": "Nama (pilihan)",
            "email": "E-mel (pilihan — hanya jika anda mahu dibalas)",
            "message": "Mesej anda",
            "send": "Hantar maklum balas",
            "ok": "✓ Maklum balas dihantar — terima kasih!",
            "empty": "Sila tulis mesej dahulu.",
            "fail": "Penghantaran gagal — sila e-mel hello@fxverter.com secara terus.",
        },
    },
}

LABELS = {
    "about": "Tentang",
    "privacy": "Dasar Privasi",
    "terms": "Terma Penggunaan",
    "contact": "Hubungi Kami",
    "feedback": "Maklum Balas",
}
