# -*- coding: utf-8 -*-
"""Trust pages (About / Privacy Policy / Terms of Use / Contact).

Real content for the languages promoted in site_config.INDEXED_LANGS.
Each entry: title, meta description and a list of sections rendered in
order — ("h", heading), ("p", paragraph) or ("li", list item; rendered
inside a single <ul> until the next non-li item).
"""

TRUST_LABELS = {
    "en": {"about": "About", "privacy": "Privacy Policy", "terms": "Terms of Use", "contact": "Contact"},
    "zh": {"about": "关于", "privacy": "隐私政策", "terms": "使用条款", "contact": "联系我们"},
    "de": {"about": "Über uns", "privacy": "Datenschutz", "terms": "Nutzungsbedingungen", "contact": "Kontakt"},
    "fr": {"about": "À propos", "privacy": "Confidentialité", "terms": "Conditions d'utilisation", "contact": "Contact"},
    "es": {"about": "Quiénes somos", "privacy": "Política de privacidad", "terms": "Términos de uso", "contact": "Contacto"},
    "pt": {"about": "Sobre", "privacy": "Política de Privacidade", "terms": "Termos de Uso", "contact": "Contato"},
    "ja": {"about": "Fxverter について", "privacy": "プライバシーポリシー", "terms": "利用規約", "contact": "お問い合わせ"},
}

# Site-wide note strings that would otherwise contradict the new pages.
# supportIntro: the old text claimed "no ads" — no longer true once advertising
# is enabled. privacyNote: now points at the full Privacy Policy.
TRUST_OVERRIDES = {
    "supportIntro": {
        "en": "Fxverter is free to use — no account, no tracking. If it helps you, a small contribution keeps it fast, free and independent. Payments are processed by Creem as merchant of record — your payment data is handled by Creem, not by this website.",
        "zh": "Fxverter 完全免费——无需账号、无追踪。如果它对你有帮助，一份小小的支持能让它保持快速、免费和独立。付款由 Creem 作为记录商户处理——你的支付数据由 Creem 处理，而非本网站。",
        "de": "Fxverter ist kostenlos nutzbar — ohne Konto, ohne Tracking. Wenn es dir hilft, hält ein kleiner Beitrag schnell, frei und unabhängig. Zahlungen werden über Creem als Merchant of Record abgewickelt — deine Zahlungsdaten werden von Creem verarbeitet, nicht von dieser Website.",
        "fr": "Fxverter est gratuit — sans compte, sans suivi. S'il vous est utile, une petite contribution le garde rapide, gratuit et indépendant. Les paiements sont traités par Creem en tant que marchand de référence — vos données de paiement sont gérées par Creem, non par ce site.",
        "es": "Fxverter es gratis — sin cuenta, sin seguimiento. Si te resulta útil, una pequeña contribución lo mantiene rápido, gratuito e independiente. Los pagos los procesa Creem como comerciante registrado — tus datos de pago los gestiona Creem, no este sitio web.",
        "pt": "O Fxverter é gratuito — sem conta, sem rastreamento. Se ele te ajuda, uma pequena contribuição o mantém rápido, gratuito e independente. Os pagamentos são processados pela Creem como merchant of record — seus dados de pagamento são tratados pela Creem, não por este site.",
        "ja": "Fxverter は無料で利用できます——アカウント登録もトラッキングもありません。役に立ったと感じたら、ささやかな支援が高速・無料・独立した状態を保つ力になります。決済は Creem が記録上の販売者として処理します——支払いデータはこのサイトではなく Creem が取り扱います。",
    },
    "supportDesc": {
        "en": "Support Fxverter: free to use — no account, no tracking. Contributions keep it fast, free and independent; payments are handled by Creem as merchant of record.",
        "zh": "支持 Fxverter：完全免费——无需账号、无追踪。你的贡献让它保持快速、免费和独立；付款由 Creem 作为记录商户处理。",
        "de": "Unterstütze Fxverter: kostenlos — ohne Konto, ohne Tracking. Beiträge halten es schnell, frei und unabhängig; Zahlungen laufen über Creem.",
        "fr": "Soutenez Fxverter : gratuit — sans compte, sans suivi. Vos contributions le gardent rapide, gratuit et indépendant ; paiements via Creem.",
        "es": "Apoya a Fxverter: gratis — sin cuenta, sin seguimiento. Tus contribuciones lo mantienen rápido, gratuito e independiente; pagos vía Creem.",
        "pt": "Apoie o Fxverter: gratuito — sem conta, sem rastreamento. Contribuições o mantêm rápido, gratuito e independente; pagamentos via Creem.",
        "ja": "Fxverter を支援：無料で利用でき、アカウント登録もトラッキングもありません。あなたの支援が高速・無料・独立を保ちます。決済は Creem が処理します。",
    },
    "privacyNote": {
        "en": "Privacy: no cookies are required and no personal data is collected. Anonymous, cookie-free visit statistics (page views and country) may be collected. The site may display advertising — see the <a href=\"{base}privacy/\">Privacy Policy</a>.",
        "zh": "隐私：本网站无需 Cookie、不收集个人数据。可能会收集匿名的、无 Cookie 的访问统计（浏览量与国家/地区）。本站可能展示广告——详见<a href=\"{base}zh/privacy/\">隐私政策</a>。",
        "de": "Datenschutz: Cookies sind nicht erforderlich und es werden keine personenbezogenen Daten erhoben. Anonyme, cookie-freie Besucherstatistiken (Seitenaufrufe und Land) können erfasst werden. Die Website kann Werbung anzeigen — siehe <a href=\"{base}de/privacy/\">Datenschutzerklärung</a>.",
        "fr": "Confidentialité : aucun cookie n'est requis et aucune donnée personnelle n'est collectée. Des statistiques de visite anonymes et sans cookies (pages vues et pays) peuvent être recueillies. Le site peut afficher de la publicité — voir la <a href=\"{base}fr/privacy/\">Politique de confidentialité</a>.",
        "es": "Privacidad: no se requieren cookies ni se recopilan datos personales. Se pueden recopilar estadísticas de visita anónimas y sin cookies (páginas vistas y país). El sitio puede mostrar publicidad — consulta la <a href=\"{base}es/privacy/\">Política de privacidad</a>.",
        "pt": "Privacidade: nenhum cookie é necessário e nenhum dado pessoal é coletado. Estatísticas de visita anônimas e sem cookies (visualizações de página e país) podem ser coletadas. O site pode exibir publicidade — consulte a <a href=\"{base}pt/privacy/\">Política de Privacidade</a>.",
        "ja": "プライバシー：Cookie は不要で、個人データは収集しません。匿名・Cookie 不要のアクセス統計（閲覧数と国）を収集する場合があります。当サイトでは広告を表示することがあります——詳しくは<a href=\"{base}ja/privacy/\">プライバシーポリシー</a>をご覧ください。",
    },
}

TRUST = {}

