#!/usr/bin/env python3
"""Batch 2: Abruptio Placenta, Rupture Uterus, Vasa Previa slides 10-20."""
import os

C1 = "#006d77"
C2 = "#83c5be"
C3 = "#edf6f9"
C4 = "#ffddd2"
C5 = "#e29578"
FONT = '"Times New Roman", serif'

def badge(page_num):
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
# SLIDE 10 – Abruptio Placenta: Definition, Incidence, Classification
# ============================================================
s10 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Abruptio Placenta</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Definition</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">APH due to premature separation of a <strong>normally situated placenta</strong> (upper uterine segment).</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Incidence</p>
    <p style="margin:0; font-size:28px; font-weight:700; color:{C5}; line-height:1.2;">1/100</p>
    <p style="margin:0; font-size:13px; color:#666;">of pregnancies</p>
  </div>
</div>

<p style="position:absolute; top:220px; left:50px; font-size:22px; font-weight:700; color:{C1}; z-index:10; margin:0;">Classification</p>

<div style="position:absolute; top:258px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C1};">
    <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C1};">Concealed</p>
    <p style="margin:0; font-size:12px; color:#444; line-height:1.4;">Blood is retained behind the placenta, inside the uterus (retroplacental hematoma).</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C5};">
    <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C5};">Revealed (Visible)</p>
    <p style="margin:0; font-size:12px; color:#444; line-height:1.4;">Blood escapes and appears externally as vaginal bleeding.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-top:3px solid {C2};">
    <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C1};">Combined / Mixed</p>
    <p style="margin:0; font-size:12px; color:#444; line-height:1.4;">Part of blood is retained inside the uterus and part escapes as vaginal bleeding.</p>
  </div>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; background:rgba(0,109,119,0.08); border-radius:6px; padding:10px 14px; z-index:10;">
  <p style="margin:0; font-size:12px; color:{C1}; line-height:1.4;"><strong>Ultrasound picture:</strong> Abruptio placenta may show a retroplacental hematoma — a collection of blood between the placenta and uterine wall.</p>
</div>
'''
with open('slides/slide-10.html','w') as f: f.write(wrap('Abruptio Def', s10, page_num=10))

# ============================================================
# SLIDE 11 – Abruptio Placenta: Etiology
# ============================================================
s11 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Abruptio Placenta — Etiology</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">1. Hypertensive Disorders</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Especially <strong>pre-eclampsia</strong> — the most common associated condition.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C5};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C5};">2. Trauma</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Trauma to the pregnant woman (e.g., fall, MVA, direct blow).</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">3. Thrombophilia</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Thrombophilia with pregnancy increases risk of placental abruption.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C5};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C5};">4. Submucous Fibroid</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Submucous fibroid with pregnancy.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">5. Premature ROM</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Premature rupture of membrane on top of <strong>polyhydramnios</strong>.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid #ccc;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:#888;">6. Idiopathic</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">No identifiable cause found in many cases.</p>
  </div>
</div>
'''
with open('slides/slide-11.html','w') as f: f.write(wrap('Abruptio Etiology', s11, page_num=11))

# ============================================================
# SLIDE 12 – Abruptio Placenta: Clinical Picture
# ============================================================
s12 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Abruptio Placenta — Clinical Picture</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Symptoms</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.7;">
      <li>Vaginal bleeding (<strong>80%</strong> of patients)</li>
      <li>Blood remains concealed (<strong>20%</strong> of patients)</li>
      <li><strong>Abdominal pain</strong> from uterine contractions</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Signs</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.7;">
      <li>Uterine tenderness</li>
      <li>Board-like abdomen, tenderness &amp; rigidity</li>
      <li>Fundal level &gt; period of amenorrhea (blood accumulation)</li>
    </ul>
  </div>
</div>

<div style="position:absolute; top:280px; left:50px; right:50px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Additional Signs</p>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.7;">
    <li>Fetal parts are <strong>difficult to palpate</strong> due to rigidity</li>
    <li>Fetal heart rate shows <strong>distress or absent</strong> (IUFD)</li>
  </ul>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:{C1}; border-radius:6px; padding:10px 14px;">
    <p style="margin:0; font-size:12px; color:#ffffff; line-height:1.4;"><strong>80%</strong> Revealed bleeding</p>
  </div>
  <div style="background:{C5}; border-radius:6px; padding:10px 14px;">
    <p style="margin:0; font-size:12px; color:#ffffff; line-height:1.4;"><strong>20%</strong> Concealed bleeding</p>
  </div>
