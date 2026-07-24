import os

# Color Palette 10: Education & Charts
C = {
    'dart': '#264653',   # dark teal
    'teal': '#2a9d8f',   # teal
    'gold': '#e9c46a',   # yellow/gold
    'org' : '#f4a261',   # orange
    'coral':'#e76f51',   # coral/red
    'white':'#ffffff',
    'bg'  : '#f8f9fa',
    'text':'#264653',
}

BADGE = '''
<div style="position:absolute; right:32px; bottom:24px; z-index:100;">
  <svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
    <circle cx="20" cy="20" r="18" fill="#264653" stroke="#2a9d8f" stroke-width="2"/>
    <text x="20" y="26" text-anchor="middle" font-family="Times New Roman, serif" font-size="16" font-weight="700" fill="#ffffff">PAGE</text>
  </svg>
</div>'''

def slide_html(content, page_num, is_cover=False):
    badge = '' if is_cover else BADGE.replace('PAGE', str(page_num))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body {{ margin:0; padding:0; width:100%; height:100%; overflow:hidden; display:flex; justify-content:center; align-items:center; background:#000; }}
.slide-content {{ width:960px; height:540px; position:relative; transform-origin:center center; }}
</style>
<script>
function scaleSlide(){{const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform=`scale(${{sc}})`;s.style.transformOrigin='center center';s.style.flexShrink='0';}}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px; height:540px; background:#fdf0d5; font-family:'Times New Roman',serif; color:#264653; overflow:hidden;">
{content}
{badge}
</div>
</body>
</html>'''

def write_slide(num, content, is_cover=False):
    fname = f'slide-{num:02d}.html'
    with open(fname, 'w') as f:
        f.write(slide_html(content, num, is_cover))
    print(f'  Wrote {fname}')

# ============ SLIDE GENERATION ============
n = 0

# ----- COVER -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, #264653 0%, #2a9d8f 100%);"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <circle cx="800" cy="100" r="200" fill="rgba(233,196,106,0.08)"/>
    <circle cx="150" cy="450" r="150" fill="rgba(244,162,97,0.08)"/>
    <circle cx="480" cy="270" r="300" fill="rgba(231,111,81,0.05)"/>
    <line x1="60" y1="180" x2="160" y2="180" stroke="#e9c46a" stroke-width="5"/>
  </svg>
</div>
<div style="position:absolute; top:120px; left:70px;">
  <p style="font-size:28px; color:rgba(255,255,255,0.7); margin:0; font-weight:400;">Department of Obstetrics &amp; Gynecology</p>
  <p style="font-size:52px; color:#e9c46a; margin:20px 0 0 0; font-weight:700; line-height:1.1;">Early Pregnancy<br>Complications</p>
  <p style="font-size:22px; color:rgba(255,255,255,0.85); margin:30px 0 0 0; font-weight:400;">Abortion &bull; Ectopic Pregnancy &bull; Gestational Trophoblastic Disease</p>
  <p style="font-size:16px; color:rgba(255,255,255,0.5); margin:50px 0 0 0;">Obstetrics &amp; Gynecology &mdash; Clinical Module</p>
</div>
''', is_cover=True)

# ----- TOC -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#264653;"></div>
<div style="position:absolute; top:30px; left:60px;">
  <p style="font-size:32px; color:#e9c46a; font-weight:700; margin:0;">Table of Contents</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:12px;"></div>
</div>
<div style="position:absolute; top:100px; left:60px; right:60px; display:grid; grid-template-columns:1fr; gap:12px;">
  <div style="display:flex; align-items:center; gap:16px; background:rgba(255,255,255,0.08); padding:14px 20px; border-radius:6px;">
    <span style="font-size:24px; font-weight:700; color:#e9c46a; width:40px;">01</span>
    <span style="font-size:20px; color:#ffffff; font-weight:400;">Abortion &mdash; Definition, Types, Management &amp; Recurrent Abortion</span>
  </div>
  <div style="display:flex; align-items:center; gap:16px; background:rgba(255,255,255,0.08); padding:14px 20px; border-radius:6px;">
    <span style="font-size:24px; font-weight:700; color:#e9c46a; width:40px;">02</span>
    <span style="font-size:20px; color:#ffffff; font-weight:400;">Ectopic Pregnancy &mdash; Types, Diagnosis, Medical &amp; Surgical Management</span>
  </div>
  <div style="display:flex; align-items:center; gap:16px; background:rgba(255,255,255,0.08); padding:14px 20px; border-radius:6px;">
    <span style="font-size:24px; font-weight:700; color:#e9c46a; width:40px;">03</span>
    <span style="font-size:20px; color:#ffffff; font-weight:400;">Gestational Trophoblastic Disease &mdash; Hydatidiform Mole, GTT, Management</span>
  </div>
</div>
''')

print("=== SECTION 1: ABORTION ===")

# ----- Section Divider: Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, #264653 0%, #1a3a3f 100%);"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="8" height="540" fill="#e9c46a"/>
  </svg>
</div>
<div style="position:absolute; top:140px; left:80px;">
  <p style="font-size:28px; color:#e9c46a; font-weight:400; margin:0;">Chapter 21</p>
  <p style="font-size:48px; color:#ffffff; font-weight:700; margin:16px 0 0 0; line-height:1.1;">Abortion</p>
  <p style="font-size:18px; color:rgba(255,255,255,0.65); margin:24px 0 0 0;">Termination of pregnancy before viability of the fetus</p>
</div>
<div style="position:absolute; bottom:80px; left:80px;">
  <p style="font-size:14px; color:rgba(255,255,255,0.4); margin:0;">Video: <span style="color:#2a9d8f;">https://youtu.be/YntEqJ-WD3o</span></p>
</div>
''')

# ----- ILOs Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Intended Learning Outcomes</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:20px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px; border-left:4px solid #2a9d8f; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:16px; color:#264653; margin:0 0 8px 0; line-height:1.5;">&#8226; Differentiate different types of abortion</p>
    <p style="font-size:16px; color:#264653; margin:0 0 8px 0; line-height:1.5;">&#8226; Describe the clinical management of variable types of abortion</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px; border-left:4px solid #e9c46a; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:16px; color:#264653; margin:0 0 8px 0; line-height:1.5;">&#8226; Explain the etiology, investigations and management of recurrent abortion</p>
  </div>
</div>
''')

# ----- Definition & Incidence -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Abortion &mdash; Definition &amp; Incidence</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.6;">Termination of pregnancy before viability of the fetus i.e. before <strong>20 weeks</strong>.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Incidence</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.6;">Varies between <strong>12&ndash;25%</strong> of all pregnancies.</p>
  </div>
</div>
''')

# ----- Etiology -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Etiology of Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.7;">&#8226; <strong>Chromosomal abnormalities</strong>: 50% of early abortions</p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Maternal infections</strong>: Acute fever</p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Trauma</strong>: External or during operations</p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Immunological causes</strong>: SLE and Antiphospholipid antibodies</p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Uterine defects</strong>: Septum, Asherman's syndrome</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.7;">&#8226; <strong>Idiopathic</strong></p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Endocrine</strong>: Progesterone deficiency, Hypothyroidism</p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Drugs and environmental</strong> causes</p>
    <p style="font-size:16px; color:#264653; margin:4px 0; line-height:1.7;">&#8226; <strong>Maternal anoxia and malnutrition</strong></p>
  </div>