# ─────────────────────────── ENGLISH ───────────────────────────
TRUST["en"] = {
    "about": {
        "title": "About Fxverter — Free, Open-Source Currency Converter",
        "desc": "Who is behind Fxverter, why it exists and what makes it different: a privacy-first, open-source currency converter with honest reference rates and plain-language guides.",
        "sections": [
            ("p", "Fxverter is a free, open-source online currency converter that runs entirely in your browser. It shows reference exchange rates for over 140 world currencies, requires no API key, no sign-up and no installation — you open the website and start converting."),
            ("h", "Why we built it"),
            ("p", "Most converter sites bury the actual rate under pop-ups, sign-up walls and app-install nagging. We wanted the opposite: a fast, private tool that shows the honest mid-market reference rate first and gets out of the way. The whole product is one static page that works on any device, in 29 languages, even offline after installation."),
            ("h", "What makes it different"),
            ("li", "No account, no tracking — conversions run locally in your browser"),
            ("li", "Three switchable public data sources: Frankfurter (European Central Bank reference rates), ExchangeRate-API and the Fawaz Currency API"),
            ("li", "56 major currencies with dedicated pages: live conversion tables, 30/90-day trend charts and currency profiles"),
            ("li", "Plain-language guides that explain how exchange rates actually work"),
            ("li", "Installable as an app (PWA) that keeps working offline with the last known rates"),
            ("h", "The data"),
            ("p", "Rates are indicative reference rates from public central-bank and market sources, updated daily. They are the same benchmark you see on Google or in financial news — useful for comparison and planning, not a contractual quote for a specific transfer."),
            ("h", "Who is behind it"),
            ("p", "Fxverter is built and maintained by an independent developer and supported by its users. The complete source code is public on GitHub — anyone can audit it, self-host it or contribute improvements."),
            ("p", "Questions, corrections or ideas? Write to <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — we read everything."),
        ],
    },
    "privacy": {
        "title": "Privacy Policy | Fxverter",
        "desc": "What Fxverter does and does not collect: no cookies required, no accounts, anonymous statistics only — plus how advertising and third-party services are handled.",
        "sections": [
            ("p", "Fxverter is designed to be usable without handing over any personal information. This policy explains what the site does and does not collect, and how advertising and third-party services are handled. Last updated: September 2026."),
            ("h", "What we do not collect"),
            ("p", "No account is required and no advertising cookies are set by the site itself. Conversions run locally in your browser — we never see the amounts or currency pairs you convert."),
            ("h", "Information collected automatically"),
            ("p", "Anonymous, aggregate visit statistics (page views and country, cookie-free) may be collected to understand overall usage and improve the tool. These statistics cannot be used to identify you."),
            ("h", "Information you choose to send"),
            ("p", "If you use the feedback form, the name, email address and message you submit are used only to read and reply to your feedback. If you support the project, the payment is processed by Creem.io as merchant of record — we never receive your full payment details. Supporters are listed by name only with their explicit consent."),
            ("h", "Third-party services"),
            ("p", "Exchange rates are fetched by your browser directly from public APIs (Frankfurter/ECB, ExchangeRate-API, Fawaz Currency API) — those requests come from your device, not through our servers. The site is hosted as static files, and anonymous analytics may run through Cloudflare."),
            ("h", "Advertising"),
            ("p", "This site may display advertising served through Google AdSense. Third-party vendors, including Google, use cookies and similar technologies to serve ads based on your prior visits to this or other websites. Google's use of advertising cookies enables it and its partners to serve ads to you based on your visits to our site and/or other sites on the internet."),
            ("p", "You may opt out of personalized advertising at <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google Ads Settings</a>, or opt out of third-party vendor cookies at <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Where required by law — for example in the EEA and the UK — personalized advertising is only shown with your consent, and non-personalized advertising is used otherwise. For details, see <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">how Google uses information from sites that use its services</a>."),
            ("h", "Local storage"),
            ("p", "Your theme choice, font size, saved currency pairs and install-banner timing are stored in your browser's local storage. This data never leaves your device and can be cleared at any time via your browser settings."),
            ("h", "Retention and your rights"),
            ("p", "Feedback messages are kept only as long as needed to respond. You may ask us to delete any feedback you have sent by writing to <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
            ("h", "Changes to this policy"),
            ("p", "If the site's data practices change, this page will be updated and the date above revised. Continued use of the site after a change means you accept the updated policy."),
        ],
    },
    "terms": {
        "title": "Terms of Use | Fxverter",
        "desc": "The ground rules for using Fxverter: rates are indicative reference values, not quotes; the service is provided as is; and how liability, intellectual property and acceptable use are handled.",
        "sections": [
            ("p", "By using fxverter.com you agree to these terms. If you do not agree, please do not use the site. Last updated: September 2026."),
            ("h", "The service"),
            ("p", "Fxverter is a free, open-source online currency converter, provided \"as is\" and \"as available\" without warranties of any kind, express or implied — including accuracy, availability or fitness for a particular purpose."),
            ("h", "Exchange rates are indicative only"),
            ("p", "All rates shown are reference rates collected from public sources such as central banks and open currency APIs, usually updated once per day. They are benchmarks for comparison — not quotes, not financial advice, and not a price any provider will actually give you. Do not use them for financial transactions, bank transfers, invoicing or official accounting; always verify the rate with your bank or financial institution before transacting."),
            ("h", "Limitation of liability"),
            ("p", "To the maximum extent permitted by law, the Fxverter maintainers are not liable for any loss or damage arising from the use of, or inability to use, the site or its data — including decisions made in reliance on the displayed rates."),
            ("h", "Intellectual property"),
            ("p", "The source code is open source under the MIT license and available on GitHub. The site's text, design and brand remain the property of the Fxverter project; you may not republish the site's content wholesale without permission."),
            ("h", "Third-party services and links"),
            ("p", "The site relies on third-party public APIs and may link to third-party websites. We do not control them and are not responsible for their content, availability or practices."),
            ("h", "Acceptable use"),
            ("p", "You agree not to disrupt the service, attempt to overload it, or use automated tools in a way that degrades it for other visitors."),
            ("h", "Changes to these terms"),
            ("p", "These terms may be updated from time to time; the current version is always this page. Questions? Write to <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
        ],
    },
    "contact": {
        "title": "Contact | Fxverter",
        "desc": "How to reach the Fxverter team: feedback, rate corrections, licensing and press — hello@fxverter.com or the online feedback form.",
        "sections": [
            ("p", "The fastest way to reach us is email: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. We read every message and usually reply within a few days."),
            ("h", "What to write about"),
            ("li", "Feedback and feature ideas — what works, what doesn't, what's missing"),
            ("li", "Corrections — if something looks wrong on a page, tell us which one"),
            ("li", "Licensing and republishing questions"),
            ("li", "Press and partnership inquiries"),
            ("h", "Bugs and code issues"),
            ("p", "Fxverter is open source — bug reports and pull requests are welcome directly on the project's GitHub repository, where they are public and trackable."),
            ("h", "A note on rates"),
            ("p", "All rates are indicative reference values from public sources, updated daily — see the <a href=\"../guides/\">guides</a> for what that means in practice. Before you write about a \"wrong\" rate, please compare with a second source at the same time of day: small differences between reference rates and provider quotes are normal."),
            ("h", "Privacy"),
            ("p", "Your email address is used only to reply to you — no newsletter, no marketing. See the <a href=\"../privacy/\">Privacy Policy</a> for details."),
        ],
    },
}

# ─────────────────────────── 中文 ───────────────────────────
TRUST["zh"] = {
    "about": {
        "title": "关于 Fxverter — 免费开源的货币换算器",
        "desc": "Fxverter 背后是谁、为什么做这个站、它有什么不同：一个隐私优先、开源的货币换算器，展示诚实的参考汇率并用大白话解释汇率知识。",
        "sections": [
            ("p", "Fxverter 是一个完全在浏览器中运行的免费开源货币换算器。它展示 140 多种世界货币的参考汇率，无需 API 密钥、无需注册、无需安装——打开网页就能换算。"),
            ("h", "为什么做这个站"),
            ("p", "大多数换算网站用弹窗、注册墙和装 App 提醒把真正的汇率埋在底下。我们想做相反的东西：一个快速、私密的工具，把诚实的中间市场参考汇率放在第一位，其余一律不打扰。整个产品就是一个静态页面，任何设备都能用，支持 29 种语言，安装为应用后离线也能用。"),
            ("h", "它有什么不同"),
            ("li", "无需账号、无追踪——换算全部在你自己的浏览器中完成"),
            ("li", "三个可切换的公开数据源：Frankfurter（欧洲央行参考汇率）、ExchangeRate-API 和 Fawaz Currency API"),
            ("li", "56 种主流货币各有独立页面：实时换算表、30/90 天趋势图和货币档案"),
            ("li", "用大白话解释汇率究竟怎么运作的科普指南"),
            ("li", "可安装为应用（PWA），离线也能用最后一次缓存的汇率"),
            ("h", "关于数据"),
            ("p", "汇率来自公开的央行和市场数据源，每日更新，仅供参考。它们与你在 Google 或财经新闻里看到的是同一类基准——适合比价和规划，不是某笔具体汇款的成交报价。"),
            ("h", "谁在做这个站"),
            ("p", "Fxverter 由一名独立开发者构建和维护，靠用户支持运转。全部源代码在 GitHub 上公开——任何人都可以审查、自托管或提交改进。"),
            ("p", "有问题、勘误或想法？写信到 <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>——每封邮件我们都会看。"),
        ],
    },
    "privacy": {
        "title": "隐私政策 | Fxverter",
        "desc": "Fxverter 收集什么、不收集什么：无需 Cookie、无账号、只有匿名统计——以及广告和第三方服务如何处理。",
        "sections": [
            ("p", "Fxverter 的设计目标是不提交任何个人信息也能正常使用。本政策说明本站收集什么、不收集什么，以及广告和第三方服务如何处理。最后更新：2026 年 9 月。"),
            ("h", "我们不收集什么"),
            ("p", "无需注册账号，本站自身不设置广告 Cookie。换算在本地浏览器中完成——你换算的金额和货币对我们完全不可见。"),
            ("h", "自动收集的信息"),
            ("p", "为了解整体使用情况、改进工具，本站可能收集匿名的、汇总的访问统计（浏览量与国家/地区，无 Cookie）。这些统计无法用于识别你的身份。"),
            ("h", "你主动发送的信息"),
            ("p", "如果你使用反馈表单，提交的姓名、邮箱和留言只用于阅读并回复你的反馈。如果你支持本项目，付款由 Creem.io 作为记录商户处理——我们不会收到你的完整支付信息。支持者名单只有在获得明确同意后才会展示姓名。"),
            ("h", "第三方服务"),
            ("p", "汇率数据由你的浏览器直接从公开 API（Frankfurter/欧洲央行、ExchangeRate-API、Fawaz Currency API）获取——请求来自你的设备，不经过我们的服务器。本站以静态文件方式托管，匿名统计可能经由 Cloudflare 运行。"),
            ("h", "广告"),
            ("p", "本站可能展示由 Google AdSense 投放的广告。包括 Google 在内的第三方供应商会使用 Cookie 和类似技术，根据你此前对本站或其他网站的访问投放广告。Google 对广告 Cookie 的使用使其及其合作伙伴能够根据你对我们网站和/或其他网站的访问向你投放广告。"),
            ("p", "你可以在 <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google 广告设置</a>中选择停用个性化广告，或在 <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a> 停用第三方供应商的 Cookie。在法律要求的地区（例如欧洲经济区与英国），个性化广告仅在获得你的同意后展示，否则使用非个性化广告。详见 <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">Google 如何使用其服务所覆盖网站的信息</a>。"),
            ("h", "本地存储"),
            ("p", "你的主题选择、字号、收藏的货币对和安装横幅计时保存在浏览器的本地存储中。这些数据不会离开你的设备，随时可以通过浏览器设置清除。"),
            ("h", "数据保留与你的权利"),
            ("p", "反馈留言只在回复所需的时间内保留。你可以写信到 <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> 要求删除你发送过的任何反馈。"),
            ("h", "政策变更"),
            ("p", "如果本站的数据处理方式发生变化，本页面将更新并修订上方日期。变更后继续使用本站即表示你接受更新后的政策。"),
        ],
    },
    "terms": {
        "title": "使用条款 | Fxverter",
        "desc": "使用 Fxverter 的基本规则：汇率仅为参考、服务按现状提供，以及责任、知识产权与可接受使用的约定。",
        "sections": [
            ("p", "使用 fxverter.com 即表示你同意本条款。如不同意，请不要使用本站。最后更新：2026 年 9 月。"),
            ("h", "服务本身"),
            ("p", "Fxverter 是免费的开源在线货币换算器，按\"现状\"和\"可用状态\"提供，不作任何明示或默示的保证——包括准确性、可用性或对特定用途的适用性。"),
            ("h", "汇率仅供参考"),
            ("p", "本站展示的所有汇率均为来自央行和公开货币 API 等公开来源的参考汇率，通常每日更新一次。它们是用于比较的基准——不是报价、不构成理财建议，也不是任何机构实际会给你的价格。请勿将其用于金融交易、银行汇款、开票或正式记账；交易前请务必与你的银行或金融机构核实汇率。"),
            ("h", "责任限制"),
            ("p", "在法律允许的最大范围内，Fxverter 维护者不对因使用或无法使用本站及其数据而产生的任何损失或损害承担责任——包括基于所展示汇率做出的决策。"),
            ("h", "知识产权"),
            ("p", "源代码按 MIT 许可证开源，可在 GitHub 获取。本站的文字、设计与品牌归 Fxverter 项目所有；未经许可不得整体转载本站内容。"),
            ("h", "第三方服务与链接"),
            ("p", "本站依赖第三方公开 API，并可能链接到第三方网站。我们无法控制这些服务，也不对其内容、可用性或做法负责。"),
            ("h", "可接受使用"),
            ("p", "你同意不干扰本服务、不试图使其过载，不以影响其他访客的方式使用自动化工具。"),
            ("h", "条款变更"),
            ("p", "本条款可能不时更新，当前版本始终以本页面为准。有问题？写信到 <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>。"),
        ],
    },
    "contact": {
        "title": "联系我们 | Fxverter",
        "desc": "如何联系 Fxverter 团队：反馈、汇率勘误、授权与媒体合作——hello@fxverter.com 或在线反馈表单，无需注册。",
        "sections": [
            ("p", "最快的联系方式是邮件：<a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>。每封邮件我们都会阅读，通常几天内回复。"),
            ("h", "可以写些什么"),
            ("li", "反馈与功能建议——哪里好用、哪里不好用、还缺什么"),
            ("li", "勘误——如果某个页面有问题，请告诉我们是哪一页"),
            ("li", "授权与转载事宜"),
            ("li", "媒体与合作洽谈"),
            ("h", "错误与代码问题"),
            ("p", "Fxverter 是开源项目——欢迎直接在项目的 GitHub 仓库提交 Issue 和 Pull Request，公开且可追踪。"),
            ("h", "关于汇率"),
            ("p", "所有汇率均为来自公开来源的参考值，每日更新——具体含义见<a href=\"../guides/\">汇率指南</a>。如果你觉得某个汇率\"不对\"，请在同一时段用第二个数据源对比后再写信：参考汇率与机构报价之间的细小差异是正常的。"),
            ("h", "隐私"),
            ("p", "你的邮箱地址只用于回复——没有订阅、没有营销。详见<a href=\"../privacy/\">隐私政策</a>。"),
        ],
    },
}

# ─────────────────────────── DEUTSCH ───────────────────────────
TRUST["de"] = {
    "about": {
        "title": "Über Fxverter — Kostenloser Open-Source-Währungsrechner",
        "desc": "Wer hinter Fxverter steckt, warum es existiert und was es anders macht: ein datenschutzfreundlicher Open-Source-Währungsrechner mit ehrlichen Referenzkursen.",
        "sections": [
            ("p", "Fxverter ist ein kostenloser Open-Source-Währungsrechner, der vollständig in deinem Browser läuft. Er zeigt Referenzwechselkurse für über 140 Währungen — ohne API-Schlüssel, ohne Anmeldung, ohne Installation: Website öffnen, umrechnen."),
            ("h", "Warum es Fxverter gibt"),
            ("p", "Die meisten Rechner-Seiten begraben den eigentlichen Kurs unter Pop-ups, Anmelde-Aufforderungen und App-Werbebanner. Wir wollten das Gegenteil: ein schnelles, privates Tool, das zuerst den ehrlichen Mid-Market-Referenzkurs zeigt und sonst nichts will. Das ganze Produkt ist eine statische Seite, die auf jedem Gerät läuft, in 29 Sprachen — und nach der Installation sogar offline."),
            ("h", "Was es anders macht"),
            ("li", "Kein Konto, kein Tracking — Umrechnungen laufen lokal in deinem Browser"),
            ("li", "Drei umschaltbare öffentliche Datenquellen: Frankfurter (EZB-Referenzkurse), ExchangeRate-API und die Fawaz Currency API"),
            ("li", "56 wichtige Währungen mit eigenen Seiten: Live-Umrechnungstabellen, 30/90-Tage-Charts und Währungsprofile"),
            ("li", "Verständliche Ratgeber, die erklären, wie Wechselkurse wirklich entstehen"),
            ("li", "Als App installierbar (PWA), die offline mit den letzten bekannten Kursen weiterarbeitet"),
            ("h", "Die Daten"),
            ("p", "Die Kurse sind indikative Referenzkurse aus öffentlichen Notenbank- und Marktquellen, täglich aktualisiert. Es ist derselbe Maßstab wie bei Google oder in Finanznachrichten — geeignet für Vergleich und Planung, kein verbindliches Angebot für eine konkrete Überweisung."),
            ("h", "Wer dahintersteckt"),
            ("p", "Fxverter wird von einem unabhängigen Entwickler gebaut und gepflegt und von seinen Nutzern getragen. Der komplette Quellcode ist öffentlich auf GitHub — jeder kann ihn prüfen, selbst hosten oder Verbesserungen beitragen."),
            ("p", "Fragen, Korrekturen oder Ideen? Schreib an <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — wir lesen alles."),
        ],
    },
    "privacy": {
        "title": "Datenschutzerklärung | Fxverter",
        "desc": "Was Fxverter sammelt und was nicht: keine Cookies nötig, keine Konten, nur anonyme Statistiken — plus wie Werbung und Drittanbieter behandelt werden.",
        "sections": [
            ("p", "Fxverter ist so gebaut, dass es ohne jede persönliche Angabe nutzbar ist. Diese Richtlinie erklärt, was die Website erfasst und was nicht, und wie Werbung und Drittanbieter behandelt werden. Stand: September 2026."),
            ("h", "Was wir nicht sammeln"),
            ("p", "Kein Konto nötig; die Website selbst setzt keine Werbe-Cookies. Umrechnungen laufen lokal in deinem Browser — wir sehen niemals, welche Beträge oder Währungspaare du umrechnest."),
            ("h", "Automatisch erfasste Informationen"),
            ("p", "Anonyme, aggregierte Besucherstatistiken (Seitenaufrufe und Land, ohne Cookies) können erfasst werden, um die Nutzung insgesamt zu verstehen und das Tool zu verbessern. Diese Statistiken können dich nicht identifizieren."),
            ("h", "Informationen, die du selbst sendest"),
            ("p", "Über das Feedback-Formular werden Name, E-Mail-Adresse und Nachricht nur verwendet, um dein Feedback zu lesen und zu beantworten. Bei einer Unterstützung läuft die Zahlung über Creem.io als Merchant of Record — wir erhalten nie deine vollständigen Zahlungsdaten. Unterstützer werden nur mit ausdrücklicher Zustimmung namentlich genannt."),
            ("h", "Drittanbieter"),
            ("p", "Kurse werden von deinem Browser direkt aus öffentlichen APIs geladen (Frankfurter/EZB, ExchangeRate-API, Fawaz Currency API) — diese Anfragen kommen von deinem Gerät, nicht über unsere Server. Die Website wird als statische Dateien gehostet; anonyme Statistiken können über Cloudflare laufen."),
            ("h", "Werbung"),
            ("p", "Diese Website kann Werbung über Google AdSense einblenden. Drittanbieter einschließlich Google verwenden Cookies und ähnliche Technologien, um Werbung auf Grundlage deiner vorherigen Besuche dieser oder anderer Websites einzublenden. Googles Verwendung von Werbe-Cookies ermöglicht es Google und seinen Partnern, dir Werbung auf Grundlage deiner Besuche auf unserer Website und/oder anderen Websites im Internet anzuzeigen."),
            ("p", "Du kannst personalisierte Werbung unter <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google Anzeigeneinstellungen</a> deaktivieren oder Cookies von Drittanbietern unter <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a> ablehnen. Wo gesetzlich erforderlich — etwa im EWR und im Vereinigten Königreich — wird personalisierte Werbung nur mit deiner Zustimmung gezeigt, andernfalls nicht-personalisierte Werbung. Details: <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">Wie Google Informationen von Websites, die seine Dienste nutzen, verwendet</a>."),
            ("h", "Lokaler Speicher"),
            ("p", "Themenwahl, Schriftgröße, gespeicherte Währungspaare und das Timing des Installationsbanners liegen im lokalen Speicher deines Browsers. Diese Daten verlassen dein Gerät nie und lassen sich jederzeit über die Browsereinstellungen löschen."),
            ("h", "Speicherdauer und deine Rechte"),
            ("p", "Feedback-Nachrichten werden nur so lange aufbewahrt, wie zur Beantwortung nötig. Du kannst die Löschung jeder gesendeten Rückmeldung per E-Mail an <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> verlangen."),
            ("h", "Änderungen dieser Richtlinie"),
            ("p", "Ändern sich die Datenpraktiken der Website, wird diese Seite aktualisiert und das Datum oben angepasst. Die weitere Nutzung der Website nach einer Änderung gilt als Zustimmung zur aktualisierten Richtlinie."),
        ],
    },
    "terms": {
        "title": "Nutzungsbedingungen | Fxverter",
        "desc": "Die Grundregeln für die Nutzung von Fxverter: Kurse sind nur Referenzwerte, keine Angebote; die Dienstleistung wird ohne Gewähr bereitgestellt.",
        "sections": [
            ("p", "Mit der Nutzung von fxverter.com stimmst du diesen Bedingungen zu. Wenn nicht, nutze die Website bitte nicht. Stand: September 2026."),
            ("h", "Die Dienstleistung"),
            ("p", "Fxverter ist ein kostenloser Open-Source-Währungsrechner, der \"wie besehen\" und \"wie verfügbar\" und ohne jegliche Gewährleistung bereitgestellt wird — weder ausdrücklich stillschweigend, einschließlich Genauigkeit, Verfügbarkeit oder Eignung für einen bestimmten Zweck."),
            ("h", "Wechselkurse sind nur Richtwerte"),
            ("p", "Alle angezeigten Kurse sind Referenzkurse aus öffentlichen Quellen wie Notenbanken und offenen Währungs-APIs, meist einmal täglich aktualisiert. Sie sind Vergleichsmaßstäbe — keine Angebote, keine Anlageberatung und kein Preis, den dir ein Anbieter tatsächlich geben würde. Verwende sie nicht für Finanztransaktionen, Banküberweisungen, Rechnungsstellung oder offizielle Buchhaltung; prüfe den Kurs vor jeder Transaktion bei deiner Bank oder deinem Finanzinstitut."),
            ("h", "Haftungsbeschränkung"),
            ("p", "Im gesetzlich zulässigen Höchstumfang haften die Fxverter-Betreuer nicht für Verluste oder Schäden aus der Nutzung oder Nichtnutzbarkeit der Website oder ihrer Daten — einschließlich Entscheidungen, die auf den angezeigten Kursen beruhen."),
            ("h", "Geistiges Eigentum"),
            ("p", "Der Quellcode ist unter der MIT-Lizenz Open Source und auf GitHub verfügbar. Texte, Design und Marke der Website bleiben Eigentum des Fxverter-Projekts; ganzseitige Weiterveröffentlichung der Inhalte ist ohne Erlaubnis nicht gestattet."),
            ("h", "Drittanbieter und Links"),
            ("p", "Die Website nutzt öffentliche APIs von Drittanbietern und kann auf externe Websites verlinken. Wir kontrollieren diese nicht und sind nicht für deren Inhalte, Verfügbarkeit oder Praktiken verantwortlich."),
            ("h", "Akzeptable Nutzung"),
            ("p", "Du stimmst zu, den Dienst nicht zu stören, nicht zu überlasten und automatisierte Tools nicht in einer Weise einzusetzen, die anderen Besuchern schadet."),
            ("h", "Änderungen dieser Bedingungen"),
            ("p", "Diese Bedingungen können gelegentlich aktualisiert werden; maßgeblich ist stets diese Seite. Fragen? Schreib an <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
        ],
    },
    "contact": {
        "title": "Kontakt | Fxverter",
        "desc": "So erreichst du das Fxverter-Team: Feedback, Kurskorrekturen, Lizenzen und Presse — hello@fxverter.com oder das Online-Feedback-Formular.",
        "sections": [
            ("p", "Am schnellsten erreichst du uns per E-Mail: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Wir lesen jede Nachricht und antworten meist innerhalb weniger Tage."),
            ("h", "Worum es gehen kann"),
            ("li", "Feedback und Funktionswünsche — was gut funktioniert, was nicht, was fehlt"),
            ("li", "Korrekturen — wenn auf einer Seite etwas falsch aussieht, sag uns, welche"),
            ("li", "Fragen zu Lizenzen und Weiterveröffentlichung"),
            ("li", "Presse- und Kooperationsanfragen"),
            ("h", "Fehler und Code-Probleme"),
            ("p", "Fxverter ist Open Source — Fehlerberichte und Pull Requests sind direkt im GitHub-Repository des Projekts willkommen, öffentlich und nachverfolgbar."),
            ("h", "Ein Hinweis zu den Kursen"),
            ("p", "Alle Kurse sind Richtwerte aus öffentlichen Quellen, täglich aktualisiert — die <a href=\"../guides/\">Ratgeber</a> erklären, was das praktisch bedeutet. Bevor du über einen \"falschen\" Kurs schreibst, vergleiche ihn bitte zur gleichen Tageszeit mit einer zweiten Quelle: kleine Differenzen zwischen Referenzkursen und Anbieterkursen sind normal."),
            ("h", "Datenschutz"),
            ("p", "Deine E-Mail-Adresse wird nur zur Antwort verwendet — kein Newsletter, kein Marketing. Details in der <a href=\"../privacy/\">Datenschutzerklärung</a>."),
        ],
    },
}

# ─────────────────────────── FRANÇAIS ───────────────────────────
TRUST["fr"] = {
    "about": {
        "title": "À propos de Fxverter — Convertisseur de devises libre et gratuit",
        "desc": "Qui est derrière Fxverter, pourquoi ce site existe et ce qui le rend différent : un convertisseur open-source respectueux de la vie privée, avec des taux de référence honnêtes.",
        "sections": [
            ("p", "Fxverter est un convertisseur de devises en ligne gratuit et open source qui fonctionne entièrement dans votre navigateur. Il affiche des taux de change de référence pour plus de 140 devises, sans clé API, sans inscription ni installation — vous ouvrez le site et vous convertissez."),
            ("h", "Pourquoi nous l'avons créé"),
            ("p", "La plupart des sites de conversion enterrent le vrai taux sous les pop-ups, les murs d'inscription et les relances d'installation d'application. Nous voulions l'inverse : un outil rapide et privé qui montre d'abord le taux de référence du marché interbancaire, sans rien demander en échange. Tout le produit tient en une page statique qui fonctionne sur n'importe quel appareil, en 29 langues — et même hors ligne après installation."),
            ("h", "Ce qui le rend différent"),
            ("li", "Aucun compte, aucun suivi — les conversions s'exécutent localement dans votre navigateur"),
            ("li", "Trois sources publiques commutables : Frankfurter (taux de référence de la BCE), ExchangeRate-API et Fawaz Currency API"),
            ("li", "56 grandes devises avec une page dédiée : tables de conversion en direct, graphiques 30/90 jours et profils de devise"),
            ("li", "Des guides en langage clair qui expliquent comment les taux de change fonctionnent vraiment"),
            ("li", "Installable comme application (PWA) qui continue de fonctionner hors ligne avec les derniers taux connus"),
            ("h", "Les données"),
            ("p", "Les taux sont des taux de référence indicatifs provenant de sources publiques (banques centrales, marchés), mis à jour chaque jour. C'est la même référence que sur Google ou dans la presse financière — utile pour comparer et planifier, mais ce n'est pas un devis contractuel pour un virement précis."),
            ("h", "Qui est derrière"),
            ("p", "Fxverter est développé et maintenu par un développeur indépendant et soutenu par ses utilisateurs. Le code source complet est public sur GitHub — chacun peut l'auditer, l'héberger lui-même ou contribuer des améliorations."),
            ("p", "Questions, corrections ou idées ? Écrivez à <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — nous lisons tout."),
        ],
    },
    "privacy": {
        "title": "Politique de confidentialité | Fxverter",
        "desc": "Ce que Fxverter collecte et ne collecte pas : aucun cookie requis, aucun compte, uniquement des statistiques anonymes — et comment la publicité et les tiers sont gérés.",
        "sections": [
            ("p", "Fxverter est conçu pour être utilisable sans fournir la moindre information personnelle. Cette politique explique ce que le site collecte et ne collecte pas, et comment la publicité et les services tiers sont gérés. Dernière mise à jour : septembre 2026."),
            ("h", "Ce que nous ne collectons pas"),
            ("p", "Aucun compte n'est requis et le site ne dépose pas lui-même de cookies publicitaires. Les conversions s'exécutent localement dans votre navigateur — nous ne voyons jamais les montants ni les paires de devises que vous convertissez."),
            ("h", "Informations collectées automatiquement"),
            ("p", "Des statistiques de visite anonymes et agrégées (pages vues et pays, sans cookies) peuvent être recueillies pour comprendre l'usage global et améliorer l'outil. Ces statistiques ne permettent pas de vous identifier."),
            ("h", "Informations que vous choisissez d'envoyer"),
            ("p", "Si vous utilisez le formulaire de retour, le nom, l'adresse e-mail et le message transmis servent uniquement à lire et répondre à votre retour. En cas de soutien financier, le paiement est traité par Creem.io en tant que marchand de référence — nous ne recevons jamais vos informations de paiement complètes. Les soutiens ne sont cités nommément qu'avec leur accord explicite."),
            ("h", "Services tiers"),
            ("p", "Les taux sont récupérés par votre navigateur directement auprès d'API publiques (Frankfurter/BCE, ExchangeRate-API, Fawaz Currency API) — ces requêtes proviennent de votre appareil et non de nos serveurs. Le site est hébergé sous forme de fichiers statiques ; des statistiques anonymes peuvent passer par Cloudflare."),
            ("h", "Publicité"),
            ("p", "Ce site peut afficher de la publicité diffusée via Google AdSense. Des fournisseurs tiers, y compris Google, utilisent des cookies et technologies similaires pour diffuser des annonces en fonction de vos visites précédentes sur ce site ou d'autres sites. L'utilisation des cookies publicitaires par Google lui permet, à elle et à ses partenaires, de vous diffuser des annonces en fonction de vos visites sur notre site et/ou d'autres sites d'Internet."),
            ("p", "Vous pouvez désactiver la publicité personnalisée dans les <a href=\"https://adssettings.google.com\" rel=\"noopener\">paramètres des annonces Google</a> ou refuser les cookies de fournisseurs tiers sur <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Là où la loi l'exige — par exemple dans l'EEE et au Royaume-Uni — la publicité personnalisée n'est affichée qu'avec votre consentement ; sinon, une publicité non personnalisée est utilisée. Détails : <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">comment Google utilise les informations des sites utilisant ses services</a>."),
            ("h", "Stockage local"),
            ("p", "Votre choix de thème, la taille de police, les paires de devises enregistrées et le calendrier de la bannière d'installation sont stockés dans le stockage local de votre navigateur. Ces données ne quittent jamais votre appareil et peuvent être effacées à tout moment dans les réglages du navigateur."),
            ("h", "Conservation et vos droits"),
            ("p", "Les messages de retour ne sont conservés que le temps nécessaire pour répondre. Vous pouvez demander la suppression de tout retour envoyé en écrivant à <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
            ("h", "Modifications de cette politique"),
            ("p", "Si les pratiques du site évoluent, cette page sera mise à jour et la date ci-dessus révisée. Toute utilisation du site après une modification vaut acceptation de la politique actualisée."),
        ],
    },
    "terms": {
        "title": "Conditions d'utilisation | Fxverter",
        "desc": "Les règles de base pour utiliser Fxverter : les taux sont indicatifs, le service est fourni en l'état — responsabilité, propriété intellectuelle et usage acceptable.",
        "sections": [
            ("p", "En utilisant fxverter.com, vous acceptez ces conditions. Si vous n'êtes pas d'accord, veuillez ne pas utiliser le site. Dernière mise à jour : septembre 2026."),
            ("h", "Le service"),
            ("p", "Fxverter est un convertisseur de devises en ligne gratuit et open source, fourni « en l'état » et « selon disponibilité », sans garantie d'aucune sorte, expresse ou implicite — y compris d'exactitude, de disponibilité ou d'adéquation à un usage particulier."),
            ("h", "Les taux de change sont indicatifs"),
            ("p", "Tous les taux affichés sont des taux de référence collectés auprès de sources publiques telles que les banques centrales et les API de devises ouvertes, généralement mis à jour une fois par jour. Ce sont des repères de comparaison — ni des devis, ni un conseil financier, ni un prix qu'un prestataire vous proposerait réellement. Ne les utilisez pas pour des transactions financières, des virements bancaires, de la facturation ou de la comptabilité officielle ; vérifiez toujours le taux auprès de votre banque avant toute opération."),
            ("h", "Limitation de responsabilité"),
            ("p", "Dans la mesure maximale permise par la loi, les mainteneurs de Fxverter ne sont pas responsables de toute perte ou dommage résultant de l'utilisation ou de l'impossibilité d'utiliser le site ou ses données — y compris les décisions prises sur la foi des taux affichés."),
            ("h", "Propriété intellectuelle"),
            ("p", "Le code source est open source sous licence MIT et disponible sur GitHub. Les textes, le design et la marque du site restent la propriété du projet Fxverter ; la republication du contenu du site en bloc n'est pas autorisée sans permission."),
            ("h", "Services tiers et liens"),
            ("p", "Le site s'appuie sur des API publiques tierces et peut renvoyer vers des sites tiers. Nous ne les contrôlons pas et ne sommes pas responsables de leur contenu, disponibilité ou pratiques."),
            ("h", "Usage acceptable"),
            ("p", "Vous acceptez de ne pas perturber le service, de ne pas tenter de le surcharger et de ne pas utiliser d'outils automatisés au détriment des autres visiteurs."),
            ("h", "Modifications de ces conditions"),
            ("p", "Ces conditions peuvent être mises à jour de temps à autre ; la version en vigueur est toujours celle de cette page. Des questions ? Écrivez à <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
        ],
    },
    "contact": {
        "title": "Contact | Fxverter",
        "desc": "Comment joindre l'équipe Fxverter : retours, corrections de taux, licences et presse — hello@fxverter.com ou le formulaire de commentaires en ligne.",
        "sections": [
            ("p", "Le moyen le plus rapide de nous joindre est l'e-mail : <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Nous lisons chaque message et répondons généralement sous quelques jours."),
            ("h", "De quoi nous écrire"),
            ("li", "Retours et idées de fonctionnalités — ce qui marche, ce qui coince, ce qui manque"),
            ("li", "Corrections — si une page semble fausse, dites-nous laquelle"),
            ("li", "Questions de licence et de republication"),
            ("li", "Demandes presse et partenariats"),
            ("h", "Bugs et problèmes de code"),
            ("p", "Fxverter est open source — les rapports de bugs et les pull requests sont les bienvenus directement sur le dépôt GitHub du projet, publics et traçables."),
            ("h", "À propos des taux"),
            ("p", "Tous les taux sont des valeurs de référence de sources publiques, mises à jour chaque jour — les <a href=\"../guides/\">guides</a> expliquent ce que cela signifie concrètement. Avant de nous écrire au sujet d'un taux « faux », comparez-le avec une deuxième source à la même heure : de petites différences entre taux de référence et taux proposés sont normales."),
            ("h", "Confidentialité"),
            ("p", "Votre adresse e-mail sert uniquement à vous répondre — pas de newsletter, pas de marketing. Voir la <a href=\"../privacy/\">Politique de confidentialité</a>."),
        ],
    },
}

# ─────────────────────────── ESPAÑOL ───────────────────────────
TRUST["es"] = {
    "about": {
        "title": "Quiénes somos — Fxverter, conversor de divisas libre y gratuito",
        "desc": "Quién está detrás de Fxverter, por qué existe y qué lo hace diferente: un conversor open-source que respeta tu privacidad, con tasas de referencia honestas.",
        "sections": [
            ("p", "Fxverter es un conversor de divisas en línea gratuito y de código abierto que funciona totalmente en tu navegador. Muestra tasas de cambio de referencia para más de 140 divisas, sin clave API, sin registro ni instalación — abres el sitio y empiezas a convertir."),
            ("h", "Por qué lo creamos"),
            ("p", "La mayoría de los sitios de conversión entierran la tasa real bajo ventanas emergentes, muros de registro y avisos de instalación de apps. Queríamos lo contrario: una herramienta rápida y privada que muestre primero la tasa de referencia del mercado interbancario, sin pedir nada a cambio. Todo el producto es una página estática que funciona en cualquier dispositivo, en 29 idiomas — e incluso sin conexión tras instalarla."),
            ("h", "Qué lo hace diferente"),
            ("li", "Sin cuenta y sin seguimiento — las conversiones se ejecutan en tu propio navegador"),
            ("li", "Tres fuentes públicas conmutables: Frankfurter (tasas de referencia del Banco Central Europeo), ExchangeRate-API y la Fawaz Currency API"),
            ("li", "56 divisas principales con página propia: tablas de conversión en vivo, gráficos de 30/90 días y perfiles de divisa"),
            ("li", "Guías en lenguaje sencillo que explican cómo funcionan realmente los tipos de cambio"),
            ("li", "Instalable como app (PWA) que sigue funcionando sin conexión con las últimas tasas conocidas"),
            ("h", "Los datos"),
            ("p", "Las tasas son tasas de referencia indicativas de fuentes públicas (bancos centrales y mercados), actualizadas a diario. Es la misma referencia que ves en Google o en la prensa financiera — útil para comparar y planificar, no una cotización contractual para una transferencia concreta."),
            ("h", "Quién está detrás"),
            ("p", "Fxverter lo construye y mantiene un desarrollador independiente y lo sostienen sus usuarios. El código fuente completo es público en GitHub — cualquiera puede auditarlo, alojarlo por su cuenta o aportar mejoras."),
            ("p", "¿Preguntas, correcciones o ideas? Escribe a <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — leemos todo."),
        ],
    },
    "privacy": {
        "title": "Política de privacidad | Fxverter",
        "desc": "Qué recopila Fxverter y qué no: sin cookies obligatorias, sin cuentas, solo estadísticas anónimas — y cómo se gestionan la publicidad y los terceros.",
        "sections": [
            ("p", "Fxverter está diseñado para poder usarse sin entregar ningún dato personal. Esta política explica qué recopila el sitio y qué no, y cómo se gestionan la publicidad y los servicios de terceros. Última actualización: septiembre de 2026."),
            ("h", "Lo que no recopilamos"),
            ("p", "No se requiere cuenta y el propio sitio no instala cookies publicitarias. Las conversiones se ejecutan localmente en tu navegador — nunca vemos los importes ni los pares de divisas que conviertes."),
            ("h", "Información recopilada automáticamente"),
            ("p", "Se pueden recopilar estadísticas de visita anónimas y agregadas (páginas vistas y país, sin cookies) para entender el uso global y mejorar la herramienta. Estas estadísticas no permiten identificarte."),
            ("h", "Información que tú decides enviar"),
            ("p", "Si usas el formulario de comentarios, el nombre, el correo electrónico y el mensaje enviados se usan únicamente para leer y responder a tus comentarios. Si apoyas el proyecto, el pago lo procesa Creem.io como comerciante registrado — nunca recibimos tus datos completos de pago. Los partidarios solo aparecen por su nombre con su consentimiento expreso."),
            ("h", "Servicios de terceros"),
            ("p", "Las tasas las obtiene tu navegador directamente de API públicas (Frankfurter/BCE, ExchangeRate-API, Fawaz Currency API) — esas peticiones salen de tu dispositivo, no pasan por nuestros servidores. El sitio se aloja como archivos estáticos; las estadísticas anónimas pueden circular por Cloudflare."),
            ("h", "Publicidad"),
            ("p", "Este sitio puede mostrar publicidad servida mediante Google AdSense. Proveedores externos, incluido Google, usan cookies y tecnologías similares para mostrar anuncios basados en tus visitas previas a este u otros sitios web. El uso de cookies publicitarias por parte de Google permite a Google y a sus socios mostrarte anuncios según tus visitas a nuestro sitio y/u otros sitios de internet."),
            ("p", "Puedes desactivar la publicidad personalizada en la <a href=\"https://adssettings.google.com\" rel=\"noopener\">configuración de anuncios de Google</a> o excluirte de las cookies de proveedores externos en <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Cuando la ley lo exige —por ejemplo en el EEE y el Reino Unido— la publicidad personalizada solo se muestra con tu consentimiento; en caso contrario se usa publicidad no personalizada. Detalles: <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">cómo usa Google la información de los sitios que emplean sus servicios</a>."),
            ("h", "Almacenamiento local"),
            ("p", "Tu elección de tema, el tamaño de fuente, los pares de divisas guardados y el calendario del aviso de instalación se guardan en el almacenamiento local de tu navegador. Esos datos nunca salen de tu dispositivo y puedes borrarlos cuando quieras desde la configuración del navegador."),
            ("h", "Conservación y tus derechos"),
            ("p", "Los mensajes de comentarios se conservan solo el tiempo necesario para responder. Puedes pedirnos que borremos cualquier comentario enviado escribiendo a <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
            ("h", "Cambios en esta política"),
            ("p", "Si cambian las prácticas de datos del sitio, esta página se actualizará y se revisará la fecha anterior. Seguir usando el sitio tras un cambio implica aceptar la política actualizada."),
        ],
    },
    "terms": {
        "title": "Términos de uso | Fxverter",
        "desc": "Las reglas básicas para usar Fxverter: las tasas son valores de referencia, no cotizaciones; el servicio se ofrece tal cual — responsabilidad, propiedad intelectual y uso aceptable.",
        "sections": [
            ("p", "Al usar fxverter.com aceptas estos términos. Si no estás de acuerdo, no uses el sitio. Última actualización: septiembre de 2026."),
            ("h", "El servicio"),
            ("p", "Fxverter es un conversor de divisas en línea gratuito y de código abierto, ofrecido \"tal cual\" y \"según disponibilidad\", sin garantías de ningún tipo, expresas o implícitas — incluidas la exactitud, la disponibilidad o la idoneidad para un fin concreto."),
            ("h", "Los tipos de cambio son solo orientativos"),
            ("p", "Todas las tasas mostradas son tasas de referencia de fuentes públicas como bancos centrales y API de divisas abiertas, normalmente actualizadas una vez al día. Son puntos de comparación — ni cotizaciones, ni asesoramiento financiero, ni el precio que un proveedor realmente te daría. No las uses para transacciones financieras, transferencias bancarias, facturación ni contabilidad oficial; verifica siempre la tasa con tu banco antes de operar."),
            ("h", "Limitación de responsabilidad"),
            ("p", "En la máxima medida permitida por la ley, los mantenedores de Fxverter no responden de ninguna pérdida o daño derivado del uso o la imposibilidad de uso del sitio o de sus datos — incluidas las decisiones tomadas confiando en las tasas mostradas."),
            ("h", "Propiedad intelectual"),
            ("p", "El código fuente es open source bajo licencia MIT y está disponible en GitHub. Los textos, el diseño y la marca del sitio siguen siendo propiedad del proyecto Fxverter; no se permite republicar el contenido del sitio en bloque sin permiso."),
            ("h", "Servicios de terceros y enlaces"),
            ("p", "El sitio depende de API públicas de terceros y puede enlazar a sitios externos. No los controlamos y no respondemos de su contenido, disponibilidad o prácticas."),
            ("h", "Uso aceptable"),
            ("p", "Aceptas no perturbar el servicio, no intentar sobrecargarlo y no emplear herramientas automatizadas de forma que perjudique a otros visitantes."),
            ("h", "Cambios en estos términos"),
            ("p", "Estos términos pueden actualizarse de vez en cuando; la versión vigente es siempre esta página. ¿Preguntas? Escribe a <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
        ],
    },
    "contact": {
        "title": "Contacto | Fxverter",
        "desc": "Cómo contactar con el equipo de Fxverter: comentarios, correcciones de tasas, licencias y prensa — hello@fxverter.com o el formulario de comentarios en línea.",
        "sections": [
            ("p", "La forma más rápida de contactarnos es el correo electrónico: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Leemos cada mensaje y solemos responder en unos días."),
            ("h", "Sobre qué escribirnos"),
            ("li", "Comentarios e ideas de funciones — qué funciona, qué no y qué falta"),
            ("li", "Correcciones — si algo se ve mal en una página, dinos cuál"),
            ("li", "Cuestiones de licencias y republicación"),
            ("li", "Consultas de prensa y alianzas"),
            ("h", "Errores y problemas de código"),
            ("p", "Fxverter es open source — los reportes de errores y los pull requests son bienvenidos directamente en el repositorio de GitHub del proyecto, públicos y trazables."),
            ("h", "Una nota sobre las tasas"),
            ("p", "Todas las tasas son valores de referencia de fuentes públicas, actualizados a diario — las <a href=\"../guides/\">guías</a> explican qué significa eso en la práctica. Antes de escribirnos por una tasa \"incorrecta\", compárala con una segunda fuente a la misma hora: las pequeñas diferencias entre tasas de referencia y cotizaciones de proveedores son normales."),
            ("h", "Privacidad"),
            ("p", "Tu dirección de correo solo se usa para responderte — sin boletines ni marketing. Consulta la <a href=\"../privacy/\">Política de privacidad</a>."),
        ],
    },
}

# ─────────────────────────── PORTUGUÊS ───────────────────────────
TRUST["pt"] = {
    "about": {
        "title": "Sobre o Fxverter — Conversor de moedas livre e gratuito",
        "desc": "Quem está por trás do Fxverter, por que ele existe e o que o torna diferente: um conversor open-source que respeita sua privacidade, com taxas de referência honestas.",
        "sections": [
            ("p", "O Fxverter é um conversor de moedas on-line gratuito e de código aberto que funciona inteiramente no seu navegador. Ele mostra taxas de câmbio de referência para mais de 140 moedas, sem chave de API, sem cadastro e sem instalação — você abre o site e começa a converter."),
            ("h", "Por que criamos"),
            ("p", "A maioria dos sites de conversão enterra a taxa real sob pop-ups, barreiras de cadastro e insistentes pedidos de instalação de aplicativo. Queríamos o oposto: uma ferramenta rápida e privada que mostra primeiro a taxa de referência do mercado interbancário e não pede nada em troca. O produto inteiro é uma página estática que funciona em qualquer aparelho, em 29 idiomas — e até offline depois de instalada."),
            ("h", "O que o torna diferente"),
            ("li", "Sem conta e sem rastreamento — as conversões rodam no seu próprio navegador"),
            ("li", "Três fontes públicas comutáveis: Frankfurter (taxas de referência do Banco Central Europeu), ExchangeRate-API e a Fawaz Currency API"),
            ("li", "56 moedas principais com página própria: tabelas de conversão em tempo real, gráficos de 30/90 dias e perfis de moeda"),
            ("li", "Guias em linguagem simples que explicam como os câmbios realmente funcionam"),
            ("li", "Instalável como app (PWA) que continua funcionando offline com as últimas taxas conhecidas"),
            ("h", "Os dados"),
            ("p", "As taxas são valores de referência indicativos de fontes públicas (bancos centrais e mercados), atualizados diariamente. É a mesma referência que você vê no Google ou na imprensa financeira — útil para comparar e planejar, não uma cotação contratual para uma transferência específica."),
            ("h", "Quem está por trás"),
            ("p", "O Fxverter é construído e mantido por um desenvolvedor independente e sustentado por seus usuários. O código-fonte completo é público no GitHub — qualquer pessoa pode auditá-lo, hospedá-lo por conta própria ou contribuir com melhorias."),
            ("p", "Perguntas, correções ou ideias? Escreva para <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — lemos tudo."),
        ],
    },
    "privacy": {
        "title": "Política de Privacidade | Fxverter",
        "desc": "O que o Fxverter coleta e o que não coleta: sem cookies obrigatórios, sem contas, apenas estatísticas anônimas — e como publicidade e terceiros são tratados.",
        "sections": [
            ("p", "O Fxverter foi desenhado para ser usado sem entregar nenhuma informação pessoal. Esta política explica o que o site coleta e o que não coleta, e como publicidade e serviços de terceiros são tratados. Última atualização: setembro de 2026."),
            ("h", "O que não coletamos"),
            ("p", "Nenhuma conta é necessária e o próprio site não instala cookies publicitários. As conversões rodam localmente no seu navegador — nunca vemos os valores nem os pares de moedas que você converte."),
            ("h", "Informações coletadas automaticamente"),
            ("p", "Estatísticas de visita anônimas e agregadas (visualizações de página e país, sem cookies) podem ser coletadas para entender o uso geral e melhorar a ferramenta. Essas estatísticas não permitem identificá-lo."),
            ("h", "Informações que você escolhe enviar"),
            ("p", "Se você usar o formulário de feedback, o nome, o e-mail e a mensagem enviados servem apenas para ler e responder ao seu feedback. Se apoiar o projeto, o pagamento é processado pela Creem.io como merchant of record — nunca recebemos seus dados completos de pagamento. Apoiadores só aparecem pelo nome com consentimento expresso."),
            ("h", "Serviços de terceiros"),
            ("p", "As taxas são buscadas pelo seu navegador diretamente de APIs públicas (Frankfurter/BCE, ExchangeRate-API, Fawaz Currency API) — essas requisições partem do seu aparelho, não passam pelos nossos servidores. O site é hospedado como arquivos estáticos; estatísticas anônimas podem passar pelo Cloudflare."),
            ("h", "Publicidade"),
            ("p", "Este site pode exibir publicidade veiculada pelo Google AdSense. Fornecedores terceiros, incluindo o Google, usam cookies e tecnologias semelhantes para veicular anúncios com base em suas visitas anteriores a este ou a outros sites. O uso de cookies publicitários pelo Google permite que o Google e seus parceiros veiculem anúncios para você com base em suas visitas ao nosso site e/ou a outros sites da internet."),
            ("p", "Você pode desativar a publicidade personalizada nas <a href=\"https://adssettings.google.com\" rel=\"noopener\">configurações de anúncios do Google</a> ou cancelar cookies de fornecedores terceiros em <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Onde a lei exigir — por exemplo no EEE e no Reino Unido — a publicidade personalizada só é exibida com o seu consentimento; caso contrário usa-se publicidade não personalizada. Detalhes: <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">como o Google usa informações de sites que empregam seus serviços</a>."),
            ("h", "Armazenamento local"),
            ("p", "Sua escolha de tema, o tamanho da fonte, os pares de moedas salvos e o intervalo do aviso de instalação ficam no armazenamento local do seu navegador. Esses dados nunca saem do seu aparelho e podem ser apagados a qualquer momento nas configurações do navegador."),
            ("h", "Retenção e seus direitos"),
            ("p", "Mensagens de feedback são mantidas apenas pelo tempo necessário para responder. Você pode pedir a exclusão de qualquer feedback enviado escrevendo para <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
            ("h", "Mudanças nesta política"),
            ("p", "Se as práticas de dados do site mudarem, esta página será atualizada e a data acima revisada. Continuar usando o site após uma mudança significa aceitar a política atualizada."),
        ],
    },
    "terms": {
        "title": "Termos de Uso | Fxverter",
        "desc": "As regras básicas para usar o Fxverter: as taxas são valores de referência, não cotações; o serviço é oferecido no estado em que se encontra — responsabilidade, propriedade intelectual e uso aceitável.",
        "sections": [
            ("p", "Ao usar o fxverter.com você concorda com estes termos. Se não concordar, por favor não use o site. Última atualização: setembro de 2026."),
            ("h", "O serviço"),
            ("p", "O Fxverter é um conversor de moedas on-line gratuito e de código aberto, oferecido \"no estado em que se encontra\" e \"conforme disponível\", sem garantias de qualquer tipo, expressas ou implícitas — incluindo precisão, disponibilidade ou adequação a um fim específico."),
            ("h", "As taxas de câmbio são apenas indicativas"),
            ("p", "Todas as taxas exibidas são taxas de referência coletadas de fontes públicas como bancos centrais e APIs de câmbio abertas, normalmente atualizadas uma vez ao dia. São pontos de comparação — não cotações, não aconselhamento financeiro e não o preço que um provedor realmente lhe daria. Não as use para transações financeiras, transferências bancárias, faturamento ou contabilidade oficial; verifique sempre a taxa com seu banco antes de qualquer operação."),
            ("h", "Limitação de responsabilidade"),
            ("p", "Na extensão máxima permitida pela lei, os mantenedores do Fxverter não respondem por qualquer perda ou dano decorrente do uso ou da impossibilidade de uso do site ou de seus dados — incluindo decisões tomadas com base nas taxas exibidas."),
            ("h", "Propriedade intelectual"),
            ("p", "O código-fonte é open source sob a licença MIT e está disponível no GitHub. Os textos, o design e a marca do site permanecem propriedade do projeto Fxverter; republicar o conteúdo do site em bloco sem permissão não é permitido."),
            ("h", "Serviços de terceiros e links"),
            ("p", "O site depende de APIs públicas de terceiros e pode apontar para sites externos. Não os controlamos e não somos responsáveis pelo seu conteúdo, disponibilidade ou práticas."),
            ("h", "Uso aceitável"),
            ("p", "Você concorda em não interromper o serviço, não tentar sobrecarregá-lo e não usar ferramentas automatizadas de modo a prejudicar outros visitantes."),
            ("h", "Mudanças nestes termos"),
            ("p", "Estes termos podem ser atualizados de tempos em tempos; a versão vigente é sempre esta página. Perguntas? Escreva para <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."),
        ],
    },
    "contact": {
        "title": "Contato | Fxverter",
        "desc": "Como falar com a equipe do Fxverter: feedback, correções de taxas, licenciamento e imprensa — hello@fxverter.com ou o formulário de feedback on-line.",
        "sections": [
            ("p", "A forma mais rápida de falar conosco é o e-mail: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Lemos cada mensagem e costumamos responder em poucos dias."),
            ("h", "Sobre o que escrever"),
            ("li", "Feedback e ideias de recursos — o que funciona, o que não funciona e o que falta"),
            ("li", "Correções — se algo parece errado numa página, diga-nos qual"),
            ("li", "Questões de licenciamento e republicação"),
            ("li", "Consultas de imprensa e parcerias"),
            ("h", "Bugs e problemas de código"),
            ("p", "O Fxverter é open source — relatos de bugs e pull requests são bem-vindos diretamente no repositório do projeto no GitHub, públicos e rastreáveis."),
            ("h", "Uma nota sobre as taxas"),
            ("p", "Todas as taxas são valores de referência de fontes públicas, atualizados diariamente — os <a href=\"../guides/\">guias</a> explicam o que isso significa na prática. Antes de escrever sobre uma taxa \"errada\", compare com uma segunda fonte no mesmo horário: pequenas diferenças entre taxas de referência e cotações de provedores são normais."),
            ("h", "Privacidade"),
            ("p", "Seu endereço de e-mail é usado apenas para responder — sem newsletter, sem marketing. Veja a <a href=\"../privacy/\">Política de Privacidade</a>."),
        ],
    },
}

# ─────────────────────────── 日本語 ───────────────────────────
TRUST["ja"] = {
    "about": {
        "title": "Fxverter について — 無料・オープンソースの通貨コンバーター",
        "desc": "Fxverter を作っているのは誰か、なぜ存在するのか、何が違うのか：プライバシー第一の中間レートを表示するオープンソース通貨コンバーター。",
        "sections": [
            ("p", "Fxverter はブラウザ上だけで動く、無料のオープンソース通貨コンバーターです。140 以上の世界通貨の参考為替レートを表示し、API キーも登録もインストールも不要——サイトを開けばすぐ換算できます。"),
            ("h", "なぜ作ったのか"),
            ("p", "ほとんどの換算サイトは、ポップアップや登録の壁、アプリ導入の催促の下に本当のレートを埋めています。私たちはその逆を作りたかった——誠実なミッドマーケットの参考レートを真っ先に見せて、あとは何も求めない、速くてプライバシーに配慮したツールです。製品全体が 1 枚の静的ページで、29 か国語、どんなデバイスでも動き、インストール後はオフラインでも使えます。"),
            ("h", "他と違うところ"),
            ("li", "アカウント不要・トラッキングなし——換算はあなたのブラウザ内で完結します"),
            ("li", "切り替え可能な 3 つの公開データソース：Frankfurter（欧州中央銀行の参考レート）、ExchangeRate-API、Fawaz Currency API"),
            ("li", "主要 56 通貨に専用ページ：リアルタイム換算表、30/90 日のトレンドチャート、通貨プロフィール"),
            ("li", "為替レートの仕組みを平易な言葉で解説するガイド"),
            ("li", "アプリ（PWA）としてインストールでき、オフラインでも最後の既知レートで動作"),
            ("h", "データについて"),
            ("p", "レートは公開されている中央銀行・市場データソース由来の参考レートで、毎日更新されます。Google や経済ニュースで見るのと同じベンチマークであり、比較や計画には役立ちますが、特定の送金のための契約上の見積もりではありません。"),
            ("h", "運営者について"),
            ("p", "Fxverter は独立した開発者が構築・保守し、利用者の支援によって運営されています。ソースコードは GitHub で完全に公開されており、誰でも監査・セルフホスト・改善の貢献ができます。"),
            ("p", "ご質問・訂正・ご意見は <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> へ——すべて目を通しています。"),
        ],
    },
    "privacy": {
        "title": "プライバシーポリシー | Fxverter",
        "desc": "Fxverter が収集するものとしないもの：Cookie 不要・アカウント不要・匿名統計のみ——広告と第三者サービスの扱いについて。",
        "sections": [
            ("p", "Fxverter は、個人情報を一切提供しなくても利用できるよう設計されています。本ポリシーは、当サイトが収集するものとしないもの、広告および第三者サービスの扱いを説明します。最終更新：2026 年 9 月。"),
            ("h", "収集しないもの"),
            ("p", "アカウントは不要で、当サイト自身は広告用 Cookie を設定しません。換算はブラウザ内でローカルに実行されるため、換算された金額や通貨ペアは当方からは一切見えません。"),
            ("h", "自動的に収集される情報"),
            ("p", "全体的な利用状況の把握とツール改善のため、匿名化された集計統計（閲覧数と国、Cookie 不要）を収集する場合があります。これらの統計からあなたを特定することはできません。"),
            ("h", "ご自身で送信する情報"),
            ("p", "フィードバックフォームを利用した場合、送信された氏名・メールアドレス・メッセージは、フィードバックの閲読と返信のためだけに使われます。プロジェクトを支援いただいた場合、決済は記録上の販売者（merchant of record）である Creem.io が処理し、当方は完全な決済情報を受け取りません。サポーターの氏名は、明示的な同意がある場合にのみ掲載します。"),
            ("h", "第三者サービス"),
            ("p", "為替レートはブラウザが公開 API（Frankfurter/ECB、ExchangeRate-API、Fawaz Currency API）から直接取得します——これらのリクエストはあなたのデバイスから発信され、当方のサーバーを経由しません。当サイトは静的ファイルとしてホストされ、匿名統計は Cloudflare 経由で行われる場合があります。"),
            ("h", "広告"),
            ("p", "当サイトでは Google AdSense による広告を表示することがあります。Google を含む第三者のベンダーは、このサイトや他のサイトへの過去のアクセスに基づいて広告を配信するために、Cookie および類似の技術を使用します。Google による広告 Cookie の利用により、Google とそのパートナーは、当サイトやインターネット上の他サイトへのアクセスに基づいて広告を表示できます。"),
            ("p", "パーソナライズ広告は <a href=\"https://adssettings.google.com\" rel=\"noopener\">Google 広告設定</a>で無効化でき、第三者ベンダーの Cookie は <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a> でオプトアウトできます。法律で求められる地域（EEA および英国など）では、パーソナライズ広告は同意がある場合にのみ表示され、それ以外では非パーソナライズ広告が使用されます。詳細は <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">Google によるサービス利用サイトの情報の取り扱い</a>をご覧ください。"),
            ("h", "ローカルストレージ"),
            ("p", "テーマの選択、文字サイズ、保存した通貨ペア、インストールバナーの表示間隔は、ブラウザのローカルストレージに保存されます。これらのデータが端末の外に出ることはなく、ブラウザ設定からいつでも消去できます。"),
            ("h", "保存期間とお客様の権利"),
            ("p", "フィードバックのメッセージは、返信に必要な期間のみ保管します。送信済みのフィードバックの削除をご希望の場合は <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> までご連絡ください。"),
            ("h", "ポリシーの変更"),
            ("p", "当サイトのデータ取り扱いが変わった場合は、本ページを更新し上記の日付を改訂します。変更後も当サイトを利用し続けた場合は、更新後のポリシーに同意したものとみなされます。"),
        ],
    },
    "terms": {
        "title": "利用規約 | Fxverter",
        "desc": "Fxverter の利用ルール：レートは参考値であり見積もりではありません。サービスは現状有姿で提供され、責任・知的財産・許容される利用について定めています。",
        "sections": [
            ("p", "fxverter.com を利用することで、本規約に同意したものとみなされます。同意できない場合は、当サイトを利用しないでください。最終更新：2026 年 9 月。"),
            ("h", "サービスについて"),
            ("p", "Fxverter は無料のオープンソース通貨コンバーターであり、「現状有姿」かつ「利用可能な範囲で」、明示・黙示を問わず一切の保証なく提供されます——正確性、可用性、特定目的への適合性を含みます。"),
            ("h", "為替レートは参考値です"),
            ("p", "表示されるすべてのレートは、中央銀行や公開為替 API などの公開ソースから収集した参考レートで、通常は 1 日 1 回更新されます。これらは比較のためのベンチマークであり、見積もりでも金融アドバイスでもなく、実際のプロバイダが提示する価格でもありません。金融取引・銀行送金・請求書発行・公式の会計処理には使用しないでください。取引の前に必ず銀行等でレートをご確認ください。"),
            ("h", "責任の制限"),
            ("p", "法律で認められる最大限の範囲において、Fxverter の開発者は、当サイトまたはそのデータの利用・利用不能から生じたいかなる損害についても責任を負いません——表示されたレートに基づいて行われた判断を含みます。"),
            ("h", "知的財産権"),
            ("p", "ソースコードは MIT ライセンスのオープンソースとして GitHub で公開されています。サイトの文章・デザイン・ブランドは Fxverter プロジェクトに帰属し、許可なくサイトの内容を丸ごと再掲することはできません。"),
            ("h", "第三者サービスとリンク"),
            ("p", "当サイトは第三者の公開 API に依存し、外部サイトへリンクすることがあります。これらを管理しておらず、その内容・可用性・慣行について責任を負いません。"),
            ("h", "許容される利用"),
            ("p", "サービスを妨害しないこと、過負荷をかけようとしないこと、他の訪問者の利用を損なう形で自動化ツールを使用しないことに同意いただきます。"),
            ("h", "規約の変更"),
            ("p", "本規約は随時更新されることがあり、常にこのページの内容が現行版です。ご質問は <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> まで。"),
        ],
    },
    "contact": {
        "title": "お問い合わせ | Fxverter",
        "desc": "Fxverter チームへの連絡方法：フィードバック、レートの訂正、ライセンス、報道——hello@fxverter.com またはオンラインのフィードバックフォーム。",
        "sections": [
            ("p", "最も速い連絡手段はメールです：<a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>。すべてのメッセージに目を通し、通常は数日以内に返信します。"),
            ("h", "こんな内容を歓迎します"),
            ("li", "フィードバックと機能のアイデア——使えるところ、使えないところ、足りないところ"),
            ("li", "訂正——ページに問題があれば、どのページかをお知らせください"),
            ("li", "ライセンスや転載に関するご相談"),
            ("li", "報道・提携のお問い合わせ"),
            ("h", "バグとコードの問題"),
            ("p", "Fxverter はオープンソースです——バグ報告やプルリクエストは、プロジェクトの GitHub リポジトリで直接受け付けています。公開され、追跡可能です。"),
            ("h", "レートについてのひとこと"),
            ("p", "すべてのレートは公開ソース由来の参考値で、毎日更新されます。実際の意味は<a href=\"../guides/\">ガイド</a>で解説しています。「レートが違う」とご連絡の前には、同じ時間帯に別のソースと比較してみてください。参考レートとプロバイダの提示レートとの小さな差は正常です。"),
            ("h", "プライバシー"),
            ("p", "メールアドレスは返信のためだけに使用します——メルマガもマーケティングもありません。詳細は<a href=\"../privacy/\">プライバシーポリシー</a>をご覧ください。"),
        ],
    },
}

# ═══════════════════════════════════════════════════════════════
# Feedback pages — standalone /feedback/ form page (splitforms).
# The inline toolbar panel stays, but the form now also has its own
# findable page linked from every trust-links row.
# ═══════════════════════════════════════════════════════════════

TRUST_LABELS["en"]["feedback"] = "Feedback"
TRUST_LABELS["zh"]["feedback"] = "意见反馈"
TRUST_LABELS["de"]["feedback"] = "Feedback"
TRUST_LABELS["fr"]["feedback"] = "Commentaires"
TRUST_LABELS["es"]["feedback"] = "Comentarios"
TRUST_LABELS["pt"]["feedback"] = "Feedback"
TRUST_LABELS["ja"]["feedback"] = "フィードバック"

FEEDBACK = {
    "en": {
        "title": "Send Feedback | Fxverter",
        "desc": "Tell us what works, what breaks and what's missing — the Fxverter feedback form goes straight to the team's inbox, no account needed.",
        "sections": [
            ("p", "Found a bug, a rate that looks off, or an idea that would make Fxverter more useful? The form below goes straight to our inbox — no account needed, and it takes about thirty seconds."),
            ("h", "What helps us most"),
            ("li", "Which page or feature you were using"),
            ("li", "What you expected and what actually happened"),
            ("li", "Your browser or device, if the problem is visual"),
            ("h", "Prefer email?"),
            ("p", "Write to <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — or just use the form below, it reaches the same place."),
        ],
        "form": {
            "name": "Name (optional)",
            "email": "Email (optional — only if you want a reply)",
            "message": "Your message",
            "send": "Send feedback",
            "ok": "✓ Feedback sent — thank you!",
            "empty": "Please write a message first.",
            "fail": "Sending failed — please email hello@fxverter.com directly.",
        },
    },
    "zh": {
        "title": "意见反馈 | Fxverter",
        "desc": "告诉我们哪里好用、哪里出问题、还缺什么——Fxverter 反馈表单直达团队邮箱，无需注册。",
        "sections": [
            ("p", "发现了问题、某个汇率看起来不对，或者有能让 Fxverter 更好用的想法？下面的表单直达我们的邮箱——无需注册，大约 30 秒就能填完。"),
            ("h", "怎样写最有帮助"),
            ("li", "你在使用哪个页面或功能"),
            ("li", "你期望发生什么、实际发生了什么"),
            ("li", "如果是显示问题，说明你的浏览器或设备"),
            ("h", "更想写邮件？"),
            ("p", "写信到 <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>——或者直接用下面的表单，两者都会到达同一处。"),
        ],
        "form": {
            "name": "姓名（可选）",
            "email": "邮箱（可选——需要回复时填写）",
            "message": "你的反馈",
            "send": "发送反馈",
            "ok": "✓ 反馈已发送——感谢！",
            "empty": "请先写下反馈内容。",
            "fail": "发送失败——请直接发邮件到 hello@fxverter.com。",
        },
    },
    "de": {
        "title": "Feedback senden | Fxverter",
        "desc": "Sag uns, was funktioniert, was klemmt und was fehlt — das Fxverter-Feedback-Formular landet direkt im Postfach des Teams, ohne Konto.",
        "sections": [
            ("p", "Einen Fehler gefunden, einen Kurs, der seltsam aussieht, oder eine Idee, die Fxverter nützlicher macht? Das Formular unten landet direkt in unserem Postfach — ohne Konto, in etwa dreißig Sekunden ausgefüllt."),
            ("h", "Was uns am meisten hilft"),
            ("li", "Welche Seite oder Funktion du benutzt hast"),
            ("li", "Was du erwartet hast und was tatsächlich passiert ist"),
            ("li", "Browser oder Gerät, falls das Problem visuell ist"),
            ("h", "Lieber eine E-Mail?"),
            ("p", "Schreib an <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — oder nutze einfach das Formular unten, beides kommt am selben Ort an."),
        ],
        "form": {
            "name": "Name (optional)",
            "email": "E-Mail (optional — nur wenn du eine Antwort möchtest)",
            "message": "Deine Nachricht",
            "send": "Feedback senden",
            "ok": "✓ Feedback gesendet — vielen Dank!",
            "empty": "Bitte zuerst eine Nachricht schreiben.",
            "fail": "Senden fehlgeschlagen — bitte direkt eine E-Mail an hello@fxverter.com schreiben.",
        },
    },
    "fr": {
        "title": "Envoyer un commentaire | Fxverter",
        "desc": "Dites-nous ce qui marche, ce qui coince et ce qui manque — le formulaire de Fxverter arrive directement dans la boîte de l'équipe, sans compte.",
        "sections": [
            ("p", "Un bug, un taux qui semble faux, ou une idée qui rendrait Fxverter plus utile ? Le formulaire ci-dessous arrive directement dans notre boîte — sans compte, et cela prend une trentaine de secondes."),
            ("h", "Ce qui nous aide le plus"),
            ("li", "La page ou la fonctionnalité utilisée"),
            ("li", "Ce que vous attendiez et ce qui s'est réellement passé"),
            ("li", "Votre navigateur ou appareil, si le problème est visuel"),
            ("h", "Plutôt un e-mail ?"),
            ("p", "Écrivez à <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — ou utilisez simplement le formulaire ci-dessous, cela arrive au même endroit."),
        ],
        "form": {
            "name": "Nom (facultatif)",
            "email": "E-mail (facultatif — seulement si vous souhaitez une réponse)",
            "message": "Votre message",
            "send": "Envoyer le commentaire",
            "ok": "✓ Commentaire envoyé — merci !",
            "empty": "Veuillez d'abord écrire un message.",
            "fail": "Échec de l'envoi — écrivez directement à hello@fxverter.com.",
        },
    },
    "es": {
        "title": "Enviar comentarios | Fxverter",
        "desc": "Cuéntanos qué funciona, qué falla y qué falta — el formulario de Fxverter llega directo al buzón del equipo, sin cuenta.",
        "sections": [
            ("p", "¿Encontraste un error, un tipo de cambio que se ve raro, o una idea que haría Fxverter más útil? El formulario de abajo llega directo a nuestro buzón — sin cuenta, y se llena en unos treinta segundos."),
            ("h", "Lo que más nos ayuda"),
            ("li", "Qué página o función estabas usando"),
            ("li", "Qué esperabas y qué pasó en realidad"),
            ("li", "Tu navegador o dispositivo, si el problema es visual"),
            ("h", "¿Prefieres el correo?"),
            ("p", "Escribe a <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — o usa el formulario de abajo, ambos llegan al mismo lugar."),
        ],
        "form": {
            "name": "Nombre (opcional)",
            "email": "Correo (opcional — solo si quieres respuesta)",
            "message": "Tu mensaje",
            "send": "Enviar comentarios",
            "ok": "✓ Comentarios enviados — ¡gracias!",
            "empty": "Escribe un mensaje primero.",
            "fail": "Error al enviar — escribe directamente a hello@fxverter.com.",
        },
    },
    "pt": {
        "title": "Enviar feedback | Fxverter",
        "desc": "Conte-nos o que funciona, o que falha e o que falta — o formulário do Fxverter chega direto à caixa da equipe, sem cadastro.",
        "sections": [
            ("p", "Encontrou um bug, uma taxa que parece errada, ou uma ideia que deixaria o Fxverter mais útil? O formulário abaixo chega direto à nossa caixa — sem cadastro, e leva uns trinta segundos."),
            ("h", "O que mais nos ajuda"),
            ("li", "Qual página ou recurso você estava usando"),
            ("li", "O que você esperava e o que realmente aconteceu"),
            ("li", "Seu navegador ou aparelho, se o problema for visual"),
            ("h", "Prefere e-mail?"),
            ("p", "Escreva para <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — ou use o formulário abaixo, ambos chegam ao mesmo lugar."),
        ],
        "form": {
            "name": "Nome (opcional)",
            "email": "E-mail (opcional — só se quiser resposta)",
            "message": "Sua mensagem",
            "send": "Enviar feedback",
            "ok": "✓ Feedback enviado — obrigado!",
            "empty": "Escreva uma mensagem primeiro.",
            "fail": "Falha no envio — escreva diretamente para hello@fxverter.com.",
        },
    },
    "ja": {
        "title": "フィードバックを送る | Fxverter",
        "desc": "使えるところ、問題のあるところ、足りないところをお知らせください——Fxverter のフィードバックフォームはチームの受信箱に直接届きます。アカウント不要。",
        "sections": [
            ("p", "バグ、妙に見えるレート、あるいは Fxverter をもっと便利にするアイデアを見つけましたか？下のフォームは私たちの受信箱に直接届きます——アカウント不要、30 秒ほどで入力できます。"),
            ("h", "ありがたい情報"),
            ("li", "どのページ・機能を使っていたか"),
            ("li", "何を期待して、実際に何が起きたか"),
            ("li", "表示の問題ならブラウザやデバイスの種類"),
            ("h", "メールがよい方は"),
            ("p", "<a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> へどうぞ——または下のフォームから。どちらも同じ場所に届きます。"),
        ],
        "form": {
            "name": "お名前（任意）",
            "email": "メールアドレス（任意 — 返信をご希望の場合のみ）",
            "message": "メッセージ",
            "send": "フィードバックを送信",
            "ok": "✓ フィードバックを送信しました — ありがとうございます！",
            "empty": "先にメッセージを入力してください。",
            "fail": "送信に失敗しました — hello@fxverter.com まで直接メールをお願いします。",
        },
    },
}
for _lang, _fb in FEEDBACK.items():
    TRUST[_lang]["feedback"] = _fb

# ── Contact pages: the site is for general visitors — replace the
# developer-facing GitHub/bugs section with a pointer to the feedback form.
_CONTACT_PATCH = {
    "en": ("Bugs and code issues", "The quick way",
           "Don't feel like writing an email? Use the <a href=\"../feedback/\">online feedback form</a> — it reaches the same inbox and takes about thirty seconds."),
    "zh": ("错误与代码问题", "更快的方式",
           "懒得写邮件？使用<a href=\"../feedback/\">在线反馈表单</a>——同样直达我们的邮箱，大约 30 秒就能填完。"),
    "de": ("Fehler und Code-Probleme", "Der schnelle Weg",
           "Keine Lust auf eine E-Mail? Nutze das <a href=\"../feedback/\">Online-Feedback-Formular</a> — es landet im selben Postfach und ist in etwa dreißig Sekunden ausgefüllt."),
    "fr": ("Bugs et problèmes de code", "Le plus rapide",
           "Pas envie d'écrire un e-mail ? Utilisez le <a href=\"../feedback/\">formulaire de commentaires en ligne</a> — il arrive dans la même boîte et prend une trentaine de secondes."),
    "es": ("Errores y problemas de código", "La vía rápida",
           "¿No te apetece escribir un correo? Usa el <a href=\"../feedback/\">formulario de comentarios en línea</a> — llega a la misma bandeja y lleva unos treinta segundos."),
    "pt": ("Bugs e problemas de código", "O jeito rápido",
           "Sem vontade de escrever um e-mail? Use o <a href=\"../feedback/\">formulário de feedback on-line</a> — chega à mesma caixa de entrada e leva cerca de trinta segundos."),
    "ja": ("バグとコードの問題", "もっと手軽な方法",
           "メールを書くのが面倒なときは、<a href=\"../feedback/\">オンラインのフィードバックフォーム</a>を——同じ受信箱に届き、30 秒ほどで入力できます。"),
}
for _lang, (_old_h, _new_h, _new_p) in _CONTACT_PATCH.items():
    _secs = TRUST[_lang]["contact"]["sections"]
    for _i, _s in enumerate(_secs):
        if _s[0] == "h" and _s[1] == _old_h:
            _secs[_i:_i + 2] = [("h", _new_h), ("p", _new_p)]
            break

# ═══════════════════════════════════════════════════════════════
# Support pages — "Buy us a Coke" sponsorship theme, Creem checkout.
# Tier URLs stay empty until the Creem products are created: paste the
# checkout links as the third tuple element and the pending note
# disappears automatically.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"] = {
    "en": "Fxverter is free to use — no account, no tracking. If it has helped you convert a rate or two, buy us a Coke: every contribution goes toward the domain, servers and continued development. Payments are processed by Creem as merchant of record — your payment data is handled by Creem, not by this website.",
    "zh": "Fxverter 完全免费——无需账号、无追踪。如果它帮你换算过汇率，不妨请我们喝杯可乐：每一份赞助都用于域名、服务器和持续开发。付款由 Creem 作为记录商户处理——你的支付数据由 Creem 处理，而非本网站。",
    "de": "Fxverter ist kostenlos — ohne Konto, ohne Tracking. Wenn es dir bei dem einen oder anderen Kurs geholfen hat, spendier uns eine Cola: Jeder Beitrag fließt in Domain, Server und die Weiterentwicklung. Zahlungen werden über Creem als Merchant of Record abgewickelt — deine Zahlungsdaten werden von Creem verarbeitet, nicht von dieser Website.",
    "fr": "Fxverter est gratuit — sans compte, sans suivi. S'il vous a aidé à convertir un taux ou deux, offrez-nous un Coca : chaque contribution finance le domaine, les serveurs et le développement continu. Les paiements sont traités par Creem en tant que marchand de référence — vos données de paiement sont gérées par Creem, non par ce site.",
    "es": "Fxverter es gratis — sin cuenta, sin seguimiento. Si te ha ayudado a convertir algún que otro tipo de cambio, invítanos a un refresco: cada contribución se destina al dominio, los servidores y el desarrollo continuo. Los pagos los procesa Creem como comerciante registrado — tus datos de pago los gestiona Creem, no este sitio web.",
    "pt": "O Fxverter é gratuito — sem conta, sem rastreamento. Se ele já te ajudou a converter alguma taxa, nos dê um refrigerante: cada contribuição vai para o domínio, os servidores e o desenvolvimento contínuo. Os pagamentos são processados pela Creem como merchant of record — seus dados de pagamento são tratados pela Creem, não por este site.",
    "ja": "Fxverter は無料で利用でき、アカウント登録もトラッキングもありません。換算が少しでも役に立ったと感じたら、コーラをおごってください：すべての支援はドメイン・サーバー・開発の継続に使われます。決済は Creem が記録上の販売者として処理し、支払いデータはこのサイトではなく Creem が取り扱います。",
}

TRUST_OVERRIDES["support"] = {
    "en": {
        "headline": "♥ Buy us a Coke",
        "choose": "Pick a round",
        "perk": "This isn't a donation — it's a small digital thank-you: pick a tier and your name (with an optional one-line message) is listed on the supporters wall below, permanently — or anonymously, if you prefer.",
        "tiers": [("A can of Coke", "$2", ""), ("A six-pack", "$9", ""), ("A whole crate", "$29", "")],
        "note": "Our Creem checkout links are being set up — want to chip in right now? Email <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> and we'll sort it out.",
        "claim": {
                        "title": "Already supported? Claim your spot",
                        "name": "Display name",
                        "message": "One-line message (optional)",
                        "email": "Email used at checkout",
                        "anon": "List me as anonymous",
                        "send": "Claim my listing",
                        "ok": "✓ You're on the wall — refresh to see it.",
                        "fail": "Could not verify the payment — email hello@fxverter.com.",
                        "nopaid": "No matching payment found for this email yet.",
                        "needEmail": "Please enter the email you paid with.",
                        "anonLabel": "Anonymous"
                },
    },
    "zh": {
        "headline": "♥ 请我们喝杯可乐",
        "choose": "选一档请我们喝",
        "perk": "这不是捐款，而是一份数字谢礼：选择任一档位后，你的名字（可附一句留言）会永久展示在本页底部的支持者名单里，也可以选择匿名。",
        "tiers": [("一罐可乐", "$2", ""), ("六罐装", "$9", ""), ("一整箱", "$29", "")],
        "note": "Creem 收款链接正在配置中——想现在支持？直接发邮件到 <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>。",
        "claim": {
                        "title": "已经支持了？认领你的名单",
                        "name": "显示的名字",
                        "message": "一句话留言（可选）",
                        "email": "支付时用的邮箱",
                        "anon": "匿名展示",
                        "send": "认领我的名单",
                        "ok": "✓ 已提交——刷新页面就能看到。",
                        "fail": "验证支付失败——请发邮件到 hello@fxverter.com。",
                        "nopaid": "暂未找到与该邮箱匹配的支付记录。",
                        "needEmail": "请填写支付时使用的邮箱。",
                        "anonLabel": "匿名"
                },
    },
    "de": {
        "headline": "♥ Spendier uns eine Cola",
        "choose": "Runde auswählen",
        "perk": "Das ist keine Spende, sondern ein kleines digitales Dankeschön: Wähle ein Paket und dein Name (mit optionaler Zeile) erscheint dauerhaft unten in der Unterstützerliste — oder anonym, wenn du magst.",
        "tiers": [("Eine Dose Cola", "$2", ""), ("Ein Sixpack", "$9", ""), ("Eine ganze Kiste", "$29", "")],
        "note": "Die Creem-Zahlungslinks werden gerade eingerichtet — du möchtest jetzt unterstützen? Schreib direkt an <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
                        "title": "Schon unterstützt? Sichere dir deinen Platz",
                        "name": "Anzeigename",
                        "message": "Eine Zeile (optional)",
                        "email": "Beim Kauf verwendete E-Mail",
                        "anon": "Anonym anzeigen",
                        "send": "Eintrag anfordern",
                        "ok": "✓ Eingetragen — lade die Seite neu, um es zu sehen.",
                        "fail": "Zahlung konnte nicht verifiziert werden — schreib an hello@fxverter.com.",
                        "nopaid": "Noch keine passende Zahlung zu dieser E-Mail gefunden.",
                        "needEmail": "Bitte die E-Mail angeben, mit der bezahlt wurde.",
                        "anonLabel": "Anonym"
                },
    },
    "fr": {
        "headline": "♥ Offrez-nous un Coca",
        "choose": "Choisissez votre tournée",
        "perk": "Ce n'est pas un don, mais un petit merci numérique : choisissez un palier et votre nom (avec un message facultatif) figure en permanence dans la liste des soutiens ci-dessous — ou anonymement, si vous préférez.",
        "tiers": [("Une canette de cola", "$2", ""), ("Un pack de six", "$9", ""), ("Une caisse entière", "$29", "")],
        "note": "Les liens de paiement Creem sont en cours de configuration — vous voulez nous soutenir maintenant ? Écrivez à <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
                        "title": "Déjà soutenu ? Réservez votre place",
                        "name": "Nom affiché",
                        "message": "Un message d'une ligne (facultatif)",
                        "email": "E-mail utilisé pour le paiement",
                        "anon": "M'afficher anonymement",
                        "send": "Réclamer mon entrée",
                        "ok": "✓ C'est en ligne — actualisez la page pour le voir.",
                        "fail": "Vérification du paiement impossible — écrivez à hello@fxverter.com.",
                        "nopaid": "Aucun paiement correspondant à cet e-mail pour l'instant.",
                        "needEmail": "Indiquez l'e-mail utilisé pour le paiement.",
                        "anonLabel": "Anonyme"
                },
    },
    "es": {
        "headline": "♥ Invítanos a un refresco",
        "choose": "Elige una ronda",
        "perk": "No es una donación, es un pequeño agradecimiento digital: elige un nivel y tu nombre (con un mensaje opcional) aparecerá de forma permanente en la lista de partidarios de abajo — o de forma anónima, si lo prefieres.",
        "tiers": [("Una lata", "$2", ""), ("Pack de seis", "$9", ""), ("Una caja entera", "$29", "")],
        "note": "Estamos configurando los enlaces de pago de Creem — ¿quieres apoyarnos ya? Escribe a <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
                        "title": "¿Ya apoyaste? Reclama tu lugar",
                        "name": "Nombre a mostrar",
                        "message": "Mensaje de una línea (opcional)",
                        "email": "Correo usado en el pago",
                        "anon": "Mostrarme como anónimo",
                        "send": "Reclamar mi lugar",
                        "ok": "✓ Estás en la lista — actualiza para verlo.",
                        "fail": "No se pudo verificar el pago — escribe a hello@fxverter.com.",
                        "nopaid": "Aún no hay un pago que coincida con este correo.",
                        "needEmail": "Introduce el correo con el que pagaste.",
                        "anonLabel": "Anónimo"
                },
    },
    "pt": {
        "headline": "♥ Nos convide para um refrigerante",
        "choose": "Escolha uma rodada",
        "perk": "Não é uma doação — é um pequeno agradecimento digital: escolha um nível e o seu nome (com uma mensagem opcional) aparecerá permanentemente na lista de apoiadores abaixo — ou anonimamente, se preferir.",
        "tiers": [("Uma lata", "$2", ""), ("Pack com seis", "$9", ""), ("Uma caixa inteira", "$29", "")],
        "note": "Os links de pagamento do Creem estão sendo configurados — quer apoiar agora? Escreva para <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
                        "title": "Já apoiou? Reserve o seu lugar",
                        "name": "Nome a exibir",
                        "message": "Mensagem de uma linha (opcional)",
                        "email": "E-mail usado no pagamento",
                        "anon": "Exibir-me como anônimo",
                        "send": "Reservar meu lugar",
                        "ok": "✓ Você está na lista — atualize a página para ver.",
                        "fail": "Não foi possível verificar o pagamento — escreva para hello@fxverter.com.",
                        "nopaid": "Ainda não há pagamento correspondente a este e-mail.",
                        "needEmail": "Informe o e-mail usado no pagamento.",
                        "anonLabel": "Anônimo"
                },
    },
    "ja": {
        "headline": "♥ コーラをおごる",
        "choose": "おごる本数を選ぶ",
        "perk": "これは寄付ではなく、小さなデジタルな感謝のしるしです：いずれかのプランを選ぶと、あなたの名前（一言メッセージ可）がこのページ下部のサポーターリストに恒久掲載されます。匿名も選べます。",
        "tiers": [("コーラ 1 本", "$2", ""), ("6 本パック", "$9", ""), ("1 ケース", "$29", "")],
        "note": "Creem の決済リンクは準備中です——今すぐ支援したい方は <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> までメールをどうぞ。",
        "claim": {
                        "title": "すでに支援済み？掲載を申し込む",
                        "name": "表示名",
                        "message": "ひとことメッセージ（任意）",
                        "email": "決済時に使ったメールアドレス",
                        "anon": "匿名で掲載",
                        "send": "名簿に掲載する",
                        "ok": "✓ 掲載されました——更新すると表示されます。",
                        "fail": "決済を確認できませんでした——hello@fxverter.com までご連絡ください。",
                        "nopaid": "このメールアドレスに一致する決済記録がまだありません。",
                        "needEmail": "決済に使用したメールアドレスを入力してください。",
                        "anonLabel": "匿名"
                },
    },
}

# FAQ heading on flagship currency pages (rendered above the FAQ details).
TRUST_OVERRIDES["curFaq"] = {
    "en": "Frequently asked questions",
    "zh": "常见问题",
    "de": "Häufig gestellte Fragen",
    "fr": "Questions fréquentes",
    "es": "Preguntas frecuentes",
    "pt": "Perguntas frequentes",
    "ja": "よくある質問",
    "ko": "자주 묻는 질문",
    "ru": "Часто задаваемые вопросы",
    "hi": "अक्सर पूछे जाने वाले प्रश्न",
    "ar": "الأسئلة الشائعة",
    "it": "Domande frequenti",
    "th": "คำถามที่พบบ่อย",
    "tr": "Sıkça sorulan sorular",
    "id": "Pertanyaan yang sering diajukan",
    "ms": "Soalan lazim",
    "tl": "Mga madalas itanong",
    "nl": "Veelgestelde vragen",
    "pl": "Często zadawane pytania",
    "uk": "Часті запитання",
    "sv": "Vanliga frågor",
    "vi": "Câu hỏi thường gặp",
    "el": "Συχνές ερωτήσεις",
    "lo": "ຄຳຖາມທີ່ພົບເລື້ອຍ",
    "bn": "সাধারণ প্রশ্ন",
    "fa": "سوالات متداول",
    "cs": "Často kladené otázky",
    "ro": "Întrebări frecvente",
    "da": "Ofte stillede spørgsmål",
}


# ═══════════════════════════════════════════════════════════════
# Round-5 extension: ads-aware support & privacy copy for the six
# languages promoted in round 4 (ko/ru/hi/ar/it/th). Until now these
# six fell back to the pre-advertising texts in content_ui/page_meta,
# which still claimed "no ads" — contradicting their own privacy pages.
# Same structures as the seven canonical languages above.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"].update({
    "ko": "Fxverter는 무료이며 계정도 추적도 없습니다. 몇 번의 환율 확인에 도움이 되었다면 콜라 한 캔 사 주는 건 어떨까요: 모든 후원금은 도메인·서버·지속적인 개발에 쓰입니다. 결제는 Creem이 기록 판매자(merchant of record)로 처리하며, 결제 데이터는 이 사이트가 아니라 Creem이 다룹니다.",
    "ru": "Fxverter бесплатен — без аккаунтов и слежки. Если он помог вам перевести пару курсов, угостите нас колой: каждый взнос идёт на домен, серверы и дальнейшую разработку. Платежи обрабатывает Creem в качестве merchant of record — ваши платёжные данные обрабатывает Creem, а не этот сайт.",
    "hi": "Fxverter मुफ़्त है — न खाता, न ट्रैकिंग। अगर इसने आपकी कुछ दरें बदलने में मदद की, तो हमें एक कोला दिला दें: हर योगदान डोमेन, सर्वर और निरंतर विकास में लगता है। भुगतान Creem के ज़रिए merchant of record के रूप में संसाधित होता है — आपका भुगतान डेटा इस वेबसाइट नहीं, Creem संभालता है।",
    "ar": "Fxverter مجاني — بلا حسابات ولا تتبّع. إذا ساعدك في تحويل سعر أو سعرين، أكرمنا بعلبة كولا: كل مساهمة تذهب إلى النطاق والخوادم والتطوير المستمر. تُعالَج المدفوعات عبر Creem بصفته التاجر المسجّل (merchant of record) — بيانات الدفع يديرها Creem لا هذا الموقع.",
    "it": "Fxverter è gratuito — senza account e senza tracciamento. Se ti ha aiutato a convertire un tasso o due, offrici una Coca: ogni contributo va a dominio, server e sviluppo continuo. I pagamenti sono elaborati da Creem in qualità di merchant of record — i tuoi dati di pagamento sono gestiti da Creem, non da questo sito.",
    "th": "Fxverter ใช้ฟรี — ไม่มีบัญชี ไม่มีการติดตาม ถ้าช่วยคุณแปลงอัตราได้ไม่กี่ครั้ง ชวนเราดื่มโค้กสักกระป๋อง: ทุกการสนับสนุนนำไปใช้กับโดเมน เซิร์ฟเวอร์ และการพัฒนาต่อ การชำระเงินดำเนินการโดย Creem ในฐานะผู้ขายผู้บันทึกรายการ (merchant of record) — ข้อมูลการชำระเงินของคุณถูกจัดการโดย Creem ไม่ใช่เว็บไซต์นี้",
})

TRUST_OVERRIDES["supportDesc"].update({
    "ko": "Fxverter 지원하기: 무료로 사용할 수 있고 계정도 추적도 없습니다. 후원이 빠르고 무료이며 독립적인 상태를 지켜 줍니다; 결제는 Creem이 처리합니다.",
    "ru": "Поддержите Fxverter: бесплатно — без аккаунта и слежки. Взносы сохраняют его быстрым, бесплатным и независимым; платежи через Creem.",
    "hi": "Fxverter को सहयोग करें: मुफ़्त — न खाता, न ट्रैकिंग। योगदान इसे तेज़, मुफ़्त और स्वतंत्र रखते हैं; भुगतान Creem से।",
    "ar": "ادعم Fxverter: مجاني — بلا حساب ولا تتبّع. المساهمات تبقيه سريعًا ومجانيًا ومستقلًا؛ المدفوعات عبر Creem.",
    "it": "Sostieni Fxverter: gratuito — senza account, senza tracciamento. I contributi lo mantengono veloce, gratuito e indipendente; pagamenti via Creem.",
    "th": "สนับสนุน Fxverter: ใช้ฟรี — ไม่มีบัญชี ไม่มีการติดตาม การสนับสนุนช่วยให้เร็ว ฟรี และเป็นอิสระ; ชำระเงินผ่าน Creem",
})

TRUST_OVERRIDES["privacyNote"].update({
    "ko": "개인정보 보호: 쿠키가 필요 없고 개인 데이터를 수집하지 않습니다. 익명의 쿠키 없는 방문 통계(페이지뷰와 국가)가 수집될 수 있습니다. 이 사이트는 광고를 표시할 수 있습니다 — 자세한 내용은 <a href=\"{base}ko/privacy/\">개인정보 처리방침</a>을 참고하세요.",
    "ru": "Приватность: cookie не требуются, персональные данные не собираются. Могут собираться анонимные статистические данные о посещениях без cookie (просмотры страниц и страна). Сайт может показывать рекламу — см. <a href=\"{base}ru/privacy/\">Политику конфиденциальности</a>.",
    "hi": "प्राइवेसी: कुकी की ज़रूरत नहीं है और न ही कोई व्यक्तिगत डेटा इकट्ठा होता है। बिना कुकी के अनाम विज़िट आँकड़े (पेज व्यू और देश) इकट्ठा हो सकते हैं। यह साइट विज्ञापन दिखा सकती है — विवरण के लिए <a href=\"{base}hi/privacy/\">प्राइवेसी पॉलिसी</a> देखें।",
    "ar": "الخصوصية: لا حاجة إلى ملفات تعريف الارتباط ولا تُجمَع أي بيانات شخصية. قد تُجمَع إحصاءات زيارات مجهولة وخالية من الكوكيز (مشاهدات الصفحات والبلد). قد يعرض الموقع إعلانات — راجع <a href=\"{base}ar/privacy/\">سياسة الخصوصية</a>.",
    "it": "Privacy: nessun cookie richiesto e nessun dato personale raccolto. Possono essere raccolte statistiche di visita anonime e senza cookie (visualizzazioni di pagina e paese). Il sito può mostrare pubblicità — vedi la <a href=\"{base}it/privacy/\">Informativa sulla privacy</a>.",
    "th": "ความเป็นส่วนตัว: ไม่ต้องใช้คุกกี้และไม่เก็บข้อมูลส่วนบุคคล อาจมีการเก็บสถิติการเข้าชมแบบไม่ระบุตัวตนและไม่ใช้คุกกี้ (การเข้าชมหน้าเว็บและประเทศ) เว็บไซต์อาจแสดงโฆษณา — ดู<a href=\"{base}th/privacy/\">นโยบายความเป็นส่วนตัว</a>",
})

TRUST_OVERRIDES["support"].update({
    "ko": {
        "headline": "♥ 콜라 한 캔 사 주기",
        "choose": "한 잔 사 주기",
        "perk": "이것은 기부가 아니라 작은 디지털 감사 선물입니다: 등급을 하나 고르시면 이름(한 줄 메시지 선택 가능)이 아래 지지자 명단에 영구히 올라갑니다 — 원하시면 익명으로도 가능합니다.",
        "tiers": [("콜라 한 캔", "$2", ""), ("6캔 팩", "$9", ""), ("한 상자", "$29", "")],
        "note": "Creem 결제 링크를 준비 중입니다 — 지금 바로 후원하시려면 <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>으로 메일 주세요.",
        "claim": {
            "title": "이미 후원하셨나요? 명단에 등록하세요",
            "name": "표시할 이름",
            "message": "한 줄 메시지(선택)",
            "email": "결제 시 사용한 이메일",
            "anon": "익명으로 표시",
            "send": "내 이름 등록하기",
            "ok": "✓ 등록 완료 — 페이지를 새로 고침하면 보입니다.",
            "fail": "결제를 확인하지 못했습니다 — hello@fxverter.com으로 메일 주세요.",
            "nopaid": "해당 이메일로 결제 기록을 아직 찾지 못했습니다.",
            "needEmail": "결제에 사용한 이메일을 입력해 주세요.",
            "anonLabel": "익명",
        },
    },
    "ru": {
        "headline": "♥ Угостите нас колой",
        "choose": "Выберите угощение",
        "perk": "Это не пожертвование, а небольшое цифровое «спасибо»: выберите уровень — и ваше имя (с необязательной строкой) навсегда появится в списке сторонников ниже — или анонимно, если хотите.",
        "tiers": [("Банка колы", "$2", ""), ("Упаковка из шести банок", "$9", ""), ("Целый ящик", "$29", "")],
        "note": "Платёжные ссылки Creem ещё настраиваются — хотите поддержать прямо сейчас? Напишите на <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Уже поддержали? Займите место в списке",
            "name": "Отображаемое имя",
            "message": "Сообщение в одну строку (необязательно)",
            "email": "Эл. почта, указанная при оплате",
            "anon": "Указать меня анонимно",
            "send": "Заявить о себе",
            "ok": "✓ Вы в списке — обновите страницу, чтобы увидеть.",
            "fail": "Не удалось подтвердить платёж — напишите на hello@fxverter.com.",
            "nopaid": "Платёж по этому адресу пока не найден.",
            "needEmail": "Введите адрес, с которого платили.",
            "anonLabel": "Анонимно",
        },
    },
    "hi": {
        "headline": "♥ हमें एक कोला दिलाएँ",
        "choose": "एक राउंड चुनें",
        "perk": "यह दान नहीं, एक छोटा डिजिटल धन्यवाद है: कोई भी स्तर चुनें — आपका नाम (चाहें तो एक-पंक्ति का संदेश) नीचे समर्थकों की दीवार पर स्थायी रूप से दिखेगा — चाहें तो गुमनाम रूप से।",
        "tiers": [("कोला का एक कैन", "$2", ""), ("छह कैन का पैक", "$9", ""), ("पूरा क्रेट", "$29", "")],
        "note": "Creem चेकआउट लिंक तैयार हो रहे हैं — अभी सहयोग करना चाहें? <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> पर ईमेल करें।",
        "claim": {
            "title": "पहले से सहयोग किया है? अपनी जगह दर्ज करें",
            "name": "प्रदर्शित होने वाला नाम",
            "message": "एक-पंक्ति का संदेश (वैकल्पिक)",
            "email": "चेकआउट पर इस्तेमाल ईमेल",
            "anon": "मुझे गुमनाम रूप से दिखाएँ",
            "send": "मेरी एंट्री दर्ज करें",
            "ok": "✓ आप दीवार पर हैं — देखने के लिए पेज रीफ़्रेश करें।",
            "fail": "भुगतान सत्यापित नहीं हो सका — hello@fxverter.com पर ईमेल करें।",
            "nopaid": "इस ईमेल से मेल खाता भुगतान अभी नहीं मिला।",
            "needEmail": "कृपया वही ईमेल दर्ज करें जिससे भुगतान किया था।",
            "anonLabel": "गुमनाम",
        },
    },
    "ar": {
        "headline": "♥ أكرمنا بعلبة كولا",
        "choose": "اختر ضيافة",
        "perk": "هذه ليست تبرعًا، بل شكر رقمي صغير: اختر إحدى الفئات وسيظهر اسمك (مع سطر رسالة اختياري) في جدار الداعمين أدناه بشكل دائم — أو بشكل مجهول إن فضّلت.",
        "tiers": [("علبة كولا", "$2", ""), ("عبوة من ست علب", "$9", ""), ("صندوق كامل", "$29", "")],
        "note": "روابط الدفع عبر Creem قيد الإعداد — تريد الدعم الآن؟ راسلنا على <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "هل دعمت سابقًا؟ احجز مكانك",
            "name": "الاسم المعروض",
            "message": "رسالة من سطر واحد (اختياري)",
            "email": "البريد الإلكتروني المستخدم عند الدفع",
            "anon": "اعرضني بشكل مجهول",
            "send": "أكّد تسجيلي",
            "ok": "✓ أنت على الجدار — حدّث الصفحة لتراه.",
            "fail": "لم نتمكن من التحقق من الدفع — راسل hello@fxverter.com.",
            "nopaid": "لم نعثر بعد على دفعة مطابقة لهذا البريد.",
            "needEmail": "أدخل البريد الإلكتروني الذي دفعت به.",
            "anonLabel": "مجهول",
        },
    },
    "it": {
        "headline": "♥ Offrici una Coca",
        "choose": "Scegli cosa offrire",
        "perk": "Non è una donazione, ma un piccolo grazie digitale: scegli un livello e il tuo nome (con un facoltativo messaggio di una riga) resta per sempre nella bacheca dei sostenitori qui sotto — oppure in forma anonima, se preferisci.",
        "tiers": [("Una lattina di Coca", "$2", ""), ("Un pack da sei", "$9", ""), ("Una cassa intera", "$29", "")],
        "note": "I link di pagamento Creem sono in preparazione — vuoi sostenere subito? Scrivi a <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Hai già sostenuto? Rivendica il tuo posto",
            "name": "Nome visualizzato",
            "message": "Messaggio di una riga (facoltativo)",
            "email": "Email usata al pagamento",
            "anon": "Elenca come anonimo",
            "send": "Rivendica la mia posizione",
            "ok": "✓ Sei sulla bacheca — aggiorna la pagina per vederlo.",
            "fail": "Impossibile verificare il pagamento — scrivi a hello@fxverter.com.",
            "nopaid": "Nessun pagamento trovato per questa email.",
            "needEmail": "Inserisci l'email con cui hai pagato.",
            "anonLabel": "Anonimo",
        },
    },
    "th": {
        "headline": "♥ ชวนเราดื่มโค้ก",
        "choose": "เลี้ยงสักรอบ",
        "perk": "นี่ไม่ใช่การบริจาค แต่เป็นของขอบคุณดิจิทัลชิ้นเล็ก: เลือกแพ็กเกจแล้วชื่อของคุณ (พร้อมข้อความสั้น ๆ ถ้าต้องการ) จะปรากฏบนกำแพงผู้สนับสนุนด้านล่างแบบถาวร — หรือจะไม่ระบุตัวตนก็ได้",
        "tiers": [("โค้ก 1 กระป๋อง", "$2", ""), ("แพ็ก 6 กระป๋อง", "$9", ""), ("ทั้งลัง", "$29", "")],
        "note": "ลิงก์ชำระเงินผ่าน Creem กำลังจัดเตรียม — อยากสนับสนุนตอนนี้เลย? ส่งอีเมลมาที่ <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>",
        "claim": {
            "title": "สนับสนุนไปแล้ว? อ้างสิทธิ์ชื่อของคุณ",
            "name": "ชื่อที่แสดง",
            "message": "ข้อความสั้น ๆ (ไม่บังคับ)",
            "email": "อีเมลที่ใช้ชำระเงิน",
            "anon": "แสดงเป็นผู้ไม่ประสงค์ออกนาม",
            "send": "ยืนยันรายชื่อของฉัน",
            "ok": "✓ คุณอยู่บนกำแพงแล้ว — รีเฟรชหน้าเพื่อดู",
            "fail": "ยืนยันการชำระเงินไม่สำเร็จ — ส่งอีเมลมาที่ hello@fxverter.com",
            "nopaid": "ยังไม่พบรายการชำระเงินที่ตรงกับอีเมลนี้",
            "needEmail": "กรุณากรอกอีเมลที่ใช้ชำระเงิน",
            "anonLabel": "ไม่ประสงค์ออกนาม",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
# Round-6 promotion: Turkish (tr) joins the indexed languages.
# Same ads-aware support/privacy copy structure as the round-5 block.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"].update({
    "tr": "Fxverter \u00fccretsizdir \u2014 hesap yok, takip yok. Birka\u00e7 kurdun \u00e7evrilmesine yard\u0131mc\u0131 olduysa bize bir kola \u0131smarlay\u0131n: her katk\u0131 alan ad\u0131na, sunuculara ve s\u00fcrekli geli\u015ftirmeye gider. \u00d6demeler, kay\u0131t tutan sat\u0131c\u0131 (merchant of record) olarak Creem \u00fczerinden i\u015flenir \u2014 \u00f6deme verilerinizi bu site de\u011fil, Creem y\u00f6netir.",
})

TRUST_OVERRIDES["supportDesc"].update({
    "tr": "Fxverter\u2019i destekleyin: \u00fccretsiz \u2014 hesap yok, takip yok. Katk\u0131lar onu h\u0131zl\u0131, \u00fccretsiz ve ba\u011f\u0131ms\u0131z tutar; \u00f6demeler Creem \u00fczerinden.",
})

TRUST_OVERRIDES["privacyNote"].update({
    "tr": "Gizlilik: \u00e7erez gerekmez ve ki\u015fisel veri toplanmaz. Anonim, \u00e7erezsiz ziyaret istatistikleri (sayfa g\u00f6r\u00fcnt\u00fcleme ve \u00fclke) toplanabilir. Site reklam g\u00f6sterebilir \u2014 ayr\u0131nt\u0131lar i\u00e7in <a href=\"{base}tr/privacy/\">Gizlilik Politikas\u0131</a> sayfas\u0131na bak\u0131n.",
})

TRUST_OVERRIDES["support"].update({
    "tr": {
        "headline": "\u2665 Bize bir kola \u0131smarlay\u0131n",
        "choose": "Bir tur \u0131smarla",
        "perk": "Bu bir ba\u011f\u0131\u015f de\u011fil, k\u00fc\u00e7\u00fck bir dijital te\u015fekk\u00fcrd\u00fcr: bir paket se\u00e7in; ad\u0131n\u0131z (iste\u011fe ba\u011fl\u0131 tek sat\u0131rl\u0131k mesajla) a\u015fa\u011f\u0131daki destek\u00e7iler listesine kal\u0131c\u0131 olarak eklenir \u2014 isterseniz anonim olarak.",
        "tiers": [("Bir kutu kola", "$2", ""), ("Alt\u0131l\u0131 paket", "$9", ""), ("Koca bir kasa", "$29", "")],
        "note": "Creem \u00f6deme ba\u011flant\u0131lar\u0131 haz\u0131rlan\u0131yor \u2014 hemen destek olmak ister misiniz? <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> adresine yaz\u0131n.",
        "claim": {
            "title": "Zaten destek verdiniz mi? Ad\u0131n\u0131z\u0131 ekleyin",
            "name": "G\u00f6r\u00fcnen ad",
            "message": "Tek sat\u0131rl\u0131k mesaj (iste\u011fe ba\u011fl\u0131)",
            "email": "\u00d6demede kullan\u0131lan e-posta",
            "anon": "Anonim olarak listele",
            "send": "Kayd\u0131m\u0131 ekle",
            "ok": "\u2713 Listedesiniz \u2014 g\u00f6rmek i\u00e7in sayfay\u0131 yenileyin.",
            "fail": "\u00d6deme do\u011frulanamad\u0131 \u2014 hello@fxverter.com adresine yaz\u0131n.",
            "nopaid": "Bu e-postaya ait bir \u00f6deme kayd\u0131 hen\u00fcz bulunamad\u0131.",
            "needEmail": "L\u00fctfen \u00f6demede kulland\u0131\u011f\u0131n\u0131z e-postay\u0131 girin.",
            "anonLabel": "Anonim",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
# Round-6 promotion: Indonesian (id) joins the indexed languages.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"].update({
    "id": "Fxverter gratis digunakan \u2014 tanpa akun, tanpa pelacakan. Jika pernah membantu Anda mengonversi beberapa kurs, traktir kami satu kola: setiap kontribusi digunakan untuk domain, server, dan pengembangan berkelanjutan. Pembayaran diproses oleh Creem selaku merchant of record \u2014 data pembayaran Anda dikelola oleh Creem, bukan oleh situs ini.",
})

TRUST_OVERRIDES["supportDesc"].update({
    "id": "Dukung Fxverter: gratis \u2014 tanpa akun, tanpa pelacakan. Kontribusi menjaganya tetap cepat, gratis, dan independen; pembayaran melalui Creem.",
})

TRUST_OVERRIDES["privacyNote"].update({
    "id": "Privasi: tidak perlu kuki dan tidak ada data pribadi yang dikumpulkan. Statistik kunjungan anonim tanpa kuki (tampilan halaman dan negara) dapat dikumpulkan. Situs ini dapat menampilkan iklan \u2014 lihat <a href=\"{base}id/privacy/\">Kebijakan Privasi</a>.",
})

TRUST_OVERRIDES["support"].update({
    "id": {
        "headline": "\u2665 Traktir kami satu kola",
        "choose": "Traktir satu ronde",
        "perk": "Ini bukan donasi, melainkan ucapan terima kasih digital kecil: pilih salah satu paket, dan nama Anda (dengan pesan satu baris opsional) tercantum permanen di dinding pendukung di bawah \u2014 atau anonim, jika Anda mau.",
        "tiers": [("Satu kaleng kola", "$2", ""), ("Paket enam kaleng", "$9", ""), ("Sekardus penuh", "$29", "")],
        "note": "Tautan pembayaran Creem sedang disiapkan \u2014 ingin mendukung sekarang? Kirim surel ke <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Sudah mendukung? Klaim tempat Anda",
            "name": "Nama yang ditampilkan",
            "message": "Pesan satu baris (opsional)",
            "email": "Email yang dipakai saat membayar",
            "anon": "Cantumkan saya secara anonim",
            "send": "Klaim daftar saya",
            "ok": "\u2713 Anda ada di dinding \u2014 muat ulang halaman untuk melihatnya.",
            "fail": "Tidak dapat memverifikasi pembayaran \u2014 surel ke hello@fxverter.com.",
            "nopaid": "Belum ada pembayaran yang cocok untuk email ini.",
            "needEmail": "Masukkan email yang Anda pakai untuk membayar.",
            "anonLabel": "Anonim",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
# Round-6 promotion: Malay (ms), Filipino (tl), Dutch (nl) join the
# indexed languages.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"].update({
    "ms": "Fxverter percuma digunakan \u2014 tiada akaun, tiada penjejakan. Jika ia pernah membantu anda menukar beberapa kadar, belanja kami secawan kola: setiap sumbangan digunakan untuk domain, pelayan dan pembangunan berterusan. Pembayaran diproses oleh Creem selaku peniaga rekod (merchant of record) \u2014 data pembayaran anda dikendalikan oleh Creem, bukan oleh tapak web ini.",
    "tl": "Libreng gamitin ang Fxverter \u2014 walang account, walang tracking. Kung nakatulong ito sa ilang conversion mo, bumili kami ng isang Coke: ang bawat kontribusyon ay pambayad sa domain, server at tuloy-tuloy na development. Ang mga bayad ay ipoproseso ng Creem bilang merchant of record \u2014 ang payment data mo ay hina-handle ng Creem, hindi ng website na ito.",
    "nl": "Fxverter is gratis te gebruiken \u2014 geen account, geen tracking. Als het je aan een paar koersen heeft geholpen, trakteer ons op een cola: elke bijdrage gaat naar domein, servers en verdere ontwikkeling. Betalingen worden verwerkt door Creem als merchant of record \u2014 je betaalgegevens worden door Creem behandeld, niet door deze website.",
})

TRUST_OVERRIDES["supportDesc"].update({
    "ms": "Sokong Fxverter: percuma \u2014 tiada akaun, tiada penjejakan. Sumbangan mengekalkannya pantas, percuma dan bebas; pembayaran melalui Creem.",
    "tl": "Suportahan ang Fxverter: libre \u2014 walang account, walang tracking. Pinapanatili ng mga kontribusyon itong mabilis, libre at independyente; bayad via Creem.",
    "nl": "Steun Fxverter: gratis \u2014 geen account, geen tracking. Bijdragen houden het snel, gratis en onafhankelijk; betalingen via Creem.",
})

TRUST_OVERRIDES["privacyNote"].update({
    "ms": "Privasi: tiada kuki diperlukan dan tiada data peribadi dikumpul. Statistik lawatan tanpa nama dan tanpa kuki (paparan halaman dan negara) mungkin dikumpul. Tapak web ini mungkin memaparkan iklan \u2014 lihat <a href=\"{base}ms/privacy/\">Dasar Privasi</a>.",
    "tl": "Privacy: walang kinakailangang cookie at walang personal na data na kinokolekta. Maaaring mangolekta ng anonymous, cookie-free na istatistika ng pagbisita (page views at bansa). Maaaring magpakita ng advertising ang site \u2014 tingnan ang <a href=\"{base}tl/privacy/\">Privacy Policy</a>.",
    "nl": "Privacy: geen cookies nodig en er worden geen persoonlijke gegevens verzameld. Anonieme, cookievrije bezoekstatistieken (paginaweergaven en land) kunnen worden verzameld. De website kan advertenties tonen \u2014 zie het <a href=\"{base}nl/privacy/\">Privacybeleid</a>.",
})

TRUST_OVERRIDES["support"].update({
    "ms": {
        "headline": "\u2665 Belanja kami secawan kola",
        "choose": "Belanja satu pusingan",
        "perk": "Ini bukan derma \u2014 ia ucapan terima kasih digital yang kecil: pilih satu pakej, dan nama anda (dengan mesej satu baris pilihan) tersenarai secara kekal di dinding penyokong di bawah \u2014 atau secara tanpa nama, jika anda mahu.",
        "tiers": [("Secawan kola", "$2", ""), ("Pakej enam tin", "$9", ""), ("Sepeti penuh", "$29", "")],
        "note": "Pautan pembayaran Creem sedang disediakan \u2014 mahu menyokong sekarang? E-mel ke <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Sudah menyokong? Tuntut tempat anda",
            "name": "Nama paparan",
            "message": "Mesej satu baris (pilihan)",
            "email": "E-mel yang digunakan semasa bayar",
            "anon": "Senaraikan saya secara tanpa nama",
            "send": "Tuntut senarai saya",
            "ok": "\u2713 Anda sudah di dinding \u2014 muat semula untuk melihatnya.",
            "fail": "Tidak dapat mengesahkan pembayaran \u2014 e-mel ke hello@fxverter.com.",
            "nopaid": "Belum ada pembayaran yang sepadan untuk e-mel ini.",
            "needEmail": "Masukkan e-mel yang anda gunakan untuk membayar.",
            "anonLabel": "Tanpa nama",
        },
    },
    "tl": {
        "headline": "\u2665 Bumili kayo ng Coke",
        "choose": "Pumili ng isang round",
        "perk": "Hindi ito donation \u2014 maliit na digital na pasasalamat ito: pumili ng tier, at ang pangalan mo (na may opsyonal na one-line message) ay permanente nang nakalista sa supporters wall sa ibaba \u2014 o anonymous, kung gusto mo.",
        "tiers": [("Isang lata ng Coke", "$2", ""), ("Six-pack", "$9", ""), ("Buong crate", "$29", "")],
        "note": "Inaayos pa ang mga Creem checkout link \u2014 gusto mo nang suportahan ngayon? Mag-email sa <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Nakadeposit na? I-claim ang slot mo",
            "name": "Display name",
            "message": "One-line message (opsyonal)",
            "email": "Email na ginamit sa checkout",
            "anon": "Ilagay ako bilang anonymous",
            "send": "I-claim ang listing ko",
            "ok": "\u2713 Nasa wall ka na \u2014 i-refresh para makita.",
            "fail": "Hindi ma-verify ang bayad \u2014 mag-email sa hello@fxverter.com.",
            "nopaid": "Wala pang tumugmang bayad para sa email na ito.",
            "needEmail": "Ilagay ang email na ginamit mo sa pagbabayad.",
            "anonLabel": "Anonymous",
        },
    },
    "nl": {
        "headline": "\u2665 Trakteer ons op een cola",
        "choose": "Trakteer een ronde",
        "perk": "Dit is geen donatie, maar een klein digitaal dankje: kies een pakket en je naam (met een optionele regel) staat permanent op de supporterswand hieronder \u2014 of anoniem, als je wilt.",
        "tiers": [("Een blikje cola", "$2", ""), ("Een sixpack", "$9", ""), ("Een hele krat", "$29", "")],
        "note": "De Creem-betaallinks worden ingesteld \u2014 wil je nu steunen? Mail naar <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Al gesteund? Claim je plekje",
            "name": "Weergavenaam",
            "message": "E\u00e9n regel bericht (optioneel)",
            "email": "E-mail gebruikt bij de betaling",
            "anon": "Vermeld me anoniem",
            "send": "Mijn vermelding claimen",
            "ok": "\u2713 Je staat op de wand \u2014 verversen om te zien.",
            "fail": "Kon de betaling niet verifi\u00ebren \u2014 mail naar hello@fxverter.com.",
            "nopaid": "Nog geen betaling gevonden voor deze e-mail.",
            "needEmail": "Vul de e-mail in waarmee je betaald hebt.",
            "anonLabel": "Anoniem",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
# Round-6 promotion: Polish (pl), Ukrainian (uk), Swedish (sv) join the
# indexed languages.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"].update({
    "pl": "Fxverter jest darmowy — bez konta i bez \u015bledzenia. Je\u015fli pom\u00f3g\u0142 ci przewalutowa\u0107 kilka kwot, postaw nam kaw\u0119... a w\u0142a\u015bciwie col\u0119: ka\u017cda wp\u0142ata idzie na domen\u0119, serwery i dalszy rozw\u00f3j. P\u0142atno\u015bci obs\u0142uguje Creem jako merchant of record \u2014 twoje dane p\u0142atnicze przetwarza Creem, nie ta strona.",
    "uk": "Fxverter безкоштовний — без акаунтів і стеження. Якщо він допоміг вам конвертувати кілька курсів, пригоствуйте нас колою: кожен внесок іде на домен, сервери та подальший розвиток. Платежі обробляє Creem як merchant of record — ваші платіжні дані обробляє Creem, а не цей сайт.",
    "sv": "Fxverter \u00e4r gratis att anv\u00e4nda \u2014 inget konto, ingen sp\u00e5rning. Om den hj\u00e4lpt dig v\u00e4xla ett par kurs erbjuder du oss g\u00e4rna en cola: varje bidrag g\u00e5r till dom\u00e4nen, servrarna och fortsatt utveckling. Betalningar hanteras av Creem som merchant of record \u2014 dina betaluppgifter hanteras av Creem, inte av denna webbplats.",
})

TRUST_OVERRIDES["supportDesc"].update({
    "pl": "Wesprzyj Fxverter: bezp\u0142atny — bez konta i bez \u015bledzenia. Wp\u0142aty utrzymuj\u0105 go szybkim, darmowym i niezale\u017cnym; p\u0142atno\u015bci przez Creem.",
    "uk": "Підтримайте Fxverter: безкоштовно — без акаунта і стеження. Внески тримають його швидким, безкоштовним і незалежним; платежі через Creem.",
    "sv": "St\u00f6d Fxverter: gratis \u2014 inget konto, ingen sp\u00e5rning. Bidragen h\u00e5ller den snabb, gratis och oberoende; betalningar via Creem.",
})

TRUST_OVERRIDES["privacyNote"].update({
    "pl": "Prywatno\u015b\u0107: nie s\u0105 wymagane ciasteczka i nie zbieramy danych osobowych. Anonimowe statystyki odwiedzin bez ciasteczek (wy\u015bwietlenia stron i kraj) mog\u0105 by\u0107 zbierane. Strona mo\u017ce wy\u015bwietla\u0107 reklamy — zobacz <a href=\"{base}pl/privacy/\">Polityk\u0119 prywatno\u015bci</a>.",
    "uk": "Приватність: cookie не потрібні, персональні дані не збираються. Можуть збиратися анонімні статистичні дані про відвідування без cookie (перегляди сторінок і країна). Сайт може показувати рекламу — див. <a href=\"{base}uk/privacy/\">Політику конфіденційності</a>.",
    "sv": "Integritet: inga cookies kr\u00e4vs och inga personuppgifter samlas in. Anonym, cookiefri bes\u00f6ksstatistik (sidvisningar och land) kan samlas in. Webbplatsen kan visa reklam \u2014 se <a href=\"{base}sv/privacy/\">integritetspolicyn</a>.",
})

TRUST_OVERRIDES["support"].update({
    "pl": {
        "headline": "\u2665 Postaw nas col\u0119",
        "choose": "Postaw kolejk\u0119",
        "perk": "To nie darowizna, a ma\u0142e cyfrowe podzi\u0119kowanie: wybierz pakiet, a twoje imi\u0119 (z opcjonaln\u0105 jednolinijkow\u0105 wiadomo\u015bci\u0105) trafi na sta\u0142e na list\u0119 wspieraj\u0105cych poni\u017cej — lub anonimowo, je\u015bli wolisz.",
        "tiers": [("Puszka coli", "$2", ""), ("Sześciopak", "$9", ""), ("Ca\u0142a skrzynka", "$29", "")],
        "note": "Linki p\u0142atno\u015bci Creem s\u0105 w przygotowaniu — chcesz wesprze\u0107 ju\u017c teraz? Napisz na <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Ju\u017c wspierasz? Zarezerwuj swoje miejsce",
            "name": "Nazwa wy\u015bwietlana",
            "message": "Jednolinijkowa wiadomo\u015b\u0107 (opcjonalnie)",
            "email": "E-mail u\u017cyty przy p\u0142atno\u015bci",
            "anon": "Wymie\u0144 mnie anonimowo",
            "send": "Zg\u0142o\u015b sw\u00f3j wpis",
            "ok": "\u2713 Jeste\u015b na li\u015bcie — od\u015bwie\u017c, aby zobaczy\u0107.",
            "fail": "Nie uda\u0142o si\u0119 potwierdzi\u0107 p\u0142atno\u015bci — napisz na hello@fxverter.com.",
            "nopaid": "Nie znaleziono jeszcze p\u0142atno\u015bci dla tego e-maila.",
            "needEmail": "Podaj e-mail, kt\u00f3rym p\u0142aci\u0142e\u015b.",
            "anonLabel": "Anonimowo",
        },
    },
    "uk": {
        "headline": "\u2665 Пригоствуйте нас колою",
        "choose": "Пригоствуйте за рахунок",
        "perk": "Це не пожертва, а невелика цифрова подяка: оберіть рівень — і ваше ім'я (з необов'язковим рядком) назавжди з'явиться у списку прихильників нижче — або анонімно, якщо хочете.",
        "tiers": [("Банка коли", "$2", ""), ("Упаковка з шести", "$9", ""), ("Цілий ящик", "$29", "")],
        "note": "Платіжні посилання Creem ще налаштовуються — хочете підтримати прямо зараз? Напишіть на <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Вже підтримали? Займіть місце у списку",
            "name": "Ім'я для показу",
            "message": "Повідомлення в один рядок (необов'язково)",
            "email": "Ел. пошта, вказана при оплаті",
            "anon": "Вказати мене анонімно",
            "send": "Заявити про себе",
            "ok": "\u2713 Ви у списку — оновіть сторінку, щоб побачити.",
            "fail": "Не вдалося підтвердити платіж — напишіть на hello@fxverter.com.",
            "nopaid": "Платежу за цією адресою поки не знайдено.",
            "needEmail": "Введіть адресу, з якої платили.",
            "anonLabel": "Анонімно",
        },
    },
    "sv": {
        "headline": "\u2665 Bjud oss p\u00e5 en cola",
        "choose": "Bjud en runda",
        "perk": "Detta \u00e4r inte en donation, utan ett litet digitalt tack: v\u00e4lj ett paket och ditt namn (med ett valfritt meddelande p\u00e5 en rad) listas permanent p\u00e5 supporterv\u00e4ggen nedan \u2014 eller anonymt, om du f\u00f6redrar.",
        "tiers": [("En burk cola", "$2", ""), ("En sexpack", "$9", ""), ("En hel l\u00e5da", "$29", "")],
        "note": "Creems betall\u00e4nkar f\u00f6rbereds \u2014 vill du st\u00f6dja redan nu? Maila till <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Redan st\u00f6tt? Ans\u00f6k om din plats",
            "name": "Visningsnamn",
            "message": "Meddelande p\u00e5 en rad (valfritt)",
            "email": "E-post anv\u00e4nd vid betalning",
            "anon": "Lista mig anonymt",
            "send": "Ans\u00f6k om min notering",
            "ok": "\u2713 Du \u00e4r p\u00e5 v\u00e4ggen \u2014 uppdatera sidan f\u00f6r att se.",
            "fail": "Kunde inte verifiera betalningen \u2014 maila hello@fxverter.com.",
            "nopaid": "Ingen matchande betalning hittad f\u00f6r denna e-post \u00e4nnu.",
            "needEmail": "Ange e-posten du betalade med.",
            "anonLabel": "Anonymt",
        },
    },
})


# ═══════════════════════════════════════════════════════════════
# Round-6 finale: Lao (lo), Vietnamese (vi), Bengali (bn), Persian (fa),
# Czech (cs), Romanian (ro), Danish (da) join the indexed languages —
# all 29 interface languages are now fully promoted.
# ═══════════════════════════════════════════════════════════════

TRUST_OVERRIDES["supportIntro"].update({
    "lo": "Fxverter ໃຊ້ຟຣີ — ບໍ່ມີບັນຊີ, ບໍ່ມີການຕິດຕາມ. ຖ້າມັນຊ່ວຍທ່ານແປງອັດຕາໄດ້ບໍ່ດົນ, ຊື້ໂຄລາໃຫ້ພວກເຮົາແທ່ງໜຶ່ງ: ທຸກການສະໜັບສະໜູນໄປສູ່ຊື່ໂດເມນ, ເຊີບເວີ ແລະ ການພັດທະນາຕໍ່ເນື່ອງ. ການຈ່າຍເງິນດຳເນີນໂດຍ Creem ໃນຖານະຜູ້ຂາຍບັນທຶກ (merchant of record) — ຂໍ້ມູນການຈ່າຍເງິນຂອງທ່ານ Creem ເປັນຜູ້ຄຸ້ມຄອງ, ບໍ່ແມ່ນເວັບໄຊນີ້.",
    "vi": "Fxverter miễn phí sử dụng — không tài khoản, không theo dõi. Nếu nó từng giúp bạn quy đổi vài tỷ giá, mời chúng tôi một lon Coca: mỗi đóng góp dành cho tên miền, máy chủ và phát triển liên tục. Thanh toán do Creem xử lý với tư cách merchant of record — dữ liệu thanh toán của bạn do Creem quản lý, không phải website này.",
    "bn": "Fxverter ব্যবহার করা ফ্রি — কোনো অ্যাকাউন্ট নেই, ট্র্যাকিং নেই। কয়েকটি হার রূপান্তরে সাহায্য করলে আমাদের একটি কোকা কিনে দিন: প্রতিটি অবদান যায় ডোমেইন, সার্ভার ও চলমান উন্নয়নে। পেমেন্ট প্রসেস করে Creem, merchant of record হিসেবে — আপনার পেমেন্ট ডেটা এই ওয়েবসাইট নয়, Creem সামলায়।",
    "fa": "استفاده از Fxverter رایگان است — بدون حساب، بدون ردیابی. اگر در تبدیل چند نرخ کمکتان کرده، یک نوشابه مهمان ما کنید: هر کمک به دامنه، سرورها و توسعه مستمر می‌رود. پرداخت‌ها توسط Creem به‌عنوان merchant of record انجام می‌شود — داده‌های پرداخت شما را Creem مدیریت می‌کند، نه این وب‌سایت.",
    "cs": "Fxverter je zdarma — bez \u00fa\u010dtu a bez sledov\u00e1n\u00ed. Pokud v\u00e1m pomohl p\u0159ev\u00e9st p\u00e1r kurz\u016f, dop\u0159ejte n\u00e1m colu: ka\u017ed\u00fd p\u0159\u00edsp\u011bvek jde na dom\u00e9nu, servery a dal\u0161\u00ed rozvoj. Platby zpracov\u00e1v\u00e1 Creem jako merchant of record \u2014 va\u0161e platebn\u00ed \u00fadaje zpracov\u00e1v\u00e1 Creem, nikoli tato str\u00e1nka.",
    "ro": "Fxverter este gratuit de folosit — f\u0103r\u0103 cont, f\u0103r\u0103 urm\u0103rire. Dac\u0103 te-a ajutat s\u0103 converte\u015fti c\u00e2teva cursuri, trateaz\u0103-ne la o cola: fiecare contribuție merge pe domeniu, servere și dezvoltare continu\u0103. Pl\u0103țile sunt procesate de Creem ca merchant of record \u2014 datele tale de plat\u0103 sunt gestionate de Creem, nu de acest site.",
    "da": "Fxverter er gratis at bruge \u2014 ingen konto, ingen sporing. Hvis den har hjulpet dig med at omregne et par kurser, giver du os gerne en cola: hver bidrag g\u00e5r til dom\u00e6net, serverne og fortsat udvikling. Betalinger h\u00e5ndteres af Creem som merchant of record \u2014 dine betalingsdata h\u00e5ndteres af Creem, ikke af dette website.",
})

TRUST_OVERRIDES["supportDesc"].update({
    "lo": "ສະໜັບສະໜູນ Fxverter: ຟຣີ — ບໍ່ມີບັນຊີ, ບໍ່ມີການຕິດຕາມ. ການສະໜັບສະໜູນຊ່ວຍໃຫ້ມັນໄວ, ຟຣີ ແລະ ເປັນເອກະລາດ; ຈ່າຍຜ່ານ Creem.",
    "vi": "Ủng hộ Fxverter: miễn phí — không tài khoản, không theo dõi. Đóng góp giữ nó nhanh, miễn phí và độc lập; thanh toán qua Creem.",
    "bn": "Fxverter-কে সমর্থন করুন: ফ্রি — অ্যাকাউন্ট নেই, ট্র্যাকিং নেই। অবদান একে দ্রুত, ফ্রি ও স্বাধীন রাখে; পেমেন্ট Creem-এর মাধ্যমে।",
    "fa": "از Fxverter حمایت کنید: رایگان — بدون حساب، بدون ردیابی. کمک‌ها آن را سریع، رایگان و مستقل نگه می‌دارند؛ پرداخت از طریق Creem.",
    "cs": "Podpo\u0159te Fxverter: zdarma — bez \u00fa\u010dtu, bez sledov\u00e1n\u00ed. P\u0159\u00edsp\u011bvky ho udr\u017euj\u00ed rychl\u00fd, bezplatn\u00fd a nez\u00e1visl\u00fd; platby p\u0159es Creem.",
    "ro": "Susține Fxverter: gratuit — f\u0103r\u0103 cont, f\u0103r\u0103 urm\u0103rire. Contribuțiile îl mențin rapid, gratuit și independent; plăți via Creem.",
    "da": "St\u00f8t Fxverter: gratis \u2014 ingen konto, ingen sporing. Bidrag holder den hurtig, gratis og uafh\u00e6ngig; betalinger via Creem.",
})

TRUST_OVERRIDES["privacyNote"].update({
    "lo": "ຄວາມເປັນສ່ວນຕົວ: ບໍ່ຕ້ອງການ cookie ແລະ ບໍ່ເກັບກຳຂໍ້ມູນສ່ວນບຸກຄົນ. ສະຖິຕິການເຂົ້າຊົມແບບນິລະນາມ ບໍ່ມີ cookie (ການເບິ່ງໜ້າ ແລະ ປະເທດ) ອາດຖືກເກັບກຳ. ເວັບໄຊນີ້ອາດສະແດງໂຄສະນາ — ເບິ່ງ <a href=\"{base}lo/privacy/\">ນະໂຍບາຍຄວາມເປັນສ່ວນຕົວ</a>.",
    "vi": "Quyền riêng tư: không cần cookie và không thu thập dữ liệu cá nhân. Số liệu truy cập ẩn danh không cookie (lượt xem trang và quốc gia) có thể được thu thập. Trang web có thể hiển thị quảng cáo — xem <a href=\"{base}vi/privacy/\">Chính sách quyền riêng tư</a>.",
    "bn": "গোপনীয়তা: কুকির প্রয়োজন নেই এবং কোনো ব্যক্তিগত ডেটা সংগ্রহ করা হয় না। নাম-গোপন, কুকি-মুক্ত ভিজিট পরিসংখ্যান (পেজ ভিউ ও দেশ) সংগ্রহ হতে পারে। সাইটটি বিজ্ঞাপন দেখাতে পারে — দেখুন <a href=\"{base}bn/privacy/\">গোপনীয়তা নীতি</a>।",
    "fa": "حریم خصوصی: نیازی به کوکی نیست و هیچ داده شخصی جمع‌آوری نمی‌شود. آمار بازدید ناشناس و بدون کوکی (بازدید صفحه و کشور) ممکن است جمع‌آوری شود. این سایت ممکن است تبلیغ نمایش دهد — ببینید <a href=\"{base}fa/privacy/\">سیاست حریم خصوصی</a>.",
    "cs": "Soukrom\u00ed: cookies nejsou vy\u017eadov\u00e1ny a osobn\u00ed \u00fadaje se nesb\u00edraj\u00ed. Anonymn\u00ed statistiky n\u00e1v\u0161t\u011bv bez cookies (zobrazen\u00ed str\u00e1nek a zem\u011b) mohou b\u00fdt shroma\u017e\u010fov\u00e1ny. Str\u00e1nka m\u016f\u017ee zobrazovat reklamy — viz <a href=\"{base}cs/privacy/\">Z\u00e1sady ochrany osobn\u00edch \u00fadaj\u016f</a>.",
    "ro": "Confidențialitate: nu sunt necesare cookie-uri și nu se colectează date personale. Statistici anonime de vizitare, fără cookie-uri (vizualizări de pagini și țară) pot fi colectate. Site-ul poate afișa reclame — vezi <a href=\"{base}ro/privacy/\">Politica de confidențialitate</a>.",
    "da": "Privatliv: ingen cookies er n\u00f8dvendige og ingen persondata indsamles. Anonym, cookiefri bes\u00f8gsstatistik (sidevisninger og land) kan indsamles. Webstedet kan vise reklamer — se <a href=\"{base}da/privacy/\">privatlivspolitikken</a>.",
})

TRUST_OVERRIDES["support"].update({
    "lo": {
        "headline": "\u2665 ຊື້ໂຄລາໃຫ້ພວກເຮົາ",
        "choose": "ຊື້ໜຶ່ງຮອບ",
        "perk": "ນີ້ບໍ່ແມ່ນການບິຈາກ, ແຕ່ເປັນຄຳຂອບໃຈດິຈິຕອລນ້ອຍໆ: ເລືອກແພັກເກັດໜຶ່ງ ແລະ ຊື່ຂອງທ່ານ (ພ້ອມຂໍ້ຄວາມໜຶ່ງແຖວ ຖ້າຕ້ອງການ) ຈະປາກົດຖາວອນໃນກຳແພງຜູ້ສະໜັບສະໜູນຂ້າງລຸ່ມ — ຫຼື ແບບນິລະນາມ ຖ້າທ່ານຕ້ອງການ.",
        "tiers": [("ໂຄລາໜຶ່ງກະປ໋ອງ", "$2", ""), ("ແພັກ 6 ກະປ໋ອງ", "$9", ""), ("ໃສ່ເຕັມແກັດ", "$29", "")],
        "note": "ລິ້ງການຊຳລະເງິນ Creem ກຳລັງຕັ້ງຄ່າ — ຢາກສະໜັບສະໜູນດຽວນີ້? ຂຽນເມລ໌ໄປທີ່ <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "ສະໜັບສະໜູນແລ້ວ? ຢືນຢັນບ່ອນຂອງທ່ານ",
            "name": "ຊື່ສະແດງ",
            "message": "ຂໍ້ຄວາມໜຶ່ງແຖວ (ເລືອກໄດ້)",
            "email": "ອີເມວທີ່ໃຊ້ຕອນຈ່າຍ",
            "anon": "ລະບຸຂ້ອຍແບບນິລະນາມ",
            "send": "ຢືນຢັນລາຍຊື່ຂອງຂ້ອຍ",
            "ok": "\u2713 ທ່ານຢູ່ໃນກຳແພງແລ້ວ — ຣີເຟຣຊເພື່ອເບິ່ງ.",
            "fail": "ຢືນຢັນການຈ່າຍເງິນບໍ່ສຳເລັດ — ຂຽນເມລ໌ hello@fxverter.com.",
            "nopaid": "ຍັງບໍ່ພົບການຈ່າຍເງິນທີ່ກົງກັບອີເມວນີ້.",
            "needEmail": "ກະລຸນາໃສ່ອີເມວທີ່ທ່ານໃຊ້ຈ່າຍ.",
            "anonLabel": "ນິລະນາມ",
        },
    },
    "vi": {
        "headline": "\u2665 Mời chúng tôi một lon Coca",
        "choose": "Mời một vòng",
        "perk": "Đây không phải quyên góp, mà là lời cảm ơn số nhỏ: chọn một gói, tên bạn (kèm lời nhắn một dòng tùy chọn) sẽ được liệt kê vĩnh viễn trên tường người ủng hộ bên dưới — hoặc ẩn danh, nếu bạn muốn.",
        "tiers": [("Một lon Coca", "$2", ""), ("Lốc sáu lon", "$9", ""), ("Cả thùng", "$29", "")],
        "note": "Liên kết thanh toán Creem đang được thiết lập — muốn ủng hộ ngay? Gửi thư tới <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Đã ủng hộ? Nhận chỗ của bạn",
            "name": "Tên hiển thị",
            "message": "Lời nhắn một dòng (tùy chọn)",
            "email": "Email dùng khi thanh toán",
            "anon": "Liệt kê tôi ẩn danh",
            "send": "Nhận mục của tôi",
            "ok": "\u2713 Bạn đã có mặt trên tường — tải lại trang để xem.",
            "fail": "Không thể xác minh thanh toán — gửi thư tới hello@fxverter.com.",
            "nopaid": "Chưa tìm thấy thanh toán khớp với email này.",
            "needEmail": "Nhập email bạn đã dùng để thanh toán.",
            "anonLabel": "Ẩn danh",
        },
    },
    "bn": {
        "headline": "\u2665 আমাদের একটি কোকা কিনে দিন",
        "choose": "এক রাউন্ড কিনুন",
        "perk": "এটি দান নয়, ছোট এক ডিজিটাল ধন্যবাদ: একটি প্যাক বেছে নিন, আপনার নাম (ঐচ্ছিক এক-লাইনের বার্তাসহ) নিচের সমর্থকদের প্রাচীরে স্থায়ীভাবে তালিকাভুক্ত হবে — চাইলে নাম-গোপনেও।",
        "tiers": [("এক ক্যান কোকা", "$2", ""), ("ছয় ক্যানের প্যাক", "$9", ""), ("পুরো ক্রেট", "$29", "")],
        "note": "Creem চেকআউট লিংক প্রস্তুত হচ্ছে — এখনই সমর্থন করতে চান? ইমেল করুন <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "ইতিমধ্যে সমর্থন করেছেন? আপনার জায়গা দাবি করুন",
            "name": "প্রদর্শিত নাম",
            "message": "এক-লাইনের বার্তা (ঐচ্ছিক)",
            "email": "পেমেন্টে ব্যবহৃত ইমেল",
            "anon": "আমাকে নাম-গোপনে তালিকাভুক্ত করুন",
            "send": "আমার এন্ট্রি দাবি করুন",
            "ok": "\u2713 আপনি প্রাচীরে আছেন — দেখতে রিফ্রেশ করুন।",
            "fail": "পেমেন্ট যাচাই করা গেল না — ইমেল করুন hello@fxverter.com.",
            "nopaid": "এই ইমেলের জন্য এখনো কোনো মিলে যাওয়া পেমেন্ট পাওয়া যায়নি।",
            "needEmail": "যে ইমেল দিয়ে পেমেন্ট করেছেন তা দিন।",
            "anonLabel": "নাম-গোপন",
        },
    },
    "fa": {
        "headline": "\u2665 برایمان نوشابه مهمان کنید",
        "choose": "یک دور مهمان کنید",
        "perk": "این کمک مالی نیست، بلکه تشکر دیجیتال کوچکی است: یک بسته را انتخاب کنید و نام شما (با یک پیام یک‌خطی اختیاری) برای همیشه در دیوار حامیان زیر فهرست می‌شود — یا ناشناس، اگر ترجیح می‌دهید.",
        "tiers": [("یک قوطی نوشابه", "$2", ""), ("بسته شش‌تایی", "$9", ""), ("یک جعبه کامل", "$29", "")],
        "note": "لینک‌های پرداخت Creem در حال راه‌اندازی است — می‌خواهید همین حالا حمایت کنید؟ به <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> ایمیل بزنید.",
        "claim": {
            "title": "قبلاً حمایت کرده‌اید؟ جای خود را ثبت کنید",
            "name": "نام نمایشی",
            "message": "پیام یک‌خطی (اختیاری)",
            "email": "ایمیل استفاده‌شده در پرداخت",
            "anon": "مرا ناشناس فهرست کن",
            "send": "ثبت فهرست من",
            "ok": "\u2713 شما روی دیوار هستید — برای دیدن، صفحه را تازه‌سازی کنید.",
            "fail": "تأیید پرداخت ممکن نشد — به hello@fxverter.com ایمیل بزنید.",
            "nopaid": "هنوز پرداخت منطبقی برای این ایمیل پیدا نشده.",
            "needEmail": "ایمیلی را که با آن پرداخت کرده‌اید وارد کنید.",
            "anonLabel": "ناشناس",
        },
    },
    "cs": {
        "headline": "\u2665 Dopřejte nám colu",
        "choose": "Zapla\u0165te kolo",
        "perk": "Toto nen\u00ed dar, ale mal\u00e9 digit\u00e1ln\u00ed pod\u011bkov\u00e1n\u00ed: vyberte bal\u00ed\u010dek a va\u0161e jm\u00e9no (s voliteln\u00fdm jedn\u00e1\u0159\u00e1dkov\u00fdm vzkazem) se trvale objev\u00ed na zdi podporovatel\u016f n\u00ed\u017ee — nebo anonymn\u011b, chcete-li.",
        "tiers": [("Plechovka coly", "$2", ""), ("\u0160estipack", "$9", ""), ("Cel\u00e1 bedna", "$29", "")],
        "note": "Platebn\u00ed odkazy Creem se p\u0159ipravuj\u00ed — chcete podpo\u015fit hned? Napi\u0161te na <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "U\u017e podporujete? Rezervujte si sv\u00e9 m\u00edsto",
            "name": "Zobrazovan\u00e9 jm\u00e9no",
            "message": "Jedno\u0159\u00e1dkov\u00fd vzkaz (voliteln\u00e9)",
            "email": "E-mail pou\u017eit\u00fd p\u0159i platb\u011b",
            "anon": "Uve\u010ft m\u011b anonymn\u011b",
            "send": "Rezervovat sv\u016fj z\u00e1pis",
            "ok": "\u2713 Jsme na zdi \u2014 obnovte str\u00e1nku, abyste to vid\u011bli.",
            "fail": "Platbu se nepoda\u0159ilo ov\u011b\u0159it \u2014 napi\u0161te na hello@fxverter.com.",
            "nopaid": "Pro tento e-mail zat\u00edm nebyla nalezena \u017e\u00e1dn\u00e1 platba.",
            "needEmail": "Zadejte e-mail, kter\u00fdm jste platili.",
            "anonLabel": "Anonymn\u011b",
        },
    },
    "ro": {
        "headline": "\u2665 Tratează-ne la o cola",
        "choose": "Tratează o rundă",
        "perk": "Nu este o donație, ci un mic mulțumire digitală: alege un pachet, iar numele tău (cu un mesaj opțional de un rând) apare permanent pe peretele susținătorilor de mai jos — sau anonim, dacă preferi.",
        "tiers": [("O cutie de cola", "$2", ""), ("Un pachet de șase", "$9", ""), ("O ladă întreagă", "$29", "")],
        "note": "Linkurile de plată Creem sunt în pregătire — vrei să sprijini acum? Scrie la <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Ai susținut deja? Revendică-ți locul",
            "name": "Numele afișat",
            "message": "Mesaj de un rând (opțional)",
            "email": "Emailul folosit la plată",
            "anon": "Listează-mă anonim",
            "send": "Revendică intrarea mea",
            "ok": "\u2713 Ești pe perete — reîmprospătează pentru a vedea.",
            "fail": "Nu am putut verifica plata — scrie la hello@fxverter.com.",
            "nopaid": "Încă nu a fost găsită o plată potrivită pentru acest email.",
            "needEmail": "Introdu emailul cu care ai plătit.",
            "anonLabel": "Anonim",
        },
    },
    "da": {
        "headline": "\u2665 Giv os en cola",
        "choose": "Giv en runde",
        "perk": "Dette er ikke en donation, men et lille digitalt tak: v\u00e6lg en pakke, og dit navn (med en valgfri besked p\u00e5 \u00e9n linje) listes permanent p\u00e5 supporterv\u00e6ggen nedenfor \u2014 eller anonymt, hvis du foretr\u00e6kker det.",
        "tiers": [("En d\u00e5se cola", "$2", ""), ("En sixpack", "$9", ""), ("En hel kasse", "$29", "")],
        "note": "Creems betalingslinks klarg\u00f8res \u2014 vil du st\u00f8tte med det samme? Skriv til <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Allerede st\u00f8ttet? G\u00f8r krav p\u00e5 din plads",
            "name": "Vist navn",
            "message": "Besked p\u00e9n linje (valgfri)",
            "email": "E-mail brugt ved betaling",
            "anon": "N\u00e6vnt mig anonymt",
            "send": "G\u00f8r krav p\u00e5 min notering",
            "ok": "\u2713 Du er p\u00e5 v\u00e6ggen \u2014 genindl\u00e6s for at se det.",
            "fail": "Kunne ikke verificere betalingen \u2014 skriv til hello@fxverter.com.",
            "nopaid": "Ingen matchende betaling fundet for denne e-mail endnu.",
            "needEmail": "Angiv den e-mail, du betalte med.",
            "anonLabel": "Anonymt",
        },
    },
})


