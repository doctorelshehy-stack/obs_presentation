#!/usr/bin/env python3
"""Generate HTML slides for Infectious Diseases with Pregnancy & RH Incompatibility."""

import os

SLIDES_DIR = "/media/mohamed/projects4/projects/obstaric/raw material/3_Medical_Obstetric_Disorders/3c_Infections_Immunological/slides"

# Palette 10 - Education
C = {
    "dark": "#264653",
    "teal": "#2a9d8f",
    "yellow": "#e9c46a",
    "orange": "#f4a261",
    "coral": "#e76f51",
    "white": "#ffffff",
    "light_bg": "#f0f5f5",
    "light_card": "#ffffff",
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
    return f'''<svg style="position:absolute;right:32px;bottom:24px;width:36px;height:36px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="36" height="36" rx="18" fill="{C['teal']}" />
  <text x="18" y="25" text-anchor="middle" font-family="'Times New Roman',serif" font-size="16" font-weight="700" fill="{C['white']}">{num:02d}</text>
</svg>'''

def base_html(content, page_num=None):
    badge = page_badge(page_num) if page_num is not None else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{APPENDIX_A}
</head>
<body>
<div class="slide-content" style="background:{C['light_bg']};width:960px;height:540px;overflow:hidden;font-family:'Times New Roman',serif;">
{content}
{badge}
</div>
</body>
</html>'''

def write_slide(num, content, page_num=None):
    path = os.path.join(SLIDES_DIR, f"slide-{num:02d}.html")
    with open(path, "w") as f:
        f.write(base_html(content, page_num))
    print(f"  -> slide-{num:02d}.html")

def section_divider(num, section_num, title, subtitle=None):
    """Generate a section divider slide."""
    sub_html = f'<p style="position:absolute;top:260px;left:60px;right:60px;font-size:18px;color:{C["dark"]};opacity:0.85;line-height:1.5;">{subtitle}</p>' if subtitle else ""
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['dark']};"></div>
<div style="position:absolute;top:0;left:0;width:12px;height:540px;background:{C['teal']};"></div>
<p style="position:absolute;top:120px;left:60px;font-size:96px;font-weight:700;color:{C['teal']};opacity:0.3;margin:0;">{section_num:02d}</p>
<p style="position:absolute;top:180px;left:60px;font-size:42px;font-weight:700;color:{C['white']};margin:0;">{title}</p>
{sub_html}'''
    write_slide(num, content, num)

def cover_page():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,{C['dark']} 0%,#1a3a3a 100%);"></div>
<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:radial-gradient(ellipse at 80% 40%,rgba(42,157,143,0.15) 0%,transparent 60%);"></div>
<!-- Decorative shapes -->
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="8" height="540" fill="{C['teal']}" />
  <circle cx="860" cy="80" r="120" fill="none" stroke="{C['teal']}" stroke-width="1" opacity="0.15" />
  <circle cx="880" cy="100" r="80" fill="none" stroke="{C['yellow']}" stroke-width="0.5" opacity="0.1" />
</svg>
<!-- Gold accent bar -->
<div style="position:absolute;top:120px;left:70px;width:80px;height:5px;background:{C['yellow']};border-radius:2.5px;"></div>
<!-- First heading line -->
<p style="position:absolute;top:120px;left:70px;font-size:30px;font-weight:400;color:{C['white']};opacity:0.8;margin:0;">Medical Obstetric Disorders</p>
<!-- Main title -->
<p style="position:absolute;top:175px;left:70px;right:60px;font-size:52px;font-weight:700;color:{C['teal']};margin:0;line-height:1.15;">Infectious Diseases<br>with Pregnancy &amp;<br>RH Incompatibility</p>
<!-- Subtitle -->
<p style="position:absolute;top:340px;left:70px;font-size:18px;color:{C['white']};opacity:0.7;margin:0;">A Comprehensive Obstetric Reference Presentation</p>
<!-- Supporting text -->
<p style="position:absolute;top:380px;left:70px;font-size:16px;color:{C['white']};opacity:0.4;margin:0;">Based on Standard Obstetric Curriculum • TORCH Infections • RH Isoimmunization</p>
<div style="position:absolute;bottom:40px;left:70px;right:60px;border-top:1px solid rgba(255,255,255,0.1);padding-top:12px;">
<p style="font-size:14px;color:{C['white']};opacity:0.3;margin:0;">Source: 17_Infectious_Diseases_with_Pregnancy.pdf • 45_RH_Incompatibility.pdf</p>
</div>'''
    write_slide(1, content)

def toc():
    items = [
        ("01", "Infectious Diseases with Pregnancy", [
            "TORCH Infections Overview",
            "Toxoplasmosis", "Rubella", "Cytomegalovirus", "Herpes Simplex"
        ]),
        ("02", "RH Incompatibility", [
            "Definition & Etiology", "Pathogenesis & Clinical Varieties",
            "Investigations & Diagnosis", "Management (Prophylactic & During Pregnancy)",
            "Intrauterine Transfusion", "Newborn Management",
            "ABO Incompatibility", "Hydrops Fetalis"
        ]),
    ]
    items_html = ""
    for i, (num, title, subs) in enumerate(items):
        subs_html = ""
        for s in subs:
            subs_html += f'<li style="font-size:13px;color:{C["dark"]};opacity:0.7;margin:2px 0;">{s}</li>'
        items_html += f'''<div style="display:flex;align-items:flex-start;gap:12px;padding:10px 14px;background:{'rgba(42,157,143,0.08)' if i==0 else 'rgba(233,196,106,0.08)'};border-radius:6px;border-left:3px solid {C['teal'] if i==0 else C['yellow']};">
  <span style="font-size:28px;font-weight:700;color:{C['teal'] if i==0 else C['yellow']};min-width:40px;">{num}</span>
  <div>
    <p style="font-size:20px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">{title}</p>
    <ul style="margin:0;padding-left:18px;list-style-type:disc;">{subs_html}</ul>
  </div>
</div>'''

    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:24px;left:50px;font-size:28px;font-weight:700;color:{C['dark']};margin:0;">Table of Contents</p>
<div style="position:absolute;top:62px;left:50px;width:60px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<div style="position:absolute;top:80px;left:50px;right:40px;bottom:60px;display:flex;flex-direction:column;gap:14px;">
{items_html}
</div>'''
    write_slide(2, content, 2)

# ===================== SLIDE DATA =====================

def slide_04_ilos_background():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Infectious Diseases with Pregnancy</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- ILOs Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Intended Learning Outcomes (ILOs)</p>
  <ul style="margin:0;padding-left:18px;font-size:14px;color:{C['dark']};line-height:1.5;">
    <li>Understand the etiology and mode of transmission of variable infections during pregnancy</li>
    <li>Describe the clinical picture of these infections during pregnancy</li>
    <li>Explain the management of these infections during pregnancy</li>
  </ul>
</div>
<!-- Background Card -->
<div style="position:absolute;top:195px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Background</p>
  <p style="font-size:14px;color:{C['dark']};margin:0 0 6px 0;line-height:1.5;">Viral infections in pregnancy are major causes of maternal and fetal morbidity and mortality. Infections can develop in the neonate:</p>
  <ul style="margin:0;padding-left:18px;font-size:14px;color:{C['dark']};line-height:1.6;">
    <li><strong>Trans-placentally</strong> (in utero)</li>
    <li><strong>Perinatally</strong> (from vaginal secretions or blood)</li>
    <li><strong>Postnatally</strong> (from breast milk or other sources)</li>
  </ul>
</div>
<!-- TORCH Acronym Card -->
<div style="position:absolute;top:340px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 8px 0;">TORCH Acronym — Infections Known to Produce Congenital Defects</p>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr 1fr;gap:8px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:20px;font-weight:700;color:{C['teal']};margin:0;">T</p>
      <p style="font-size:11px;color:{C['dark']};margin:2px 0 0 0;">Toxoplasma</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:20px;font-weight:700;color:{C['orange']};margin:0;">O</p>
      <p style="font-size:11px;color:{C['dark']};margin:2px 0 0 0;">Others*</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:20px;font-weight:700;color:{C['coral']};margin:0;">R</p>
      <p style="font-size:11px;color:{C['dark']};margin:2px 0 0 0;">Rubella</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:20px;font-weight:700;color:{C['teal']};margin:0;">C</p>
      <p style="font-size:11px;color:{C['dark']};margin:2px 0 0 0;">CMV</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:20px;font-weight:700;color:{C['orange']};margin:0;">H</p>
      <p style="font-size:11px;color:{C['dark']};margin:2px 0 0 0;">Herpes</p>
    </div>
  </div>
  <p style="font-size:12px;color:{C['dark']};opacity:0.7;margin:6px 0 0 0;font-style:italic;">*Others: Parvovirus B19 (B19V), Varicella-Zoster Virus (VZV), Measles virus, Enteroviruses, Human Immunodeficiency Virus (HIV)</p>
</div>'''
    write_slide(4, content, 4)

def slide_05_toxoplasmosis():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Toxoplasmosis</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Overview Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Overview</p>
  <ul style="margin:0;padding-left:18px;font-size:14px;color:{C['dark']};line-height:1.6;">
    <li>Caused by <strong>T. gondii</strong> — an obligate intracellular protozoan</li>
    <li><strong>Cats</strong> are the definitive hosts</li>
    <li>Maternal infection is acquired by eating <strong>undercooked meat</strong></li>
    <li>Primary infection causes a <strong>life-long immunity</strong> and usually prevents re-infection</li>
  </ul>
</div>
<!-- Congenital Transmission Card -->
<div style="position:absolute;top:230px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Congenital Transmission</p>
  <p style="font-size:14px;color:{C['dark']};margin:0;line-height:1.5;">The severity of infection decreases with gestational age, i.e. <strong>most severe infections occur in 1st trimester</strong>.</p>
</div>
<!-- Maternal Clinical Picture Card -->
<div style="position:absolute;top:300px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 14px;border-left:4px solid {C['orange']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Maternal Infection — Clinical Picture</p>
  <ul style="margin:0;padding-left:18px;font-size:14px;color:{C['dark']};line-height:1.6;">
    <li>In acute maternal infection, patients are <strong>usually asymptomatic</strong></li>
    <li>Some patients may present with:</li>
  </ul>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:4px 0 0 18px;">
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>•</strong> Posterior cervical lymphadenopathy</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>•</strong> Fatigue</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>•</strong> Fever</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>•</strong> Maculopapular rash</div>
  </div>
</div>
<!-- Fetal Infection Card -->
<div style="position:absolute;top:460px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 14px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Fetal Infection — Diagnostic Triad</p>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
    <div style="background:{C['white']};border-radius:6px;padding:6px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['teal']};margin:0;">Hydrocephalus</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:6px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['teal']};margin:0;">Intracranial Calcifications</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:6px;text-align:center;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['teal']};margin:0;">Chorioretinitis</p>
    </div>
  </div>
</div>'''
    write_slide(5, content, 5)

def slide_06_toxoplasmosis_2():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Toxoplasmosis — Investigations &amp; Treatment</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Investigations Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 8px 0;">Investigations</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
    <div style="background:{C['white']};border-radius:6px;padding:10px 14px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:15px;font-weight:700;color:{C['teal']};margin:0 0 4px 0;">Maternal</p>
      <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">Serology for detection of the <strong>specific IgM</strong></p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:10px 14px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:15px;font-weight:700;color:{C['orange']};margin:0 0 4px 0;">Fetal</p>
      <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
        • Isolation of <strong>Toxoplasma in amniotic fluid by PCR</strong><br>
        • Ultrasound may detect fetal anomalies: hydrocephalus, intracranial calcifications
      </p>
    </div>
  </div>
</div>
<!-- Treatment Card -->
<div style="position:absolute;top:240px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Treatment</p>
  <div style="background:{C['white']};border-radius:6px;padding:10px 14px;border:1px solid rgba(38,70,83,0.1);">
    <p style="font-size:14px;color:{C['dark']};margin:0;line-height:1.5;">The drug of choice during pregnancy is <strong style="color:{C['coral']};">Spiramycin</strong> which can reduce the risk of congenital transmission.</p>
  </div>
</div>
<!-- Key Points -->
<div style="position:absolute;top:360px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['yellow']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Key Points to Remember</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li><strong>T. gondii</strong> — obligate intracellular protozoan; cats are definitive hosts</li>
    <li>Infection via <strong>undercooked meat</strong></li>
    <li>Severity inversely related to gestational age — worst in 1st trimester</li>
    <li>Fetal triad: <strong>Hydrocephalus + Intracranial calcifications + Chorioretinitis</strong></li>
    <li>Diagnosis: Maternal IgM serology; Fetal PCR on amniotic fluid</li>
    <li>Treatment: <strong>Spiramycin</strong></li>
  </ul>
</div>'''
    write_slide(6, content, 6)

def slide_07_rubella():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Rubella</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Overview Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Overview</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>Type:</strong> RNA virus — one of the most teratogenic viruses</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>Mode of infection:</strong> Droplet infection</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>Incubation period:</strong> 2–3 weeks</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>Prevention:</strong> MMR vaccine (contraindicated in pregnancy)</div>
  </div>
</div>
<!-- CRS Card -->
<div style="position:absolute;top:195px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Congenital Rubella Syndrome (CRS)</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Intrauterine growth restriction (IUGR)</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Intracranial calcifications</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Microcephaly</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Cataracts</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Cardiac defects (PDA / pulmonary arterial hypoplasia)</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Neurologic disease (behavior disorders to meningoencephalitis)</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Osteitis</div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};"><strong>•</strong> Hepatosplenomegaly</div>
  </div>
</div>
<!-- Clinical Picture Card -->
<div style="position:absolute;top:360px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Clinical Picture</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li><strong>Maculopapular rash</strong> that persists for 3 days</li>
    <li><strong>Generalized lymphadenopathy</strong> (especially postauricular and occipital) — may precede rash</li>
    <li><strong>Transient arthritis</strong>, malaise, and headache</li>
  </ul>
</div>'''
    write_slide(7, content, 7)

def slide_08_rubella_diagnosis():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Rubella — Diagnosis, Prevention &amp; Treatment</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Diagnosis Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 8px 0;">Diagnosis</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['teal']};margin:0 0 4px 0;">Maternal</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;">If suspicion of exposure, both <strong>IgM and IgG</strong> should be done and repeated after 3 weeks.</p>
      <ul style="margin:4px 0 0 0;padding-left:14px;font-size:11px;color:{C['dark']};line-height:1.4;">
        <li>IgM (−), IgG did not rise → <strong>no acute infection</strong></li>
        <li>IgM (−), IgG level rise → infection may have occurred but <strong>reduced risk of CRS</strong></li>
        <li>IgM (+) in any sample → <strong>acute rubella infection</strong></li>
      </ul>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['orange']};margin:0 0 4px 0;">Fetal</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;">Detecting <strong>viral RNA by PCR</strong> from:</p>
      <ul style="margin:4px 0 0 0;padding-left:14px;font-size:11px;color:{C['dark']};line-height:1.4;">
        <li>Chorionic villi</li>
        <li>Fetal blood</li>
        <li>Amniotic sample</li>
      </ul>
    </div>
  </div>
