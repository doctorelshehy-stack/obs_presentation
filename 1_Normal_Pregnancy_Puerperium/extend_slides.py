import os

# ─── Color palette ───
C = {
    'bg': '#264653',
    'teal': '#2a9d8f',
    'gold': '#e9c46a',
    'org': '#f4a261',
    'coral': '#e76f51',
    'white': '#ffffff',
    'light': '#edf6f9',
}
# Direct color hexes for use in inner strings
TEAL = '#2a9d8f'
GOLD = '#e9c46a'
ORG = '#f4a261'
CORAL = '#e76f51'

def badge(num):
    return f'''<svg style="position:absolute;right:32px;bottom:24px;width:40px;height:32px;z-index:100;" aria-hidden="true">
  <rect x="0" y="0" width="40" height="32" rx="4" fill="#2a9d8f"/>
  <text x="20" y="22" font-family="Times New Roman,serif" font-size="16" font-weight="700" fill="#ffffff" text-anchor="middle">{num}</text>
</svg>'''

def slide_html(content_body, page_num=None):
    b = badge(page_num) if page_num else ""
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
function scaleSlide(){{const s=document.querySelector('.slide-content');if(!s)return;const sx=window.innerWidth/960;const sy=window.innerHeight/540;const sc=Math.min(sx,sy);s.style.width='960px';s.style.height='540px';s.style.transform='scale('+sc+')';s.style.transformOrigin='center center';s.style.flexShrink='0';}}
window.addEventListener('load',scaleSlide);window.addEventListener('resize',scaleSlide);
</script>
</head>
<body>
<div class="slide-content" style="width:960px;height:540px;background:#264653;font-family:'Times New Roman',serif;overflow:hidden;">
{content_body}
{b}
</div>
</body>
</html>'''

def write_slide(num, body, with_badge=True):
    path = f'slide-{num:02d}.html'
    with open(path, 'w') as f:
        f.write(slide_html(body, num if with_badge else None))
    print(f'  slide-{num:02d}.html')

def ulist(items, size='14px'):
    lis = "\n".join(f"      <li>{item}</li>" for item in items)
    return f'''<ul style="margin:0;padding-left:18px;color:#ffffff;font-size:{size};line-height:1.5;">
{lis}
</ul>'''

def card(title, content, accent=TEAL, title_color=GOLD, font_size='18px', body_size='14px'):
    return f'''<div style="background:rgba(42,157,143,0.1);border-radius:8px;padding:12px;border-left:4px solid {accent};margin-bottom:8px;">
  <p style="font-size:{font_size};font-weight:700;color:{title_color};margin:0 0 4px 0;">{title}</p>
  <div style="font-size:{body_size};color:#ffffff;margin:0;line-height:1.4;">{content}</div>
</div>'''

def card_no_title(content, accent=TEAL, body_size='14px'):
    return f'''<div style="background:rgba(42,157,143,0.1);border-radius:8px;padding:12px;border-left:4px solid {accent};margin-bottom:8px;">
  <div style="font-size:{body_size};color:#ffffff;margin:0;line-height:1.4;">{content}</div>
</div>'''

def two_col(c1, c2):
    return f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:6px;">\n  {c1}\n  {c2}\n</div>'

def warning_box(text):
    return f'''<div style="background:rgba(231,111,81,0.15);border-radius:6px;padding:8px 14px;border:1px solid #e76f51;margin-bottom:6px;">
  <p style="font-size:13px;color:#edf6f9;margin:0;"><b style="color:#e9c46a;">Warning:</b> {text}</p>
</div>'''

def activity_box(text):
    return f'''<div style="background:rgba(231,111,81,0.15);border-radius:6px;padding:6px 12px;border:1px solid #e76f51;margin-bottom:4px;">
  <p style="font-size:12px;color:#edf6f9;margin:0;"><b style="color:#e9c46a;">Student Activity:</b> {text}</p>
</div>'''

def content_slide(title, body_elements, title_color='#ffffff', accent_color=TEAL, top_offset=70):
    cards = "\n".join(body_elements)
    return f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:#264653;"></div>
<div style="position:absolute;top:22px;left:60px;z-index:10;">
  <p style="font-size:30px;color:{title_color};font-weight:700;margin:0;">{title}</p>
  <div style="width:60px;height:4px;background:{accent_color};margin:6px 0 10px 0;"></div>
</div>
<div style="position:absolute;top:{top_offset}px;left:55px;right:55px;bottom:50px;z-index:10;overflow:hidden;">
  {cards}
</div>'''

def section_divider(num, title, subtitle=""):
    sub = f'<p style="font-size:20px;color:#e9c46a;margin:8px 0 0 0;">{subtitle}</p>' if subtitle else ''
    return f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:#264653;"></div>
<div style="position:absolute;top:0;right:0;width:400px;height:540px;background:#2a9d8f;opacity:0.15;"></div>
<div style="position:absolute;top:140px;left:80px;z-index:10;">
  <p style="font-size:96px;font-weight:700;color:#2a9d8f;margin:0;line-height:1;">{num}</p>
  <div style="width:80px;height:4px;background:#e9c46a;margin:12px 0 15px 0;"></div>
  <p style="font-size:36px;font-weight:700;color:#ffffff;margin:0;">{title}</p>
  {sub}
</div>'''

print("=" * 60)
print("UPDATING TOC (slide-02.html)")
print("=" * 60)

# ─── New TOC with all 8 chapters ───
toc_items = [
    ("01", "Physiology of Reproduction"),
    ("02", "Maternal Adaptation to Pregnancy"),
    ("03", "Diagnosis of Pregnancy"),
    ("04", "Antenatal Care"),
    ("20", "Female Pelvis"),
    ("21", "Fetal Skull"),
    ("38", "Normal & Abnormal Puerperium"),
    ("46", "Assessment of Fetal Well-being"),
]
rows = ""
for num, title in toc_items:
    rows += f'''<div style="display:flex;align-items:center;gap:12px;padding:9px 12px;background:rgba(42,157,143,0.15);border-radius:4px;border-left:3px solid #2a9d8f;">
      <span style="font-size:20px;font-weight:700;color:#e9c46a;min-width:30px;">{num}</span>
      <span style="font-size:16px;color:#ffffff;">{title}</span>
    </div>\n'''

toc_html = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:#264653;"></div>
<div style="position:absolute;top:18px;left:60px;z-index:10;">
  <p style="font-size:30px;color:#ffffff;font-weight:700;margin:0;">Table of Contents</p>
  <div style="width:60px;height:4px;background:#2a9d8f;margin:6px 0 18px 0;"></div>
</div>
<div style="position:absolute;top:72px;left:55px;right:55px;bottom:50px;z-index:10;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 30px;">
    {rows}
  </div>
</div>'''

