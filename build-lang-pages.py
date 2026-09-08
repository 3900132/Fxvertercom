#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate per-language static pages (<code>/index.html) from index.html.

The root index.html is the canonical English entry; it auto-redirects
visitors by browser language (http/https only). Each generated page bakes
the translated UI strings into the static HTML so search engines and AI
crawlers see the target language without executing JavaScript.

Run from the repo root:  python build-lang-pages.py
Root edits (UI, FAQ, styles) should be made in index.html, then re-run.
"""
import os, re, json, datetime, sys

from page_content import CONTENT
from content.ui_strings import UI, SUPPORT_LABEL
from content.content_ui import CONTENT_UI
from content.supporters import SUPPORTERS
from content.currencies import CURRENCY_INFO

BASE = "https://fxverter.com/"

CF_BEACON = ('<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" '
             "data-cf-beacon='{\"token\": \"c616c0616b1341d6b1e4930665891a63\"}'></script>")

# Support page: create products in your Creem.io dashboard, paste the checkout
# links here, and re-run this script. Leave empty to show a "coming soon" note.
SUPPORT_TIERS = [
    # ("Buy me a coffee", "$3", "https://www.creem.io/checkout/your-product-1"),
    # ("Supporter", "$10", "https://www.creem.io/checkout/your-product-2"),
    # ("Hero", "$25", "https://www.creem.io/checkout/your-product-3"),
]

# Localized <title> / <meta description> per language.
META = {
 "en": ("Currency Converter \u2013 Live Exchange Rates for 140+ Currencies | Fxverter",
        "Free online currency converter with live exchange rates for 140+ world currencies. No API key, no sign-up, no tracking. 29 languages, mobile-friendly."),
 "tr": ("D\u00f6viz \u00c7evirici \u2013 Canl\u0131 D\u00f6viz Kurlar\u0131 | Fxverter",
        "140'dan fazla para birimi i\u00e7in \u00fccretsiz \u00e7evrimi\u00e7i d\u00f6viz \u00e7evirici. API anahtar\u0131 gerekmez, kay\u0131t yok, takip yok. Taray\u0131c\u0131n\u0131zda \u00e7al\u0131\u015f\u0131r."),
 "de": ("W\u00e4hrungsrechner \u2013 Aktuelle Wechselkurse | Fxverter",
        "Kostenloser Online-W\u00e4hrungsrechner mit aktuellen Wechselkursen f\u00fcr \u00fcber 140 W\u00e4hrungen. Kein API-Schl\u00fcssel, keine Anmeldung, kein Tracking."),
 "fr": ("Convertisseur de Devises \u2013 Taux de Change en Direct | Fxverter",
        "Convertisseur de devises en ligne gratuit avec les taux de change en direct de plus de 140 devises. Sans cl\u00e9 API, sans inscription, sans tracking."),
 "es": ("Conversor de Divisas \u2013 Tipos de Cambio en Vivo | Fxverter",
        "Conversor de divisas online gratuito con tipos de cambio en vivo de m\u00e1s de 140 monedas. Sin clave API, sin registro, sin seguimiento."),
 "pt": ("Conversor de Moedas \u2013 Taxas de C\u00e2mbio ao Vivo | Fxverter",
        "Conversor de moedas online gratuito com taxas de c\u00e2mbio ao vivo para mais de 140 moedas. Sem chave API, sem cadastro, sem rastreamento."),
 "ru": ("\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u0435\u0440 \u0412\u0430\u043b\u044e\u0442 \u2013 \u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435 \u041a\u0443\u0440\u0441\u044b \u0412\u0430\u043b\u044e\u0442 | Fxverter",
        "\u0411\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u044b\u0439 \u043e\u043d\u043b\u0430\u0439\u043d-\u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0435\u0440 \u0432\u0430\u043b\u044e\u0442 \u0441 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u043c\u0438 \u043a\u0443\u0440\u0441\u0430\u043c\u0438 \u0431\u043e\u043b\u0435\u0435 140 \u0432\u0430\u043b\u044e\u0442. \u0411\u0435\u0437 API-\u043a\u043b\u044e\u0447\u0430, \u0431\u0435\u0437 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438, \u0431\u0435\u0437 \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u044f."),
 "zh": ("\u8d27\u5e01\u6362\u7b97\u5668 \u2013 \u5b9e\u65f6\u6c47\u7387 | Fxverter",
        "\u514d\u8d39\u7684\u5728\u7ebf\u8d27\u5e01\u6362\u7b97\u5668\uff0c\u63d0\u4f9b 140 \u591a\u79cd\u8d27\u5e01\u7684\u5b9e\u65f6\u6c47\u7387\u3002\u65e0\u9700API\u5bc6\u94a5\u3001\u65e0\u9700\u6ce8\u518c\u3001\u65e0\u8ffd\u8e2a\uff0c\u6d4f\u89c8\u5668\u76f4\u63a5\u4f7f\u7528\u3002"),
 "ja": ("\u901a\u8ca8\u30b3\u30f3\u30d0\u30fc\u30bf\u30fc \u2013 \u30ea\u30a2\u30eb\u30bf\u30a4\u30e0\u70ba\u66ff\u30ec\u30fc\u30c8 | Fxverter",
        "140\u4ee5\u4e0a\u306e\u901a\u8ca8\u306e\u30ea\u30a2\u30eb\u30bf\u30a4\u30e0\u70ba\u66ff\u30ec\u30fc\u30c8\u3092\u4f7f\u3048\u308b\u7121\u6599\u30aa\u30f3\u30e9\u30a4\u30f3\u901a\u8ca8\u30b3\u30f3\u30d0\u30fc\u30bf\u30fc\u3002API\u30ad\u30fc\u4e0d\u8981\u3001\u767b\u9332\u4e0d\u8981\u3001\u30c8\u30e9\u30c3\u30ad\u30f3\u30b0\u306a\u3057\u3002"),
 "ko": ("\ud658\uc728 \uacc4\uc0b0\uae30 \u2013 \uc2e4\uc2dc\uac04 \ud658\uc728 | Fxverter",
        "140\uac1c \uc774\uc0c1 \ud1b5\ud654\uc758 \uc2e4\uc2dc\uac04 \ud658\uc728\uc744 \uc81c\uacf5\ud558\ub294 \ubb34\ub8cc \uc628\ub77c\uc778 \ud658\uc728 \uacc4\uc0b0\uae30. API \ud0a4 \ube44\ud544\uc694, \uac00\uc785 \ube44\ud544\uc694, \ucd94\uc801 \uc5c6\uc74c."),
 "ar": ("\u0645\u062d\u0648\u0644 \u0627\u0644\u0639\u0645\u0644\u0627\u062a \u2013 \u0623\u0633\u0639\u0627\u0631 \u0627\u0644\u0635\u0631\u0641 \u0627\u0644\u0645\u0628\u0627\u0634\u0631\u0629 | Fxverter",
        "\u0645\u062d\u0648\u0644 \u0639\u0645\u0644\u0627\u062a \u0645\u062c\u0627\u0646\u064a \u0639\u0628\u0631 \u0627\u0644\u0625\u0646\u062a\u0631\u0646\u062a \u0628\u0623\u0633\u0639\u0627\u0631 \u0635\u0631\u0641 \u0645\u0628\u0627\u0634\u0631\u0629 \u0644\u0623\u0643\u062b\u0631 \u0645\u0646 140 \u0639\u0645\u0644\u0629. \u0628\u062f\u0648\u0646 \u0645\u0641\u062a\u0627\u062d API\u060c \u0628\u062f\u0648\u0646 \u062a\u0633\u062c\u064a\u0644\u060c \u0628\u062f\u0648\u0646 \u062a\u062a\u0628\u0639."),
 "hi": ("\u092e\u0941\u0926\u094d\u0930\u093e \u092a\u0930\u093f\u0935\u0930\u094d\u0924\u0915 \u2013 \u0932\u093e\u0907\u0935 \u0935\u093f\u0928\u093f\u092e\u092f \u0926\u0930\u0947\u0902 | Fxverter",
        "140+ \u092e\u0941\u0926\u094d\u0930\u093e\u0913\u0902 \u0915\u0940 \u0932\u093e\u0907\u0935 \u0935\u093f\u0928\u093f\u092e\u092f \u0926\u0930\u094b\u0902 \u0935\u093e\u0932\u093e \u0928\u093f\u0903\u0936\u0941\u0932\u094d\u0915 \u0911\u0928\u0932\u093e\u0907\u0928 \u092e\u0941\u0926\u094d\u0930\u093e \u092a\u0930\u093f\u0935\u0930\u094d\u0924\u0915\u0964 \u0915\u094b\u0908 API \u0915\u0941\u0902\u091c\u0940 \u0928\u0939\u0940\u0902, \u0938\u093e\u0907\u0928-\u0905\u092a \u0928\u0939\u0940\u0902, \u091f\u094d\u0930\u0947\u0915\u093f\u0902\u0917 \u0928\u0939\u0940\u0902\u0964"),
 "id": ("Konverter Mata Uang \u2013 Kurs Real-time | Fxverter",
        "Konverter mata uang online gratis dengan kurs real-time untuk 140+ mata uang. Tanpa kunci API, tanpa daftar, tanpa pelacakan."),
 "ms": ("Penukar Mata Wang \u2013 Kadar Semasa | Fxverter",
        "Penukar mata wang dalam talian percuma dengan kadar semasa untuk 140+ mata wang. Tanpa kunci API, tanpa pendaftaran, tanpa penjejakan."),
 "tl": ("Tagapagpalit ng Pera \u2013 Live na Exchange Rates | Fxverter",
        "Libreng online na tagapagpalit ng pera na may live na exchange rates para sa 140+ pera. Walang API key, walang sign-up, walang tracking."),
 "it": ("Convertitore Valute \u2013 Tassi di Cambio in Tempo Reale | Fxverter",
        "Convertitore di valute online gratuito con tassi di cambio in tempo reale per oltre 140 valute. Senza chiave API, senza registrazione, senza tracciamento."),
 "nl": ("Valutaomrekenner \u2013 Actuele Wisselkoersen | Fxverter",
        "Gratis online valutaomrekenner met actuele wisselkoersen voor meer dan 140 valuta. Geen API-sleutel, geen registratie, geen tracking."),
 "pl": ("Przelicznik Walut \u2013 Aktualne Kursy Walut | Fxverter",
        "Darmowy przelicznik walut online z aktualnymi kursami ponad 140 walut. Bez klucza API, bez rejestracji, bez \u015bledzenia."),
 "uk": ("\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u0435\u0440 \u0412\u0430\u043b\u044e\u0442 \u2013 \u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u0456 \u041a\u0443\u0440\u0441\u0438 \u0412\u0430\u043b\u044e\u0442 | Fxverter",
        "\u0411\u0435\u0437\u043a\u043e\u0448\u0442\u043e\u0432\u043d\u0438\u0439 \u043e\u043d\u043b\u0430\u0439\u043d-\u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0435\u0440 \u0432\u0430\u043b\u044e\u0442 \u0437 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u0438\u043c\u0438 \u043a\u0443\u0440\u0441\u0430\u043c\u0438 \u043f\u043e\u043d\u0430\u0434 140 \u0432\u0430\u043b\u044e\u0442. \u0411\u0435\u0437 API-\u043a\u043b\u044e\u0447\u0430, \u0431\u0435\u0437 \u0440\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u0457, \u0431\u0435\u0437 \u0432\u0456\u0434\u0441\u0442\u0435\u0436\u0435\u043d\u043d\u044f."),
 "sv": ("Valutaomvandlare \u2013 Aktuella V\u00e4xelkurser | Fxverter",
        "Gratis online-valutaomvandlare med aktuella v\u00e4xelkurser f\u00f6r \u00f6ver 140 valutor. Utan API-nyckel, utan registrering, utan sp\u00e5rning."),
 "th": ("\u0e41\u0e1b\u0e25\u0e07\u0e2a\u0e01\u0e38\u0e25\u0e40\u0e07\u0e34\u0e19 \u2013 \u0e2d\u0e31\u0e15\u0e23\u0e32\u0e41\u0e25\u0e01\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1a\u0e1a\u0e40\u0e23\u0e35\u0e22\u0e25\u0e44\u0e17\u0e21\u0e4c | Fxverter",
        "\u0e15\u0e31\u0e27\u0e41\u0e1b\u0e25\u0e07\u0e2a\u0e01\u0e38\u0e25\u0e40\u0e07\u0e34\u0e19\u0e2d\u0e2d\u0e19\u0e44\u0e25\u0e19\u0e4c\u0e1f\u0e23\u0e35 \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e2d\u0e31\u0e15\u0e23\u0e32\u0e41\u0e25\u0e01\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e41\u0e1a\u0e1a\u0e40\u0e23\u0e35\u0e22\u0e25\u0e44\u0e17\u0e21\u0e4c\u0e01\u0e27\u0e48\u0e32 140 \u0e2a\u0e01\u0e38\u0e25 \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e43\u0e0a\u0e49 API Key \u0e44\u0e21\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e2a\u0e21\u0e31\u0e04\u0e23 \u0e44\u0e21\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e15\u0e34\u0e14\u0e15\u0e32\u0e21"),
 "lo": ("\u0e95\u0ebb\u0ea7\u0e9b\u0ec8\u0ebd\u0e99\u0eaa\u0eb0\u0e81\u0eb8\u0e99\u0ec0\u0e07\u0e34\u0e99 \u2013 \u0ead\u0eb1\u0e94\u0e95\u0eb2\u0ec1\u0ea5\u0e81\u0e9b\u0ec8\u0ebd\u0e87\u0e9b\u0eb0\u0e88\u0eb8\u0e9a\u0eb1\u0e99 | Fxverter",
        "\u0e95\u0ebb\u0ea7\u0e9b\u0ec8\u0ebd\u0e99\u0eaa\u0eb0\u0e81\u0eb8\u0e99\u0ec0\u0e07\u0e34\u0e99\u0ead\u0ead\u0e99\u0ea5\u0eb2\u0e8d\u0e9f\u0ebc\u0eb5 \u0e9e\u0ec9\u0ead\u0ea1\u0ead\u0eb1\u0e94\u0e95\u0eb2\u0ec1\u0ea5\u0e81\u0e9b\u0ec8\u0ebd\u0e87\u0e9b\u0eb0\u0e88\u0eb8\u0e9a\u0eb1\u0e99\u0e82\u0ead\u0e87\u0eaa\u0eb0\u0e81\u0eb8\u0e99\u0ec0\u0e87\u0e34\u0e99\u0e81\u0ea7\u0ec8\u0eb2 140 \u0eaa\u0eb0\u0e81\u0eb8\u0e99. \u0e9a\u0ecd\u0e95\u0ec9\u0ead\u0e87\u0ec3\u0e8a\u0ec9 API key, \u0e9a\u0ecd\u0e95\u0ec9\u0ead\u0e87\u0eaa\u0eb0\u0ec1\u0ea1\u0eb1\u0e81, \u0e9a\u0ecd\u0ea1\u0eb5\u0e81\u0eb2\u0e99\u0e95\u0eb4\u0e94\u0e95\u0eb2\u0ea1."),
 "vi": ("Chuy\u1ec3n \u0110\u1ed5i Ti\u1ec1n T\u1ec7 \u2013 T\u1ef7 Gi\u00e1 Tr\u1ef1c Tuy\u1ebfn | Fxverter",
        "C\u00f4ng c\u1ee5 chuy\u1ec3n \u0111\u1ed5i ti\u1ec1n t\u1ec7 tr\u1ef1c tuy\u1ebfn mi\u1ec5n ph\u00ed v\u1edbi t\u1ef7 gi\u00e1 tr\u1ef1c tuy\u1ebfn cho h\u01a1n 140 lo\u1ea1i ti\u1ec1n. Kh\u00f4ng c\u1ea7n API key, kh\u00f4ng c\u1ea7n \u0111\u0103ng k\u00fd, kh\u00f4ng theo d\u00f5i."),
 "el": ("\u039c\u03b5\u03c4\u03b1\u03c4\u03c1\u03bf\u03c0\u03ad\u03b1\u03c2 \u039d\u03bf\u03bc\u03b9\u03c3\u03bc\u03ac\u03c4\u03c9\u03bd \u2013 \u0396\u03c9\u03bd\u03c4\u03b1\u03bd\u03ad\u03c2 \u0399\u03c3\u03bf\u03c4\u03b9\u03bc\u03af\u03b5\u03c2 | Fxverter",
        "\u0394\u03c9\u03c1\u03b5\u03ac\u03bd online \u03bc\u03b5\u03c4\u03b1\u03c4\u03c1\u03bf\u03c0\u03ad\u03b1\u03c2 \u03bd\u03bf\u03bc\u03b9\u03c3\u03bc\u03ac\u03c4\u03c9\u03bd \u03bc\u03b5 \u03b6\u03c9\u03bd\u03c4\u03b1\u03bd\u03ad\u03c2 \u03b9\u03c3\u03bf\u03c4\u03b9\u03bc\u03af\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03c0\u03ac\u03bd\u03c9 \u03b1\u03c0\u03cc 140 \u03bd\u03bf\u03bc\u03af\u03c3\u03bc\u03b1\u03c4\u03b1. \u03a7\u03c9\u03c1\u03af\u03c2 \u03ba\u03bb\u03b5\u03b9\u03b4\u03af API, \u03c7\u03c9\u03c1\u03af\u03c2 \u03b5\u03b3\u03b3\u03c1\u03b1\u03c6\u03ae, \u03c7\u03c9\u03c1\u03af\u03c2 \u03c0\u03b1\u03c1\u03b1\u03ba\u03bf\u03bb\u03bf\u03cd\u03b8\u03b7\u03c3\u03b7."),
 "bn": ("\u09ae\u09c1\u09a6\u09cd\u09b0\u09be \u09b0\u09c2\u09aa\u09be\u09a8\u09cd\u09a4\u0995\u0995\u09be\u09b0\u09c0 \u2013 \u09b2\u09be\u0987\u09ad \u09ac\u09bf\u09a8\u09bf\u09ae\u09af\u09bc \u09b9\u09be\u09b0 | Fxverter",
        "\u09e7\u09ea\u0eec\u099f\u09bf\u09b0 \u09ac\u09c7\u09b6\u09bf \u09ae\u09c1\u09a6\u09cd\u09b0\u09be\u09b0 \u09b2\u09be\u0987\u09ad \u09ac\u09bf\u09a8\u09bf\u09ae\u09af\u09bc \u09b9\u09be\u09b0\u09b8\u09b9 \u09ab\u09cd\u09b0\u09bf \u0985\u09a8\u09b2\u09be\u0987\u09a8 \u09ae\u09c1\u09a6\u09cd\u09b0\u09be \u09b0\u09c2\u09aa\u09be\u09a8\u09cd\u09a4\u0995\u0995\u09be\u09b0\u09c0\u0964 \u0995\u09cb\u09a8\u09cb API \u0995\u09bf \u09a8\u09c7\u0987, \u09b8\u09be\u0987\u09a8-\u0986\u09aa \u09a8\u09c7\u0987, \u099f\u09cd\u09b0\u09cd\u09af\u09be\u0995\u09bf\u0982 \u09a8\u09c7\u0987\u0964"),
 "fa": ("\u062a\u0628\u062f\u06cc\u0644 \u0627\u0631\u0632 \u2013 \u0646\u0631\u062e \u0627\u0631\u0632 \u0644\u062d\u0638\u0647\u200c\u0627\u06cc | Fxverter",
        "\u0645\u0628\u062f\u0644 \u0627\u0631\u0632 \u0622\u0646\u0644\u0627\u06cc\u0646 \u0631\u0627\u06cc\u06af\u0627\u0646 \u0628\u0627 \u0646\u0631\u062e \u0627\u0631\u0632 \u0644\u062d\u0638\u0647\u200c\u0627\u06cc \u0628\u0631\u0627\u06cc \u0628\u06cc\u0634 \u0627\u0632 \u06f1\u06f4\u06f0 \u0627\u0631\u0632. \u0628\u062f\u0648\u0646 \u06a9\u0644\u06cc\u062f API\u060c \u0628\u062f\u0648\u0646 \u062b\u0628\u062a\u200c\u0646\u0627\u0645\u060c \u0628\u062f\u0648\u0646 \u0631\u062f\u06cc\u0627\u0628\u06cc."),
 "cs": ("P\u0159evodn\u00edk M\u011bn \u2013 Aktu\u00e1ln\u00ed Kurzy M\u011bn | Fxverter",
        "Bezplatn\u00fd online p\u0159evodn\u00edk m\u011bn s aktu\u00e1ln\u00edmi kurzy v\u00edce ne\u017e 140 m\u011bn. Bez kl\u00ed\u010de API, bez registrace, bez sledov\u00e1n\u00ed."),
 "ro": ("Convertor Valutar \u2013 Cursuri de Schimb \u00een Timp Real | Fxverter",
        "Convertor valutar online gratuit cu cursuri de schimb \u00een timp real pentru peste 140 de valute. F\u0103r\u0103 cheie API, f\u0103r\u0103 \u00eenregistrare, f\u0103r\u0103 urm\u0103rire."),
 "da": ("Valutaomregner \u2013 Aktuelle Valutakurser | Fxverter",
        "Gratis online valutaomregner med aktuelle valutakurser for mere end 140 valutaer. Uden API-n\u00f8gle, uden registrering, uden sporing."),
}

# brand the description of every language entry (meta/og/twitter all read from META)
for _k, _v in META.items():
    if not _v[1].startswith("Fxverter"):
        META[_k] = (_v[0], "Fxverter — " + _v[1])

OG_LOCALE = {"en":"en_US","tr":"tr_TR","de":"de_DE","fr":"fr_FR","es":"es_ES","pt":"pt_BR",
 "ru":"ru_RU","zh":"zh_CN","ja":"ja_JP","ko":"ko_KR","ar":"ar_AR","hi":"hi_IN","id":"id_ID",
 "ms":"ms_MY","tl":"tl_PH","it":"it_IT","nl":"nl_NL","pl":"pl_PL","uk":"uk_UA","sv":"sv_SE",
 "th":"th_TH","lo":"lo_LA","vi":"vi_VN","el":"el_GR","bn":"bn_IN","fa":"fa_IR","cs":"cs_CZ",
 "ro":"ro_RO","da":"da_DK"}

FIELDS = ("name","dir","appTitle","appSub","liveBadge","labelApiSource","labelAmount",
          "labelFrom","labelTo","btnText","resultLabel","footer","fsLabel")

def unesc(s):
    return s.replace("\\'", "'")

def sub1(text, pattern, repl):
    if callable(repl):
        return re.sub(pattern, repl, text, count=1)
    return re.sub(pattern, lambda m: repl, text, count=1)

html = open("index.html", encoding="utf-8").read()
block = re.search(r"const LANGS = \{(.*?)\n\};", html, re.S).group(1)

# shared crawlable lists for the per-language sections
nat_block = re.search(r"const NATIVE_NAMES = \{(.*?)\};", html, re.S).group(1)
NATIVE = {k: v.replace("\\'", "'") for k, v in re.findall(r"(\w{2}):'((?:\\.|[^'])*)'", nat_block)}
cur_block = re.search(r"const CURRENCIES=\[(.*?)\n\];", html, re.S).group(1)
CURRENCIES = [(c, n.replace("\\'", "'").replace("&", "&amp;"))
              for c, n in re.findall(r"\{code:'([A-Z]{3})',name:'((?:\\.|[^'])*)'\}", cur_block)]

_groups = {}
for _c, _n in CURRENCIES:
    _groups.setdefault(_c[0], []).append(f"{_c} — {_n}")
CUR_HTML = "".join(f"\n    <p><strong>{L}</strong> — " + " · ".join(items) + "</p>"
                   for L, items in sorted(_groups.items()))

LINK_F = '<a href="https://frankfurter.dev/" rel="noopener">Frankfurter</a>'
LINK_E = '<a href="https://www.exchangerate-api.com/" rel="noopener">ExchangeRate-API</a>'
LINK_W = '<a href="https://github.com/fawazahmed0/exchange-api" rel="noopener">Fawaz Currency API</a>'


# ═══════════════════════════════════════════════════════
# LANG PAGES
# ═══════════════════════════════════════════════════════
UI_JSON = json.dumps(UI, ensure_ascii=False, separators=(",", ":"))
UI_INJECT = "const UI_STR = window.UI_STR = " + UI_JSON + ";\n"

def inject_ui(page):
    """Add the UI_STR dictionary before LANGS on any page missing it."""
    if "const UI_STR" in page:
        return page
    return page.replace("const LANGS = {", UI_INJECT + "const LANGS = {", 1)


def build_section(code):
    """Localized, crawlable About/FAQ section for one language page."""
    c = CONTENT[code]
    faq_items = "".join(
        f"\n  <details>\n    <summary>{q}</summary>\n    <p>{a}</p>\n  </details>"
        for q, a in c["faqs"]
    )
    p2 = c["p2"].replace("{F}", LINK_F).replace("{E}", LINK_E).replace("{W}", LINK_W)
    return (
        '<section class="seo-section" aria-labelledby="aboutTitle">\n'
        f'  <h2 id="aboutTitle">{c["h2"]}</h2>\n'
        f'  <p>{c["p1"]}</p>\n'
        f'  <p>{p2}</p>\n'
        f'\n  <h3>{c["lh"]}</h3>\n'
        f'  <p><a href="{BASE}{code}/currencies/">{UI[code]["curLink"]}</a> · <a href="{BASE}{code}/guides/">{UI[code]["guideLink"]}</a></p>\n'
        f'  <p>{c["lang_intro"]} {LANG_LIST}.</p>\n'
        f'  <p>{c["cur_intro"]}</p>\n'
        f'  <details id="curList">\n    <summary>{c["cur_summary"]}</summary>{CUR_HTML}\n  </details>\n'
        f'\n  <h3 id="faqTitle">{c["faq_h"]}</h3>{faq_items}\n'
        f'\n  <p class="seo-disclaimer">{c["disc"]}</p>\n'
        f'  <p class="seo-disclaimer" lang="en">Privacy: this website uses no cookies and collects no personal data. Anonymous, cookie-free visit statistics (page views and country) may be collected to improve the tool.</p>\n</section>'
    )
langs, order = {}, []
for part in re.split(r"\n  (?=[a-z]{2}:\{)", block):
    m = re.match(r"([a-z]{2}):\{", part)
    if not m:
        continue
    code = m.group(1)
    def f(name, part=part):
        mm = re.search(name + r":'((?:\\.|[^'])*)'", part)
        return unesc(mm.group(1)) if mm else None
    langs[code] = {k: f(k) for k in FIELDS}
    order.append(code)

LANG_LIST = " · ".join(f"<strong>{c.upper()}</strong> {NATIVE[c]}" for c in order if c in NATIVE)

def hreflang_block():
    lines = [f'<link rel="alternate" hreflang="en" href="{BASE}">']
    for c in order:
        if c != "en":
            lines.append(f'<link rel="alternate" hreflang="{c}" href="{BASE}{c}/">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}">')
    return "\n".join(lines)

generated = []
for code, t in langs.items():
    if code == "en":
        continue
    page = html
    title, desc = META[code]

    # root-only redirect must not appear on language pages
    page = re.sub(r'<script id="lang-redirect">.*?</script>\s*', "", page, count=1, flags=re.S)

    rtl = ' dir="rtl"' if t["dir"] == "rtl" else ""
    page = page.replace('<html lang="en">', f'<html lang="{code}"{rtl}>', 1)
    page = sub1(page, r"<title>.*?</title>", f"<title>{title}</title>")
    page = sub1(page, r'(<meta name="description" content=")[^"]*(">)', lambda m: m.group(1) + desc + m.group(2))
    page = sub1(page, r'(<meta property="og:title" content=")[^"]*(">)', lambda m: m.group(1) + title + m.group(2))
    page = sub1(page, r'(<meta property="og:description" content=")[^"]*(">)', lambda m: m.group(1) + desc + m.group(2))
    page = sub1(page, r'(<meta name="twitter:title" content=")[^"]*(">)', lambda m: m.group(1) + title + m.group(2))
    page = sub1(page, r'(<meta name="twitter:description" content=")[^"]*(">)', lambda m: m.group(1) + desc + m.group(2))
    page = sub1(page, r'(<meta property="og:locale" content=")[^"]*(">)', lambda m: m.group(1) + OG_LOCALE[code] + m.group(2))

    # structured data: self-canonical per language, English FAQ markup stays (FAQ text is visible in English)
    page = page.replace('"url": "' + BASE + '",', '"' + "url" + '": "' + BASE + code + '/",', 1)
    page = page.replace('"@id": "' + BASE + '#app"', '"@id": "' + BASE + code + '/#app"', 1)
    page = page.replace('"@id": "' + BASE + '#faq"', '"@id": "' + BASE + code + '/#faq"', 1)
    page = page.replace('"name": "Fxverter",', '"name": "' + t["appTitle"] + '",', 1)
    page = sub1(page, r'("description": ")[^"]*(",\n      "inLanguage")', lambda m: m.group(1) + desc + m.group(2))
    page = sub1(page, r'"inLanguage": \[[^\]]*\]', f'"inLanguage": ["{code}"]')

    # canonical + full hreflang set (strip any inherited hreflang lines first)
    page = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n?', "", page)
    canon = f'<link rel="canonical" href="{BASE}{code}/">'
    page = sub1(page, r'<link rel="canonical" href="[^"]*">',
                canon + "\n" + hreflang_block())

    # bake translated UI strings into the static HTML
    page = sub1(page, r'(<h1 id="appTitle">).*?(</h1>)', lambda m: m.group(1) + t["appTitle"] + m.group(2))
    page = sub1(page, r'(<span id="appSub">).*?(</span>)', lambda m: m.group(1) + t["appSub"] + m.group(2))
    page = sub1(page, r'(<span id="liveBadge">).*?(</span>)', lambda m: m.group(1) + t["liveBadge"] + m.group(2))
    for fid in ("labelApiSource", "labelAmount", "labelFrom", "labelTo"):
        page = sub1(page, r'(id="' + fid + r'">).*?(</span>)', lambda m, v=t[fid]: m.group(1) + v + m.group(2))
    page = sub1(page, r'(<span id="btnText">).*?(</span>)', lambda m: m.group(1) + t["btnText"] + m.group(2))
    page = sub1(page, r'(id="resultLabel">).*?(</div>)', lambda m: m.group(1) + t["resultLabel"] + m.group(2))
    page = sub1(page, r'(<div class="footer" id="footerText">).*?(</div>)', lambda m: m.group(1) + t["footer"] + m.group(2))
    page = sub1(page, r'(<span class="fs-label" id="fsLabel">).*?(</span>)', lambda m: m.group(1) + t["fsLabel"] + m.group(2))

    # fixed language for the page runtime; select navigates between directories
    page = page.replace("applyLang(detectLang());", f"applyLang('{code}');", 1)
    page = page.replace('<script id="langGo" data-base="./">', '<script id="langGo" data-base="../">', 1)
    # PWA paths resolve one directory up from language pages
    page = page.replace('<link rel="manifest" href="manifest.webmanifest">', '<link rel="manifest" href="../manifest.webmanifest">', 1)
    page = page.replace('<link rel="apple-touch-icon" href="apple-touch-icon.png">', '<link rel="apple-touch-icon" href="../apple-touch-icon.png">', 1)
    page = page.replace('<script id="swReg" data-base="./">', '<script id="swReg" data-base="../">', 1)

    # fully localized About/FAQ section + localized FAQ structured data
    page = re.sub(r'<section class="seo-section".*?</section>',
                  lambda m: build_section(code), page, count=1, flags=re.S)
    # localized privacy note replaces the lang="en" line added by build_section
    page = page.replace(
        '  <p class="seo-disclaimer" lang="en">Privacy: this website uses no cookies and collects no personal data. Anonymous, cookie-free visit statistics (page views and country) may be collected to improve the tool.</p>',
        f'  <p class="seo-disclaimer" id="privacyNote">{UI[code]["privacy"]}</p>', 1)
    mainentity = '"mainEntity": ' + json.dumps(
        [{"@type": "Question", "name": q,
          "acceptedAnswer": {"@type": "Answer", "text": a}}
         for q, a in CONTENT[code]["faqs"]],
        ensure_ascii=False)
    page = re.sub(r'"mainEntity": \[.*?\]', lambda m: mainentity, page, count=1, flags=re.S)

    page = inject_ui(page)

    # footer support link: localized label + depth-correct href
    sup_label = SUPPORT_LABEL.get(code, "Support")
    page = page.replace('<a id="supportLink" href="support/">♥ <span id="supportLabel">Support</span></a>',
                        f'<a id="supportLink" href="{BASE}{code}/support/">♥ <span id="supportLabel">{sup_label}</span></a>', 1)
    # feedback link + about-section nav links: localize text, fix depth
    fb_label = UI[code]["feedback"]
    page = page.replace('<a id="feedbackLink" href="https://splitforms.com/f/fxverter" target="_blank" rel="noopener"><span id="feedbackLabel">Feedback</span></a>',
                        f'<a id="feedbackLink" href="https://splitforms.com/f/fxverter" target="_blank" rel="noopener"><span id="feedbackLabel">{fb_label}</span></a>', 1)
    page = page.replace('<a href="currencies/" id="curNavLink">Browse all currencies</a>',
                        f'<a href="{BASE}{code}/currencies/" id="curNavLink">{UI[code]["curLink"]}</a>', 1)
    page = page.replace('<a href="guides/" id="guideNavLink">Exchange-rate guides</a>',
                        f'<a href="{BASE}{code}/guides/" id="guideNavLink">{UI[code]["guideLink"]}</a>', 1)
    # Explore-more lead text lives in the localized section built from CONTENT; the root
    # paragraph is replaced wholesale by build_section, so patch the nav links there instead.

    os.makedirs(code, exist_ok=True)
    with open(os.path.join(code, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(page)
    generated.append(code)

# ═══════════════════════════════════════════════════════
# CURRENCY PAGES (/currencies/<code>/) — data-driven, edit
# content/currencies.py to add info, then re-run this script.
# ═══════════════════════════════════════════════════════
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "."))

MAJOR = ["USD", "EUR", "GBP", "JPY", "CNY", "CHF", "TRY", "INR", "KRW", "AUD",
         "CAD", "MXN", "BRL", "ZAR", "SEK", "NOK", "NZD", "SGD", "HKD", "THB"]

CUR_PAGE_CSS = """<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#0d0d14;--surface:#16161f;--surface2:#1e1e2a;--border:rgba(255,255,255,0.08);--border2:rgba(255,255,255,0.14);--text:#eeeef5;--muted:#6868a0;--muted2:#9898c0;--teal:#5ecfb0;--syne:'Syne',sans-serif;--dm:'DM Sans',sans-serif;--shadow:0 24px 60px rgba(0,0,0,0.45)}
html.theme-light{--bg:#f4f6fa;--surface:#ffffff;--surface2:#eef1f6;--border:rgba(13,13,20,0.10);--border2:rgba(13,13,20,0.18);--text:#1a1c26;--muted:#6b7192;--muted2:#4a5170;--teal:#14967a;--shadow:0 18px 44px rgba(13,20,40,0.14)}
@media (prefers-color-scheme: light){:root:not(.theme-force-dark){--bg:#f4f6fa;--surface:#ffffff;--surface2:#eef1f6;--border:rgba(13,13,20,0.10);--border2:rgba(13,13,20,0.18);--text:#1a1c26;--muted:#6b7192;--muted2:#4a5170;--teal:#14967a;--shadow:0 18px 44px rgba(13,20,40,0.14)}}
body{background:var(--bg);font-family:var(--dm);color:var(--text);min-height:100vh;display:flex;flex-direction:column;align-items:center;padding:1rem 1rem 3rem;font-size:1rem}
a{color:var(--teal);text-decoration:none}a:hover{text-decoration:underline}
.home{color:var(--muted2);font-size:0.75rem;margin-bottom:1rem}
.home a{color:var(--muted2)}
.cur-card{width:100%;max-width:560px;background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:1.6rem 1.7rem;box-shadow:0 24px 60px rgba(0,0,0,0.45)}
.cur-head{display:flex;align-items:center;gap:0.9rem;margin-bottom:1rem}
.cur-flag{font-size:2.6rem;line-height:1}
.cur-head h1{font-family:var(--syne);font-size:1.6rem;font-weight:700;line-height:1.15}
.cur-head .sub{color:var(--muted);font-size:0.82rem;margin-top:0.2rem}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:0.6rem;margin:1rem 0 1.2rem}
.fact{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:0.7rem 0.9rem}
.fact .k{font-size:0.6rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted);font-family:var(--syne)}
.fact .v{font-size:0.92rem;margin-top:0.15rem}
.about{color:var(--muted2);font-size:0.86rem;line-height:1.65;margin-bottom:1.3rem}
h2{font-family:var(--syne);font-size:1rem;font-weight:700;margin:1.3rem 0 0.6rem}
.ratebox{background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:1rem 1.1rem;margin-bottom:1.2rem}
.ratebox input{width:100%;background:var(--surface);border:1px solid var(--border);border-radius:10px;color:var(--text);font-family:var(--syne);font-size:1.15em;font-weight:700;padding:0.6rem 0.8rem;outline:none}
.ratebox input:focus{border-color:rgba(94,207,176,0.4)}
.ratebox .out{font-family:var(--syne);font-size:1.3em;font-weight:700;color:var(--teal);margin-top:0.7rem;min-height:1.5em}
.ratebox .err{color:#e87a9a;font-size:0.8rem;margin-top:0.5rem;display:none}
table{width:100%;border-collapse:collapse;font-size:0.82rem}
td,th{padding:0.45rem 0.5rem;border-bottom:1px solid var(--border);text-align:left}
th{color:var(--muted);font-size:0.65rem;letter-spacing:0.08em;text-transform:uppercase;font-family:var(--syne)}
td.r,th.r{text-align:right}
.status{color:var(--muted);font-size:0.72rem;margin-top:0.6rem}
.links{display:flex;flex-wrap:wrap;gap:0.35rem;margin-top:1rem}
.links a{background:var(--surface2);border:1px solid var(--border);border-radius:100px;padding:0.28rem 0.75rem;font-size:0.72rem;color:var(--muted2)}
.links a:hover{border-color:var(--teal);color:var(--teal);text-decoration:none}
.disc{color:var(--muted);font-size:0.68rem;margin-top:1.4rem;max-width:560px;text-align:center}
.chart-box{background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:1rem 1.1rem;margin-bottom:1.2rem}
.chart-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:0.5rem}
.chart-head .t{font-family:var(--syne);font-size:0.8rem;font-weight:700}
.chart-head .d{font-size:0.68rem;color:var(--muted);margin-top:0.35rem}
.chart-head .chg{font-size:0.75rem;font-weight:500}
.chg.up{color:#e87a9a}.chg.down{color:#5ecfb0}
html.theme-light .chg.up{color:#c74e70}html.theme-light .chg.down{color:#14967a}
@media(prefers-color-scheme:light){:root:not(.theme-force-dark) .chg.up{color:#c74e70}:root:not(.theme-force-dark) .chg.down{color:#14967a}}
.spark{width:100%;height:110px;display:block}
.spark .ln{fill:none;stroke:var(--teal);stroke-width:2}
.spark .area{fill:var(--teal);opacity:0.10;stroke:none}
.spark text{fill:var(--muted);font-size:9px;font-family:'DM Sans',sans-serif}
.fxtheme{position:fixed;top:0.8rem;right:0.9rem;z-index:50;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:0.3rem 0.55rem;color:var(--muted2);cursor:pointer;font-size:0.85rem;line-height:1}
.fxtheme:hover{border-color:var(--teal);color:var(--teal)}
@media(max-width:480px){.facts{grid-template-columns:1fr}}
</style>"""

# Shared tools bar (theme / share / feedback / install / language) appended to
# every secondary page: currency pages, currency index, guides, support.
TOOLS_CSS = """<style>
.tools-bar{width:100%;max-width:560px;display:flex;align-items:center;justify-content:space-between;gap:0.5rem;margin-bottom:1rem}
.tools-left{display:flex;gap:0.3rem}
.tool-btn{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:0.3rem 0.55rem;font-family:var(--dm);font-weight:500;color:var(--muted2);cursor:pointer;transition:all 0.15s;line-height:1;font-size:0.85rem}
.tool-btn:hover{border-color:var(--border2);color:var(--text)}
.tool-btn.ok{border-color:var(--teal);color:var(--teal)}
.lang-sel{appearance:none;background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:0.32rem 0.7rem;font-family:var(--dm);font-size:0.72rem;font-weight:500;color:var(--muted2);outline:none;cursor:pointer;max-width:150px}
.lang-sel:hover{border-color:var(--border2);color:var(--text)}
.lang-sel option{background:#1e1e2a;color:#eeeef5}
html.theme-light .lang-sel option{background:#ffffff;color:#1a1c26}
@media (prefers-color-scheme: light){:root:not(.theme-force-dark) .lang-sel option{background:#ffffff;color:#1a1c26}}
.fb-panel{display:none;width:100%;max-width:560px;margin:0 0 1rem;background:var(--surface);border:1px solid var(--border2);border-radius:14px;padding:1rem;box-shadow:0 18px 44px rgba(0,0,0,0.35)}
.fb-panel.open{display:block}
.fb-panel input[type="text"],.fb-panel input[type="email"],.fb-panel textarea{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:10px;color:var(--text);font-family:var(--dm);font-size:0.85rem;padding:0.55rem 0.8rem;margin-bottom:0.55rem;outline:none}
.fb-panel input:focus,.fb-panel textarea:focus{border-color:var(--teal)}
.fb-panel textarea{resize:vertical;min-height:70px}
.fb-err{display:none;color:#e87a9a;font-size:0.78rem;margin-bottom:0.4rem}
.fb-panel button[type="submit"]{width:100%;background:var(--teal);border:none;border-radius:10px;color:#fff;font-family:var(--syne);font-weight:700;font-size:0.85rem;padding:0.6rem;cursor:pointer}
.fb-panel button[type="submit"]:disabled{opacity:0.6;cursor:default}
.fb-ok{display:none;text-align:center;color:var(--teal);font-family:var(--syne);font-weight:700;font-size:1rem;padding:0.8rem 0}
</style>"""
CUR_PAGE_CSS = CUR_PAGE_CSS + TOOLS_CSS

THEME_HELPERS = """<script>
(function () {
  var mode = 'auto';
  try { mode = localStorage.getItem('fxTheme') || 'auto'; } catch (e) {}
  if (mode === 'light') document.documentElement.classList.add('theme-light');
  if (mode === 'dark')  document.documentElement.classList.add('theme-force-dark');
  window.__fxTheme = mode;
})();
</script>
<script>
function fxToggleTheme() {
  var order = ['auto', 'light', 'dark'];
  var next = order[(order.indexOf(window.__fxTheme || 'auto') + 1) % 3];
  window.__fxTheme = next;
  try { localStorage.setItem('fxTheme', next); } catch (e) {}
  var root = document.documentElement;
  root.classList.remove('theme-light', 'theme-force-dark');
  if (next === 'light') root.classList.add('theme-light');
  if (next === 'dark')  root.classList.add('theme-force-dark');
  var btn = document.getElementById('fxThemeBtn');
  if (btn) btn.textContent = next === 'light' ? '☀' : next === 'dark' ? '☾' : '◐';
}
</script>"""

CUR_PAGE_JS = """<script>
const CODE = "{code}";
const SYMBOL = {sym_js};
async function rates(){
  try {
    const r = await fetch('https://api.frankfurter.dev/v1/latest?from=' + CODE);
    if (r.ok) return (await r.json()).rates;
  } catch (e) {}
  try {
    const r = await fetch('https://api.exchangerate-api.com/v4/latest/' + CODE);
    if (r.ok) return (await r.json()).rates;
  } catch (e) {}
  return null;
}
let R = null;
(async () => {
  R = await rates();
  const s = document.getElementById('st');
  if (!R) { s.textContent = {fail}; return; }
  s.textContent = {loaded};
  const tb = document.getElementById('rt');
  for (const t of {targets_js}) {
    if (R[t] === undefined) continue;
    const tr = document.createElement('tr');
    tr.innerHTML = '<td><a href="{sib}' + t.toLowerCase() + '/">1 ' + CODE + '</a></td><td class="r">' + R[t].toLocaleString(undefined,{maximumFractionDigits: R[t] >= 1000 ? 2 : 4}) + ' ' + t + '</td>';
    tb.appendChild(tr);
  }
})();
function calc(v){
  const out = document.getElementById('out'), err = document.getElementById('err');
  if (!R) { err.style.display = 'block'; return; }
  err.style.display = 'none';
  const amt = parseFloat(String(v).replace(',', '.'));
  if (isNaN(amt)) { out.textContent = ''; return; }
  const to = {to_js};
  const r = R[to];
  if (r === undefined) { err.style.display = 'block'; return; }
  out.textContent = (amt * r).toLocaleString(undefined, {maximumFractionDigits:2}) + ' ' + to + (SYMBOL ? ' (' + SYMBOL + ')' : '');
}
(async () => {
  // 30-day trend: 1 CODE -> USD (inverse of USD->CODE series)
  try {
    if (CODE === 'USD') return;
    const end = new Date(), start = new Date(Date.now() - 30 * 864e5);
    const iso = d => d.toISOString().slice(0, 10);
    const r = await fetch('https://api.frankfurter.dev/v1/' + iso(start) + '..' + iso(end) + '?from=' + CODE + '&to=USD');
    if (!r.ok) return;
    const d = await r.json();
    const keys = Object.keys(d.rates || {}).sort();
    if (keys.length < 3) return;
    const pts = keys.map(k => ({date: k, v: d.rates[k].USD}));
    const W = 500, H = 110, PAD = 8;
    const vs = pts.map(p => p.v);
    const min = Math.min(...vs), max = Math.max(...vs), span = (max - min) || 1;
    const x = i => PAD + i * (W - 2 * PAD) / (pts.length - 1);
    const y = v => H - PAD - (v - min) / span * (H - 2 * PAD - 14);
    let path = pts.map((p, i) => (i ? 'L' : 'M') + x(i).toFixed(1) + ' ' + y(p.v).toFixed(1)).join(' ');
    const area = path + ' L' + x(pts.length - 1).toFixed(1) + ' ' + (H - 2) + ' L' + x(0).toFixed(1) + ' ' + (H - 2) + ' Z';
    const svg = document.getElementById('spark');
    svg.innerHTML = '<path class="area" d="' + area + '"/><path class="ln" d="' + path + '"/>' +
      '<text x="' + PAD + '" y="12">' + min.toPrecision(4) + '</text>' +
      '<text x="' + (W - PAD) + '" y="12" text-anchor="end">' + max.toPrecision(4) + '</text>';
    document.getElementById('chartBox').hidden = false;
    const chg = ((vs[vs.length - 1] - vs[0]) / vs[0]) * 100;
    const el = document.getElementById('chg');
    el.textContent = (chg >= 0 ? '▲ +' : '▼ ') + chg.toFixed(2) + '%';
    el.classList.add(chg >= 0 ? 'up' : 'down');
    document.getElementById('chartRange').textContent = pts[0].date + ' → ' + pts[pts.length - 1].date + ' · ECB reference rates';
  } catch (e) {}
})();
</script>"""


# ═══════════════════════════════════════════════════════
# SHARED TOOLS BAR — theme / share / feedback / PWA install / language switch
# present on every secondary page (currency pages, guides, support).
# ═══════════════════════════════════════════════════════
TOOLS_JS_BODY = """const FX_PAGE = __FX_PAGE__;
const FX_T = __FX_T__;
function fxShare() {
  const url = location.href.split('#')[0];
  const done = () => { const b = document.getElementById('shareBtn'); if (!b) return; b.classList.add('ok'); b.title = FX_T.shared; setTimeout(() => { b.classList.remove('ok'); b.title = FX_T.share; }, 1400); };
  if (navigator.share) { navigator.share({ title: document.title, url: url }).catch(() => {}); return; }
  if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(done).catch(() => fxCopyFallback(url, done));
  else fxCopyFallback(url, done);
}
function fxCopyFallback(text, done) {
  const ta = document.createElement('textarea');
  ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
  document.body.appendChild(ta); ta.select();
  try { document.execCommand('copy'); done(); } catch (e) {}
  document.body.removeChild(ta);
}
function fxOpenFeedback() {
  const panel = document.getElementById('fbPanel');
  if (!panel) return;
  panel.classList.toggle('open');
  if (panel.classList.contains('open')) {
    const m = document.getElementById('fbMsg');
    if (m) { m.placeholder = FX_T.fbPlaceholder; m.focus(); }
  }
}
function fxSendFeedback() {
  const name = document.getElementById('fbName').value.trim();
  const email = document.getElementById('fbEmail').value.trim();
  const message = document.getElementById('fbMsg').value.trim();
  const err = document.getElementById('fbErr');
  if (!message) { err.style.display = 'block'; err.textContent = FX_T.fbEmpty; return; }
  err.style.display = 'none';
  const btn = document.getElementById('fbSendBtn');
  btn.disabled = true;
  fetch('https://splitforms.com/api/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify({
      access_key: '99f9b5e09c4b43b3a7eef1f22ff09722',
      subject: 'Fxverter feedback',
      name: name || 'anonymous',
      email: email || '',
      message: message
    })
  }).then(r => {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    document.getElementById('fbForm').style.display = 'none';
    document.getElementById('fbOk').style.display = 'block';
    setTimeout(() => {
      document.getElementById('fbPanel').classList.remove('open');
      document.getElementById('fbForm').style.display = '';
      document.getElementById('fbOk').style.display = 'none';
      document.getElementById('fbMsg').value = '';
    }, 2500);
  }).catch(() => {
    err.style.display = 'block'; err.textContent = FX_T.fbFail;
  }).finally(() => { btn.disabled = false; });
}
function fxLangGo(c) {
  if (c === FX_PAGE.cur) return;
  try { sessionStorage.setItem('fxLangUI', c); } catch (e) {}
  if (location.protocol.indexOf('http') !== 0) return; // offline use: nothing to switch
  // same page in the chosen language, relative to the current origin;
  // pages without a localized variant fall back to that language's home page
  location.assign(location.origin + '/' + (c === 'en' ? '' : c + '/') + (FX_PAGE.sub || ''));
}
(function () {
  // PWA install: browser offers it only in a secure context (https / localhost)
  if (location.protocol.indexOf('http') !== 0) return;
  if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone) return;
  var deferred = null;
  var btn = document.getElementById('installBtn');
  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault();
    deferred = e;
    if (btn) { btn.hidden = false; btn.title = FX_T.install; }
  });
  window.fxInstall = function () {
    if (!deferred) return;
    deferred.prompt();
    deferred.userChoice.then(function () { deferred = null; if (btn) btn.hidden = true; });
  };
  window.addEventListener('appinstalled', function () { deferred = null; if (btn) btn.hidden = true; });
})();
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register(FX_PAGE.root + 'sw.js').catch(function () {});
  });
}
(function () {
  var btn = document.getElementById('fxThemeBtn');
  if (btn && window.__fxTheme) btn.textContent = window.__fxTheme === 'light' ? '☀' : window.__fxTheme === 'dark' ? '☾' : '◐';
})();"""

LANG_ORDER = list(NATIVE.keys())

def tools_bar(lang, sub, root):
    """Toolbar HTML for secondary pages: theme, share, feedback, install, language."""
    C = UI.get(lang, UI["en"])
    options = "".join(
        f'<option value="{c}"{" selected" if c == lang else ""}>{NATIVE.get(c, c.upper())}</option>'
        for c in LANG_ORDER)
    fx_t = json.dumps({
        "share": C["share"], "shared": C["shared"], "feedback": C["feedback"],
        "fbPlaceholder": C["fbPlaceholder"], "fbSend": C["fbSend"], "fbOk": C["fbOk"],
        "fbEmpty": C["fbEmpty"], "fbFail": C["fbFail"], "install": C["install"],
    }, ensure_ascii=False)
    fx_page = json.dumps({"cur": lang, "sub": sub, "base": BASE, "root": root})
    return (
        '<div class="tools-bar">'
        '<div class="tools-left">'
        '<button type="button" class="tool-btn" id="fxThemeBtn" onclick="fxToggleTheme()" title="Theme">◐</button>'
        f'<button type="button" class="tool-btn" id="shareBtn" onclick="fxShare()" title="{C["share"]}">⤴</button>'
        f'<button type="button" class="tool-btn" id="feedbackBtn" onclick="fxOpenFeedback()" title="{C["feedback"]}">✎</button>'
        f'<button type="button" class="tool-btn" id="installBtn" onclick="fxInstall()" title="{C["install"]}" hidden>⤓</button>'
        '</div>'
        f'<select class="lang-sel" id="langSel" onchange="fxLangGo(this.value)" aria-label="Language">{options}</select>'
        '</div>\n'
        '<div class="fb-panel" id="fbPanel">'
        '<form id="fbForm" onsubmit="fxSendFeedback(); return false;">'
        '<input type="text" id="fbName" maxlength="60" autocomplete="off" placeholder="Name">'
        '<input type="email" id="fbEmail" maxlength="80" placeholder="Email (optional)">'
        f'<textarea id="fbMsg" rows="4" maxlength="1000" placeholder="{C["fbPlaceholder"]}"></textarea>'
        '<input type="checkbox" style="display:none" tabindex="-1" autocomplete="off">'
        '<div class="fb-err" id="fbErr"></div>'
        f'<button type="submit" id="fbSendBtn">{C["fbSend"]}</button>'
        '</form>'
        f'<div class="fb-ok" id="fbOk" style="display:none">{C["fbOk"]}</div>'
        '</div>\n'
        '<script>' + TOOLS_JS_BODY.replace("__FX_PAGE__", fx_page).replace("__FX_T__", fx_t) + '</script>'
    )


def build_currency_page(code, en_name, lang="en"):
    C = CONTENT_UI.get(lang, CONTENT_UI["en"])
    info = CURRENCY_INFO.get(code, {})
    name = info.get("name", en_name)
    country = info.get("country", "")
    symbol = info.get("symbol", "")
    sub = info.get("sub", "")
    flag = info.get("flag", "🏳️")
    about = info.get("about",
        f"The {name} is one of the world currencies supported by Fxverter, the free online currency converter. "
        f"Fxverter shows live reference exchange rates for the {name} and 140 other currencies, sourced from "
        f"public central-bank data.")
    targets = [c for c in MAJOR if c != code]
    default_to = "USD" if code != "USD" else "EUR"

    # language-aware paths: /currencies/try/ (en) vs /zh/currencies/try/
    at_root = (lang == "en")
    dirpart = "" if at_root else f"{lang}/"
    # "All currencies" nav: one up from /currencies/try/ or two up from /zh/currencies/try/
    up = "../" if at_root else "../../"
    home = BASE if at_root else BASE + f"{lang}/"
    canon = f"{BASE}{dirpart}currencies/{code.lower()}/"
    hreflangs = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE}{"" if l == "en" else l + "/"}currencies/{code.lower()}/">'
        for l in CONTENT_UI)
    hreflangs += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}currencies/{code.lower()}/">'

    fact_defs = [("ISO", code), ("♦", symbol or "—"), ("🌍", country or "—"), ("¢", sub or "—")]
    facts = "".join(
        f'<div class="fact"><div class="k">{k}</div><div class="v">{v}</div></div>'
        for k, v in fact_defs if v and v != "—")

    # links to sibling currency pages: page sits at /currencies/<code>/ so a
    # sibling is always exactly one level up: ../usd/ — true for every language
    major_links = " ".join(
        f'<a href="../{c.lower()}/">{c}</a>'
        for c in MAJOR if c != code)

    # relative path back to the site root (for sw.js registration)
    root_up = "../../" if at_root else "../../../"
    tools = tools_bar(lang, f"currencies/{code.lower()}/", root_up)

    page = f"""<!DOCTYPE html>
<html lang="{lang}"{' dir="rtl"' if lang in ('ar', 'fa') else ''}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} ({code}) — Live Exchange Rates &amp; Currency Converter | Fxverter</title>
<meta name="description" content="{name} ({code}) live exchange rates: convert {code} to USD, EUR, GBP and 140 other currencies with the free Fxverter currency converter. Rates, facts and calculator.">
<link rel="canonical" href="{canon}">
{hreflangs}
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0d0d14">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E💱%3C/text%3E%3C/svg%3E">
<link rel="manifest" href="{BASE}manifest.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fxverter">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{name} ({code}) — Live Exchange Rates | Fxverter">
<meta property="og:description" content="Convert {code} to USD, EUR and 140+ currencies. Live reference rates, quick facts and calculator for the {name}.">
<meta property="og:image" content="{BASE}og-image.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "{canon}#page",
  "url": "{canon}",
  "name": "{name} ({code}) — Live Exchange Rates | Fxverter",
  "description": "Convert {code} to USD, EUR and 140+ currencies with live reference rates, quick facts and a calculator.",
  "inLanguage": "{lang}",
  "isPartOf": {{"@type": "WebSite", "name": "Fxverter", "url": "{BASE}"}},
  "about": {{"@type": "Thing", "name": "{name}"}}
}}
</script>
<script src="https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{code.lower()}.min.json" defer></script>
{CUR_PAGE_CSS}
{THEME_HELPERS}
</head>
<body>
{tools}
<div class="home"><a href="{home}">{C["backHome"]}</a> · <a href="{up}">{C["allCurrencies"]}</a></div>
<main class="cur-card" itemscope itemtype="https://schema.org/Thing">
  <div class="cur-head">
    <div class="cur-flag" aria-hidden="true">{flag}</div>
    <div>
      <h1 itemprop="name">{name} ({code})</h1>
      <div class="sub">{META.get(lang, META["en"])[0].split("|")[0].strip()}</div>
    </div>
  </div>
  <div class="facts">{facts}</div>
  <p class="about" itemprop="description" lang="en">{about}</p>
  <h2>{C["convert"]} {code}</h2>
  <div class="ratebox">
    <input type="text" inputmode="decimal" id="amt" placeholder="{C["calcPlaceholder"]} {code}" oninput="calc(this.value)">
    <div class="out" id="out"></div>
    <div class="err" id="err">{C["errBox"]}</div>
    <div class="status" id="st">{C["loading"]}</div>
  </div>
  <h2>1 {code} {C["rateHead"]}</h2>
  <div class="chart-box" id="chartBox" hidden>
    <div class="chart-head">
      <span class="t">{C["chartHead"].replace("{code}", code)}</span>
      <span class="chg" id="chg"></span>
    </div>
    <svg class="spark" id="spark" viewBox="0 0 500 110" preserveAspectRatio="none" role="img" aria-label="{code} to USD 30-day trend"></svg>
    <div class="d" id="chartRange"></div>
  </div>
  <table aria-label="{code} {C["rateHead"]}">
    <thead><tr><th>{code}</th><th class="r">{C["allCurrencies"]}</th></tr></thead>
    <tbody id="rt"></tbody>
  </table>
  <div class="links" aria-label="Other currencies">{major_links}</div>