</div>
<!-- Prevention Card -->
<div style="position:absolute;top:270px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Prevention</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;"><strong>MMR vaccine</strong> should be offered to all women of childbearing age. It should <strong>not</strong> be given to pregnant women.</p>
</div>
<!-- Treatment Card -->
<div style="position:absolute;top:340px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Treatment</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li><strong>Induction of abortion</strong> if infection occurs in the first trimester</li>
    <li><strong>Immunoglobulin</strong> administration</li>
  </ul>
</div>
<!-- Key Summary -->
<div style="position:absolute;top:430px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['yellow']};">
  <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;"><strong>Key:</strong> Rubella is highly teratogenic (RNA virus) → Droplet infection → CRS includes IUGR, microcephaly, cataracts, cardiac defects, neurologic disease → Diagnose by serial IgM/IgG → Prevent with MMR (pre-pregnancy) → Treat 1st trimester infection with abortion + immunoglobulin.</p>
</div>'''
    write_slide(8, content, 8)

def slide_09_cmv():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Cytomegalovirus (CMV)</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Overview Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Overview</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>Type:</strong> Double-stranded DNA herpes virus</div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 10px;font-size:13px;color:{C['dark']};"><strong>Significance:</strong> Most common congenital viral infection</div>
  </div>
</div>
<!-- Mode of infection -->
<div style="position:absolute;top:155px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Mode of Infection</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li>Contact with <strong>saliva, urine or other body fluids</strong></li>
    <li><strong>Transplacental</strong> transmission</li>
    <li>Transmission via <strong>breast milk</strong></li>
  </ul>
</div>
<!-- Clinical Picture -->
<div style="position:absolute;top:240px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Clinical Picture</p>
  <p style="font-size:13px;color:{C['dark']};margin:0 0 4px 0;">May be <strong>asymptomatic</strong>. Malaise, fever, generalized lymphadenopathy.</p>
  <p style="font-size:13px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Transplacental Infection Results In:</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;">
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Intrauterine growth restriction (IUGR)</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Sensorineural hearing loss</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Intracranial calcifications</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Microcephaly</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Hydrocephalus</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Hepatosplenomegaly</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Delayed psychomotor development</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Optic atrophy</div>
  </div>
</div>'''
    write_slide(9, content, 9)