write_slide(2, toc_html)
print()

print("=" * 60)
print("NEW CHAPTERS (slides 39+)")
print("=" * 60)

new_slides = []  # list of (body, with_badge)

# ═══════════════════════════════════════════
# CHAPTER 20: FEMALE PELVIS
# ═══════════════════════════════════════════

# Slide 39: Section Divider 20
new_slides.append((section_divider("20", "Female Pelvis", "Pelvic Diameters · Pelvic Shapes · Obstetric Axis"), True))

# Slide 40: ILOs
ilos20_body = two_col(
    card("ILOs", ulist([
        'Understand the components of true pelvis',
        'Describe various diameters of different parts of the pelvis']), GOLD, GOLD, '18px', '14px'),
    card("ILOs (cont.)", ulist([
        'Describe variable variants of the pelvis']), GOLD, GOLD, '18px', '14px')
)
new_slides.append((content_slide("Intended Learning Objectives", [ilos20_body], accent_color=GOLD), True))

# Slide 41: Pelvic Inlet Diameters
inlet_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Anteroposterior Diameters", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <b style="color:{GOLD};">Anatomical (True) Conjugate</b> = 11 cm<br>
    <span style="color:{TEAL};font-size:12px;">Tip of sacral promontory → upper border symphysis pubis</span><br>
    <b style="color:{GOLD};">Obstetric Conjugate</b> = 10.5 cm ← <b>shortest AP</b><br>
    <span style="color:{TEAL};font-size:12px;">Tip of sacral promontory → most bulging point on back of symphysis (1 cm below upper border)</span><br>
    <b style="color:{GOLD};">Diagonal Conjugate</b> = 12.5 cm<br>
    <span style="color:{TEAL};font-size:12px;">Tip of sacral promontory → lower border symphysis pubis</span>
  </div>''', TEAL, GOLD, '17px', '13px')}
  {card("Transverse & Oblique Diameters", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <b style="color:{GOLD};">Transverse Diameters:</b><br>
    • Anatomical transverse = <b>13 cm</b> (largest diameter in pelvis)<br>
    <span style="font-size:12px;">Between farthest points on iliopectineal lines, 4 cm anterior to promontory, 7 cm behind symphysis</span><br>
    • Obstetric transverse = <b>12 cm</b><br>
    <span style="font-size:12px;">Bisects the true conjugate, slightly shorter than anatomical</span><br><br>
    <b style="color:{GOLD};">Oblique Diameters:</b><br>
    • Right oblique = <b>12 cm</b> (R sacroiliac → L iliopectineal eminence)<br>
    • Left oblique = <b>12 cm</b> (L sacroiliac → R iliopectineal eminence)<br>
    • Sacro-cotyloid = <b>9.5 cm</b>
  </div>''', GOLD, GOLD, '17px', '13px')}
</div>'''
new_slides.append((content_slide("Pelvic Inlet Diameters", [inlet_body], top_offset=72), True))

# Slide 42: Pelvic Cavity & Outlet
cav_out_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Pelvic Cavity", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    Space between symphysis pubis and the sacrum.<br><br>
    <b>Boundaries:</b><br>
    • <b>Roof:</b> Plane of pelvic brim<br>
    • <b>Floor:</b> Plane of least pelvic dimension<br>
    • <b>Anterior:</b> Shorter symphysis pubis<br>
    • <b>Posterior:</b> Longer sacrum<br>
    Like a circle — half measured about <b>12 cm</b>
  </div>''', TEAL, GOLD, '17px', '13px')}
  {card("Pelvic Outlet", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <b>Anatomical outlet</b> — lozenge-shaped:<br>
    <span style="font-size:12px;">Lower border symphysis · Pubic arch · Ischial tuberosities · Sacrotuberous & sacrospinous ligaments · Tip of coccyx</span><br><br>
    <b>Obstetric outlet</b> — segment:<br>
    <span style="font-size:12px;">Roof: plane of least pelvic dimension · Floor: anatomical outlet · Anterior: lower border symphysis · Posterior: coccyx · Lateral: ischial spines</span><br><br>
    <b>AP diameters:</b><br>
    • Anatomical = <b>11 cm</b> (coccyx → lower border symphysis)<br>
    • Obstetric = <b>13 cm</b> (sacrum → lower border symphysis, as coccyx moves back in 2nd stage)<br><br>
    <b>Transverse diameters:</b><br>
    • Bituberous = <b>11 cm</b><br>
    • Interspinous = <b>10.5 cm</b>
  </div>''', GOLD, GOLD, '17px', '13px')}
</div>'''
new_slides.append((content_slide("Pelvic Cavity & Outlet", [cav_out_body], top_offset=72), True))

# Slide 43: Obstetric Axis & Pelvic Types
axis_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Obstetric Axis", ulist([
    'Imaginary line representing the path of the head during labor',
    '<b>J-shaped</b> — passes downwards & backwards along axis of inlet till ischial spines, then downwards & forwards along axis of outlet']), TEAL, GOLD, '17px', '13px')}
  {card("Types of Pelvis (Caldwell-Moloy)", f'''<div style="font-size:13px;color:#ffffff;line-height:1.5;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;">
      <div><b>Gynecoid</b> (50%)</div><div>Classic female, round brim</div>
      <div><b>Android</b> (20%)</div><div>Male type, heart-shaped brim</div>
      <div><b>Anthropoid</b> (25%)</div><div>Long oval brim</div>
      <div><b>Platypelloid</b> (5%)</div><div>Flat, kidney-shaped brim</div>
    </div>
  </div>''', CORAL, GOLD, '17px', '13px')}
