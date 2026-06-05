/* Ascendia — site interactions (vanilla, no deps) */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  // Sticky header shadow
  var header = document.getElementById("header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

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
        // close siblings
        li.parentElement.querySelectorAll(".has-menu.open").forEach(function (s) {
          if (s !== li) s.classList.remove("open");
        });
        li.classList.toggle("open", !wasOpen);
      }
    });
  });
  // Close drawer when a real link is tapped
  if (links) {
    links.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (a && !a.classList.contains("nav-top")) links.classList.remove("open");
    });
  }

  // Scroll reveal
  var reveals = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && reveals.length) {
    reveals.forEach(function (el) { el.classList.add("reveal"); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  // Lead form (demo handler — wire to Formspree/Firebase before launch)
  document.querySelectorAll("form[data-lead]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = form.querySelector("[type=email]");
      var name = form.querySelector("[name=name]");
      if (!name.value.trim() || !email.value.trim() || !/.+@.+\..+/.test(email.value)) {
        (name.value.trim() ? email : name).focus(); return;
      }
      form.innerHTML =
        '<h3>Thank you — we\'ll be in touch.</h3>' +
        '<p class="muted">We\'ve received your request and will reply within one business day. ' +
        'Reach us anytime at <a href="mailto:hello@ascendia.ai">hello@ascendia.ai</a>.</p>' +
        '<p class="form-note">Demo form — connect to Formspree or Firebase to deliver submissions.</p>';
    });
  });
})();