</div>
'''
with open('slides/slide-12.html','w') as f: f.write(wrap('Abruptio Clinical', s12, page_num=12))

# ============================================================
# SLIDE 13 – Abruptio Placenta: Investigations
# ============================================================
s13 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Abruptio Placenta — Investigations</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px;">
    <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C1};">Laboratory Investigations</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
      <li><strong>Blood grouping</strong> and cross-matching</li>
      <li><strong>CBC</strong> (Complete Blood Count)</li>
      <li><strong>Coagulation profile:</strong></li>
      <ul style="padding-left:18px; margin:2px 0;">
        <li>Prothrombin time (PT)</li>
        <li>Partial thromboplastin time (PTT)</li>
        <li>Bleeding time and coagulation time</li>
        <li>Fibrinogen level</li>
        <li>Fibrinogen degradation products</li>
      </ul>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px;">
    <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C1};">Imaging</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
      <li><strong>Ultrasonography:</strong> Can show retroplacental hematoma</li>
    </ul>
    <div style="background:rgba(0,109,119,0.08); border-radius:6px; padding:10px; margin-top:10px;">
      <p style="margin:0; font-size:12px; color:{C1}; line-height:1.4;"><strong>Ultrasound picture of abruptio placenta:</strong> A retroplacental hematoma appears as an anechoic or hypoechoic collection between the placenta and the myometrium.</p>
    </div>
  </div>
</div>
'''
with open('slides/slide-13.html','w') as f: f.write(wrap('Abruptio Investigations', s13, page_num=13))

# ============================================================
# SLIDE 14 – Abruptio Placenta: Complications
# ============================================================
s14 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Abruptio Placenta — Complications</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:20px; z-index:10;">
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C1};">
    <p style="margin:0 0 8px 0; font-size:18px; font-weight:700; color:{C1};">Maternal Complications</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
      <li>Hemorrhage, shock</li>
      <li>Rupture uterus</li>
      <li>Acute renal failure</li>
      <li>Postpartum hemorrhage</li>
      <li>Sheehan syndrome</li>
      <li>Amniotic fluid embolism</li>
      <li><strong>Consumptive coagulopathy (DIC)</strong></li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C5};">
    <p style="margin:0 0 8px 0; font-size:18px; font-weight:700; color:{C5};">Fetal Complications</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
      <li><strong>IUFD</strong> (Intrauterine Fetal Death)</li>
      <li><strong>Prematurity</strong></li>
    </ul>
    <div style="margin-top:14px; padding:10px; background:rgba(226,149,120,0.1); border-radius:6px;">
      <p style="margin:0; font-size:12px; color:{C5}; line-height:1.4;"><strong>Note:</strong> DIC is a serious consumptive coagulopathy that can result from abruptio placenta due to release of thromboplastin into maternal circulation.</p>
    </div>
  </div>
</div>
'''
with open('slides/slide-14.html','w') as f: f.write(wrap('Abruptio Complications', s14, page_num=14))

# ============================================================
# SLIDE 15 – Abruptio Placenta: Management
# ============================================================
s15 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Abruptio Placenta — Management</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C5};">
    <p style="margin:0 0 8px 0; font-size:17px; font-weight:700; color:{C5};">Termination of Pregnancy</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.5;">Indicated if:</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8; margin-top:4px;">
      <li>Fetal distress is present <strong>OR</strong></li>
      <li>Mother is unstable <strong>regardless of gestational age</strong></li>
    </ul>
    <p style="margin:8px 0 0 0; font-size:13px; color:#444; line-height:1.5;">While resuscitation is ongoing:</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
      <li>Artificial rupture of membranes + induction of labor</li>
      <li><strong>OR</strong> Cesarean section</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C1};">
    <p style="margin:0 0 8px 0; font-size:17px; font-weight:700; color:{C1};">Conservative Treatment</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.5;">Indicated if:</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8; margin-top:4px;">
      <li><strong>Both</strong> fetal and maternal hemodynamics are stable</li>
      <li>With <strong>preterm gestational age</strong></li>
    </ul>
    <p style="margin:8px 0 0 0; font-size:12px; color:#888; font-style:italic;">Close monitoring with serial ultrasounds, fetal heart rate monitoring, and maternal vital signs.</p>
  </div>
</div>
'''
with open('slides/slide-15.html','w') as f: f.write(wrap('Abruptio Management', s15, page_num=15))

