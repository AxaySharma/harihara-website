import cv2
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import subprocess
import json

orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
crop = gray_orig[305:342, 400:1115]
t, _ = cv2.threshold(crop, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
gt_bin = crop < t

text = "SERENITY CHEMICAL LLP"
chars = [c for c in text if c != ' ']

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(gt_bin.astype(np.uint8))
boxes = []
for i in range(1, num_labels):
    if stats[i, cv2.CC_STAT_AREA] > 20:
        boxes.append((stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP], stats[i, cv2.CC_STAT_WIDTH], stats[i, cv2.CC_STAT_HEIGHT]))
boxes.sort(key=lambda b: b[0])

font_med = TTFont('node_modules/@fontsource/montserrat/files/montserrat-latin-500-normal.woff')
font_reg = TTFont('node_modules/@fontsource/montserrat/files/montserrat-latin-400-normal.woff')

def get_glyph(font, char):
    glyph_name = font.getBestCmap().get(ord(char))
    pen = SVGPathPen(font.getGlyphSet())
    font.getGlyphSet()[glyph_name].draw(pen)
    return pen.getCommands()

# Render individual glyphs for unique chars at scale 0.040
for font_name, font in [('reg', font_reg), ('med', font_med)]:
    for scale in [0.038, 0.039, 0.040, 0.041, 0.042]:
        # Let's render each unique character into a small image
        unique_chars = sorted(list(set(chars)))
        char_imgs = {}
        for c in unique_chars:
            d = get_glyph(font, c)
            svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -1000 1200 1200" width="120" height="120"><path d="{d}" transform="scale(0.1, -0.1)" fill="#fff"/></svg>'
            # We can use resvg or canvas
            pass

print("Done preparing char renders.")
