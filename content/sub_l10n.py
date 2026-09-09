# -*- coding: utf-8 -*-
"""Localized minor-unit ("sub") strings per currency.

SUB_L10N[code][lang] = fully rendered sub-fact string for that language.
Languages missing for a currency fall back to the original English value from
CURRENCY_INFO.

Chinese entries are hand-written full sentences ("1美元 = 100美分"). For every
other site language the fact line is composed deterministically from small
per-language vocabularies kept in content/sub_vocab_*.py (see _load_vocab).
Adding a language = drop in one more sub_vocab file; no other edits needed.
"""

# ---------------------------------------------------------------------------
# zh: hand-written full sentences (as before)
# ---------------------------------------------------------------------------
_ZH = {
 "USD": "1美元 = 100美分",
 "EUR": "1欧元 = 100欧分",
 "GBP": "1英镑 = 100便士",
 "JPY": "1日元 = 100钱（已很少使用）",
 "TRY": "1里拉 = 100库鲁什",
 "CNY": "1元 = 10角 = 100分",
 "CHF": "1法郎 = 100生丁",
 "INR": "1卢比 = 100派士",
 "KRW": "1韩元 = 100钱（已停用）",
 "AUD": "1澳元 = 100分",
 "CAD": "1加元 = 100分",
 "MXN": "1比索 = 100分",
 "BRL": "1雷亚尔 = 100分",
 "ZAR": "1兰特 = 100分",
 "RUB": "1卢布 = 100戈比",
 "SAR": "1里亚尔 = 100哈拉拉",
 "AED": "1迪拉姆 = 100费尔",
 "SEK": "1瑞典克朗 = 100欧尔",
 "NOK": "1挪威克朗 = 100欧尔",
 "NZD": "1新西兰元 = 100分",
 "SGD": "1新加坡元 = 100分",
 "HKD": "1港元 = 100仙",
 "THB": "1泰铢 = 100萨当",
 "IDR": "1印尼盾 = 100仙",
 "MYR": "1林吉特 = 100仙",
 "PHP": "1菲律宾比索 = 100分",
 "VND": "1越南盾 = 10毫 = 100苏",
 "LAK": "1基普 = 100阿特（已停用）",
 "PKR": "1巴基斯坦卢比 = 100派沙",
 "BDT": "1塔卡 = 100波依沙",
 "NGN": "1奈拉 = 100考包",
 "EGP": "1埃及镑 = 100皮阿斯特",
 "UAH": "1格里夫纳 = 100戈比",
 "PLN": "1兹罗提 = 100格罗希",
 "CZK": "1捷克克朗 = 100赫勒",
 "DKK": "1丹麦克朗 = 100欧尔",
 "ILS": "1以色列新谢克尔 = 100阿高洛",
 "QAR": "1卡塔尔里亚尔 = 100迪拉姆",
}

ALL_CODES = list(_ZH.keys())

# canonical subunit key per currency (key into each language's UNIT_WORDS);
# EUR uses a dedicated "eur" key so languages can say "欧分/centimes/…”.
CUR_UNIT = {
 "USD": "cents", "EUR": "eur", "GBP": "pence", "JPY": "sen", "TRY": "kurus",
 "CNY": "fen", "CHF": "rappen", "INR": "paisa", "KRW": "jeon",
 "AUD": "cents", "CAD": "cents", "MXN": "centavo", "BRL": "centavo",
 "ZAR": "cents", "RUB": "kopek", "SAR": "halala", "AED": "fils",
 "SEK": "ore", "NOK": "ore", "NZD": "cents", "SGD": "cents", "HKD": "cents",
 "THB": "satang", "IDR": "sen", "MYR": "sen", "PHP": "centavo",
 "VND": "xu", "LAK": "att", "PKR": "paisa", "BDT": "poisha", "NGN": "kobo",
 "EGP": "piastre", "UAH": "kopiyok", "PLN": "groszy", "CZK": "haler",
 "DKK": "ore", "ILS": "agora", "QAR": "dirham",
}

# two-tier subdivisions: "10 A = 100 B"
TWO_TIER = {"CNY": ("jiao", "fen"), "VND": ("hao", "xu")}

# subunits no longer minted -> a localized note is appended
RARE = {"JPY": "sen", "KRW": "jeon", "LAK": "att"}

import os
import importlib

def _load_vocab():
    """Import every content/sub_vocab_*.py; each defines VOCAB = {lang: {...}}
    and optionally RARENOTES = {lang: "no longer minted"}."""
    vocab = {}
    rare = {}
    here = os.path.dirname(os.path.abspath(__file__))
    for fn in sorted(os.listdir(here)):
        if fn.startswith("sub_languages_") and fn.endswith(".py"):
            mod = importlib.import_module("content." + fn[:-3])
            for lang, d in getattr(mod, "VOCAB", {}).items():
                vocab.setdefault(lang, {}).update(d)
            for lang, note in getattr(mod, "RARENOTES", {}).items():
                rare[lang] = note
    return vocab, rare

_VOCAB, _RARE = _load_vocab()

def _word(lang_words, key):
    if key == "eur":
        v = lang_words.get("eur") or lang_words.get("cents")
    else:
        v = lang_words.get(key)
    return v or key

def _build():
    for code in ALL_CODES:
        entry = {"zh": _ZH[code]}
        for lang, words in _VOCAB.items():
            if code in TWO_TIER:
                a, b = TWO_TIER[code]
                line = "10 {} = 100 {}".format(_word(words, a), _word(words, b))
            else:
                u = _word(words, CUR_UNIT[code])
                line = "100 " + u
                if code in RARE and lang in _RARE:
                    line += " ({})".format(_RARE[lang])
            entry[lang] = line
        SUB_L10N[code] = entry

SUB_L10N = {}

_build()