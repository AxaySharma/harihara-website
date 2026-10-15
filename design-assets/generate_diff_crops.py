import cv2
import numpy as np
from PIL import Image

# Load original 1280x443
orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

# Load rendered clean SVG at 1280x443
pred = cv2.imread('design-assets/test_full_clean.png', cv2.IMREAD_UNCHANGED)
pred_bgr = pred[:, :, :3]
pred_alpha = pred[:, :, 3]

# Create white-background composite for pred
pred_white = np.full_like(orig, 255)
alpha_factor = (pred_alpha / 255.0)[:, :, np.newaxis]
pred_white = (pred_bgr * alpha_factor + pred_white * (1.0 - alpha_factor)).astype(np.uint8)

# TM Exclusion Mask
keep_mask = np.ones((443, 1280), dtype=bool)
keep_mask[340:395, 335:385] = False
keep_mask[160:205, 1210:1255] = False

# Function to generate registered crops & difference images:
# diff image: XOR/mismatch in red:
# where mismatch occurs, color red [0, 0, 255], otherwise dark/gray/white.
def create_diff_image(orig_crop, pred_crop, gt_mask, pred_mask):
    # Base is grayscale of original
    diff = cv2.cvtColor(cv2.cvtColor(orig_crop, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    # Mismatches (XOR):
    mismatch = np.logical_xor(gt_mask, pred_mask)
    # Highlight mismatches in vivid red
    diff[mismatch] = [0, 0, 255] # Red in BGR
    return diff

# 1. Element crops:
# (a) Symbol: x in [120, 375], y in [85, 345]
sym_slice = (slice(85, 345), slice(120, 375))
sym_gt_mask = (gray_orig[sym_slice] < 225) & keep_mask[sym_slice]
sym_pred_mask = (pred_alpha[sym_slice] > 128) & keep_mask[sym_slice]
sym_orig = orig[sym_slice]
sym_new = pred_white[sym_slice]
sym_diff = create_diff_image(sym_orig, sym_new, sym_gt_mask, sym_pred_mask)

cv2.imwrite('public/brand/diff_symbol_orig.png', sym_orig)
cv2.imwrite('public/brand/diff_symbol_new.png', sym_new)
cv2.imwrite('public/brand/diff_symbol_diff.png', sym_diff)

# (b) HARI: x in [395, 780], y in [185, 295]
hari_slice = (slice(185, 295), slice(395, 780))
t_hari, _ = cv2.threshold(gray_orig[hari_slice], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
hari_gt_mask = (gray_orig[hari_slice] < t_hari) & keep_mask[hari_slice]
hari_pred_mask = (pred_alpha[hari_slice] > 128) & keep_mask[hari_slice]
hari_orig = orig[hari_slice]
hari_new = pred_white[hari_slice]
hari_diff = create_diff_image(hari_orig, hari_new, hari_gt_mask, hari_pred_mask)

cv2.imwrite('public/brand/diff_hari_orig.png', hari_orig)
cv2.imwrite('public/brand/diff_hari_new.png', hari_new)
cv2.imwrite('public/brand/diff_hari_diff.png', hari_diff)

# (c) HARA: x in [780, 1220], y in [185, 295]
hara_slice = (slice(185, 295), slice(780, 1220))
t_hara, _ = cv2.threshold(gray_orig[hara_slice], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
hara_gt_mask = (gray_orig[hara_slice] < t_hara) & keep_mask[hara_slice]
hara_pred_mask = (pred_alpha[hara_slice] > 128) & keep_mask[hara_slice]
hara_orig = orig[hara_slice]
hara_new = pred_white[hara_slice]
hara_diff = create_diff_image(hara_orig, hara_new, hara_gt_mask, hara_pred_mask)

cv2.imwrite('public/brand/diff_hara_orig.png', hara_orig)
cv2.imwrite('public/brand/diff_hara_new.png', hara_new)
cv2.imwrite('public/brand/diff_hara_diff.png', hara_diff)

# (d) Line 2: x in [400, 1115], y in [305, 342]
l2_slice = (slice(305, 342), slice(400, 1115))
t_l2, _ = cv2.threshold(gray_orig[l2_slice], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
l2_gt_mask = (gray_orig[l2_slice] < t_l2)
l2_pred_mask = (pred_alpha[l2_slice] > 128)
l2_orig = orig[l2_slice]
l2_new = pred_white[l2_slice]
l2_diff = create_diff_image(l2_orig, l2_new, l2_gt_mask, l2_pred_mask)

cv2.imwrite('public/brand/diff_l2_orig.png', l2_orig)
cv2.imwrite('public/brand/diff_l2_new.png', l2_new)
cv2.imwrite('public/brand/diff_l2_diff.png', l2_diff)

# Detail crops for 400% zoom:
# 1. Triangle corners / apex / arrow: x in [220, 280], y in [200, 335]
tri_crop_orig = orig[200:335, 220:280]
tri_crop_new = pred_white[200:335, 220:280]
cv2.imwrite('public/brand/zoom_tri_orig.png', tri_crop_orig)
cv2.imwrite('public/brand/zoom_tri_new.png', tri_crop_new)

# 2. A1 (in HARI with red triangle): x in [480, 580], y in [195, 295]
a1_crop_orig = orig[195:295, 480:580]
a1_crop_new = pred_white[195:295, 480:580]
cv2.imwrite('public/brand/zoom_a1_orig.png', a1_crop_orig)
cv2.imwrite('public/brand/zoom_a1_new.png', a1_crop_new)

# 3. A2 (first A in HARA with red triangle): x in [865, 965], y in [195, 295]
a2_crop_orig = orig[195:295, 865:965]
a2_crop_new = pred_white[195:295, 865:965]
cv2.imwrite('public/brand/zoom_a2_orig.png', a2_crop_orig)
cv2.imwrite('public/brand/zoom_a2_new.png', a2_crop_new)

# 4. A3 (last A in HARA with NO triangle, solid grey bar): x in [1120, 1220], y in [195, 295]
a3_crop_orig = orig[195:295, 1120:1220]
a3_crop_new = pred_white[195:295, 1120:1220]
cv2.imwrite('public/brand/zoom_a3_orig.png', a3_crop_orig)
cv2.imwrite('public/brand/zoom_a3_new.png', a3_crop_new)

# 5. R leg shape: x in [580, 680], y in [195, 295]
r_crop_orig = orig[195:295, 580:680]
r_crop_new = pred_white[195:295, 580:680]
cv2.imwrite('public/brand/zoom_r_orig.png', r_crop_orig)
cv2.imwrite('public/brand/zoom_r_new.png', r_crop_new)

print("Generated all diff and zoom images in public/brand/.")