</div>
{card("Criteria of Adequate (Gynecoid) Pelvis", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px 20px;">
      <div>Forepelvis (brim): Round</div><div>Diagonal conjugate: ≥11.5 cm</div>
      <div>Symphysis: Average, parallel to sacrum</div><div>Sacrum: Hollow, average inclination</div>
      <div>Side walls: Straight</div><div>Ischial spines: Blunt</div>
      <div>Interspinous diameter: ≥10 cm</div><div>Sacrosciatic notch: 2.5-3 finger-breadths</div>
      <div>Subpubic angle: 90° (2 FB)</div><div>Bituberous: >8 cm</div>
      <div>Coccyx: Mobile</div><div>AP outlet: ≥11 cm</div>
    </div>
  </div>''', TEAL, GOLD, '16px', '12px')}'''
new_slides.append((content_slide("Obstetric Axis & Pelvic Types", [axis_body], top_offset=72), True))

# Slide 44: Student Activity 20
sa20_body = f'''{activity_box("Each student is requested to attend the departmental skill lab with the tutor of bedside part of the clinical round in order to revise different diameters of the pelvic inlet, cavity, and outlet on a pelvic manikin.")}
<p style="font-size:13px;color:#ffffff;margin:4px 0 0 0;"><b style="color:{GOLD};">Questions:</b> <span style="color:{TEAL};">https://forms.gle/gxxaMfhV6xd6Wjen8</span></p>'''
new_slides.append((content_slide("Student Activity — Female Pelvis", [sa20_body]), True))

# ═══════════════════════════════════════════
# CHAPTER 21: FETAL SKULL
# ═══════════════════════════════════════════

# Slide 45: Section Divider 21
new_slides.append((section_divider("21", "Fetal Skull", "Bones · Sutures · Fontanelles · Diameters"), True))

# Slide 46: ILOs
ilos21_body = two_col(
    card("ILOs", ulist([
        'Understand the components of fetal skull',
        'Differentiate between anterior and posterior fontanelle']), GOLD, GOLD, '18px', '14px'),
    card("ILOs (cont.)", ulist([
        'Describe various diameters of fetal skull']), GOLD, GOLD, '18px', '14px')
)
new_slides.append((content_slide("Intended Learning Objectives", [ilos21_body], accent_color=GOLD), True))

# Slide 47: Bones, Sutures & Fontanelles
skull_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Parts & Bones", ulist([
    '3 parts: <b>Base</b> (chin→foramen magnum), <b>Face</b> (chin→root of nose), <b>Vault</b> (3 regions)',
    '<b>2 frontal bones</b> — separated by frontal suture',
    '<b>2 parietal bones</b> — separated by sagittal suture',
    '<b>Occipital bone</b> — separated by lambdoid suture',
    '<b>Coronal suture:</b> frontal from parietal',
    '<b>Temporal suture:</b> parietal from temporal',
    '<b>Vertex:</b> bounded by ant. fontanelle + coronal suture, post. fontanelle + lambdoid, lines through parietal eminences',
    '<b>Brow:</b> from nose/supra-orbital ridges to ant. fontanelle + coronal suture']), TEAL, GOLD, '17px', '12px')}
  {card("Fontanelles", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <b>6 areas</b> at meeting of sutures. 4 temporal (no obstetric importance).<br>
    <b>Anterior (Bregma)</b> & <b>Posterior (Lambda)</b> important to diagnose:<br>
    • Vertex presentation · Position of occiput · Degree of head flexion<br><br>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;">
      <div><b style="color:{GOLD};">Anterior (Bregma)</b></div><div><b style="color:{GOLD};">Posterior (Lambda)</b></div>
      <div>Large, lozenge-shaped</div><div>Small, triangular</div>
      <div>Floor: membranous</div><div>Floor: bony</div>
      <div>Surrounded by 4 bones</div><div>Surrounded by 3 bones</div>
      <div>(2 frontal + 2 parietal)</div><div>(2 parietal + occipital)</div>
      <div>Ossified 1.5 yrs after birth</div><div>Ossified at full term</div>
      <div>Bones not overlapping during moulding</div><div>Bones overlapping during moulding</div>
    </div>
  </div>''', GOLD, GOLD, '17px', '12px')}
</div>'''
new_slides.append((content_slide("Fetal Skull — Bones, Sutures & Fontanelles", [skull_body], top_offset=72), True))

# Slide 48: Longitudinal Diameters
long_diam_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Suboccipito-bregmatic = 9.5 cm", ulist([
    'From below occipital protuberance → center of bregma',
    'Engagement diameter in <b>occipito-anterior with complete flexion</b>'], '13px'), TEAL, GOLD, '16px', '13px')}
  {card("Suboccipito-frontal = 10 cm", ulist([
    'From below occipital protuberance → anterior end of bregma',
    'Engagement diameter in <b>occipito-anterior with incomplete flexion</b>',
    'Distends vulva in OA if head extends after crowning'], '13px'), GOLD, GOLD, '16px', '13px')}
  {card("Occipito-frontal = 11.5 cm", ulist([
    'From occipital protuberance → root of nose',
    'Engagement diameter in <b>occipito-posterior</b> position',
    'Distends vulva in face-to-pubis delivery',
    'Distends vulva if head extends before crowning in OA'], '13px'), ORG, GOLD, '16px', '13px')}
  {card("Submento-bregmatic = 9.5 cm", ulist([
    'From junction of chin & neck → center of bregma',
    'Engagement diameter in <b>face presentation</b> (complete extension)'], '13px'), TEAL, GOLD, '16px', '13px')}
