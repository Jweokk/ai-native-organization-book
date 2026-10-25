/*! shelf-counter — fly2ai 书站页脚：本站访问计数 + 整本 PDF 下载计数
 *  后端 https://counter.fly2ai.top （自建，纯标准库；多站共用一套）
 *  站点改动只有两处：SITE / PDF 两个常量。后端不可用时静默隐藏，不影响站点任何功能。
 *  统计口径：每次页面加载记 1 次访问（同 IP 同页 2 秒防抖），独立访客按 IP 加盐哈希去重，
 *  PDF 计数按「点击下载链接」计（sendBeacon，不阻塞跳转，随后再回读一次权威数字）。
 */
(function () {
  "use strict";

  var SITE = "aiorg";          // 站点白名单里的 id
  var PDF = "ai-native-organization.pdf";            // 页脚展示下载数的「整本 PDF」文件名；留空则不展示
  var API = "https://counter.fly2ai.top";
  var mounted = false;
  var state = null;

  function fmt(n) {
    return (n || 0).toLocaleString("zh-CN");
  }

  function host() {
    return (
      document.querySelector(".md-footer-meta__inner") ||
      document.querySelector(".md-footer") ||
      document.querySelector(".copyright") ||
      null
    );
  }

  function slot() {
    var h = host();
    if (!h) return null;
    var el = h.querySelector(".shelf-counter-stats");
    if (el) return el;
    el = document.createElement("div");
    el.className = "shelf-counter-stats";
    el.style.cssText =
      "flex:1 1 100%;width:100%;margin-top:.5rem;font-size:.7rem;" +
      "line-height:1.6;opacity:.75;font-weight:400";
    el.hidden = true;
    h.appendChild(el);
    return el;
  }

  function render(data) {
    var el = slot();
    if (!el || !data) return;
    state = data;
    var parts = [
      "👁 本站访问 " + fmt(data.views) + " 次",
      "独立访客 " + fmt(data.visitors) + " 人"
    ];
    if (PDF) {
      parts.push("📥 整本 PDF 下载 " + fmt((data.downloads || {})[PDF]) + " 次");
    }
    el.textContent = parts.join(" · ");
    el.hidden = false;
  }

  function post(url, body) {
    try {
      return fetch(url, {
        method: "POST",
        body: JSON.stringify(body),
        keepalive: true,
        mode: "cors"
      }).then(function (r) {
        return r.ok ? r.json() : null;
      });
    } catch (e) {
      return Promise.resolve(null);
    }
  }

  function refresh() {
    try {
      fetch(API + "/api/site?site=" + SITE + "&t=" + Date.now(), { mode: "cors" })
        .then(function (r) {
          return r.ok ? r.json() : null;
        })
        .then(render)
        .catch(function () {});
    } catch (e) {
      /* 静默 */
    }
  }

  function watchDownloads() {
    document.addEventListener(
      "click",
      function (ev) {
        var a = ev.target && ev.target.closest ? ev.target.closest("a[href]") : null;
        if (!a) return;
        var href = a.getAttribute("href") || "";
        if (!/\.pdf($|[?#])/i.test(href)) return;
        var file = href.split("?")[0].split("#")[0].split("/").pop();
        if (!file) return;
        var body = { site: SITE, file: file, href: a.href };
        try {
          // sendBeacon 用的是 text/plain（CORS 安全列表内），不触发预检、不阻塞跳转
          if (!navigator.sendBeacon || !navigator.sendBeacon(API + "/api/download", JSON.stringify(body))) {
            post(API + "/api/download", body);
          }
        } catch (e) {
          /* 统计失败不影响下载 */
        }
        // 页脚立刻 +1（感觉即时），1.5 秒后再回读一次后端权威数字（页面若已跳走就算了）
        if (state && PDF && file === PDF) {
          var optimistic = JSON.parse(JSON.stringify(state));
          optimistic.downloads = optimistic.downloads || {};
          optimistic.downloads[file] = (optimistic.downloads[file] || 0) + 1;
          render(optimistic);
        }
        window.setTimeout(refresh, 1500);
      },
      true
    );
  }

  function mount() {
    if (mounted) return;
    mounted = true;
    slot();
    watchDownloads();
    post(API + "/api/hit", {
      site: SITE,
      path: location.pathname,
      lang: (navigator.language || "").slice(0, 8),
      screen: window.innerWidth + "x" + window.innerHeight
    })
      .then(render)
      .catch(function () {});
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
