# -*- coding: utf-8 -*-
"""Turkish (tr) translations of the trust pages (About / Privacy Policy /
Terms of Use / Contact / Feedback).

Mirrors the structure of TRUST["en"] in trust_l10n.py: one entry per page,
with title, meta description and an ordered list of sections —
["h", heading], ["p", paragraph] or ["li", list item]. The feedback entry
also carries the "form" dict with placeholders, buttons and status messages.
"""

TRUST_LANG = {
    "about": {
        "title": "Fxverter Hakkında — Ücretsiz, Açık Kaynaklı Döviz Çevirici",
        "desc": "Fxverter'in arkasında kim var, neden var ve onu farklı kılan nedir: Dürüst referans kurları ve sade dilli rehberler sunan, gizlilik öncelikli, açık kaynaklı bir döviz çevirici.",
        "sections": [
            ["p", "Fxverter, tamamen tarayıcınızda çalışan ücretsiz, açık kaynaklı bir çevrimiçi döviz çeviricisidir. 140'tan fazla dünya para birimi için referans döviz kurlarını gösterir; API anahtarı, kayıt ya da kurulum gerektirmez — siteyi açarsınız ve çevirmeye başlarsınız."],
            ["h", "Neden bunu geliştirdik"],
            ["p", "Çoğu çevirici site, gerçek kuru pop-up'ların, kayıt duvarlarının ve uygulama kurulum ısrarlarının altına gömer. Biz tam tersini istedik: Dürüst orta piyasa referans kurunu önce gösteren ve sonra yolunuzdan çekilen hızlı, özel bir araç. Ürünün tamamı, her cihazda çalışan, yedi dilde sunulan ve kurulumdan sonra çevrimdışı bile çalışabilen tek bir statik sayfadır."],
            ["h", "Onu farklı kılan nedir"],
            ["li", "Hesap yok, izleme yok — çevirimler tarayıcınızda yerel olarak çalışır"],
            ["li", "Üç değiştirilebilir kamuya açık veri kaynağı: Frankfurter (Avrupa Merkez Bankası referans kurları), ExchangeRate-API ve Fawaz Currency API"],
            ["li", "Kendi sayfasına sahip 40 başlıca para birimi: Canlı dönüştürme tabloları, 30/90 günlük trend grafikleri ve para birimi profilleri"],
            ["li", "Döviz kurlarının gerçekte nasıl işlediğini sade bir dille açıklayan rehberler"],
            ["li", "Uygulama olarak yüklenebilir (PWA): Bilinen son kurlarla çevrimdışı çalışmaya devam eder"],
            ["h", "Veriler"],
            ["p", "Kurlar, kamuya açık merkez bankası ve piyasa kaynaklarından gelen, günlük güncellenen gösterge niteliğinde referans kurlarıdır. Bunlar, Google'da ya da finans haberlerinde gördüğünüz ölçütün aynısıdır — karşılaştırma ve planlama için yararlıdır, belirli bir transfer için sözleşmeye dayalı bir kotasyon değildir."],
            ["h", "Arkasında kim var"],
            ["p", "Fxverter, bağımsız bir geliştirici tarafından geliştirilmekte ve sürdürülmekte, kullanıcıları tarafından desteklenmektedir. Tam kaynak kodu GitHub'da herkese açıktır — herkes onu denetleyebilir, kendi sunucusunda barındırabilir ya da iyileştirmelerle katkıda bulunabilir."],
            ["p", "Sorularınız, düzeltmeleriniz ya da fikirleriniz mi var? Şuraya yazın: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — her şeyi okuyoruz."],
        ],
    },
    "privacy": {
        "title": "Gizlilik Politikası | Fxverter",
        "desc": "Fxverter'in neyi topladığı ve neyi toplamadığı: Çerez gerekmez, hesap gerekmez, yalnızca anonim istatistikler — ayrıca reklam ve üçüncü taraf hizmetleri nasıl yönetilir.",
        "sections": [
            ["p", "Fxverter, hiçbir kişisel bilgi vermeden kullanılabilecek şekilde tasarlanmıştır. Bu politika, sitenin neyi topladığını ve neyi toplamadığını, ayrıca reklam ve üçüncü taraf hizmetlerinin nasıl yönetildiğini açıklar. Son güncelleme: Eylül 2026."],
            ["h", "Neyi toplamıyoruz"],
            ["p", "Hesap gerekmez ve sitenin kendisi hiçbir reklam çerezi ayarlamaz. Çevirimler tarayıcınızda yerel olarak çalışır — çevirdiğiniz tutarları ya da para birimi çiftlerini asla görmeyiz."],
            ["h", "Otomatik olarak toplanan bilgiler"],
            ["p", "Genel kullanımı anlamak ve aracı geliştirmek için anonim, toplu ziyaret istatistikleri (sayfa görüntülemeleri ve ülke, çerezsiz) toplanabilir. Bu istatistikler sizi tanımlamak için kullanılamaz."],
            ["h", "Göndermeyi seçtiğiniz bilgiler"],
            ["p", "Geri bildirim formunu kullanırsanız, gönderdiğiniz ad, e-posta adresi ve ileti yalnızca geri bildiriminizi okumak ve yanıtlamak için kullanılır. Projeyi desteklerseniz ödeme, kayıtlı satıcı (merchant of record) olarak Creem.io tarafından işlenir — tam ödeme ayrıntılarınızı asla almayız. Destekçiler, yalnızca açık rızaları durumunda adlarıyla listelenir."],
            ["h", "Üçüncü taraf hizmetleri"],
            ["p", "Döviz kurları, tarayıcınız tarafından doğrudan kamuya açık API'lerden alınır (Frankfurter/ECB, ExchangeRate-API, Fawaz Currency API) — bu istekler cihazınızdan gelir, sunucularımızdan geçmez. Site statik dosyalar olarak barındırılır ve anonim istatistikler Cloudflare üzerinden çalışabilir."],
            ["h", "Reklam"],
            ["p", "Bu site, Google AdSense üzerinden sunulan reklamlar gösterebilir. Google dahil üçüncü taraf sağlayıcılar, bu ya da diğer web sitelerine önceki ziyaretlerinize dayanarak reklam sunmak için çerezleri ve benzer teknolojileri kullanır. Google'ın reklam çerezlerini kullanması, Google'ın ve iş ortaklarının, sitemize ve/veya internetteki diğer sitelere yaptığınız ziyaretlere dayanarak size reklam sunmasını mümkün kılar."],
            ["p", "Kişiselleştirilmiş reklamlardan <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google Reklam Ayarları</a> üzerinden çıkabilir ya da üçüncü taraf sağlayıcı çerezlerini <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a> üzerinden reddedebilirsiniz. Yasanın gerektirdiği yerlerde — örneğin AEA'da ve Birleşik Krallık'ta — kişiselleştirilmiş reklam yalnızca onayınızla gösterilir; aksi takdirde kişiselleştirilmemiş reklam kullanılır. Ayrıntılar için <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">Google'ın, hizmetlerini kullanan sitelerden gelen bilgileri nasıl kullandığına</a> bakın."],
            ["h", "Yerel depolama"],
            ["p", "Tema seçiminiz, yazı tipi boyutunuz, kaydettiğiniz para birimi çiftleri ve yükleme banner'ı zamanlaması, tarayıcınızın yerel depolamasında saklanır. Bu veriler cihazınızdan asla ayrılmaz ve tarayıcı ayarlarınız aracılığıyla istediğiniz zaman temizlenebilir."],
            ["h", "Saklama süresi ve haklarınız"],
            ["p", "Geri bildirim iletileri yalnızca yanıt vermek için gerekli olan süre boyunca saklanır. Gönderdiğiniz herhangi bir geri bildirimin silinmesini, <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> adresine yazarak isteyebilirsiniz."],
            ["h", "Bu politikada yapılan değişiklikler"],
            ["p", "Sitenin veri uygulamaları değişirse bu sayfa güncellenecek ve yukarıdaki tarih revize edilecektir. Değişiklikten sonra siteyi kullanmaya devam etmeniz, güncellenen politikayı kabul ettiğiniz anlamına gelir."],
        ],
    },
    "terms": {
        "title": "Kullanım Koşulları | Fxverter",
        "desc": "Fxverter'i kullanmanın temel kuralları: Kurlar gösterge niteliğinde referans değerlerdir, kotasyon değildir; hizmet olduğu gibi sağlanır; ayrıca sorumluluk, fikri mülkiyet ve kabul edilebilir kullanım nasıl düzenlenmiştir.",
        "sections": [
            ["p", "fxverter.com'u kullanarak bu koşulları kabul etmiş olursunuz. Kabul etmiyorsanız lütfen siteyi kullanmayın. Son güncelleme: Eylül 2026."],
            ["h", "Hizmet"],
            ["p", "Fxverter, ücretsiz, açık kaynaklı bir çevrimiçi döviz çeviricisidir; açık ya da zımni hiçbir garanti olmaksızın, “olduğu gibi” ve “erişilebilir olduğu şekilde” sağlanır — bunlara doğruluk, erişilebilirlik ya da belirli bir amaca uygunluk da dahildir."],
            ["h", "Döviz kurları yalnızca gösterge niteliğindedir"],
            ["p", "Gösterilen tüm kurlar, merkez bankaları ve açık döviz API'leri gibi kamuya açık kaynaklardan derlenen, genellikle günde bir kez güncellenen referans kurlarıdır. Bunlar karşılaştırma ölçütleridir — kotasyon değildir, finansal tavsiye değildir ve hiçbir sağlayıcının size gerçekte vereceği fiyat değildir. Bunları finansal işlemler, banka transferleri, faturalandırma ya da resmi muhasebe için kullanmayın; işlem yapmadan önce kuru daima bankanızla ya da finans kurumunuzla doğrulayın."],
            ["h", "Sorumluluğun sınırlandırılması"],
            ["p", "Yasanın izin verdiği en üst sınıra kadar, Fxverter'in sürdürücüleri, siteyi ya da verilerini kullanmaktan ya da kullanamamaktan doğan hiçbir kayıp ya da zarardan sorumlu tutulamaz — bunlara, gösterilen kurlara dayanılarak verilen kararlar da dahildir."],
            ["h", "Fikri mülkiyet"],
            ["p", "Kaynak kod, MIT lisansı altında açık kaynaklıdır ve GitHub'da mevcuttur. Sitenin metinleri, tasarımı ve markası Fxverter projesinin mülkiyetinde kalır; sitenin içeriğini izinsiz olarak topluca yeniden yayınlayamazsınız."],
            ["h", "Üçüncü taraf hizmetleri ve bağlantılar"],
            ["p", "Site, üçüncü taraf kamuya açık API'lere dayanır ve üçüncü taraf web sitelerine bağlantı verebilir. Bunları kontrol etmeyiz; içeriklerinden, erişilebilirliklerinden ya da uygulamalarından sorumlu değiliz."],
            ["h", "Kabul edilebilir kullanım"],
            ["p", "Hizmeti aksatmamayı, aşırı yüklemeye çalışmamayı ve otomatik araçları diğer ziyaretçiler için deneyimi bozacak biçimde kullanmamayı kabul edersiniz."],
            ["h", "Bu koşullarda yapılan değişiklikler"],
            ["p", "Bu koşullar zaman zaman güncellenebilir; güncel sürüm daima bu sayfadır. Sorunuz mu var? Şuraya yazın: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
        ],
    },
    "contact": {
        "title": "İletişim | Fxverter",
        "desc": "Fxverter ekibine nasıl ulaşırsınız: Geri bildirim, kur düzeltmeleri, lisanslama ve basın — hello@fxverter.com ya da çevrimiçi geri bildirim formu.",
        "sections": [
            ["p", "Bize ulaşmanın en hızlı yolu e-postadır: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Her iletiyi okur ve genellikle birkaç gün içinde yanıt veririz."],
            ["h", "Neler yazabilirsiniz"],
            ["li", "Geri bildirim ve özellik önerileri — neyin işlediği, neyin işlemediği, neyin eksik olduğu"],
            ["li", "Düzeltmeler — bir sayfada yanlış görünen bir şey varsa, hangisi olduğunu bize söyleyin"],
            ["li", "Lisanslama ve yeniden yayınlama soruları"],
            ["li", "Basın ve ortaklık talepleri"],
            ["h", "Hatalar ve kod sorunları"],
            ["p", "Fxverter açık kaynaklıdır — hata raporları ve pull request'ler doğrudan projenin GitHub deposunda memnuniyetle karşılanır; orada herkese açık ve izlenebilirdir."],
            ["h", "Kurlar hakkında bir not"],
            ["p", "Tüm kurlar, kamuya açık kaynaklardan gelen, günlük güncellenen gösterge niteliğinde referans değerlerdir — bunun pratikte ne anlama geldiğini <a href=\"../guides/\">rehberlerde</a> bulabilirsiniz. “Yanlış” bir kur hakkında yazmadan önce, lütfen günün aynı saatinde ikinci bir kaynakla karşılaştırın: Referans kurları ile sağlayıcı kotasyonları arasındaki küçük farklar normaldir."],
            ["h", "Gizlilik"],
            ["p", "E-posta adresiniz yalnızca size yanıt vermek için kullanılır — bülten yok, pazarlama yok. Ayrıntılar için <a href=\"../privacy/\">Gizlilik Politikası</a> sayfasına bakın."],
        ],
    },
    "feedback": {
        "title": "Geri Bildirim Gönder | Fxverter",
        "desc": "Neyin işlediğini, neyin bozulduğunu ve neyin eksik olduğunu bize anlatın — Fxverter geri bildirim formu doğrudan ekibin gelen kutusuna ulaşır, hesap gerekmez.",
        "sections": [
            ["p", "Bir hata, tuhaf görünen bir kur ya da Fxverter'i daha yararlı hale getirecek bir fikir mi buldunuz? Aşağıdaki form doğrudan gelen kutumuza ulaşır — hesap gerekmez ve yaklaşık otuz saniye sürer."],
            ["h", "Bize en çok yardımcı olan"],
            ["li", "Hangi sayfayı ya da özelliği kullanıyordunuz"],
            ["li", "Beklentiniz neydi ve gerçekte ne oldu"],
            ["li", "Sorun görselse tarayıcınız ya da cihazınız"],
            ["h", "E-posta mı tercih edersiniz?"],
            ["p", "<a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> adresine yazın — ya da aşağıdaki formu kullanın; aynı yere ulaşır."],
        ],
        "form": {
            "name": "Ad (isteğe bağlı)",
            "email": "E-posta (isteğe bağlı — yalnızca yanıt istiyorsanız)",
            "message": "İletiniz",
            "send": "Geri bildirim gönder",
            "ok": "✓ Geri bildirim gönderildi — teşekkürler!",
            "empty": "Lütfen önce bir ileti yazın.",
            "fail": "Gönderim başarısız oldu — lütfen doğrudan hello@fxverter.com adresine e-posta gönderin.",
        },
    },
}

LABELS = {
    "about": "Hakkında",
    "privacy": "Gizlilik Politikası",
    "terms": "Kullanım Koşulları",
    "contact": "İletişim",
}
