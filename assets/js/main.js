/* Avanciers Digital — site interactions (vanilla, no deps) */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Scroll progress bar (injected, styled in CSS)
  var bar = document.createElement("div");
  bar.className = "scroll-progress";
  document.body.appendChild(bar);

  // Sticky header shadow + progress width
  var header = document.getElementById("header");
  var onScroll = function () {
    if (header) header.classList.toggle("scrolled", window.scrollY > 8);
    var max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + "%";
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile drawer toggle
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () { links.classList.toggle("open"); });
  }

  // Dropdown behaviour: hover on desktop (CSS), click-to-accordion on mobile
  var isMobile = function () { return window.matchMedia("(max-width:900px)").matches; };
  document.querySelectorAll(".has-menu > .nav-top").forEach(function (top) {
    top.addEventListener("click", function (e) {
      if (isMobile()) {
        e.preventDefault();
        var li = top.parentElement;
        var wasOpen = li.classList.contains("open");
        li.parentElement.querySelectorAll(".has-menu.open").forEach(function (s) {
          if (s !== li) s.classList.remove("open");
        });
        li.classList.toggle("open", !wasOpen);
      }
    });
  });
  if (links) {
    links.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (a && !a.classList.contains("nav-top")) links.classList.remove("open");
    });
  }

  // Scroll reveal with per-child stagger
  var reveals = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && reveals.length) {
    reveals.forEach(function (el) {
      el.classList.add("reveal");
      el.querySelectorAll(".card,.mini,.prop,.post,.gp,.member,.step").forEach(function (child, i) {
        child.style.setProperty("--i", i);
      });
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  // Count-up numbers ([data-count])
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    var fmt = function (n) { return n >= 1000 ? n.toLocaleString("en-US") : String(n); };
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        cio.unobserve(en.target);
        var el = en.target, target = parseInt(el.getAttribute("data-count"), 10) || 0;
        if (reduceMotion) { el.textContent = fmt(target); return; }
        var t0 = null, dur = 1200;
        var tick = function (t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
          el.textContent = fmt(Math.round(target * e));
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  // Card spotlight — pointer-tracked glow (delegated)
  document.addEventListener("pointermove", function (e) {
    var t = e.target.closest && e.target.closest(".card,.mini,.prop,.post");
    if (!t) return;
    var r = t.getBoundingClientRect();
    t.style.setProperty("--mx", (e.clientX - r.left) + "px");
    t.style.setProperty("--my", (e.clientY - r.top) + "px");
  }, { passive: true });

  // Hero particle mesh (homepage only; static frame under reduced motion)
  var canvas = document.getElementById("mesh");
  if (canvas && canvas.getContext) {
    var ctx = canvas.getContext("2d");
    var w, h, dpr, nodes = [], raf;
    var resize = function () {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      var r = canvas.parentElement.getBoundingClientRect();
      w = r.width; h = r.height;
      canvas.width = w * dpr; canvas.height = h * dpr;
      canvas.style.width = w + "px"; canvas.style.height = h + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var count = Math.max(22, Math.min(56, Math.floor((w * h) / 26000)));
      nodes = [];
      for (var i = 0; i < count; i++) nodes.push({
        x: Math.random() * w, y: Math.random() * h,
        vx: (Math.random() - .5) * .18, vy: (Math.random() - .5) * .18,
        a: Math.random() < .16
      });
    };
    var frame = function () {
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        a.x += a.vx; a.y += a.vy;
        if (a.x < 0 || a.x > w) a.vx *= -1;
        if (a.y < 0 || a.y > h) a.vy *= -1;
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = Math.hypot(dx, dy);
          if (d < 130) {
            ctx.globalAlpha = (1 - d / 130) * .18;
            ctx.strokeStyle = "#7fb2e8";
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
          }
        }
      }
      for (var k = 0; k < nodes.length; k++) {
        var n = nodes[k];
        ctx.globalAlpha = n.a ? .95 : .5;
        ctx.fillStyle = n.a ? "#e97451" : "#9cc1ea";
        ctx.beginPath(); ctx.arc(n.x, n.y, n.a ? 2.1 : 1.4, 0, 7); ctx.fill();
      }
      ctx.globalAlpha = 1;
      if (!reduceMotion) raf = requestAnimationFrame(frame);
    };
    var start = function () { if (raf) cancelAnimationFrame(raf); resize(); frame(); };
    var rto;
    window.addEventListener("resize", function () { clearTimeout(rto); rto = setTimeout(start, 160); });
    start();
  }

  // Hero headline — word-by-word entrance (progressive enhancement)
  var h1 = document.querySelector(".hero h1");
  if (h1 && !reduceMotion) {
    var parts = [];
    h1.childNodes.forEach(function (n) {
      if (n.nodeType === 3) {
        n.textContent.split(/\s+/).forEach(function (w) { if (w) parts.push('<span class="w">' + w + "</span>"); });
      } else if (n.nodeType === 1) {
        if (n.classList && n.classList.contains("rot")) {
          parts.push('<span class="w">' + n.outerHTML + "</span>");
        } else {
          var cls = n.className || "";
          n.textContent.split(/\s+/).forEach(function (w) { if (w) parts.push('<span class="w ' + cls + '">' + w + "</span>"); });
        }
      }
    });
    if (parts.length) {
      h1.innerHTML = parts.join(" ");
      h1.querySelectorAll(".w").forEach(function (w, i) { w.style.animationDelay = (90 * i) + "ms"; });
      h1.classList.add("split");
    }
  }

  // 3D tilt on feature surfaces
  if (!reduceMotion) {
    document.querySelectorAll(".bento .mini:first-child,.case--feature,.mr-media").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        var rx = ((e.clientY - r.top) / r.height - .5) * -5;
        var ry = ((e.clientX - r.left) / r.width - .5) * 6;
        el.style.transform = "perspective(900px) rotateX(" + rx.toFixed(2) + "deg) rotateY(" + ry.toFixed(2) + "deg)";
      });
      el.addEventListener("pointerleave", function () { el.style.transform = ""; });
    });
  }

  // Lead form. If FORM_ENDPOINT is set (e.g. a Formspree URL) we POST via fetch and
  // confirm success only on a 2xx. Otherwise we fall back to a mailto compose with
  // HONEST copy — we must not claim "sent" when we only opened the visitor's mail app.
  var FORM_ENDPOINT = "";  // ← set to your Formspree endpoint, e.g. "https://formspree.io/f/xxxxxxx", to capture leads server-side
  var CONTACT_EMAIL = "";  // ← TODO: branded email e.g. "hello@avanciersdigital.com" — enables the mailto fallback
  document.querySelectorAll("form[data-lead]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var val = function (n) { var el = form.querySelector("[name=" + n + "]"); return el ? el.value.trim() : ""; };
      var email = form.querySelector("[type=email]"), name = form.querySelector("[name=name]");
      if (!name.value.trim() || !email.value.trim() || !/.+@.+\..+/.test(email.value)) {
        (name.value.trim() ? email : name).focus(); return;
      }
      var consent = form.querySelector("[name=consent]");  // form is novalidate, so enforce consent in JS
      if (consent && !consent.checked) { consent.focus(); return; }
      var ok = function () {
        form.innerHTML = '<h3>Thank you — we\'ve got it.</h3>' +
          '<p class="muted">Your request is in. We reply within one business day at the email you gave us.</p>';
      };
      var fallback = function () {
        if (CONTACT_EMAIL) {
          var subject = "Consultation request — " + (val("company") || val("name"));
          var body = "Name: " + val("name") + "\nWork email: " + val("email") + "\nCompany: " + val("company") +
                     "\nPhone: " + val("phone") + "\nInterested in: " + val("interest") + "\n\n" + val("msg");
          window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
          form.innerHTML = '<h3>Opening your email app…</h3>' +
            '<p class="muted">Your request is pre-filled in your mail app — press send to reach us. If nothing opened, email ' + CONTACT_EMAIL + '.</p>';
        } else {
          form.innerHTML = '<h3>Thanks for reaching out.</h3>' +
            '<p class="muted">Our contact inbox is being finalized — please check back shortly.</p>';
        }
      };
      if (FORM_ENDPOINT) {
        var btn = form.querySelector("button[type=submit]"); if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
        fetch(FORM_ENDPOINT, { method: "POST", headers: { "Accept": "application/json" }, body: new FormData(form) })
          .then(function (r) { r.ok ? ok() : fallback(); })
          .catch(fallback);
      } else {
        fallback();
      }
    });
  });
})();