# ─── Greek (el) support/privacy overrides (missed in the vi/el batch) ───

TRUST_OVERRIDES["supportIntro"].update({
    "el": "Το Fxverter είναι δωρεάν — χωρίς λογαριασμό, χωρίς παρακολούθηση. Αν σας βοήθησε να μετατρέψετε μερικές ισοτιμίες, κερασμένум μας ένα κόλα: κάθε συνεισφορά πηγαίνει στον τομέα, τους διακομιστές και τη συνεχή ανάπτυξη. Οι πληρωμές διεκπεραιώνονται από την Creem ως merchant of record — τα στοιχεία πληρωμής σας διαχειρίζεται η Creem, όχι αυτός ο ιστότοπος.",
})

TRUST_OVERRIDES["supportDesc"].update({
    "el": "Υποστηρίξτε το Fxverter: δωρεάν — χωρίς λογαριασμό, χωρίς παρακολούθηση. Οι συνεισφορές το κρατούν γρήγορο, δωρεάν και ανεξάρτητο· πληρωμές μέσω Creem.",
})

TRUST_OVERRIDES["privacyNote"].update({
    "el": "Απόρρητο: δεν απαιτούνται cookies και δεν συλλέγονται προσωπικά δεδομένα. Μπορούν να συλλέγονται ανώνυμα στατιστικά επισκέψεων χωρίς cookies (προβολές σελίδων και χώρα). Ο ιστότοπος μπορεί να εμφανίζει διαφημίσεις — δείτε την <a href=\"{base}el/privacy/\">Πολιτική Απορρήτου</a>.",
})