</main>
<p class="disc">{C["disclaimer"]} · <a href="{home}">Fxverter</a></p>
{CUR_PAGE_JS.replace("{code}", code).replace("{sib}", "../").replace("{sym_js}", json.dumps(symbol)).replace("{targets_js}", json.dumps(targets)).replace("{to_js}", json.dumps(default_to)).replace("{loading}", json.dumps(C["loading"], ensure_ascii=False)).replace("{loaded}", json.dumps(C["ratesLoaded"], ensure_ascii=False)).replace("{fail}", json.dumps(C["ratesFail"], ensure_ascii=False))}
</body>
</html>"""
    return page


cur_dir = os.path.join("currencies")
os.makedirs(cur_dir, exist_ok=True)

def build_cur_index(lang="en"):
    C = CONTENT_UI.get(lang, CONTENT_UI["en"])
    at_root = (lang == "en")
    idx_items = "".join(
        f'<li><a href="{c.lower()}/">{c} — {CURRENCY_INFO.get(c, {}).get("name", dict(CURRENCIES).get(c, c))}</a></li>'
        for c, n in CURRENCIES)
    home = BASE if at_root else BASE + f"{lang}/"
    up = "../" if at_root else "../../"
    hreflangs = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE}{"" if l == "en" else l + "/"}currencies/">'
        for l in CONTENT_UI)
    hreflangs += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}currencies/">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{C["allCurrencies"]} (141) | Fxverter</title>
<meta name="description" content="Fxverter supports 141 world currencies — US Dollar, Euro, Turkish Lira, Japanese Yen and more. Live reference rates and a dedicated page for each currency.">
<link rel="canonical" href="{BASE}{"" if at_root else lang + "/"}currencies/">
{hreflangs}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E💱%3C/text%3E%3C/svg%3E">
<meta name="theme-color" content="#0d0d14">
{CUR_PAGE_CSS}
{THEME_HELPERS}
{CF_BEACON}
</head>
<body>
{tools_bar(lang, "currencies/", "../" if at_root else "../../")}
<div class="home"><a href="{home}">{C["backHome"]}</a></div>
<main class="cur-card">
<h1>{C["allCurrencies"]}</h1>
<p class="about">{C["curLangIntro"]}</p>
<ul style="columns:2;-webkit-columns:2;gap:1.5rem;padding-left:1.2rem;font-size:0.85rem;line-height:1.9" aria-label="Currency list">
{idx_items}
</ul>
</main>
</body>
</html>"""

