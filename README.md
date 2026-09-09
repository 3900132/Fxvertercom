# 💱 Fxverter

> **[🌐 Live Demo → seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)** · No API key · No backend · Just open and use

---

## 🇬🇧 English

### What is this?
A free, multilingual online currency converter that runs entirely in your browser. No server, no API key, no tracking — open the website and convert, or install it as an app (PWA).

### Features
- 🌍 **29 languages** with automatic browser language detection
- 💱 **140+ currencies** from every corner of the world
- 🔄 **3 data sources** you can switch between:
  - [Frankfurter](https://frankfurter.app) — most stable, ~33 major currencies
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+ currencies, free tier
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ currencies, CDN-hosted, zero CORS
- ⚡ **Smart caching** — rates are fetched once per session per base currency, no redundant requests
- 🔁 **Manual refresh** button with last-updated timestamp
- 🔤 **Font size control** — 3 sizes (A / A+ / A++) for accessibility
- 📱 **Mobile-first** design, works on all screen sizes
- ↔️ **RTL support** for Arabic and Persian

### Who is it for?
Travelers, freelancers, students, e-commerce sellers, investors — anyone who needs a quick and reliable currency reference.

### Who should NOT rely on it for?
Bank transfers, official invoices, accounting records, or any financial transaction requiring exact rates. All rates are **indicative** — always verify with your bank or broker before transacting.

### How to use
1. **Online:** Visit **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)**
2. **Install as an app:** Open the site in Chrome/Edge/Safari and choose "Install" — it then works like a native app (PWA).

### Language versions
Each language has its own directory (`/tr/`, `/zh/`, `/ja/`, …, 29 in total) with fully translated static HTML, linked via `rel="alternate" hreflang` — the SEO/GEO-friendly setup for search engines and AI crawlers. The root page auto-redirects visitors by browser language and defaults to English. After editing `index.html`, regenerate the language pages with:

```bash
python build-lang-pages.py
```

### Supported languages & currencies

**29 interface languages** — auto-detected on first visit, switchable in the header:

**EN** English · **TR** Türkçe · **DE** Deutsch · **FR** Français · **ES** Español · **PT** Português · **RU** Русский · **ZH** 中文 · **JA** 日本語 · **KO** 한국어 · **AR** العربية · **HI** हिन्दी · **ID** Bahasa Indonesia · **MS** Bahasa Melayu · **TL** Filipino · **IT** Italiano · **NL** Nederlands · **PL** Polski · **UK** Українська · **SV** Svenska · **TH** ไทย · **LO** ພາສາລາວ · **VI** Tiếng Việt · **EL** Ελληνικά · **BN** বাংলা · **FA** فارسی · **CS** Čeština · **RO** Română · **DA** Dansk

**141 currencies** — searchable in the app's dropdowns (per-request availability depends on the selected data source: Frankfurter ~30 majors, ExchangeRate-API 160+, Fawaz API 170+; missing pairs fall back to another source automatically):

<details>
<summary>Full currency list</summary>

**A** — AED — UAE Dirham · AFN — Afghan Afghani · ALL — Albanian Lek · AMD — Armenian Dram · ANG — NL Antillean Guilder · AOA — Angolan Kwanza · ARS — Argentine Peso · AUD — Australian Dollar · AWG — Aruban Florin · AZN — Azerbaijani Manat

**B** — BAM — Bosnia Mark · BBD — Barbados Dollar · BDT — Bangladeshi Taka · BGN — Bulgarian Lev · BHD — Bahraini Dinar · BIF — Burundian Franc · BMD — Bermudian Dollar · BND — Brunei Dollar · BOB — Bolivian Boliviano · BRL — Brazilian Real · BSD — Bahamian Dollar · BTN — Bhutanese Ngultrum · BWP — Botswanan Pula · BYN — Belarusian Ruble · BZD — Belize Dollar

**C** — CAD — Canadian Dollar · CDF — Congolese Franc · CHF — Swiss Franc · CLP — Chilean Peso · CNY — Chinese Yuan · COP — Colombian Peso · CRC — Costa Rican Colón · CUP — Cuban Peso · CVE — Cape Verdean Escudo · CZK — Czech Koruna

