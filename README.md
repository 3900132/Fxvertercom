# 💱 Fxverter

> **[🌐 fxverter.com](https://fxverter.com)** · No API key · No sign-up · No tracking · 141 currencies · 29 languages | [🇨🇳 中文说明](#-中文版)

A free, multilingual online currency converter that runs entirely in your browser. No server, no account, no tracking — open the website and convert, or install it as an app (PWA).

---

## ✨ Features

- 💱 **141 currencies** from every corner of the world
- 🌍 **29 languages** with automatic browser-language detection, full RTL support for Arabic and Persian
- 🔄 **3 switchable data sources**:
  - [Frankfurter](https://frankfurter.dev) — ECB reference rates, most stable, ~30 major currencies
  - [ExchangeRate-API](https://www.exchangerate-api.com) — 160+ currencies, free tier
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ currencies, CDN-hosted, zero CORS
- ⚡ **Smart caching** — rates are fetched once per session per base currency; missing pairs fall back to another source automatically
- 📲 **Installable app (PWA)** with a guided install banner — offered once every 12 hours until installed or dismissed (with native install prompt on Android/desktop and "Add to Home Screen" guidance on iOS); works offline after install with the last known rates
- 📊 **Per-currency pages** (e.g. [USD](https://fxverter.com/currencies/usd/)) with 30/90-day trend charts, quick facts and a calculator — available in all 29 languages
- 📚 **Plain-language exchange-rate guides** (e.g. [how exchange rates work](https://fxverter.com/guides/))
- 🌓 Light / dark / auto **theme**, 3-level **font-size control** (A / A+ / A++) for accessibility
- 🔖 Saved currency pairs, share button, in-page feedback form
- ♥ Optional supporter tiers and a contact address (hello@fxverter.com) on the [support page](https://fxverter.com/support/)
- 🔒 **Privacy-first** — no cookies, no accounts, no tracking; conversions run locally in your browser

## 🚀 How to use

1. **Online:** visit **[fxverter.com](https://fxverter.com)** — the root page auto-redirects to your language
2. **Install as an app:** open the site in Chrome/Edge/Safari and accept the install banner (or use the browser's "Install app" / "Add to Home Screen") — it then works like a native app, even offline
3. **Self-host:** the site is 100% static HTML — clone the repo and serve it from any static host (GitHub Pages, Cloudflare Pages, …)

## 🛠️ Development

Five source files generate the whole site (175+ static pages); after editing any of them, run the build once:

```bash
python build-lang-pages.py
```

| Source file | What it controls |
|---|---|
| `index.html` | Main template: UI, styles, converter logic, head meta. All 29 language pages are generated from it |
| `page_content.py` | About/FAQ translations (28 languages) |
| `content/ui_strings.py` | UI strings — buttons, banners, install prompt (29 languages) |
| `content/content_ui.py` | Secondary-page chrome: currency pages, guides, support page |
| `content/currencies.py` | Currency profiles: flag, country, symbol, minor unit, about text |
| `guides/*.md` | Exchange-rate guide articles |

See `DEVELOPMENT.md` for the full workflow (build, deploy to GitHub Pages with the `fxverter.com` CNAME, PWA notes, checklist).

## 🌐 Language versions

Each language has its own directory (`/tr/`, `/zh/`, `/ja/`, …, 29 in total) with fully translated static HTML, linked via `rel="alternate" hreflang` — the SEO/GEO-friendly setup for search engines and AI crawlers.

**EN** English · **TR** Türkçe · **DE** Deutsch · **FR** Français · **ES** Español · **PT** Português · **RU** Русский · **ZH** 中文 · **JA** 日本語 · **KO** 한국어 · **AR** العربية · **HI** हिन्दी · **ID** Bahasa Indonesia · **MS** Bahasa Melayu · **TL** Filipino · **IT** Italiano · **NL** Nederlands · **PL** Polski · **UK** Українська · **SV** Svenska · **TH** ไทย · **LO** ພາສາລາວ · **VI** Tiếng Việt · **EL** Ελληνικά · **BN** বাংলা · **FA** فارسی · **CS** Čeština · **RO** Română · **DA** Dansk

## ⚠️ Disclaimer

All exchange rates are **indicative only** and sourced from free, open APIs. Do not use for financial transactions, bank transfers, or official accounting. Always verify rates with your bank or financial institution.

---

## 🇨🇳 中文版

免费的在线货币换算器，完全在浏览器中运行。无需服务器、无需注册、无追踪——打开网站即可换算，也可以安装为应用（PWA）。

### ✨ 功能

- 💱 **141 种货币**，覆盖全球
- 🌍 **29 种界面语言**，自动检测浏览器语言；阿拉伯语和波斯语完整支持从右到左（RTL）
- 🔄 **3 个可切换的数据源**：
  - [Frankfurter](https://frankfurter.dev) — 欧洲央行参考汇率，最稳定，约 30 种主要货币
  - [ExchangeRate-API](https://www.exchangerate-api.com) — 160+ 种货币，免费额度
  - [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) — 170+ 种货币，CDN 分发，零 CORS 限制
- ⚡ **智能缓存** — 每个会话每种基准货币只请求一次；某数据源缺少的货币对会自动切换到其他源获取
- 📲 **可安装应用（PWA）** — 带引导式安装横幅，未安装时每 12 小时提醒一次（可关闭）；Android/桌面调起浏览器原生安装弹窗，iOS 显示"添加到主屏幕"引导；安装后离线可用，显示最后一次缓存的汇率
- 📊 **币种详情页**（如 [人民币 CNY](https://fxverter.com/zh/currencies/cny/)）：30/90 天趋势图、币种资料、汇率计算器——29 种语言各自独立
- 📚 **汇率科普指南**（如[汇率是怎么定出来的](https://fxverter.com/zh/guides/)）
- 🌓 浅色/深色/跟随系统**主题**，三档**字号调节**（A / A+ / A++）
- 🔖 收藏常用货币对、分享按钮、页面内反馈表单
- ♥ 支持者等级与联系邮箱（hello@fxverter.com）见[支持页](https://fxverter.com/zh/support/)
- 🔒 **隐私优先** — 无 Cookie、无账号、无追踪；换算全部在本地浏览器完成

### 🚀 如何使用

1. **在线：** 访问 **[fxverter.com](https://fxverter.com)** — 首页会按浏览器语言自动跳转
2. **安装为应用：** 在 Chrome/Edge/Safari 中打开网站，接受安装横幅（或用浏览器的"安装应用 / 添加到主屏幕"）——之后像原生应用一样使用，离线也能打开
3. **自托管：** 本站是 100% 静态 HTML — 克隆仓库后可部署到任意静态托管（GitHub Pages、Cloudflare Pages 等）

### 🛠️ 开发说明

六个源文件生成整站（175+ 静态页面）；改完任意源文件后跑一次构建：

```bash
python build-lang-pages.py
```

| 源文件 | 管什么 |
|---|---|
| `index.html` | 主模板：界面、样式、换算逻辑、head 元信息。29 个语言页都由它生成 |
| `page_content.py` | About/FAQ 正文翻译（28 种语言） |
| `content/ui_strings.py` | UI 文案——按钮、横幅、安装提示（29 种语言） |
| `content/content_ui.py` | 二级页面框架：币种页、指南页、支持页 |
| `content/currencies.py` | 币种档案：国旗、国家、符号、辅币单位、介绍 |
| `guides/*.md` | 汇率指南文章 |

完整流程（构建、GitHub Pages 部署绑定 fxverter.com、PWA 说明、检查清单）见 `DEVELOPMENT.md`。

### ⚠️ 免责声明

所有汇率均为**仅供参考**的参考汇率，来自免费公开 API。请勿用于金融交易、银行汇款或正式记账——进行任何交易前请与银行或金融机构核实。

### 📄 许可证

MIT — 可自由使用、修改和分发。

---

## 🇹🇷 Türkçe

Tarayıcıda tamamen çalışan, ücretsiz ve çok dilli bir döviz çevirici. Sunucu yok, hesap gerekmez, takip yok — siteyi açın ve çevirin, ya da uygulama (PWA) olarak kurun.

**Öne çıkanlar:** 141 para birimi · 29 dil (otomatik algılama) · 3 veri kaynağı: [Frankfurter](https://frankfurter.dev) (ECB, ~30 ana para birimi), [ExchangeRate-API](https://www.exchangerate-api.com) (160+), [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) (170+) · akıllı önbellekleme, eksik parlar otomatik yedek kaynağa düşer · 12 saatlik döngüyle kurulum bildirimi gösteren, kurulumdan sonra çevrimdışı çalışan **PWA** · para başına trend grafiği ve hesap makinesi olan 141 ayrı sayfa · açıklayıcı döviz kuru rehberleri · açık/koyu/otomatik tema · 3 kademeli yazı boyutu (A / A+ / A++) · kayıtlı çiftler, paylaşım, geri bildirim formu · [destek sayfası](https://fxverter.com/tr/support/) ve hello@fxverter.com iletişim adresi · çerez yok, hesap yok, takip yok.

**Kullanım:** [fxverter.com](https://fxverter.com) adresini ziyaret edin; tarayıcı Chrome/Edge/Safari ise "Yükle / Ana ekrana ekle" ile uygulamayı kurun (kurulumdan sonra çevrimdışı çalışır). Site 100% statiktir — repoyu klonlayıp herhangi bir statik barındırıcıda çalıştırabilirsiniz.

**Geliştirme:** Kaynak dosyaları düzenledikten sonra tüm siteyi (175+ sayfa) yeniden üretmek için bir kez çalıştırın: `python build-lang-pages.py`. Ayrıntılar için `DEVELOPMENT.md`.

**Yasal uyarı:** Tüm kurlar yalnızca **gösterge niteliğindedir** ve ücretsiz, açık API'lerden alınır. Finansal işlemler, banka transferleri veya resmi muhasebe için kullanmayın; bankanızla doğrulayın.

---

## 🇩🇪 Deutsch

Ein kostenloser, mehrsprachiger Währungsrechner, der vollständig im Browser läuft. Kein Server, keine Anmeldung, kein Tracking — Website öffnen und umrechnen, oder als App (PWA) installieren.

**Highlights:** 141 Währungen · 29 Sprachen (automatische Erkennung) · 3 Datenquellen: [Frankfurter](https://frankfurter.dev) (EZB, ~30 Hauptwährungen), [ExchangeRate-API](https://www.exchangerate-api.com) (160+), [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) (170+) · intelligentes Caching, fehlende Paare weichen automatisch auf eine andere Quelle aus · **PWA** mit Installationsbanner im 12-Stunden-Rhythmus, nach der Installation offline nutzbar · 141 einzelne Währungsseiten mit Trendchart und Rechner · verständliche Wechselkurs-Ratgeber · Hell-/Dunkel-/Auto-Design · 3 Schriftgrößen (A / A+ / A++) · gespeicherte Paare, Teilen, Feedback-Formular · [Support-Seite](https://fxverter.com/de/support/) und Kontakt hello@fxverter.com · keine Cookies, keine Konten, kein Tracking.

**Nutzung:** [fxverter.com](https://fxverter.com) besuchen; in Chrome/Edge/Safari über „Installieren / Zum Startbildschirm hinzufügen" als App installieren (danach offline nutzbar). Die Seite ist 100 % statisch — Repository klonen und auf jedem statischen Hoster betreiben.

**Entwicklung:** Nach dem Bearbeiten der Quelldateien einmal `python build-lang-pages.py` ausführen, um die gesamte Website (175+ Seiten) neu zu erzeugen. Details in `DEVELOPMENT.md`.

**Haftungsausschluss:** Alle Kurse sind **nur Richtwerte** aus freien, offenen APIs. Nicht für Finanztransaktionen, Banküberweisungen oder offizielle Buchhaltung verwenden — mit deiner Bank abstimmen.

---

## 🇫🇷 Français

Un convertisseur de devises gratuit et multilingue qui fonctionne entièrement dans votre navigateur. Pas de serveur, pas de compte, pas de suivi — ouvrez le site et convertissez, ou installez-le comme application (PWA).

**Points forts :** 141 devises · 29 langues (détection automatique) · 3 sources de données : [Frankfurter](https://frankfurter.dev) (BCE, ~30 devises principales), [ExchangeRate-API](https://www.exchangerate-api.com) (160+), [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) (170+) · cache intelligent, les paires manquantes basculent automatiquement vers une autre source · **PWA** avec bannière d'installation au rythme de 12 heures, utilisable hors ligne après installation · 141 pages de devises avec graphique de tendance et calculatrice · guides clairs sur les taux de change · thème clair/sombre/auto · 3 tailles de police (A / A+ / A++) · paires enregistrées, partage, formulaire de retour · [page de soutien](https://fxverter.com/fr/support/) et contact hello@fxverter.com · pas de cookies, pas de comptes, pas de suivi.

**Utilisation :** visitez [fxverter.com](https://fxverter.com) ; dans Chrome/Edge/Safari, installez l'application via « Installer / Ajouter à l'écran d'accueil » (fonctionne ensuite hors ligne). Le site est 100 % statique — clonez le dépôt et hébergez-le où vous voulez.

**Développement :** après avoir modifié les fichiers sources, exécutez une fois `python build-lang-pages.py` pour régénérer tout le site (175+ pages). Détails dans `DEVELOPMENT.md`.

**Avertissement :** tous les taux sont **indicatifs** et proviennent d'API publiques gratuites. À ne pas utiliser pour des transactions financières, virements bancaires ou comptabilité officielle — vérifiez avec votre banque.

---

## 🇪🇸 Español

Un conversor de divisas gratuito y multilingüe que funciona completamente en tu navegador. Sin servidor, sin cuenta, sin rastreo — abre la web y convierte, o instálalo como app (PWA).

**Lo destacado:** 141 divisas · 29 idiomas (detección automática) · 3 fuentes de datos: [Frankfurter](https://frankfurter.dev) (BCE, ~30 divisas principales), [ExchangeRate-API](https://www.exchangerate-api.com) (160+), [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) (170+) · caché inteligente, los pares que faltan pasan automáticamente a otra fuente · **PWA** con banner de instalación cada 12 horas, funciona sin conexión tras instalarla · 141 páginas por divisa con gráfico de tendencia y calculadora · guías claras sobre tipos de cambio · tema claro/oscuro/auto · 3 tamaños de fuente (A / A+ / A++) · pares guardados, botón de compartir, formulario de feedback · [página de apoyo](https://fxverter.com/es/support/) y contacto hello@fxverter.com · sin cookies, sin cuentas, sin rastreo.

**Uso:** visita [fxverter.com](https://fxverter.com); en Chrome/Edge/Safari instala la app con «Instalar / Añadir a pantalla de inicio» (después funciona sin conexión). El sitio es 100 % estático — clona el repositorio y hazlo funcionar en cualquier alojamiento estático.

**Desarrollo:** tras editar los archivos fuente, ejecuta una vez `python build-lang-pages.py` para regenerar todo el sitio (175+ páginas). Detalles en `DEVELOPMENT.md`.

**Aviso legal:** todos los tipos de cambio son **solo orientativos** y provienen de APIs públicas gratuitas. No los uses para transacciones financieras, transferencias bancarias ni contabilidad oficial — verifica con tu banco.

---

## 🇯🇵 日本語

ブラウザだけで動作する、無料の多言語通貨コンバーター。サーバー不要・アカウント不要・追跡なし——サイトを開いて換算するか、アプリ（PWA）としてインストールできます。

**主な機能：** 141 通貨 · 29 言語（自動検出）· 3 つのデータソース：[Frankfurter](https://frankfurter.dev)（ECB、約 30 の主要通貨）、[ExchangeRate-API](https://www.exchangerate-api.com)（160+）、[Fawaz Currency API](https://github.com/fawazahmed0/exchange-api)（170+）·スマートキャッシュ、欠けたペアは自動で別ソースに切替 · **PWA** は 12 時間ごとのインストール案内バナー付き、インストール後はオフラインで動作 · 通貨ごとの 141 ページ（トレンドチャート・計算機付き）·わかりやすい為替ガイド · ライト/ダーク/自動テーマ · 3 段階の文字サイズ（A / A+ / A++）· 通貨ペアの保存、共有、フィードバックフォーム · [サポートページ](https://fxverter.com/ja/support/)と連絡先 hello@fxverter.com · クッキーなし・アカウントなし・追跡なし。

**使い方：** [fxverter.com](https://fxverter.com) にアクセス。Chrome/Edge/Safari なら「インストール / ホーム画面に追加」でアプリとして導入できます（導入後はオフラインで動作）。サイトは 100% 静的 — リポジトリをクローンして任意の静的ホスティングで運用できます。

**開発：** ソースファイルを編集したら `python build-lang-pages.py` を一度実行してサイト全体（175+ ページ）を再生成。詳細は `DEVELOPMENT.md`。

**免責事項：** 表示されるレートは**参考値**であり、無料の公開 API からのものです。金融取引・銀行送金・正式な会計には使用しないでください。取引の前に銀行で確認してください。

---

## 🇧🇷 Português

Um conversor de moedas gratuito e multilíngue que funciona inteiramente no seu navegador. Sem servidor, sem conta, sem rastreamento — abra o site e converta, ou instale como aplicativo (PWA).

**Destaques:** 141 moedas · 29 idiomas (detecção automática) · 3 fontes de dados: [Frankfurter](https://frankfurter.dev) (BCE, ~30 moedas principais), [ExchangeRate-API](https://www.exchangerate-api.com) (160+), [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) (170+) · cache inteligente, pares ausentes caem automaticamente para outra fonte · **PWA** com banner de instalação a cada 12 horas, funciona offline após instalar · 141 páginas por moeda com gráfico de tendência e calculadora · guias claros sobre câmbio · tema claro/escuro/automático · 3 tamanhos de fonte (A / A+ / A++) · pares salvos, compartilhar, formulário de feedback · [página de apoio](https://fxverter.com/pt/support/) e contato hello@fxverter.com · sem cookies, sem contas, sem rastreamento.

**Como usar:** visite [fxverter.com](https://fxverter.com); no Chrome/Edge/Safari, instale o app via «Instalar / Adicionar à Tela de Início» (depois funciona offline). O site é 100% estático — clone o repositório e hospede onde quiser.

**Desenvolvimento:** depois de editar os arquivos-fonte, execute uma vez `python build-lang-pages.py` para regenerar todo o site (175+ páginas). Detalhes em `DEVELOPMENT.md`.

**Aviso legal:** todas as taxas são **apenas indicativas**, de APIs públicas gratuitas. Não use para transações financeiras, transferências bancárias ou contabilidade oficial — confirme com seu banco.

---

## 📄 License

MIT — free to use, modify, and distribute.

## 🙏 Credits

- [Frankfurter API](https://frankfurter.dev) — ECB reference rates
- [ExchangeRate-API](https://www.exchangerate-api.com)
- [Fawaz Currency API](https://github.com/fawazahmed0/exchange-api) by @fawazahmed0
- Built with ❤️ — [source code on GitHub](https://github.com/SeyyidKadir/fx-currency-converter)