for _lang in CONTENT_UI:
    ld = cur_dir if _lang == "en" else os.path.join(_lang, "currencies")
    os.makedirs(ld, exist_ok=True)
    with open(os.path.join(ld, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_cur_index(_lang))

cur_pages = 0
for lang in CONTENT_UI:
    for code, en_name in CURRENCIES:
        d = os.path.join("currencies", code.lower()) if lang == "en" else os.path.join(lang, "currencies", code.lower())
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(build_currency_page(code, en_name, lang))
        cur_pages += 1

# ── guides: guides/*.md → /guides/<slug>/ pages ──
GUIDE_CSS = CUR_PAGE_CSS
guides_dir = "guides"
guide_entries = []
if os.path.isdir(guides_dir):
    md_files = sorted(f for f in os.listdir(guides_dir) if f.endswith(".md"))
    for mf in md_files:
        raw = open(os.path.join(guides_dir, mf), encoding="utf-8").read()
        parts = raw.split("---", 2)
        meta = {}
        body = raw
        if len(parts) == 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
            body = parts[2]
        slug = meta.get("slug", os.path.splitext(mf)[0])
        title = meta.get("title", slug.replace("-", " ").title())
        desc = meta.get("description", body.strip()[:150])
        # minimal markdown: paragraphs, ## headings, - lists, **bold**
        html_body = []
        for block in re.split(r"\n\s*\n", body.strip()):
            lines = block.split("\n")
            if lines[0].startswith("## "):
                html_body.append(f"<h2>{lines[0][3:].strip()}</h2>")
                rest = [l for l in lines[1:] if l.strip()]
                if rest:
                    html_body.append("<p>" + "<br>".join(l.strip() for l in rest) + "</p>")
            elif lines[0].startswith("- "):
                items = "".join(f"<li>{l[2:].strip()}</li>" for l in lines if l.startswith("- "))
                html_body.append(f"<ul>{items}</ul>")
            else:
                text = "<br>".join(l.strip() for l in lines if l.strip())
                text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
                html_body.append(f"<p>{text}</p>")
        content_html = "\n".join(html_body)
        d = os.path.join(guides_dir, slug)
        os.makedirs(d, exist_ok=True)
        gpage = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Fxverter</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}guides/{slug}/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E💱%3C/text%3E%3C/svg%3E">
