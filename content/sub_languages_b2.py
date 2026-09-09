# -*- coding: utf-8 -*-
"""Per-language minor-unit vocabularies. See content/sub_l10n.py.

VOCAB[lang][canonical_key] = localized unit word (as displayed after "100 ").
RARENOTES[lang] = short "no longer minted" phrase (used for JPY/KRW/LAK)."""

VOCAB = {
 "ru": {
  "cents": "центов", "eur": "евроцентов", "pence": "пенсов",
  "sen": "сенов", "kurus": "курушей", "jiao": "цзяо",
  "fen": "фэнь", "jeon": "чон",
  "rappen": "раппенов", "paisa": "пайса", "centavo": "сентаво",
  "kopek": "копеек", "kopiyok": "копеек", "halala": "халала",
  "fils": "филс", "ore": "эре", "satang": "сатанг", "hao": "хао",
  "xu": "су", "att": "ат", "poisha": "пойша", "kobo": "кобо",
  "piastre": "пиастров", "groszy": "грошей", "haler": "геллеров",
  "agora": "агора", "dirham": "дирхам",
 },
 "uk": {
  "cents": "центів", "eur": "євроцентів", "pence": "пенсів",
  "sen": "сенів", "kurus": "курушів", "jiao": "цзяо",
  "fen": "фень", "jeon": "чонів",
  "rappen": "раппенів", "paisa": "пайсів", "centavo": "сентаво",
  "kopek": "копійок", "kopiyok": "копійок", "halala": "халала",
  "fils": "філ", "ore": "ере", "satang": "сатанг", "hao": "хао",
  "xu": "су", "att": "ат", "poisha": "пойша", "kobo": "кобо",
  "piastre": "піастрів", "groszy": "грошей", "haler": "галерів",
  "agora": "агора", "dirham": "дирхамів",
 },
 "tr": {
  "cents": "sent", "eur": "sent", "pence": "pence",
  "sen": "sen", "kurus": "kuruş", "jiao": "jiao",
  "fen": "fen", "jeon": "jeon",
  "rappen": "rappen", "paisa": "paisa", "centavo": "centavo",
  "kopek": "kopek", "kopiyok": "kopek", "halala": "halala",
  "fils": "fil", "ore": "ore", "satang": "satang", "hao": "hao",
  "xu": "xu", "att": "at", "poisha": "poisha", "kobo": "kobo",
  "piastre": "piastre", "groszy": "grosz", "haler": "haler",
  "agora": "agora", "dirham": "dirhem",
 },
 "pl": {
  "cents": "centów", "eur": "eurocentów", "pence": "pensów",
  "sen": "senów", "kurus": "kuruşów", "jiao": "jiao",
  "fen": "fen", "jeon": "jeon",
  "rappen": "rappen", "paisa": "paisa", "centavo": "centavo",
  "kopek": "kopiejek", "kopiyok": "kopiejek", "halala": "halala",
  "fils": "fils", "ore": "ore", "satang": "satang", "hao": "hao",
  "xu": "xu", "att": "att", "poisha": "poisha", "kobo": "kobo",
  "piastre": "piastrów", "groszy": "groszy", "haler": "halerzy",
  "agora": "agorot", "dirham": "dirhamów",
 },
 "cs": {
  "cents": "centů", "eur": "eurocentů", "pence": "pencí",
  "sen": "senů", "kurus": "kurušů", "jiao": "jiao",
  "fen": "fen", "jeon": "jeon",
  "rappen": "rappen", "paisa": "paisa", "centavo": "centavo",
  "kopek": "kopejek", "kopiyok": "kopejek", "halala": "halala",
  "fils": "fils", "ore": "ore", "satang": "satang", "hao": "hao",
  "xu": "xu", "att": "att", "poisha": "poisha", "kobo": "kobo",
  "piastre": "piastr", "groszy": "grosz", "haler": "haléřů",
  "agora": "agorot", "dirham": "dirhamů",
 },
}
RARENOTES = {
 "ru": "больше не выпускаются",
 "uk": "більше не випускаються",
 "tr": "artık basılmıyor",
 "pl": "już nie są wybijane",
 "cs": "již se nerazí",
}