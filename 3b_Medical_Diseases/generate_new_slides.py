#!/usr/bin/env python3
"""
Generate slides for Hypertension, Diabetes Mellitus, and UTI with Pregnancy.
Appends to existing 44-slide presentation. Updates cover, TOC, and summary.
"""

import os

SLIDES_DIR = "/media/mohamed/projects4/projects/obstaric/raw material/3_Medical_Obstetric_Disorders/3b_Medical_Diseases/slides"

C = {
    "dark": "#264653",
    "teal": "#2a9d8f",
    "gold": "#e9c46a",
    "orange": "#f4a261",
    "coral": "#e76f51",
    "bg": "#edf6f9",
    "white": "#ffffff",
}

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
    return f'''<svg style="position:absolute;right:32px;bottom:24px;width:48px;height:32px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="48" height="28" rx="6" fill="{C["teal"]}" />
  <text x="24" y="20" text-anchor="middle" font-family="Times New Roman,serif" font-size="16" font-weight="700" fill="{C["white"]}">{num:02d}</text>
</svg>'''

def slide_wrap(body, page_num=None):
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

def two_col_card(left_title, left_items, right_title, right_items, left_color=C["teal"], right_color=C["coral"]):
    def build_card(title, items, color):
        html = f'<div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {color};height:fit-content;">'
        html += f'<p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:\'Times New Roman\',serif;margin:0 0 6px 0;">{title}</p>'
        html += f'<ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:\'Times New Roman\',serif;line-height:1.5;">'
        for item in items:
            html += f'<li>{item}</li>'
        html += '</ul></div>'
        return html
    return f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  {build_card(left_title, left_items, left_color)}
  {build_card(right_title, right_items, right_color)}
</div>'''

def single_card(title, items, color=C["teal"], border_pos="left"):
    border = f"border-left:4px solid {color}"
    html = f'<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;{border};margin-bottom:10px;">'
    html += f'<p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:\'Times New Roman\',serif;margin:0 0 6px 0;">{title}</p>'
    html += f'<ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:\'Times New Roman\',serif;line-height:1.5;">'
    for item in items:
        html += f'<li>{item}</li>'
    html += '</ul></div>'
    return html

def simple_card(title, content, color=C["teal"]):
    return f'<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {color};margin-bottom:10px;"><p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:\'Times New Roman\',serif;margin:0 0 6px 0;">{title}</p><p style="font-size:13px;color:{C["dark"]};font-family:\'Times New Roman\',serif;line-height:1.35;margin:0;">{content}</p></div>'

def icon_bullet(text, color=C["dark"], size="13px"):
    return f'''<div style="display:flex;align-items:flex-start;gap:6px;margin-bottom:3px;">
  <span style="color:{C["teal"]};font-size:9px;margin-top:4px;">●</span>
  <span style="color:{color};font-size:{size};font-weight:400;font-family:\'Times New Roman\',serif;line-height:1.3;">{text}</span>
</div>'''


# ════════════════════════════════════════════════════════════
# SECTION 5: HYPERTENSION WITH PREGNANCY
# ════════════════════════════════════════════════════════════

new_slides = []

# Slide 45: Section Divider
new_slides.append(("slide-45.html", slide_wrap(section_divider("05", "Hypertension with Pregnancy", "Preeclampsia, Eclampsia & Chronic Hypertension"), 45)))

# Slide 46: ILOs, Definition, Incidence, Classification
htn_ilo = content_slide("Hypertension with Pregnancy — ILOs & Classification", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">ILOs</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Understand definition of hypertension of pregnancy</li>
      <li>Classify hypertensive disorders of pregnancy</li>
      <li>Outline risk factors of preeclampsia</li>
      <li>Explain clinical management of preeclampsia</li>
      <li>Describe management of gestational & chronic hypertension</li>
      <li>Describe clinical management of eclampsia</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Definition & Incidence</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 8px 0;">
      <b>Definition:</b> SBP ≥140 mmHg or DBP ≥90 mmHg on two occasions at least 6 hours apart during pregnancy.
    </p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 8px 0;">
      <b>Incidence:</b> 10–20% of all pregnancies. Second leading cause of maternal death & perinatal morbidity/mortality after severe bleeding.
    </p>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Classification (4 categories)</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Chronic hypertension (diagnosed before 20th week)</li>
      <li>Gestational hypertension</li>
      <li>Chronic hypertension + superimposed preeclampsia</li>
      <li>Preeclampsia</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-46.html", slide_wrap(htn_ilo, 46)))

# Slide 47: Chronic HTN
htn_chronic = content_slide("Chronic (Pre-existing) Hypertension", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Definition</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
      BP ≥140/90 mmHg diagnosed before pregnancy or develops before 20 weeks of gestation or persists &gt;42 days postpartum.
    </p>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Causes</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Chronic kidney disease</li>
      <li>Primary aldosteronism</li>
      <li>Pheochromocytoma</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Management</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Mild Chronic HTN:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Serial antenatal screening</li>
      <li>Serial BP measurement</li>
      <li>Serial urine protein assessment</li>
      <li>Termination at term by IOL if cervix favorable</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">Severe Chronic HTN:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Start antihypertensives: α-methyldopa, labetalol, or CCBs to maintain BP &lt;160/100</li>
      <li>Serial BP & urine protein assessment</li>
      <li>Delivery at 37 wks</li>
      <li>If delivery before 34 wks → steroids for fetal lung maturity</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-47.html", slide_wrap(htn_chronic, 47)))

# Slide 48: Superimposed Preeclampsia & Gestational HTN
htn_super = content_slide("Superimposed Preeclampsia & Gestational Hypertension", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Chronic HTN + Superimposed Preeclampsia</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Pre-existing hypertension with further worsening of BP after 20 weeks, followed by proteinuria (≥3 g/24h).
    </p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 0 0;">Management:</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Same as preeclampsia.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Gestational Hypertension</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Definition:</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Pregnancy-induced hypertension after 20 weeks with absence of proteinuria.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Diagnosis:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>No symptoms of preeclampsia</li>
      <li>Lab tests normal</li>
      <li>Proteinuria absent</li>
      <li>Key finding: sustained BP elevation</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">Management:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Conservative outpatient management</li>
      <li>Serial lab testing to rule out preeclampsia</li>
      <li>Antihypertensives only if BP &gt;160/100</li>
      <li>Delivery at term (vaginal if cervix favorable, otherwise CS)</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-48.html", slide_wrap(htn_super, 48)))

# Slide 49: Preeclampsia - Definition, Incidence, Risk Factors, Etiology
pe_def = content_slide("Preeclampsia — Definition, Risk Factors & Etiology", f'''
<div style="display:grid;grid-template-columns:2fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Definition</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
      Hypertension ≥140/90 mmHg on two occasions at least 4 hours apart <b>+</b> proteinuria ≥300 mg in 24-hour urine after 20 weeks in a previously normotensive woman.
    </p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;"><b>Incidence:</b> 5–10% of pregnancies.</p>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 4px 0;">Risk Factors</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>More in primigravida</li>
      <li>Enlarged placenta (DM, multiple pregnancies, hydrops)</li>
      <li>Pre-existing hypertension or renal diseases</li>
      <li>Pre-existing vascular disease (DM, autoimmune vasculitis)</li>
      <li>Obesity</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Etiology</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 4px 0;">Disorder of unknown etiology peculiar to human pregnancy. Theories include:</p>
    <ul style="margin:0;padding-left:16px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Abnormal placentation</li>
      <li>Abnormal trophoblastic invasion</li>
      <li>Immunologic phenomena</li>
      <li>Renin-angiotensin system</li>
      <li>Coagulation abnormalities</li>
      <li>Abnormal cardiovascular adaptation</li>
      <li>Dietary factors</li>
      <li>Genetic factors</li>
      <li>Vasculopathy & inflammatory changes</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-49.html", slide_wrap(pe_def, 49)))