</div>
''')

# ----- Threatened Abortion CP -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Threatened Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Clinical Picture</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Symptoms and signs of pregnancy coincide with its duration.</li>
      <li><strong>Vaginal bleeding</strong>: slight or mild, bright red in colour.</li>
      <li><strong>Pain</strong>: absent or slight.</li>
      <li><strong>Cervix</strong>: closed.</li>
      <li><strong>Ultrasound</strong>: living fetus.</li>
    </ul>
  </div>
</div>
<div style="position:absolute; bottom:80px; left:60px; right:60px;">
  <div style="background:rgba(42,157,143,0.1); border-radius:8px; padding:12px 20px; border-left:4px solid #2a9d8f;">
    <p style="font-size:14px; color:#264653; margin:0;"><strong>Key feature</strong>: Bleeding with closed cervix and viable fetus &mdash; pregnancy may continue.</p>
  </div>
</div>
''')

# ----- Threatened Abortion Mx -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Threatened Abortion &mdash; Management</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:2;">
      <li><strong>Bed rest</strong> and avoid strenuous activity and sexual intercourse.</li>
      <li><strong>Progesterone</strong> supplementation.</li>
      <li><strong>Follow up</strong> with serial ultrasound and clinical assessment.</li>
    </ul>
  </div>
</div>
''')

# ----- Inevitable Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Inevitable Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Clinical Picture</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Symptoms and signs of pregnancy.</li>
      <li><strong>Heavy vaginal bleeding</strong> with clots.</li>
      <li><strong>Suprapubic colic</strong> referred to the back.</li>
      <li><strong>Dilated cervix</strong>.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:20px; color:#e76f51; font-weight:700; margin:0 0 12px 0;">Management</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li><strong>Medical</strong>: oxytocin drip, prostaglandins.</li>
      <li><strong>Surgical</strong>: evacuation.</li>
      <li>Blood transfusion if needed.</li>
    </ul>
  </div>
</div>
''')

# ----- Complete Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Complete Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">All products of conception have been expelled from the uterus.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Clinical Picture</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Bleeding: mild and decreases.</li>
      <li>Cessation of pain.</li>
      <li>Closed cervix.</li>
      <li>Uterus: slightly larger than normal.</li>
      <li>Ultrasound: shows empty cavity.</li>
    </ul>
  </div>
</div>
<div style="position:absolute; bottom:80px; left:60px; right:60px;">
  <div style="background:rgba(42,157,143,0.1); border-radius:8px; padding:12px 20px; border-left:4px solid #2a9d8f;">
    <p style="font-size:16px; color:#264653; margin:0;"><strong>Management</strong>: Ecbolics and antibiotics. <strong>No evacuation</strong> required.</p>
  </div>
</div>
''')

# ----- Incomplete Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Incomplete Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Retention of a part of the products of conception inside the uterus.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Clinical Picture</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Passage of a part of the conception products.</li>
      <li>Bleeding is continuous.</li>
      <li>Opened cervix.</li>
      <li>Uterus: less than period of amenorrhea.</li>
      <li>Ultrasonography: shows the retained contents.</li>
    </ul>
  </div>
  <div style="background:rgba(231,111,81,0.1); border-radius:8px; padding:12px 20px; border-left:4px solid #e76f51; margin-top:12px;">
    <p style="font-size:16px; color:#264653; margin:0;"><strong>Management</strong>: Evacuation (medical or surgical).</p>
  </div>
</div>
''')

# ----- Cervical Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Cervical Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">The products of conception is separated from the uterus but retained inside the cervical canal.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Clinical Picture</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Bleeding with severe lower abdominal pain referred to the back.</li>
      <li>On examination, the products of conception are felt through the dilated cervix.</li>
    </ul>
  </div>
  <div style="background:rgba(231,111,81,0.1); border-radius:8px; padding:12px 20px; border-left:4px solid #e76f51; margin-top:12px;">
    <p style="font-size:16px; color:#264653; margin:0;"><strong>Management</strong>: Cervical dilatation and evacuation of cervical contents followed by curettage.</p>
  </div>
</div>
''')

# ----- Missed Abortion Symptoms & Signs -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Missed Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0;">Retention of dead products of conception.</p>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:18px; color:#e76f51; font-weight:700; margin:0 0 8px 0;">Symptoms</p>
      <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
        <li>Regression of pregnancy symptoms (nausea, vomiting, breast symptoms).</li>
        <li>The abdomen does not increase.</li>
        <li>The fetal movements are not felt.</li>
        <li>Dark brown vaginal discharge (prune juice discharge).</li>
      </ul>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:18px; color:#e76f51; font-weight:700; margin:0 0 8px 0;">Signs</p>
      <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
        <li>The uterus fails to grow and becomes firmer.</li>
        <li>The cervix is closed.</li>
        <li>Absent fetal heart sounds.</li>
      </ul>
    </div>
  </div>
</div>
''')

# ----- Missed Abortion Investigations & Treatment -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Missed Abortion &mdash; Investigation &amp; Treatment</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Investigations</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Pregnancy test becomes <strong>negative</strong> within two weeks from the ovum death.</li>
      <li>Ultrasound shows a <strong>collapsed gestational sac</strong>, absent fetal heart pulsations or fetal movement.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Treatment</p>
    <p style="font-size:16px; color:#264653; margin:0 0 6px 0;"><strong>Evacuation</strong></p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>&lt;12 weeks: <strong>Surgical evacuation</strong></li>
      <li>&gt;12 weeks: <strong>Medical evacuation</strong> (e.g. by Prostaglandins or Oxytocin)</li>
    </ul>
  </div>
</div>
''')

# ----- Septic Abortion Def & Micro -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Septic Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0;">It is any type of abortion complicated by infection.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Microbiology</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.7;">
      <em>E. coli</em>, Bacteroides, anaerobic streptococci, Clostridia, Streptococci and Staphylococci are the most causative organisms.
    </p>
  </div>
</div>
''')

# ----- Septic Abortion Clinical Picture -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Septic Abortion &mdash; Clinical Picture</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#e76f51; font-weight:700; margin:0 0 8px 0;">General Examination</p>
    <ul style="font-size:14px; color:#264653; margin:0; padding-left:16px; line-height:1.6;">
      <li>Pyrexia, Rigors and tachycardia</li>
      <li>Malaise, sweating, headache, joint pain</li>
      <li>Jaundice</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#e76f51; font-weight:700; margin:0 0 8px 0;">Abdominal Examination</p>
    <ul style="font-size:14px; color:#264653; margin:0; padding-left:16px; line-height:1.6;">
      <li>Tenderness</li>
      <li>Rigidity</li>
      <li>Distension</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#e76f51; font-weight:700; margin:0 0 8px 0;">Local Examination</p>
    <ul style="font-size:14px; color:#264653; margin:0; padding-left:16px; line-height:1.6;">
      <li>Offensive vaginal discharge</li>
      <li>Tender uterus</li>
    </ul>
  </div>
