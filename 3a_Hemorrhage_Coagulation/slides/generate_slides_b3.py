#!/usr/bin/env python3
"""Batch 3: Vasa Previa, DIC, Summary slides 21-31."""
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
# SLIDE 21 – Vasa Previa: Definition, Diagnosis, Causes
# ============================================================
s21 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Vasa Previa</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Definition</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.4;">Fetal hemorrhage (bleeding of <strong>fetal origin</strong>) due to laceration of abnormally situated umbilical (fetal) vessels.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px;">
    <p style="margin:0 0 4px 0; font-size:15px; font-weight:700; color:{C1};">Diagnosis</p>
    <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.7;">
      <li><strong>Antenatally:</strong> by Doppler ultrasonography</li>
      <li><strong>During labor:</strong> sudden fetal distress with <strong>minimal</strong> amount of vaginal bleeding (highly suspect it)</li>
    </ul>
  </div>
</div>

<p style="position:absolute; top:260px; left:50px; font-size:20px; font-weight:700; color:{C1}; z-index:10; margin:0;">Causes</p>

<div style="position:absolute; top:292px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; text-align:center; border-top:3px solid {C1};">
    <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C1};">Bi-lobed Placenta</p>
    <p style="margin:0; font-size:12px; color:#666;">Placenta has two separate lobes</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; text-align:center; border-top:3px solid {C5};">
    <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C5};">Velamentous Insertion</p>
    <p style="margin:0; font-size:12px; color:#666;">Umbilical cord inserts into the membranes</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; text-align:center; border-top:3px solid {C2};">
    <p style="margin:0 0 4px 0; font-size:14px; font-weight:700; color:{C1};">Succenturiate Lobe</p>
    <p style="margin:0; font-size:12px; color:#666;">Accessory lobe of placenta</p>
  </div>
</div>
'''
with open('slides/slide-21.html','w') as f: f.write(wrap('Vasa Previa', s21, page_num=21))

# ============================================================
# SLIDE 22 – Vasa Previa: Risk Factors & Management
# ============================================================
s22 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Vasa Previa — Risk Factors &amp; Management</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Risk Factors</p>
  <ul style="margin:0; padding-left:16px; font-size:13px; color:#444; line-height:1.8;">
    <li>Bilobed and succenturiate placentas</li>
    <li>Velamentous insertion of the cord</li>
    <li>Low-lying placenta</li>
    <li>Multiple gestation</li>
    <li>Pregnancies resulting from <strong>in vitro fertilization</strong></li>
  </ul>
</div>

<div style="position:absolute; top:90px; right:50px; width:420px; background:#ffffff; border-radius:8px; padding:14px 16px; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C1};">Management</p>
  <div style="border-left:3px solid {C1}; padding-left:12px;">
    <p style="margin:0; font-size:13px; color:#444; line-height:1.5;">When vasa previa is diagnosed <strong>prior to labor</strong>, elective <strong>Cesarean section</strong> is the delivery method of choice.</p>
  </div>
  <div style="margin-top:12px; background:rgba(0,109,119,0.06); border-radius:6px; padding:10px;">
    <p style="margin:0; font-size:12px; color:{C1}; line-height:1.4;"><strong>Key point:</strong> Vasa previa is a fetal hemorrhage — the blood lost is fetal blood, which can rapidly lead to fetal exsanguination.</p>
  </div>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:{C1}; border-radius:6px; padding:10px 14px;">
    <p style="margin:0; font-size:12px; color:#ffffff; line-height:1.4;"><strong>Antenatal diagnosis</strong> → Doppler ultrasound → Elective C/S</p>
  </div>
  <div style="background:{C5}; border-radius:6px; padding:10px 14px;">
    <p style="margin:0; font-size:12px; color:#ffffff; line-height:1.4;"><strong>Intrapartum suspicion</strong> → Fetal distress + minimal bleeding → Emergency C/S</p>
  </div>
</div>
'''
with open('slides/slide-22.html','w') as f: f.write(wrap('VP Risk Mgmt', s22, page_num=22))