def slide_10_cmv_diagnosis():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">CMV — Diagnosis &amp; Management</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Diagnosis Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 8px 0;">Diagnosis</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['teal']};margin:0 0 4px 0;">1. Maternal</p>
      <p style="font-size:13px;color:{C['dark']};margin:0;">Detection of <strong>CMV-IgM and IgG</strong> antibodies</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:14px;font-weight:700;color:{C['orange']};margin:0 0 4px 0;">2. Fetal</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;">
        <strong>Fetal Ultrasound:</strong><br>
        Microcephaly, ventriculomegaly, intracranial calcifications, oligohydramnios, IUGR
      </p>
      <p style="font-size:12px;color:{C['dark']};margin:4px 0 0 0;"><strong>Amniocentesis &amp; Cordocentesis</strong> for PCR DNA testing to diagnose intrauterine infection.</p>
    </div>
  </div>
</div>
<!-- Management Card -->
<div style="position:absolute;top:270px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Management</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">Symptomatic Treatment</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Supportive care based on clinical manifestations</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['coral']};margin:0 0 2px 0;">Passive Immunization</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">CMV specific immunoglobulin</p>
    </div>
  </div>
</div>
<!-- Key facts summary -->
<div style="position:absolute;top:400px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['yellow']};">
  <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;"><strong>Key:</strong> CMV is the most common congenital viral infection (dsDNA herpes virus). Transmission via body fluids, transplacental, breast milk. Can cause IUGR, hearing loss, intracranial calcifications, microcephaly, hydrocephalus. Diagnosed by maternal serology (IgM/IgG) and fetal US/PCR. Managed symptomatically and with CMV-specific immunoglobulin.</p>
