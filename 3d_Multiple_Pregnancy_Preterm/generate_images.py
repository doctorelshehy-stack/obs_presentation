#!/usr/bin/env python3
"""Generate medical-themed images for the presentation slides."""
import os
from PIL import Image, ImageDraw, ImageFont
import math

IMGS_DIR = "/media/mohamed/projects4/projects/obstaric/raw material/3_Medical_Obstetric_Disorders/3d_Multiple_Pregnancy_Preterm/slides/imgs"
os.makedirs(IMGS_DIR, exist_ok=True)

# Colors from Palette 10
DARK = (38, 70, 83)       # #264653
TEAL = (42, 157, 143)     # #2a9d8f
YELLOW = (233, 196, 106)  # #e9c46a
ORANGE = (244, 162, 97)   # #f4a261
RED = (231, 118, 81)      # #e76f51
WHITE = (255, 255, 255)
LIGHT_BG = (237, 242, 244)  # light gray bg

def create_image(filename, width, height, draw_fn):
    """Create an image with given draw function."""
    img = Image.new('RGB', (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    draw_fn(draw, width, height)
    path = os.path.join(IMGS_DIR, filename)
    img.save(path, 'PNG')
    print(f"  Created {path}")
    return path

# ─── COVER IMAGE ────────────────────────────────────────────
def draw_cover(draw, w, h):
    # Background gradient-like blocks
    draw.rectangle([0, 0, w, h], fill=LIGHT_BG)
    # Decorative circles
    draw.ellipse([-60, -60, 200, 200], fill=TEAL + (80,), outline=None)
    draw.ellipse([w-150, h-150, w+50, h+50], fill=RED + (60,), outline=None)
    draw.ellipse([w//2-80, h//2-80, w//2+80, h//2+80], fill=YELLOW + (40,), outline=None)
    # Medical cross SVG-like shape
    cx, cy = w//2, h//2-40
    # Draw a stylized medical/obstetric icon - simple cross
    draw.rectangle([cx-15, cy-40, cx+15, cy+40], fill=DARK)
    draw.rectangle([cx-40, cy-15, cx+40, cy+15], fill=DARK)
    # Small baby/uterus icon
    draw.ellipse([cx-50, cy+50, cx+50, cy+100], outline=DARK, width=3)
    # Bottom bar
    draw.rectangle([0, h-8, w, h], fill=TEAL)

create_image("cover.png", 960, 540, draw_cover)

# ─── MULTIPLE PREGNANCY IMAGES ─────────────────────────────
def draw_twins_types(draw, w, h):
    draw.rectangle([0, 0, w, h], fill=WHITE)
    # Monozygotic
    draw.ellipse([30, 30, 130, 130], fill=TEAL + (100,), outline=TEAL, width=2)
    draw.ellipse([170, 30, 270, 130], fill=TEAL + (100,), outline=TEAL, width=2)
    draw.text((60, 20), "Monozygotic", fill=DARK)
    draw.text((45, 135), "Identical", fill=DARK)
    # Dizygotic
    draw.ellipse([350, 30, 450, 130], fill=RED + (80,), outline=RED, width=2)
    draw.ellipse([490, 30, 590, 130], fill=ORANGE + (80,), outline=ORANGE, width=2)
    draw.text((380, 20), "Dizygotic", fill=DARK)
    draw.text((380, 135), "Fraternal", fill=DARK)
    # Membrane diagrams
    # Dichorionic
    draw.rectangle([30, 200, 280, 350], outline=DARK, width=2)
    draw.ellipse([55, 220, 130, 295], fill=TEAL + (60,), outline=TEAL, width=2)
    draw.ellipse([180, 220, 255, 295], fill=TEAL + (60,), outline=TEAL, width=2)
    draw.text((50, 360), "Dichorionic-Diamniotic", fill=DARK)
    draw.text((55, 380), "(Lambda sign / thick membrane)", fill=TEAL)
    # Monochorionic
    draw.rectangle([340, 200, 590, 350], outline=DARK, width=2)
    draw.ellipse([370, 220, 440, 295], fill=TEAL + (60,), outline=TEAL, width=2)
    draw.ellipse([470, 220, 540, 295], fill=TEAL + (60,), outline=TEAL, width=2)
    draw.text((370, 360), "Monochorionic-Diamniotic", fill=DARK)
    draw.text((375, 380), "(T sign / thin membrane)", fill=TEAL)

create_image("twins-types.png", 640, 420, draw_twins_types)

def draw_ttts(draw, w, h):
    draw.rectangle([0, 0, w, h], fill=WHITE)
    # Draw placenta
    draw.ellipse([w//2-80, 30, w//2+80, 130], fill=RED + (80,), outline=RED, width=2)
    draw.text((w//2-30, 135), "Placenta", fill=DARK)
    # Vessels
    draw.line([w//2-20, 80, w//4, 250], fill=RED, width=3)
    draw.line([w//2+20, 80, 3*w//4, 250], fill=TEAL, width=3)
    # Donor
    draw.ellipse([w//4-40, 250-40, w//4+40, 250+40], fill=TEAL + (80,), outline=TEAL, width=2)
    draw.text((w//4-20, 295), "Donor", fill=DARK)
    draw.text((w//4-30, 315), "Anemia", fill=RED)
    draw.text((w//4-30, 335), "Oligohydramnios", fill=RED)
    # Recipient
    draw.ellipse([3*w//4-40, 250-40, 3*w//4+40, 250+40], fill=RED + (80,), outline=RED, width=2)
    draw.text((3*w//4-30, 295), "Recipient", fill=DARK)
    draw.text((3*w//4-30, 315), "Polycythemia", fill=RED)
    draw.text((3*w//4-30, 335), "Polyhydramnios", fill=RED)
    # Arrow
    draw.line([w//4+45, 250, 3*w//4-45, 250], fill=ORANGE, width=2)
    draw.polygon([3*w//4-35, 245, 3*w//4-45, 250, 3*w//4-35, 255], fill=ORANGE)

create_image("ttts.png", 640, 380, draw_ttts)

# ─── PRETERM LABOR IMAGES ──────────────────────────────────
def draw_cervix(draw, w, h):
    draw.rectangle([0, 0, w, h], fill=WHITE)
    # Uterus shape
    draw.ellipse([50, 50, w-50, h-80], outline=DARK, width=3)
    # Cervix
    draw.rectangle([w//2-30, h-80, w//2+30, h-20], outline=DARK, width=3)
    # Internal os
    draw.line([w//2-30, h-80, w//2-10, h-80], fill=RED, width=3)
    draw.line([w//2+10, h-80, w//2+30, h-80], fill=RED, width=3)
    # T shape label
    draw.text((w//2+40, h-100), "T shape (normal)", fill=TEAL)
    draw.text((w//2+40, h-80), "→ Y → V → U (PTL)", fill=RED)
    # Fetus
    draw.ellipse([w//2-30, 130, w//2+30, 200], fill=TEAL + (60,), outline=TEAL, width=2)
    draw.text((w//2-25, 205), "Fetus", fill=DARK)

create_image("cervix.png", 640, 300, draw_cervix)

def draw_tocolytics(draw, w, h):
    draw.rectangle([0, 0, w, h], fill=WHITE)
    drugs = [
        ("Indomethacin", "PG synthetase inhibitor", TEAL),
        ("Nifedipine", "Ca channel blocker", ORANGE),
        ("Atosiban", "Oxytocin antagonist", RED),
        ("MgSO4", "Magnesium sulfate", DARK),
        ("Ritodrine", "Beta agonist", TEAL),
    ]
    y_start = 20
    for i, (name, desc, color) in enumerate(drugs):
        y = y_start + i * 55
        draw.rectangle([40, y, 40+60, y+40], fill=color)
        draw.text((110, y+5), name, fill=DARK)
        draw.text((110, y+22), desc, fill=color)
    # Note
    draw.text((40, y_start+5*55+10), "Contraindications: Chorioamnionitis, advanced labor,", fill=RED)
    draw.text((40, y_start+5*55+28), ">34 wks, preeclampsia, abruption, fetal distress", fill=RED)

create_image("tocolytics.png", 640, 320, draw_tocolytics)

# ─── PROM IMAGES ──────────────────────────────────────────
def draw_prom_diagnosis(draw, w, h):
    draw.rectangle([0, 0, w, h], fill=WHITE)
    # Speculum
    draw.rectangle([50, 50, 200, 250], outline=DARK, width=3)
    draw.text((70, 260), "Speculum Exam", fill=DARK)
    draw.text((60, 280), "(First step)", fill=TEAL)
    # Nitrazine
    draw.rectangle([270, 50, 420, 180], outline=DARK, width=3)
    draw.rectangle([310, 90, 380, 150], fill=ORANGE + (150,))
    draw.text((280, 190), "Nitrazine Test", fill=DARK)
    draw.text((275, 210), "pH 7-7.5 → Blue", fill=TEAL)
    draw.text((275, 230), "pH 3.5-4.5 → Yellow", fill=RED)
    # Fern
    draw.ellipse([480, 60, 600, 180], outline=DARK, width=2)
    # Simple fern-like lines
    for x, y in [(530, 120), (540, 100), (520, 140), (550, 110), (545, 130)]:
        draw.line([540, 180, x, y], fill=DARK, width=2)
    draw.text((480, 190), "Fern Test", fill=DARK)
    draw.text((475, 210), "Fern pattern = PROM", fill=TEAL)

create_image("prom-diagnosis.png", 640, 320, draw_prom_diagnosis)

print("All images generated successfully!")
