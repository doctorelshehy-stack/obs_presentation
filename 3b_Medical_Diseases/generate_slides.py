#!/usr/bin/env python3
"""
Batch-generate HTML slides for Medical Obstetric Disorders presentation.
4 topics: Vomiting, Anemia, Cardiac Diseases, Thromboembolism.
Palette #10: #264653 #2a9d8f #e9c46a #f4a261 #e76f51
"""

import os

SLIDES_DIR = "/media/mohamed/projects4/projects/obstaric/raw material/3_Medical_Obstetric_Disorders/3b_Medical_Diseases/slides"
os.makedirs(SLIDES_DIR, exist_ok=True)
os.makedirs(os.path.join(SLIDES_DIR, "imgs"), exist_ok=True)

# ── Palette ──
C = {
    "dark": "#264653",
    "teal": "#2a9d8f",
    "gold": "#e9c46a",
    "orange": "#f4a261",
    "coral": "#e76f51",
    "bg": "#edf6f9",
    "white": "#ffffff",
}

# ── Appendix A snippet ──
APPENDIX_A = '''<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform=`scale(${sc})`;s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>'''

def page_badge(num):
    """Return SVG page badge HTML."""
    return f'''<svg style="position:absolute;right:32px;bottom:24px;width:48px;height:32px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="48" height="28" rx="6" fill="{C["teal"]}" />
  <text x="24" y="20" text-anchor="middle" font-family="Times New Roman,serif" font-size="16" font-weight="700" fill="{C["white"]}">{num:02d}</text>
</svg>'''

def bullet(text, color=C["dark"], size="15px", bold=False, ml="20px"):
    w = "700" if bold else "400"
    return f'''<div style="display:flex;align-items:flex-start;gap:8px;margin-left:{ml};margin-bottom:4px;">
  <span style="color:{C["teal"]};font-size:10px;margin-top:6px;">●</span>
  <span style="color:{color};font-size:{size};font-weight:{w};font-family:'Times New Roman',serif;line-height:1.35;">{text}</span>
</div>'''

def sub_bullet(text, color=C["dark"], size="14px"):
    return f'''<div style="display:flex;align-items:flex-start;gap:6px;margin-left:40px;margin-bottom:3px;">
  <span style="color:{C["orange"]};font-size:8px;margin-top:5px;">▪</span>
  <span style="color:{color};font-size:{size};font-weight:400;font-family:'Times New Roman',serif;line-height:1.3;">{text}</span>
</div>'''

def slide_wrap(body, page_num=None):
    """Wrap body content in full slide HTML."""
    badge = page_badge(page_num) if page_num is not None else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:{C["bg"]};overflow:hidden;position:relative;font-family:'Times New Roman',serif;">
{badge}
{body}
</div>
</body>
</html>'''

# ════════════════════════════════════════════════════
# SLIDE 01 – COVER PAGE
# ════════════════════════════════════════════════════
cover_body = f'''<!-- Decorative shapes -->
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" aria-hidden="true">
  <rect x="0" y="0" width="420" height="540" fill="{C["dark"]}" />
  <rect x="420" y="0" width="540" height="540" fill="{C["white"]}" />
  <!-- accent bar top right -->
  <rect x="420" y="0" width="8" height="540" fill="{C["teal"]}" />
  <!-- decorative circles -->
  <circle cx="670" cy="120" r="140" fill="none" stroke="{C["teal"]}" stroke-width="1" opacity="0.15" />
  <circle cx="720" cy="100" r="90" fill="none" stroke="{C["gold"]}" stroke-width="1" opacity="0.2" />
  <circle cx="800" cy="400" r="180" fill="none" stroke="{C["orange"]}" stroke-width="1" opacity="0.1" />
</svg>

<!-- Left side content -->
<div style="position:absolute;top:60px;left:50px;width:320px;z-index:10;">
  <div style="width:70px;height:5px;background:{C["gold"]};border-radius:3px;margin-bottom:20px;"></div>
  <p style="font-size:28px;font-weight:400;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;opacity:0.9;">Medical Disorders</p>
  <p style="font-size:48px;font-weight:700;color:{C["white"]};font-family:'Times New Roman',serif;margin:0 0 10px 0;line-height:1.1;">in Pregnancy</p>
  <div style="width:70px;height:3px;background:{C["teal"]};border-radius:2px;margin-bottom:16px;"></div>
  <p style="font-size:18px;font-weight:400;color:{C["bg"]};font-family:'Times New Roman',serif;margin:0;opacity:0.8;">Vomiting &bull; Anemia &bull; Cardiac &bull; Thromboembolism</p>
</div>

<!-- Right side -->
<div style="position:absolute;top:340px;left:480px;width:420px;z-index:10;">
  <p style="font-size:16px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;opacity:0.6;">Obstetrics &amp; Gynecology</p>
  <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;opacity:0.4;">Integrated Clinical Module</p>
</div>

<!-- Bottom info -->
<div style="position:absolute;bottom:30px;left:50px;z-index:10;">
  <p style="font-size:14px;color:{C["bg"]};font-family:'Times New Roman',serif;margin:0;opacity:0.6;">Medical Obstetric Disorders &mdash; 3b</p>
</div>'''

# ════════════════════════════════════════════════════
# SLIDE 02 – TABLE OF CONTENTS
# ════════════════════════════════════════════════════
toc_items = [
    ("01", "Vomiting with Pregnancy"),
    ("02", "Anemia with Pregnancy"),
    ("03", "Cardiac Diseases with Pregnancy"),
    ("04", "Thromboembolism during Pregnancy"),
]
toc_html = ""
for i, (num, title) in enumerate(toc_items):
    y = 100 + i * 90
    toc_html += f'''
  <div style="position:absolute;top:{y}px;left:70px;width:820px;display:flex;align-items:center;gap:20px;">
    <div style="width:50px;height:50px;border-radius:8px;background:{C["teal"]};display:flex;align-items:center;justify-content:center;">
      <span style="color:{C["white"]};font-size:22px;font-weight:700;font-family:'Times New Roman',serif;">{num}</span>
    </div>
    <div style="flex:1;border-bottom:2px solid rgba(38,70,83,0.1);padding-bottom:14px;">
      <span style="font-size:22px;font-weight:600;color:{C["dark"]};font-family:'Times New Roman',serif;">{title}</span>
    </div>
  </div>'''

toc_body = f'''<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{C["white"]}" />
  <rect x="0" y="0" width="6" height="540" fill="{C["teal"]}" />
  <rect x="850" y="0" width="110" height="540" fill="{C["bg"]}" opacity="0.4" />
