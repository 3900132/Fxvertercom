/* FX Currency Converter — service worker
   Strategy:
   - App shell (same-origin pages/assets): stale-while-revalidate, works offline
   - Rate APIs (frankfurter / exchangerate-api / jsdelivr): network-first,
     falls back to the last cached response so the last known rates stay
     available offline
*/
const CACHE = 'fxcc-v6';
const CORE = [
  './',
  './manifest.webmanifest',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png',
  './og-image.png'
];
const API_HOSTS = ['api.frankfurter.dev', 'api.exchangerate-api.com', 'cdn.jsdelivr.net'];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((cache) =>
      Promise.all(CORE.map((u) => cache.add(u).catch(() => {})))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // rate APIs: network-first, fall back to the last cached response when offline
  if (API_HOSTS.includes(url.hostname)) {
    e.respondWith(
      fetch(req).then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => caches.match(req))
    );
    return;
  }

  // same-origin app shell: stale-while-revalidate
  if (url.origin === location.origin) {
    e.respondWith(
      caches.open(CACHE).then(async (cache) => {
        const cached = await cache.match(req);
        const network = fetch(req).then((res) => {
          if (res && res.ok) cache.put(req, res.clone());
          return res;
        }).catch(() => cached);
        return cached || network;
      })
    );
  }
});
