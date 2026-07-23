#!/usr/bin/env python3
"""Generate all HTML slides for the combined Obstetric Disorders presentation."""
import os

SLIDES_DIR = "/media/mohamed/projects4/projects/obstaric/raw material/3_Medical_Obstetric_Disorders/3d_Multiple_Pregnancy_Preterm/slides"
IMGS_DIR = os.path.join(SLIDES_DIR, "imgs")
os.makedirs(SLIDES_DIR, exist_ok=True)

# Colors from Palette 10 (Education & Charts)
DARK = "#264653"
TEAL = "#2a9d8f"
YELLOW = "#e9c46a"
ORANGE = "#f4a261"
RED = "#e76f51"
WHITE = "#ffffff"
LIGHT = "#edf2f4"

def page_badge(page_num):
    """Return SVG page number badge HTML."""
    return f'''<div style="position:absolute; right:32px; bottom:24px; z-index:100; width:44px; height:44px;">
<svg width="44" height="44" viewBox="0 0 44 44" aria-hidden="true">
  <circle cx="22" cy="22" r="20" fill="{DARK}" stroke="{TEAL}" stroke-width="2"/>
  <text x="22" y="28" text-anchor="middle" fill="{WHITE}" font-family="Times New Roman, serif" font-size="18" font-weight="bold">{page_num}</text>
</svg>
</div>'''

def head(title):
    """Return HTML head with Appendix A scaling snippet."""
    return f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Slide</title>
