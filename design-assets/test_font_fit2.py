import cv2
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import subprocess

orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
crop = gray_orig[305:342, 400:1115]
t, _ = cv2.threshold(crop, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
gt_bin = crop < t

text = "SERENITY CHEMICAL LLP"
chars = [c for c in text if c != ' ']

# The 19 letter horizontal spans in original:
# We know the approximate centers or left edges of the 19 letters:
# Let's find each letter's connected component bounding box in gt_bin
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(gt_bin.astype(np.uint8))
boxes = []
for i in range(1, num_labels):
    if stats[i, cv2.CC_STAT_AREA] > 20:
        boxes.append((stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP], stats[i, cv2.CC_STAT_WIDTH], stats[i, cv2.CC_STAT_HEIGHT]))
boxes.sort(key=lambda b: b[0])

font_med = TTFont('node_modules/@fontsource/montserrat/files/montserrat-latin-500-normal.woff')
font_reg = TTFont('node_modules/@fontsource/montserrat/files/montserrat-latin-400-normal.woff')

def get_glyph_path(font, char):
    glyph_name = font.getBestCmap().get(ord(char))
    pen = SVGPathPen(font.getGlyphSet())
    font.getGlyphSet()[glyph_name].draw(pen)
    bounds = font['glyf'][glyph_name]
    return pen.getCommands(), bounds.xMin, bounds.yMin, bounds.xMax, bounds.yMax

# Let's optimize per-letter x, y, scale for each font
for name, font in [("Medium", font_med), ("Regular", font_reg)]:
    best_placements = []
    for char, (bx, by, bw, bh) in zip(chars, boxes):
        d, xmin, ymin, xmax, ymax = get_glyph_path(font, char)
        gw = xmax - xmin
        gh = ymax - ymin
        
        # We search scale, x, y to maximize local overlap with this letter's crop
        best_char_iou = 0
        best_cfg = None
        
        # local GT patch
        pad = 4
        x0 = max(0, bx - pad)
        x1 = min(crop.shape[1], bx + bw + pad)
        local_gt = gt_bin[:, x0:x1]
        
        for scale in np.linspace(0.038, 0.043, 6):
            for x_pos in np.linspace(bx - 2, bx + 2, 9):
                for baseline in np.linspace(31.0, 33.5, 6):
                    # test single glyph render
                    # to make it fast, we can test by rendering
                    pass
    print(f"Testing font {name}...")