</div>'''
    write_slide(10, content, 10)

def slide_11_herpes():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Herpes Simplex (HSV)</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Overview Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Overview</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">It is a <strong>double stranded DNA virus</strong>.</p>
</div>
<!-- Mode of infection -->
<div style="position:absolute;top:152px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Mode of Infection</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li>Direct contact with <strong>mucous membranes or skin</strong> infected with the virus, commonly through <strong>sexual contact</strong></li>
    <li>Fetal infection with HSV can occur <strong>transplacentally</strong>, or as an <strong>ascending infection from the cervix</strong></li>
  </ul>
</div>
<!-- Clinical Picture -->
<div style="position:absolute;top:277px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Clinical Picture</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">Maternal</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Painful, <strong>vesicular lesions</strong> and ulcers</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['coral']};margin:0 0 2px 0;">Fetal / Neonatal</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;">
        Neonatal herpes acquired from passage through <strong>infected birth canal</strong>.<br>
        Risk of vertical transmission:
      </p>
      <ul style="margin:2px 0 0 0;padding-left:14px;font-size:11px;color:{C['dark']};">
        <li><strong>50%</strong> for primary HSV infection</li>
        <li><strong>0–4%</strong> in women with recurrent disease</li>
      </ul>
      <p style="font-size:11px;color:{C['dark']};margin:4px 0 0 0;">Congenital infections are <strong>very rare</strong> and may produce disseminated or CNS disease.</p>
    </div>
  </div>
</div>'''
    write_slide(11, content, 11)

def slide_12_herpes_2():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Herpes Simplex — Diagnosis, Prevention &amp; Management</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Diagnosis Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Diagnosis</p>
  <p style="font-size:13px;color:{C['dark']};margin:0 0 4px 0;"><strong>Maternal:</strong> PCR for detection of <strong>IgM and IgG</strong> antibodies.</p>
</div>
<!-- Prevention Card -->
<div style="position:absolute;top:142px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Prevention</p>
  <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
    <p style="font-size:13px;color:{C['dark']};margin:0;"><strong>Cesarean section</strong> delivery is recommended for all pregnancies complicated by <strong>primary genital HSV in labor</strong>.</p>
  </div>
</div>
<!-- Management Card -->
<div style="position:absolute;top:215px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Management</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">In Pregnancy</p>
      <p style="font-size:13px;color:{C['dark']};margin:0;"><strong>Acyclovir</strong></p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['coral']};margin:0 0 2px 0;">In Labor</p>
      <p style="font-size:13px;color:{C['dark']};margin:0;"><strong>Cesarean delivery</strong></p>
    </div>
  </div>
</div>
<!-- Summary Card -->
<div style="position:absolute;top:325px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['yellow']};">
  <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;"><strong>Key:</strong> HSV (dsDNA) → Sexual contact/transplacental/ascending → Painful vesicular lesions → 50% vertical transmission risk in primary infection → Neonatal herpes (disseminated/CNS) → Diagnose by PCR (IgM/IgG) → Prevent with C-section if primary HSV in labor → Treat with Acyclovir in pregnancy + C-section in labor.</p>
</div>'''
    write_slide(12, content, 12)

# ===================== RH INCOMPATIBILITY =====================

def slide_14_rh_definition():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">RH Incompatibility — Definition &amp; Etiology</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- ILOs -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:6px;padding:5px 12px;border-left:3px solid {C['teal']};">
  <p style="font-size:14px;font-weight:700;color:{C['dark']};margin:0 0 2px 0;">ILOs</p>
  <ul style="margin:0;padding-left:16px;font-size:12px;color:{C['dark']};line-height:1.4;">
    <li>Understand the definition of RH incompatibility and its etiology</li>
    <li>Describe how such clinical problem can be diagnosed during pregnancy</li>
    <li>Explain how to avoid the occurrence and how to manage it</li>
  </ul>
</div>
<!-- Definition Card -->
<div style="position:absolute;top:160px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Definition</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">It is an <strong>immunological disorder</strong> resulting in destruction of fetal red blood cells by antibodies which pass through placenta from maternal blood.</p>
</div>
<!-- Rh Genes Card -->
<div style="position:absolute;top:238px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Rh Genes</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
    There are <strong>5 main Rh genes</strong> (C, D, E, c, and e) — the most important gene is <strong>D</strong>.<br>
    Rh factor is a <strong>lipoprotein component</strong> on cell wall of red blood cells.<br>
    In human about <strong>85%</strong> of population are Rh positive and about <strong>15%</strong> are Rh negative.
  </p>
</div>
<!-- Etiology Card -->
<div style="position:absolute;top:340px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Etiology</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
    The problem occurs when <strong>Rh negative mother</strong> is pregnant from <strong>Rh positive husband</strong>.
  </p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:6px 0 0 0;">
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>Father homozygous (2DD):</strong><br>100% of babies Rh positive
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>Father heterozygous (Dd):</strong><br>50% Rh positive, 50% Rh negative
    </div>
  </div>
</div>'''
    write_slide(14, content, 14)

def slide_15_sensitization():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Sensitization &amp; Pathogenesis</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Sensitization card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Sensitization of Rh −ve Mother</p>
  <p style="font-size:12px;color:{C['dark']};margin:0 0 4px 0;">Occurs when Rh +ve red blood cells enter maternal circulation:</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;">
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"><strong>During pregnancy:</strong></div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"><strong>Before pregnancy:</strong></div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Placental separation (most important)</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Previous blood transfusion of Rh +ve blood</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Abortion</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Grandmother syndrome (in utero exposure)</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Ectopic pregnancy</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"></div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Vesicular mole</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"></div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Amniocentesis</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"></div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• External cephalic version</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"></div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};">• Antepartum hemorrhage</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 8px;font-size:11px;color:{C['dark']};"></div>
  </div>
</div>
<!-- Pathogenesis Card -->
<div style="position:absolute;top:310px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Pathogenesis</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
    Attachment of <strong>IgG</strong> to fetal RBCs causes hemolysis leading to:
  </p>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin:6px 0 0 0;">
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};text-align:center;">
      <strong style="color:{C['coral']};">Anemia</strong><br>→ Anemic heart failure<br>→ Generalized edema
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};text-align:center;">
      <strong style="color:{C['orange']};">Extramedullary hematopoiesis</strong><br>→ Hepatosplenomegaly<br>→ Portal hypertension, ascites, hypoproteinemia, edema
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};text-align:center;">
      <strong style="color:{C['yellow']};">Excess bilirubin</strong><br>→ Jaundice<br>→ Kernicterus risk
    </div>
  </div>