<meta name="theme-color" content="#0d0d14">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "{desc}",
  "author": {{"@type": "Person", "name": "Seyyid Kadir"}},
  "publisher": {{"@type": "Organization", "name": "Fxverter", "url": "{BASE}"}},
  "mainEntityOfPage": "{BASE}guides/{slug}/"
}}
</script>
{GUIDE_CSS}
{THEME_HELPERS}
</head>
<body>
{tools_bar("en", "", "../../")}
<div class="home"><a href="{BASE}">← Fxverter — Currency Converter</a> · <a href="../">All guides</a></div>
<main class="cur-card">
<h1>{title}</h1>
<article class="about" style="font-size:0.92rem;color:var(--text)">
{content_html}
</article>
</main>
<p class="disc">© 2026 Fxverter · <a href="{BASE}">Free currency converter</a> — 141 currencies, 29 languages, no sign-up.</p>
</body>
</html>"""
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(gpage)
        guide_entries.append((slug, title, desc))

# guides index
if guide_entries or True:
    d = "guides"
    os.makedirs(d, exist_ok=True)
    items = "".join(
        f'<li><a href="{s}/">{t}</a><br><span style="color:var(--muted);font-size:0.75rem">{de[:110]}</span></li>'
        for s, t, de in guide_entries) or '<li style="color:var(--muted)">Guides are coming soon.</li>'
    gi = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Exchange-Rate Guides | Fxverter</title>
<meta name="description" content="Plain-language guides about exchange rates: how rates are set, mid-market rates, when to exchange money and more. By Fxverter, the free currency converter.">
<link rel="canonical" href="{BASE}guides/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E💱%3C/text%3E%3C/svg%3E">
<meta name="theme-color" content="#0d0d14">
{CUR_PAGE_CSS}
{THEME_HELPERS}
</head>
<body>
{tools_bar("en", "", "../")}
<div class="home"><a href="{BASE}">← Fxverter — Currency Converter</a></div>
<main class="cur-card">
<h1>Exchange-rate guides</h1>
<p class="about">Plain-language explanations of how exchange rates work, by the Fxverter team.</p>
<ul style="padding-left:1.2rem;font-size:0.88rem;line-height:2.2">
{items}
</ul>
</main>
</body>
</html>"""
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(gi)