# Slide 50: Preeclampsia - Pathology
pe_path = content_slide("Preeclampsia — Pathology", f'''
<div style="background:{C["bg"]};padding:8px 14px;border-radius:8px;border-left:4px solid {C["coral"]};margin-bottom:10px;">
  <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Core Pathology</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    <b>Vasospasm</b> and <b>hemoconcentration</b> are the main pathology — accounts for hypertension. Leads to vascular changes and local hypoxia → hemorrhage, necrosis and other pathological changes.
  </p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 10px;">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">1. CNS</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Ischemia, hemorrhages, edema.</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:8px 10px;">
    <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">2. Liver</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Subcapsular hemorrhage, periportal necrosis, infarctions.</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["gold"]};border-radius:8px;padding:8px 10px;">
    <p style="font-size:14px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">3. Kidney</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">↓ Renal blood flow → glomerular damage (glomerular endotheliosis) → ↓ GFR by ~50%, proteinuria (albuminuria).</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["orange"]};border-radius:8px;padding:8px 10px;">
    <p style="font-size:14px;font-weight:700;color:{C["orange"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">4. Heart & Lungs</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Myocardial & endocardial hemorrhage/necrosis. Lungs: hemorrhage, secondary bronchopneumonia.</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:8px 10px;">
    <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">5. Retina</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Hemorrhage, exudate, rarely retinal detachment (severe).</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 10px;">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">6. Coagulation</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">↑ Fibrin production, ↓ fibrinolytic activity, ↑ Factor VII/VIII, ↑ FDP, thrombocytopenia.</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["gold"]};border-radius:8px;padding:8px 10px;grid-column:1/3;">
    <p style="font-size:14px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">7. Endocrine Glands</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Necrosis and hemorrhage in pituitary, pancreas, and adrenal glands.</p>
  </div>
</div>
''')
new_slides.append(("slide-50.html", slide_wrap(pe_path, 50)))