</div>'''
new_slides.append((content_slide("Fetal Skull — Longitudinal Diameters (1)", [long_diam_body], top_offset=72), True))

# Slide 49: Longitudinal Diameters 2 + Transverse + Activity
diam2_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;">
  {card("Submento-vertical = 11.5 cm", ulist([
    'From junction of chin & neck → vertical point on sagittal suture',
    'Engagement in <b>incompletely extended face</b>',
    'Distends vulva during face delivery'], '12px'), ORG, GOLD, '15px', '12px')}
  {card("Mento-vertical = 13.5 cm", ulist([
    'From tip of chin → vertical point',
    'Engagement in <b>brow presentation</b>',
    'Longer than largest pelvic brim diameter → <b>cannot enter pelvis</b>'], '12px'), CORAL, GOLD, '15px', '12px')}
  {card("Transverse Diameters", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    <b>Biparietal</b> = 9.5 cm<br>
    <span style="font-size:11px;">Between 2 parietal eminences</span><br>
    <b>Subparietal-supraparietal</b> = 9 cm<br>
    <span style="font-size:11px;">Below one parietal eminence → above opposite. Engagement in asynclitism</span><br>
    <b>Bitemporal</b> = 8 cm<br>
    <span style="font-size:11px;">Between anterior ends of temporal sutures</span><br>
    <b>Bimastoid</b> = 7.5 cm<br>
    <span style="font-size:11px;">Between tips of 2 mastoid processes</span>
  </div>''', CORAL, GOLD, '15px', '12px')}
</div>
{activity_box("Each student is requested to go to skill lab to check and evaluate by himself (herself) the various components and diameters of fetal skull.")}
<p style="font-size:13px;color:#ffffff;margin:2px 0 0 0;"><b style="color:{GOLD};">Questions:</b> <span style="color:{TEAL};">https://forms.gle/fvNnbzfYgKicAcZSA</span></p>'''
new_slides.append((content_slide("Fetal Skull — Diameters (2) & Student Activity", [diam2_body], top_offset=72), True))

# ═══════════════════════════════════════════
# CHAPTER 38: NORMAL AND ABNORMAL PUERPERIUM
# ═══════════════════════════════════════════

# Slide 50: Section Divider 38
new_slides.append((section_divider("38", "Normal & Abnormal Puerperium", "Involution · Puerperal Pyrexia · Subinvolution"), True))