</svg>
<div style="position:absolute;top:32px;left:60px;z-index:10;">
  <p style="font-size:32px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Table of Contents</p>
  <div style="width:60px;height:4px;background:{C["gold"]};border-radius:2px;margin-top:8px;"></div>
</div>
{toc_html}'''

# ════════════════════════════════════════════════════
# SECTION DIVIDER HELPER
# ════════════════════════════════════════════════════
def section_divider(num, title, subtitle=""):
    body = f'''<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{C["dark"]}" />
  <rect x="0" y="0" width="960" height="540" fill="url(#sdGrad)" opacity="0.3" />
  <defs><linearGradient id="sdGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{C["gold"]}" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="{C["teal"]}" stop-opacity="0.15"/>
  </linearGradient></defs>
  <rect x="80" y="140" width="4" height="260" fill="{C["gold"]}" />
</svg>
<div style="position:absolute;top:160px;left:120px;z-index:10;">
  <p style="font-size:80px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0;opacity:0.6;">{num}</p>
  <p style="font-size:40px;font-weight:700;color:{C["white"]};font-family:'Times New Roman',serif;margin:8px 0 0 0;">{title}</p>
  <div style="width:80px;height:4px;background:{C["teal"]};border-radius:2px;margin-top:14px;"></div>
  {f'<p style="font-size:18px;color:{C["bg"]};font-family:\'Times New Roman\',serif;margin:12px 0 0 0;opacity:0.7;">{subtitle}</p>' if subtitle else ""}
</div>'''
    return body

# ════════════════════════════════════════════════════
# CONTENT SLIDE HELPER
# ════════════════════════════════════════════════════
def content_slide(title, body_html, extra_svg=""):
    return f'''<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{C["white"]}" />
  <rect x="0" y="0" width="960" height="4" fill="{C["teal"]}" />
  <rect x="0" y="0" width="4" height="540" fill="{C["teal"]}" opacity="0.3" />
  {extra_svg}
</svg>
<div style="position:absolute;top:20px;left:50px;right:50px;z-index:10;">
  <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
    <div style="width:6px;height:28px;background:{C["gold"]};border-radius:3px;"></div>
    <p style="font-size:26px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">{title}</p>
  </div>
  <div style="width:100%;height:1px;background:{C["bg"]};margin-bottom:10px;"></div>
  {body_html}
</div>'''

# ════════════════════════════════════════════════════
# BUILD ALL SLIDES
# ════════════════════════════════════════════════════

slides = []

# ── Slide 01: Cover ──
slides.append(("slide-01.html", slide_wrap(cover_body)))

# ── Slide 02: TOC ──
slides.append(("slide-02.html", slide_wrap(toc_body, 2)))

# ════════════════════════════════════════
# SECTION 1: VOMITING WITH PREGNANCY
# ════════════════════════════════════════

# Slide 03: Section Divider
slides.append(("slide-03.html", slide_wrap(section_divider("01", "Vomiting with Pregnancy", "Emesis Gravidarum & Hyperemesis Gravidarum"), 3)))

# Slide 04: ILOs & Causes
ilo_causes = content_slide("Vomiting with Pregnancy — ILOs & Causes", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
  <div style="background:{C["bg"]};padding:12px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">ILOs</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Understand etiological pathogenesis of emesis with pregnancy</li>
      <li>Identify clinical picture of hyperemesis gravidarum</li>
      <li>Describe management of hyperemesis gravidarum</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:12px 14px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Causes of Vomiting in Pregnancy</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Pregnancy-related:</b> NVP (emesis gravidarum, hyperemesis gravidarum)</li>
      <li><b>Complications:</b> Severe preeclampsia, vesicular mole</li>
      <li><b>Gynecological:</b> Red degeneration of fibroid, torsion of ovarian cyst</li>
      <li><b>Medical:</b> Food poisoning, gastritis, cholecystitis, pyelonephritis</li>
      <li><b>Surgical:</b> Appendicitis, gall stones, peptic ulcer</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-04.html", slide_wrap(ilo_causes, 4)))

# Slide 05: Emesis Gravidarum & Hyperemesis Gravidarum definitions
eg_hg = content_slide("Emesis Gravidarum & Hyperemesis Gravidarum", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:4px;">
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-top:4px solid {C["teal"]};">
    <p style="font-size:17px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Emesis Gravidarum</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
      Nausea &amp; vomiting on getting up in the morning which starts early in pregnancy about the <b>12th week</b>. It <b>does not affect</b> the general condition.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-top:4px solid {C["coral"]};">
    <p style="font-size:17px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Hyperemesis Gravidarum (HG)</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
      Severe nausea &amp; vomiting during pregnancy leading to fluid, electrolyte and acid-base imbalance, nutritional deficiency and weight loss.
    </p>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 14px;margin-top:12px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Etiology &amp; Pathogenesis</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Unknown — may be related to: Hormonal factors, Immune dysregulation, GI dysmotility, Psychosocial factors, Infection (H. pylori), Allergic theory.
  </p>
</div>
''')
slides.append(("slide-05.html", slide_wrap(eg_hg, 5)))