# ═══════════════════════════════════════════════════════
# SUPPORT PAGE (/support/) — Creem.io checkout tiers + supporters wall.
# ═══════════════════════════════════════════════════════

def build_support_page(lang="en"):
    C = CONTENT_UI.get(lang, CONTENT_UI["en"])
    at_root = (lang == "en")
    home = BASE if at_root else BASE + f"{lang}/"
    canon = f"{BASE}support/" if at_root else f"{BASE}{lang}/support/"
    hreflangs = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE}{"" if l == "en" else l + "/"}support/">'
        for l in CONTENT_UI)
    hreflangs += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}support/">'
    tiers_html = "".join(
        f'<a class="tier" href="{url}" target="_blank" rel="noopener"><span class="tier-name">{name}</span><span class="tier-amt">{amt}</span></a>'
        for name, amt, url in SUPPORT_TIERS) or \
        f'<p class="about" style="color:var(--muted)">{C["supportComing"]}</p>'
    if SUPPORTERS:
        wall = "".join(
            f'<div class="sup-card"><b>{s["name"]}</b><span class="tier-tag">{s.get("tier","")}</span>'
            + (f'<p class="sup-msg">“{s["message"]}”</p>' if s.get("message") else "")
            + '</div>'
            for s in SUPPORTERS)
        wall_html = f'<h2>{C["supportThanks"]}</h2><div class="sup-wall">{wall}</div>'
    else:
        wall_html = f'<p class="about">{C["supportFirst"]}</p>'
    return f"""<!DOCTYPE html>
<html lang="{lang}"{' dir="rtl"' if lang in ('ar', 'fa') else ''}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{C["supportPrivacyNote"].split("©")[0].strip()} | Fxverter</title>
<meta name="description" content="Fxverter is free, with no ads and no tracking. If you find it useful, support its development — every contribution keeps it free for everyone.">
<link rel="canonical" href="{canon}">
{hreflangs}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E💱%3C/text%3E%3C/svg%3E">
<meta name="theme-color" content="#0d0d14">
<meta property="og:title" content="Support Fxverter">
<meta property="og:description" content="Fxverter is free, with no ads and no tracking. Support its development if you find it useful.">
<meta property="og:image" content="{BASE}og-image.png">
{CUR_PAGE_CSS}
<style>
.tier{{display:flex;justify-content:space-between;align-items:center;gap:1rem;background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:0.9rem 1.1rem;margin-bottom:0.55rem;text-decoration:none;color:var(--text);transition:all .15s}}
.tier:hover{{border-color:var(--teal);color:var(--teal)}}
.tier-name{{font-family:var(--syne);font-weight:700}}
.tier-amt{{color:var(--teal);font-weight:700;font-family:var(--syne)}}
h2{{font-family:var(--syne);font-size:1rem;font-weight:700;margin:1.4rem 0 0.6rem}}
.sup-wall{{display:grid;grid-template-columns:1fr 1fr;gap:0.55rem}}
.sup-card{{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:0.7rem 0.9rem;font-size:0.82rem}}
.sup-card b{{color:var(--text)}}
.tier-tag{{margin-left:0.5rem;color:var(--teal);font-size:0.72rem}}
.sup-msg{{margin-top:0.35rem;color:var(--muted2);font-style:italic}}
@media(max-width:480px){{.sup-wall{{grid-template-columns:1fr}}}}
</style>
{THEME_HELPERS}
{CF_BEACON}
</head>
<body>
{tools_bar(lang, "support/", "../" if at_root else "../../")}
<div class="home"><a href="{home}">{C["backHome"]}</a></div>
<main class="cur-card">
<h1>♥ Fxverter</h1>
<p class="about">{C["supportIntro"]}</p>
<h2>{C["supportChoose"]}</h2>
{tiers_html}
{wall_html}
<p class="disc" style="margin-top:1.2rem">{C["supportPrivacyNote"]}</p>
</main>
</body>
</html>"""