# Slide 51: ILOs + Definition + Genital tract changes
puerp1_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("ILOs & Definition", f'''<p style="font-size:13px;color:#ffffff;margin:0 0 4px 0;"><b style="color:{GOLD};">ILOs:</b></p>
  <ul style="margin:0;padding-left:18px;color:#ffffff;font-size:12px;line-height:1.3;">
    <li>Understand definition of normal & abnormal puerperium</li>
    <li>Describe genital & non-genital body changes during puerperium</li>
    <li>Explain etiology of uterine subinvolution & puerperal pyrexia and their management</li>
  </ul>
  <p style="font-size:13px;color:#ffffff;margin:4px 0 0 0;"><b style="color:{GOLD};">Definition:</b></p>
  <p style="font-size:13px;color:#ffffff;margin:0;line-height:1.3;">Time from delivery till <b>6 weeks (42 days)</b> postpartum, during which most changes of pregnancy, labor, and delivery have resolved and body reverts to non-pregnant state.</p>''', GOLD, GOLD, '17px', '13px')}
  {card("Genital Tract Changes", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <b style="color:{GOLD};">Uterus:</b><br>
    <b>Weight:</b> Immediately: 1000g → 1wk: 500g → 2wks: 250g → 6wks: 60-80g<br>
    <b>Level:</b> Immediately at umbilicus → by 6 wks reaches non-pregnant size<br>
    <span style="font-size:12px;">Fundus descends ~1 cm/day. After 7-10 days no longer palpable abdominally.</span><br><br>
    <b style="color:{GOLD};">Cervix:</b> After 1wk: external os closed (finger cannot be easily introduced)<br><br>
    <b style="color:{GOLD};">Vagina:</b> Diminishes in size, rugae reappear (non-breastfeeding)<br><br>
    <b style="color:{GOLD};">Vulva & perineum:</b> Swelling & engorgement gone within 1-2 weeks<br><br>
    <b style="color:{GOLD};">Ovary:</b> Ovulation/menses return:<br>
    • Non-lactating: 1.5-2 months<br>
    • Lactating: 6 months or earlier
  </div>''', TEAL, GOLD, '17px', '12px')}
</div>'''
new_slides.append((content_slide("Puerperium — Definition & Genital Changes", [puerp1_body], top_offset=70), True))

# Slide 52: General Body Changes
gen_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  {card("Pulse & Temperature", ulist([
    '<b>Pulse:</b> Normal. Tachycardia (>100 b/m) → infection or anemia',
    '<b>Temperature:</b> May ↑ in 1st 24 hrs (muscular effort), but <38°C and <24 hrs'], '13px'), TEAL, GOLD, '16px', '13px')}
  {card("Breasts & After Pains", ulist([
    '<b>Breasts:</b> Larger, firmer, heavier. Colostrum released first 2-3 days after delivery',
    '<b>After pains:</b> Painful uterine contractions in early puerperium, ↑ with suckling (oxytocin release)'], '13px'), GOLD, GOLD, '16px', '13px')}
  {card("Abdominal Wall & Urinary", ulist([
    '<b>Abdominal wall:</b> Gradual regain of tone. Striae become white (albicans)',
    '<b>Urinary tract:</b> Increased diuresis after delivery'], '13px'), ORG, GOLD, '16px', '13px')}
  {card("GIT & Blood", ulist([
    '<b>Constipation:</b> Due to intestinal atony, abdominal laxity, decreased fluid intake',
    '<b>Blood:</b> ↑ Thrombosis risk (first 2 wks, especially with ↓ fluid). Hematological changes gradually reversed'], '13px'), CORAL, GOLD, '16px', '13px')}
</div>'''
new_slides.append((content_slide("General Body Changes in Puerperium", [gen_body], top_offset=72), True))

# Slide 53: Management of Normal Puerperium
mgmt_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  {card("Immediate Postpartum Care", ulist([
    '<b>Vital signs:</b> Frequent observation',
    '<b>Uterus:</b> Massage + monitoring vaginal bleeding every 15 min for ≥1 hr',
    '<b>Position:</b> Semi-sitting → encourages lochia drainage',
    '<b>Ambulation:</b> Movement + breathing exercises → minimize DVT risk',
    '<b>Diet:</b> 2 hrs after uncomplicated vaginal delivery, no dietary restriction'], '13px'), TEAL, GOLD, '16px', '12px')}
  {card("Ongoing Care", ulist([
    '<b>Perineal care:</b> Wash with antiseptic lotion. Add local antibiotic if stitches',
    '<b>Breast care:</b> Before each feed, wash nipple & areola with warm water & soap',
    '<b>Bowel care:</b> Green vegetables & fruits to avoid constipation',
    '<b>Newborn care:</b> If mother Rh-ve & baby Rh+ve → anti-D within 1st 72 hrs',
    '<b>Pelvic floor exercise:</b> Alternating contraction & relaxation',
    '<b>Future contraception:</b> Counsel mother before leaving hospital'], '13px'), GOLD, GOLD, '16px', '12px')}
</div>'''
new_slides.append((content_slide("Management of Normal Puerperium", [mgmt_body], top_offset=72), True))

# Slide 54: Uterine Subinvolution + Puerperal Pyrexia + Activity
abn_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Uterine Subinvolution", f'''<p style="font-size:13px;color:#ffffff;margin:0 0 4px 0;"><b style="color:{GOLD};">Definition:</b> Uterus did not regress to pre-pregnancy size by end of puerperium.</p>
  <p style="font-size:13px;color:#ffffff;margin:0 0 4px 0;"><b style="color:{GOLD};">Etiology:</b></p>
  <ul style="margin:0;padding-left:18px;color:#ffffff;font-size:12px;line-height:1.3;">
    <li>Retained placental fragments</li>
    <li>Infection</li>
    <li>Antepartum overdistension (e.g. multiple pregnancy)</li>
    <li>Non-lactating women</li>
  </ul>
  <p style="font-size:13px;color:#ffffff;margin:4px 0 0 0;"><b style="color:{GOLD};">Treatment:</b> Treat cause + ecbolics & antibiotics</p>''', CORAL, GOLD, '16px', '12px')}
  {card("Puerperal Pyrexia", f'''<p style="font-size:13px;color:#ffffff;margin:0 0 4px 0;"><b style="color:{GOLD};">Definition:</b> Temperature ≥38°C lasting ≥24 hrs during first 10 days of puerperium.</p>
  <p style="font-size:13px;color:#ffffff;margin:0 0 4px 0;"><b style="color:{GOLD};">Causes:</b></p>
  <ul style="margin:0;padding-left:18px;color:#ffffff;font-size:12px;line-height:1.3;">
    <li>Milk engorgement (most common)</li>
    <li>Puerperal sepsis (most serious)</li>
    <li>Urinary tract infection</li>
    <li>Breast infection</li>
    <li>Respiratory infection</li>
    <li>Deep venous thrombosis</li>
    <li>Intercurrent febrile illness (e.g. typhoid)</li>
  </ul>
  <p style="font-size:13px;color:{CORAL};margin:4px 0 0 0;font-weight:700;">Any case of puerperal pyrexia should be considered puerperal infection (sepsis) until proved otherwise.</p>''', CORAL, GOLD, '16px', '12px')}
</div>
{activity_box("The students are requested to attend outpatient clinic in order to check with the clinic specialist the physiological changes which occur in the puerperium of postpartum attendant women.")}
<p style="font-size:13px;color:#ffffff;margin:2px 0 0 0;"><b style="color:{GOLD};">Questions:</b> <span style="color:{TEAL};">https://forms.gle/khJQEkyMMA64rRV28</span></p>'''
new_slides.append((content_slide("Uterine Subinvolution & Puerperal Pyrexia", [abn_body], top_offset=72), True))

# ═══════════════════════════════════════════
# CHAPTER 46: ASSESSMENT OF FETAL WELL-BEING
# ═══════════════════════════════════════════

# Slide 55: Section Divider 46
new_slides.append((section_divider("46", "Assessment of Fetal Well-being", "NST · CST · CTG · BPP · Doppler"), True))

# Slide 56: ILOs
ilos46_body = card("ILOs", ulist([
    'Describe various fetal well-being tests regarding the indications, procedure steps and interpretation']), GOLD, GOLD, '18px', '14px')
new_slides.append((content_slide("Intended Learning Objectives", [ilos46_body], accent_color=GOLD), True))

# Slide 57: Fetal Movement Counting & NST
nst_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Fetal Movement Counting", ulist([
    '<b>Timing:</b> After 30 weeks\' gestation',
    '<b>Method:</b> Mother counts kicks in 3 hrs during 12-hr period (9am-9pm) — 1 hr morning, 1 hr midday, 1 hr evening',
    'Multiply by 4 to get kicks/12 hrs',
    'If <b>&lt;10 kicks</b> → needs Non-Stress Test (NST)'], '13px'), TEAL, GOLD, '17px', '13px')}
  {card("Non-Stress Test (NST)", ulist([
    '<b>Purpose:</b> FHR acceleration in response to fetal movement (sign of fetal health)',
    '<b>Timing:</b> After 32 weeks\' gestation',
    '<b>Method:</b> Doppler-detected FHR acceleration coincident with fetal movements perceived by mother',
    '<b>Normal (reactive):</b> ≥2 accelerations ≥15 bpm above baseline, lasting ≥15 sec, within 20 min',
    '<b>Abnormal:</b> Baseline oscillates &lt;5 bpm',
    '<b>Frequency:</b> Every 7 days. More frequent for post-term, DM type 1, FGR, hypertension'], '13px'), GOLD, GOLD, '17px', '13px')}