</div>
''')

# ----- Septic Abortion Treatment -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Septic Abortion &mdash; Treatment</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
      <li><strong>Resuscitation</strong></li>
      <li>Prompt administration of <strong>intravenous broad-spectrum antibiotics</strong> followed by uterine evacuation.</li>
      <li>Rest in <strong>semi-sitting position</strong>.</li>
      <li>Observation for <strong>vital signs</strong>.</li>
      <li><strong>Oxytocin infusion</strong>: to control bleeding and enhance expulsion.</li>
      <li>Evacuation of the uterus after commencing IV therapy.</li>
      <li><strong>Hysterectomy</strong> may be the last choice to save life.</li>
    </ul>
  </div>
</div>
''')

# ----- Other Types of Abortion -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Other Types of Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:20px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
    <p style="font-size:20px; color:#264653; font-weight:700; margin:0 0 8px 0;">Therapeutic Abortion</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Abortion induced for a <strong>medical indication</strong>.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e76f51;">
    <p style="font-size:20px; color:#264653; font-weight:700; margin:0 0 8px 0;">Criminal Abortion</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Illegal abortion induced for a <strong>non-medical indication</strong>.</p>
  </div>
</div>
''')

# ----- Recurrent Abortion Definition & Causes -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Recurrent (Habitual) Abortion</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 6px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0;">Three (two by some authors) or more consecutive spontaneous abortions.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Causes (Persistent causes of abortion)</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px 20px;">
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Genetic factors</strong>: Paternal chromosomal rearrangements, embryonic abnormalities</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Anatomical factors</strong>: Septate uterus, cervical incompetence</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Antiphospholipid syndrome</strong></p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Endocrinological</strong>: DM, thyroid abnormalities</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Thrombophilias</strong></p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Infective agents</strong>: STORCH</p>
    </div>
  </div>
</div>
''')

# ----- Recurrent Abortion Investigations -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Recurrent Abortion &mdash; Investigations</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">1. Laboratory</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.7;">
      <strong>Urine analysis</strong>: pus cells (UTI), proteins (nephritis) &amp; glucose (DM).<br>
      <strong>Blood</strong>: serum creatinine, antiphospholipid antibodies and coagulation profile.
    </p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">2. Imaging</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.7;">
      <strong>Ultrasound</strong>: To exclude submucous fibroid, incompetent cervix.<br>
      <strong>HSG</strong>: To exclude submucous fibroid, incompetent cervix, intrauterine adhesions.
    </p>
  </div>
</div>
<div style="position:absolute; top:310px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">3. Hysteroscopy</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.5;">To exclude submucous fibroid, intrauterine adhesions, congenital anomalies of uterine cavity.</p>
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:12px 0 4px 0;">4. Genetic Study</p>
    <p style="font-size:15px; color:#264653; margin:0;">Of the abortus to exclude chromosomal aberrations.</p>
  </div>
</div>
''')

# ----- Recurrent Abortion Treatment Before Pregnancy -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Recurrent Abortion &mdash; Treatment</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
    <p style="font-size:18px; color:#264653; font-weight:700; margin:0 0 10px 0;">a) Before Pregnancy</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.7;">
      Treat detectable causes:<br>
      &#8226; Hysteroscopic resection of uterine septum or submucous fibroid.<br>
      &#8226; Treatment of luteal phase defect.<br>
      &#8226; Strict control of DM.
    </p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e9c46a;">
    <p style="font-size:18px; color:#264653; font-weight:700; margin:0 0 10px 0;">b) During Pregnancy</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.7;">
      &#8226; <strong>Rest</strong>: Physical, mental (sedation) and sexual abstinence.<br>
      &#8226; <strong>Diet</strong>: Good balanced diet.<br>
      &#8226; <strong>Natural progesterone</strong>: if proved progesterone deficiency.<br>
      &#8226; <strong>Others</strong>: Strict DM control, cerclage for incompetent cervix, Heparin for Antiphospholipid syndrome.
    </p>
  </div>
</div>
''')

# ----- Student Activity & Questions (Abortion) -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Student Activity &amp; Questions</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Student Activity</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Each student is requested to diagnose the type of abortion and its management by prepared histories of first trimester abortion by the tutor guide during bedside teaching part of the clinical round.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Questions</p>
    <p style="font-size:16px; color:#264653; margin:0;">Online form: <span style="color:#2a9d8f;">https://forms.gle/sn9d7eqytqp5qbsK8</span></p>
  </div>
</div>
''')

print("=== SECTION 2: ECTOPIC PREGNANCY ===")

# ----- Section Divider: Ectopic Pregnancy -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, #264653 0%, #1a3a3f 100%);"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="8" height="540" fill="#e9c46a"/>
  </svg>
</div>
<div style="position:absolute; top:140px; left:80px;">
  <p style="font-size:28px; color:#e9c46a; font-weight:400; margin:0;">Chapter 22</p>
  <p style="font-size:48px; color:#ffffff; font-weight:700; margin:16px 0 0 0; line-height:1.1;">Ectopic Pregnancy</p>
  <p style="font-size:18px; color:rgba(255,255,255,0.65); margin:24px 0 0 0;">Implantation of the fertilized ovum outside the uterine cavity</p>
</div>
<div style="position:absolute; bottom:80px; left:80px;">
  <p style="font-size:14px; color:rgba(255,255,255,0.4); margin:0;">Video: <span style="color:#2a9d8f;">https://youtu.be/NPR1ocFayFc</span></p>
</div>
''')

# ----- EP ILOs -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Intended Learning Outcomes</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
      <li>Identify variable risk factors of ectopic pregnancy.</li>
      <li>Identify different types of ectopic pregnancy.</li>
      <li>Describe clinical picture of ectopic pregnancy.</li>
      <li>Request suitable investigations for diagnosis of ectopic pregnancy.</li>
      <li>Understand the concept of discriminatory zone when both ultrasound and hCG are used for diagnosis.</li>
      <li>Describe variable treatment policies of ectopic pregnancy.</li>
    </ul>
  </div>
</div>
''')

# ----- EP Definition & Sites -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Definition &amp; Sites</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Implantation of the fertilized ovum outside the uterine cavity.</p>
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:16px 0 8px 0;">Incidence</p>
    <p style="font-size:16px; color:#264653; margin:0;">2% of all pregnancies.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Sites of Ectopic Pregnancy</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px 16px;">
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Tubal</strong> (99% &mdash; commonest)</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Cervical</strong></p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Rudimentary horn</strong></p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Cornual</strong> (Interstitial)</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Ovarian</strong></p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Abdominal</strong></p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Broad ligamentary</strong></p>
    </div>
  </div>
</div>
''')

# ----- EP Risk Factors -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Etiology / Risk Factors</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <ul style="font-size:16px; color:#264653; margin:0; padding-left:18px; line-height:1.8;">
        <li>Pelvic Inflammatory Disease (PID)</li>
        <li>Previous ectopic</li>
        <li>Previous tubal surgery</li>
        <li>Previous pelvic or abdominal surgery</li>
        <li>Tubal pathology</li>
      </ul>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <ul style="font-size:16px; color:#264653; margin:0; padding-left:18px; line-height:1.8;">
        <li>IUCD (Intrauterine Contraceptive Device)</li>
        <li>Tubal sterilization</li>
        <li>Cigarette smoking</li>
      </ul>
    </div>
  </div>
