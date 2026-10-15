import cv2
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import re

# Load original
orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
l2_crop = gray_orig[310:355, 400:1115]

# Otsu threshold on line 2 in original
t_l2, _ = cv2.threshold(l2_crop, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"Line 2 Otsu threshold: {t_l2}")

text = "SERENITY CHEMICAL LLP"

# Test both 400 (Regular) and 500 (Medium)
for weight in [400, 500]:
    font_path = f"node_modules/@fontsource/montserrat/files/montserrat-latin-{weight}-normal.woff"
    font = TTFont(font_path)
    glyph_set = font.getGlyphSet()
    units_per_em = font['head'].unitsPerEm
    print(f"Weight {weight}: unitsPerEm = {units_per_em}")