**D** — DJF — Djiboutian Franc · DKK — Danish Krone · DOP — Dominican Peso · DZD — Algerian Dinar

**E** — EGP — Egyptian Pound · ERN — Eritrean Nakfa · ETB — Ethiopian Birr · EUR — Euro

**F** — FJD — Fijian Dollar

**G** — GBP — British Pound · GEL — Georgian Lari · GHS — Ghanaian Cedi · GMD — Gambian Dalasi · GTQ — Guatemalan Quetzal

**H** — HKD — Hong Kong Dollar · HNL — Honduran Lempira · HRK — Croatian Kuna · HTG — Haitian Gourde · HUF — Hungarian Forint

**I** — IDR — Indonesian Rupiah · ILS — Israeli Shekel · INR — Indian Rupee · IQD — Iraqi Dinar · IRR — Iranian Rial · ISK — Icelandic Króna

**J** — JMD — Jamaican Dollar · JOD — Jordanian Dinar · JPY — Japanese Yen

**K** — KES — Kenyan Shilling · KGS — Kyrgyzstani Som · KHR — Cambodian Riel · KMF — Comorian Franc · KPW — North Korean Won · KRW — South Korean Won · KWD — Kuwaiti Dinar · KZT — Kazakhstani Tenge

**L** — LAK — Laotian Kip · LBP — Lebanese Pound · LKR — Sri Lankan Rupee · LYD — Libyan Dinar

**M** — MAD — Moroccan Dirham · MDL — Moldovan Leu · MKD — Macedonian Denar · MMK — Myanmar Kyat · MNT — Mongolian Tögrög · MRU — Mauritanian Ouguiya · MUR — Mauritian Rupee · MVR — Maldivian Rufiyaa · MWK — Malawian Kwacha · MXN — Mexican Peso · MYR — Malaysian Ringgit · MZN — Mozambican Metical

**N** — NAD — Namibian Dollar · NGN — Nigerian Naira · NIO — Nicaraguan Córdoba · NOK — Norwegian Krone · NPR — Nepalese Rupee · NZD — New Zealand Dollar

**O** — OMR — Omani Riyal

**P** — PAB — Panamanian Balboa · PEN — Peruvian Sol · PGK — Papua New Guinean Kina · PHP — Philippine Peso · PKR — Pakistani Rupee · PLN — Polish Złoty · PYG — Paraguayan Guaraní

**Q** — QAR — Qatari Riyal

**R** — RON — Romanian Leu · RSD — Serbian Dinar · RUB — Russian Ruble · RWF — Rwandan Franc

**S** — SAR — Saudi Riyal · SBD — Solomon Islands Dollar · SDG — Sudanese Pound · SEK — Swedish Krona · SGD — Singapore Dollar · SLE — Sierra Leonean Leone · SOS — Somali Shilling · SSP — South Sudanese Pound · SYP — Syrian Pound

**T** — THB — Thai Baht · TJS — Tajikistani Somoni · TMT — Turkmenistani Manat · TND — Tunisian Dinar · TOP — Tongan Paʻanga · TRY — Turkish Lira · TTD — Trinidad & Tobago Dollar · TWD — New Taiwan Dollar · TZS — Tanzanian Shilling

**U** — UAH — Ukrainian Hryvnia · UGX — Ugandan Shilling · USD — US Dollar · UYU — Uruguayan Peso · UZS — Uzbekistani Som

**V** — VES — Venezuelan Bolívar · VND — Vietnamese Dong · VUV — Vanuatu Vatu

**W** — WST — Samoan Tala

**X** — XAF — Central African CFA · XCD — East Caribbean Dollar · XOF — West African CFA · XPF — CFP Franc

**Y** — YER — Yemeni Rial

**Z** — ZAR — South African Rand · ZMW — Zambian Kwacha · ZWL — Zimbabwean Dollar

</details>

---

## 🇹🇷 Türkçe

### Bu nedir?
Tamamen tarayıcıda çalışan, hafif ve çok dilli bir döviz çevirici. Sunucu yok, API anahtarı yok, takip yok — sadece tek bir HTML dosyası.