</div>
<div style="position:absolute; bottom:80px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 6px 0;">Tubal Implantation Sites</p>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:8px;">
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Ampulla</strong>: 80%</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; <strong>Isthmus</strong>: 12%</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; Interstitial part</p>
      <p style="font-size:15px; color:#264653; margin:0;">&#8226; Fimbrial end</p>
    </div>
  </div>
</div>
''')

# ----- EP Clinical Picture Symptoms -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Clinical Picture &mdash; Symptoms</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
    <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:20px; color:#e76f51; font-weight:700; margin:0 0 12px 0;">Symptoms</p>
      <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
        <li>History of <strong>missed period</strong></li>
        <li><strong>Vaginal bleeding</strong></li>
        <li><strong>Abdominal or pelvic pain</strong></li>
      </ul>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 12px 0;">Signs</p>
      <p style="font-size:16px; color:#264653; margin:0 0 4px 0;"><strong>General:</strong> Signs of pregnancy.</p>
      <p style="font-size:16px; color:#264653; margin:0 0 4px 0;"><strong>Abdominal:</strong> Abdominal or pelvic tenderness, abdominal rigidity.</p>
      <p style="font-size:16px; color:#264653; margin:0;"><strong>Vaginal:</strong> Soft enlarged uterus, cervical motion tenderness (jumping sign).</p>
    </div>
  </div>
</div>
''')

# ----- EP Types: Undisturbed, Acute, Chronic -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Types of Ectopic Pregnancy</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="display:grid; grid-template-columns:1fr; gap:10px;">
    <div style="background:#ffffff; border-radius:8px; padding:14px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-left:5px solid #2a9d8f;">
      <p style="font-size:17px; color:#264653; font-weight:700; margin:0 0 4px 0;">1. Undisturbed Ectopic</p>
      <p style="font-size:15px; color:#264653; margin:0;">The clinical picture is as mentioned before (missed period, vaginal bleeding, pain, closed cervix, adnexal mass).</p>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:14px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-left:5px solid #e76f51;">
      <p style="font-size:17px; color:#264653; font-weight:700; margin:0 0 4px 0;">2. Acute Disturbed Ectopic</p>
      <p style="font-size:15px; color:#264653; margin:0;"><strong>General:</strong> Signs of pregnancy, pallor, fainting attacks, shoulder pain, shock, tachycardia, hypotension. <strong>Abdominal:</strong> Tenderness, rebound tenderness, rigidity. <strong>Vaginal:</strong> Severe cervical motion tenderness.</p>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:14px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-left:5px solid #e9c46a;">
      <p style="font-size:17px; color:#264653; font-weight:700; margin:0 0 4px 0;">3. Chronic Disturbed Ectopic</p>
      <p style="font-size:15px; color:#264653; margin:0;">Recurrent lower abdominal pain, pelvic heaviness, rectal tenesmus, dysuria, dyschezia, dyspareunia. Tender cervical motion, tender adnexal swelling.</p>
    </div>
  </div>
</div>
''')

# ----- EP Investigations: hCG -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Investigations &mdash; &beta;-hCG</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">1. Quantitative &beta;-hCG</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
      <li>If the test is <strong>negative</strong>, normal and abnormal pregnancy including ectopic are <strong>excluded</strong>.</li>
      <li><strong>Doubling time</strong>: In normal pregnancy, &beta;-hCG doubles every <strong>48 hours</strong> during the first 42 days.</li>
      <li>Ectopic pregnancy usually shows <strong>&lt;66% increase</strong> in &beta;-hCG level within 48 hours.</li>
    </ul>
  </div>
</div>
''')

# ----- EP Investigations: Ultrasound -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Investigations &mdash; Ultrasound &amp; Doppler</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:20px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">2. Ultrasound and Doppler</p>
    <p style="font-size:16px; color:#264653; margin:0 0 10px 0;"><strong>Visualization of intrauterine sac + fetal pulsation</strong>: mostly excludes ectopic pregnancy.</p>
    <p style="font-size:16px; color:#264653; font-weight:700; margin:0 0 6px 0;">Signs of Ectopic Pregnancy:</p>
    <ol style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Empty uterine cavity</li>
      <li>Free fluid in Douglas pouch</li>
      <li>Adnexal swelling: if associated with fetal pulsation &rarr; sure sign of ectopic</li>
    </ol>
  </div>
</div>
''')

# ----- The Discriminatory Zone -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Discriminatory Zone &amp; Other Tests</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">3. hCG + U/S: Discriminatory Zone</p>
    <p style="font-size:15px; color:#264653; margin:0 0 6px 0;"><strong>Definition</strong>: hCG level at which all intrauterine pregnancies should be visible on US.</p>
    <p style="font-size:15px; color:#264653; margin:0;"><strong>Values</strong>:<br>TAU: 6000 mIU/ml<br>TVU: 2000 mIU/ml</p>
    <p style="font-size:15px; color:#264653; margin:8px 0 0 0;">If hCG is above the discriminatory zone and uterus is empty on U/S &rarr; <strong>ectopic pregnancy</strong>.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">4. Progesterone</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.5;">It is <strong>lower</strong> in ectopic than normal pregnancy (&lt; 15 ng/ml).</p>
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:16px 0 6px 0;">5. Laparoscopy</p>
    <p style="font-size:15px; color:#264653; margin:0;">For diagnosis and treatment.</p>
  </div>
</div>
''')

# ----- Differential Diagnosis -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Differential Diagnosis</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
    <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
      <p style="font-size:17px; color:#264653; font-weight:700; margin:0 0 8px 0;">1. Other Causes of Bleeding in Early Pregnancy</p>
      <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
        <li>Abortion</li>
        <li>Vesicular mole (GTD)</li>
      </ul>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e76f51;">
      <p style="font-size:17px; color:#264653; font-weight:700; margin:0 0 8px 0;">2. Other Causes of Acute Abdomen During Pregnancy</p>
      <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
        <li>Appendicitis</li>
        <li>Ovarian cyst accident</li>
        <li>Others</li>
      </ul>
    </div>
  </div>
</div>
''')

# ----- Resuscitation -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Treatment &mdash; Resuscitation</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#e76f51; border-radius:8px; padding:20px 24px; color:#ffffff;">
    <p style="font-size:18px; font-weight:700; margin:0 0 8px 0;">Immediate Resuscitation in Unstable Patient</p>
    <ul style="font-size:16px; margin:0; padding-left:20px; line-height:1.8;">
      <li>2 large bore IV lines + fluids</li>
      <li>Oxygen: 100% by mask</li>
      <li>Cardiac monitor and pulse-oximetry</li>
      <li>CBC and blood groups</li>
      <li>Blood transfusion</li>
    </ul>
  </div>
</div>
''')

# ----- Expectant Management -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Treatment &mdash; Expectant Management</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Indications</p>
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
      <li>Women who are <strong>clinically stable</strong>.</li>
      <li>Size of the ectopic pregnancy is <strong>&lt; 3.5 cm</strong> with no visible heartbeat on TVU.</li>
      <li>Serum &beta;-hCG <strong>less than 1500 IU/L</strong>.</li>
    </ul>
  </div>
