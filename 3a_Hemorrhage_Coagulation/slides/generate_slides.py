#!/usr/bin/env python3
"""Batch generate medical presentation slides from APH and DIC PDF content."""
import os

# === PALETTE: #1 现代与健康 ===
C1 = "#006d77"  # dark teal - headings, accents
C2 = "#83c5be"  # light teal - secondary accents
C3 = "#edf6f9"  # light blue-gray - backgrounds
C4 = "#ffddd2"  # light peach - highlights
C5 = "#e29578"  # coral - emphasis

FONT = '"Times New Roman", serif'

def badge(page_num):
    """SVG page number badge - bottom right."""
    return f'''<div style="position:absolute; right:32px; bottom:24px; width:40px; height:40px; z-index:100;">
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="20" cy="20" r="18" fill="{C1}" stroke="{C2}" stroke-width="2"/>
  <text x="20" y="26" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="700" fill="#ffffff">{page_num}</text>
</svg>
</div>'''

def head_script():
    return '''<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body { margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }
.slide-content { width:960px; height:540px; position:relative; transform-origin:center center; }
</style>
<script>
function scaleSlide(){const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform=`scale(${sc})`;s.style.transformOrigin='center center';s.style.flexShrink='0';}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>'''

def wrap(title, body_html, page_num=None, bg_color=C3):
    """Wrap content into full HTML slide."""
    badge_html = badge(page_num) if page_num else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{head_script()}
</head>
<body>
<div class="slide-content" style="background:{bg_color}; overflow:hidden; font-family:{FONT};">
{body_html}
{badge_html}
</div>
</body>
</html>'''

# ============================================================
# SLIDE 1 – COVER
# ============================================================
slide1_body = f'''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, {C1} 0%, {C1} 45%, {C2} 100%);"></div>
<svg style="position:absolute; top:0; left:0; width:960px; height:540px;" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="800" cy="-50" r="300" fill="rgba(255,255,255,0.06)"/>
  <circle cx="900" cy="400" r="250" fill="rgba(255,255,255,0.04)"/>
  <circle cx="100" cy="500" r="200" fill="rgba(255,255,255,0.05)"/>
</svg>
<div style="position:absolute; top:120px; left:70px; width:80px; height:5px; background:{C4}; border-radius:2.5px; z-index:10;"></div>
<p style="position:absolute; top:120px; left:180px; font-size:28px; font-weight:400; color:{C4}; opacity:0.9; z-index:10; margin:0;">3a — Hemorrhage &amp; Coagulation</p>
<p style="position:absolute; top:185px; left:70px; font-size:48px; font-weight:700; color:#ffffff; z-index:10; margin:0; line-height:1.2;">Antepartum Hemorrhage</p>
<p style="position:absolute; top:248px; left:70px; font-size:36px; font-weight:700; color:{C4}; z-index:10; margin:0; line-height:1.2;">&amp; Disseminated Intravascular<br>Coagulopathy</p>
<p style="position:absolute; top:340px; left:70px; font-size:18px; font-weight:400; color:rgba(255,255,255,0.8); z-index:10; margin:0;">Obstetric Disorders — Complete Lecture Notes</p>
<div style="position:absolute; bottom:50px; left:70px; display:flex; gap:16px; align-items:center; z-index:10;">
  <svg width="30" height="2" viewBox="0 0 30 2" xmlns="http://www.w3.org/2000/svg"><rect width="30" height="2" fill="{C4}" opacity="0.6"/></svg>
  <span style="font-size:14px; color:rgba(255,255,255,0.7);">Medical Obstetrics</span>