<style>
html, body {{ margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }}
.slide-content {{ width:960px; height:540px; position:relative; transform-origin:center center; }}
</style>
<script>
function scaleSlide(){{const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:{WHITE};overflow:hidden;position:relative;font-family:'Times New Roman',serif;">
'''

def foot():
    return "</div>\n</body>\n</html>"

def write_slide(num, body):
    path = os.path.join(SLIDES_DIR, f"slide-{num:02d}.html")
    with open(path, 'w') as f:
        f.write(body)
    print(f"  Written {path}")

# ═══════════════════════════════════════════════════════════════
# SLIDE 01 - COVER
# ═══════════════════════════════════════════════════════════════
s = head("Cover")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{LIGHT};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{LIGHT}"/>
  <circle cx="-40" cy="-40" r="200" fill="{TEAL}" opacity="0.12"/>
  <circle cx="900" cy="480" r="180" fill="{RED}" opacity="0.10"/>
  <circle cx="480" cy="270" r="120" fill="{YELLOW}" opacity="0.08"/>
  <rect x="0" y="532" width="960" height="8" fill="{TEAL}"/>
  <rect x="70" y="110" width="80" height="5" fill="{YELLOW}"/>
</svg>
</div>
<div style="position:absolute; top:70px; left:80px; width:500px;">
  <p style="font-size:28px; color:{TEAL}; margin:0; font-weight:400; letter-spacing:2px;">3_Medical_Obstetric_Disorders</p>
  <p style="font-size:52px; color:{DARK}; margin:20px 0 0 0; font-weight:700; line-height:1.1;">Multiple Pregnancy,<br>Preterm Labor &amp;<br>Premature Rupture of Membranes</p>
  <div style="width:80px; height:4px; background:{TEAL}; margin:24px 0; border-radius:2px;"></div>
  <p style="font-size:20px; color:{RED}; margin:0; font-weight:400;">Obstetrics &amp; Gynecology — Study Material</p>
  <p style="font-size:16px; color:{DARK}; margin:12px 0 0 0; opacity:0.6;">Comprehensive Lecture Notes — Full Content Preserved</p>
</div>
<div style="position:absolute; right:60px; bottom:60px; width:300px; height:200px; border-radius:12px; overflow:hidden; opacity:0.9;">
  <img src="imgs/cover.png" alt="Cover illustration" style="width:100%; height:100%; object-fit:cover; border-radius:12px; border:2px solid {TEAL};">
</div>'''
s += foot()
write_slide(1, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 02 - TABLE OF CONTENTS
# ═══════════════════════════════════════════════════════════════
s = head("TOC")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="8" height="540" fill="{TEAL}"/>
  <rect x="0" y="0" width="960" height="540" fill="none"/>
</svg>
</div>
<p style="position:absolute; top:24px; left:40px; font-size:32px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Table of Contents</p>
<div style="position:absolute; top:62px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>'''

toc_items = [
    ("1", "Multiple Pregnancy", "04"),
    ("", "Definition & Terminology", ""),
    ("", "Monozygotic & Dizygotic Twins", ""),
    ("", "Incidence, Risk Factors & Classification", ""),
    ("", "Diagnosis & Ultrasound Findings", ""),
    ("", "Management & Delivery", ""),
    ("", "Maternal & Fetal Complications", ""),
    ("", "Twin-to-Twin Transfusion Syndrome", ""),
    ("2", "Preterm Labor", "16"),
    ("", "Definition & Risk Factors", ""),
    ("", "Diagnosis & Investigations", ""),
    ("", "Management & Tocolytic Therapy", ""),
    ("", "Antibiotic Therapy & Mode of Delivery", ""),
    ("3", "Premature Rupture of Membranes", "27"),
    ("", "Definition, Etiology & Diagnosis", ""),
    ("", "Management & Chorioamnionitis", ""),
]

y = 90
for i, (section, title, pnum) in enumerate(toc_items):
    color = DARK if section else TEAL
    fw = "700" if section else "400"
    sz = "18px" if section else "15px"
    if section:
        s += f'''<p style="position:absolute; top:{y}px; left:40px; font-size:20px; font-weight:700; color:{TEAL}; margin:0; z-index:10;">Section {section}</p>'''
        y += 22
    else:
        s += f'''<p style="position:absolute; top:{y}px; left:60px; font-size:{sz}; font-weight:{fw}; color:{color}; margin:0; z-index:10;">• {title}</p>'''
        y += 26

s += page_badge(2)
s += foot()
write_slide(2, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 03 - SECTION 1 DIVIDER: MULTIPLE PREGNANCY
# ═══════════════════════════════════════════════════════════════
s = head("Section 1")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{DARK};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{DARK}"/>
  <circle cx="800" cy="100" r="250" fill="{TEAL}" opacity="0.08"/>
  <circle cx="200" cy="400" r="180" fill="{YELLOW}" opacity="0.06"/>
  <rect x="60" y="120" width="80" height="5" fill="{YELLOW}"/>
</svg>
</div>
<p style="position:absolute; top:80px; left:60px; font-size:80px; font-weight:700; color:{TEAL}; margin:0; z-index:10;">01</p>
<p style="position:absolute; top:150px; left:60px; font-size:42px; font-weight:700; color:{WHITE}; margin:0; z-index:10;">Multiple Pregnancy</p>
<p style="position:absolute; top:210px; left:60px; font-size:18px; color:{YELLOW}; margin:0; z-index:10; opacity:0.8;">Definition • Classification • Diagnosis • Management • Complications</p>'''
s += page_badge(3)
s += foot()
write_slide(3, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 04 - DEFINITION & TERMINOLOGY
# ═══════════════════════════════════════════════════════════════
s = head("Definition")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
  <circle cx="900" cy="500" r="120" fill="{TEAL}" opacity="0.06"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Definition &amp; Important Terminology</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<p style="position:absolute; top:95px; left:40px; font-size:18px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Definition</p>
<p style="position:absolute; top:120px; left:40px; font-size:16px; color:{DARK}; margin:0; z-index:10; max-width:880px;">A pregnancy with more than 1 fetus inside the uterus.</p>

<p style="position:absolute; top:165px; left:40px; font-size:18px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Important Terminology</p>

<div style="position:absolute; top:195px; left:40px; width:880px; height:auto; z-index:10;">
<table style="width:100%; border-collapse:collapse; font-size:14px; color:{DARK};">
  <tr style="background:{DARK}; color:{WHITE};">
    <th style="padding:8px 12px; border:1px solid {DARK}; text-align:left; font-weight:700;">Term</th>
    <th style="padding:8px 12px; border:1px solid {DARK}; text-align:left; font-weight:700;">Definition</th>
  </tr>
  <tr>
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700; color:{TEAL};">Zygosity</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">The genetic make up of a twin pregnancy</td>
  </tr>
  <tr style="background:#f8fafa;">
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700; color:{TEAL};">Monozygotic twins</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Result from division of a single zygote. Share the same genetic material. Identical twins.</td>
  </tr>
  <tr>
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700; color:{TEAL};">Dizygotic twins</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Result from 2 separate eggs fertilized by 2 separate sperm. Share approximately 50% of the genetic material. Fraternal twins.</td>
  </tr>
  <tr style="background:#f8fafa;">
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700; color:{TEAL};">Chorionicity</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">The number of chorions (equal to the number of placentas)</td>
  </tr>
  <tr>
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700; color:{TEAL};">Amnionicity</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">The number of amnions surrounding the fetuses</td>
  </tr>
</table>
</div>'''
s += page_badge(4)
s += foot()
write_slide(4, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 05 - MONOZYGOTIC & DIZYGOTIC TWINS
# ═══════════════════════════════════════════════════════════════
s = head("Twins")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Monozygotic &amp; Dizygotic Twins</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:40px; width:880px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
  <div style="background:#f8fafa; border-radius:8px; padding:16px; border-left:4px solid {TEAL};">
    <p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Monozygotic (Identical)</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>Division of a single zygote</li>
      <li>Share <b>100%</b> genetic material</li>
      <li>Identical twins</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:16px; border-left:4px solid {ORANGE};">
    <p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Dizygotic (Fraternal)</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>2 eggs × 2 separate sperm</li>
      <li>Share ~50% genetic material</li>
      <li>Fraternal twins</li>
    </ul>
  </div>
</div>
</div>

<div style="position:absolute; top:230px; left:40px; width:880px; z-index:10;">
<p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Incidence</p>
<p style="font-size:15px; color:{DARK}; margin:0;">Twins: 1 in 80 pregnancies. Triplets: 1 in 80² (1 in 6400).</p>
</div>

<div style="position:absolute; top:290px; left:40px; width:880px; z-index:10;">
<p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Risk Factors</p>
<ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
  <li>Prior history of multiple pregnancies</li>
  <li>History of twins in the maternal family</li>
  <li>Maternal weight and height — BMI ≥ 30 kg/m² and ≥ 165 cm → ↑ risk for dizygotic twin births</li>
  <li>↑ Maternal age</li>
  <li>↑ Parity</li>
  <li>Racial and ethnic variation</li>
</ul>
</div>

<div style="position:absolute; right:30px; bottom:55px; width:180px; height:120px; border-radius:8px; overflow:hidden; border:1px solid #ddd;">
  <img src="imgs/twins-types.png" alt="Twins types diagram" style="width:100%; height:100%; object-fit:cover;">
</div>'''
s += page_badge(5)
s += foot()
write_slide(5, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 06 - CLASSIFICATION (TIMING OF CLEAVAGE)
# ═══════════════════════════════════════════════════════════════
s = head("Classification")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Classification of Multiple Pregnancy</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<p style="position:absolute; top:95px; left:40px; font-size:18px; font-weight:700; color:{TEAL}; margin:0; z-index:10;">Dizygotic Twins</p>
<p style="position:absolute; top:120px; left:40px; font-size:15px; color:{DARK}; margin:0; z-index:10;">Always dichorionic-diamniotic.</p>

<p style="position:absolute; top:155px; left:40px; font-size:18px; font-weight:700; color:{TEAL}; margin:0; z-index:10;">Monozygotic Twins — Classified by Timing of Cleavage</p>

<div style="position:absolute; top:185px; left:40px; width:880px; z-index:10;">
<table style="width:100%; border-collapse:collapse; font-size:14px; color:{DARK};">
  <tr style="background:{DARK}; color:{WHITE};">
    <th style="padding:8px 12px; border:1px solid {DARK}; text-align:left;">Timing</th>
    <th style="padding:8px 12px; border:1px solid {DARK}; text-align:left;">Type</th>
    <th style="padding:8px 12px; border:1px solid {DARK}; text-align:left;">Features</th>
  </tr>
  <tr>
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700;">First 3 days</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Dichorionic Diamniotic</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Lambda sign, thick membrane, 2 placentae</td>
  </tr>
  <tr style="background:#f8fafa;">
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700;">4–8 days</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Monochorionic Diamniotic</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">T sign, thin membrane, single placenta</td>
  </tr>
  <tr>
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700;">8–12 days</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Monochorionic Monoamniotic</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">No intertwin membrane</td>
  </tr>
  <tr style="background:#f8fafa;">
    <td style="padding:6px 12px; border:1px solid #ddd; font-weight:700;">After 12 days</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Conjoined Twins</td>
    <td style="padding:6px 12px; border:1px solid #ddd;">Incomplete separation</td>
  </tr>
</table>
</div>

<div style="position:absolute; top:370px; left:40px; width:880px; z-index:10;">
<p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Chorionicity &amp; Amnionicity Diagram</p>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-left:4px solid {TEAL};">
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Dichorionic-Diamniotic</p>
    <p style="font-size:13px; color:{DARK}; margin:0;">Lambda sign: thick, triangular protrusion of tissue leading up to the intertwin membrane. Thick intertwin membrane. 2 separate placentae.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-left:4px solid {ORANGE};">
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Monochorionic-Diamniotic</p>
    <p style="font-size:13px; color:{DARK}; margin:0;">T sign: the interface between 2 amniotic membranes. Thin intertwin membrane. Single placenta.</p>
  </div>
</div>
<p style="font-size:14px; color:{RED}; margin:8px 0 0 0; font-weight:700;">Monochorionic-Monoamniotic: No intertwin membrane.</p>
</div>'''
s += page_badge(6)
s += foot()
write_slide(6, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 07 - DIAGNOSIS: SIGNS & SYMPTOMS
# ═══════════════════════════════════════════════════════════════
s = head("Diagnosis")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Diagnosis of Multiple Pregnancy</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:40px; width:880px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {TEAL};">
    <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Signs &amp; Symptoms</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>Exaggerated early pregnancy symptoms (e.g. hyperemesis gravidarum)</li>
      <li>Symphyseal-fundal height greater than expected for gestational age</li>
      <li>Abdominal overdistension</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {ORANGE};">
    <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Abdominal Examination</p>
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Inspection:</p>
    <p style="font-size:14px; color:{DARK}; margin:0 0 6px 0;">Oversized uterus.</p>
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Palpation:</p>
    <p style="font-size:14px; color:{DARK}; margin:0 0 6px 0;">Fundal level higher than the period of amenorrhea. Fundal, umbilical and first pelvic grips: can detect multiple fetal poles (at least 3 poles should be palpated). Fetal limbs felt as multiple knobs.</p>
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Auscultation:</p>
    <p style="font-size:14px; color:{DARK}; margin:0;">Fetal heart sounds heard simultaneously by 2 observers with minimum difference of 10 beats/minute. Arnaux sign: superimposition of 2 fetal heart sounds produces a gallop sound.</p>
  </div>
</div>
</div>

<div style="position:absolute; top:320px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {RED};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Ultrasound Findings</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>≥ 2 fetuses and ≥ 2 heart activities</li>
    <li>Diagnosis of congenital anomalies and placenta previa</li>
  </ul>
</div>
</div>'''
s += page_badge(7)
s += foot()
write_slide(7, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 08 - MANAGEMENT: ANTENATAL CARE
# ═══════════════════════════════════════════════════════════════
s = head("Antenatal")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Management — Antenatal Care</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<p style="font-size:16px; color:{RED}; font-weight:700; margin:0 0 12px 0;">Multiple pregnancy is considered a high-risk pregnancy.</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
    <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Antenatal Care Measures</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>More frequent prenatal visits</li>
      <li>More frequent ultrasounds to monitor fetal growth</li>
      <li>Adequate maternal nutrition</li>
      <li>Monitoring for maternal complications (e.g. gestational diabetes and preeclampsia)</li>
      <li>Monitoring for fetal complications (e.g. congenital anomalies)</li>
      <li>Prevention of preterm delivery</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {ORANGE};">
    <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Obstetric Care</p>
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Route of Delivery</p>
    <ul style="margin:0; padding-left:20px; font-size:13px; color:{DARK};">
      <li>Non-vertex presenting fetus / higher-order multiples (triplets) → Cesarean section</li>
      <li>Monochorionic-monoamniotic twins → Cesarean section</li>
      <li>Vertex/vertex → vaginal delivery</li>
      <li>Vertex/nonvertex → vaginal delivery of 1st twin, then ECV or IPV and breech extraction of 2nd twin</li>
    </ul>
  </div>
</div>
</div>

<div style="position:absolute; top:330px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {YELLOW};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Timing of Delivery in Uncomplicated Cases</p>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; font-size:13px;">
    <div style="background:{DARK}; color:{WHITE}; border-radius:6px; padding:8px; text-align:center;">
      <p style="font-weight:700; margin:0; font-size:14px;">Dichorionic-Diamniotic</p>
      <p style="margin:4px 0 0 0;">38<sup>0/7</sup> – 38<sup>6/7</sup> weeks</p>
    </div>
    <div style="background:{TEAL}; color:{WHITE}; border-radius:6px; padding:8px; text-align:center;">
      <p style="font-weight:700; margin:0; font-size:14px;">Monochorionic-Diamniotic</p>
      <p style="margin:4px 0 0 0;">34<sup>0/7</sup> – 37<sup>6/7</sup> weeks</p>
    </div>
    <div style="background:{RED}; color:{WHITE}; border-radius:6px; padding:8px; text-align:center;">
      <p style="font-weight:700; margin:0; font-size:14px;">Monochorionic-Monoamniotic</p>
      <p style="margin:4px 0 0 0;">32<sup>0/7</sup> – 34<sup>0/7</sup> weeks</p>
    </div>
  </div>
</div>
</div>'''
s += page_badge(8)
s += foot()
write_slide(8, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 09 - THIRD STAGE & COMPLICATIONS
# ═══════════════════════════════════════════════════════════════
s = head("ThirdStage")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Third Stage &amp; Complications</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">In the Third Stage</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Examine the placenta and the membranes for zygosity</li>
    <li>If retained, manual removal may be performed</li>
    <li>Exploration of genital tract for retained products and lacerations</li>
    <li>Guard against postpartum hemorrhage by uterine massage &amp; ecbolics</li>
    <li>Guard against puerperal sepsis</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:210px; left:40px; width:880px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {RED};">
    <p style="font-size:17px; font-weight:700; color:{RED}; margin:0 0 8px 0;">Maternal Complications</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>Hyperemesis gravidarum</li>
      <li>Gestational diabetes mellitus</li>
      <li>Hypertensive pregnancy disorders (e.g. preeclampsia)</li>
      <li>Anemia</li>
      <li>Excessive weight gain</li>
      <li>Postpartum hemorrhage (uterine atony or lacerations)</li>
      <li>Miscarriages</li>
      <li>Placental abnormalities (e.g., placenta previa)</li>
      <li>Increased risk for cesarean delivery</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {ORANGE};">
    <p style="font-size:17px; font-weight:700; color:{ORANGE}; margin:0 0 8px 0;">Fetal Complications</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>Preterm labor and birth</li>
      <li>Congenital anomalies</li>
      <li>Low birth weight</li>
      <li>Discordant growth</li>
      <li>Neonatal death</li>
    </ul>
  </div>
</div>
</div>'''
s += page_badge(9)
s += foot()
write_slide(9, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 10 - TWIN-TO-TWIN TRANSFUSION SYNDROME
# ═══════════════════════════════════════════════════════════════
s = head("TTTS")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Twin-to-Twin Transfusion Syndrome (TTTS)</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<p style="font-size:16px; color:{DARK}; margin:0 0 8px 0;">Occurs in <b>10%–15%</b> of monochorionic twins.</p>
<p style="font-size:15px; color:{DARK}; margin:0 0 12px 0;">Due to <b>arterio-venous anastomosis</b> with imbalanced blood flow. Blood flows in a fixed direction from 1 fetus (donor) to another (recipient).</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
    <p style="font-size:17px; font-weight:700; color:{TEAL}; margin:0 0 6px 0;">Donor Twin</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li style="margin-bottom:4px;">Anemia</li>
      <li style="margin-bottom:4px;">Growth restriction</li>
      <li>Oligohydramnios</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {RED};">
    <p style="font-size:17px; font-weight:700; color:{RED}; margin:0 0 6px 0;">Recipient Twin</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li style="margin-bottom:4px;">Polycythemia</li>
      <li style="margin-bottom:4px;">Macrosomia</li>
      <li>Polyhydramnios</li>
    </ul>
  </div>
</div>
</div>

<div style="position:absolute; top:300px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {ORANGE};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Management</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Amnioreduction</li>
    <li>Fetoscopic laser occlusion of placental vessels</li>
  </ul>
</div>
</div>

<div style="position:absolute; right:30px; bottom:55px; width:170px; height:100px; border-radius:8px; overflow:hidden; border:1px solid #ddd;">
  <img src="imgs/ttts.png" alt="TTTS diagram" style="width:100%; height:100%; object-fit:cover;">
</div>'''
s += page_badge(10)
s += foot()
write_slide(10, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 11 - SECTION 2 DIVIDER: PRETERM LABOR
# ═══════════════════════════════════════════════════════════════
s = head("Section 2")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{DARK};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{DARK}"/>
  <circle cx="800" cy="100" r="250" fill="{TEAL}" opacity="0.08"/>
  <circle cx="200" cy="400" r="180" fill="{ORANGE}" opacity="0.06"/>
  <rect x="60" y="120" width="80" height="5" fill="{YELLOW}"/>
</svg>
</div>
<p style="position:absolute; top:80px; left:60px; font-size:80px; font-weight:700; color:{TEAL}; margin:0; z-index:10;">02</p>
<p style="position:absolute; top:150px; left:60px; font-size:42px; font-weight:700; color:{WHITE}; margin:0; z-index:10;">Preterm Labor</p>
<p style="position:absolute; top:210px; left:60px; font-size:18px; color:{YELLOW}; margin:0; z-index:10; opacity:0.8;">Definition • Etiology • Diagnosis • Management • Tocolytic Therapy</p>'''
s += page_badge(11)
s += foot()
write_slide(11, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 12 - PRETERM LABOR: DEFINITION
# ═══════════════════════════════════════════════════════════════
s = head("PTL Definition")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Preterm Labor — Definition</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:16px; border-left:4px solid {RED};">
  <p style="font-size:16px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Definition</p>
  <p style="font-size:15px; color:{DARK}; margin:0 0 6px 0;">Regular uterine contractions associated with cervical change occurring between <b>20–37 weeks</b> gestation.</p>
  <p style="font-size:15px; color:{DARK}; margin:0;">It means onset of labor (regular painful uterine contractions associated with effacement and dilatation of the cervix) prior to completion of 37 weeks.</p>
</div>
</div>

<div style="position:absolute; top:190px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:16px; border-left:4px solid {ORANGE};">
  <p style="font-size:16px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Premature Infant</p>
  <p style="font-size:15px; color:{DARK}; margin:0;">Infant born before 37 completed weeks of gestation.</p>
</div>
</div>

<div style="position:absolute; top:260px; left:40px; width:880px; z-index:10;">
<p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Causes &amp; Risk Factors</p>
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-top:3px solid {RED};">
    <p style="font-size:15px; font-weight:700; color:{RED}; margin:0 0 6px 0;">Maternal Causes</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:{DARK};">
      <li>Most common: idiopathic</li>
      <li>Previous preterm labor</li>
      <li>Local or systemic infection</li>
      <li>Congenital anomalies of uterus &amp; incompetent os</li>
      <li>Smoking, obesity, diabetes, low socioeconomic status</li>
      <li>Uterine overdistension (multiple gestations, polyhydramnios)</li>
      <li>Maternal age: &lt;18 or &gt;35 years</li>
      <li>2nd- or 3rd-trimester bleeding; placenta previa or abruption</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-top:3px solid {TEAL};">
    <p style="font-size:15px; font-weight:700; color:{TEAL}; margin:0 0 6px 0;">Fetal Factors</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:{DARK};">
      <li>Fetal anomalies</li>
      <li>IUGR</li>
    </ul>
  </div>
</div>
</div>'''
s += page_badge(12)
s += foot()
write_slide(12, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 13 - DIAGNOSIS OF PRETERM LABOR
# ═══════════════════════════════════════════════════════════════
s = head("PTL Diagnosis")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Diagnosis of Preterm Labor</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:40px; width:880px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {RED};">
    <p style="font-size:17px; font-weight:700; color:{RED}; margin:0 0 6px 0;">Symptoms &amp; Signs</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>Uterine contractions: 4 in 20 min or 8 in 60 min</li>
      <li>Lower back pain</li>
      <li>Passage of blood-stained vaginal discharge (show)</li>
      <li>Sensation of pelvic pressure</li>
      <li>Bulging membranes / rupture of membranes</li>
    </ul>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {TEAL};">
    <p style="font-size:17px; font-weight:700; color:{TEAL}; margin:0 0 6px 0;">Investigations — Ultrasound</p>
    <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
      <li>Identify obvious fetal malformations</li>
      <li>Identify abnormalities in fetal growth</li>
      <li>Identify abnormalities in amniotic fluid volume (oligo- or polyhydramnios)</li>
      <li>Confirm fetal presentation</li>
      <li>Evaluate the placenta and its location</li>
    </ul>
  </div>
</div>
</div>

<div style="position:absolute; top:275px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {ORANGE};">
  <p style="font-size:17px; font-weight:700; color:{ORANGE}; margin:0 0 8px 0;">Transvaginal Ultrasound (TVUS)</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Dilatation of cervix &gt;2 cm</li>
    <li>Shape of cervix: Normal = T shape → Y → V → U shape (PTL progression)</li>
    <li>Bulging of fetal membranes into a widened internal os in PTL</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:385px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {TEAL};">
  <p style="font-size:17px; font-weight:700; color:{TEAL}; margin:0 0 4px 0;">Fetal Fibronectin Test</p>
  <p style="font-size:14px; color:{DARK}; margin:0;">Fibronectin assay: presence of fibronectin glycoprotein produced by fetal amnion in the cervico-vaginal discharge between 24 and 34 weeks is a predictor of PTL.</p>
</div>
</div>

<div style="position:absolute; right:25px; bottom:55px; width:160px; height:90px; border-radius:8px; overflow:hidden; border:1px solid #ddd;">
  <img src="imgs/cervix.png" alt="Cervix shape diagram" style="width:100%; height:100%; object-fit:cover;">
</div>'''
s += page_badge(13)
s += foot()
write_slide(13, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 14 - MANAGEMENT: PROPHYLACTIC
# ═══════════════════════════════════════════════════════════════
s = head("PTL Prophylactic")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Management of Preterm Labor</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
  <p style="font-size:18px; font-weight:700; color:{TEAL}; margin:0 0 8px 0;">Prophylactic (Preventive) Management</p>
  <ul style="margin:0; padding-left:20px; font-size:15px; color:{DARK};">
    <li>Stop smoking</li>
    <li>Cerclage surgery if cervical incompetence is present</li>
    <li>Progesterone</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:195px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {ORANGE};">
  <p style="font-size:18px; font-weight:700; color:{ORANGE}; margin:0 0 8px 0;">Curative Management</p>
  <p style="font-size:15px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">I. Bed Rest and Hydration</p>
  <p style="font-size:14px; color:{DARK}; margin:0 0 12px 0;">Hydration, both orally and intravenously.</p>

  <p style="font-size:15px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">II. Drug Therapy</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Antenatal corticosteroids</li>
    <li>Tocolytic therapy</li>
    <li>Antibiotic therapy</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:370px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {YELLOW};">
  <p style="font-size:18px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Antenatal Corticosteroids</p>
  <p style="font-size:14px; color:{DARK}; margin:0 0 8px 0;">Corticosteroids decrease the chance of respiratory distress syndrome and other prematurity complications.</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:14px;">
    <div style="background:{DARK}; color:{WHITE}; border-radius:6px; padding:10px; text-align:center;">
      <p style="font-weight:700; margin:0 0 4px 0;">Betamethasone</p>
      <p style="margin:0;">2 doses of 12 mg IM</p>
      <p style="margin:0;">24 hours apart</p>
    </div>
    <div style="background:{TEAL}; color:{WHITE}; border-radius:6px; padding:10px; text-align:center;">
      <p style="font-weight:700; margin:0 0 4px 0;">Dexamethasone</p>
      <p style="margin:0;">4 doses of 6 mg IM</p>
      <p style="margin:0;">12 hours apart</p>
    </div>
  </div>
</div>
</div>'''
s += page_badge(14)
s += foot()
write_slide(14, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 15 - TOCOLYTIC THERAPY
# ═══════════════════════════════════════════════════════════════
s = head("Tocolytics")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Tocolytic Therapy</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<p style="font-size:16px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Drugs Used for Tocolysis</p>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:13px;">
  <div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {TEAL};">
    <p style="font-weight:700; color:{TEAL}; margin:0 0 4px 0;">Prostaglandin Synthetase Inhibitor</p>
    <p style="margin:0; color:{DARK};">Indomethacin</p>
    <p style="margin:4px 0 0 0; color:{DARK};">50–100 mg twice daily oral/rectal, then 25–50 mg orally q6h for 48h. Not used after 30 wks.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {ORANGE};">
    <p style="font-weight:700; color:{ORANGE}; margin:0 0 4px 0;">Calcium Channel Blocker</p>
    <p style="margin:0; color:{DARK};">Nifedipine</p>
    <p style="margin:4px 0 0 0; color:{DARK};">20 mg orally, then 20 mg after 30 min. Maintenance: 20 mg q4-8h (max 160 mg/day). Low side effects (hypotension, dizziness, flushing).</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {RED};">
    <p style="font-weight:700; color:{RED}; margin:0 0 4px 0;">Oxytocin Antagonist</p>
    <p style="margin:0; color:{DARK};">Atosiban</p>
    <p style="margin:4px 0 0 0; color:{DARK};">6.75 mg bolus, then 300 μg/min IV × 3h, then 100 μg/min. Very expensive.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {DARK};">
    <p style="font-weight:700; color:{DARK}; margin:0 0 4px 0;">Magnesium Sulfate</p>
    <p style="margin:0; color:{DARK};">4–6 gm loading dose, then 1–2 gm for 24–48 hours.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {TEAL};">
    <p style="font-weight:700; color:{TEAL}; margin:0 0 4px 0;">Beta Agonist</p>
    <p style="margin:0; color:{DARK};">Ritodrine, Terbutaline</p>
    <p style="margin:4px 0 0 0; color:{RED};">Have dangerous complications (heart failure).</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {ORANGE};">
    <p style="font-weight:700; color:{ORANGE}; margin:0 0 4px 0;">Nitric Oxide Donor</p>
    <p style="margin:0; color:{DARK};">Glyceryl trinitrate</p>
  </div>
</div>
</div>

<div style="position:absolute; top:380px; left:40px; width:880px; z-index:10;">
<div style="background:#fde8e4; border-radius:8px; padding:12px; border-left:4px solid {RED};">
  <p style="font-size:16px; font-weight:700; color:{RED}; margin:0 0 4px 0;">Contraindications of Tocolytics</p>
  <p style="font-size:13px; color:{DARK}; margin:0;">Chorioamnionitis • Advanced labor • Pregnancy &gt;34 weeks • Pre-eclampsia and eclampsia • Abruptio placenta • Fetal demise and distress • Congenital anomaly not compatible with life</p>
</div>
</div>

<div style="position:absolute; right:25px; bottom:55px; width:150px; height:85px; border-radius:8px; overflow:hidden; border:1px solid #ddd;">
  <img src="imgs/tocolytics.png" alt="Tocolytic drugs" style="width:100%; height:100%; object-fit:cover;">
</div>'''
s += page_badge(15)
s += foot()
write_slide(15, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 16 - ANTIBIOTIC THERAPY & MODE OF DELIVERY
# ═══════════════════════════════════════════════════════════════
s = head("PTL Antibiotics")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Antibiotic Therapy &amp; Mode of Delivery</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
  <p style="font-size:17px; font-weight:700; color:{TEAL}; margin:0 0 8px 0;">Antibiotic Therapy for Prevention of Group B Streptococci Infection</p>
  <p style="font-size:14px; color:{DARK}; margin:0 0 6px 0;">Benzyl penicillin or ampicillin should be given for an established PTL as a prophylaxis against early onset of neonatal sepsis due to group B streptococcus.</p>
  <p style="font-size:14px; color:{DARK}; margin:0;">In cases of penicillin allergy, clindamycin can be used.</p>
</div>
</div>

<div style="position:absolute; top:205px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {ORANGE};">
  <p style="font-size:17px; font-weight:700; color:{ORANGE}; margin:0 0 8px 0;">Mode of Delivery</p>
  <ul style="margin:0; padding-left:20px; font-size:15px; color:{DARK};">
    <li><b>Cephalic presentation:</b> Vaginal delivery is preferred, even if delivery at &lt;34 weeks.</li>
    <li><b>Breech presentation:</b> Vaginal delivery is allowed if &gt;34 weeks; if &lt;34 weeks, cesarean section is performed.</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:320px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {YELLOW};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Student Activity</p>
  <p style="font-size:14px; color:{DARK}; margin:0;">The students are requested to attend with the tutor of bedside part of the clinical round a morning ward on admitted departmental cases with the diagnosis of preterm labor in order to revise the presentation and management done for these cases.</p>
</div>
</div>'''
s += page_badge(16)
s += foot()
write_slide(16, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 17 - SECTION 3 DIVIDER: PROM
# ═══════════════════════════════════════════════════════════════
s = head("Section 3")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{DARK};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{DARK}"/>
  <circle cx="800" cy="100" r="250" fill="{TEAL}" opacity="0.08"/>
  <circle cx="200" cy="400" r="180" fill="{ORANGE}" opacity="0.06"/>
  <rect x="60" y="120" width="80" height="5" fill="{YELLOW}"/>
</svg>
</div>
<p style="position:absolute; top:80px; left:60px; font-size:80px; font-weight:700; color:{TEAL}; margin:0; z-index:10;">03</p>
<p style="position:absolute; top:150px; left:60px; font-size:42px; font-weight:700; color:{WHITE}; margin:0; z-index:10;">Premature Rupture<br>of Membranes</p>
<p style="position:absolute; top:225px; left:60px; font-size:18px; color:{YELLOW}; margin:0; z-index:10; opacity:0.8;">Definition • Etiology • Diagnosis • Management • Chorioamnionitis</p>'''
s += page_badge(17)
s += foot()
write_slide(17, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 18 - PROM: DEFINITION & ETIOLOGY
# ═══════════════════════════════════════════════════════════════
s = head("PROM Definition")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">PROM — Definition &amp; Etiology</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {RED};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Definition</p>
  <p style="font-size:15px; color:{DARK}; margin:0;">A spontaneous rupture of membranes before the onset of labor. It could be <b>term</b> (after 37 completed weeks of gestation) or <b>preterm</b> (before 37 completed weeks).</p>
</div>
</div>

<div style="position:absolute; top:185px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {ORANGE};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Etiology</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Intrauterine infection</li>
    <li>Prior history of PPROM</li>
    <li>Trauma</li>
    <li>Amniocentesis</li>
    <li>Polyhydramnios</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:295px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Presentation</p>
  <p style="font-size:15px; color:{DARK}; margin:0;">Patients present with a typical history of sudden gush of clear or pale yellow fluid leaking from vagina.</p>
</div>
</div>'''
s += page_badge(18)
s += foot()
write_slide(18, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 19 - PROM: DIAGNOSIS
# ═══════════════════════════════════════════════════════════════
s = head("PROM Diagnosis")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Diagnosis of PROM</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {TEAL};">
    <p style="font-size:17px; font-weight:700; color:{TEAL}; margin:0 0 6px 0;">Speculum Examination</p>
    <p style="font-size:14px; color:{DARK}; margin:0;">It is the first step in the diagnosis of PROM to demonstrate leaking of fluid.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {ORANGE};">
    <p style="font-size:17px; font-weight:700; color:{ORANGE}; margin:0 0 6px 0;">Nitrazine Test</p>
    <p style="font-size:13px; color:{DARK}; margin:0 0 4px 0;">pH of amniotic fluid = 7 to 7.5</p>
    <p style="font-size:13px; color:{DARK}; margin:0 0 4px 0;">pH of vaginal discharge = 3.5 to 4.5</p>
    <p style="font-size:13px; color:{DARK}; margin:0;">Yellow nitrazine paper → turns <b style="color:{TEAL};">blue</b> = alkaline amniotic fluid (PROM confirmed). Remains yellow = no amniotic fluid.</p>
  </div>
</div>
</div>

<div style="position:absolute; top:220px; left:40px; width:880px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {YELLOW};">
    <p style="font-size:17px; font-weight:700; color:{YELLOW}; margin:0 0 6px 0;">Fern Test</p>
    <p style="font-size:14px; color:{DARK}; margin:0 0 4px 0;">Fluid from the posterior vaginal fornix is swabbed on a glass slide and allowed to dry for 10 minutes.</p>
    <p style="font-size:14px; color:{DARK}; margin:0;">If on drying, fern pattern appears → amniotic fluid is present (PROM).</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:14px; border-top:3px solid {DARK};">
    <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Ultrasonography</p>
    <p style="font-size:14px; color:{DARK}; margin:0 0 6px 0;">Oligohydramnios or anhydramnios.</p>
    <p style="font-size:14px; font-weight:700; color:{DARK}; margin:0 0 4px 0;">Fetal Fibronectin Protein</p>
    <p style="font-size:14px; color:{DARK}; margin:0;">A glycoprotein present in large amounts in amniotic fluid. Can be detected in 39% of females with PROM by ELISA test.</p>
  </div>
</div>
</div>

<div style="position:absolute; right:25px; bottom:55px; width:160px; height:90px; border-radius:8px; overflow:hidden; border:1px solid #ddd;">
  <img src="imgs/prom-diagnosis.png" alt="PROM diagnosis methods" style="width:100%; height:100%; object-fit:cover;">
</div>'''
s += page_badge(19)
s += foot()
write_slide(19, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 20 - EFFECTS & MANAGEMENT OF PROM
# ═══════════════════════════════════════════════════════════════
s = head("PROM Effects")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Effects &amp; Management of Preterm PROM</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {RED};">
  <p style="font-size:17px; font-weight:700; color:{RED}; margin:0 0 6px 0;">Effects of Preterm PROM</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Preterm labor</li>
    <li>Pulmonary hypoplasia due to severe oligohydramnios</li>
    <li>Skeletal and joint deformities of the fetus due to compression</li>
    <li>Chorioamnionitis</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:200px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {TEAL};">
  <p style="font-size:17px; font-weight:700; color:{TEAL}; margin:0 0 8px 0;">General Management</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Bed rest</li>
    <li>Sterile pads for inspection for meconium staining and signs of infection</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:295px; left:40px; width:880px; z-index:10;">
<p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 8px 0;">Management by Gestational Age</p>
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-top:3px solid {RED}; text-align:center;">
    <p style="font-size:15px; font-weight:700; color:{RED}; margin:0 0 6px 0;">Before 26 weeks</p>
    <p style="font-size:13px; color:{DARK}; margin:0;">Risk of chorioamnionitis is very high → <b>termination of pregnancy</b> is better.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-top:3px solid {TEAL}; text-align:center;">
    <p style="font-size:15px; font-weight:700; color:{TEAL}; margin:0 0 6px 0;">26–34 weeks</p>
    <p style="font-size:13px; color:{DARK}; margin:0;">Conservative treatment: hospitalization, maternal &amp; fetal observation, antibiotics, corticosteroids &amp; tocolysis for 48h.</p>
  </div>
  <div style="background:#f8fafa; border-radius:8px; padding:12px; border-top:3px solid {ORANGE}; text-align:center;">
    <p style="font-size:15px; font-weight:700; color:{ORANGE}; margin:0 0 6px 0;">After 34 weeks</p>
    <p style="font-size:13px; color:{DARK}; margin:0;"><b>Delivery.</b></p>
  </div>
</div>
</div>

<div style="position:absolute; top:430px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:10px; border-left:4px solid {TEAL};">
  <p style="font-size:14px; font-weight:700; color:{TEAL}; margin:0 0 4px 0;">Antibiotic Regimen (26–34 weeks)</p>
  <p style="font-size:12px; color:{DARK}; margin:0;">IV ampicillin 2 g + erythromycin 250 mg/6h × 48h, then oral amoxicillin 250 mg/8h + erythromycin 250 mg/6h × 5 days.</p>
</div>
</div>'''
s += page_badge(20)
s += foot()
write_slide(20, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 21 - CHORIOAMNIONITIS
# ═══════════════════════════════════════════════════════════════
s = head("Chorioamnionitis")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{WHITE};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{TEAL}"/>
</svg>
</div>
<p style="position:absolute; top:28px; left:40px; font-size:34px; font-weight:700; color:{DARK}; margin:0; z-index:10;">Chorioamnionitis</p>
<div style="position:absolute; top:68px; left:40px; width:80px; height:3px; background:{TEAL}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:95px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {RED};">
  <p style="font-size:17px; font-weight:700; color:{RED}; margin:0 0 6px 0;">Definition</p>
  <p style="font-size:15px; color:{DARK}; margin:0 0 12px 0;">Inflammation of fetal membranes which means intrauterine infection.</p>

  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Etiology</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li>Prolonged PROM</li>
    <li>Prolonged labor</li>
    <li>Prenatal diagnostic procedures (amniocentesis, CVS)</li>
    <li>Bacterial vaginosis</li>
  </ul>
</div>
</div>

<div style="position:absolute; top:285px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {ORANGE};">
  <p style="font-size:17px; font-weight:700; color:{ORANGE}; margin:0 0 6px 0;">Diagnosis</p>
  <p style="font-size:14px; color:{DARK}; margin:0 0 6px 0;">Fever &gt;38°C with any of the following:</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:13px;">
    <div>
      <ul style="margin:0; padding-left:18px; color:{DARK};">
        <li>Maternal tachycardia</li>
        <li>Fetal tachycardia</li>
        <li>Uterine tenderness</li>
        <li>Foul smelling amniotic fluid</li>
      </ul>
    </div>
    <div>
      <ul style="margin:0; padding-left:18px; color:{DARK};">
        <li>Maternal leukocytosis &gt;16,000/cc</li>
        <li>Raised C-reactive protein &gt;2.5</li>
        <li>High vaginal swab culture and stain positive</li>
      </ul>
    </div>
  </div>
</div>
</div>

<div style="position:absolute; top:425px; left:40px; width:880px; z-index:10;">
<div style="background:#f8fafa; border-radius:8px; padding:14px; border-left:4px solid {YELLOW};">
  <p style="font-size:17px; font-weight:700; color:{DARK}; margin:0 0 6px 0;">Management</p>
  <ul style="margin:0; padding-left:20px; font-size:14px; color:{DARK};">
    <li><b>Definitive treatment:</b> Delivery and evacuation of the uterine contents.</li>
    <li><b>Antibiotics:</b> Ampicillin (2 g IV every 6 h) plus gentamicin sulfate (2 mg/kg IV loading, then 1.5 mg/kg IV every 8 h) until delivery.</li>
    <li>If cesarean delivery is performed, clindamycin or metronidazole is added for anaerobic coverage.</li>
  </ul>
</div>
</div>'''
s += page_badge(21)
s += foot()
write_slide(21, s)

# ═══════════════════════════════════════════════════════════════
# SLIDE 22 - SUMMARY / CLOSING
# ═══════════════════════════════════════════════════════════════
s = head("Summary")
s += f'''<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{DARK};"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
<svg width="960" height="540" aria-hidden="true">
  <rect x="0" y="0" width="960" height="540" fill="{DARK}"/>
  <circle cx="100" cy="480" r="200" fill="{TEAL}" opacity="0.06"/>
  <circle cx="850" cy="80" r="180" fill="{YELLOW}" opacity="0.05"/>
  <rect x="60" y="80" width="80" height="5" fill="{YELLOW}"/>
</svg>
</div>
<p style="position:absolute; top:60px; left:60px; font-size:44px; font-weight:700; color:{WHITE}; margin:0; z-index:10;">Key Takeaways</p>

<div style="position:absolute; top:130px; left:60px; width:840px; z-index:10;">
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;">
  <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:16px; border-top:3px solid {TEAL};">
    <p style="font-size:18px; font-weight:700; color:{TEAL}; margin:0 0 8px 0;">Multiple Pregnancy</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:rgba(255,255,255,0.9);">
      <li>Monozygotic vs Dizygotic</li>
      <li>Chorionicity &amp; Amnionicity</li>
      <li>Timing of delivery by type</li>
      <li>TTTS in 10-15% monochorionic</li>
    </ul>
  </div>
  <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:16px; border-top:3px solid {YELLOW};">
    <p style="font-size:18px; font-weight:700; color:{YELLOW}; margin:0 0 8px 0;">Preterm Labor</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:rgba(255,255,255,0.9);">
      <li>20-37 weeks gestation</li>
      <li>Idiopathic most common</li>
      <li>Corticosteroids for fetal lung maturity</li>
      <li>Tocolytics with contraindications</li>
    </ul>
  </div>
  <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:16px; border-top:3px solid {RED};">
    <p style="font-size:18px; font-weight:700; color:{RED}; margin:0 0 8px 0;">PROM</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:rgba(255,255,255,0.9);">
      <li>Rupture before labor onset</li>
      <li>Nitrazine &amp; Fern tests</li>
      <li>Conservative vs delivery by GA</li>
      <li>Chorioamnionitis management</li>
    </ul>
  </div>
</div>
</div>

<div style="position:absolute; bottom:70px; left:60px; z-index:10;">
  <p style="font-size:18px; color:{WHITE}; margin:0; opacity:0.8;">Obstetrics &amp; Gynecology — Complete Lecture Notes</p>
  <p style="font-size:14px; color:{YELLOW}; margin:6px 0 0 0; opacity:0.6;">Full content preserved. All definitions, classifications, management protocols included.</p>
</div>'''
s += page_badge(22)
s += foot()
write_slide(22, s)

print(f"\nTotal slides: 22")
print("All slides generated successfully in:", SLIDES_DIR)