</div>
''')

# ----- Medical Treatment Indications -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Medical Treatment &mdash; Methotrexate</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Indications</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>No significant pain.</li>
      <li>Unruptured tubal ectopic pregnancy with adnexal mass <strong>&lt; 3.5 cm</strong> and no visible fetal cardiac pulsations.</li>
      <li>&beta;-hCG <strong>&lt; 1500 IU/L</strong>.</li>
      <li>No intrauterine pregnancy.</li>
      <li>The patient is able to return for follow up.</li>
    </ul>
  </div>
</div>
''')

# ----- MTX Contraindications -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Methotrexate &mdash; Contraindications</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px 20px;">
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Hepatic dysfunction</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Renal disease (Cr &gt; 1.5 mg/dL)</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Active peptic ulcer disease</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Blood diseases (WBC &lt; 3000/&mu;L or platelets &lt; 100,000/&mu;L)</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Poor patient compliance</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; History of active hepatic or renal disease</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Presence of fetal cardiac activity</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Breast feeding</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Known sensitivity to methotrexate</p>
      <p style="font-size:14px; color:#264653; margin:0;">&#8226; Active pulmonary disease</p>
    </div>
  </div>
</div>
''')

# ----- MTX Protocols -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:30px; left:60px;">
  <p style="font-size:32px; color:#264653; font-weight:700; margin:0;">Methotrexate &mdash; Protocols</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:95px; left:60px; right:60px;">
  <table style="width:100%; border-collapse:collapse; font-size:14px; color:#264653; background:#ffffff; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-radius:8px; overflow:hidden;">
    <tr style="background:#264653; color:#ffffff;">
      <th style="padding:10px 12px; text-align:left; font-weight:700;">Parameter</th>
      <th style="padding:10px 12px; text-align:left; font-weight:700;">Single Dose</th>
      <th style="padding:10px 12px; text-align:left; font-weight:700;">Two Dose</th>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 12px; font-weight:700;">Dosing</td>
      <td style="padding:8px 12px;">One dose; repeat if necessary</td>
      <td style="padding:8px 12px;">Days 0 and 4</td>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 12px; font-weight:700;">Medication Dosage</td>
      <td style="padding:8px 12px;">50 mg/m&sup2; BSA on day-1</td>
      <td style="padding:8px 12px;">50 mg/m&sup2; BSA per dose</td>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 12px; font-weight:700;">Serum &beta;-hCG level</td>
      <td style="padding:8px 12px;">Days 0, 4, and 7</td>
      <td style="padding:8px 12px;">Days 0, 4, 7. Days 11 and 14 if repeat dose given</td>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 12px; font-weight:700;">Indication for additional dose</td>
      <td style="padding:8px 12px;">If &beta;-hCG does not decline by 15% from day 4 to day 7</td>
      <td style="padding:8px 12px;">If &lt;15% decline from day 4 to 7 OR day 7 to 11</td>
    </tr>
    <tr>
      <td style="padding:8px 12px; font-weight:700;">Post-therapy surveillance</td>
      <td style="padding:8px 12px;">Weekly until &beta;-hCG undetectable</td>
      <td style="padding:8px 12px;">Weekly until &beta;-hCG undetectable</td>
    </tr>
  </table>
  <div style="background:rgba(233,196,106,0.15); border-radius:8px; padding:10px 16px; margin-top:12px;">
    <p style="font-size:13px; color:#264653; margin:0;"><strong>Key monitoring:</strong> &ge;15% decline in &beta;-hCG between measured timepoints indicates treatment response.</p>
  </div>
</div>
''')

# ----- Surgical Treatment Indications -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Surgical Treatment &mdash; Indications</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#e76f51; border-radius:8px; padding:20px 24px; color:#ffffff;">
    <p style="font-size:18px; font-weight:700; margin:0 0 10px 0;">Indications for Surgery</p>
    <ul style="font-size:16px; margin:0; padding-left:20px; line-height:1.8;">
      <li><strong>Significant pain</strong>.</li>
      <li>Ectopic pregnancy with adnexal mass <strong>&gt; 3.5 cm</strong> or with visible fetal cardiac pulsations.</li>
      <li>&beta;-hCG <strong>&gt; 5000 IU/L</strong>.</li>
    </ul>
  </div>
</div>
''')

# ----- Salpingostomy vs Salpingectomy -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Surgical Options</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
    <p style="font-size:20px; color:#264653; font-weight:700; margin:0 0 8px 0;">Salpingostomy</p>
    <p style="font-size:15px; color:#264653; margin:0 0 8px 0;">Removal of the gestational sac through <strong>linear tubal incision</strong>.</p>
    <p style="font-size:15px; color:#264653; font-weight:700; margin:0 0 4px 0;">Indications:</p>
    <p style="font-size:15px; color:#264653; margin:0;">When future fertility is required.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e76f51;">
    <p style="font-size:20px; color:#264653; font-weight:700; margin:0 0 8px 0;">Salpingectomy</p>
    <p style="font-size:15px; color:#264653; margin:0 0 8px 0;">Removal of the tube containing ectopic pregnancy.</p>
    <p style="font-size:15px; color:#264653; font-weight:700; margin:0 0 4px 0;">Indications:</p>
    <ul style="font-size:14px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
      <li>&gt; 40 years</li>
      <li>Completed her family</li>
      <li>Uncontrolled bleeding during salpingostomy</li>
    </ul>
  </div>
</div>
<div style="position:absolute; bottom:30px; left:60px; right:60px;">
  <p style="font-size:13px; color:#666; margin:0;">Both procedures can be performed by <strong>laparotomy</strong> or <strong>laparoscopy</strong>.</p>
</div>
''')

# ----- Interstitial (Cornual) Pregnancy -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Interstitial (Cornual) Pregnancy</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
      <li>Implantation in the proximal tubal segment that lies <strong>within the muscular uterine wall</strong>.</li>
      <li>Swelling <strong>lateral to the insertion of the round ligament</strong> is the characteristic anatomic finding.</li>
      <li>Because of the proximity to the uterine and ovarian arteries, there is a risk of <strong>severe hemorrhage</strong>.</li>
      <li>Surgical management involves <strong>cornual resection</strong> either by laparotomy or laparoscopy.</li>
      <li>The risk of <strong>uterine rupture</strong> with subsequent pregnancies is high. Careful observation and consideration of elective cesarean delivery is warranted.</li>
    </ul>
  </div>
</div>
''')

# ----- Ovarian Ectopic -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Ovarian Ectopic Pregnancy</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.6;">Clinical picture is the same as tubal ectopic.</p>
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:16px 0 10px 0;">Spiegelberg Criteria</p>
    <ol style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>The pregnancy occupies the site of the ovary and cannot be separated from it &amp; surrounded by healthy ovarian tissues.</li>
      <li>The gestational sac is connected to the uterus by <strong>ovarian ligament</strong>.</li>
      <li>No adhesion between the tube and the ovary.</li>
      <li>Fallopian tube on the affected side is healthy &amp; the mesosalpinx is free from hemorrhage or masses.</li>
    </ol>
    <p style="font-size:16px; color:#e76f51; font-weight:700; margin:12px 0 0 0;">Treatment: Oophorectomy.</p>
  </div>
</div>
''')

