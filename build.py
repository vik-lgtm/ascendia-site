#!/usr/bin/env python3
"""
Ascendia static site generator.
One source of truth for the dropdown nav, header, footer and all page content.
Run:  python3 build.py      → regenerates every .html under site/
Edit content below (brand name, service copy, leadership) and re-run.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
BRAND = "Ascendia"
TAGLINE = ""
YEAR = "2026"

# ----------------------------------------------------------------------------
# CONTENT — services (from the Google Cloud Company Services strategy doc)
# ----------------------------------------------------------------------------
AGENTIC = [
    dict(slug="enterprise-ai-agents", name="Enterprise AI Agents", tag="Flagship",
        nav="Gemini agents that automate work across every department.",
        eyebrow="Flagship · agentic automation",
        intro="We design and deploy Gemini-powered AI agents that automate complex workflows, answer questions, analyze information and complete tasks across departments — with a human in the loop where it matters. Most clients begin with a focused 4–6 week pilot on one high-value workflow, then expand.",
        deliver=["Internal business assistants","Customer support agents","Sales and proposal agents","HR and onboarding agents","Finance and reporting agents","Operations and logistics agents","Document review & summarization agents","Multi-step workflow automation agents"],
        impact=["Reduce repetitive manual work","Improve response times","Instant access to company knowledge","Automate high-volume processes","Scalable AI support across the org"],
        steps=[("Scope","Pick one high-value workflow and the success metric."),("Build","Design the Gemini agent on Google Cloud."),("Integrate","Connect to your tools and data with guardrails."),("Launch","Go live with human-in-the-loop approvals."),("Expand","Measure ROI, then scale into managed services.")]),
    dict(slug="ai-knowledge-search", name="AI Knowledge Search & Enterprise Intelligence", tag="Knowledge",
        nav="Ask questions, get answers from approved company data.",
        eyebrow="Knowledge · enterprise search",
        intro="We turn scattered business information into intelligent, searchable knowledge systems powered by Google AI. Instead of hunting across emails, documents, drives and spreadsheets, teams ask questions and receive accurate, context-aware answers from approved company data.",
        deliver=["AI knowledge bases","Internal search assistants","Document intelligence systems","Company policy assistants","Research & reporting assistants","AI-powered intranet search","Knowledge systems connected to business data"],
        impact=["Make company knowledge easy to access","Reduce time spent searching","Improve internal decision-making","Preserve institutional knowledge","Greater speed and accuracy"],
        steps=[("Connect","Index approved sources securely."),("Ground","Build a retrieval layer on your data."),("Assist","Deploy the search and answer assistant."),("Govern","Set permissions and access controls."),("Adopt","Roll out and measure usage.")]),
    dict(slug="agentic-data-decision-intelligence", name="Agentic Data & Decision Intelligence", tag="Decisions",
        nav="From static dashboards to AI-powered decision systems.",
        eyebrow="Decisions · conversational BI",
        intro="We help businesses move from static dashboards to AI-powered decision systems. Using Google Cloud, BigQuery, Looker and Gemini, we build data platforms that let leaders ask natural-language questions, identify trends, detect inconsistencies, generate forecasts and receive decision-ready insights.",
        deliver=["AI-powered dashboards","Conversational business intelligence","Executive decision assistants","Predictive analytics systems","Sales & operations forecasting","Customer & market intelligence platforms","Automated reporting & insight generation"],
        impact=["Turn business data into clear decisions","Reduce dependency on manual reporting","Faster access to insights","Detect risks and opportunities earlier","A smarter, more responsive organization"],
        steps=[("Model","Unify data in BigQuery."),("Visualize","Build Looker dashboards."),("Converse","Add a Gemini ask-your-data layer."),("Predict","Forecasting and alerts."),("Operate","Automated insight delivery.")]),
    dict(slug="workspace-ai-transformation", name="Google Workspace AI Transformation", tag="Productivity",
        nav="Put Gemini to work across Gmail, Docs, Sheets and Meet.",
        eyebrow="Productivity · Gemini for Workspace",
        intro="We help companies transform daily work using Gemini across Google Workspace. We design practical AI workflows for Gmail, Docs, Sheets, Slides, Drive, Meet, Calendar and Chat so employees write faster, summarize information, analyze spreadsheets, prepare meetings and collaborate more effectively.",
        deliver=["AI productivity systems","Gmail & inbox automation","Meeting note & follow-up automation","AI document drafting workflows","Spreadsheet analysis workflows","Team collaboration systems","Workspace training & adoption programs"],
        impact=["Improve employee productivity","Reduce administrative workload","Accelerate communication & documentation","Standardize AI usage across teams","Help employees adopt AI safely"],
        steps=[("Assess","Map daily workflows."),("Design","Practical Gemini workflows."),("Pilot","Start with one team."),("Train","Run an adoption program."),("Scale","Org-wide rollout.")]),
    dict(slug="custom-gemini-applications", name="Custom Gemini Applications", tag="Custom",
        nav="Bespoke AI apps built on Google's AI and cloud.",
        eyebrow="Build · custom AI products",
        intro="We design and build custom AI applications on Google's AI and cloud ecosystem — from customer-facing AI tools to internal automation platforms, intelligent portals, recommendation engines and document-processing systems, including multimodal applications across text, images, audio and video.",
        deliver=["AI web applications","Customer-facing chatbots","Internal AI tools","AI-powered portals","Recommendation systems","Document processing platforms","Multimodal AI applications","Cloud-native apps on Google Cloud"],
        impact=["Launch AI products faster","Automate specialized workflows","Improve customer & employee experiences","Build scalable cloud-native systems","Create differentiated digital capabilities"],
        steps=[("Discover","Define the problem and users."),("Prototype","Validate fast on Vertex AI."),("Build","Cloud-native on Google Cloud."),("Harden","Security and evaluation."),("Launch","Ship and iterate.")]),
    dict(slug="ai-customer-experience", name="AI Customer Experience Automation", tag="Experience",
        nav="Faster, personalized, multilingual customer experiences.",
        eyebrow="Experience · customer AI",
        intro="We help companies build intelligent customer experiences using Google AI — from customer-service agents to personalized recommendations and multilingual support — so businesses respond faster, serve better and scale engagement across channels.",
        deliver=["AI customer service agents","Sales assistants","Multilingual support bots","Customer onboarding assistants","Personalized recommendation tools","Voice & chat support workflows","Customer insight & sentiment analysis"],
        impact=["Reduce support workload","Improve customer response times","Increase personalization","Support customers across channels & languages","More consistent experiences"],
        steps=[("Map","Customer journeys and intents."),("Design","Conversation and escalation flows."),("Build","Agents on Google AI."),("Connect","CRM and channels."),("Optimize","Measure CSAT and deflection.")]),
    dict(slug="secure-ai-adoption-governance", name="Secure AI Adoption & Governance", tag="Trust",
        nav="Adopt AI safely — governance, access control, oversight.",
        eyebrow="Trust · responsible AI",
        intro="We help organizations adopt AI safely, responsibly and at scale. Our approach covers security, access control, data governance, human-approval workflows, responsible-AI practices and enterprise-ready deployment standards — so you use AI confidently without losing control of sensitive data, systems or decisions. Our own compliance program targets ISO 42001 (AI management), ISO 27001, SOC 2 and GDPR.",
        deliver=["AI governance frameworks","Secure Gemini deployment plans","Access control & permission models","Human-in-the-loop approval workflows","AI usage policies","Cloud security foundations","Monitoring & compliance workflows"],
        impact=["Reduce AI adoption risk","Protect sensitive business data","Give leaders control over AI usage","Support responsible, compliant deployment","Build trust in enterprise AI"],
        steps=[("Assess","Risk and data review."),("Frame","Policies and guardrails."),("Control","Access and approvals."),("Monitor","Logging and compliance."),("Sustain","Ongoing governance.")]),
]

CLOUD_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>'
CHART_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><rect x="7" y="11" width="3" height="6"/><rect x="12" y="7" width="3" height="10"/><rect x="17" y="13" width="3" height="4"/></svg>'
GRID_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>'

CORE = [
    dict(slug="cloud-migration-modernization", name="Google Cloud Migration & Modernization", icon=CLOUD_ICON,
        nav="Move applications and workloads to Google Cloud.",
        eyebrow="Foundation · cloud", chips=["Migration planning","Cloud Run","DR & backup","Cost optimization"],
        intro="We help businesses move applications, databases and workloads to Google Cloud — improving scalability, performance, reliability and cost efficiency while preparing systems for future AI and automation.",
        deliver=["Cloud migration planning","Application & database migration","Google Cloud infrastructure setup","Cloud Run & serverless deployment","VM & storage configuration","Backup & disaster recovery","Cloud cost optimization"],
        impact=["Reduce infrastructure complexity","Improve performance & reliability","Lower long-term technology costs","Prepare systems for AI integration","Build a scalable cloud foundation"],
        steps=[("Assess","Inventory and readiness."),("Plan","Migration strategy."),("Migrate","Apps, data and workloads."),("Optimize","Cost and performance."),("Modernize","Serverless and AI-ready.")]),
    dict(slug="data-analytics-reporting", name="Data Analytics, Dashboards & Reporting", icon=CHART_ICON,
        nav="Turn business data into decisions with BigQuery & Looker.",
        eyebrow="Foundation · data", chips=["BigQuery","Looker","Pipelines","KPI tracking"],
        intro="We help companies turn business data into actionable insights using Google data tools. With BigQuery, Looker, Looker Studio, Sheets and Google Cloud, we build reporting systems that help leaders track performance, identify trends and make smarter decisions.",
        deliver=["Business dashboards","Looker & Looker Studio reports","BigQuery data warehouse setup","Sales, finance, operations & marketing reporting","Data pipeline development","Spreadsheet automation","KPI tracking systems"],
        impact=["Improve visibility across the business","Reduce manual reporting","Make faster, data-driven decisions","Standardize performance tracking","Create a single source of truth"],
        steps=[("Map","Sources and metrics."),("Model","BigQuery warehouse."),("Build","Looker dashboards."),("Automate","Pipelines and refreshes."),("Operate","KPI tracking.")]),
    dict(slug="google-workspace", name="Google Workspace Setup, Migration & Optimization", icon=GRID_ICON,
        nav="Migrate to Workspace and collaborate securely.",
        eyebrow="Foundation · workplace", chips=["Email migration","Admin console","Security","Adoption"],
        intro="We help businesses set up, migrate and optimize Google Workspace so teams collaborate securely and efficiently. Whether moving from Microsoft 365, legacy email or disconnected tools, we support a seamless transition to Gmail, Drive, Docs, Meet and the full Suite.",
        deliver=["Workspace setup & configuration","Email & file migration","Gmail, Drive, Calendar & Meet implementation","Shared drives & permission structures","Workspace security settings","Admin console configuration","Employee training & adoption"],
        impact=["Improve team collaboration","Reduce workplace tool complexity","Enable secure file sharing","Streamline communication","Create a modern productivity environment"],
        steps=[("Assess","Current tools and data."),("Configure","Workspace and security."),("Migrate","Email, files, calendars."),("Secure","Admin and permissions."),("Adopt","Training and support.")]),
]

# ----------------------------------------------------------------------------
# CONTENT — Insights articles (case studies + white papers / points of view)
# Add a dict here + re-run build.py to publish a new article.
# ----------------------------------------------------------------------------
ARTICLES = [
    dict(slug="enterprise-ai-agents-from-pilot-to-production", kind="Point of view", topic="Agentic AI", date="2026",
        title="From pilots to production: making enterprise AI agents real",
        dek="Why most enterprise AI pilots stall — and the operating model that gets agents into daily work.",
        body=[
            '<p>Every enterprise is running AI pilots. Far fewer have agents doing real work in production. The gap is rarely the model — it is the operating model around it. Here is what separates the pilots that ship from the ones that quietly die.</p>',
            '<h2>The pilot trap</h2><p>A demo that impresses in a conference room is not an agent that survives contact with real work. Pilots stall for predictable reasons: no clear owner, no integration with the systems where work actually happens, no governance to make security and legal comfortable, and no agreed metric to prove it was worth doing. The technology works; the model around it does not.</p>',
            '<h2>1. Start with one workflow, not a platform</h2><p>The fastest path to production is the narrowest one. Pick a single, high-value, bounded workflow — support triage, proposal drafting, finance reporting — and define the one number that says it worked: hours saved, response time, deflection rate. A focused four-to-six-week pilot beats a year-long platform programme that never ships.</p>',
            '<h2>2. Build for integration, not the demo</h2><p>An agent earns its keep when it can read and write the systems your team already uses, and when a human stays in the loop for the decisions that matter. Connect it to your real data and tools from day one, and design the hand-offs and approvals before you polish the prompts.</p>',
            '<h2>3. Govern from the first day</h2><p>Security, access control and responsible-AI practices are not a launch checklist — they are how you earn permission to launch at all. Treat governance, the discipline behind standards like ISO 42001, as part of the build, so the agent is something you can put in front of both your data and your board.</p>',
            '<h2>4. Measure, then expand</h2><p>Prove the metric, share the result internally, and use that win to fund the next workflow. Production AI is a sequence of small, measured expansions, not a big-bang transformation. Over time the pilots compound into an AI-first operating model.</p>',
            '<div class="callout"><strong>The model in one line:</strong> one workflow &rarr; an integrated build with a human in the loop &rarr; governed from day one &rarr; measured &rarr; expand. That is how a pilot becomes production.</div>',
        ]),
    dict(slug="we-ran-our-own-company-on-google", kind="Case study", topic="Data & AI", date="2026",
        title="We ran our own company on Google Cloud",
        dek="How we re-platformed our own operating data onto BigQuery, Looker and Gemini — and made it our first reference implementation.",
        metrics=[("27k+", "transactions unified"), ("1", "ask-your-business agent"), ("days&rarr;min", "to an answer")],
        body=[
            '<p>The hardest test of an AI-for-operations platform is whether you would run your own business on it. We do. Before we take a pattern to clients, we prove it on ourselves.</p>',
            '<h2>The challenge</h2><p>Like most growing companies, our operating data lived in spreadsheets and disconnected systems — sales, delivery, finance and recruiting each telling part of the story. Answering a straightforward leadership question often meant a manual pull across several files, and the answer could take days. There was no single source of truth, and reporting consumed real time every week.</p>',
            '<h2>The approach</h2><p>We treated our own company as a client. The goal was simple: one trustworthy model of the business, reporting leaders actually use, and the ability to ask questions in plain language instead of waiting for a report.</p>',
            '<h2>What we built, on Google Cloud</h2><ul><li><strong>A unified data model on BigQuery</strong> — records from our operating systems brought into one warehouse with consistent, conformed definitions.</li><li><strong>Executive reporting in Looker</strong> — dashboards for the metrics leadership tracks, refreshed automatically.</li><li><strong>An &ldquo;ask-your-business&rdquo; Gemini agent</strong> — natural-language questions answered from the approved model, with every number traceable back to source.</li></ul>',
            '<h2>The outcome</h2><p>Questions that used to take days are answered in minutes. Reporting is standardized and largely automated. Most importantly, we now have a single source of truth — and a working reference implementation we can show any client weighing the same move.</p>',
            '<div class="callout"><strong>Why it matters:</strong> we do not pitch AI-for-operations from theory. We re-platformed our own company onto BigQuery, Looker and Gemini first — and we build the same foundation for you.</div>',
        ]),
]

# ----------------------------------------------------------------------------
# NAV
# ----------------------------------------------------------------------------
NAV = [
    dict(label="Agentic AI", key="agentic", href="agentic-ai/index.html", mega=True, head="AI-first services",
         children=[dict(label="Overview", desc="All agentic AI services", href="agentic-ai/index.html")]
                  + [dict(label=s["name"], desc=s["nav"], href="agentic-ai/%s.html" % s["slug"]) for s in AGENTIC]),
    dict(label="Core Services", key="core", href="core-services/index.html", head="Foundation services",
         children=[dict(label="Overview", desc="All core services", href="core-services/index.html")]
                  + [dict(label=s["name"], desc=s["nav"], href="core-services/%s.html" % s["slug"]) for s in CORE]),
    dict(label="Partnership", key="partnership", href="partnership.html"),
    dict(label="About", key="about", href="about.html",
         children=[dict(label="Overview", desc="Who we are", href="about.html"),
                   dict(label="Leadership", desc="The team", href="about.html#leadership"),
                   dict(label="Backed by Avanciers", desc="Our backbone", href="about.html#backed")]),
    dict(label="Insights", key="insights", href="insights.html"),
]

CARET = '<svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'

def logo(stroke, dot):
    return ('<svg class="logo" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<path d="M6 31 L16 22 L25 26 L34 9" stroke="%s" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="6" cy="31" r="3.4" fill="%s"/><circle cx="16" cy="22" r="3.4" fill="%s"/>'
            '<circle cx="25" cy="26" r="3.4" fill="%s"/><circle cx="34" cy="9" r="4.6" fill="#e97451"/></svg>' % (stroke, dot, dot, dot))

def rel(p, href):
    if href.startswith(("http", "#", "mailto:")):
        return href
    return p + href

def nav_html(p, active):
    items = []
    for it in NAV:
        if it.get("children"):
            mega = " dropdown--mega" if it.get("mega") else ""
            drops = ['<div class="drop-head">%s</div>' % it["head"]] if it.get("head") else []
            for c in it["children"]:
                drops.append('<a class="drop-item" href="%s"><span class="di-title">%s</span><span class="di-desc">%s</span></a>'
                             % (rel(p, c["href"]), c["label"], c["desc"]))
            items.append(
                '<li class="has-menu%s">'
                '<a class="nav-top" href="%s">%s %s</a>'
                '<div class="dropdown%s"><div class="dropdown-inner">%s</div></div></li>'
                % (" active" if active == it["key"] else "", rel(p, it["href"]), it["label"], CARET, mega, "".join(drops)))
        else:
            items.append('<li class="%s"><a class="nav-top" href="%s">%s</a></li>'
                         % ("active" if active == it["key"] else "", rel(p, it["href"]), it["label"]))
    return "".join(items)

def header(p, active):
    return (
    '<header class="site-header" id="header"><div class="container nav">'
    '<a href="%sindex.html" class="brand" aria-label="%s home">%s'
    '<span class="brand-text"><span class="brand-name">%s</span></span></a>'
    '<ul class="nav-links" id="navLinks">%s</ul>'
    '<div class="nav-cta"><a href="%scontact.html" class="btn btn-primary">Talk to us</a>'
    '<button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button></div>'
    '</div></header>' % (p, BRAND, logo("#0b2a4a", "#16466e"), BRAND, nav_html(p, active), p))

def footer(p):
    ag = "".join('<li><a href="%s">%s</a></li>' % (rel(p, "agentic-ai/%s.html" % s["slug"]), s["name"].split(" &")[0]) for s in AGENTIC[:5])
    co = "".join('<li><a href="%s">%s</a></li>' % (rel(p, "core-services/%s.html" % s["slug"]), s["name"].split(",")[0].split(" Setup")[0]) for s in CORE)
    return (
    '<footer class="footer"><div class="container"><div class="footer-top">'
    '<div><a href="%sindex.html" class="brand" style="margin-bottom:6px">%s'
    '<span class="brand-text"><span class="brand-name">%s</span></span></a>'
    '<p class="footer-blurb">Google-first AI, data and cloud transformation. We turn Google technology into measurable business outcomes.</p>'
    '<span class="badge" style="background:rgba(255,255,255,.06)"><span class="gdots"><i></i><i></i><i></i><i></i></span> Certified Google Cloud Partner</span></div>'
    '<div><h4>Agentic AI</h4><ul>%s</ul></div>'
    '<div><h4>Core Services</h4><ul>%s</ul></div>'
    '<div><h4>Company</h4><ul>'
    '<li><a href="%sabout.html">About</a></li><li><a href="%spartnership.html">Partnership</a></li>'
    '<li><a href="%sinsights.html">Insights</a></li><li><a href="%scontact.html">Contact</a></li>'
    '<li><a href="https://www.avanciers.com" target="_blank" rel="noopener">Avanciers</a></li></ul></div>'
    '</div><div class="footer-bottom"><span>© %s %s. All rights reserved.</span>'
    '<span class="footer-legal"><a href="%sprivacy.html">Privacy</a><a href="%sprivacy.html">Cookies</a><a href="%sprivacy.html">Terms</a></span>'
    '</div></div></footer>' % (p, logo("#ffffff", "#9fb3cc"), BRAND, ag, co, p, p, p, p, YEAR, BRAND, p, p, p))

def head(p, title, desc):
    return (
    '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    '<meta name="robots" content="noindex">'  # PRE-LAUNCH: remove this line + rebuild to allow search indexing at launch
    '<title>%s</title><meta name="description" content="%s">'
    '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website">'
    '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">'
    '<link rel="stylesheet" href="%sassets/css/styles.css"></head><body>' % (title, desc, title, desc, p))

def cta_simple(p, heading, text, aside=""):
    return ('<section class="cta-band"><div class="container"><div class="cta-inner">'
            '<div><p class="eyebrow eyebrow--light">Let\'s build</p><h2>%s</h2><p class="lead">%s</p>'
            '<a href="%scontact.html" class="btn btn-primary btn-lg" style="margin-top:20px">Request a consultation <span class="arrow">→</span></a></div>'
            '%s</div></div></section>' % (heading, text, p, aside))

def lead_form():
    return (
    '<form class="form" data-lead novalidate><h3>Request a consultation</h3>'
    '<div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required placeholder="Your name"></div>'
    '<div class="field"><label for="email">Work email</label><input id="email" name="email" type="email" required placeholder="you@company.com"></div>'
    '<div class="field"><label for="company">Company</label><input id="company" name="company" type="text" placeholder="Company name"></div>'
    '<div class="field"><label for="interest">I\'m interested in</label><select id="interest" name="interest">'
    '<option>Enterprise AI agents</option><option>Data analytics on BigQuery &amp; Looker</option><option>Google Cloud migration</option>'
    '<option>Workspace + Gemini rollout</option><option>Custom Gemini application</option><option>Not sure yet — let\'s talk</option></select></div>'
    '<div class="field"><label for="msg">What do you want to tackle first?</label><textarea id="msg" name="msg" rows="3" placeholder="A sentence is plenty."></textarea></div>'
    '<button type="submit" class="btn btn-primary">Request a consultation</button>'
    '<p class="form-note">We reply within one business day. No spam, ever.</p></form>')

def steps_html(steps):
    return '<div class="steps">%s</div>' % "".join('<div class="step"><h3>%s</h3><p>%s</p></div>' % (n, d) for n, d in steps)

def checks(items):
    half = (len(items) + 1) // 2
    def col(group): return '<ul class="list-check">%s</ul>' % "".join('<li>%s</li>' % i for i in group)
    return '<div class="deliver-grid">%s%s</div>' % (col(items[:half]), col(items[half:]))

def impact_box(items):
    return '<div class="impact-box"><p style="font-weight:700;color:var(--navy-800);font-family:var(--display);margin-bottom:6px">Business impact</p><ul>%s</ul></div>' % "".join('<li>%s</li>' % i for i in items)

def write(path, title, desc, body, active):
    p = "../" * path.count("/")
    htmlout = head(p, title, desc) + header(p, active) + body + footer(p) + ('<script src="%sassets/js/main.js"></script></body></html>' % p)
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(htmlout)
    return path

# ----------------------------------------------------------------------------
# PAGE BODIES
# ----------------------------------------------------------------------------
def service_body(s, hub, hub_label):
    p = "../"
    siblings = [x for x in (AGENTIC if hub == "agentic-ai" else CORE) if x["slug"] != s["slug"]][:3]
    rel_cards = "".join(
        '<a class="mini" href="%s.html"><span class="tag">%s</span><h3>%s</h3><p>%s</p><span class="more">Learn more →</span></a>'
        % (x["slug"], x.get("tag", "Service"), x["name"], x["nav"]) for x in siblings)
    return (
    '<section class="page-hero"><div class="container"><div class="inner">'
    '<p class="crumb"><a href="%sindex.html">Home</a> › <a href="index.html">%s</a> › %s</p>'
    '<p class="eyebrow eyebrow--light">%s</p><h1>%s</h1><p class="lead">%s</p>'
    '<div class="hero-cta" style="margin-top:26px"><a href="%scontact.html" class="btn btn-primary btn-lg">Talk to us <span class="arrow">→</span></a></div>'
    '</div></div></section>'
    '<section class="section"><div class="container"><div class="two-col"><div>'
    '<p class="eyebrow">What it is</p><h2>%s</h2><p class="lead">%s</p></div>%s</div></div></section>'
    '<section class="section section--alt"><div class="container"><div class="section-head"><p class="eyebrow">What we deliver</p><h2>What\'s included.</h2></div>%s</div></section>'
    '<section class="section"><div class="container"><div class="section-head center"><p class="eyebrow">How we work</p><h2>A clear path to value.</h2></div>%s</div></section>'
    '<section class="section section--soft"><div class="container"><div class="section-head"><p class="eyebrow">Related</p><h2>Explore more %s.</h2></div><div class="related">%s</div></div></section>'
    '%s'
    % (p, hub_label, s["name"], s["eyebrow"], s["name"], s["intro"], p,
       s["name"] + ".", s["intro"], impact_box(s["impact"]),
       checks(s["deliver"]),
       steps_html(s["steps"]),
       hub_label.lower(), rel_cards,
       cta_simple(p, "Ready to start?", "Tell us what you want to tackle first and we'll scope a focused way to begin.")))

def hub_body(items, hub, eyebrow, title, intro, kind):
    p = "../"
    ph_bg = '<img class="ph-bg" src="%sassets/img/%s.webp" alt="" aria-hidden="true">' % (p, hub)
    if kind == "agentic":
        cards = "".join(
            '<a class="mini" href="%s.html"><span class="tag">%s</span><h3>%s</h3><p>%s</p><span class="more">Learn more →</span></a>'
            % (s["slug"], s["tag"], s["name"], s["nav"]) for s in items)
        grid = '<div class="cards-7">%s</div>' % cards
    else:
        cards = "".join(
            '<div class="card"><div class="ic">%s</div><h3>%s</h3><p>%s</p>'
            '<ul class="deliver">%s</ul><a href="%s.html" class="card-link">Learn more →</a></div>'
            % (s["icon"], s["name"], s["intro"], "".join('<li>%s</li>' % c for c in s["chips"]), s["slug"]) for s in items)
        grid = '<div class="cards">%s</div>' % cards
    return (
    '<section class="page-hero">%s<div class="container"><div class="inner">'
    '<p class="crumb"><a href="%sindex.html">Home</a> › %s</p>'
    '<p class="eyebrow eyebrow--light">%s</p><h1>%s</h1><p class="lead">%s</p></div></div></section>'
    '<section class="section"><div class="container">%s</div></section>'
    '%s' % (ph_bg, p, title, eyebrow, title, intro, grid,
            cta_simple(p, "Not sure where to start?", "Most clients begin with one focused pilot, then expand. Let's find your highest-value first step.")))

def media_row(p, img, eyebrow, title, body_html, side="right", cls=""):
    media = '<div class="mr-media"><img src="%sassets/img/%s.webp" alt="" loading="lazy"></div>' % (p, img)
    text = '<div class="mr-text"><p class="eyebrow">%s</p><h2>%s</h2>%s</div>' % (eyebrow, title, body_html)
    inner = (text + media) if side == "right" else (media + text)
    return '<section class="section %s" data-reveal><div class="container"><div class="media-row mr-%s">%s</div></div></section>' % (cls, side, inner)

def home_body():
    p = ""
    ph_platform = '<img class="ph-bg" src="assets/img/platform.webp" alt="" aria-hidden="true">'
    core_cards = "".join(
        '<div class="card"><div class="ic">%s</div><h3>%s</h3><p>%s</p>'
        '<ul class="deliver">%s</ul><a href="core-services/%s.html" class="card-link">Learn more →</a></div>'
        % (s["icon"], s["name"], s["intro"], "".join('<li>%s</li>' % c for c in s["chips"]), s["slug"]) for s in CORE)
    ag_cards = "".join(
        '<a class="mini" href="agentic-ai/%s.html"><span class="tag">%s</span><h3>%s</h3><p>%s</p><span class="more">Learn more →</span></a>'
        % (s["slug"], s["tag"], s["name"], s["nav"]) for s in AGENTIC)
    gproducts = [("Gemini","Agents & generative AI"),("Vertex AI","Model platform & MLOps"),("BigQuery","Data warehouse & analytics"),
                 ("Looker","BI & decision intelligence"),("Google Workspace","Productivity & collaboration"),("Cloud Run","Serverless applications"),
                 ("Firebase","App & product platform"),("Maps Platform","Location intelligence")]
    gp = "".join('<div class="gp"><div class="gp-name">%s</div><div class="gp-desc">%s</div></div>' % (n, d) for n, d in gproducts)
    return (
    # hero
    '<section class="hero"><img class="hero-bg" src="assets/img/hero.webp" alt="" aria-hidden="true" fetchpriority="high">'
    '<div class="container"><div class="hero-inner"><p class="eyebrow eyebrow--light">Google-first · AI · Data · Cloud</p>'
    '<h1>Build your AI-first business on Google.</h1>'
    '<p class="lead">We help enterprises modernize on Google Cloud and put Gemini-powered AI agents to work across the business — turning Google technology into measurable outcomes, securely and at scale.</p>'
    '<div class="hero-cta"><a href="contact.html" class="btn btn-primary btn-lg">Request a consultation <span class="arrow">→</span></a>'
    '<a href="agentic-ai/index.html" class="btn btn-outline btn-lg">Explore services</a></div>'
    '<div class="hero-trust"><span class="badge"><span class="gdots"><i></i><i></i><i></i><i></i></span> Certified Google Cloud Partner</span>'
    '<span>Backed by <strong>Avanciers</strong> · operating since 2014 across 4 countries</span></div></div></div></section>'
    # stat band
    '<section class="stat-band"><div class="container"><div class="stat-grid">'
    '<div class="stat"><div class="num">Strategic</div><div class="label">Google Cloud Partner</div></div>'
    '<div class="stat"><div class="num">10<span>+</span> yrs</div><div class="label">Enterprise delivery heritage</div></div>'
    '<div class="stat"><div class="num">4</div><div class="label">Countries · 4 entities</div></div>'
    '<div class="stat"><div class="num">1,500<span>+</span></div><div class="label">Specialists placed since 2015</div></div>'
    '<div class="stat"><div class="num">300<span>+</span></div><div class="label">Consultants on tap</div></div></div>'
    '<p class="stat-note">Credentials and delivery scale of our parent and operating engine, Avanciers — a women-owned global talent &amp; technology firm.</p></div></section>'
    # overview + props
    '<section class="section" data-reveal><div class="container"><div class="section-head"><p class="eyebrow">Who we are</p>'
    '<h2>A Google-first organization, built for the AI era.</h2>'
    '<p class="lead">We work with companies to unlock performance using Google\'s AI, cloud, data, productivity, location and security technologies — from Workspace and Google Cloud through to Gemini-powered agents, BigQuery analytics, custom applications and workflow automation.</p></div>'
    '<div class="props">'
    '<div class="prop"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div><h3>Google specialist</h3><p>One ecosystem, mastered — not a generalist juggling three clouds.</p></div>'
    '<div class="prop"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a4 4 0 0 1 4 4c1.5 0 3 1.5 3 3a3.5 3.5 0 0 1 0 7c0 1.5-1.5 3-3 3a4 4 0 0 1-8 0c-1.5 0-3-1.5-3-3a3.5 3.5 0 0 1 0-7c0-1.5 1.5-3 3-3a4 4 0 0 1 4-4z"/></svg></div><h3>Agentic-AI first</h3><p>We design Gemini agents that act, not just answer.</p></div>'
    '<div class="prop"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/></svg></div><h3>Outcome &amp; ROI-led</h3><p>Every engagement is scoped to a result and measured.</p></div>'
    '<div class="prop"><div class="ic"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3>Secure &amp; governed</h3><p>Responsible AI and data governance built in. ISO 27001, ISO 42001, SOC 2 &amp; GDPR in progress.</p></div></div></div></section>'
    # why now
    '<section class="section section--alt" data-reveal><div class="container"><div class="whynow"><div>'
    '<p class="eyebrow">Why now</p><h2>The AI window is open. Most enterprises can\'t walk through it alone.</h2>'
    '<ul class="whynow-list">'
    '<li><span class="n">1</span><div><h3>Agents move to production</h3><p>AI is shifting from chat demos to agents that complete work across support, ops, finance and HR.</p></div></li>'
    '<li><span class="n">2</span><div><h3>Google\'s platform moment</h3><p>Gemini, Vertex AI, BigQuery, Looker and Workspace now form one coherent stack for agentic enterprise AI.</p></div></li>'
    '<li><span class="n">3</span><div><h3>The capability gap</h3><p>Ambition is everywhere; in-house delivery muscle is rare. That gap is where we create value.</p></div></li></ul></div>'
    '<div class="whynow-card"><div class="big">24<span> mo</span></div><p>The window in which AI-first operating models become the default — and laggards lose ground. We get you to production inside it, starting with a single high-value workflow.</p></div></div></div></section>'
    # core services
    '<section class="section" id="core" data-reveal><div class="container"><div class="section-head"><p class="eyebrow">Core Google technology services</p>'
    '<h2>The foundation: cloud, data and a modern workplace.</h2>'
    '<p class="lead">Get the platform right first. We move workloads to Google Cloud, turn data into decisions, and modernize the way teams work in Google Workspace.</p></div>'
    '<div class="cards">%s</div>'
    '<p style="margin-top:26px"><a href="core-services/index.html" class="card-link">See all core services →</a></p></div></section>'
    # agentic
    '<section class="section section--soft" id="agentic" data-reveal><div class="container"><div class="section-head"><p class="eyebrow">Advanced AI-first services</p>'
    '<h2>Agentic AI that does the work.</h2>'
    '<p class="lead">Gemini-powered agents and intelligent systems that automate workflows, surface knowledge and turn data into decisions — deployed responsibly across your organization.</p></div>'
    '<div class="cards-7">%s</div>'
    '<p style="margin-top:26px"><a href="agentic-ai/index.html" class="card-link">See all agentic AI services →</a></p></div></section>'
    # approach
    '<section class="section" data-reveal><div class="container"><div class="section-head center"><p class="eyebrow">Our approach</p>'
    '<h2>We don\'t just implement technology. We redesign how work gets done.</h2>'
    '<p class="lead" style="margin:0 auto">We start where AI, cloud, data and automation create the most value — then design secure, scalable solutions and integrate them into the tools your teams already use.</p></div>'
    '<div class="steps"><div class="step"><h3>Identify</h3><p>Find the highest-value workflows and decisions.</p></div>'
    '<div class="step"><h3>Design</h3><p>Architect secure, scalable solutions on Google.</p></div>'
    '<div class="step"><h3>Build &amp; Migrate</h3><p>Modernize systems and ship agents, apps and analytics.</p></div>'
    '<div class="step"><h3>Govern</h3><p>Access control, human-in-the-loop and responsible AI.</p></div>'
    '<div class="step"><h3>Scale</h3><p>Adopt, measure ROI and expand the operating model.</p></div></div></div></section>'
    '%s'
    # partnership
    '<section class="section partner" id="partnership" data-reveal>%s<div class="container"><div class="section-head"><p class="eyebrow eyebrow--light">The Google advantage</p>'
    '<h2>One ecosystem. Every layer of the AI-first enterprise.</h2>'
    '<p class="lead">As a Certified Google Cloud Partner, we build across the full Google stack — and bring co-sell, funded proofs-of-concept and Marketplace access to every engagement.</p></div>'
    '<div class="gproducts">%s</div>'
    '<p style="margin-top:28px"><a href="partnership.html" class="btn btn-outline">More on our partnership →</a></p></div></section>'
    # proof
    '<section class="section section--alt" data-reveal><div class="container"><div class="section-head"><p class="eyebrow">Proof</p>'
    '<h2>We start by doing it to ourselves.</h2><p class="lead">Our first reference implementation is our own business — the surest test of whether an AI-first model actually works.</p></div>'
    '<div class="cases"><div class="case case--feature"><div class="case-body"><p class="kicker">Reference implementation · Internal</p>'
    '<h3>We ran our own company on it.</h3><p>We unified our entire operating dataset into a single model on Google Cloud, rebuilt executive reporting in Looker, and stood up a Gemini agent that answers leadership questions in plain language — the same platform we now build for clients.</p>'
    '<div class="metrics"><div class="metric"><div class="m">27k+</div><div class="l">transactions unified</div></div>'
    '<div class="metric"><div class="m">1</div><div class="l">ask-your-business agent</div></div>'
    '<div class="metric"><div class="m">days→min</div><div class="l">to a decision</div></div></div><a href="insights/we-ran-our-own-company-on-google.html" class="card-link" style="color:#ffb79d;margin-top:18px">Read the case study →</a></div></div>'
    '<div class="case case--soon"><div class="case-body"><p class="kicker">Client story</p><p>First client case study — coming soon as pilots land.</p></div></div>'
    '<div class="case case--soon"><div class="case-body"><p class="kicker">Client story</p><p>Your engagement could be the next one featured here.</p></div></div></div></div></section>'
    # backed
    '<section class="section" data-reveal><div class="container"><div class="backed"><div>'
    '<p class="eyebrow">Backed by Avanciers</p><h2>A startup\'s focus. An established firm\'s backbone.</h2>'
    '<p class="lead">%s is launched and backed by <strong>Avanciers</strong> — a women-owned global talent and technology firm operating since 2014 across Canada, the USA, Mexico and India, serving Big-4 and Tier-1 enterprises.</p>'
    '<div class="creds"><span class="cred">Certified Google Cloud Partner (Strategic)</span><span class="cred">Certified Salesforce Partner</span>'
    '<span class="cred">Women-owned &amp; diversity-certified</span><span class="cred">OECM Supplier Partner</span><span class="cred">ISO 27001 · ISO 42001 · SOC 2 · GDPR — in progress</span></div>'
    '<p style="margin-top:18px"><a href="about.html" class="card-link">More about us →</a></p></div>'
    '<div><div class="impact-box"><p style="font-weight:700;color:var(--navy-800);margin-bottom:14px;font-family:var(--display)">Trusted by leading enterprises &amp; system integrators</p>'
    '<div class="logos-row"><span>Deloitte</span><span>Wipro</span><span>Infosys</span><span>Cognizant</span><span>Tech&nbsp;Mahindra</span><span>Mphasis</span><span>Sonata</span><span>ABB</span></div>'
    '<p class="muted" style="font-size:.86rem;margin:20px 0 0">4 entities · 350+ families supported through our consultant network.</p></div></div></div></div></section>'
    # cta + form
    '<section class="cta-band" id="contact"><div class="container"><div class="cta-inner"><div>'
    '<p class="eyebrow eyebrow--light">Let\'s build</p><h2>Build your AI-first business on Google.</h2>'
    '<p class="lead">Tell us the workflow, decision or migration you want to tackle first. We\'ll come back with a focused, fixed-scope way to start — usually a 4–6 week pilot.</p></div>%s</div></div></section>'
    % (core_cards, ag_cards, media_row(p, "consultant", "The people", "Specialists who deliver, not just advise.", "<p>Certified Google Cloud architects and AI engineers who stay in the build from scoping to production — measured against your number, not ours.</p>", side="right"), ph_platform, gp, BRAND, lead_form()))

def partnership_body():
    p = ""
    gproducts = [("Gemini","Agents & generative AI"),("Vertex AI","Model platform & MLOps"),("BigQuery","Data warehouse & analytics"),
                 ("Looker","BI & decision intelligence"),("Google Workspace","Productivity & collaboration"),("Cloud Run","Serverless applications"),
                 ("Firebase","App & product platform"),("Maps Platform","Location intelligence")]
    gp = "".join('<div class="gp"><div class="gp-name">%s</div><div class="gp-desc">%s</div></div>' % (n, d) for n, d in gproducts)
    return (
    '<section class="page-hero"><div class="container"><div class="inner"><p class="crumb"><a href="index.html">Home</a> › Partnership</p>'
    '<p class="eyebrow eyebrow--light">The Google advantage</p><h1>A Certified Google Cloud Partner.</h1>'
    '<p class="lead">We concentrate on one ecosystem so you get depth, not breadth — and the benefits of Google\'s partner programs on every engagement.</p></div></div></section>'
    '<section class="section"><div class="container"><div class="props">'
    '<div class="prop"><h3>Co-sell &amp; funding</h3><p>Access to Google co-sell motions and funded proofs-of-concept that lower the cost and risk of getting started.</p></div>'
    '<div class="prop"><h3>Marketplace</h3><p>Procure our solutions through Google Cloud Marketplace, drawing down committed spend.</p></div>'
    '<div class="prop"><h3>Certified expertise</h3><p>Engineers certified across Google Cloud, data and AI — kept current as the platform evolves.</p></div>'
    '<div class="prop"><h3>Early access</h3><p>Hands-on with the latest Gemini, Vertex AI and Workspace capabilities as they ship.</p></div></div></div></section>'
    '%s'
    '<section class="section section--alt partner" style="background:var(--navy-900)"><div class="container"><div class="section-head"><p class="eyebrow eyebrow--light">The stack</p>'
    '<h2 style="color:#fff">Every layer of the AI-first enterprise.</h2><p class="lead" style="color:#cdd9e8">We build across the full Google technology stack.</p></div><div class="gproducts">%s</div></div></section>'
    '%s' % (media_row(p, "team-collab2", "Delivery", "A partner team that has done this before.", "<p>Co-sell, funded proofs of concept and Marketplace access — delivered by senior people who have shipped Google Cloud and AI for Tier-1 enterprises.</p>", side="left", cls="section--soft"), gp, cta_simple(p, "Build on Google with a partner.", "Bring us your goal — we'll bring the ecosystem.")))

def about_body():
    p = ""
    ph_bg = '<img class="ph-bg" src="assets/img/about.webp" alt="" aria-hidden="true">'
    return (
    '<section class="page-hero">%s<div class="container"><div class="inner"><p class="crumb"><a href="index.html">Home</a> › About</p>'
    '<p class="eyebrow eyebrow--light">About us</p><h1>Operators building the AI-first enterprise.</h1>'
    '<p class="lead">%s is a Google-first AI, data and cloud transformation firm — launched and backed by Avanciers, with a singular focus on turning Google technology into measurable business outcomes.</p></div></div></section>'
    '<section class="section"><div class="container"><div class="two-col"><div>'
    '<p class="eyebrow">Our story</p><h2>Specialist by design.</h2>'
    '<p class="lead">The market is full of generalists juggling three clouds. We chose the opposite path: go deep on Google. As a Certified Google Cloud Partner, we pair that focus with a decade of enterprise delivery from our parent, Avanciers — so clients get a specialist\'s edge with an established firm\'s backbone.</p>'
    '<p>We prove every capability on our own business before we sell it, then deliver it with secure, governed, ROI-led engagements.</p></div>'
    '<div class="impact-box"><p style="font-weight:700;color:var(--navy-800);font-family:var(--display);margin-bottom:6px">What we believe</p><ul>'
    '<li>Specialization beats breadth</li><li>Agents should act, not just answer</li><li>Every engagement has a measurable result</li><li>AI must be secure and governed</li><li>Prove it on ourselves first</li></ul></div></div></div></section>'
    '%s%s'
    # leadership
    '<section class="section section--soft" id="leadership"><div class="container"><div class="section-head center"><p class="eyebrow">Leadership</p><h2>Operators who have built this before.</h2></div>'
    '<div class="team"><div class="member veteran"><div class="avatar">★</div><h3>[Industry Veteran]</h3><p class="role">Chairman &amp; Strategic Advisor</p>'
    '<p class="ph">Three decades scaling enterprise technology and services businesses. Bio to confirm — placeholder for the new partner who authored the strategy.</p></div>'
    '<div class="member"><div class="avatar">VW</div><h3>Vik Wahi</h3><p class="role">Co-Founder &amp; CEO</p><p>Co-founder of Avanciers. Builds the data, AI and analytics systems that prove the model before it ships to clients.</p></div>'
    '<div class="member"><div class="avatar">AW</div><h3>Adi Wahi</h3><p class="role">Co-Founder</p><p>Co-founder of Avanciers. Leads partnerships and the Google-first go-to-market across North America.</p></div></div></div></section>'
    # backed
    '<section class="section" id="backed"><div class="container"><div class="backed"><div>'
    '<p class="eyebrow">Backed by Avanciers</p><h2>A startup\'s focus. An established firm\'s backbone.</h2>'
    '<p class="lead">Avanciers is a women-owned global talent and technology firm operating since 2014 across Canada, the USA, Mexico and India, serving Big-4 and Tier-1 enterprises.</p>'
    '<div class="creds"><span class="cred">Certified Google Cloud Partner (Strategic)</span><span class="cred">Certified Salesforce Partner</span>'
    '<span class="cred">Women-owned &amp; diversity-certified</span><span class="cred">OECM Supplier Partner</span><span class="cred">ISO 27001 · ISO 42001 · SOC 2 · GDPR — in progress</span></div></div>'
    '<div><div class="impact-box"><p style="font-weight:700;color:var(--navy-800);margin-bottom:14px;font-family:var(--display)">Trusted by leading enterprises &amp; system integrators</p>'
    '<div class="logos-row"><span>Deloitte</span><span>Wipro</span><span>Infosys</span><span>Cognizant</span><span>Tech&nbsp;Mahindra</span><span>Mphasis</span><span>Sonata</span><span>ABB</span></div>'
    '<p class="muted" style="font-size:.86rem;margin:20px 0 0">4 entities · 350+ families supported through our consultant network.</p></div></div></div></div></section>'
    '%s' % (ph_bg, BRAND, media_row(p, "team-collab", "How we work", "Senior people, in the room with you.", "<p>You work with the architects and engineers who do the build — not a layer of account managers. Small, senior teams, with a human in the loop on every decision that matters.</p>", side="right"), media_row(p, "people-work", "Proof", "We prove it on ourselves first.", "<p>Before a pattern reaches a client it runs in our own business — our operating data on Google Cloud, our reporting in Looker, our questions answered by a Gemini agent.</p>", side="left", cls="section--soft"), cta_simple(p, "Work with us.", "Tell us what you want to build on Google.")))

def insights_body():
    p = ""
    imgmap = {"enterprise-ai-agents-from-pilot-to-production": "insight-pilot", "we-ran-our-own-company-on-google": "insight-google"}
    cards = "".join('<a class="post" href="insights/%s.html"><div class="thumb"><img src="assets/img/%s.webp" alt="" loading="lazy"></div><div class="pbody"><span class="ptag">%s</span><h3>%s</h3><p>%s</p><span class="pmeta">%s · Read →</span></div></a>' % (a["slug"], imgmap.get(a["slug"], "insight-pilot"), a["kind"], a["title"], a["dek"], a["topic"]) for a in ARTICLES)
    cards += '<div class="post"><div class="thumb"><img src="assets/img/insight-data.webp" alt="" loading="lazy"></div><div class="pbody"><span class="ptag">Playbook</span><h3>Your BigQuery + Looker decision foundation</h3><p>A practical sequence for turning scattered data into decisions leaders trust.</p><span class="pmeta">Coming soon</span></div></div>'
    return (
    '<section class="page-hero"><div class="container"><div class="inner"><p class="crumb"><a href="index.html">Home</a> › Insights</p>'
    '<p class="eyebrow eyebrow--light">Insights</p><h1>Ideas on AI-first business.</h1>'
    '<p class="lead">Practical points of view on building, governing and scaling AI on Google — written for operators, not hype.</p></div></div></section>'
    '<section class="section"><div class="container"><div class="posts">%s</div>'
    '<p class="muted" style="margin-top:30px">More articles publishing soon. Want our point of view on a specific challenge? <a href="contact.html">Ask us</a>.</p></div></section>'
    '%s' % (cards, cta_simple(p, "Have a harder question?", "Tell us the problem you're chewing on — we'll share how we'd approach it.")))

def contact_body():
    p = ""
    return (
    '<section class="page-hero"><div class="container"><div class="inner"><p class="crumb"><a href="index.html">Home</a> › Contact</p>'
    '<p class="eyebrow eyebrow--light">Talk to us</p><h1>Let\'s scope your first win.</h1>'
    '<p class="lead">Tell us the workflow, decision or migration you want to tackle. We\'ll come back with a focused, fixed-scope way to start.</p></div></div></section>'
    '<section class="section"><div class="container"><div class="contact-grid"><div class="contact-info">'
    '<div class="ci"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="m4 6 8 6 8-6"/></svg></div><div><h3>Email</h3><p><a href="mailto:hello@ascendia.ai">hello@ascendia.ai</a></p></div></div>'
    '<div class="ci"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div><div><h3>Response time</h3><p>We reply within one business day.</p></div></div>'
    '<div class="ci"><div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0b2a4a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div><div><h3>Where we operate</h3><p>Through Avanciers, across four countries.</p><div class="offices"><span class="office">Canada</span><span class="office">USA</span><span class="office">Mexico</span><span class="office">India</span></div></div></div>'
    '</div><div>%s</div></div></div></section>' % lead_form())

def legal_body():
    sec = lambda h, b: f'<h2 style="margin-top:36px">{h}</h2><p class="muted">{b}</p>'
    notice = (f'<div class="impact-box" style="margin-bottom:30px"><p class="muted" style="margin:0">'
              f'<strong>Template notice:</strong> This is placeholder legal text for the {BRAND} website and must be '
              f'reviewed and finalized by counsel before launch — especially alongside the ISO 27001 / ISO 42001 / SOC 2 program and any'
              f'GDPR/PIPEDA obligations.</p></div>')
    body = (
        '<h2 id="privacy">Privacy</h2><p class="muted">We collect only the information you provide through our contact form '
        '(name, work email, company and your message) to respond to your enquiry. We do not sell your data. You can request '
        'access to or deletion of your information at any time by emailing <a href="mailto:hello@ascendia.ai">hello@ascendia.ai</a>.</p>'
        + sec("Cookies", "We use essential cookies to run the site and privacy-respecting analytics to understand traffic. You can control cookies in your browser settings.")
        + sec("Terms of use", f"Content on this site is provided for general information about {BRAND} services and is offered without warranty. Trademarks and product names (including Google, Google Cloud, Gemini, BigQuery and Looker) belong to their respective owners.")
        + sec("Data security", "Information is handled in line with our information-security program (ISO 27001, ISO 42001, SOC 2 and GDPR — in progress, targeted 2026). Contact us for our current security posture.")
        + '<p class="muted" style="margin-top:30px">Questions? <a href="contact.html">Contact us</a>.</p>')
    return (
        '<section class="page-hero"><div class="container"><div class="inner"><p class="crumb"><a href="index.html">Home</a> › Legal</p>'
        '<p class="eyebrow eyebrow--light">Legal</p><h1>Privacy, cookies &amp; terms.</h1>'
        '<p class="lead">How we handle your information and the terms of using this site.</p></div></div></section>'
        '<section class="section"><div class="container" style="max-width:820px">' + notice + body + '</div></section>')

def article_body(a):
    p = "../"
    metrics = ""
    if a.get("metrics"):
        metrics = '<div class="article-metrics">' + "".join('<div><div class="m">%s</div><div class="l">%s</div></div>' % (m, l) for m, l in a["metrics"]) + '</div>'
    return (
    '<section class="page-hero"><div class="container"><div class="inner">'
    '<p class="crumb"><a href="%sindex.html">Home</a> › <a href="../insights.html">Insights</a> › %s</p>'
    '<p class="eyebrow eyebrow--light">%s · %s</p><h1>%s</h1><p class="dek">%s</p></div></div></section>'
    '<section class="section"><div class="container"><div class="article prose">%s%s'
    '<p class="article-foot">Published by %s. This reflects how we work with clients — <a href="%scontact.html">talk to us</a> about applying it to your business.</p>'
    '</div></div></section>%s'
    % (p, a["kind"], a["kind"], a["topic"], a["title"], a["dek"], metrics, "".join(a["body"]), BRAND, p,
       cta_simple(p, "Want this for your business?", "Tell us the workflow or decision you want to tackle first.")))

# ----------------------------------------------------------------------------
# GENERATE
# ----------------------------------------------------------------------------
pages = []
pages.append(write("index.html", "%s — Build your AI-first business on Google" % BRAND,
    "%s is a Google-first AI, data and cloud transformation firm. We modernize enterprises on Google Cloud and put Gemini-powered AI agents to work — securely, with measurable ROI." % BRAND,
    home_body(), "home"))

pages.append(write("agentic-ai/index.html", "Agentic AI Services — %s" % BRAND,
    "Gemini-powered AI agents, knowledge search, decision intelligence, Workspace AI, custom apps, CX automation and AI governance.",
    hub_body(AGENTIC, "agentic-ai", "Advanced AI-first services", "Agentic AI",
             "Gemini-powered agents and intelligent systems that automate workflows, surface knowledge and turn data into decisions — deployed responsibly across your organization.", "agentic"), "agentic"))
for s in AGENTIC:
    pages.append(write("agentic-ai/%s.html" % s["slug"], "%s — %s" % (s["name"], BRAND), s["intro"][:155],
        service_body(s, "agentic-ai", "Agentic AI"), "agentic"))

pages.append(write("core-services/index.html", "Core Google Technology Services — %s" % BRAND,
    "Google Cloud migration & modernization, data analytics on BigQuery & Looker, and Google Workspace setup, migration & optimization.",
    hub_body(CORE, "core-services", "Core Google technology services", "Core Services",
             "Get the platform right first. We move workloads to Google Cloud, turn data into decisions, and modernize the way teams work in Google Workspace.", "core"), "core"))
for s in CORE:
    pages.append(write("core-services/%s.html" % s["slug"], "%s — %s" % (s["name"], BRAND), s["intro"][:155],
        service_body(s, "core-services", "Core Services"), "core"))

pages.append(write("partnership.html", "Partnership — Certified Google Cloud Partner — %s" % BRAND,
    "As a Certified Google Cloud Partner, we build across the full Google stack with co-sell, funded POCs and Marketplace access.", partnership_body(), "partnership"))
pages.append(write("about.html", "About — %s" % BRAND,
    "A Google-first AI, data and cloud transformation firm, launched and backed by Avanciers. Leadership, story and credentials.", about_body(), "about"))
pages.append(write("insights.html", "Insights — %s" % BRAND,
    "Practical points of view on building, governing and scaling AI on Google.", insights_body(), "insights"))
pages.append(write("contact.html", "Contact — %s" % BRAND,
    "Talk to us about building your AI-first business on Google. We reply within one business day.", contact_body(), "contact"))
pages.append(write("privacy.html", "Legal — Privacy, Cookies & Terms — %s" % BRAND,
    "Privacy, cookies and terms for the %s website." % BRAND, legal_body(), ""))
for a in ARTICLES:
    pages.append(write("insights/%s.html" % a["slug"], "%s — %s" % (a["title"], BRAND), a["dek"][:155], article_body(a), "insights"))

print("Generated %d pages:" % len(pages))
for p in pages:
    print("  ", p)