</div>'''
    write_slide(15, content, 15)

def slide_16_clinical_varieties():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Clinical Varieties</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Three clinical varieties -->
<div style="position:absolute;top:80px;left:50px;right:50px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">
  <!-- Hydrops fetalis -->
  <div style="background:{C['light_bg']};border-radius:8px;padding:10px 12px;border-top:4px solid {C['coral']};">
    <p style="font-size:14px;font-weight:700;color:{C['coral']};margin:0 0 4px 0;">1. Hydrops fetalis</p>
    <p style="font-size:11px;color:{C['dark']};margin:0;line-height:1.4;">
      <strong>Most severe form</strong> → IUFD due to anemic heart failure.
    </p>
    <ul style="margin:4px 0 0 0;padding-left:14px;font-size:10px;color:{C['dark']};line-height:1.3;">
      <li>Macrosomic baby</li>
      <li>Severe hemolytic anemia (cord Hb &lt; 8 gm/dL)</li>
      <li>Hepatosplenomegaly</li>
      <li>Generalized edema</li>
      <li>Ascites</li>
      <li>Scalp edema</li>
      <li>Hydrothorax</li>
      <li>Large edematous placenta</li>
    </ul>
  </div>
  <!-- Icterus gravis neonatorum -->
  <div style="background:{C['light_bg']};border-radius:8px;padding:10px 12px;border-top:4px solid {C['orange']};">
    <p style="font-size:14px;font-weight:700;color:{C['orange']};margin:0 0 4px 0;">2. Icterus Gravis Neonatorum</p>
    <p style="font-size:11px;color:{C['dark']};margin:0;line-height:1.4;">
      <strong>Commonest form</strong> — occurs after delivery.
    </p>
    <ul style="margin:4px 0 0 0;padding-left:14px;font-size:10px;color:{C['dark']};line-height:1.3;">
      <li>Nausea, vomiting</li>
      <li>Anemia (Hb 8–12 gm/dL)</li>
      <li>Jaundice</li>
      <li>Hepatosplenomegaly</li>
    </ul>
    <p style="font-size:10px;color:{C['coral']};margin:4px 0 0 0;font-weight:700;">⚠ Severe: Bilirubin crosses BBB → deposited in basal ganglia → <strong>Kernicterus</strong> (extrapyramidal effects + convulsions)</p>
    <p style="font-size:10px;color:{C['dark']};margin:2px 0 0 0;">Increased bilirubin → yellow staining of amniotic fluid, cord and vernix.</p>
  </div>
  <!-- Congenital hemolytic anemia -->
  <div style="background:{C['light_bg']};border-radius:8px;padding:10px 12px;border-top:4px solid {C['teal']};">
    <p style="font-size:14px;font-weight:700;color:{C['teal']};margin:0 0 4px 0;">3. Congenital Hemolytic Anemia</p>
    <p style="font-size:11px;color:{C['dark']};margin:0;line-height:1.4;">
      <strong>Mildest form</strong>
    </p>
    <ul style="margin:4px 0 0 0;padding-left:14px;font-size:10px;color:{C['dark']};line-height:1.3;">
      <li>Mild anemia at birth (Hb &lt; 14 gm/dL)</li>
      <li>Mild pallor</li>
      <li>Transient jaundice</li>
    </ul>
  </div>
</div>'''
    write_slide(16, content, 16)

def slide_17_investigations():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Investigations — Screening</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Screening Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">I. Screening — Assessment of Maternal and Paternal Blood</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">Initial Evaluation</p>
      <ul style="margin:0;padding-left:14px;font-size:12px;color:{C['dark']};line-height:1.4;">
        <li>Maternal blood group &amp; Rh</li>
        <li>Paternal blood group &amp; Rh</li>
      </ul>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['orange']};margin:0 0 2px 0;">If Rh −ve mother + Rh +ve father</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Perform <strong>indirect Coomb's test</strong> to detect maternal immunization.</p>
      <p style="font-size:12px;color:{C['coral']};margin:4px 0 0 0;font-weight:700;">Titer &gt; 1/16 (critical titer) → significant risk of sensitization &amp; stillbirth</p>
    </div>
  </div>
</div>
<!-- Diagnosis of affected fetus -->
<div style="position:absolute;top:230px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">II. Diagnosis of the Affected Fetus</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">During Pregnancy</p>
      <ul style="margin:0;padding-left:14px;font-size:12px;color:{C['dark']};line-height:1.4;">
        <li>Amniocentesis</li>
        <li>Cordocentesis</li>
        <li>Ultrasound</li>
      </ul>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['orange']};margin:0 0 2px 0;">After Delivery</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Cord blood sampling examined for:</p>
      <ul style="margin:2px 0 0 0;padding-left:14px;font-size:11px;color:{C['dark']};line-height:1.4;">
        <li>ABO group &amp; Rh typing</li>
        <li>Hemoglobin &amp; Hematocrit</li>
        <li>Reticulocytic count</li>
        <li>Direct Coomb's test</li>
        <li>Bilirubin level</li>
        <li>Serum protein level</li>
      </ul>
    </div>
  </div>
</div>'''
    write_slide(17, content, 17)

def slide_18_ultrasound():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Ultrasound &amp; Amniocentesis</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Ultrasound Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Ultrasound</p>
  <p style="font-size:13px;color:{C['dark']};margin:0 0 4px 0;">Preliminary before amniocentesis or cordocentesis.</p>
  <p style="font-size:13px;font-weight:700;color:{C['dark']};margin:0 0 2px 0;">Signs of Hydrops Fetalis:</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;margin:0 0 6px 0;">
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Scalp edema</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Increased amniotic fluid</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Placental thickening</div>
    <div style="background:{C['white']};border-radius:4px;padding:4px 8px;font-size:12px;color:{C['dark']};">• Hepatosplenomegaly</div>
  </div>
  <p style="font-size:13px;color:{C['dark']};margin:0;"><strong>Doppler on Middle Cerebral Artery (MCA)</strong> to predict fetal anemia by measuring its <strong>peak systolic velocity</strong>.</p>
</div>
<!-- Amniocentesis Card -->
<div style="position:absolute;top:280px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Serial Amniocentesis</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">
    <div style="background:{C['white']};border-radius:4px;padding:6px 8px;font-size:12px;color:{C['dark']};">
      <strong>Indications:</strong><br>
      • High maternal antibody titer to certify degree of fetal hemolysis<br>
      • Past history of hydrops fetalis or exchange transfusion
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 8px;font-size:12px;color:{C['dark']};">
      <strong>Value:</strong><br>
      Indirect assessment of fetal RBCs hemolysis by measuring <strong>amniotic fluid bilirubin</strong> by spectrophotometry plotted against gestational age → results placed on <strong>Liley chart</strong>
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:6px 8px;font-size:12px;color:{C['dark']};grid-column:span 2;">
      <strong>Timing:</strong><br>
      • Before 22–24 weeks if high antibody titer level<br>
      • Otherwise taken between 30–32 weeks<br>
      • If past history of IUFD → done 10 weeks before the expected time of this event
    </div>
  </div>
</div>'''
    write_slide(18, content, 18)