# ----- Cervical EP -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Cervical Ectopic Pregnancy</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Diagnostic Criteria</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>The presence of <strong>cervical glands opposite</strong> the placental attachment site.</li>
      <li>A portion of or the entire placenta must be located <strong>below the entrance of the uterine vessels</strong>.</li>
    </ul>
    <p style="font-size:16px; color:#264653; margin:12px 0 0 0; line-height:1.5;">Early diagnosis is important to avoid <strong>severe hemorrhage</strong> and subsequent hysterectomy.</p>
    <p style="font-size:16px; color:#264653; font-weight:700; margin:10px 0 0 0;">Treatment:</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.6;">
      <li>Medically by <strong>methotrexate</strong></li>
      <li>Cervical evacuation and packing</li>
      <li>In severe bleeding: <strong>hysterectomy</strong></li>
    </ul>
  </div>
</div>
''')

# ----- Cesarean Scar Pregnancy -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:30px; left:60px;">
  <p style="font-size:32px; color:#264653; font-weight:700; margin:0;">Cesarean Section Scar Pregnancy</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:90px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.5;">Implantation of the pregnancy sac within the scar of a previous cesarean delivery. It can cause serious maternal morbidity and mortality from <strong>massive hemorrhage</strong>.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:12px;">
    <p style="font-size:17px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Four Sonographic Criteria:</p>
    <ol style="font-size:14px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
      <li>An <strong>empty uterine cavity</strong>.</li>
      <li>An <strong>empty cervical canal</strong>.</li>
      <li>A gestational sac in the <strong>anterior part of the uterine isthmus</strong>.</li>
      <li><strong>Absence of healthy myometrium</strong> between the bladder and gestational sac.</li>
    </ol>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:12px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:12px;">
    <p style="font-size:14px; color:#264653; margin:0; line-height:1.5;">Imaging with <strong>3D color Doppler</strong> or <strong>MRI</strong> can aid in evaluation. Treatment: methotrexate, or resection by laparoscopy or laparotomy.</p>
  </div>
</div>
''')

# ----- Heterotopic & PUL -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:30px; left:60px;">
  <p style="font-size:32px; color:#264653; font-weight:700; margin:0;">Heterotopic &amp; Unknown Location</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:90px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
    <p style="font-size:18px; color:#264653; font-weight:700; margin:0 0 8px 0;">Heterotopic Pregnancy</p>
    <ul style="font-size:14px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
      <li>Presence of a <strong>uterine pregnancy</strong> with an <strong>extrauterine pregnancy</strong>.</li>
      <li>When a tubal pregnancy coexists with a uterine pregnancy, <strong>potassium chloride</strong> can be injected into the tubal pregnancy sac.</li>
      <li><strong>Methotrexate is contraindicated</strong> due to detrimental effects on the normal pregnancy.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e9c46a;">
    <p style="font-size:18px; color:#264653; font-weight:700; margin:0 0 8px 0;">Pregnancy of Unknown Location (PUL)</p>
    <p style="font-size:14px; color:#264653; margin:0; line-height:1.6;">A condition in which there is a <strong>positive pregnancy test</strong> and absent intrauterine gestational sac without any evidence of extrauterine pregnancy. This term is used till a final diagnosis is made, either an abnormal or normal intrauterine pregnancy or ectopic.</p>
  </div>
</div>
''')

# ----- EP Student Activity & Questions -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Student Activity &amp; Questions</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Student Activity</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Each student is requested to navigate the web in order to provide online three ultrasonographic pictures of three ectopic pregnancies to be shown to his (her) tutor in bedside teaching part of the clinical round.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Questions</p>
    <p style="font-size:16px; color:#264653; margin:0;">Online form: <span style="color:#2a9d8f;">https://forms.gle/J1rMkBL6Jx9kjfyg8</span></p>
  </div>
</div>
''')

print("=== SECTION 3: GESTATIONAL TROPHOBLASTIC DISEASE ===")

# ----- Section Divider: GTD -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, #264653 0%, #1a3a3f 100%);"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="8" height="540" fill="#e9c46a"/>
  </svg>
</div>
<div style="position:absolute; top:140px; left:80px;">
  <p style="font-size:28px; color:#e9c46a; font-weight:400; margin:0;">Chapter 23</p>
  <p style="font-size:48px; color:#ffffff; font-weight:700; margin:16px 0 0 0; line-height:1.1;">Gestational<br>Trophoblastic Disease</p>
  <p style="font-size:18px; color:rgba(255,255,255,0.65); margin:24px 0 0 0;">Tumors arising from the trophoblastic cells of the placenta</p>
</div>
''')

# ----- GTD ILOs & Definition -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">ILOs &amp; Definition</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Intended Learning Outcomes</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.7;">
      <li>Understand the pathogenesis of molar pregnancy.</li>
      <li>Describe the clinical picture of GTD.</li>
      <li>Outline the management of this pregnancy associated disorder.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0;">Tumors arising from the <strong>trophoblastic cells</strong> of the placenta.</p>
  </div>
</div>
''')

# ----- GTD Classification -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Classification of GTD</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:20px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
    <p style="font-size:20px; color:#264653; font-weight:700; margin:0 0 10px 0;">A. Benign</p>
    <p style="font-size:16px; color:#264653; font-weight:600; margin:0 0 4px 0;">Hydatidiform Mole</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
      <li>Complete hydatidiform mole</li>
      <li>Partial hydatidiform mole</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e76f51;">
    <p style="font-size:20px; color:#264653; font-weight:700; margin:0 0 10px 0;">B. Malignant (GTT)</p>
    <p style="font-size:16px; color:#264653; font-weight:600; margin:0 0 4px 0;">Gestational Trophoblastic Tumor</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.6;">
      <li>Invasive mole</li>
      <li>Choriocarcinoma</li>
      <li>Placental site trophoblastic tumor</li>
    </ul>
  </div>
</div>
<div style="position:absolute; bottom:20px; left:60px; right:60px;">
  <div style="background:rgba(42,157,143,0.08); border-radius:6px; padding:8px 16px;">
    <p style="font-size:13px; color:#666; margin:0;"><strong>Spectrum:</strong> Complete mole &rarr; Partial mole &rarr; Coexistent mole &amp; fetus &rarr; Invasive mole &rarr; Choriocarcinoma &rarr; Placental site trophoblastic tumor</p>
  </div>
</div>
''')

# ----- Hydatidiform Mole Definition & Incidence -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Hydatidiform Mole &mdash; Overview</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Definition</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">It is a benign tumor of trophoblastic tissue in which <strong>hydropic degeneration of the chorionic villi</strong> occurs.</p>
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:16px 0 8px 0;">Incidence</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
      <div style="background:rgba(42,157,143,0.08); border-radius:6px; padding:10px 16px; text-align:center;">
        <p style="font-size:20px; color:#e76f51; font-weight:700; margin:0;">1 / 1000</p>
        <p style="font-size:14px; color:#264653; margin:0;">Complete mole</p>
      </div>
      <div style="background:rgba(42,157,143,0.08); border-radius:6px; padding:10px 16px; text-align:center;">
        <p style="font-size:20px; color:#e76f51; font-weight:700; margin:0;">3 / 1000</p>
        <p style="font-size:14px; color:#264653; margin:0;">Partial mole</p>
      </div>
    </div>
  </div>
</div>
''')