### Özellikler
- 🌍 Tarayıcı diline göre otomatik algılama ile **29 dil** desteği
- 💱 Dünyanın her köşesinden **140+ para birimi**
- 🔄 Aralarında geçiş yapabileceğiniz **3 veri kaynağı:**
  - [Frankfurter](https://frankfurter.app) — en kararlı, ~33 ana para birimi
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+ para birimi, ücretsiz
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ para birimi, CDN, sıfır CORS
- ⚡ **Akıllı önbellekleme** — kurlar oturum başına bir kez çekilir, gereksiz istek yok
- 🔁 Son güncelleme saatiyle birlikte **manuel yenileme** butonu
- 🔤 Erişilebilirlik için **yazı boyutu kontrolü** — 3 kademe (A / A+ / A++)
- 📱 Tüm ekran boyutlarında çalışan **mobil öncelikli** tasarım
- ↔️ Arapça ve Farsça için **RTL desteği**

### Kimler kullanmalı?
Gezginler, freelancer'lar, öğrenciler, e-ticaret satıcıları, yatırımcılar — hızlı ve güvenilir bir kur referansına ihtiyaç duyan herkes.

### Kimler için uygun değil?
Banka transferleri, resmi faturalar, muhasebe kayıtları veya kesin kur gerektiren finansal işlemler. Tüm kurlar **gösterge niteliğindedir** — işlem yapmadan önce bankanızla doğrulayın.

### Nasıl kullanılır?
1. **Online:** **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)** adresini ziyaret edin
2. **Offline:** `index.html` dosyasını indirin, herhangi bir tarayıcıda açın — kurulum yok, sunucu yok.

---

## 🇩🇪 Deutsch

### Was ist das?
Ein leichtgewichtiger, mehrsprachiger Währungsrechner, der vollständig im Browser läuft. Kein Server, kein API-Schlüssel, kein Tracking — nur eine einzige HTML-Datei.

### Funktionen
- 🌍 **29 Sprachen** mit automatischer Browserspracherkennung
- 💱 **140+ Währungen** aus aller Welt
- 🔄 **3 Datenquellen** zum Umschalten:
  - [Frankfurter](https://frankfurter.app) — zuverlässigste Option, ~33 Hauptwährungen
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+ Währungen, kostenlos
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ Währungen, CDN, kein CORS
- ⚡ **Intelligentes Caching** — Kurse werden einmal pro Sitzung abgerufen
- 🔤 **Schriftgrößensteuerung** für Barrierefreiheit (A / A+ / A++)
- 📱 **Mobile-first** Design

### Für wen?
Reisende, Freelancer, Studenten, Online-Händler, Investoren — alle, die schnell einen zuverlässigen Währungsüberblick benötigen.

### Wie benutzen?
1. **Online:** **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)** besuchen
2. **Offline:** `index.html` herunterladen und im Browser öffnen.

---

## 🇫🇷 Français

### C'est quoi ?
Un convertisseur de devises léger et multilingue qui fonctionne entièrement dans votre navigateur. Pas de serveur, pas de clé API, pas de tracking — un seul fichier HTML.

### Fonctionnalités
- 🌍 **29 langues** avec détection automatique de la langue du navigateur
- 💱 **140+ devises** du monde entier
- 🔄 **3 sources de données** commutables :
  - [Frankfurter](https://frankfurter.app) — plus stable, ~33 devises principales
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+ devises, gratuit
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ devises, CDN, zéro CORS
- ⚡ **Mise en cache intelligente** — les taux sont récupérés une fois par session
- 🔤 **Contrôle de la taille de police** pour l'accessibilité (A / A+ / A++)
- 📱 Design **mobile-first**

### Comment utiliser ?
1. **En ligne :** Visiter **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)**
2. **Hors ligne :** Télécharger `index.html` et l'ouvrir dans n'importe quel navigateur.

---

## 🇪🇸 Español

### ¿Qué es esto?
Un conversor de divisas ligero y multilingüe que funciona completamente en tu navegador. Sin servidor, sin clave API, sin rastreo — solo un archivo HTML.