</div>'''
new_slides.append((content_slide("Fetal Movement Counting & NST", [nst_body], top_offset=72), True))

# Slide 58: Contraction Stress Test (CST)
cst_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Contraction Stress Test (CST)", ulist([
    'Evaluates FHR in response to uterine contractions (induced by breast stimulation or oxytocin infusion)',
    'Once <b>3 contractions in 10 min</b> occur, FHR is observed for reactivity and decelerations'], '14px'), TEAL, GOLD, '17px', '14px')}
  {card("Interpretation", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    <div style="display:grid;grid-template-columns:1fr 2fr;gap:2px;">
      <div><b style="color:{TEAL};">Negative</b></div><div>No late or significant variable decelerations</div>
      <div><b style="color:{CORAL};">Positive</b></div><div>Late decelerations following ≥50% of contractions</div>
      <div><b style="color:{GOLD};">Equivocal-suspicious</b></div><div>Intermittent late decelerations or significant variable decelerations</div>
      <div><b style="color:{GOLD};">Equivocal-hyperstimulatory</b></div><div>Decelerations with contractions more frequent than every 2 min or lasting >90 sec</div>
      <div><b style="color:{ORG};">Unsatisfactory</b></div><div>&lt;3 contractions in 10 min or uninterpretable tracing</div>
    </div>
  </div>''', GOLD, GOLD, '17px', '12px')}
</div>'''
new_slides.append((content_slide("Contraction Stress Test (CST)", [cst_body], top_offset=72), True))

# Slide 59: Cardiotocography (CTG) - Basics
ctg1_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Cardiotocography (CTG)", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    Technical means of recording <b>fetal heart beat</b> (cardio-) and <b>uterine contractions</b> (-toco-) during pregnancy, typically in the 3rd trimester.<br><br>
    Simultaneous recordings by <b>2 separate transducers</b>:<br>
    • One for FHR measurement<br>
    • One for uterine contractions
  </div>''', TEAL, GOLD, '17px', '13px')}
  {card("CTG Interpretation Requires", ulist([
    '<b>Uterine activity</b> (contractions)',
    '<b>Baseline FHR</b>',
    '<b>Baseline FHR variability</b>',
    '<b>Presence of accelerations</b>',
    '<b>Periodic or episodic decelerations</b>'], '13px'), GOLD, GOLD, '17px', '13px')}
</div>
{card("Uterine Activity Definition", ulist([
    '<b>Normal:</b> ≤5 contractions in 10 min, averaged over 30-min window',
    '<b>Tachysystole:</b> >5 contractions in 10 min, averaged over 30-min window'], '13px'), TEAL, GOLD, '16px', '13px')}'''
new_slides.append((content_slide("Cardiotocography (CTG) — Basics", [ctg1_body], top_offset=70), True))

# Slide 60: Baseline FHR & Variability
baseline_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Baseline FHR", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <b>Normal:</b> <span style="color:{TEAL};font-size:18px;font-weight:700;">110-160 bpm</span><br><br>
    <b style="color:{CORAL};">Bradycardia:</b> baseline FHR &lt;110 bpm<br><br>
    <b style="color:{CORAL};">Tachycardia:</b> baseline FHR >160 bpm
  </div>''', TEAL, GOLD, '17px', '13px')}
  {card("Baseline FHR Variability", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    Fluctuations in baseline FHR that are irregular in amplitude and frequency.<br><br>
    <b style="color:{GOLD};">Normal variability:</b> <span style="color:{TEAL};font-size:16px;font-weight:700;">6-25 bpm</span><br><br>
    <b style="color:{CORAL};">Reduced/absent variability:</b> &lt;5 bpm<br>
    <span style="font-size:12px;">May indicate: fetal sleep, acidemia/hypoxia, medication effects (opioids, MgSO4), CNS depression</span>
  </div>''', GOLD, GOLD, '17px', '13px')}
</div>
{card("Accelerations", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    Abrupt increase from onset to peak in ≤30 sec.<br>
    <b>Peak ≥15 bpm</b> above baseline.<br>
    <b>Duration ≥15 seconds</b> from onset to return.<br>
    <span style="color:{TEAL};">Reassuring sign of fetal well-being — indicates intact fetal autonomic nervous system and adequate oxygenation.</span>
  </div>''', TEAL, GOLD, '16px', '13px')}'''
new_slides.append((content_slide("Baseline FHR, Variability & Accelerations", [baseline_body], top_offset=70), True))

# Slide 61: Decelerations
decel_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
  {card("Early Decelerations", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    Symmetrical, gradual decrease & return of FHR associated with contraction.<br>
    <b>Nadir at same time as contraction peak.</b><br>
    Caused by <b>head compression</b> → vagal stimulation.<br>
    <span style="color:{TEAL};">Normal/physiological — no intervention needed.</span>
  </div>''', TEAL, GOLD, '15px', '12px')}
  {card("Late Decelerations", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    Gradual decrease & return of FHR associated with contraction.<br>
    <b>Nadir AFTER contraction peak</b> (delayed timing).<br>
    Caused by <b>uteroplacental insufficiency</b> → fetal hypoxia.<br>
    <span style="color:{CORAL};">Non-reassuring/abnormal — requires immediate intervention.</span>
  </div>''', CORAL, GOLD, '15px', '12px')}
  {card("Variable Decelerations", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    Abrupt decrease in FHR, may be associated or not with contractions.<br>
    V-shaped, rapid onset & recovery.<br>
    Caused by <b>cord compression</b>.<br>
    <span style="color:{ORG};">Variable significance depending on depth, duration, and recurrence.</span>
  </div>''', ORG, GOLD, '15px', '12px')}
  {card("Prolonged Deceleration", f'''<div style="font-size:12px;color:#ffffff;line-height:1.3;">
    Visually apparent decrease in FHR ≥15 bpm from baseline, lasting <b>≥2 min but &lt;10 min</b>.<br><br>
    <b>Sinusoidal Pattern:</b> Rare ominous pattern with severe fetal anemia & associated hypoxia.
  </div>''', CORAL, GOLD, '15px', '12px')}
