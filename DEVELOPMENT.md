# Fxverter — 开发与内容维护指南

Fxverter 是一个纯静态多语言换汇工具站：首页（29 语言页）+ 141 个币种页 + 指南区 + 支持页，共 175 个页面。**你日常只编辑 5 个源文件，其余 170+ 个页面全部由构建脚本自动生成。**

---

## 一、核心工作流（最重要的一张表）

```
你编辑的源文件                         生成的页面（不要手动碰）
────────────────────────────          ─────────────────────────────
index.html          ─┐                /  +  tr/ zh/ ja/ … 28 个语言页
page_content.py      ├─ python        currencies/ ×141 + 索引页
content/ui_strings.py│  build-        guides/ 文章页 + 索引
content/currencies.py│  lang-         support/ 支持页
guides/*.md          ─┘  pages.py     sitemap.xml
```

**唯一要记住的命令**（在本目录下运行）：

```bash
python build-lang-pages.py
```

改完任何源文件后跑一次，然后提交/推送全部文件。没有服务器端代码——Python 只在你电脑上跑，GitHub Pages 只托管生成的 HTML。

---

## 二、五个源文件分别管什么

### 1. `index.html` — 网站主模板

首页本身 + 所有语言页的母版。改**界面样式、功能逻辑、FAQ 结构、head 里的 meta** 都在这里改。注意：

- head 里每个 `<meta>`/`og:` 标签会被复制到全部语言页；语言相关文本（标题、描述）由构建脚本替换
- `<script>` 里的 `LANGS`（界面翻译）和 `UI_STR`（按钮/提示翻译）是自动注入的，不要手动编辑，改翻译请去 `content/ui_strings.py`
- 域名相关的 URL 都来自构建脚本的 `BASE` 常量

### 2. `page_content.py` — 28 种语言的正文翻译

About/FAQ 区块的翻译（h2 标题、两段简介、FAQ 问答、免责声明）。每个语言一个 dict，想改某语言的措辞，找到对应语言键改文本即可。`{F}` `{E}` `{W}` 是三个数据源链接的占位符，保留即可。

### 3. `content/ui_strings.py` — 按钮/提示的翻译

主题按钮、收藏、复制、分享、反馈、支持、页脚链接等 UI 文案（29 语言 × 16 字段）。同上，按键改文本。`SUPPORT_LABEL` 单独一行管理页脚"♥ 支持"的各语言说法。

### 4. `content/currencies.py` — 币种档案数据

141 个币种里 38 个主要币种有手写介绍（国旗、国家、符号、辅币单位、about 介绍段）。想充实某个币种页，照格式加一段即可；没写 `about` 的币种自动用模板生成的通用介绍。

```python
"USD": {"name": "US Dollar", "country": "United States",
        "symbol": "$", "sub": "100 cents", "flag": "🇺🇸",
        "about": "一两句介绍……"},
```

### 5. `guides/*.md` — 汇率指南文章

**写文章就看这里**。每篇文章一个 Markdown 文件，格式：

```markdown
---
slug: how-exchange-rates-work      ← 决定 URL（/guides/how-exchange-rates-work/）
title: How Exchange Rates Are Set  ← 页面标题（也是 <title> 和 JSON-LD）
description: 一句话摘要             ← meta description
---

正文随便写。支持的结构：
## 二级标题      → 变成 <h2>
- 列表项         → 变成 <ul><li>
**加粗**        → 变成 <strong>
普通段落        → 变成 <p>
```

保存 → 跑 `python build-lang-pages.py` → 文章自动出现在 /guides/ 索引和 sitemap。删除 .md 文件即删除文章（记得重跑构建并删除已生成的对应目录，或直接留着也无害，但建议删干净）。

**写作建议**：每篇瞄准一个搜索意图（一个问题），600–900 词，面向"想弄懂换汇的人"而不是金融从业者；结尾自然带回主工具页的链接（生成模板已自动带）。

---

## 三、专项任务速查

| 想做什么 | 改哪里 | 然后做什么 |
|---------|--------|-----------|
| 加/改一种界面语言 | index.html 的 `LANGS` + page_content.py + ui_strings.py + 构建脚本 META | 重跑构建 |
| 加一个币种 | index.html 的 `CURRENCIES` 数组（按字母序） | 重跑构建（全站计数不会自动变，需同步改正文里的数字） |
| 改汇率数据源 | index.html 的 `fetchRates()` | 无需构建（但语言页要同步就重跑） |
| 上线捐赠档位 | 构建脚本顶部 `SUPPORT_TIERS` 填 Creem 的 checkout 链接 | 重跑构建 |
| 添加致谢名单 | `content/supporters.py` 加一条 | 重跑构建 |
| 换反馈渠道 | 全局搜索 `splitforms.com` 替换 | 重跑构建 |
| 强制用户刷新缓存 | `sw.js` 里 `fxcc-v3` 改成 `v4` | 推送即可 |

---

## 四、部署（GitHub Pages）

1. 全部文件提交到 `main` 分支并 push（包括生成的 28 个语言目录、currencies/、guides/、support/）
2. 仓库 Settings → Pages：Branch 选 `main`，目录选 `/ (root)`
3. 域名：根目录已有 `CNAME` 文件（内容 `fxverter.com`）。注册域名后，在域名商处添加 4 条 A 记录：`185.199.108–111.153` 指向根域名，GitHub Pages 会自动绑定并签发 HTTPS
4. 上线后：[Google Search Console](https://search.google.com/search-console) 添加资源 `fxverter.com`，提交 `https://fxverter.com/sitemap.xml`，并对首页"请求编入索引"

**统计**：Cloudflare Web Analytics 代码已内置在全部 175 页（token 已配置）。登录 [dash.cloudflare.com](https://dash.cloudflare.com) → Web Analytics 即可看到访问量、国家、来源。

---

## 五、PWA 说明（安装后才"看得见"）

PWA 没有界面上可见的按钮，它的表现是：

- **桌面 Chrome/Edge**：地址栏右侧出现"安装"图标（⊕ 或显示器图标），点击后 Fxverter 变成独立窗口应用
- **手机**：浏览器菜单里出现"添加到主屏幕/安装应用"，安装后桌面出现 Fxverter 图标（青色渐变 💱）
- **离线能力**：装过之后断网也能打开最近访问过的页面，汇率显示最后一次缓存的数据
- 开发者工具验证：F12 → Application → Manifest 可看到应用配置；Service Workers 面板可见已注册的 `sw.js`

本地 `file://` 打开单个 HTML 时不加载 PWA（属预期行为，保持单文件可用性）。

---

## 六、发布新内容检查清单

1. 改源文件（见上表）
2. `python build-lang-pages.py`
3. 浏览器抽查：根页 + 一两个语言页 + 相关内容页
4. push 到 GitHub
5. 大改动（新页面类型/新语言）时：把 `sw.js` 版本号 +1，确保老访客拿到新缓存