# ----- Complete vs Partial Mole -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:30px; left:60px;">
  <p style="font-size:32px; color:#264653; font-weight:700; margin:0;">Complete vs Partial Mole</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:90px; left:60px; right:60px;">
  <table style="width:100%; border-collapse:collapse; font-size:14px; background:#ffffff; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-radius:8px; overflow:hidden;">
    <tr style="background:#264653; color:#ffffff;">
      <th style="padding:10px 14px; text-align:left;">Feature</th>
      <th style="padding:10px 14px; text-align:left;">Complete Mole</th>
      <th style="padding:10px 14px; text-align:left;">Partial Mole</th>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 14px; font-weight:700;">Uterine Content</td>
      <td style="padding:8px 14px;">Full of vesicles. No embryo.</td>
      <td style="padding:8px 14px;">Part of tissue shows molar changes. Fetus or parts present.</td>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 14px; font-weight:700;">Genetics</td>
      <td style="padding:8px 14px;">Anucleated ovum + sperm &rarr; duplicate &rarr; 46 chromosomes (all paternal)</td>
      <td style="padding:8px 14px;">Ovum + 2 sperms &rarr; 69 chromosomes (triploid)</td>
    </tr>
    <tr style="border-bottom:1px solid #e9ecef;">
      <td style="padding:8px 14px; font-weight:700;">Karyotype</td>
      <td style="padding:8px 14px;">46,XX or 46,XY</td>
      <td style="padding:8px 14px;">69,XXX or 69,XXY</td>
    </tr>
    <tr>
      <td style="padding:8px 14px; font-weight:700;">Malignant Transformation</td>
      <td style="padding:8px 14px;">16%</td>
      <td style="padding:8px 14px;">0.5%</td>
    </tr>
  </table>
</div>
<div style="position:absolute; bottom:20px; left:60px; right:60px;">
  <div style="background:rgba(42,157,143,0.08); border-radius:6px; padding:8px 16px;">
    <p style="font-size:13px; color:#264653; margin:0;"><strong>Complete mole pathogenesis:</strong> Empty egg (no chromosomes) fertilized by 1 sperm &rarr; chromosome duplication &rarr; 46XX/46XY all paternal. <strong>Partial mole:</strong> Normal egg fertilized by 2 sperm (dispermy) &rarr; 69XXX/69XXY triploid.</p>
  </div>
</div>
''')

# ----- Risk Factors -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Risk Factors</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:17px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">(1) Age</p>
      <p style="font-size:15px; color:#264653; margin:0; line-height:1.5;">The most consistent risk factor. Pregnancies below 16 years and above 45 years have the highest risk.</p>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:17px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">(2) Previous GTN</p>
      <p style="font-size:15px; color:#264653; margin:0; line-height:1.5;">After one mole: &lt;2% risk. After two moles: 16%. After three moles: 50%.</p>
    </div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px;">
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:17px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">(3) Family History</p>
      <p style="font-size:15px; color:#264653; margin:0;">Positive family history increases risk.</p>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:17px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">(4) Dietary &amp; Ethnic</p>
      <p style="font-size:15px; color:#264653; margin:0;">Low animal fat intake may be associated with increased risk. More common in Asian populations.</p>
    </div>
  </div>
</div>
''')

# ----- Pathology -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Pathology</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:16px; color:#264653; line-height:1.6; margin:0;">
      The uterus is full of thin-walled, translucent, grape-like vesicles of different sizes.
    </p>
    <p style="font-size:16px; color:#264653; line-height:1.6; margin:12px 0 0 0;">
      <strong>Trophoblastic proliferation</strong> with mitotic activity affecting both syncytial and cytotrophoblastic layers leads to excessive secretion of:
    </p>
    <ul style="font-size:15px; color:#264653; margin:8px 0 0 0; padding-left:20px; line-height:1.7;">
      <li><strong>hCG</strong> (human chorionic gonadotropin)</li>
      <li><strong>Chorionic thyrotrophin</strong></li>
      <li><strong>Progesterone</strong></li>
    </ul>
    <p style="font-size:16px; color:#264653; line-height:1.5; margin:12px 0 0 0;">
      Ovaries: The high hCG leads to <strong>multiple theca lutein cysts</strong>.
    </p>
    <p style="font-size:16px; color:#264653; line-height:1.5; margin:6px 0 0 0;">
      The high hCG leads to exaggeration of early pregnancy symptoms and signs.
    </p>
  </div>
</div>
''')

# ----- Clinical Features -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Clinical Features</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
    <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Symptoms</p>
      <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
        <li><strong>Amenorrhea</strong></li>
        <li><strong>Vaginal bleeding</strong></li>
        <li>Symptoms of pregnancy in <strong>exaggerated form</strong></li>
        <li><strong>Early onset pre-eclampsia</strong> before 20th weeks</li>
        <li><strong>Hyperemesis gravidarum</strong></li>
        <li><strong>Hyperthyroidism</strong></li>
      </ul>
    </div>
    <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
      <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Complications</p>
      <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
        <li>Complications of <strong>theca lutein cyst</strong> of ovary (rupture, torsion)</li>
      </ul>
    </div>
  </div>
</div>
''')

# ----- Examinations -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Examinations</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Abdominal Examination</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
      <li>Uterus is <strong>large</strong> and its consistency is <strong>soft and doughy</strong>.</li>
      <li>No fetal part or fetal heart can be detected.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Pelvic Examination</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
      <li>Sometimes <strong>grape-like vesicles</strong> of mole may be detected which confirm the diagnosis.</li>
    </ul>
  </div>
</div>
''')

# ----- Investigations -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Investigations</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">A) Ultrasound</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
      <li><strong>Snow storm appearance</strong>: uterine cavity filled with multiple sonolucent areas of varying size and shape.</li>
      <li><strong>Absence of fetus</strong>.</li>
      <li><strong>Theca lutein cyst</strong> of ovary.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">B) &beta;-hCG</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
      <li>Is <strong>highly elevated</strong> (&gt; 100,000 mIU/ml).</li>
    </ul>
  </div>
</div>
<div style="position:absolute; bottom:30px; left:60px; right:60px;">
  <div style="background:rgba(42,157,143,0.08); border-radius:6px; padding:8px 16px;">
    <p style="font-size:13px; color:#666; margin:0;">Transvaginal ultrasound shows a classic "snowstorm" pattern: multiple cystic spaces (hydropic villi) without identifiable fetal parts.</p>
  </div>
</div>
''')

# ----- Treatment -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:30px; left:60px;">
  <p style="font-size:32px; color:#264653; font-weight:700; margin:0;">Treatment</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:90px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:17px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Evacuation</p>
    <p style="font-size:15px; color:#264653; margin:0; line-height:1.5;">Suction curettage is performed under <strong>general anesthesia</strong> with <strong>available blood</strong>.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:12px;">
    <p style="font-size:17px; color:#e76f51; font-weight:700; margin:0 0 8px 0;">Indications for Hysterectomy</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.6;">
      <li>Older women or those of high parity.</li>
      <li>Severe uncontrolled hemorrhage.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:16px 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:12px;">
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:20px; line-height:1.6;">
      <li>Theca lutein cysts regress in size and need <strong>no special treatment</strong>, unless complicated (rupture, torsion).</li>
      <li><strong>Histopathological examination</strong> of evacuated tissue.</li>
      <li><strong>Anti D</strong> should be given to non-sensitized Rh negative mother.</li>
    </ul>
  </div>