# Slide 51: Diagnostic Criteria
pe_dx = content_slide("Preeclampsia — Diagnostic Criteria", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Signs</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Hypertension:</b> BP ≥140/90 after 20 weeks in previously normotensive woman</li>
      <li><b>Proteinuria:</b> Urinary protein &gt;0.3 g/L in 24h or spot protein/creatinine ratio ≥0.3</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">Symptoms</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Headache and blurred vision</li>
      <li>Epigastric or right upper quadrant pain</li>
      <li>Nausea and vomiting</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Investigations</p>
    <ol style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Complete urine examination (proteinuria)</li>
      <li>Kidney function tests</li>
      <li>Liver function tests</li>
      <li>Coagulation status: Platelets, fibrinogen, FDP (DIC may develop)</li>
      <li>Fundus examination</li>
      <li><b>Fetal assessment:</b>
        <ul style="margin:2px 0 0 16px;font-size:12px;">
          <li>Daily fetal movement (kick counts)</li>
          <li>NST twice weekly</li>
          <li>Biophysical profile if nonreactive NST</li>
          <li>Amniotic fluid volume weekly</li>
          <li>U/S fetal growth every 3 weeks</li>
        </ul>
      </li>
    </ol>
  </div>
</div>
''')
new_slides.append(("slide-51.html", slide_wrap(pe_dx, 51)))

# Slide 52: Screening & Types
pe_screen = content_slide("Preeclampsia — Screening & Types", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Screening for Preeclampsia</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Mid-trimester mean BP:</b> If &gt;90 mmHg → increased risk of PE</li>
      <li><b>Urinary assay</b> for microalbuminuria</li>
      <li><b>Blood urate:</b> Serial increase is a warning sign</li>
      <li><b>Doppler velocimetry:</b> Detects uteroplacental hypoperfusion</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Types of Preeclampsia</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Preeclampsia:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">BP &lt;160/110, absence of symptoms, normal lab data.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Preeclampsia with Severe Features (ACOG 2013):</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0;">
      BP ≥160/110 on two occasions at least 6 hours apart with any of:
    </p>
    <ul style="margin:2px 0 0 16px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>↑ Liver enzymes, hepatic hemorrhage & rupture</li>
      <li>↑ Creatinine, ATN, renal failure</li>
      <li>HELLP syndrome</li>
      <li>IUGR, oligohydramnios, IUFD, placental abruption</li>
      <li>Symptoms: headache, blurring vision, epigastric/RUQ pain, N/V</li>
      <li>Oliguria (&lt;500 mL/24h)</li>
      <li>Pulmonary edema/cyanosis</li>
      <li>Thrombocytopenia (&lt;100,000/µL)</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-52.html", slide_wrap(pe_screen, 52)))

# Slide 53: Complications
pe_comp = content_slide("Preeclampsia — Complications", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:16px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Maternal Effects</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Accidental hemorrhage</li>
      <li>Acute renal failure</li>
      <li>HELLP syndrome (hemolysis, elevated liver enzymes, low platelet count)</li>
      <li>Acute pulmonary edema &amp; heart failure</li>
      <li>Antepartum eclampsia</li>
      <li>DIC</li>
      <li>Cerebrovascular accidents</li>
      <li>Residual and recurrent hypertension</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:16px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Fetal Effects</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>IUGR:</b> Due to placental insufficiency from vasospasm</li>
      <li><b>IUFD</b></li>
    </ul>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 14px;margin-top:10px;">
  <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">HELLP Syndrome</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;line-height:1.35;">
    <b>H</b>emolysis — <b>EL</b>evated <b>L</b>iver enzymes — <b>L</b>ow <b>P</b>latelet count. A severe complication of preeclampsia.
  </p>
</div>
''')
new_slides.append(("slide-53.html", slide_wrap(pe_comp, 53)))

# Slide 54: Prophylactic Treatment
pe_proph = content_slide("Preeclampsia — Prophylactic Treatment", f'''
<div style="background:{C["bg"]};padding:12px 16px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:16px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Prophylactic Measures</p>
  <ol style="margin:0;padding-left:20px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
    <li><b>Proper antenatal care</b> — for early detection of high risk patients</li>
    <li><b>Low dose aspirin</b></li>
    <li><b>Calcium</b></li>
    <li><b>Antioxidants</b></li>
  </ol>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 16px;margin-top:12px;">
  <p style="font-size:16px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Curative Treatment — General Principles</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
    <b>Delivery remains the ultimate treatment.</b> When possible, vaginal delivery is preferred to avoid added physiologic stressors of CS. For CS, regional anesthesia preferred (less maternal risk); contraindicated if coagulopathy.
  </p>
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">1. General Measures</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Hospitalization for observation of maternal and fetal conditions.</p>
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">2. Medical Treatment</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
    <li><b>Antihypertensives:</b> α-methyldopa (Aldomet), CCBs (Nifedipine), Labetalol, Hydralazine</li>
    <li><b>Diuretics:</b> In heart failure and pulmonary edema</li>
  </ul>
</div>
''')
new_slides.append(("slide-54.html", slide_wrap(pe_proph, 54)))