# Slide 06: Etiology Part 1
etio1 = content_slide("Etiology & Pathogenesis (Part 1)", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">a. Hormonal Factors</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>NVP worse with elevated hCG (molar pregnancies, multiple gestations, Down's syndrome)</li>
      <li>Progesterone decreases smooth muscle contractility → altered gastric emptying → increased NVP</li>
      <li>Thyroid dysfunction — cross reactivity between hCG and TSH receptor</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["orange"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">b. Immune System Dysregulation</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:4px 0 0 0;">
      Immune system changes during pregnancy may contribute to the development of NVP and HG.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["gold"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">c. Gastrointestinal Dysmotility</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:4px 0 0 0;">
      Alterations in lower esophageal sphincter (LES) resting pressure and esophageal peristalsis.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">d. Psychosocial Factors</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:4px 0 0 0;">
      Early studies proposed that NVP may be a psychosomatic illness.
    </p>
  </div>
</div>
''')
slides.append(("slide-06.html", slide_wrap(etio1, 6)))

# Slide 07: Etiology Part 2 + Prevention
etio2 = content_slide("Etiology (Part 2) & Prevention", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">e. Infection</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:4px 0 0 0;">
      About <b>90%</b> of cases are infected with <i>Helicobacter pylori</i>.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">f. Allergic Theory</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:4px 0 0 0;">
      Patient is allergic to corpus luteum of pregnancy; some improve on antihistaminics and after the 1st trimester when corpus luteum degenerates.
    </p>
  </div>
</div>
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["gold"]};margin-top:12px;">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Prevention</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
    <li>Multivitamin with folic acid in early pregnancy</li>
    <li>Treating heartburn and acid reflux</li>
  </ul>
</div>
''')
slides.append(("slide-07.html", slide_wrap(etio2, 7)))

# Slide 08: Complications
comps = content_slide("Complications of Hyperemesis Gravidarum", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;">
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Wernicke encephalopathy</b> — vitamin B1 deficiency</li>
      <li><b>Bleeding/embryopathy</b> — vitamin K deficiency</li>
      <li><b>Malnutrition</b> → immunosuppression, poor wound healing, muscle wasting</li>
      <li><b>Esophageal tears</b> (Mallory-Weiss) and esophageal rupture</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;">
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Hepatic insufficiency</b></li>
      <li><b>Venous thrombosis</b></li>
      <li><b>Acute tubular necrosis</b></li>
      <li><b>Placental dysfunction</b> → preeclampsia, abruption, SGA</li>
    </ul>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 14px;margin-top:10px;">
  <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Investigations</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
    <div><b>Laboratory:</b> Kidney &amp; liver functions, CBC, hematocrit, electrolytes, blood gases</div>
    <div><b>Urine:</b> Ketonuria, oliguria, proteinuria, urine culture &amp; sensitivity</div>
    <div><b>Fundus exam</b> of eyes of mother</div>
    <div><b>Ultrasonography:</b> exclude multiple pregnancy &amp; vesicular mole</div>
  </div>
</div>
''')
slides.append(("slide-08.html", slide_wrap(comps, 8)))

# Slide 09: Management without hypovolemia - Dietary
diet = content_slide("Management (Without Hypovolemia) — Dietary Changes", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">A. Dietary Changes</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
    <li>Avoid empty or fully full stomach</li>
    <li>Meals and snacks should be eaten slowly and in small amounts every one to two hours</li>
    <li>Eliminate coffee and spicy, odorous, high-fat, acidic, or very sweet foods</li>
    <li>Instead consume protein, salty, low-fat, bland, and/or dry food</li>
    <li>Avoid iron supplements which cause gastric irritation and can provoke nausea and vomiting</li>
    <li><b>Fluids:</b> at least 30 minutes before or after solid food; better tolerated if cold, clear, and carbonated</li>
  </ul>
</div>
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["orange"]};margin-top:10px;">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">B. Trigger Avoidance</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
    Avoidance of environmental triggers: odors, heat, humidity, noise, or physical motion.
  </p>
</div>
''')
slides.append(("slide-09.html", slide_wrap(diet, 9)))

# Slide 10: Pharmacotherapy Part 1
pharm1 = content_slide("Pharmacotherapy (Part 1)", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">1. Pyridoxine (Vitamin B6)</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">10–25 mg orally every 6–8 h. Max dose 100 mg/day.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">2. Antihistamine (H1 Antagonists)</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">Decreases stimulation of the vomiting center.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">3. Doxylamine</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">10–40 mg orally.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">4. Diphenhydramine &amp; Meclizine</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">25–50 mg orally every 4–6 h.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">5. Dopamine Antagonist</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">Stimulates gastric motility and emptying.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">6. Metoclopramide</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">5–10 mg orally, IV, or IM every 6–8 h.</p>
  </div>
</div>
''')
slides.append(("slide-10.html", slide_wrap(pharm1, 10)))

# Slide 11: Pharmacotherapy Part 2
pharm2 = content_slide("Pharmacotherapy (Part 2)", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">7. Promethazine</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">12.5–25 mg every four hours.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">8. Serotonin Antagonist</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">Ondansetron.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">9. Acid-Reducing Agents</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">Antacids, H2 blockers, proton pump inhibitors.</p>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:8px 14px;margin-top:10px;">
  <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">C. Pharmacotherapy Summary</p>
  <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
    Multiple drug classes available: Vitamin B6, antihistamines (H1 antagonists), doxylamine, diphenhydramine/meclizine, dopamine antagonists, metoclopramide, promethazine, serotonin antagonists (ondansetron), and acid-reducing agents.
  </p>
</div>
''')
slides.append(("slide-11.html", slide_wrap(pharm2, 11)))

# Slide 12: Management with Hypovolemia
hypov = content_slide("Management with Hypovolemia (Hyperemesis Gravidarum)", f'''
<div style="display:grid;grid-template-columns:1fr 2fr;gap:12px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Diagnosis</p>
    <p style="font-size:12px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Symptoms:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;line-height:1.35;">Lassitude, postural dizziness, thirst.</p>
    <p style="font-size:12px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Signs:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">Weight loss, dry skin/tongue, tachycardia, hypotension, oliguria.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Treatment</p>
    <ol style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Hospitalization</b></li>
      <li><b>Replacement fluid therapy:</b> IV hydration (Saline, Ringer lactate), short gut rest, then reintroduce oral intake + pharmacotherapy</li>
      <li><b>Thiamine 100 mg daily IM/IV</b> before glucose administration to prevent Wernicke encephalopathy</li>
      <li><b>Diet:</b> Start with bananas, rice; advance as tolerated</li>
      <li><b>Pharmacotherapy:</b> Non-oral routes — Antihistamines (H1 antagonists), dopamine antagonists, serotonin antagonists. <b>Glucocorticoids</b> for refractory cases: Methylprednisolone 16 mg IV q8h or Hydrocortisone 100 mg IV twice daily</li>
      <li><b>Tube feeding and parenteral nutrition</b></li>
    </ol>
  </div>
</div>
''')
slides.append(("slide-12.html", slide_wrap(hypov, 12)))

# Slide 13: Indications for Termination
term = content_slide("Indications for Termination of Pregnancy", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Indications for Termination</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Appearance of jaundice</li>
      <li>Proteinuria &amp; progressive oliguria</li>
      <li>Creatinine rise</li>
      <li>Deterioration of general condition despite treatment</li>
      <li>Encephalopathy</li>
      <li>Fundus changes</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-left:4px solid {C["gold"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Student Activity</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
      Each group of students is requested to pick up a case of vomiting with pregnancy among outpatient attendants at outpatient clinic then identify whether she has hyperemesis with pregnancy or not with the aid of outpatient specialist.
    </p>
  </div>
</div>
''')
slides.append(("slide-13.html", slide_wrap(term, 13)))


# ════════════════════════════════════════
# SECTION 2: ANEMIA WITH PREGNANCY
# ════════════════════════════════════════

# Slide 14: Section Divider
slides.append(("slide-14.html", slide_wrap(section_divider("02", "Anemia with Pregnancy", "Iron Deficiency, Megaloblastic & Thalassemia"), 14)))

# Slide 15: ILOs, Definition, Normal Values
anemia_def = content_slide("Anemia with Pregnancy — ILOs & Definition", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">ILOs</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Classify different types of anemia with pregnancy</li>
      <li>Describe etiology and clinical features of each type</li>
      <li>Explain the management of anemia with pregnancy</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Definition</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
      Decrease in total RBCs or hemoglobin in blood during pregnancy leading to decreased oxygen carrying capacity.
    </p>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 14px;margin-top:10px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Normal Values During Pregnancy</p>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
    <div style="background:{C["bg"]};padding:8px;text-align:center;border-radius:6px;"><b>1st Trimester</b><br>&gt;11 g/dL</div>
    <div style="background:{C["bg"]};padding:8px;text-align:center;border-radius:6px;"><b>2nd Trimester</b><br>&gt;10.5 g/dL</div>
    <div style="background:{C["bg"]};padding:8px;text-align:center;border-radius:6px;"><b>3rd Trimester</b><br>&gt;11 g/dL</div>
    <div style="background:{C["bg"]};padding:8px;text-align:center;border-radius:6px;"><b>Postpartum</b><br>&gt;10 g/dL</div>
  </div>
</div>
''')
slides.append(("slide-15.html", slide_wrap(anemia_def, 15)))

# Slide 16: Signs & Symptoms, Causes
anemia_sx = content_slide("Signs, Symptoms & Causes of Anemia", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Signs &amp; Symptoms</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Headache, fatigue and lethargy</li>
      <li>Tachycardia and tachypnea</li>
      <li>Paresthesia and pallor</li>
      <li>Tongue glossitis</li>
      <li>Severe cases: congestive heart failure</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Causes</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0 0 6px 0;">
      Anemia results from impaired production, increased destruction, or blood loss.
    </p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Congenital:</b> Sickle cell anemia, thalassemia</li>
      <li><b>Acquired:</b> Iron-deficiency anemia</li>
    </ul>
  </div>
</div>
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["gold"]};margin-top:10px;">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Physiologic Anemia (Dilutional Anemia)</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Increase in overall blood volume during pregnancy occurs with plasma increasing more than RBC mass.
  </p>
</div>
''')
slides.append(("slide-16.html", slide_wrap(anemia_sx, 16)))

# Slide 17: Effects of Anemia on Pregnancy
anemia_eff = content_slide("Effects of Anemia on Pregnancy", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;">
    <p style="font-size:16px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Maternal Effects</p>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">During Pregnancy:</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Pregnancy induced hypertension</li>
      <li>Accidental hemorrhage</li>
      <li>Preterm labor</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">During Labor:</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Prolonged labor and inertia</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">During Puerperium:</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Atony and postpartum hemorrhage</li>
      <li>Puerperal sepsis</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;">
    <p style="font-size:16px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Fetal Effects</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Abortion</li>
      <li>IUGR (Intrauterine Growth Restriction)</li>
      <li>IUFD (Intrauterine Fetal Death)</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:12px 0 4px 0;">Effect of Pregnancy on Anemia</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">Aggravation of pre-existing anemia.</p>
  </div>
</div>
''')
slides.append(("slide-17.html", slide_wrap(anemia_eff, 17)))

# Slide 18: Iron Deficiency Anemia - Diagnosis
ida_dx = content_slide("Iron Deficiency Anemia — Diagnosis", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Iron Deficiency Anemia</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 8px 0;">
    Occurs from increased production of RBCs requiring a lot of iron and from inadequate intake of iron during pregnancy.
  </p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Diagnostic Findings</p>
    <table style="width:100%;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;border-collapse:collapse;">
      <tr><td style="padding:4px 0;"><b>Blood film</b></td><td style="padding:4px 0;">Microcytic hypochromic anemia</td></tr>
      <tr><td style="padding:4px 0;"><b>Serum iron</b></td><td style="padding:4px 0;">Decreased (n=60–170 µg/dl)</td></tr>
      <tr><td style="padding:4px 0;"><b>Iron binding capacity</b></td><td style="padding:4px 0;">Increased (n=200–450 µg/dl)</td></tr>
      <tr><td style="padding:4px 0;"><b>Serum ferritin</b></td><td style="padding:4px 0;">Diagnostic: &lt;30 ng/mL</td></tr>
    </table>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["gold"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Prophylactic Treatment</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Eating iron-rich foods: dark green leafy vegetables, eggs, meat, fish, dried beans, fortified grains</li>
      <li>Supplemental oral iron 27–30 mg daily</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-18.html", slide_wrap(ida_dx, 18)))

# Slide 19: Iron Therapy - Oral
ida_rx = content_slide("Iron Deficiency Anemia — Therapeutic Treatment", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Oral Iron Therapy</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Ferrous sulphate, ferrous gluconate</li>
      <li>40–200 mg elemental iron daily</li>
      <li>On empty stomach, 1 hour before meals</li>
      <li>With vitamin C (ascorbic acid) e.g. orange juice to maximize absorption</li>
      <li><b>Adverse effects:</b> GI side effects, nausea, diarrhea, constipation</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["orange"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Factors Influencing Iron Absorption</p>
    <p style="font-size:13px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Inhibit:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Calcium-rich foods, Tannins in tea, Phytates in cereals</p>
    <p style="font-size:13px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Enhance:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Heme iron, Ferrous iron (Fe²⁺), Ascorbic acid</p>
  </div>
</div>
''')
slides.append(("slide-19.html", slide_wrap(ida_rx, 19)))

# Slide 20: Parenteral Iron & Blood Transfusion
parenteral = content_slide("Parenteral Iron & Blood Transfusion", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Parenteral Iron</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
      For those who cannot be managed with oral therapy (lack of compliance, severe GI side effects, malabsorption, continuing blood loss).
    </p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>IM:</b> Low molecular weight iron dextran — painful, risk of permanent skin staining</li>
      <li><b>IV:</b> Iron hydroxide sucrose complex — for severe iron deficiency anemia</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Contraindications for IV Iron</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>History of anaphylaxis/reactions to parenteral iron</li>
      <li>First trimester of pregnancy</li>
      <li>Active acute or chronic infection</li>
      <li>Chronic liver disease</li>
    </ul>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:8px 14px;margin-top:10px;">
  <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Blood Transfusion</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Reserved for imminent cardiac compromise or low iron immediately before delivery at 37 weeks of pregnancy.
  </p>
</div>
''')
slides.append(("slide-20.html", slide_wrap(parenteral, 20)))

# Slide 21: Folic Acid Deficiency Anemia
folate = content_slide("Megaloblastic Anemia — Folic Acid Deficiency", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Daily Requirement</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">200–300 µg/day during pregnancy.</p>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">Etiology</p>
    <ol style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Inadequate intake</li>
      <li>Defective absorption</li>
      <li>Increased demand (e.g. pregnancy)</li>
      <li>Drugs: folic acid antagonists (anti-epileptic drugs)</li>
    </ol>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Clinical Picture</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">General symptoms of anemia + GIT manifestations:</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Dyspepsia</li>
      <li>Anorexia</li>
      <li>Nausea</li>
      <li>Vomiting</li>
      <li>Diarrhea</li>
    </ul>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["gold"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Investigations</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Blood film:</b> Macrocytic hyperchromic RBCs, hypersegmented neutrophilic nuclei (&gt;5 lobes)</li>
      <li><b>Serum folate:</b> Low (radioimmunoassay)</li>
      <li><b>Bone marrow:</b> Abnormal red cell precursors (megaloblasts)</li>
    </ul>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Treatment</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Diet rich in folic acid: liver, kidney, meat</li>
      <li>Folic acid 5–15 mg/day orally</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-21.html", slide_wrap(folate, 21)))

# Slide 22: Vitamin B12 Deficiency Anemia
b12 = content_slide("Vitamin B12 Deficiency Anemia", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Etiology</p>
    <ol style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Inadequate intake (rare)</li>
      <li>Deficient intrinsic factor — atrophic gastritis or gastrectomy</li>
      <li>Malabsorption syndrome</li>
      <li>Increased demand (e.g. pregnancy)</li>
    </ol>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Clinical Picture</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>General symptoms of anemia</li>
      <li>GIT manifestations (as folic acid deficiency)</li>
      <li><b>Nervous manifestations:</b>
        <ul style="margin:2px 0 0 0;padding-left:16px;">
          <li>Subacute combined degeneration</li>
          <li>Peripheral neuritis</li>
        </ul>
      </li>
    </ul>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["gold"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Investigations</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">
      As folic acid deficiency + decreased serum vitamin B12.
    </p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Treatment</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">
      Vitamin B12 IM injection.
    </p>
  </div>
</div>
''')
slides.append(("slide-22.html", slide_wrap(b12, 22)))

# Slide 23: Thalassemia
thal = content_slide("Thalassemia — Types & Effects", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Definition</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Autosomal inherited disorder from failure of production of either α chain (α-thalassemia) or β chain (β-thalassemia) of hemoglobin, replaced with other polypeptide chains.
  </p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">(I) α-Thalassemia</p>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Major (Homozygous):</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Fetus affected in utero: polyhydramnios, erythroblastosis, anemia, hydrops</li>
      <li>Fetus does not survive — inability of oxygen transfer (α-chain carries O₂)</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">Minor (Heterozygous):</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Mild progressive anemia during pregnancy.</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">(II) β-Thalassemia</p>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Major (Homozygous):</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Starts in childhood → death of patient</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">Minor (Heterozygous):</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Same as α-thalassemia minor.</p>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">Effect on Pregnancy:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Anemia severe in 2nd trimester; heart failure may occur.</p>
  </div>
</div>
''')
slides.append(("slide-23.html", slide_wrap(thal, 23)))

# Slide 24: Thalassemia - Investigations & Treatment
thal2 = content_slide("Thalassemia — Investigations & Treatment", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px;">
  <div style="background:{C["bg"]};padding:12px 14px;border-radius:8px;border-left:4px solid {C["gold"]};">
    <p style="font-size:16px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Investigations</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>Blood film:</b> Microcytic hypochromic anemia</li>
      <li><b>Electrophoresis:</b> Detect type of hemoglobin</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:12px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:16px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Treatment</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>Blood transfusion:</b> In acute attacks</li>
      <li><b>Folic acid:</b> May be indicated</li>
      <li><b>Mode of delivery:</b> Cesarean section (CS)</li>
    </ul>
  </div>
</div>
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};margin-top:16px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Student Activity</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Each student is requested to comment on a full blood count report (FBC) of an admitted pregnant woman in the department of Obstetrics &amp; Gynecology during bedside teaching part of clinical rounds.
  </p>
</div>
''')
slides.append(("slide-24.html", slide_wrap(thal2, 24)))


# ════════════════════════════════════════
# SECTION 3: CARDIAC DISEASES WITH PREGNANCY
# ════════════════════════════════════════

# Slide 25: Section Divider
slides.append(("slide-25.html", slide_wrap(section_divider("03", "Cardiac Diseases with Pregnancy", "NYHA Classification & Management"), 25)))

# Slide 26: ILOs, Physiology, Incidence & Etiology
card_ilo = content_slide("Cardiac Diseases — ILOs, Physiology & Etiology", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">ILOs</p>
    <ul style="margin:0;padding-left:16px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Correlate symptoms of cardiac pregnant patient with physiological changes</li>
      <li>Understand various etiologies of cardiac diseases with pregnancy</li>
      <li>Describe features of pregnant woman with cardiac disease</li>
      <li>Assign patient to NYHA category</li>
      <li>Explain management of pregnant women with cardiac diseases</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Physiology during Pregnancy</p>
    <ul style="margin:0;padding-left:16px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Increased cardiac output (↑ stroke volume + ↑ heart rate)</li>
      <li>Reduced systemic vascular resistance</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 4px 0;">Incidence: 1–4%</p>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">Etiology</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.4;">
      <b>Congenital:</b> ASD, VSD, PDA (most common)<br>
      <b>Acquired:</b> Rheumatic heart 85% (commonest = mitral stenosis), ischemic heart, cardiomyopathies.
    </p>
  </div>
</div>
''')
slides.append(("slide-26.html", slide_wrap(card_ilo, 26)))

# Slide 27: NYHA Classification
nyha = content_slide("NYHA Functional Classification", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px;">
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-left:6px solid {C["teal"]};">
    <p style="font-size:20px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Class I</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      No symptoms &amp; no limitation in ordinary physical activity.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-left:6px solid {C["gold"]};">
    <p style="font-size:20px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Class II</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Mild symptoms &amp; slight limitation during ordinary physical activity.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-left:6px solid {C["orange"]};">
    <p style="font-size:20px;font-weight:700;color:{C["orange"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Class III</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Marked limitation in activity, even during less than ordinary activity. Only comfortable at rest.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:14px;border-radius:8px;border-left:6px solid {C["coral"]};">
    <p style="font-size:20px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Class IV</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Severe limitations, symptoms even at rest.
    </p>
  </div>
</div>
''')
slides.append(("slide-27.html", slide_wrap(nyha, 27)))

# Slide 28: Diagnosis - History & Examination
card_dx = content_slide("Diagnosis — History & Examination", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">History</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Rheumatic fever</li>
      <li>Heart lesion</li>
      <li>Dyspnea</li>
      <li>Paroxysmal nocturnal dyspnea</li>
      <li>Orthopnea</li>
      <li>Hemoptysis</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Examination</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Murmur</li>
      <li>Accentuated heart sound</li>
      <li>Arrhythmia</li>
      <li>Central cyanosis</li>
      <li>Displaced apex beat</li>
      <li><b>Left heart failure:</b> Gallop rhythm, crepitations over lung bases, pleural effusion</li>
      <li><b>Right heart failure:</b> Congested neck veins, enlarged tender liver, ascitis, edema lower limbs</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-28.html", slide_wrap(card_dx, 28)))

# Slide 29: Investigations & Misleading Findings
card_inv = content_slide("Investigations & Misleading Findings", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Investigations</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Chest X-ray:</b> Cardiac enlargement, pulmonary congestion, pleural effusion</li>
      <li><b>ECG</b></li>
      <li><b>Echocardiography:</b> Cardiac structure and function</li>
    </ul>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Misleading Findings in Pregnancy</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Dyspnea and tachycardia</b> — common in normal pregnancy</li>
      <li><b>↑ JVP:</b> Up to +5 cm is normal due to high cardiac output</li>
      <li><b>Auscultation changes</b> from hyperkinetic circulation:
        <ul style="margin:2px 0 0 16px;">
          <li>Systolic ejection murmur</li>
          <li>Splitting of first heart sound</li>
          <li>Early diastolic murmur (↑ velocity through aortic/pulmonary valves)</li>
          <li>Third heart sound</li>
        </ul>
      </li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-29.html", slide_wrap(card_inv, 29)))

# Slide 30: Effects of Pregnancy on Heart Disease & Vice Versa
card_eff = content_slide("Effects of Pregnancy & Heart Disease", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Effect of Pregnancy on Heart Disease</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Deteriorates patient by one functional class</li>
      <li>May precipitate heart failure (peak at 28–32 weeks, 2nd/3rd/4th stage of labor)</li>
      <li>Increases risk of:
        <ul style="margin:2px 0 0 16px;">
          <li>Subacute bacterial endocarditis</li>
          <li>Thromboembolism</li>
          <li>Rheumatic attacks</li>
        </ul>
      </li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Effect of Heart Disease on Pregnancy</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;">
      <ul style="margin:0;padding-left:18px;line-height:1.5;">
        <li>Polyhydramnios</li>
        <li>Preterm labor</li>
        <li>Postpartum hemorrhage</li>
        <li>Abortion</li>
        <li>↑ Congenital malformations</li>
      </ul>
      <ul style="margin:0;padding-left:18px;line-height:1.5;">
        <li>IUGR &amp; IUFD</li>
        <li>Excess weight gain</li>
        <li>Preeclampsia</li>
        <li>Placental abruption</li>
        <li>Gestational diabetes</li>
        <li>Progressive heart failure</li>
        <li>Maternal or fetal death</li>
      </ul>
    </div>
  </div>
</div>
''')
slides.append(("slide-30.html", slide_wrap(card_eff, 30)))

# Slide 31: Management during Pregnancy
card_mgmt_preg = content_slide("Management during Pregnancy", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Antenatal Management</p>
  <ol style="margin:0;padding-left:20px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
    <li><b>Frequent antenatal visits</b> — close monitoring</li>
    <li><b>Rest</b> — adequate rest throughout pregnancy</li>
    <li><b>Prevent and treat anemia</b> — anemia may induce heart failure</li>
    <li><b>Hospitalisation</b> if signs of decompensation occur:
      <ul style="margin:2px 0 0 16px;">
        <li>Earliest evidence: tachycardia &gt;100 bpm + crepitations at lung bases</li>
        <li>Rest in hospital in last 2 weeks of pregnancy</li>
      </ul>
    </li>
    <li><b>Heparin</b> — indicated in patients with artificial valves or atrial fibrillation</li>
    <li><b>Digoxin and diuretics</b> — in cases of heart failure</li>
  </ol>
</div>
''')
slides.append(("slide-31.html", slide_wrap(card_mgmt_preg, 31)))

# Slide 32: Management during Delivery
card_mgmt_del = content_slide("Management during Delivery", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">General Principles</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>High-risk unit, multidisciplinary team (senior obstetrician, cardiologist, anesthesiologist)</li>
      <li><b>Vaginal delivery</b> allowed except in restricted cardiac output (tight MS, severe AS, primary pulmonary HTN, Eisenmenger syndrome, Marfan's with aortic root &gt;4 cm)</li>
      <li><b>Timing:</b> Usually at term; if heart failure → preterm termination. Not allowed to go postterm.</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Stage-Specific Management</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">1st Stage:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Semi-sitting position, O₂ mask, sedation, control fluid intake, IE prophylaxis.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">2nd Stage:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Sedation, shorten 2nd stage, close observation.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">3rd Stage:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Avoid ergot alkaloids. Diuretics can be given to decrease blood volume and cardiac output.</p>
  </div>
</div>
''')
slides.append(("slide-32.html", slide_wrap(card_mgmt_del, 32)))

# Slide 33: Puerperium & Contraception
card_puerp = content_slide("Puerperium & Contraception", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:30px;">
  <div style="background:{C["bg"]};padding:14px 16px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:17px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Puerperium</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>Postpartum observation for 48 hours</b> is essential — high risk of heart failure in this period</li>
      <li><b>Breastfeeding</b> is allowed unless there is heart failure</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:14px 16px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:17px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Contraception</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>Progesterone-only methods</b> can be used</li>
      <li><b>Sterilization</b> is recommended if decompensation occurred in this pregnancy</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-33.html", slide_wrap(card_puerp, 33)))


# ════════════════════════════════════════
# SECTION 4: THROMBOEMBOLISM DURING PREGNANCY
# ════════════════════════════════════════

# Slide 34: Section Divider
slides.append(("slide-34.html", slide_wrap(section_divider("04", "Thromboembolism during Pregnancy", "DVT, Thrombophlebitis & Pulmonary Embolism"), 34)))

# Slide 35: ILOs & Superficial Thrombophlebitis
thromb_ilo = content_slide("Thromboembolism — ILOs & Superficial Thrombophlebitis", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">ILOs</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Understand meaning, forms and predisposing factors of thromboembolism</li>
      <li>Describe clinical pictures of various forms</li>
      <li>Describe management of these serious clinical situations during pregnancy</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Superficial Thrombophlebitis</p>
    <p style="font-size:13px;font-weight:600;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Common sites:</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Veins of calf, thigh, inguinal region and vulva.</p>
    <p style="font-size:13px;font-weight:600;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Clinical Picture:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">Localized discomfort, erythema, superficial tenderness, pain, palpable lump/cord, low-grade fever.</p>
    <p style="font-size:13px;font-weight:600;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Complications:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">↑ Risk of DVT.</p>
    <p style="font-size:13px;font-weight:600;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Treatment:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Bed rest, analgesic, elastic support. Give heparin if DVT confirmed.</p>
  </div>
</div>
''')
slides.append(("slide-35.html", slide_wrap(thromb_ilo, 35)))

# Slide 36: DVT - Predisposing Factors
dvt_pred = content_slide("Deep Venous Thrombosis — Definition & Predisposing Factors", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Definition</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    A medical condition that occurs when a blood clot forms in a deep vein (lower leg, thigh, or pelvis).
  </p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Virchow's Triad</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Hypercoagulation</li>
      <li>Vascular damage</li>
      <li>Venous stasis</li>
    </ul>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Prothrombotic Changes in Pregnancy</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>Increased procoagulants:</b> fibrinogen, etc.</li>
      <li><b>Decreased fibrinolysis:</b> decreased protein S</li>
      <li><b>Mechanical factors:</b> compression of left iliac vein</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-36.html", slide_wrap(dvt_pred, 36)))

# Slide 37: Risk Factors & Clinical Picture of DVT
dvt_rf = content_slide("DVT — Risk Factors & Clinical Picture", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Risk Factors</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <ul style="margin:0;padding-left:18px;">
        <li>Past history of VTE</li>
        <li>Thrombophilia</li>
        <li>Old age</li>
        <li>DM</li>
        <li>Hypertension</li>
      </ul>
      <ul style="margin:0;padding-left:18px;">
        <li>Prolonged labor</li>
        <li>Cesarean section</li>
        <li>Dehydration</li>
        <li>Gross varicose veins</li>
        <li>Prolonged immobilization</li>
      </ul>
    </div>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Clinical Picture</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Most common in deep veins of left side</li>
      <li>Fever</li>
      <li>Leg swelling and pain</li>
      <li>Hotness and cyanosis of the leg</li>
      <li>Tender calf muscle</li>
      <li><b>Positive Homan's sign</b> (calf pain with foot dorsiflexion)</li>
      <li><b>50% of cases are asymptomatic</b></li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-37.html", slide_wrap(dvt_rf, 37)))

# Slide 38: Investigations for DVT
dvt_inv = content_slide("DVT — Investigations", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Diagnostic Workup</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;">
    <div style="background:{C["white"]};padding:12px;border-radius:8px;border:1px solid {C["teal"]};">
      <p style="font-weight:700;color:{C["teal"]};font-size:14px;margin:0 0 4px 0;">Imaging</p>
      <ul style="margin:0;padding-left:18px;line-height:1.5;">
        <li>Compression Duplex ultrasonography</li>
        <li>Venography</li>
        <li>MRI (suspected pelvic vein thrombosis)</li>
        <li>If PE is obvious → start heparin immediately, then perfusion (V/Q) scan, CT, MRI</li>
      </ul>
    </div>
    <div style="background:{C["white"]};padding:12px;border-radius:8px;border:1px solid {C["coral"]};">
      <p style="font-weight:700;color:{C["coral"]};font-size:14px;margin:0 0 4px 0;">Laboratory</p>
      <ul style="margin:0;padding-left:18px;line-height:1.5;">
        <li>CBC</li>
        <li>Coagulation profile</li>
        <li>D-dimer</li>
      </ul>
    </div>
  </div>
</div>
''')
slides.append(("slide-38.html", slide_wrap(dvt_inv, 38)))

# Slide 39: Management - Prophylactic & Active (stockings)
dvt_mgmt1 = content_slide("DVT — Prophylactic & Active Management", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Prophylactic Treatment</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Early ambulation after delivery</li>
      <li>Prophylactic heparin in risky cases</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Active Management</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Graduated compression stockings</b></li>
      <li><b>Start anticoagulant therapy</b> (see next slides)</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-39.html", slide_wrap(dvt_mgmt1, 39)))

# Slide 40: Unfractionated Heparin
heparin = content_slide("Anticoagulant Therapy — Unfractionated Heparin", f'''
<div style="display:grid;grid-template-columns:1fr 2fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Mode of Action</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Enhance antithrombin activity</li>
      <li>Increase factor Xa inhibitor activity</li>
      <li>Inhibit platelet aggregation</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Dose</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Start with bolus of 5000 IU</li>
      <li>IV drip 15000 IU every 12 hours for 5–10 days</li>
      <li>Then SC maintenance: 10000 IU every 8–12 hours</li>
      <li>Keep aPTT 1.5–2.5 times control</li>
    </ul>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Complications</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Hemorrhage</li>
      <li>Osteoporosis</li>
      <li>Thrombocytopenia</li>
      <li>Skin necrosis</li>
    </ul>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Antidote</p>
    <p style="font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">1% protamine sulphate solution 10 mg</p>
  </div>
</div>
''')
slides.append(("slide-40.html", slide_wrap(heparin, 40)))

# Slide 41: Low Molecular Weight Heparin
lmwh = content_slide("Low Molecular Weight Heparin (LMWH)", f'''
<div style="display:grid;grid-template-columns:2fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Enoxaparin (Clexane)</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0 0 4px 0;">
      <b>Mechanism:</b> Inhibits factor Xa activity. Given SC once or twice daily.
    </p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:6px;">
      <div style="background:{C["white"]};padding:8px 10px;border-radius:6px;border-left:3px solid {C["teal"]};">
        <p style="font-size:13px;font-weight:700;color:{C["teal"]};margin:0 0 2px 0;">Prophylactic Dose</p>
        <p style="font-size:14px;color:{C["dark"]};margin:0;">40 mg daily</p>
      </div>
      <div style="background:{C["white"]};padding:8px 10px;border-radius:6px;border-left:3px solid {C["coral"]};">
        <p style="font-size:13px;font-weight:700;color:{C["coral"]};margin:0 0 2px 0;">Therapeutic Dose</p>
        <p style="font-size:14px;color:{C["dark"]};margin:0;">1 mg/kg/12 hours</p>
      </div>
    </div>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["gold"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Advantages over UFH</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Better bioavailability</li>
      <li>Longer plasma half-life</li>
      <li>Lower risk of hemorrhagic complications</li>
    </ul>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 14px;margin-top:8px;">
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">
    <b>Duration:</b> Treatment in relation to pregnancy should continue for <b>6–12 weeks after delivery</b>.
  </p>
</div>
''')
slides.append(("slide-41.html", slide_wrap(lmwh, 41)))

# Slide 42: Pulmonary Embolism - Clinical Picture & Investigations
pe_dx = content_slide("Pulmonary Embolism — Clinical Picture & Investigations", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Clinical Picture</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Symptoms:</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Dyspnea</li>
      <li>Cough</li>
      <li>Chest pain</li>
      <li>Frothy blood-stained sputum</li>
      <li>Hemoptysis</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">Signs:</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Mild pyrexia, tachycardia, tachypnea</li>
      <li>Cyanosis</li>
      <li>Raised JVP</li>
      <li>Pleural friction rub</li>
      <li>Pleural effusion</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Investigations</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Arterial blood gases (hypoxia &amp; hypercapnea)</li>
      <li>ECG</li>
      <li>Ventilation/perfusion (V/Q) imaging</li>
      <li>Chest spiral CT</li>
      <li>Pulmonary angiography</li>
      <li>MRA (magnetic resonance angiography)</li>
      <li>Investigations for DVT</li>
    </ul>
  </div>
</div>
''')
slides.append(("slide-42.html", slide_wrap(pe_dx, 42)))

# Slide 43: Pulmonary Embolism - Treatment
pe_rx = content_slide("Pulmonary Embolism — Treatment", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["coral"]};">
  <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Treatment of Pulmonary Embolism</p>
  <ol style="margin:0;padding-left:20px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
    <li><b>Stabilization of the patient</b></li>
    <li><b>Start immediately anticoagulant</b> — IV unfractionated heparin is the preferred treatment</li>
    <li><b>IVC filter</b> (inferior vena cava filter)</li>
    <li><b>Thrombolysis</b></li>
    <li><b>Pulmonary embolectomy</b></li>
  </ol>
</div>
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};margin-top:12px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Student Activity</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Each group of students is requested to design an algorithm for diagnosis &amp; management of thromboembolic disorders of pregnancy to be supervised by the tutor of bedside teaching part of students clinical rounds.
  </p>
</div>
''')
slides.append(("slide-43.html", slide_wrap(pe_rx, 43)))


# ════════════════════════════════════════
# SUMMARY / CLOSING SLIDE
# ════════════════════════════════════════

summary_body = f'''<svg style="position:absolute;top:0;left:0;width:960px;height:540px;z-index:0;" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{C["dark"]}" />
  <rect x="0" y="460" width="960" height="80" fill="{C["teal"]}" opacity="0.2" />
  <circle cx="800" cy="380" r="200" fill="none" stroke="{C["gold"]}" stroke-width="1" opacity="0.1" />
</svg>
<div style="position:absolute;top:50px;left:60px;right:60px;z-index:10;">
  <p style="font-size:44px;font-weight:700;color:{C["white"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Key Takeaways</p>
  <div style="width:80px;height:4px;background:{C["gold"]};border-radius:2px;margin-bottom:24px;"></div>
  
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
    <div style="background:rgba(42,157,143,0.15);padding:14px 16px;border-radius:8px;border-left:4px solid {C["teal"]};">
      <p style="font-size:18px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Vomiting with Pregnancy</p>
      <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["bg"]};font-family:'Times New Roman',serif;line-height:1.45;">
        <li>Hyperemesis gravidarum → fluid/electrolyte imbalance, weight loss</li>
        <li>Multifactorial etiology: hormonal, immune, GI, H. pylori, allergic</li>
        <li>Management: dietary, trigger avoidance, pharmacotherapy, IV hydration</li>
        <li>Terminate if jaundice, oliguria, encephalopathy, fundus changes</li>
      </ul>
    </div>
    <div style="background:rgba(42,157,143,0.15);padding:14px 16px;border-radius:8px;border-left:4px solid {C["gold"]};">
      <p style="font-size:18px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Anemia with Pregnancy</p>
      <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["bg"]};font-family:'Times New Roman',serif;line-height:1.45;">
        <li>Iron deficiency, megaloblastic (folate/B12), thalassemia</li>
        <li>Oral/parenteral iron, folic acid, B12 injections</li>
        <li>Thalassemia → blood transfusion, CS delivery</li>
      </ul>
    </div>
    <div style="background:rgba(42,157,143,0.15);padding:14px 16px;border-radius:8px;border-left:4px solid {C["teal"]};">
      <p style="font-size:18px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Cardiac Diseases</p>
      <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["bg"]};font-family:'Times New Roman',serif;line-height:1.45;">
        <li>NYHA classification guides management</li>
        <li>Peak heart failure risk: 28–32 weeks &amp; labor stages</li>
        <li>Multidisciplinary care, vaginal delivery unless contraindicated</li>
      </ul>
    </div>
    <div style="background:rgba(42,157,143,0.15);padding:14px 16px;border-radius:8px;border-left:4px solid {C["gold"]};">
      <p style="font-size:18px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Thromboembolism</p>
      <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["bg"]};font-family:'Times New Roman',serif;line-height:1.45;">
        <li>DVT: Virchow's triad, 50% asymptomatic, Homan's sign</li>
        <li>Anticoagulation: UFH or LMWH (enoxaparin)</li>
        <li>PE: immediate heparin, IVC filter, thrombolysis, embolectomy</li>
      </ul>
    </div>
  </div>
  
  <div style="text-align:center;margin-top:18px;">
    <p style="font-size:16px;color:{C["bg"]};font-family:'Times New Roman',serif;opacity:0.7;">Medical Obstetric Disorders — Integrated Clinical Module</p>
  </div>
</div>'''

slides.append(("slide-44.html", slide_wrap(summary_body, 44)))

# ════════════════════════════════════════
# WRITE ALL SLIDES
# ════════════════════════════════════════

for fname, html in slides:
    fpath = os.path.join(SLIDES_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {fpath}")

print(f"\nTotal: {len(slides)} slides generated.")
