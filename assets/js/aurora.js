/* ============================================================================
   aurora.js — Aurora experience layer (loaded AFTER main.js)
   Augments the existing site interactions. Does NOT re-run reveals / counters /
   tilt / spotlight (main.js owns those). Adds:
     • Three.js 3D particle hero, injected into the page hero
     • Custom trailing cursor (fine pointers only)
     • Magnetic primary buttons
     • GSAP hero parallax on scroll (if GSAP is present)
   All gated on prefers-reduced-motion + graceful if a CDN lib fails to load.
   ============================================================================ */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(pointer:fine)").matches && !reduce;
  var hasGSAP = typeof window.gsap !== "undefined";
  var hasTHREE = typeof window.THREE !== "undefined";

  /* ---------- Custom cursor ---------- */
  if (fine) {
    var de = document.documentElement;
    de.classList.add("aurora-cursor");
    var ring = document.createElement("div"); ring.className = "cur-ring";
    var dot = document.createElement("div"); dot.className = "cur-dot";
    document.body.appendChild(ring); document.body.appendChild(dot);
    var mx = 0, my = 0, rx = 0, ry = 0;
    window.addEventListener("pointermove", function (e) {
      mx = e.clientX; my = e.clientY;
      dot.style.transform = "translate(" + mx + "px," + my + "px)";
    }, { passive: true });
    (function loop() { rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18; ring.style.transform = "translate(" + rx + "px," + ry + "px)"; requestAnimationFrame(loop); })();
    var hot = function (on) { return function () { ring.classList.toggle("hot", on); }; };
    document.querySelectorAll("a,button,.card,.mini,.prop,.post,.gp,.member,input,textarea,select").forEach(function (el) {
      el.addEventListener("mouseenter", hot(true));
      el.addEventListener("mouseleave", hot(false));
    });
  }

  /* ---------- Magnetic buttons ---------- */
  if (fine) {
    document.querySelectorAll(".btn-primary,.btn-outline,.btn-lg").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.3;
        var y = (e.clientY - r.top - r.height / 2) * 0.4;
        el.style.transform = "translate(" + x + "px," + y + "px)";
      });
      el.addEventListener("pointerleave", function () { el.style.transform = ""; });
    });
  }

  /* ---------- Three.js particle hero ---------- */
  function dotTexture() {
    var c = document.createElement("canvas"); c.width = c.height = 64;
    var g = c.getContext("2d");
    var grd = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    grd.addColorStop(0, "rgba(255,255,255,1)"); grd.addColorStop(0.3, "rgba(255,255,255,0.85)"); grd.addColorStop(1, "rgba(255,255,255,0)");
    g.fillStyle = grd; g.fillRect(0, 0, 64, 64);
    return new THREE.CanvasTexture(c);
  }

  function initHero(hero) {
    var canvas = document.createElement("canvas");
    canvas.className = "aurora-canvas";
    hero.insertBefore(canvas, hero.firstChild);

    var W = hero.clientWidth || window.innerWidth, H = hero.clientHeight || 600;
    var scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x050C1A, 0.02);
    var camera = new THREE.PerspectiveCamera(60, W / H, 0.1, 120);
    camera.position.z = 30;
    var renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(W, H, false);

    var COUNT = 2300, R = 13;
    var pos = new Float32Array(COUNT * 3), col = new Float32Array(COUNT * 3);
    var blue = new THREE.Color(0x00D4FF), gold = new THREE.Color(0xFFB800), orange = new THREE.Color(0xFF6B2B);
    var GA = Math.PI * (3 - Math.sqrt(5));
    for (var i = 0; i < COUNT; i++) {
      var y = 1 - (i / (COUNT - 1)) * 2;
      var rad = Math.sqrt(1 - y * y);
      var th = GA * i;
      var jit = 0.86 + (((i * 73) % 100) / 100) * 0.3;
      var rr = R * jit;
      pos[i * 3] = Math.cos(th) * rad * rr;
      pos[i * 3 + 1] = y * rr;
      pos[i * 3 + 2] = Math.sin(th) * rad * rr;
      var t = (y + 1) / 2;
      var c = blue.clone().lerp(gold, t);
      if (((i * 37) % 100) < 6) c = orange.clone();
      col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b;
    }
    var geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    geo.setAttribute("color", new THREE.BufferAttribute(col, 3));
    var mat = new THREE.PointsMaterial({ size: 0.26, map: dotTexture(), vertexColors: true, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, sizeAttenuation: true });
    var points = new THREE.Points(geo, mat);
    scene.add(points);

    requestAnimationFrame(function () { canvas.classList.add("in"); });

    var tmx = 0, tmy = 0, cmx = 0, cmy = 0;
    window.addEventListener("pointermove", function (e) { tmx = e.clientX / window.innerWidth - 0.5; tmy = e.clientY / window.innerHeight - 0.5; }, { passive: true });

    var running = true, raf = null, t0 = (window.performance && performance.now ? performance.now() : 0);
    function frame(now) {
      if (!running) return;
      raf = requestAnimationFrame(frame);
      var t = ((now || 0) - t0) / 1000;
      points.rotation.y += 0.0016;
      points.rotation.x = Math.sin(t * 0.14) * 0.09;
      cmx += (tmx - cmx) * 0.04; cmy += (tmy - cmy) * 0.04;
      camera.position.x = cmx * 8; camera.position.y = -cmy * 8;
      camera.lookAt(0, 0, 0);
      renderer.render(scene, camera);
    }
    function start() { if (!raf) raf = requestAnimationFrame(frame); running = true; }
    function stop() { running = false; if (raf) { cancelAnimationFrame(raf); raf = null; } }
    raf = requestAnimationFrame(frame);

    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) start(); else stop(); }); }, { threshold: 0.02 }).observe(canvas);
    }
    document.addEventListener("visibilitychange", function () { if (document.hidden) stop(); else start(); });
    window.addEventListener("resize", function () {
      W = hero.clientWidth || window.innerWidth; H = hero.clientHeight || 600;
      camera.aspect = W / H; camera.updateProjectionMatrix(); renderer.setSize(W, H, false);
    });

    /* GSAP hero parallax */
    if (hasGSAP && window.ScrollTrigger) {
      gsap.registerPlugin(ScrollTrigger);
      var content = hero.querySelector(".container");
      if (content) {
        gsap.to(content, { yPercent: 16, opacity: 0.35, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
      }
      gsap.to(canvas, { yPercent: 12, ease: "none", scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true } });
    }
  }

  if (hasTHREE && !reduce) {
    var hero = document.querySelector(".hero");  // 3D sphere = homepage signature only; inner pages use SVG motifs
    if (hero) { try { initHero(hero); } catch (e) { /* WebGL unavailable → dimmed image + glow fallback remains */ } }
  }

  /* ---------- Hero entrance choreography (sequenced, not all-at-once) ---------- */
  if (hasGSAP && !reduce) {
    var heroEl = document.querySelector(".hero, .page-hero");
    if (heroEl) {
      var isPageHero = heroEl.classList.contains("page-hero");
      var seq = [];
      var pick = function (sel) { return heroEl.querySelector(sel); };
      // .hero h1 is word-split by main.js; only sequence the page-hero h1 here.
      [".crumb", ".eyebrow", isPageHero ? "h1" : null, ".lead", ".dek", ".hero-cta", ".hero-trust"]
        .forEach(function (s) { var el = s && pick(s); if (el) seq.push(el); });
      if (seq.length) {
        var tl = gsap.timeline({ defaults: { ease: "power3.out" }, delay: 0.1 });
        tl.from(seq, { opacity: 0, y: 18, duration: 0.7, stagger: 0.11 });
      }
    }
  }

  /* ---------- v3 section animations (bento, vertical timeline, pipeline) ---------- */
  if (hasGSAP && !reduce) {
    gsap.registerPlugin(ScrollTrigger);
    document.querySelectorAll(".svc-bento").forEach(function (grid) {
      gsap.from(grid.children, { opacity: 0, y: 26, duration: 0.7, ease: "power3.out", stagger: 0.07, scrollTrigger: { trigger: grid, start: "top 85%" } });
    });
    document.querySelectorAll(".vstep").forEach(function (st) {
      gsap.from(st, { opacity: 0, y: 24, duration: 0.7, ease: "power3.out", scrollTrigger: { trigger: st, start: "top 88%" } });
    });
    document.querySelectorAll(".vtl").forEach(function (vtl) {
      var fill = vtl.querySelector(".vfill");
      if (fill) gsap.fromTo(fill, { scaleY: 0 }, { scaleY: 1, ease: "none", scrollTrigger: { trigger: vtl, start: "top 72%", end: "bottom 78%", scrub: true } });
    });
    document.querySelectorAll(".pipeline").forEach(function (pl) {
      gsap.from(pl, { opacity: 0, y: 24, duration: 0.9, ease: "power3.out", scrollTrigger: { trigger: pl, start: "top 85%" } });
    });
  }
})();