</div>
'''
with open('slides/slide-01.html','w') as f: f.write(wrap('Cover', slide1_body, page_num=None, bg_color=C1))

# ============================================================
# SLIDE 2 – TABLE OF CONTENTS
# ============================================================
toc_items = [
    ("1", "Antepartum Hemorrhage — Definition &amp; Classification"),
    ("2", "Plenta Previa — Overview &amp; Degrees"),
    ("3", "Placenta Previa — Clinical Picture"),
    ("4", "Placenta Previa — Investigations &amp; Management"),
    ("5", "Placenta Previa — Delivery"),
    ("6", "Abruptio Placenta — Classification &amp; Etiology"),
    ("7", "Abruptio Placenta — Clinical Picture &amp; Investigations"),
    ("8", "Abruptio Placenta — Complications &amp; Management"),
    ("9", "Rupture Uterus — Etiology &amp; Risk Factors"),
    ("10", "Rupture Uterus — Clinical Picture &amp; Management"),
    ("11", "Vasa Previa &amp; Diagnostic Tests"),
    ("12", "Disseminated Intravascular Coagulopathy (DIC)"),
]

toc_html = f'''
<p style="position:absolute; top:24px; left:60px; font-size:28px; font-weight:700; color:{C1}; z-index:10; margin:0;">Table of Contents</p>
<div style="position:absolute; top:64px; left:60px; width:80px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>
<div style="position:absolute; top:80px; left:60px; right:60px; bottom:70px; display:grid; grid-template-columns:1fr 1fr; gap:12px 32px; align-content:start; z-index:10;">
'''
for i, (num, title) in enumerate(toc_items):
    col = i % 2
    row = i // 2
    top_px = 80 + row * 68
    toc_html += f'''
  <div style="display:flex; align-items:flex-start; gap:12px;">
    <div style="min-width:32px; height:32px; background:{C1}; border-radius:50%; display:flex; align-items:center; justify-content:center;">
      <span style="color:#ffffff; font-size:14px; font-weight:700;">{num}</span>
    </div>
    <div>
      <p style="margin:0; font-size:14px; color:{C1}; font-weight:600; line-height:1.3;">{title}</p>
    </div>
  </div>'''
toc_html += '</div>'
with open('slides/slide-02.html','w') as f: f.write(wrap('TOC', toc_html, page_num=2))

# ============================================================
# SLIDE 3 – SECTION DIVIDER: Antepartum Hemorrhage
# ============================================================
slide3_body = f'''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{C1};"></div>
<svg style="position:absolute; top:0; left:0; width:960px; height:540px;" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="0" y="0" width="8" height="540" fill="{C4}"/>
  <circle cx="850" cy="80" r="180" fill="rgba(255,255,255,0.05)"/>
  <circle cx="-50" cy="450" r="200" fill="rgba(255,255,255,0.04)"/>
</svg>
<p style="position:absolute; top:80px; left:60px; font-size:72px; font-weight:700; color:{C4}; opacity:0.5; z-index:10; margin:0; line-height:1;">01</p>
<p style="position:absolute; top:170px; left:60px; font-size:42px; font-weight:700; color:#ffffff; z-index:10; margin:0; line-height:1.2;">Antepartum<br>Hemorrhage</p>
<div style="position:absolute; top:270px; left:60px; width:80px; height:4px; background:{C4}; border-radius:2px; z-index:10;"></div>
<p style="position:absolute; top:300px; left:60px; font-size:16px; color:rgba(255,255,255,0.8); z-index:10; margin:0; max-width:500px;">Definition &bull; Classification &bull; Placenta Previa &bull; Abruptio Placenta &bull; Rupture Uterus &bull; Vasa Previa</p>
'''
with open('slides/slide-03.html','w') as f: f.write(wrap('Section Divider', slide3_body, page_num=3, bg_color=C1))

# ============================================================
# SLIDE 4 – APH Definition & Classification
# ============================================================
slide4_body = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Antepartum Hemorrhage — Definition</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:88px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:16px 20px; border-left:4px solid {C1}; z-index:10;">
  <p style="margin:0; font-size:15px; color:#333; line-height:1.5;"><strong style="color:{C1};">Definition:</strong> Bleeding from the vagina occurring at any time after <strong>20th week</strong> of pregnancy and before the child birth.</p>
</div>

<p style="position:absolute; top:200px; left:50px; font-size:22px; font-weight:700; color:{C1}; z-index:10; margin:0;">Etiological Classification</p>

<div style="position:absolute; top:235px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C1};">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">1. Placenta Previa</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Hemorrhage due to partial separation of <strong>abnormally situated</strong> placenta in the lower uterine segment.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C1};">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">2. Abruptio Placenta</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Hemorrhage due to partial separation of <strong>normally situated</strong> placenta (in the upper uterine segment).</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C5};">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C5};">3. Vasa Previa</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;"><strong>Fetal hemorrhage</strong> due to laceration of abnormally situated umbilical (fetal) vessels.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C5};">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C5};">4. Extraplacental Bleeding</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Rupture uterus, hemorrhage due to lesions of cervix or vagina (erosion, polyp, carcinoma). Called <strong>incidental hemorrhage</strong>.</p>
  </div>
</div>

<p style="position:absolute; bottom:24px; left:50px; font-size:12px; color:#888; z-index:10; margin:0; font-style:italic;">ILOs: Understand classification; differentiate clinically; describe management; realize complications.</p>
'''
with open('slides/slide-04.html','w') as f: f.write(wrap('APH Definition', slide4_body, page_num=4))