# ============================================================
# SLIDE 23 – Kleihauer-Betke Test & Apt Test
# ============================================================
s23 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Diagnostic Tests</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C1};">
    <p style="margin:0 0 8px 0; font-size:17px; font-weight:700; color:{C1};">Kleihauer-Betke Test</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.5;">A blood test used to measure the amount of <strong>fetal hemoglobin</strong> transferred from a fetus to the mother's bloodstream.</p>
    <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8; margin-top:6px;">
      <li>Used to determine the required dose of <strong>Rh immune globulin</strong></li>
      <li>Used for detecting <strong>fetomaternal hemorrhage</strong></li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:10px; padding:18px 20px; border-top:4px solid {C5};">
    <p style="margin:0 0 8px 0; font-size:17px; font-weight:700; color:{C5};">Apt Test</p>
    <p style="margin:0; font-size:13px; color:#444; line-height:1.5;">Allows determination whether the source of blood is <strong>fetal</strong> (vasa previa) or <strong>maternal</strong>.</p>
    <p style="margin:8px 0 4px 0; font-size:13px; font-weight:600; color:{C1};">Procedure:</p>
    <ol style="margin:0; padding-left:18px; font-size:12px; color:#444; line-height:1.7;">
      <li>Place 5 mL water in each of 2 test tubes</li>
      <li>Add 5 drops vaginal blood to tube 1; 5 drops maternal (adult) blood to tube 2</li>
      <li>Add 6 drops 10% NaOH to each tube</li>
      <li>Observe for 2 minutes</li>
    </ol>
  </div>
</div>

<div style="position:absolute; bottom:28px; left:50px; right:50px; background:#ffffff; border-radius:8px; padding:10px 16px; border:1px dashed {C1}; z-index:10;">
  <p style="margin:0; font-size:13px; color:{C1}; line-height:1.4;"><strong>Apt Test Result:</strong> Maternal (adult) blood turns <strong>yellow-green-brown</strong> while fetal blood stays <strong>pink</strong>. If fetal blood → rapid delivery.</p>
</div>
'''
with open('slides/slide-23.html','w') as f: f.write(wrap('Diagnostic Tests', s23, page_num=23))

# ============================================================
# SLIDE 24 – Student Activity & Questions (APH)
# ============================================================
s24 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Student Activity — APH</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:18px 22px; border-left:4px solid {C1}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C1};">Emergency Cases Evaluation</p>
  <p style="margin:0; font-size:13px; color:#444; line-height:1.6;">Each group of students is requested to evaluate the emergency cases registration files in order to provide a report on:</p>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
    <li>The number of recorded departmental admitted cases of antepartum hemorrhage during the <strong>last three months</strong></li>
    <li><strong>Etiological classification</strong> of these cases</li>
    <li>Their <strong>outcome</strong></li>
  </ul>
</div>

<div style="position:absolute; top:250px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:18px 22px; border-left:4px solid {C5}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C5};">Ruptured Uterus — File Review</p>
  <p style="margin:0; font-size:13px; color:#444; line-height:1.6;">For included cases of ruptured uterus, look into the files of these cases in order to identify the <strong>possible underlying cause</strong> of this catastrophe.</p>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; background:{C1}; border-radius:8px; padding:12px 18px; z-index:10;">
  <p style="margin:0; font-size:14px; color:#ffffff; line-height:1.4; text-align:center;">📋 Questions: <a href="https://forms.gle/hzvEPyfmNCjJE1EE7" style="color:{C4};">https://forms.gle/hzvEPyfmNCjJE1EE7</a></p>
</div>
'''
with open('slides/slide-24.html','w') as f: f.write(wrap('Activity APH', s24, page_num=24))

# ============================================================
# SLIDE 25 – SECTION DIVIDER: DIC
# ============================================================
s25 = f'''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:{C1};"></div>
<svg style="position:absolute; top:0; left:0; width:960px; height:540px;" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect x="0" y="0" width="8" height="540" fill="{C4}"/>
  <circle cx="100" cy="100" r="160" fill="rgba(255,255,255,0.05)"/>
  <circle cx="850" cy="480" r="180" fill="rgba(255,255,255,0.04)"/>
</svg>
<p style="position:absolute; top:80px; left:60px; font-size:72px; font-weight:700; color:{C4}; opacity:0.5; z-index:10; margin:0; line-height:1;">02</p>
<p style="position:absolute; top:170px; left:60px; font-size:42px; font-weight:700; color:#ffffff; z-index:10; margin:0; line-height:1.2;">Disseminated<br>Intravascular<br>Coagulopathy</p>
<div style="position:absolute; top:310px; left:60px; width:80px; height:4px; background:{C4}; border-radius:2px; z-index:10;"></div>
<p style="position:absolute; top:340px; left:60px; font-size:16px; color:rgba(255,255,255,0.8); z-index:10; margin:0; max-width:500px;">Definition &bull; Etiology &bull; Investigations &bull; Treatment &bull; Student Activity</p>
'''
with open('slides/slide-25.html','w') as f: f.write(wrap('Section DIC', s25, page_num=25, bg_color=C1))