# ============================================================
# SLIDE 16 – Rupture Uterus: Definition, Incidence, Etiology (During Pregnancy)
# ============================================================
s16 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Rupture Uterus</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Definition</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Disruption of the uterine wall during pregnancy or labor.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Incidence</p>
    <p style="margin:0; font-size:24px; font-weight:700; color:{C5}; line-height:1.2;">1–4 / 1000</p>
    <p style="margin:0; font-size:13px; color:#666;">95% in multipara</p>
  </div>
</div>

<p style="position:absolute; top:210px; left:50px; font-size:20px; font-weight:700; color:{C1}; z-index:10; margin:0;">Etiology — During Pregnancy</p>

<div style="position:absolute; top:242px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:12px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:12px 14px; border-left:4px solid {C1};">
    <p style="margin:0 0 4px 0; font-size:13px; font-weight:700; color:{C1};">Spontaneous Rupture</p>
    <ul style="margin:0; padding-left:14px; font-size:12px; color:#444; line-height:1.6;">
      <li>Rupture of uterine scar (weak scar)</li>
      <li>Abruptio placenta with severe concealed hemorrhage</li>
      <li>Invasive trophoblastic disease</li>
      <li>Rupture of angular pregnancy / rudimentary horn</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:12px 14px; border-left:4px solid {C5};">
    <p style="margin:0 0 4px 0; font-size:13px; font-weight:700; color:{C5};">Traumatic Rupture</p>
    <ul style="margin:0; padding-left:14px; font-size:12px; color:#444; line-height:1.6;">
      <li>Perforation during evacuation</li>
      <li>External trauma (ECV, stab wound, kick)</li>
    </ul>
  </div>
</div>

<p style="position:absolute; bottom:30px; left:50px; font-size:12px; color:#888; z-index:10; margin:0;">Weak scar causes: infection of wound, erosion by chorionic villi, USCS, uterine overdistension, repeated vaginal deliveries after CS</p>
'''
with open('slides/slide-16.html','w') as f: f.write(wrap('RU Etiology Pregnancy', s16, page_num=16))

# ============================================================
# SLIDE 17 – Rupture Uterus: Etiology During Labor
# ============================================================
s17 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Rupture Uterus — Etiology During Labor</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 18px; border-top:3px solid {C1};">
    <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C1};">Spontaneous Rupture</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
      <li><strong>Obstructed labor:</strong> contracted pelvis, neglected shoulder, hydrocephalus, malposition, macrosomia</li>
      <li>Rupture of uterine scar</li>
      <li><strong>Misuse of ecbolics</strong> (uterotonic drugs)</li>
      <li><strong>Multiparity:</strong></li>
      <ul style="padding-left:18px; margin:2px 0;">
        <li>Weak uterine wall from previous deliveries</li>
        <li>Increased incidence of malpresentation, macrosomia, prolonged labor, abnormal uterine action</li>
        <li>False sense of security due to previous spontaneous vaginal delivery</li>
      </ul>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 18px; border-top:3px solid {C5};">
    <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C5};">Traumatic Rupture</p>
    <p style="margin:0 0 4px 0; font-size:13px; color:#444; font-weight:600;">Intrauterine manipulation:</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
      <li>Internal version (after drainage of liquor)</li>
      <li>Manual separation of the placenta</li>
      <li>Breech extraction</li>
      <li>Destructive operations</li>
      <li>Manual dilatation of the cervix</li>
      <li>Forceps or Ventouse application</li>
    </ul>
  </div>
</div>
'''
with open('slides/slide-17.html','w') as f: f.write(wrap('RU Etiology Labor', s17, page_num=17))

# ============================================================
# SLIDE 18 – Rupture Uterus: Risk Factors, Types & Site
# ============================================================
s18 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Rupture Uterus — Risk Factors, Types &amp; Site</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Risk Factors</p>
  <ul style="margin:0; padding-left:16px; font-size:12px; color:#444; line-height:1.8;">
    <li>Excessive uterine stimulation</li>
    <li>History of previous C/S</li>
    <li>Trauma</li>
    <li>Prior rupture</li>
    <li>Previous uterine surgery</li>
    <li>Multiparity</li>
    <li>Non-vertex fetal presentation</li>
    <li>Shoulder dystocia</li>
    <li>Forceps delivery</li>
  </ul>