# ============================================================
# SLIDE 5 – Placenta Previa: Definition, Incidence, Degrees (1-2)
# ============================================================
slide5_body = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Placenta Previa</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:88px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Definition</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Antepartum hemorrhage due to premature separation of <strong>abnormally situated placenta</strong> (in the lower uterine segment).</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Incidence</p>
    <p style="margin:0; font-size:28px; font-weight:700; color:{C5}; line-height:1.2;">1/200</p>
    <p style="margin:0; font-size:13px; color:#666;">of pregnancies</p>
  </div>
</div>

<p style="position:absolute; top:210px; left:50px; font-size:22px; font-weight:700; color:{C1}; z-index:10; margin:0;">Degrees of Placenta Previa</p>

<div style="position:absolute; top:248px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:12px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C2};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Type I — Placenta Previa Lateralis</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">The placenta is only partially attached to the lower uterine segment, which may be anterior or posterior.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C2};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Type II — Placenta Previa Marginalis</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">A great part of the placenta is attached to the lower uterine segment so that its lower margin reaches down to the internal os.</p>
  </div>
</div>

<p style="position:absolute; bottom:24px; left:50px; font-size:12px; color:#888; z-index:10; margin:0;">YouTube: https://youtu.be/rCn6a28cf2E</p>
'''
with open('slides/slide-05.html','w') as f: f.write(wrap('Placenta Previa 1', slide5_body, page_num=5))

# ============================================================
# SLIDE 6 – Placenta Previa: Degrees (3-4)
# ============================================================
slide6_body = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Degrees of Placenta Previa (cont.)</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:16px; z-index:10;">
  <div style="background:#ffffff; border-radius:10px; padding:20px; border-top:4px solid {C5};">
    <p style="margin:0 0 8px 0; font-size:18px; font-weight:700; color:{C1};">Type III — Incomplete Centralis</p>
    <p style="margin:0; font-size:14px; color:#444; line-height:1.5;">The placenta covers the internal os when it is closed or partially dilated <strong>but not</strong> when it is fully dilated.</p>
  </div>
  <div style="background:#ffffff; border-radius:10px; padding:20px; border-top:4px solid {C1};">
    <p style="margin:0 0 8px 0; font-size:18px; font-weight:700; color:{C5};">Type IV — Complete Centralis</p>
    <p style="margin:0; font-size:14px; color:#444; line-height:1.5;">The placenta covers the internal os <strong>completely</strong> whether the cervix is partially or fully dilated.</p>
  </div>
</div>

<div style="position:absolute; top:280px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:16px 20px; border-left:4px solid {C2}; z-index:10;">
  <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C1};">Key Points</p>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.7;">
    <li>Mean gestational age at diagnosis is <strong>32 weeks</strong></li>
    <li>Associated with increased risk of congenital abnormalities and <strong>IUGR</strong></li>
  </ul>
</div>
'''
with open('slides/slide-06.html','w') as f: f.write(wrap('Placenta Previa 2', slide6_body, page_num=6))

# ============================================================
# SLIDE 7 – Placenta Previa: Clinical Picture
# ============================================================
slide7_body = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Placenta Previa — Clinical Picture</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};"><svg width="16" height="16" viewBox="0 0 16 16" style="vertical-align:middle; margin-right:4px;" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="7" fill="{C5}"/></svg> Symptoms</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.7;">
      <li><strong>Painless</strong> causeless recurrent vaginal bleeding in third trimester</li>
      <li>Mean gestational age at diagnosis: <strong>32 weeks</strong></li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};"><svg width="16" height="16" viewBox="0 0 16 16" style="vertical-align:middle; margin-right:4px;" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="7" fill="{C5}"/></svg> Abdominal Examination</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.7;">
      <li>Abdomen is <strong>lax</strong>, no tenderness or rigidity</li>
      <li>Fundal level equals period of amenorrhea</li>
      <li>Fetal parts are <strong>easily felt</strong></li>
      <li>FHS usually normal</li>
      <li><strong>Malpresentation &amp; non-engagement</strong>: common</li>
    </ul>
  </div>
</div>

