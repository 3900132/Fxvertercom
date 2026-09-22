/**
 * creem-worker.js — Cloudflare Worker：Creem 支付 → 支持者名单自动化
 *
 * ── 工作原理 ─────────────────────────────────────────────────────
 * 1. POST /creem-webhook  Creem 支付成功后推送事件到这里，
 *    Worker 记录"该邮箱已付费"（30 天有效）。
 * 2. POST /claim          支持者在支持页表单里填支付邮箱 + 展示名，
 *    Worker 核对确有付费记录后，把名字写进公开名单（防冒领）。
 * 3. GET  /supporters     公开名单 JSON。把这个地址填到
 *    build-lang-pages.py 的 SUPPORTERS_API 并重新构建，
 *    支持页的名单墙就会自动从这个接口渲染。
 *
 * ── 部署步骤 ─────────────────────────────────────────────────────
 * 1. Cloudflare Dashboard → Workers & Pages → Create Worker，
 *    把本文件全部粘贴进去。
 * 2. Worker → Settings → Bindings：新建 KV namespace，绑定变量名 KV。
 * 3. Worker → Settings → Variables 添加：
 *      CREEM_WEBHOOK_SECRET = Creem 后台 Webhook 设置里的签名密钥
 *      ALLOWED_ORIGIN       = https://fxverter.com
 * 4. Creem 后台 → Developers/Webhooks：新建 Webhook，
 *    URL 填 https://<你的worker域名>/creem-webhook，
 *    订阅 payment.succeeded / checkout.completed 事件。
 * 5. Creem 后台创建 3 个产品（对应支持页三档），把 checkout 链接
 *    粘贴到 content/trust_l10n.py 的 TRUST_OVERRIDES["support"][lang]
 *    ["tiers"] 每档第三个元素，重新构建站点。
 * 6. 把 https://<你的worker域名>/supporters 填到
 *    build-lang-pages.py 的 SUPPORTERS_API，重新构建。
 */

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const cors = {
      "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN || "*",
      "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };
    if (req.method === "OPTIONS") return new Response(null, { headers: cors });

    // ── 1. Creem webhook：记录已付费邮箱 ──
    if (url.pathname === "/creem-webhook" && req.method === "POST") {
      const raw = await req.text();
      // 签名校验：以 Creem 后台为准（Webhook 设置页会给出签名方式/密钥）。
      // 上线前务必按官方文档补上校验，此处先保留原始 body 供校验使用。
      // const expected = await hmacHex(env.CREEM_WEBHOOK_SECRET, raw);
      // if (req.headers.get("x-creem-signature") !== expected) return new Response("bad signature", { status: 401 });
      let evt;
      try { evt = JSON.parse(raw); } catch { return new Response("bad json", { status: 400 }); }
      const type = evt.eventType || evt.type || "";
      if (!/succeeded|completed|paid/i.test(type)) return new Response("ignored", { headers: cors });
      const data = evt.data || evt;
      const cust = data.customer || evt.customer || {};
      const order = data.order || evt.order || {};
      const email = String(cust.email || "").toLowerCase().trim();
      if (!email) return new Response("no email", { status: 400, headers: cors });
      const dedupeId = String(evt.id || order.id || crypto.randomUUID());
      if (await env.KV.get("evt:" + dedupeId)) return new Response("dup", { headers: cors });
      await env.KV.put("evt:" + dedupeId, "1", { expirationTtl: 60 * 60 * 24 * 7 });
      await env.KV.put("paid:" + email, JSON.stringify({
        orderId: order.id || "",
        product: order.productName || order.product_name || "",
        ts: Date.now(),
      }), { expirationTtl: 60 * 60 * 24 * 30 }); // 30 天内可认领
      return new Response("ok", { headers: cors });
    }

    // ── 2. 支持者认领：核对付费记录后上榜 ──
    if (url.pathname === "/claim" && req.method === "POST") {
      const b = await req.json().catch(() => ({}));
      const email = String(b.email || "").toLowerCase().trim();
      if (!email) return json({ ok: false, error: "need-email" }, 400, cors);
      const paidRaw = await env.KV.get("paid:" + email);
      if (!paidRaw) return json({ ok: false, error: "no-paid-order" }, 403, cors);
      if (await env.KV.get("claimed:" + email)) return json({ ok: false, error: "already-claimed" }, 409, cors);
      const paid = JSON.parse(paidRaw);
      const name = String(b.displayName || "").trim().slice(0, 40);
      const rec = {
        name: b.anonymous ? null : (name || null),
        message: String(b.message || "").trim().slice(0, 120) || null,
        tier: paid.product || null,
        ts: Date.now(),
      };
      await env.KV.put("claimed:" + email, "1", { expirationTtl: 60 * 60 * 24 * 30 });
      const list = JSON.parse((await env.KV.get("supporters")) || "[]");
      list.unshift(rec);
      await env.KV.put("supporters", JSON.stringify(list.slice(0, 200)));
      return json({ ok: true }, 200, cors);
    }

    // ── 3. 公开名单 JSON ──
    if (url.pathname === "/supporters" && req.method === "GET") {
      const list = JSON.parse((await env.KV.get("supporters")) || "[]");
      return new Response(JSON.stringify(list), {
        headers: { ...cors, "Content-Type": "application/json", "Cache-Control": "public, max-age=300" },
      });
    }

    return new Response("not found", { status: 404, headers: cors });
  },
};

function json(obj, status, cors) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...cors, "Content-Type": "application/json" },
  });
}
