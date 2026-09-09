# -*- coding: utf-8 -*-
"""Per-language minor-unit vocabularies. See content/sub_l10n.py.

VOCAB[lang][canonical_key] = localized unit word (as displayed after "100 ").
RARENOTES[lang] = short "no longer minted" phrase (used for JPY/KRW/LAK)."""

VOCAB = {
 "ms": {
  "cents": "sen", "eur": "sen", "pence": "pence", "sen": "sen",
  "kurus": "kuruş", "jiao": "jiao", "fen": "fen", "jeon": "jeon",
  "rappen": "rappen", "paisa": "paisa", "centavo": "centavo",
  "kopek": "kopek", "kopiyok": "kopiyok", "halala": "halala",
  "fils": "fils", "ore": "öre", "satang": "satang", "hao": "hào",
  "xu": "xu", "att": "att", "poisha": "poisha", "kobo": "kobo",
  "piastre": "piastre", "groszy": "groszy", "haler": "haler",
  "agora": "agora", "dirham": "dirham",
 },
 "vi": {
  "cents": "xu", "eur": "cent", "pence": "pence", "sen": "sen",
  "kurus": "kuruş", "jiao": "hào", "fen": "phân", "jeon": "jeon",
  "rappen": "rappen", "paisa": "paisa", "centavo": "centavo",
  "kopek": "kopek", "kopiyok": "kopiyok", "halala": "halala",
  "fils": "fils", "ore": "ore", "satang": "xatang", "hao": "hào",
  "xu": "xu", "att": "att", "poisha": "poisha", "kobo": "kobo",
  "piastre": "piastre", "groszy": "groszy", "haler": "haler",
  "agora": "agora", "dirham": "dirham",
 },
 "th": {
  "cents": "เซนต์", "eur": "เซนต์", "pence": "เพนซ์", "sen": "เซน",
  "kurus": "กูรุช", "jiao": "เจียว", "fen": "เฟิน", "jeon": "ชอน",
  "rappen": "แรปเพน", "paisa": "ไปซา", "centavo": "เซนตาโว",
  "kopek": "คอปเปก", "kopiyok": "คอปปี้", "halala": "ฮาลาลา",
  "fils": "ฟิลส์", "ore": "เออเรอ", "satang": "สตางค์", "hao": "ฮ่าว",
  "xu": "ซู", "att": "อัต", "poisha": "โปยชา", "kobo": "โกโบ",
  "piastre": "เพียสเตอร์", "groszy": "กรอสซี", "haler": "ฮาเลอร์",
  "agora": "อโกรา", "dirham": "ดิร์แฮม",
 },
 "tl": {
  "cents": "sentimo", "eur": "sentimo", "pence": "pence", "sen": "sen",
  "kurus": "kuruş", "jiao": "jiao", "fen": "fen", "jeon": "jeon",
  "rappen": "rappen", "paisa": "paisa", "centavo": "sentimo",
  "kopek": "kopeck", "kopiyok": "kopiyok", "halala": "halala",
  "fils": "fils", "ore": "ore", "satang": "satang", "hao": "hào",
  "xu": "xu", "att": "att", "poisha": "poysha", "kobo": "kobo",
  "piastre": "piastre", "groszy": "grosz", "haler": "haler",
  "agora": "agora", "dirham": "dirham",
 },
 "ja": {
  "cents": "セント", "eur": "ユーロセント", "pence": "ペンス", "sen": "セン",
  "kurus": "クルシュ", "jiao": "ジャオ", "fen": "フェン", "jeon": "ジョン",
  "rappen": "ラッペン", "paisa": "パイサ", "centavo": "センタボ",
  "kopek": "コペイカ", "kopiyok": "コピーカ", "halala": "ハララ",
  "fils": "フィルス", "ore": "エーレ", "satang": "サタン", "hao": "ハオ",
  "xu": "スー", "att": "アット", "poisha": "ポイシャ", "kobo": "コボ",
  "piastre": "ピアストル", "groszy": "グロス", "haler": "ハレーシュ",
  "agora": "アゴラ", "dirham": "ディルハム",
 },
}

RARENOTES = {
 "ms": "tidak lagi digunakan",
 "vi": "không còn được sử dụng",
 "th": "ไม่มีการใช้แล้ว",
 "tl": "hindi na ginagamit",
 "ja": "現在は使われていない",
}