<div style="position:absolute; top:320px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:rgba(0,109,119,0.08); border-radius:8px; padding:12px 16px;">
    <p style="margin:0; font-size:13px; color:{C1}; line-height:1.5;"><strong>Ultrasound picture</strong> of placenta previa — The placenta is seen covering or partially covering the internal os on transvaginal ultrasound.</p>
  </div>
  <div style="background:rgba(0,109,119,0.08); border-radius:8px; padding:12px 16px;">
    <p style="margin:0; font-size:13px; color:{C1}; line-height:1.5;"><strong>MRI picture</strong> of placenta previa — Magnetic resonance imaging is used when ultrasound is inconclusive, especially for posterior placenta.</p>
  </div>
</div>
'''
with open('slides/slide-07.html','w') as f: f.write(wrap('PP Clinical', slide7_body, page_num=7))

# ============================================================
# SLIDE 8 – Placenta Previa: Investigations & Management
# ============================================================
slide8_body = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Placenta Previa — Investigations &amp; Management</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Investigations</p>
  <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.8;">
    <li><strong>Ultrasound</strong> is the diagnostic technique of choice — especially transvaginal ultrasound</li>
    <li><strong>Magnetic Resonance Imaging (MRI)</strong></li>
  </ul>
</div>

<div style="position:absolute; top:90px; right:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">General Management</p>
  <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.8;">
    <li>High intensity care area</li>
    <li>Intravenous access</li>
    <li>Blood typing and saving</li>
    <li>Serial hematocrit</li>
    <li>Vital signs observation</li>
    <li>Ultrasound scanning</li>
  </ul>
</div>

<p style="position:absolute; top:290px; left:50px; font-size:20px; font-weight:700; color:{C1}; z-index:10; margin:0;">Expectant Management (Remote from Term)</p>
<div style="position:absolute; top:320px; left:50px; right:50px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0; font-size:13px; color:#444; line-height:1.8;">Provided that maternal and fetal hemodynamics are stable:</p>
  <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.7;">
    <li>Magnesium sulfate as tocolytic for preterm contractions</li>
    <li>Replace blood loss to keep hematocrit &gt; 30%</li>
    <li><strong>Steroids</strong> to enhance fetal lung maturity (24–34 weeks)</li>
    <li>Serial ultrasound examinations every <strong>2 weeks</strong></li>
    <li>Bed rest in hospital</li>
  </ul>
</div>
'''
with open('slides/slide-08.html','w') as f: f.write(wrap('PP Investigations', slide8_body, page_num=8))

# ============================================================
# SLIDE 9 – Placenta Previa: Home Care & Delivery
# ============================================================
slide9_body = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Placenta Previa — Home Care &amp; Delivery</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; background:#ffffff; border-radius:8px; padding:16px 20px; border-left:4px solid {C5}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C5};">Home Care — Only Under Ideal Circumstances</p>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
    <li>Highly motivated patient</li>
    <li>Full understanding of risks</li>
    <li>Ability to maintain bed rest</li>
    <li>Location near hospital</li>
    <li>24-hour transportation available</li>
  </ul>
</div>

<div style="position:absolute; top:260px; left:50px; right:50px; background:#ffffff; border-radius:8px; padding:16px 20px; border-left:4px solid {C1}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C1};">Delivery</p>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
    <li><strong>Vaginal delivery</strong> is allowed when the placental edge is <strong>&gt; 2 cm</strong> from the internal os</li>
    <li>If &lt; 2 cm, delivery is by <strong>Cesarean section</strong></li>
    <li>In incomplete and complete centralis (Types III &amp; IV): well-planned <strong>elective Cesarean section</strong> at <strong>36–37 weeks</strong></li>
  </ul>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:{C2}; border-radius:6px; padding:10px 14px;">
    <p style="margin:0; font-size:12px; color:#ffffff; line-height:1.4;"><strong>Edge &gt; 2 cm from os</strong> → Vaginal delivery allowed</p>
  </div>
  <div style="background:{C5}; border-radius:6px; padding:10px 14px;">
    <p style="margin:0; font-size:12px; color:#ffffff; line-height:1.4;"><strong>Edge &lt; 2 cm or centralis</strong> → Cesarean section</p>
  </div>
</div>
'''
with open('slides/slide-09.html','w') as f: f.write(wrap('PP Home & Delivery', slide9_body, page_num=9))

print('Slides 1-9 generated successfully.')