# ============================================================
# SLIDE 26 – DIC: Definition & Clinical Picture
# ============================================================
s26 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">DIC — Definition &amp; Clinical Picture</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:18px 22px; border-left:4px solid {C1}; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:16px; font-weight:700; color:{C1};">Definition</p>
  <p style="margin:0; font-size:14px; color:#444; line-height:1.6;">A disorder of hemostasis in which <strong>intravascular activation</strong> of both clotting and fibrinolytic systems occurs leading to <strong>consumption</strong> of coagulation factors and platelets.</p>
</div>

<div style="position:absolute; top:210px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:18px 22px; border-left:4px solid {C5}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C5};">Clinical Picture</p>
  <ul style="margin:0; padding-left:18px; font-size:14px; color:#444; line-height:1.9;">
    <li>The patient will experience <strong>systemic hemorrhage</strong> and oozing during operations</li>
    <li><strong>Postpartum hemorrhage</strong> (PPH)</li>
  </ul>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; background:rgba(0,109,119,0.08); border-radius:8px; padding:12px 18px; z-index:10;">
  <p style="margin:0; font-size:13px; color:{C1}; line-height:1.5;"><strong>Pathophysiology:</strong> Intravascular coagulation consumes clotting factors and platelets → depletion → uncontrolled bleeding. Simultaneously, fibrinolysis is activated, producing fibrin degradation products (D-dimer).</p>
</div>
'''
with open('slides/slide-26.html','w') as f: f.write(wrap('DIC Definition', s26, page_num=26))

# ============================================================
# SLIDE 27 – DIC: Etiology
# ============================================================
s27 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">DIC — Etiology in Pregnancy</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; right:50px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C1};">1. Preeclampsia &amp; Eclampsia</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Hypertensive disorders of pregnancy — endothelial damage triggers coagulation cascade.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C5};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C5};">2. Amniotic Fluid Embolism</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Amniotic fluid enters maternal circulation → triggers massive clotting.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C1};">3. Abruptio Placenta</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Release of thromboplastin from retroplacental clot into maternal circulation.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C5};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C5};">4. Vesicular Mole</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Hydatidiform mole can trigger DIC.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C1};">5. IUFD &amp; Missed Abortion</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Prolonged retention of dead fetus releases thromboplastin.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C5};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C5};">6. Incompatible Blood Transfusion</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Transfusion reaction triggers DIC.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C1};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C1};">7. Rupture Uterus</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Massive tissue trauma and hemorrhage.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:14px 16px; border-left:4px solid {C5};">
    <p style="margin:0; font-size:14px; font-weight:700; color:{C5};">8. Placenta Accreta</p>
    <p style="margin:4px 0 0 0; font-size:12px; color:#444; line-height:1.4;">Abnormal placental adherence can cause massive hemorrhage and DIC.</p>
  </div>
</div>
'''
with open('slides/slide-27.html','w') as f: f.write(wrap('DIC Etiology', s27, page_num=27))

# ============================================================
# SLIDE 28 – DIC: Investigations & Treatment
# ============================================================
s28 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">DIC — Investigations &amp; Treatment</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:90px; left:50px; width:430px; background:#ffffff; border-radius:10px; padding:16px 20px; border-top:4px solid {C1}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C1};">Investigations</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
    <div style="background:rgba(0,109,119,0.06); border-radius:6px; padding:10px; text-align:center;">
      <p style="margin:0; font-size:20px; font-weight:700; color:{C5}; line-height:1.2;">↑</p>
      <p style="margin:2px 0 0 0; font-size:11px; color:#444;"><strong>Increased</strong></p>
      <p style="margin:0; font-size:11px; color:#666;">Prothrombin time (PT)<br>PTT<br>FDP (D-dimer)</p>
    </div>
    <div style="background:rgba(226,149,120,0.06); border-radius:6px; padding:10px; text-align:center;">
      <p style="margin:0; font-size:20px; font-weight:700; color:{C1}; line-height:1.2;">↓</p>
      <p style="margin:2px 0 0 0; font-size:11px; color:#444;"><strong>Decreased</strong></p>
      <p style="margin:0; font-size:11px; color:#666;">Platelet count<br>Fibrinogen level</p>
    </div>
  </div>
