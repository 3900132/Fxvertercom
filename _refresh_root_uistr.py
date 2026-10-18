# -*- coding: utf-8 -*-
"""One-off: regenerate the inline UI_STR snapshot inside index.html from
content/ui_strings.py. The root page is the only page the build script does
not rewrite, so its baked-in dictionary goes stale when new keys are added."""
import io, re, json, sys
sys.path.insert(0, ".")
from content.ui_strings import UI

path = "index.html"
src = io.open(path, encoding="utf-8").read()
fresh = "const UI_STR = window.UI_STR = " + json.dumps(UI, ensure_ascii=False, separators=(",", ":")) + ";"
new, n = re.subn(r"^const UI_STR = window\.UI_STR = \{.*\};$", lambda m: fresh, src, count=1, flags=re.M)
assert n == 1, f"inline UI_STR line not found (n={n})"
io.open(path, "w", encoding="utf-8", newline="\n").write(new)
print("inline UI_STR refreshed,", len(UI), "languages")
