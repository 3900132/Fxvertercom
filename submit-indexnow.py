#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Submit fxverter.com URLs to IndexNow (Bing / Yandex / Seznam / Naver).

Ownership is proven by a key file at the site root (ebad7e82a81a05f950421869b7058a56.txt,
committed to this repo), so every GitHub Pages deploy keeps the site verified —
no Bing Webmaster settings to touch. The shared endpoint api.indexnow.org
routes the submission to every participating engine at once.

Run after each deploy (the sitemap only contains indexable pages):
    python submit-indexnow.py            # submit every sitemap URL
    python submit-indexnow.py --dry-run  # show the payload, send nothing
"""
import json, sys, urllib.error, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

HOST = "fxverter.com"
KEY = "ebad7e82a81a05f950421869b7058a56"
SITEMAP = Path(__file__).with_name("sitemap.xml")
ENDPOINT = "https://api.indexnow.org/indexnow"


def sitemap_urls():
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(SITEMAP).getroot()
    return [loc.text.strip() for loc in root.findall("s:url/s:loc", ns) if loc.text]


def main():
    dry = "--dry-run" in sys.argv
    urls = sitemap_urls()
    if not urls:
        sys.exit("sitemap.xml has no <loc> entries — run build-lang-pages.py first")
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEY}.txt",
        "urlList": urls,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    print(f"{len(urls)} URLs loaded from sitemap.xml" + (" (dry run)" if dry else ""))
    if dry:
        print(json.dumps({**payload, "urlList": urls[:3] + ["…"]}, ensure_ascii=False, indent=2))
        return
    req = urllib.request.Request(
        ENDPOINT, data=body, headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"HTTP {resp.status} — accepted. Engines will crawl shortly.")
    except urllib.error.HTTPError as e:
        hints = {
            400: "malformed payload",
            403: "key not valid — is the key .txt file deployed to the site root?",
            422: "URLs don't belong to the host, or the key file doesn't match",
            429: "too many requests — back off and retry later",
        }
        sys.exit(f"HTTP {e.code} — {hints.get(e.code, e.reason)}")
    except urllib.error.URLError as e:
        sys.exit(f"network error: {e.reason}")


if __name__ == "__main__":
    main()