</div>

<div style="position:absolute; top:90px; right:50px; width:430px; background:#ffffff; border-radius:10px; padding:16px 20px; border-top:4px solid {C5}; z-index:10;">
  <p style="margin:0 0 8px 0; font-size:16px; font-weight:700; color:{C5};">Treatment</p>
  <ol style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.9;">
    <li><strong>Treatment of the cause</strong> — most important step</li>
    <li>Transfusion of:</li>
    <ul style="padding-left:18px;">
      <li><strong>Fresh blood</strong></li>
      <li><strong>Fresh frozen plasma (FFP)</strong></li>
      <li><strong>Cryoprecipitate</strong> (fibrinogen replacement)</li>
      <li><strong>Platelets</strong></li>
    </ul>
    <li><strong>Anticoagulant</strong> therapy (e.g., heparin) in selected cases</li>
  </ol>
</div>

<div style="position:absolute; bottom:28px; left:50px; right:50px; background:{C1}; border-radius:6px; padding:8px 14px; z-index:10;">
  <p style="margin:0; font-size:12px; color:#ffffff; text-align:center;"><strong>Key principle:</strong> Treat the underlying cause first. Replacement therapy supports hemostasis while the cause is being addressed.</p>
</div>
'''
with open('slides/slide-28.html','w') as f: f.write(wrap('DIC Invest Tx', s28, page_num=28))

# ============================================================
# SLIDE 29 – DIC: Student Activity & Questions
# ============================================================
s29 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">Student Activity — DIC</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:100px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:24px 28px; border-left:4px solid {C1}; z-index:10;">
  <p style="margin:0 0 10px 0; font-size:18px; font-weight:700; color:{C1};">DIC Case Identification</p>
  <p style="margin:0; font-size:14px; color:#444; line-height:1.6;">Each group of students is assigned a task to check the investigations of <strong>five departmental admitted pregnant cases</strong> in order to identify whether they had DIC or not.</p>
</div>

<div style="position:absolute; top:280px; left:50px; right:50px; background:#ffffff; border-radius:10px; padding:18px 22px; border:1px dashed {C5}; z-index:10;">
  <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C5};">Suggested Approach</p>
  <ul style="margin:0; padding-left:18px; font-size:13px; color:#444; line-height:1.8;">
    <li>Review PT, PTT, platelet count, fibrinogen, D-dimer for each case</li>
    <li>Look for the characteristic pattern: ↑PT, ↑PTT, ↑D-dimer, ↓platelets, ↓fibrinogen</li>
    <li>Correlate with clinical presentation (hemorrhage, oozing, PPH)</li>
    <li>Identify the underlying obstetrical cause</li>
  </ul>
</div>

<div style="position:absolute; bottom:30px; left:50px; right:50px; background:{C1}; border-radius:8px; padding:12px 18px; z-index:10;">
  <p style="margin:0; font-size:14px; color:#ffffff; line-height:1.4; text-align:center;">📋 Questions: <a href="https://forms.gle/YtkyrT7QnGwrmSVf8" style="color:{C4};">https://forms.gle/YtkyrT7QnGwrmSVf8</a></p>
</div>
'''
with open('slides/slide-29.html','w') as f: f.write(wrap('Activity DIC', s29, page_num=29))