</div>

<div style="position:absolute; top:90px; right:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Types</p>
  <div style="border-left:3px solid {C1}; padding-left:12px; margin-bottom:10px;">
    <p style="margin:0; font-size:13px; font-weight:700; color:{C1};">Complete Rupture</p>
    <p style="margin:0; font-size:12px; color:#444; line-height:1.4;">Tearing of the uterine wall <strong>including</strong> the peritoneum.</p>
  </div>
  <div style="border-left:3px solid {C5}; padding-left:12px; margin-bottom:14px;">
    <p style="margin:0; font-size:13px; font-weight:700; color:{C5};">Incomplete Rupture</p>
    <p style="margin:0; font-size:12px; color:#444; line-height:1.4;">Tearing of the uterine wall <strong>without</strong> the peritoneum.</p>
  </div>
  <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Site of Rupture</p>
  <ul style="margin:0; padding-left:16px; font-size:12px; color:#444; line-height:1.7;">
    <li>Lower segment — in <strong>obstructed labor</strong></li>
    <li>At the site of <strong>scar</strong></li>
    <li>Extension of cervical tear into lower segment</li>
  </ul>
</div>
'''
with open('slides/slide-18.html','w') as f: f.write(wrap('RU Risk Types', s18, page_num=18))

# ============================================================
# SLIDE 19 – Rupture Uterus: Severity of Bleeding & Clinical Picture
# ============================================================
s19 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Rupture Uterus — Severity &amp; Clinical Picture</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Severity of Bleeding</p>
  <div style="border-left:3px solid {C5}; padding-left:12px; margin-bottom:8px;">
    <p style="margin:0; font-size:13px; font-weight:700; color:{C5};">Severe bleeding</p>
    <p style="margin:0; font-size:12px; color:#444;">If <strong>uterine artery</strong> is torn.</p>
  </div>
  <div style="border-left:3px solid {C1}; padding-left:12px;">
    <p style="margin:0; font-size:13px; font-weight:700; color:{C1};">Mild bleeding</p>
    <p style="margin:0; font-size:12px; color:#444; line-height:1.4;">If fetus and placenta escape into the peritoneal cavity. The empty uterus retracts so bleeding is mild.</p>
  </div>
</div>

<div style="position:absolute; top:90px; right:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Clinical Picture</p>
  <ul style="margin:0; padding-left:16px; font-size:12px; color:#444; line-height:1.9;">
    <li>Vaginal bleeding</li>
    <li>Pain</li>
    <li>Cessation of contractions</li>
    <li>Absence / deterioration of fetal heart rate</li>
    <li>Loss of station of the fetal head from the birth canal</li>
    <li>Easily palpable fetal parts</li>
    <li>Profound maternal tachycardia and hypotension</li>
  </ul>
</div>
'''
with open('slides/slide-19.html','w') as f: f.write(wrap('RU Severity Clinical', s19, page_num=19))

# ============================================================
# SLIDE 20 – Rupture Uterus: Management
# ============================================================
s20 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Rupture Uterus — Management</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C1};">
    <p style="margin:0 0 8px 0; font-size:17px; font-weight:700; color:{C1};">Prophylactic Management</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
      <li>Proper <strong>antenatal care</strong> (early detection of causes of obstructed labor)</li>
      <li>Grand multipara should <strong>deliver in hospital</strong></li>
      <li>Proper <strong>intranatal care</strong>:</li>
      <ul style="padding-left:18px;">
        <li>Judicious use of ecbolics</li>
        <li>Safe version, forceps, ventouse</li>
        <li>Exploration of birth canal after difficult or instrumental labor</li>
      </ul>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C5};">
    <p style="margin:0 0 8px 0; font-size:17px; font-weight:700; color:{C5};">Curative Management</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
      <li><strong>Emergent laparotomy</strong></li>
    </ul>
    <p style="margin:4px 0; font-size:13px; color:#444;">Then either:</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
      <li><strong>Repair</strong> of the uterine rupture</li>
      <li><strong>Hysterectomy</strong></li>
    </ul>
    <p style="margin:8px 0 0 0; font-size:13px; color:#444; line-height:1.4;"><strong>Internal iliac artery ligation</strong> in cases of broad ligament hematoma.</p>
  </div>
</div>
'''
with open('slides/slide-20.html','w') as f: f.write(wrap('RU Management', s20, page_num=20))

print("Slides 10-20 generated successfully.")