</div>
''')

# ----- Postmolar Follow Up -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Postmolar Follow Up</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <ul style="font-size:16px; color:#264653; margin:0; padding-left:20px; line-height:1.8;">
      <li><strong>hCG measurement</strong> every 1 to 2 weeks until it becomes negative.</li>
      <li><strong>Monthly for 1 year</strong> after hCG becomes negative is recommended for all patients with molar gestation.</li>
    </ul>
    <div style="background:rgba(231,111,81,0.1); border-radius:6px; padding:12px 16px; border-left:4px solid #e76f51; margin-top:12px;">
      <p style="font-size:15px; color:#264653; margin:0;"><strong>Aim:</strong> To detect any changes suggestive of malignancy because <strong>16%</strong> of complete hydatidiform mole and <strong>0.5%</strong> of partial hydatidiform mole undergo malignant transformation.</p>
    </div>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 8px 0;">Contraception</p>
    <p style="font-size:16px; color:#264653; margin:0;">The <strong>combined oral pills</strong> is the method of choice.</p>
  </div>
</div>
''')

# ----- Chemotherapy Indications & Subsequent Pregnancy -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Chemotherapy &amp; Subsequent Pregnancy</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px; display:grid; grid-template-columns:1fr 1fr; gap:16px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #e76f51;">
    <p style="font-size:18px; color:#264653; font-weight:700; margin:0 0 10px 0;">Chemotherapy Indications</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
      <li>hCG titer <strong>rises or plateaus</strong> during follow up.</li>
      <li>Evidence of <strong>choriocarcinoma</strong>.</li>
      <li><strong>Persistent uterine bleeding</strong> and positive hCG.</li>
    </ul>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); border-top:4px solid #2a9d8f;">
    <p style="font-size:18px; color:#264653; font-weight:700; margin:0 0 10px 0;">Subsequent Pregnancy</p>
    <ul style="font-size:15px; color:#264653; margin:0; padding-left:18px; line-height:1.7;">
      <li>An early <strong>ultrasound</strong> should be performed in all subsequent pregnancies because of the <strong>1&ndash;2% risk of recurrence</strong>.</li>
    </ul>
  </div>
</div>
''')

# ----- GTD Student Activity & Questions -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#fdf0d5;"></div>
<div style="position:absolute; top:36px; left:60px;">
  <p style="font-size:36px; color:#264653; font-weight:700; margin:0;">Student Activity &amp; Questions</p>
  <div style="width:80px; height:4px; background:#2a9d8f; margin-top:10px;"></div>
</div>
<div style="position:absolute; top:110px; left:60px; right:60px;">
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Student Activity</p>
    <p style="font-size:16px; color:#264653; margin:0; line-height:1.5;">Each group of students is requested to search for a case report on gestational trophoblastic disease across the web to be discussed at bedside teaching part of the clinical round.</p>
  </div>
  <div style="background:#ffffff; border-radius:8px; padding:20px 24px; box-shadow:0 2px 8px rgba(0,0,0,0.08); margin-top:16px;">
    <p style="font-size:18px; color:#2a9d8f; font-weight:700; margin:0 0 10px 0;">Questions</p>
    <p style="font-size:16px; color:#264653; margin:0;">Online form: <span style="color:#2a9d8f;">https://forms.gle/nugdnS5mJuhcrKvA7</span></p>
  </div>
</div>
''')

# ----- Summary Slide -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:linear-gradient(135deg, #264653 0%, #2a9d8f 100%);"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <circle cx="800" cy="80" r="180" fill="rgba(233,196,106,0.08)"/>
    <circle cx="120" cy="460" r="140" fill="rgba(244,162,97,0.08)"/>
  </svg>
</div>
<div style="position:absolute; top:60px; left:70px;">
  <p style="font-size:44px; color:#ffffff; font-weight:700; margin:0;">Summary</p>
  <div style="width:80px; height:4px; background:#e9c46a; margin-top:12px;"></div>
</div>
<div style="position:absolute; top:150px; left:70px; right:70px; display:grid; grid-template-columns:1fr; gap:12px;">
  <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:14px 20px;">
    <p style="font-size:17px; color:#ffffff; font-weight:700; margin:0 0 4px 0;">1. Abortion</p>
    <p style="font-size:14px; color:rgba(255,255,255,0.8); margin:0; line-height:1.4;">Termination before 20 weeks. Types: Threatened, Inevitable, Complete, Incomplete, Cervical, Missed, Septic. Recurrent abortion requires genetic, anatomical, and immunological workup.</p>
  </div>
  <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:14px 20px;">
    <p style="font-size:17px; color:#ffffff; font-weight:700; margin:0 0 4px 0;">2. Ectopic Pregnancy</p>
    <p style="font-size:14px; color:rgba(255,255,255,0.8); margin:0; line-height:1.4;">Implantation outside uterine cavity. 99% tubal. Diagnosis via &beta;-hCG, ultrasound, discriminatory zone. Treatment: Expectant, Methotrexate, or Surgery (salpingostomy/salpingectomy).</p>
  </div>
  <div style="background:rgba(255,255,255,0.12); border-radius:8px; padding:14px 20px;">
    <p style="font-size:17px; color:#ffffff; font-weight:700; margin:0 0 4px 0;">3. Gestational Trophoblastic Disease</p>
    <p style="font-size:14px; color:rgba(255,255,255,0.8); margin:0; line-height:1.4;">Tumors from trophoblastic cells. Complete mole (46,XX all paternal) vs Partial mole (69,XXY triploid). Diagnosed by snow-storm U/S and high hCG. Treated by suction evacuation with postmolar hCG follow-up.</p>
  </div>
</div>
''')

# ----- Closing Slide -----
n += 1
write_slide(n, '''
<div style="position:absolute; top:0; left:0; width:960px; height:540px; background:#264653;"></div>
<div style="position:absolute; top:0; left:0; width:960px; height:540px;">
  <svg width="960" height="540" xmlns="http://www.w3.org/2000/svg">
    <circle cx="480" cy="270" r="220" fill="rgba(42,157,143,0.15)"/>
    <line x1="380" y1="210" x2="580" y2="210" stroke="#e9c46a" stroke-width="3"/>
  </svg>
</div>
<div style="position:absolute; top:160px; left:0; width:960px; text-align:center;">
  <p style="font-size:52px; color:#e9c46a; font-weight:700; margin:0;">Thank You</p>
  <p style="font-size:20px; color:rgba(255,255,255,0.7); margin:20px 0 0 0;">Early Pregnancy Complications &mdash; Complete Module</p>
  <p style="font-size:16px; color:rgba(255,255,255,0.4); margin:40px 0 0 0;">Obstetrics &amp; Gynecology</p>
</div>
''')

print(f"\nDone! Total slides generated: {n}")