# ============================================================
# SLIDE 30 – APH Overview Comparison Table
# ============================================================
s30 = f'''
<p style="position:absolute; top:28px; left:50px; font-size:30px; font-weight:700; color:{C1}; z-index:10; margin:0;">APH — Placenta Previa vs Abruptio Placenta</p>
<div style="position:absolute; top:68px; left:50px; width:70px; height:3px; background:{C5}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:88px; left:50px; right:50px; z-index:10;">
  <table style="width:100%; border-collapse:collapse; font-size:13px;">
    <tr style="background:{C1};">
      <th style="padding:10px 12px; color:#fff; text-align:left; border:1px solid {C1};">Feature</th>
      <th style="padding:10px 12px; color:#fff; text-align:left; border:1px solid {C1};">Placenta Previa</th>
      <th style="padding:10px 12px; color:#fff; text-align:left; border:1px solid {C1};">Abruptio Placenta</th>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Placenta Site</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Lower uterine segment</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Upper uterine segment (normal)</td>
    </tr>
    <tr style="background:{C3};">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Pain</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Painless</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Painful (abdominal pain)</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Uterine Tone</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Lax, soft</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Board-like, rigid, tender</td>
    </tr>
    <tr style="background:{C3};">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Fundal Height</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Equals gestational age</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Greater than gestational age</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Fetal Palpation</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Easy</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Difficult</td>
    </tr>
    <tr style="background:{C3};">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">FHS</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Usually normal</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Distress or absent</td>
    </tr>
    <tr style="background:#ffffff;">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Bleeding</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">Always revealed</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">80% revealed / 20% concealed</td>
    </tr>
    <tr style="background:{C3};">
      <td style="padding:8px 10px; border:1px solid #ddd; font-weight:600; color:{C1};">Incidence</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">1/200 pregnancies</td>
      <td style="padding:8px 10px; border:1px solid #ddd;">1/100 pregnancies</td>
    </tr>
  </table>
</div>
'''
with open('slides/slide-30.html','w') as f: f.write(wrap('Comparison', s30, page_num=30))

# ============================================================
# SLIDE 31 – Summary / Closing
# ============================================================
s31 = f'''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, {C1} 0%, {C1} 45%, {C2} 100%);"></div>
<svg style="position:absolute; top:0; left:0; width:960px; height:540px;" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <circle cx="150" cy="-30" r="200" fill="rgba(255,255,255,0.05)"/>
  <circle cx="850" cy="500" r="250" fill="rgba(255,255,255,0.04)"/>
</svg>
<p style="position:absolute; top:40px; left:60px; font-size:36px; font-weight:700; color:#ffffff; z-index:10; margin:0;">Key Takeaways</p>
<div style="position:absolute; top:88px; left:60px; width:60px; height:3px; background:{C4}; border-radius:1.5px; z-index:10;"></div>

<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:14px; z-index:10;">
  <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:14px 18px; backdrop-filter:blur(2px);">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C4};">Antepartum Hemorrhage</p>
    <ul style="margin:0; padding-left:16px; font-size:12px; color:rgba(255,255,255,0.9); line-height:1.7;">
      <li>4 types: Placenta previa, Abruptio, Vasa previa, Extraplacental</li>
      <li>Placenta previa → painless bleeding, lax abdomen</li>
      <li>Abruptio → painful, rigid, board-like abdomen</li>
      <li>Rupture uterus → emergent laparotomy</li>
      <li>Vasa previa → fetal hemorrhage, elective C/S</li>
    </ul>
  </div>
  <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:14px 18px; backdrop-filter:blur(2px);">
    <p style="margin:0 0 6px 0; font-size:15px; font-weight:700; color:{C4};">Disseminated Intravascular Coagulopathy</p>
    <ul style="margin:0; padding-left:16px; font-size:12px; color:rgba(255,255,255,0.9); line-height:1.7;">
      <li>Consumption coagulopathy — clotting + fibrinolysis activated</li>
      <li>Causes: Pre-eclampsia, AFE, Abruptio, IUFD, etc.</li>
      <li>Investigations: ↑PT, ↑PTT, ↑D-dimer, ↓platelets, ↓fibrinogen</li>
      <li>Treatment: treat cause + replace factors (FFP, cryo, platelets)</li>
    </ul>
  </div>
</div>

<div style="position:absolute; bottom:50px; left:60px; right:60px; background:rgba(255,255,255,0.1); border-radius:8px; padding:12px 18px; z-index:10;">
  <p style="margin:0; font-size:14px; color:rgba(255,255,255,0.8); text-align:center;">Medical Obstetric Disorders — Hemorrhage &amp; Coagulation | Complete Lecture Notes</p>
</div>
'''
with open('slides/slide-31.html','w') as f: f.write(wrap('Summary', s31, page_num=31, bg_color=C1))

print("Slides 21-31 generated successfully.")
print("Total: 31 slides")