# Slide 55: Obstetric Management & Antihypertensives
pe_obstet = content_slide("Preeclampsia — Obstetric Management & Antihypertensives", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">3. Obstetric Management</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Magnesium sulphate</b> to prevent convulsions: 4–6 g loading dose, then 1–2 g/hour continuous infusion</li>
      <li>Control maternal BP within safe range</li>
      <li>Induction of labor to initiate delivery</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">Timing of Delivery</p>
    <p style="font-size:13px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Preeclampsia:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>≥37 weeks → Delivery</li>
      <li>&lt;37 weeks → Expectant management (maternal & fetal monitoring)</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:4px 0 2px 0;">Preeclampsia with Severe Features:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>≥34 weeks → Delivery (after rapid maternal stabilization)</li>
      <li>&lt;34 weeks → Expectant management in tertiary care center if BP controlled, good fetal/maternal status. Delivery if maternal/fetal complication.</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Antihypertensives</p>
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Hydralazine</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">5–10 mg boluses q20–30min (max 20 mg).</p>
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Labetalol</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">20–40 mg boluses (max 220 mg). Then 200 mg orally q8h (max 600 mg q6h).</p>
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Nifedipine</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">10–20 mg orally q30min (max 50 mg). Then 10–20 mg q4–6h (max 120 mg/day).</p>
    <p style="font-size:12px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0;">
      Aim: DBP 90–100, SBP 140–150. Avoid hypotension → risk of decreased uteroplacental perfusion.
    </p>
  </div>
</div>
''')
new_slides.append(("slide-55.html", slide_wrap(pe_obstet, 55)))

# Slide 56: Delivery Algorithm
pe_delivery = content_slide("Preeclampsia — Delivery Protocol", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Tertiary Care Setting</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">In tertiary health care hospital with on-site blood banking, ICU & NICU services.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Severe PE diagnosed → initiate:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li><b>Medications:</b> MgSO₄ for 48 hours; antihypertensives (IV then oral)</li>
      <li><b>Observation:</b> Maternal (BP, urine protein, symptoms, weight); Fetal (kicks, NST, BPP, serial U/S for growth & AFV)</li>
    </ul>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["coral"]};border-radius:8px;padding:10px 12px;">
    <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Indications for Urgent Delivery</p>
    <p style="font-size:13px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Maternal:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>Symptoms</li>
      <li>Eclampsia (2%)</li>
      <li>HELLP (20%)</li>
      <li>Uncontrolled BP</li>
      <li>End organ damage (2–5%)</li>
      <li>APH (abruption)</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:4px 0 2px 0;">Fetal:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>Non-reassuring FHR tracing</li>
      <li>Persistent oligohydramnios</li>
      <li>FGR (40%)</li>
      <li>Reaching 34 weeks</li>
    </ul>
  </div>
</div>
<div style="background:{C["bg"]};padding:8px 14px;border-radius:8px;border-left:4px solid {C["gold"]};margin-top:8px;">
  <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Initiation of Delivery Process</p>
  <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
    <li>Vaginal delivery preferred unless obstetrically contraindicated</li>
    <li>Oxytocin infusion for IOL/augmentation may be given simultaneously with MgSO₄</li>
    <li>Total fluid intake limited to 80–100 mL/hour (1 mL/kg/hour)</li>
    <li>Continuous fetal monitoring throughout</li>
    <li>After delivery: close observation minimum 24 hours; MgSO₄ continued for 48 hours</li>
  </ul>
</div>
''')
new_slides.append(("slide-56.html", slide_wrap(pe_delivery, 56)))

# Slide 57: Eclampsia Definition & Clinical Features
ecl_def = content_slide("Eclampsia — Definition & Clinical Features", f'''
<div style="display:grid;grid-template-columns:1fr 2fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Definition</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Development of convulsions or coma unrelated to other cerebral conditions during pregnancy or postpartum in patients with signs/symptoms of preeclampsia.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Clinical Features — The 4 Stages of a Fit</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">The fit may follow stimuli (visual, auditory, touch). Each fit occurs in 4 stages without intervals:</p>
    <ol style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Premonitory stage:</b> Pupils dilated, eyes move side to side, muscular twitches in tongue, face & hands</li>
      <li><b>Tonic stage:</b> All voluntary muscles undergo tonic contraction → cyanosis (respiratory muscles), saliva accumulation, patient may arch back</li>
      <li><b>Clonic stage:</b> Irregular intermittent contractions & relaxation of voluntary muscles. Tongue may be bitten. Involuntary passage of urine/stools</li>
      <li><b>Coma stage:</b> Lasts minutes, hours or even days. A new fit may start while still in coma or after recovery</li>
    </ol>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:4px 0 0 0;">Body temperature rises during a fit due to increased muscular activity.</p>
  </div>
</div>
''')
new_slides.append(("slide-57.html", slide_wrap(ecl_def, 57)))