</div>'''
new_slides.append((content_slide("Types of FHR Decelerations", [decel_body], top_offset=72), True))

# Slide 62: CTG Interpretation (NICE 2022)
nice_body = f'''<div style="font-size:12px;color:#ffffff;margin-bottom:4px;">
  <b style="color:{GOLD};font-size:14px;">CTG Interpretation (NICE, 2022)</b>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;font-size:11px;line-height:1.2;">
  <div style="background:rgba(42,157,143,0.1);border-radius:6px;padding:6px;border-left:3px solid #ffffff;">
    <p style="font-size:12px;font-weight:700;color:#ffffff;margin:0 0 3px 0;">White (Normal)</p>
    <p style="color:#ffffff;margin:0;"><b>UC:</b> &lt;5 in 10 min</p>
    <p style="color:#ffffff;margin:0;"><b>FHR:</b> 110-160 bpm stable</p>
    <p style="color:#ffffff;margin:0;"><b>Variability:</b> 5-25 bpm</p>
    <p style="color:#ffffff;margin:0;"><b>Decels:</b> None or early</p>
  </div>
  <div style="background:rgba(233,196,106,0.12);border-radius:6px;padding:6px;border-left:3px solid #e9c46a;">
    <p style="font-size:12px;font-weight:700;color:#e9c46a;margin:0 0 3px 0;">Amber (Intermediate)</p>
    <p style="color:#ffffff;margin:0;"><b>UC:</b> ≥5 in 10 min or hypertonus</p>
    <p style="color:#ffffff;margin:0;"><b>FHR:</b> 100-109 or ↑20 bpm from baseline</p>
    <p style="color:#ffffff;margin:0;"><b>Variability:</b> &lt;5 for 30-50 min or >25 for ≤10 min</p>
    <p style="color:#ffffff;margin:0;"><b>Decels:</b> Repetitive variable &lt;30 min or repetitive late &lt;30 min</p>
  </div>
  <div style="background:rgba(231,111,81,0.15);border-radius:6px;padding:6px;border:1px solid #e76f51;">
    <p style="font-size:12px;font-weight:700;color:#e76f51;margin:0 0 3px 0;">Red (Abnormal)</p>
    <p style="color:#ffffff;margin:0;"><b>FHR:</b> &lt;100 or >160 bpm</p>
    <p style="color:#ffffff;margin:0;"><b>Variability:</b> &lt;5 for >50 min or >25 for >10 min</p>
    <p style="color:#ffffff;margin:0;"><b>Decels:</b> Repetitive variable >30 min or repetitive late >30 min</p>
  </div>
</div>
<div style="margin-top:6px;">
  {card_no_title('<p style="font-size:12px;color:#ffffff;margin:0;line-height:1.3;"><b style="color:{GOLD};">Fetal Hypoxia/Acidosis:</b> Fetal acid-base determination from scalp blood sample during labor (risks: fetal infection, hemorrhage).</p>', TEAL, '12px')}
</div>'''
new_slides.append((content_slide("CTG Interpretation (NICE, 2022)", [nice_body], top_offset=70), True))

# Slide 63: Fetal Biophysical Profile (BPP)
bpp_body = f'''<div style="font-size:13px;color:#ffffff;margin-bottom:4px;">
  <b style="color:{GOLD};font-size:16px;">Fetal Biophysical Profile (BPP)</b><br>
  Combined use of 5 fetal components — more accurate assessment of fetal health than any one alone. Requires 30 minutes.
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;font-size:12px;line-height:1.3;">
  <div style="background:rgba(42,157,143,0.1);border-radius:6px;padding:8px;border-left:3px solid #2a9d8f;">
    <p style="font-size:13px;font-weight:700;color:{GOLD};margin:0 0 4px 0;">Parameter — Score 2</p>
    <p style="color:#ffffff;margin:0;"><b>FHR:</b> Reactivity present</p>
    <p style="color:#ffffff;margin:0;"><b>Tone:</b> ≥1 episode extremity extension/flexion in 30 min</p>
    <p style="color:#ffffff;margin:0;"><b>Movement:</b> ≥3 gross body movements in 30 min</p>
    <p style="color:#ffffff;margin:0;"><b>Breathing:</b> Sustained >30 sec, ≥1 episode in 30 min</p>
    <p style="color:#ffffff;margin:0;"><b>AFI:</b> Pocket >2 cm or AFI >5 cm</p>
  </div>
  <div style="background:rgba(231,111,81,0.12);border-radius:6px;padding:8px;border-left:3px solid #e76f51;">
    <p style="font-size:13px;font-weight:700;color:{CORAL};margin:0 0 4px 0;">Parameter — Score 0</p>
    <p style="color:#ffffff;margin:0;"><b>FHR:</b> Absence of reactivity</p>
    <p style="color:#ffffff;margin:0;"><b>Tone:</b> No extension/flexion</p>
    <p style="color:#ffffff;margin:0;"><b>Movement:</b> &lt;3 movements in 30 min</p>
    <p style="color:#ffffff;margin:0;"><b>Breathing:</b> Absent</p>
    <p style="color:#ffffff;margin:0;"><b>AFI:</b> Less fluid</p>
  </div>