### Características
- 🌍 **29 idiomas** con detección automática del idioma del navegador
- 💱 **140+ divisas** de todo el mundo
- 🔄 **3 fuentes de datos** intercambiables:
  - [Frankfurter](https://frankfurter.app) — más estable, ~33 divisas principales
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+ divisas, gratis
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ divisas, CDN, sin CORS
- ⚡ **Caché inteligente** — los tipos se obtienen una vez por sesión
- 🔤 **Control del tamaño de fuente** para accesibilidad (A / A+ / A++)
- 📱 Diseño **mobile-first**

### ¿Cómo usar?
1. **Online:** Visitar **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)**
2. **Offline:** Descargar `index.html` y abrirlo en cualquier navegador.

---

## 🇨🇳 中文

### 这是什么？
一个轻量级多语言货币换算器，完全在浏览器中运行。无需服务器、无需 API 密钥、无追踪——只需一个 HTML 文件。

### 功能
- 🌍 **29种语言**，自动检测浏览器语言
- 💱 来自全球的 **140+种货币**
- 🔄 可切换的 **3个数据源**：
  - [Frankfurter](https://frankfurter.app) — 最稳定，约33种主要货币
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+种货币，免费
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+种货币，CDN，零CORS
- ⚡ **智能缓存** — 每次会话只获取一次汇率
- 🔤 **字体大小控制**，提高可访问性（A / A+ / A++）
- 📱 **移动优先**设计

### 如何使用？
1. **在线：** 访问 **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)**
2. **离线：** 下载 `index.html`，在任意浏览器中打开。

---

## 🇯🇵 日本語

### これは何ですか？
ブラウザだけで動作する軽量な多言語通貨コンバーター。サーバー不要、APIキー不要、追跡なし — HTMLファイル1つだけ。

### 機能
- 🌍 ブラウザ言語自動検出付き **29言語**対応
- 💱 世界中の **140以上の通貨**
- 🔄 切り替え可能な **3つのデータソース**：
  - [Frankfurter](https://frankfurter.app) — 最も安定、約33の主要通貨
  - [ExchangeRate-API](https://exchangerate-api.com) — 160以上の通貨、無料
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170以上の通貨、CDN、CORSなし
- ⚡ **スマートキャッシュ** — レートはセッションごとに1回のみ取得
- 🔤 アクセシビリティのための**フォントサイズ調整**（A / A+ / A++）
- 📱 **モバイルファースト**デザイン

### 使い方
1. **オンライン：** **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)** にアクセス
2. **オフライン：** `index.html` をダウンロードしてブラウザで開く。

---

## 🇧🇷 Português

### O que é isso?
Um conversor de moedas leve e multilíngue que funciona inteiramente no seu navegador. Sem servidor, sem chave API, sem rastreamento — apenas um arquivo HTML.

### Recursos
- 🌍 **29 idiomas** com detecção automática do idioma do navegador
- 💱 **140+ moedas** de todo o mundo
- 🔄 **3 fontes de dados** alternáveis:
  - [Frankfurter](https://frankfurter.app) — mais estável, ~33 moedas principais
  - [ExchangeRate-API](https://exchangerate-api.com) — 160+ moedas, gratuito
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ moedas, CDN, zero CORS
- ⚡ **Cache inteligente** — taxas buscadas uma vez por sessão
- 🔤 **Controle de tamanho de fonte** para acessibilidade (A / A+ / A++)
- 📱 Design **mobile-first**

### Como usar?
1. **Online:** Acessar **[seyyidkadir.github.io/fx-currency-converter](https://seyyidkadir.github.io/fx-currency-converter)**
2. **Offline:** Baixar `index.html` e abrir em qualquer navegador.

---

## ⚠️ Disclaimer / Yasal Uyarı

> All exchange rates are **indicative only** and sourced from free, open APIs. Do not use for financial transactions, bank transfers, or official accounting. Always verify rates with your bank or financial institution.

> Tüm döviz kurları yalnızca **gösterge niteliğindedir** ve ücretsiz, açık API'lerden alınmaktadır. Finansal işlemler, banka transferleri veya resmi muhasebe için kullanmayın. Kurları bankanız veya finansal kuruluşunuzla doğrulayın.

---

## 📄 License

MIT — free to use, modify, and distribute.

---

## 🙏 Credits

- [Frankfurter API](https://frankfurter.app)
- [ExchangeRate-API](https://exchangerate-api.com)
- [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) by @fawazahmed0
- Built with ❤️ and [Claude](https://claude.ai)