def slide_19_prophylactic():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Prophylactic Management</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Prophylactic Management Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Prophylactic Management</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">Blood Transfusion Policy</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">No Rh +ve blood is given to <strong>Rh negative mother</strong>.</p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['coral']};margin:0 0 2px 0;">Anti D Immunoglobulin</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Should be given to Rh −ve mothers <strong>after labor or abortion</strong>.</p>
    </div>
  </div>
</div>
<!-- Management During Pregnancy Card -->
<div style="position:absolute;top:210px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Management During Pregnancy</p>
  <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);margin-bottom:6px;">
    <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
      <strong>If titer &lt; 1/16 (unsensitized):</strong><br>
      No intervention required. At <strong>28 weeks</strong>, a standard dose of <strong>300 µg of anti D immunoglobulin</strong> is administered.
    </p>
  </div>
  <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
    <p style="font-size:13px;color:{C['dark']};margin:0 0 4px 0;">
      <strong>If indirect Coomb's test is above critical value:</strong><br>
      Do amniocentesis and put results on Liley curve, then manage accordingly:
    </p>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;">
      <div style="background:{C['light_bg']};border-radius:4px;padding:4px 6px;text-align:center;border:1px solid {C['teal']};">
        <p style="font-size:16px;font-weight:700;color:{C['teal']};margin:0;">Zone 1 (A)</p>
        <p style="font-size:10px;color:{C['dark']};margin:0;">Minimal/Absent<br>fetal affection<br><strong>Deliver at term</strong></p>
      </div>
      <div style="background:{C['light_bg']};border-radius:4px;padding:4px 6px;text-align:center;border:1px solid {C['orange']};">
        <p style="font-size:16px;font-weight:700;color:{C['orange']};margin:0;">Zone 2 (B)</p>
        <p style="font-size:10px;color:{C['dark']};margin:0;">Moderate affection<br>(low &amp; high B)<br><strong>Allow until AF bilirubin increases or 32 wks</strong></p>
      </div>
      <div style="background:{C['light_bg']};border-radius:4px;padding:4px 6px;text-align:center;border:1px solid {C['coral']};">
        <p style="font-size:16px;font-weight:700;color:{C['coral']};margin:0;">Zone 3 (C)</p>
        <p style="font-size:10px;color:{C['dark']};margin:0;">Severe affection<br>Risk of IUFD<br>within 7–10 days<br><strong>Deliver or transfuse</strong></p>
      </div>
    </div>
  </div>
</div>'''
    write_slide(19, content, 19)

def slide_20_mca_plasmapheresis():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">MCA Doppler, Plasmapheresis &amp; IUT</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- MCA Doppler Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Middle Cerebral Artery (MCA) Doppler</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li>Recently used as a <strong>noninvasive</strong> test to diagnose fetal anemia — <strong>eliminates the need for amniocentesis</strong></li>
    <li>Done every <strong>1 to 2 weeks</strong> to detect anemia</li>
    <li>May begin as early as <strong>16 to 18 weeks</strong></li>
    <li>The MCA peak systolic velocity of blood is <strong>increased in severe anemia</strong> due to decreased blood viscosity</li>
  </ul>
</div>
<!-- Plasmapheresis Card -->
<div style="position:absolute;top:215px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Maternal Plasmapheresis</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
    To <strong>wash antibodies</strong> from maternal circulation.<br>
    Indicated for <strong>severe cases before 24 weeks</strong> of pregnancy when intrauterine transfusion cannot be done.
  </p>
</div>
<!-- IUT Card -->
<div style="position:absolute;top:310px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Intrauterine Fetal Transfusion</p>
  <p style="font-size:13px;color:{C['dark']};margin:0 0 4px 0;"><strong>Timing:</strong> 24–32 weeks gestation</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};">
      <strong>Indications:</strong><br>
      • Severe fetal affection (low Hct, high zone 2 or zone 3 on Liley)<br>
      • 10 weeks earlier than previous IUFD
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};">
      <strong>Blood type:</strong> Group O, Rh −ve blood
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};">
      <strong>Procedures:</strong><br>
      • <strong>Intraperitoneal:</strong> needle into fetal peritoneal cavity (US-guided)<br>
      • <strong>Intravascular:</strong> into the umbilical vein
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};">
      <strong>Amount:</strong> (GA in weeks − 20) × 10<br>
      = 10 for each week after 20 weeks
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};grid-column:span 2;">
      <strong>Complications:</strong> Fetal injuries, bradycardia, cord hematoma, fetal death, chorioamnionitis
    </div>
  </div>
</div>'''
    write_slide(20, content, 20)

def slide_21_obstetric_postpartum():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Obstetric Management &amp; Postpartum Care</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Obstetric Management -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Obstetric Management</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li><strong>Route of delivery:</strong> Vaginal; CS is reserved for obstetric indication and compromised fetus</li>
    <li>After delivery, the cord is <strong>immediately clamped</strong> to avoid further passage of antibodies from the placenta and divided <strong>2–3 inches from the umbilicus</strong> to facilitate exchange transfusion</li>
    <li><strong>Manual removal of the placenta</strong> should be avoided</li>
  </ul>
</div>
<!-- Postpartum Card -->
<div style="position:absolute;top:215px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Postpartum Management</p>
  <p style="font-size:13px;color:{C['dark']};margin:0 0 4px 0;">Both the patient and infant are screened.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;">
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};text-align:center;">
      <strong>Neonate Rh D −ve</strong><br>
      Anti D immunoglobulin <strong>not necessary</strong>
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};text-align:center;">
      <strong>Neonate Rh D +ve<br>Mother antibody −ve</strong><br>
      Standard dose of anti D immunoglobulin given <strong>in the 1st 72 hours</strong>
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:11px;color:{C['dark']};text-align:center;">
      <strong>Neonate Rh D +ve<br>Mother antibody +ve</strong><br>
      No anti D immunoglobulin given.<br>
      Next pregnancy managed as <strong>Rh sensitized</strong>
    </div>
  </div>
</div>
<!-- Newborn Management -->
<div style="position:absolute;top:370px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Management of the Newborn</p>
  <ul style="margin:0;padding-left:18px;font-size:13px;color:{C['dark']};line-height:1.5;">
    <li><strong>Immediate cord clamping</strong></li>
    <li><strong>Admission to neonatal ICU</strong></li>
    <li>Cord blood sample for: blood group, Rh, hemoglobin, hematocrit, serum bilirubin, direct Coomb's test</li>
  </ul>
