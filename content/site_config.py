# -*- coding: utf-8 -*-
"""Site-wide indexation policy: which pages are submitted to search engines.

Everything not listed here is still built and served (visitors keep the full
tool in all languages), but it is marked `noindex, follow` and left out of
sitemap.xml. Promote a language or currency here only after its content
passes quality review — thin, noindexed pages can be flipped back with one
edit to this file.
"""

BASE = "https://fxverter.com/"

# Languages promoted to search engines. All other generated language
# directories stay online for visitors but are noindexed until their
# deep content is written and reviewed.
INDEXED_LANGS = ["en", "zh", "de", "fr", "es", "pt", "ja"]

# Currency pages promoted to search engines (40 mainstream currencies).
# Every page outside this list stays online and usable but noindexed.
INDEXED_CURRENCIES = [
    "USD", "EUR", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "TRY", "INR",
    "MXN", "BRL", "ZAR", "SEK", "NOK", "NZD", "SGD", "HKD", "THB", "KRW",
    "DKK", "CZK", "PLN", "HUF", "RON", "BGN", "IDR", "ILS", "PHP", "MYR",
    "ISK", "AED", "SAR", "VND", "PKR", "NGN", "EGP", "TWD", "ARS", "CLP",
]

# Currencies covered by the ECB reference-rate set (Frankfurter time series)
# — the only pages that can render the 30/90-day trend chart. Currencies
# outside this set must not ship the chart module (it would fetch, fail and
# leave an empty box on the page).
ECB_SET = {
    "AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP",
    "HKD", "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "MXN", "MYR",
    "NOK", "NZD", "PHP", "PLN", "RON", "SEK", "SGD", "THB", "TRY", "USD",
    "ZAR",
}

# Trust pages (About / Privacy / Terms / Contact / Feedback), generated for
# these languages only; en lives at the site root.
TRUST_PAGES = ("about", "privacy", "terms", "contact", "feedback")