# Slide 58: Eclampsia - Causes, DDx, Types, Bad Prognosis
ecl_ddx = content_slide("Eclampsia — Causes, DDx, Types & Prognosis", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Causes</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Cerebral edema & cerebral vasoconstriction → ischemia & hypoxia, microthrombi, or retention of sodium ions → cerebral irritability.
    </p>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 4px 0;">Differential Diagnosis</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li><b>Idiopathic:</b> Epilepsy</li>
      <li><b>Brain lesions:</b> Head trauma, encephalitis, abscess, tumor, aneurysm</li>
      <li><b>Metabolic:</b> Renal/hepatic failure, hypoglycemia, hyponatremia, hypoparathyroidism</li>
      <li><b>Toxic:</b> Arsenic poisoning, barbiturate withdrawal, alcohol withdrawal syndrome</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Types of Eclampsia</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Antepartum:</b> Fits start during pregnancy before onset of labor</li>
      <li><b>Intrapartum:</b> Fits start for first time during labor</li>
      <li><b>Postpartum:</b> Fits start after delivery, usually within first 48 hours</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">Signs of Bad Prognosis (Eden's Criteria)</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 4px 0;">Severe if ≥2 of:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Fits &gt;10</li>
      <li>Coma &gt;6 hours</li>
      <li>Pulse &gt;120 bpm</li>
      <li>Temp &gt;39°C</li>
      <li>SBP &gt;200 mmHg</li>
      <li>RR &gt;40/min</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-58.html", slide_wrap(ecl_ddx, 58)))

# Slide 59: Eclampsia - Complications & Treatment
ecl_rx = content_slide("Eclampsia — Complications & Treatment", f'''
<div style="display:grid;grid-template-columns:1fr 2fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Complications</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Abruptio placentae</li>
      <li>Pulmonary edema</li>
      <li>Acute renal failure</li>
      <li>Aspiration pneumonia</li>
      <li>Intracerebral hemorrhage</li>
      <li>Retinal detachment</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Treatment</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Basic Principle:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Stabilize general condition → then terminate pregnancy.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">1. Support of Cardio-Respiratory Functions:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>Assess & establish airway patency</li>
      <li>Suction as needed; protect patient (elevated padded bed rails)</li>
      <li>Oxygen to improve maternal O₂ & fetal delivery</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">2. Control of Convulsions (MgSO₄):</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;">
      <li>Same dose as preeclampsia</li>
      <li>Monitor for toxicity: patellar reflex (first sign), urinary output (&lt;30 mL/hr), respiratory rate (depression)</li>
      <li>Antidote for Mg toxicity: 10 mL of 10% calcium gluconate IV</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:6px 0 2px 0;">Delivery remains the ultimate treatment.</p>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 14px;margin-top:8px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Student Activity</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Each student is requested to measure the blood pressure of four admitted pregnant women according to clinical guidelines for measurement of blood pressure during pregnancy then comment if there is hypertension or not and what to do if there is a recorded hypertensive blood pressure value.
  </p>
</div>
''')
new_slides.append(("slide-59.html", slide_wrap(ecl_rx, 59)))


# ════════════════════════════════════════════════════════════
# SECTION 6: DIABETES MELLITUS WITH PREGNANCY
# ════════════════════════════════════════════════════════════

# Slide 60: Section Divider
new_slides.append(("slide-60.html", slide_wrap(section_divider("06", "Diabetes Mellitus with Pregnancy", "Gestational & Pregestational Diabetes"), 60)))

# Slide 61: ILOs, Definition, Incidence, Classification
dm_ilo = content_slide("Diabetes Mellitus — ILOs, Definition & Classification", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">ILOs</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Understand effect of diabetes on pregnancy and vice versa</li>
      <li>Describe how to screen for diabetes mellitus in pregnancy</li>
      <li>Explain management of diabetic pregnant woman</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 4px 0;">Definition</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      A disorder in carbohydrate metabolism characterized by hyperglycemia and glucosuria.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Incidence & Classification</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 8px 0;">
      <b>Incidence:</b> 3–5% GDM; 0.5–1% pregestational diabetes.
    </p>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">[A] Pregestational Diabetes</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Type 1:</b> Juvenile onset (autoimmune)</li>
      <li><b>Type 2:</b> Adult onset (insulin resistance)</li>
    </ul>
    <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">[B] Gestational Diabetes (GDM)</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Carbohydrate intolerance of variable severity first diagnosed during pregnancy. Classic GDM diagnosed at 24–28 weeks. GDM diagnosed before 24 weeks → probably undiagnosed type 2 DM, managed as pregestational diabetes.
    </p>
  </div>
</div>
''')
new_slides.append(("slide-61.html", slide_wrap(dm_ilo, 61)))

# Slide 62: Physiologic Changes
dm_phys = content_slide("Diabetes — Physiologic Changes During Pregnancy", f'''
<div style="background:{C["bg"]};padding:10px 14px;border-radius:8px;border-left:4px solid {C["teal"]};">
  <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Physiologic Changes in Carbohydrate Metabolism</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
    <li>Hyperplasia of pancreatic islet cells → doubling in insulin production between 1st and 3rd trimesters</li>
    <li>Initial increase in insulin sensitivity during first trimester</li>
    <li>Progressive glucose intolerance with advanced gestation due to release of insulin-resistant hormones from placenta: <b>HPL, glucagon, progesterone, corticotrophin releasing hormone</b></li>
    <li>Increased glucose uptake of fetus and increased peripheral uptake</li>
    <li>Increased glycogenesis and reduced hepatic gluconeogenesis</li>
    <li>Reduced renal tubular threshold for glucose → glucosuria</li>
    <li><b>Overall:</b> Fasting glucose levels fall by 10–20%; postprandial levels are higher</li>
  </ul>
</div>
''')
new_slides.append(("slide-62.html", slide_wrap(dm_phys, 62)))

# Slide 63: Effects - Pregnancy on DM & DM on Pregnancy (Fetal)
dm_eff1 = content_slide("Diabetes — Effects of Pregnancy on DM & Fetal Risks", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Effect of Pregnancy on DM</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Disease may appear for first time during pregnancy</li>
      <li>Insulin requirements gradually increase after 3rd month until term</li>
      <li>Ketoacidosis can occur with lower blood glucose levels</li>
      <li>Aggravation of diabetic microangiopathy (nephropathy, retinopathy, neuropathy)</li>
      <li>During delivery: liability to hypoglycemia from uterine activity</li>
      <li>After delivery: insulin requirement decreases (drop in placental hormones)</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Effects of DM on Pregnancy — Fetal Risks</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <ul style="margin:0;padding-left:18px;">
        <li>Miscarriage</li>
        <li>Congenital anomaly (doubled) — CVS & NTDs</li>
        <li>Macrosomia</li>
        <li>Prematurity</li>
        <li>Shoulder dystocia & birth injury</li>
        <li>Respiratory distress</li>
      </ul>
      <ul style="margin:0;padding-left:18px;">
        <li>Neonatal hypoglycemia</li>
        <li>IUFD</li>
        <li>IUGR</li>
        <li>Neonatal hyperbilirubinemia, hypocalcemia, hypothermia</li>
        <li>Risk of having diabetes: 15% in type 2, 2% in type 1</li>
      </ul>
    </div>
  </div>
</div>
''')
new_slides.append(("slide-63.html", slide_wrap(dm_eff1, 63)))

# Slide 64: Maternal Risks & Risk Factors for GDM
dm_eff2 = content_slide("Diabetes — Maternal Risks & Risk Factors for GDM", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Maternal Risks</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Hypoglycemia</li>
      <li>Diabetic ketoacidosis</li>
      <li>Polyhydramnios</li>
      <li>Obstructed labor</li>
      <li>Operative delivery</li>
      <li>Worsening of retinal disease</li>
      <li>Worsening of renal disease</li>
      <li>Pre-eclampsia</li>
      <li>Postpartum hemorrhage</li>
      <li>Infection</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Risk Factors for Gestational DM</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>BMI &gt;30 kg/m²</li>
      <li>Previous macrosomic infant ≥4.5 kg</li>
      <li>Previous GDM (30–84%)</li>
      <li>First degree relative with diabetes</li>
      <li>Glycosuria 2+</li>
      <li>Unexplained IUFD</li>
      <li>Current macrosomia and polyhydramnios</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-64.html", slide_wrap(dm_eff2, 64)))

# Slide 65: Screening & Diagnosis
dm_screen = content_slide("Diabetes — Screening & Diagnosis", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">One-Hour Glucose Challenge Test (GCT)</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>50-g glucose at 24–28 weeks</li>
      <li>No fasting required</li>
      <li>Normal: serum/plasma glucose &lt;140 mg/dL</li>
      <li>Positive screen → confirm with oral GTT</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Three-Hour Oral Glucose Tolerance Test (GTT)</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
      If GCT ≥140 mg/dL → 3-hour diagnostic GTT with 100 g glucose after 8-hour fast. Use Carpenter & Coustan values.
    </p>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["gold"]};border-radius:8px;padding:10px 14px;margin-top:10px;">
  <p style="font-size:14px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">GTT Diagnostic Values</p>
  <table style="width:100%;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;border-collapse:collapse;">
    <tr style="background:{C["teal"]};color:{C["white"]};">
      <th style="padding:6px;text-align:left;">Time</th>
      <th style="padding:6px;text-align:left;">NDDG</th>
      <th style="padding:6px;text-align:left;">Carpenter & Coustan</th>
    </tr>
    <tr style="background:{C["bg"]};">
      <td style="padding:4px 6px;"><b>Fasting</b></td>
      <td style="padding:4px 6px;">105 mg/dL (5.8 mmol/L)</td>
      <td style="padding:4px 6px;">95 mg/dL (5.3 mmol/L)</td>
    </tr>
    <tr>
      <td style="padding:4px 6px;"><b>1-hour</b></td>
      <td style="padding:4px 6px;">190 mg/dL (10.5 mmol/L)</td>
      <td style="padding:4px 6px;">180 mg/dL (10.0 mmol/L)</td>
    </tr>
    <tr style="background:{C["bg"]};">
      <td style="padding:4px 6px;"><b>2-hour</b></td>
      <td style="padding:4px 6px;">165 mg/dL (9.2 mmol/L)</td>
      <td style="padding:4px 6px;">155 mg/dL (8.6 mmol/L)</td>
    </tr>
    <tr>
      <td style="padding:4px 6px;"><b>3-hour</b></td>
      <td style="padding:4px 6px;">145 mg/dL (8.0 mmol/L)</td>
      <td style="padding:4px 6px;">140 mg/dL (7.8 mmol/L)</td>
    </tr>
  </table>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 0 0;">If any <b>two or more</b> diagnostic values are met or exceeded → diagnosis of GDM.</p>
</div>
''')
new_slides.append(("slide-65.html", slide_wrap(dm_screen, 65)))

# Slide 66: Management of GDM (A1 & A2)
dm_gdm = content_slide("Management of Gestational Diabetes", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Antenatal Care</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Frequent antenatal care visits</li>
      <li><b>Glycemic control targets:</b>
        <ul style="margin:2px 0 0 14px;">
          <li>Fasting: &lt;95 mg/dL</li>
          <li>1-hour postprandial: &lt;140 mg/dL</li>
          <li>2-hour postprandial: &lt;115 mg/dL</li>
        </ul>
      </li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">I. GDM-A1 (Diet-Controlled)</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Diet:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">1,800–2,400 kcal/day (30 kcal/kg): 15–20% protein, 50–60% carbs, 20% fat. Nutritional consultation.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 2px 0;">Exercise:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Moderate exercise lowers maternal glucose concentrations.</p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">II. GDM-A2 (Pharmacologic)</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
      When glycemic status inadequately controlled by diet alone.
    </p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Glucose Monitoring:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.4;margin:0 0 6px 0;">
      Glucometer: record fasting & 1-hr (or 2-hr) postprandial values.
    </p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Goal Values:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Fasting: 60–90 mg/dL</li>
      <li>1-hr postprandial: &lt;140 mg/dL</li>
      <li>2-hr postprandial: &lt;120 mg/dL</li>
      <li>Bedtime: &lt;120 mg/dL</li>
      <li>2:00–6:00 AM: 60–90 mg/dL</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">Oral Hypoglycemic:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Metformin for women who decline insulin therapy.</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 2px 0;">Fetal Wellbeing:</p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">U/S and NST in last trimester every 2 weeks.</p>
  </div>
</div>
''')
new_slides.append(("slide-66.html", slide_wrap(dm_gdm, 66)))

# Slide 67: Pre-gestational DM - HbA1C & Insulin
dm_pregest = content_slide("Management of Pre-gestational Diabetes Mellitus", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">HbA1C Monitoring</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Reflects glycemic control over past 8–12 weeks</li>
      <li>Assesses risk of fetal anomalies in 1st trimester</li>
      <li>Measured every trimester</li>
      <li>Diagnosis of overt DM: A1C ≥6.5%</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Insulin Dosage — Two-Dose Regimen</p>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Daily dose by trimester:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>1st trimester: 0.7 units/kg</li>
      <li>2nd trimester: 0.8 units/kg</li>
      <li>3rd trimester: 0.9–1.1 units/kg</li>
    </ul>
    <p style="font-size:13px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:6px 0 4px 0;">Administration:</p>
    <ul style="margin:0;padding-left:18px;font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.45;">
      <li>Total daily dose divided in half — morning & evening</li>
      <li><b>Morning (before breakfast):</b> ⅔ NPH (intermediate) + ⅓ rapid-acting</li>
      <li><b>Evening (before dinner):</b> ½ NPH + ½ rapid-acting</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-67.html", slide_wrap(dm_pregest, 67)))

# Slide 68: Management of Labor & Delivery
dm_labor = content_slide("Diabetes — Management of Labor & Delivery", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Timing of Delivery</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>At 38 weeks:</b> Controlled DM, no fetal/maternal complications</li>
      <li><b>Before 38 weeks:</b> Uncontrolled DM, fetal complications (IUGR), maternal complications (preeclampsia)</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:8px 0 4px 0;">Route of Delivery</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>IOL:</b> Controlled DM, no maternal/fetal indications (macrosomia, malpresentation)</li>
      <li><b>CS:</b> Uncontrolled DM, maternal/fetal complications, failed IOL, macrosomia, malpresentations, obstetric indication</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Intrapartum Glucose Control</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Patient must be <b>euglycemic</b> during intrapartum period:
        <br>Maternal hyperglycemia → fetal hyperglycemia → fetal hyperinsulinemia → neonatal hypoglycemia → neonatal seizures & death</li>
      <li>Infusion fluid adjusted based on glucose levels</li>
      <li>Short-acting insulin boluses may be added to target 80–100 mg/dL</li>
      <li>Check blood glucose every 1–2 hours</li>
      <li>Patient receives normal insulin dose previous evening</li>
      <li><b>On morning of induction:</b> withhold usual insulin dose</li>
    </ul>
  </div>
</div>
<div style="background:{C["bg"]};padding:8px 14px;border-radius:8px;border-left:4px solid {C["gold"]};margin-top:8px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Elective Cesarean Section</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Withhold morning insulin dose. Monitor glucose frequently during and immediately after surgery.
  </p>
</div>
''')
new_slides.append(("slide-68.html", slide_wrap(dm_labor, 68)))

# Slide 69: Postpartum, Breastfeeding, Contraception
dm_post = content_slide("Diabetes — Postpartum Care, Breastfeeding & Contraception", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Postpartum Glucose Monitoring</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Check glucose every 4–6 hours</li>
      <li>Administer 5% dextrose with lactated Ringer's or NS (~125 mL/hr)</li>
      <li>Use short-acting insulin only if glucose &gt;150 mg/dL</li>
      <li>Once on full diabetic diet: restart insulin at ⅓ to ½ antepartum dosage</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">Postpartum Evaluation in GDM</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Follow-up fasting BG + 2-hour 75-g GTT (6–12 weeks postpartum)</li>
      <li>If threshold values met → diagnosis of type 2 DM</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Breastfeeding</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Breastfeeding ↑ frequency of hypoglycemia in insulin-dependent diabetics</li>
      <li>Women should have a snack before or during breastfeeding</li>
      <li>Women with pre-existing type 2 DM can safely take metformin while breastfeeding</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">Contraception</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Progesterone-only methods</b> and <b>mechanical methods</b> can be used</li>
      <li>IUCD can cause pelvic inflammatory disease</li>
      <li><b>Combined pills are contraindicated</b></li>
    </ul>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 14px;margin-top:8px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Student Activity</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Each student should check the blood glucose measurements/investigations of admitted departmental pregnant women to pick up either suspected or confirmed cases of diabetes and explain the next steps during bedside teaching part of the clinical rounds.
  </p>
</div>
''')
new_slides.append(("slide-69.html", slide_wrap(dm_post, 69)))


# ════════════════════════════════════════════════════════════
# SECTION 7: URINARY TRACT INFECTION WITH PREGNANCY
# ════════════════════════════════════════════════════════════

# Slide 70: Section Divider
new_slides.append(("slide-70.html", slide_wrap(section_divider("07", "Urinary Tract Infection with Pregnancy", "Asymptomatic Bacteriuria, Cystitis & Pyelonephritis"), 70)))

# Slide 71: ILOs, Incidence, Risk Factors
uti_ilo = content_slide("UTI — ILOs, Incidence & Risk Factors", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">ILOs</p>
    <ul style="margin:0;padding-left:16px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Understand incidence and risk factors of UTI during pregnancy</li>
      <li>Describe clinical picture of UTI during pregnancy</li>
      <li>Explain management of UTI during pregnancy</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Incidence</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 8px 0;">
      Urinary tract infection is more common during pregnancy.
    </p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Asymptomatic bacteriuria</b> (&gt;100,000 organisms/mL without symptoms): 4–7% of pregnancies</li>
      <li><b>Cystitis:</b> ~1% of pregnancies</li>
      <li><b>Pyelonephritis:</b> 1–2% of pregnant women</li>
    </ul>
    <p style="font-size:15px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:10px 0 6px 0;">Risk Factors</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>History of UTI in previous pregnancy or before pregnancy</li>
      <li>Diabetic patient</li>
      <li>Patient receiving steroids or immunosuppression</li>
      <li>Patient with congenital abnormalities of urinary tract</li>
      <li>Patient with renal calculi</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-71.html", slide_wrap(uti_ilo, 71)))

# Slide 72: Clinical Picture
uti_cp = content_slide("UTI — Clinical Picture", f'''
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-top:4px solid {C["teal"]};">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Asymptomatic Bacteriuria</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
      Typically no symptoms. If left untreated, <b>~40%</b> develop symptomatic UTI.
    </p>
    <p style="font-size:12px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.3;margin:6px 0 0 0;">
      All pregnant females should be screened with MSU at booking. If negative, chance of developing UTI in pregnancy is &lt;2%.
    </p>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-top:4px solid {C["orange"]};">
    <p style="font-size:14px;font-weight:700;color:{C["orange"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Cystitis</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;margin:0;">
      Presents with:
    </p>
    <ul style="margin:4px 0 0 16px;padding-left:0;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Frequency</li>
      <li>Dysuria</li>
      <li>Hematuria</li>
      <li>Proteinuria</li>
      <li>Supra-pubic pain</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-top:4px solid {C["coral"]};">
    <p style="font-size:14px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Pyelonephritis</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;margin:0;">
      Presents with:
    </p>
    <ul style="margin:4px 0 0 16px;padding-left:0;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li>Fever</li>
      <li>Rigors</li>
      <li>Vomiting</li>
      <li>Loin pain</li>
    </ul>
  </div>
</div>
''')
new_slides.append(("slide-72.html", slide_wrap(uti_cp, 72)))

# Slide 73: Investigations
uti_inv = content_slide("UTI — Investigations", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:30px;">
  <div style="background:{C["bg"]};padding:12px 16px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:16px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Urine Analysis</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li>Dipstick for <b>nitrites</b> and <b>leukocyte esterase</b></li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:12px 16px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:16px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 8px 0;">Midstream Urine (MSU) Culture</p>
    <ul style="margin:0;padding-left:18px;font-size:14px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.6;">
      <li><b>Mandatory</b></li>
      <li>&gt;100,000 organisms/mL → diagnostic of asymptomatic bacteriuria</li>
    </ul>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px;">
  <div style="background:{C["white"]};border:1.5px solid {C["gold"]};border-radius:8px;padding:10px 14px;">
    <p style="font-size:14px;font-weight:700;color:{C["gold"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">CBC & Renal Function Tests</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Indicated in the presence of pyrexia.</p>
  </div>
  <div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:10px 14px;">
    <p style="font-size:14px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Ultrasound of Urinary Tract</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0;">Indicated in repeated infections.</p>
  </div>
</div>
''')
new_slides.append(("slide-73.html", slide_wrap(uti_inv, 73)))

# Slide 74: Treatment & Student Activity
uti_rx = content_slide("UTI — Treatment & Student Activity", f'''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["teal"]};">
    <p style="font-size:15px;font-weight:700;color:{C["teal"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Treatment Principles</p>
    <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0 0 6px 0;">
      Antibiotic choice depends on sensitivity.
    </p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Asymptomatic bacteriuria:</b> Oral antibiotic for 3 days</li>
      <li><b>Cystitis:</b> Treatment for 7 days</li>
      <li><b>All bacteriuria in pregnancy should be treated</b> to prevent pyelonephritis and preterm delivery</li>
    </ul>
  </div>
  <div style="background:{C["bg"]};padding:10px 12px;border-radius:8px;border-left:4px solid {C["coral"]};">
    <p style="font-size:15px;font-weight:700;color:{C["coral"]};font-family:'Times New Roman',serif;margin:0 0 6px 0;">Pyelonephritis Management</p>
    <ul style="margin:0;padding-left:18px;font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.5;">
      <li><b>Hospitalization</b></li>
      <li>IV fluids</li>
      <li>Antipyretics</li>
      <li><b>Parenteral broad spectrum antibiotics</b> (e.g. cephalosporins) until culture results or fever settles</li>
      <li>Then oral antibiotic according to sensitivity for total of <b>10–14 days</b></li>
    </ul>
  </div>
</div>
<div style="background:{C["white"]};border:1.5px solid {C["teal"]};border-radius:8px;padding:8px 14px;margin-top:12px;">
  <p style="font-size:14px;font-weight:700;color:{C["dark"]};font-family:'Times New Roman',serif;margin:0 0 4px 0;">Student Activity</p>
  <p style="font-size:13px;color:{C["dark"]};font-family:'Times New Roman',serif;line-height:1.35;margin:0;">
    Each student is requested to check the urine analysis of admitted departmental pregnant women for pyuria then evaluate pregnant women with +ve pyuria for symptoms of pyelonephritis with the aid of the tutor during bedside teaching part of clinical round.
  </p>
</div>
''')
new_slides.append(("slide-74.html", slide_wrap(uti_rx, 74)))


# ════════════════════════════════════════════════════════════
# WRITE NEW SLIDES
# ════════════════════════════════════════════════════════════

for fname, html in new_slides:
    fpath = os.path.join(SLIDES_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {fpath}")

print(f"\nNew slides: {len(new_slides)} generated.")
print("Total slides now: 44 + 30 = 74")