</div>
{card_no_title(f'''<p style="font-size:13px;color:#ffffff;margin:0;line-height:1.3;">
    <b>Score 8-10:</b> Good fetal well-being, normal pH | <b>Score 6:</b> Equivocal — repeat | <b>Score ≤4:</b> Predictor of abnormal outcome
  </p>''', TEAL, '13px')}'''
new_slides.append((content_slide("Fetal Biophysical Profile (BPP)", [bpp_body], top_offset=68), True))

# Slide 64: Umbilical Artery Doppler + Student Activity
doppler_body = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
  {card("Umbilical Artery Doppler Velocimetry", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    Non-invasive technique to assess blood flow in the umbilical artery.<br><br>
    <b>S/D ratio</b> (systolic/diastolic) — most commonly used index.<br>
    <b style="color:{CORAL};">Abnormal:</b> >95th percentile for gestational age.<br><br>
    <b style="color:{GOLD};">Absent end-diastolic flow:</b> ↑ resistance to umbilical artery flow.<br><br>
    <b style="color:{GOLD};">Reversed end-diastolic flow:</b> Most severe form — >70% placental obliteration, high fetal mortality.<br><br>
    Results from poorly vascularized placental villi — seen in most extreme FGR cases.
  </div>''', TEAL, GOLD, '16px', '13px')}
  {card("Doppler Waveform Patterns", f'''<div style="font-size:13px;color:#ffffff;line-height:1.4;">
    <p style="margin:0 0 4px 0;"><b style="color:{TEAL};">A. Normal:</b> Positive end-diastolic flow, continuous forward flow.</p>
    <p style="margin:0 0 4px 0;"><b style="color:{ORG};">B. Absent EDF:</b> Waveform touches baseline — ~25-50% placental obliteration, ↑ perinatal morbidity.</p>
    <p style="margin:0 0 4px 0;"><b style="color:{CORAL};">C. Reversed EDF:</b> Flow below baseline — >70% placental obliteration, high fetal mortality (~50%).</p>
    <p style="margin:4px 0 0 0;"><span style="color:{CORAL};font-weight:700;">Requires urgent intervention (emergent delivery).</span></p>
  </div>''', CORAL, GOLD, '16px', '13px')}
</div>
{activity_box("Each student is requested to attend during bedside part of the clinical round a session of non-stress test by CTG or biophysical ultrasonographic profile guided by clinical round tutor.")}
<p style="font-size:13px;color:#ffffff;margin:2px 0 0 0;"><b style="color:{GOLD};">Questions:</b> <span style="color:{TEAL};">https://forms.gle/Uy7xHrKqM6uPcCNY8</span></p>'''
new_slides.append((content_slide("Umbilical Artery Doppler & Student Activity", [doppler_body], top_offset=72), True))

# ═══════════════════════════════════════════
# SLIDE 65: COMPREHENSIVE SUMMARY
# ═══════════════════════════════════════════
summary_html = f'''<div style="position:absolute;top:20px;left:60px;z-index:10;">
  <p style="font-size:32px;font-weight:700;color:#ffffff;margin:0;">Summary</p>
  <div style="width:60px;height:4px;background:#e9c46a;margin:6px 0 14px 0;"></div>
</div>
<div style="position:absolute;top:68px;left:50px;right:50px;bottom:50px;z-index:10;">
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;">
    {card("Physiology of Reproduction", ulist([
      'Fertilization→implantation (6-7d)',
      'Placenta: 500g, gas/nutrition/hormones',
      'HCG, HPL, estrogen, progesterone',
      'Amniotic fluid: 800-1000ml',
      'Cord: 2A+1V in Wharton jelly'], '11px'), TEAL, GOLD, '14px', '11px')}
    {card("Maternal Adaptation", ulist([
      'Uterus: 50g→1000g, Braxton Hicks',
      'Blood vol ↑30-40%, hypercoagulable',
      'CO ↑40%, BP ↓ (2nd tri)',
      'Nausea, heartburn, constipation',
      'Chloasma, striae, linea nigra'], '11px'), GOLD, GOLD, '14px', '11px')}
    {card("Diagnosis & Antenatal Care", ulist([
      '1st tri: amenorrhea, Hegar, hCG, US',
      '2nd tri: quickening, ballottement, FHS',
      '3rd tri: engagement, sure signs',
      'Visits: monthly→2wk→weekly',
      'Screening: CBC, Rh, glucose, rubella'], '11px'), ORG, GOLD, '14px', '11px')}
    {card("Female Pelvis & Fetal Skull", ulist([
      'Pelvis: Gynecoid (50%), Android (20%)',
      'Inlet: True conj. 11cm, Obst. 10.5cm',
      'Outlet: Bituberous 11cm',
      'Skull: Biparietal 9.5cm, OF 11.5cm',
      'Fontanelles: Bregma & Lambda'], '11px'), TEAL, GOLD, '14px', '11px')}
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:6px;">
    {card("Puerperium", ulist([
      '6 wks postpartum, uterus 1000g→60g',
      'Subinvolution: retained fragments/infection',
      'Puerperal pyrexia: ≥38°C ≥24h in 10 days',
      'Mgmt: massage, anti-D if Rh-ve, contraception'], '11px'), CORAL, GOLD, '14px', '11px')}
    {card("Fetal Well-being Assessment", ulist([
      'NST: ≥2 accelerations in 20 min',
      'CST: Negative/Positive/Equivocal',
      'CTG: Baseline 110-160, variability 6-25',
      'BPP: 5 components, score 8-10=normal',
      'Doppler: S/D ratio, absent/reversed EDF'], '11px'), TEAL, GOLD, '14px', '11px')}
  </div>
</div>'''

new_slides.append((summary_html, True))

print(f"\nTotal new slides: {len(new_slides)}")

# Write all new slides
start_num = 39
for i, (body, wb) in enumerate(new_slides):
    num = start_num + i
    write_slide(num, body, wb)

# Also update slide 38 (old summary → bridge to new content)
# Make it a "Continued" section transition
bridge_html = f'''<div style="position:absolute;top:0;left:0;width:960px;height:540px;background:#264653;"></div>
<div style="position:absolute;top:0;right:0;width:400px;height:540px;background:#2a9d8f;opacity:0.12;"></div>
<div style="position:absolute;top:120px;left:80px;z-index:10;">
  <p style="font-size:28px;font-weight:700;color:#2a9d8f;margin:0;letter-spacing:2px;">CONTINUED</p>
  <div style="width:80px;height:4px;background:#e9c46a;margin:12px 0 18px 0;"></div>
  <p style="font-size:36px;font-weight:700;color:#ffffff;margin:0;">Additional Topics</p>
  <p style="font-size:20px;color:#e9c46a;margin:10px 0 0 0;">Female Pelvis · Fetal Skull · Puerperium · Fetal Well-being</p>
</div>'''
write_slide(38, bridge_html, True)

print("\n=== DONE ===")
print(f"Total slides now: 1-37 (original) + 38 (transition) + 39-{start_num + len(new_slides) - 1} (new) = {start_num + len(new_slides) - 1}")