</div>'''
    write_slide(21, content, 21)

def slide_22_exchange_transfusion():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Exchange Transfusion</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Exchange Transfusion Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Exchange Transfusion</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['coral']};margin:0 0 2px 0;">Indications</p>
      <ul style="margin:0;padding-left:14px;font-size:12px;color:{C['dark']};line-height:1.4;">
        <li>Cord blood bilirubin &gt; <strong>5 mg%</strong></li>
        <li>Cord hemoglobin &lt; <strong>10 gm</strong></li>
        <li>Rapidly rising bilirubin in the <strong>first 24 hours</strong></li>
        <li>Clinical jaundice in the <strong>first 12 hours</strong></li>
        <li>Past history of severely affected baby</li>
      </ul>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">Aims</p>
      <ol style="margin:0;padding-left:18px;font-size:12px;color:{C['dark']};line-height:1.6;">
        <li>Correction of neonatal <strong>anemia</strong></li>
        <li>Removal of <strong>excess bilirubin</strong></li>
      </ol>
    </div>
  </div>
</div>
<!-- Phototherapy Card -->
<div style="position:absolute;top:250px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 4px 0;">Phototherapy &amp; Hydration</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">
    Used as <strong>adjuvant</strong> for exchange transfusion in cases of high but not toxic bilirubin.<br><br>
    <strong>Idea:</strong> Blue or blue-green light converts the <strong>unconjugated bilirubin</strong> into non-toxic, water-soluble isomers which are excreted in bile and urine without the need for hepatic conjugation.
  </p>
</div>
<!-- Phenobarbitone Card -->
<div style="position:absolute;top:380px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:14px;font-weight=700;color:{C['dark']};margin:0 0 2px 0;">Phenobarbitone</p>
  <p style="font-size:12px;color:{C['dark']};margin:0;line-height:1.4;">It is an <strong>enzyme inducer</strong> that increases activity of <strong>Glucuronyl transferase</strong> enzyme leading to increase bilirubin conjugation and excretion.</p>
</div>'''
    write_slide(22, content, 22)

def slide_23_abo_incompatibility():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">ABO Incompatibility</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- ABO Incompatibility Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Differences from Rh Incompatibility</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>Can affect the first baby</strong> — most group O women have Anti-A and Anti-B
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>IgM type antibodies</strong> — most Anti-A and Anti-B are IgM, so <strong>cannot cross the placenta</strong>
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>No need for amniocentesis</strong> or preterm delivery
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>Mild condition</strong> — rarely causes significant anemia
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      Affected infant typically has <strong>mild neonatal anemia and jaundice</strong> treated by phototherapy
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>Negative Coomb's test</strong>
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>No progressive course</strong>
    </div>
    <div style="background:{C['white']};border-radius:4px;padding:5px 8px;font-size:12px;color:{C['dark']};">
      <strong>More common</strong> than Rh incompatibility
    </div>
  </div>
</div>'''
    write_slide(23, content, 23)

def slide_24_causes_jaundice():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Causes of Neonatal Jaundice</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Causes Grid -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:12px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:16px;font-weight:700;color:{C['dark']};margin:0 0 8px 0;">Comprehensive List of Causes</p>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['teal']};">Physiological jaundice</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['coral']};">Rh incompatibility</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['orange']};">ABO incompatibility</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['teal']};">Congenital biliary atresia</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['orange']};">Breast milk jaundice</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['coral']};">Infections (hepatitis, STORCH)</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['orange']};">Congenital spherocytosis</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['teal']};">Infant of diabetic mother</div>
    <div style="background:{C['white']};border-radius:6px;padding:6px 10px;font-size:13px;color:{C['dark']};border-left:3px solid {C['coral']};">Drug induced</div>
  </div>
</div>'''
    write_slide(24, content, 24)

def slide_25_hydrops_fetalis():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:{C['white']};"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="6" height="540" fill="{C['teal']}" />
</svg>
<p style="position:absolute;top:20px;left:50px;font-size:32px;font-weight:700;color:{C['dark']};margin:0;">Hydrops Fetalis</p>
<div style="position:absolute;top:62px;left:50px;width:70px;height:3px;background:{C['teal']};border-radius:1.5px;"></div>
<!-- Definition Card -->
<div style="position:absolute;top:80px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:8px 16px;border-left:4px solid {C['teal']};">
  <p style="font-size:14px;font-weight:700;color:{C['dark']};margin:0 0 2px 0;">Definition</p>
  <p style="font-size:13px;color:{C['dark']};margin:0;line-height:1.4;">Accumulation of fluid in the <strong>interstitial tissue (skin)</strong> and <strong>two or more body cavities</strong> (pleural, pericardial effusions or ascites).</p>
</div>
<!-- Types Card -->
<div style="position:absolute;top:155px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['coral']};">
  <p style="font-size:15px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Types of Hydrops Fetalis</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap=8px;">
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['coral']};margin:0 0 2px 0;">Immune Hydrops</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Due to <strong>Rh and ABO isoimmunization</strong></p>
    </div>
    <div style="background:{C['white']};border-radius:6px;padding:8px 12px;border:1px solid rgba(38,70,83,0.1);">
      <p style="font-size:13px;font-weight:700;color:{C['teal']};margin:0 0 2px 0;">Non-Immune Hydrops</p>
      <p style="font-size:12px;color:{C['dark']};margin:0;">Due to various etiologies (see below)</p>
    </div>
  </div>
</div>
<!-- Non-Immune Causes -->
<div style="position:absolute;top:310px;left:50px;right:50px;background:{C['light_bg']};border-radius:8px;padding:10px 16px;border-left:4px solid {C['orange']};">
  <p style="font-size:14px;font-weight:700;color:{C['dark']};margin:0 0 6px 0;">Non-Immune Hydrops Fetalis — Etiologies</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;">
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Genetic:</strong> Aneuploidy syndromes</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Cardiovascular:</strong> AVSD, Hypoplastic Rt, cardiomyopathy, arrhythmia</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Pulmonary:</strong> Pulmonary lymphangiectasia</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Infections:</strong> CMV, Toxoplasma</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Renal/GI:</strong> Congenital nephrosis, gut duplication, malrotation</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Hematological:</strong> Alpha thalassemia, aplastic anemia</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Placental:</strong> AV fistula, chorioangiomas</div>
    <div style="background:{C['white']};border-radius:4px;padding:3px 6px;font-size:11px;color:{C['dark']};"><strong>Others:</strong> Twin-twin transfusion, liver cirrhosis, true knots of cord</div>
  </div>
