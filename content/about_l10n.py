# -*- coding: utf-8 -*-
"""Per-language "about" paragraphs (专属介绍) for every currency page.

ABOUT_L10N[lang][code] = localized intro paragraph shown on
/<lang>/currencies/<code>/ pages. Chinese entries come from content/about_zh.py
(hand-written); every other language lives in a content/about_batch_*.py file
(ABOUT_BATCH dict, lang-keyed). A language/code pair with no entry falls back
to the localized template in CONTENT_UI["curAbout"], so missing blocks simply
degrade gracefully.
"""
import os
import importlib

from content.about_zh import ABOUT_ZH

ABOUT_L10N = {"zh": dict(ABOUT_ZH)}

_here = os.path.dirname(os.path.abspath(__file__))
for _fn in sorted(os.listdir(_here)):
    if _fn.startswith("about_batch_") and _fn.endswith(".py"):
        _mod = importlib.import_module("content." + _fn[:-3])
        for _lang, _d in getattr(_mod, "ABOUT_BATCH", {}).items():
            ABOUT_L10N.setdefault(_lang, {}).update(_d)