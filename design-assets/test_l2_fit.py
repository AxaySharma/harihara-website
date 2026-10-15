import cv2
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import subprocess

orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
t_l2, _ = cv2.threshold(gray_orig[305:342, 400:1115], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
gt_l2 = gray_orig[305:342, 400:1115] < t_l2

text = "SERENITY CHEMICAL LLP"
chars = [c for c in text if c != ' ']

# Original bounding boxes of each letter (x, y, w, h)
orig_boxes = [
    (405, 308, 22, 29), # S
    (441, 308, 22, 28), # E
    (477, 308, 24, 28), # R
    (516, 308, 21, 28), # E
    (552, 308, 24, 28), # N
    (593, 308, 4, 28),  # I
    (610, 308, 25, 28), # T
    (644, 308, 24, 28), # Y
    (702, 308, 25, 28), # C
    (743, 308, 24, 28), # H
    (784, 308, 21, 28), # E
    (820, 308, 31, 28), # M
    (868, 308, 4, 28),  # I
    (887, 308, 25, 28), # C
    (923, 308, 28, 28), # A
    (965, 308, 19, 28), # L
    (1020, 308, 20, 28), # L
    (1053, 308, 20, 28), # L
    (1086, 308, 22, 28), # P
]

def get_glyph(font, char):
    glyph_name = font.getBestCmap().get(ord(char))
    pen = SVGPathPen(font.getGlyphSet())
    font.getGlyphSet()[glyph_name].draw(pen)
    bounds = font['glyf'][glyph_name]
    return pen.getCommands(), bounds.xMin, bounds.yMin, bounds.xMax, bounds.yMax

best_overall = (0, None)

for weight in [400, 500, 600]:
    font_path = f"node_modules/@fontsource/montserrat/files/montserrat-latin-{weight}-normal.woff"
    font = TTFont(font_path)
    
    # Target height 28.5 -> scale ~ 28.5 / 700 = 0.0407
    # Baseline ~ 337
    for scale in np.linspace(0.038, 0.043, 11):
        for baseline_y in [336.0, 336.5, 337.0, 337.5, 338.0]:
            svg_paths = []
            for char, (bx, by, bw, bh) in zip(chars, orig_boxes):
                d, xmin, ymin, xmax, ymax = get_glyph(font, char)
                gw = (xmax - xmin) * scale
                # center the glyph inside the measured box width or align left
                gx = bx + (bw - gw) / 2.0
                svg_paths.append(f'<path d="{d}" transform="translate({gx:.3f},{baseline_y:.3f}) scale({scale:.5f},{-scale:.5f})" fill="#1B1B1B" />')
            
            test_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="400 305 715 37" width="715" height="37">{"".join(svg_paths)}</svg>'
            with open('design-assets/test_l2_temp.svg', 'w') as f:
                f.write(test_svg)
            
            subprocess.run(["node", "-e", """
                const fs = require('fs');
                const { Resvg } = require('@resvg/resvg-js');
                const svg = fs.readFileSync('design-assets/test_l2_temp.svg');
                const resvg = new Resvg(svg, { fitTo: { mode: 'original' } });
                fs.writeFileSync('design-assets/test_l2_temp.png', resvg.render().asPng());
            """], check=True)
            
            pred_img = cv2.imread('design-assets/test_l2_temp.png', cv2.IMREAD_UNCHANGED)
            pred_alpha = pred_img[:, :, 3] > 128
            
            intersection = np.logical_and(gt_l2, pred_alpha).sum()
            union = np.logical_or(gt_l2, pred_alpha).sum()
            iou = intersection / union
            if iou > best_overall[0]:
                best_overall = (iou, (weight, scale, baseline_y))
                print(f"NEW BEST: Weight {weight}, scale {scale:.5f}, baseline {baseline_y:.1f}: IoU = {iou:.4f} ({iou*100:.2f}%)")

print("FINAL BEST:", best_overall)