TRUST_OVERRIDES["support"].update({
    "el": {
        "headline": "♥ Κερασμένум μας ένα κόλα",
        "choose": "Κερασμένум έναν γύρο",
        "perk": "Δεν είναι δωρεά — είναι ένα μικρό ψηφιακό ευχαριστώ: επιλέξτε πακέτο και το όνομά σας (με προαιρετικό μήνυμα ενός στίχου) εμφανίζεται μόνιμα στον τοίχο υποστηρικτών παρακάτω — ή ανώνυμα, αν προτιμάτε.",
        "tiers": [("Ένα κουτί κόλα", "$2", ""), ("Συσκευασία έξι", "$9", ""), ("Ολόκληρο κιβώτιο", "$29", "")],
        "note": "Οι σύνδεσμοι πληρωμής Creem ετοιμάζονται — θέλετε να στηρίξετε τώρα; Γράψτε στο <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>.",
        "claim": {
            "title": "Υποστηρίξατε ήδη; Διεκδικήστε τη θέση σας",
            "name": "Εμφανιζόμενο όνομα",
            "message": "Μήνυμα ενός στίχου (προαιρετικό)",
            "email": "Email που χρησιμοποιήθηκε στην πληρωμή",
            "anon": "Αναφέρατε με ανώνυμα",
            "send": "Διεκδίκηση της καταχώρισής μου",
            "ok": "✓ Είστε στον τοίχο — ανανεώστε για να το δείτε.",
            "fail": "Δεν ήταν δυνατή η επαλήθευση της πληρωμής — γράψτε στο hello@fxverter.com.",
            "nopaid": "Δεν βρέθηκε ακόμη πληρωμή για αυτό το email.",
            "needEmail": "Εισάγετε το email με το οποίο πληρώσατε.",
            "anonLabel": "Ανώνυμα",
        },
    },
})
