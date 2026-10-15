import cv2
import numpy as np
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import subprocess

orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
t_l2, _ = cv2.threshold(gray_orig[310:355, 400:1115], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
gt_l2 = gray_orig[310:355, 400:1115] < t_l2

text = "SERENITY CHEMICAL LLP"

# Let's extract paths for characters from font
def get_char_path(font, char):
    glyph_name = font.getBestCmap().get(ord(char))
    if not glyph_name:
        return "", 0
    pen = SVGPathPen(font.getGlyphSet())
    font.getGlyphSet()[glyph_name].draw(pen)
    width = font['hmtx'][glyph_name][0]
    return pen.getCommands(), width

# Let's test Montserrat Regular (400) and Medium (500)
for weight in [400, 500]:
    font_path = f"node_modules/@fontsource/montserrat/files/montserrat-latin-{weight}-normal.woff"
    font = TTFont(font_path)
    
    # In original:
    # First letter 'S' starts around x=408
    # Last letter 'P' ends around x=1104
    # Total span = ~696 px
    # Cap height in original is ~23.5 px (from y=318 to y=341.5)
    # Montserrat cap height is 700 / 1000 em.
    # So font-size ~ 23.5 / 0.7 = 33.5 px.
    
    # We can optimize: font_size (scale), letter_spacing, start_x, baseline_y
    best_iou = 0
    best_params = None
    
    for fs in [31.5, 32.0, 32.5, 33.0, 33.5]:
        scale = fs / 1000.0
        for start_x in [406, 407, 408, 409, 410]:
            for baseline_y in [341, 341.5, 342, 342.5]:
                for tracking in [13.0, 13.5, 14.0, 14.5, 15.0, 15.5]:
                    # Build SVG of line 2
                    cur_x = start_x
                    svg_paths = []
                    for c in text:
                        if c == ' ':
                            cur_x += 250 * scale + tracking
                            continue
                        d, w = get_char_path(font, c)
                        if d:
                            svg_paths.append(f'<path d="{d}" transform="translate({cur_x},{baseline_y}) scale({scale},{-scale})" fill="#1B1B1B" />')
                        cur_x += w * scale + tracking
                    
                    # We can render just this crop using a tiny node script or opencv approximation, or resvg
                    # To do this quickly, let's write a small batch of top candidates
                    pass

print("Script template ready.")
