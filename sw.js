// AI Creator Academy – service worker. Network first: online loads the latest lessons; offline uses the saved copy.
const VERSION = "6.6.0";
const CACHE = "ai-creator-academy-" + VERSION;
const SHELL = ["./", "./index.html", "./courses.json", "./curriculum-business.json", "./curriculum-creator.json", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png", "./apple-touch-icon.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith("ai-creator-academy-") && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const req = e.request; if (req.method !== "GET") return;
  const url = new URL(req.url);
  const inScope = url.origin === self.location.origin && url.pathname.startsWith(new URL("./", self.location).pathname);
  const isFont = url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com";
  if (!inScope && !isFont) return;
  e.respondWith(fetch(req).then(res => {
    if (res && (res.ok || res.type === "opaque")) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
    return res;
  }).catch(() => caches.open(CACHE).then(c => c.match(req, {ignoreSearch: true})).then(r => r || (req.mode === "navigate" ? caches.open(CACHE).then(c => c.match("./index.html")) : new Response("Risorsa non disponibile offline", {status:503})))));
});