for _lang in CONTENT_UI:
    d = "support" if _lang == "en" else os.path.join(_lang, "support")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(build_support_page(_lang))

# inject the Cloudflare beacon into every generated currency / guide page
def add_beacon(path):
    p = os.path.join(path, "index.html")
    if not os.path.exists(p):
        return
    t = open(p, encoding="utf-8").read()
    if "cloudflareinsights" not in t:
        t = t.replace("</head>", CF_BEACON + "\n</head>", 1)
        open(p, "w", encoding="utf-8", newline="\n").write(t)

for code, _ in CURRENCIES:
    add_beacon(os.path.join("currencies", code.lower()))
add_beacon("currencies")
for slug, _t, _d in guide_entries:
    add_beacon(os.path.join("guides", slug))
add_beacon("guides")

# sitemap: root + languages + currencies + guides + support
lastmod = datetime.date.today().isoformat()
urls = [f"""  <url>
    <loc>{BASE}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""]
for c in order:
    if c == "en":
        continue
    urls.append(f"""  <url>
    <loc>{BASE}{c}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")
urls.append(f"""  <url>
    <loc>{BASE}currencies/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")
for code, _ in CURRENCIES:
    urls.append(f"""  <url>
    <loc>{BASE}currencies/{code.lower()}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>""")
# localized currency pages: /zh/currencies/try/ etc.
for l in CONTENT_UI:
    if l == "en":
        continue
    urls.append(f"""  <url>
    <loc>{BASE}{l}/currencies/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>""")
    for code, _ in CURRENCIES:
        urls.append(f"""  <url>
    <loc>{BASE}{l}/currencies/{code.lower()}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>""")
for slug, _t, _d in guide_entries:
    urls.append(f"""  <url>
    <loc>{BASE}guides/{slug}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")
urls.append(f"""  <url>
    <loc>{BASE}guides/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>""")
urls.append(f"""  <url>
    <loc>{BASE}support/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.4</priority>
  </url>""")
for _l in CONTENT_UI:
    if _l == "en":
        continue
    urls.append(f"""  <url>
    <loc>{BASE}{_l}/support/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.4</priority>
  </url>""")
with open("sitemap.xml", "w", encoding="utf-8", newline="\n") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
             + "\n".join(urls) + "\n</urlset>\n")

print(f"generated {len(generated)} language pages: {' '.join(generated)}")
print(f"generated {cur_pages} currency pages + /currencies/ index")
print(f"generated {len(guide_entries)} guide pages + /guides/ index")
print("sitemap.xml rewritten with", len(urls), "urls")