</div>'''
    write_slide(25, content, 25)

def slide_26_summary():
    content = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:linear-gradient(135deg,{C['dark']} 0%,#1a3a3a 100%);"></div>
<svg style="position:absolute;top:0;left:0;width:960px;height:540px;" aria-hidden="true">
  <rect x="0" y="0" width="8" height="540" fill="{C['teal']}" />
  <circle cx="860" cy="460" r="140" fill="none" stroke="{C['teal']}" stroke-width="1" opacity="0.1" />
</svg>
<p style="position:absolute;top:24px;left:50px;font-size:32px;font-weight:700;color:{C['white']};margin:0;">Summary &amp; Key Takeaways</p>
<div style="position:absolute;top:62px;left:50px;width:60px;height:3px;background:{C['yellow']};border-radius:1.5px;"></div>
<div style="position:absolute;top:80px;left:50px;right:50px;bottom:50px;display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  <!-- Section 1 -->
  <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:12px 16px;border-left:3px solid {C['teal']};">
    <p style="font-size:16px;font-weight:700;color:{C['teal']};margin:0 0 6px 0;">Infectious Diseases in Pregnancy</p>
    <ul style="margin:0;padding-left:16px;font-size:12px;color:{C['white']};opacity:0.9;line-height:1.6;">
      <li><strong>TORCH</strong>: Toxoplasma, Others, Rubella, CMV, Herpes</li>
      <li><strong>Toxoplasmosis</strong>: T. gondii, undercooked meat, Spiramycin</li>
      <li><strong>Rubella</strong>: Highly teratogenic RNA virus, MMR vaccine, termination if 1st trimester</li>
      <li><strong>CMV</strong>: Most common congenital viral infection, US + PCR diagnosis</li>
      <li><strong>HSV</strong>: 50% vertical transmission in primary, Acyclovir, C-section in labor</li>
    </ul>
  </div>
  <!-- Section 2 -->
  <div style="background:rgba(255,255,255,0.08);border-radius:8px;padding:12px 16px;border-left:3px solid {C['yellow']};">
    <p style="font-size:16px;font-weight:700;color:{C['yellow']};margin:0 0 6px 0;">RH Incompatibility</p>
    <ul style="margin:0;padding-left:16px;font-size:12px;color:{C['white']};opacity:0.9;line-height:1.6;">
      <li>Rh −ve mother + Rh +ve fetus → isoimmunization</li>
      <li>Clinical forms: Hydrops fetalis, Icterus gravis, Hemolytic anemia</li>
      <li>Liley curve zones guide management (1=term, 2=32wks, 3=deliver/IUT)</li>
      <li>Anti D immunoglobulin prophylaxis (28 wks + postpartum)</li>
      <li>Exchange transfusion for severe jaundice</li>
      <li>ABO incompatibility: milder, more common, phototherapy</li>
    </ul>
  </div>
</div>
<!-- Bottom message -->
<div style="position:absolute;bottom:20px;left:50px;right:50px;text-align:center;border-top:1px solid rgba(255,255,255,0.1);padding-top:8px;">
  <p style="font-size:13px;color:{C['white']};opacity:0.5;margin:0;">Comprehensive Obstetric Reference — All content preserved from source materials</p>
</div>'''
    write_slide(26, content, 26)


# ===================== GENERATE ALL SLIDES =====================

if __name__ == "__main__":
    print("Generating slides...")
    
    # Cover
    print("Slide 01: Cover")
    cover_page()
    
    # TOC
    print("Slide 02: Table of Contents")
    toc()
    
    # Section Divider 1
    print("Slide 03: Section Divider - Infectious Diseases")
    section_divider(3, 1, "Infectious Diseases with Pregnancy", "TORCH Infections • Toxoplasmosis • Rubella • Cytomegalovirus • Herpes Simplex")
    
    # Content slides
    print("Slide 04: ILOs & Background")
    slide_04_ilos_background()
    
    print("Slide 05: Toxoplasmosis")
    slide_05_toxoplasmosis()
    
    print("Slide 06: Toxoplasmosis - Investigations & Treatment")
    slide_06_toxoplasmosis_2()
    
    print("Slide 07: Rubella")
    slide_07_rubella()
    
    print("Slide 08: Rubella - Diagnosis, Prevention & Treatment")
    slide_08_rubella_diagnosis()
    
    print("Slide 09: CMV")
    slide_09_cmv()
    
    print("Slide 10: CMV - Diagnosis & Management")
    slide_10_cmv_diagnosis()
    
    print("Slide 11: Herpes Simplex")
    slide_11_herpes()
    
    print("Slide 12: Herpes Simplex - Diagnosis, Prevention & Management")
    slide_12_herpes_2()
    
    # Section Divider 2
    print("Slide 13: Section Divider - RH Incompatibility")
    section_divider(13, 2, "RH Incompatibility", "Definition • Etiology • Pathogenesis • Management • ABO Incompatibility • Hydrops Fetalis")
    
    print("Slide 14: RH - Definition & Etiology")
    slide_14_rh_definition()
    
    print("Slide 15: RH - Sensitization & Pathogenesis")
    slide_15_sensitization()
    
    print("Slide 16: RH - Clinical Varieties")
    slide_16_clinical_varieties()
    
    print("Slide 17: RH - Investigations & Screening")
    slide_17_investigations()
    
    print("Slide 18: RH - Ultrasound & Amniocentesis")
    slide_18_ultrasound()
    
    print("Slide 19: RH - Prophylactic Management & Management During Pregnancy")
    slide_19_prophylactic()
    
    print("Slide 20: RH - MCA Doppler, Plasmapheresis & IUT")
    slide_20_mca_plasmapheresis()
    
    print("Slide 21: RH - Obstetric Management & Postpartum")
    slide_21_obstetric_postpartum()
    
    print("Slide 22: RH - Exchange Transfusion")
    slide_22_exchange_transfusion()
    
    print("Slide 23: ABO Incompatibility")
    slide_23_abo_incompatibility()
    
    print("Slide 24: Causes of Neonatal Jaundice")
    slide_24_causes_jaundice()
    
    print("Slide 25: Hydrops Fetalis")
    slide_25_hydrops_fetalis()
    
    print("Slide 26: Summary & Closing")
    slide_26_summary()
    
    print("\n✅ All 26 slides generated successfully!")
