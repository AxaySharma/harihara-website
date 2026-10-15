import cv2
import numpy as np

orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
test_bgra = cv2.imread('design-assets/test_otsu_render.png', cv2.IMREAD_UNCHANGED)
alpha_test = test_bgra[:, :, 3] if test_bgra.shape[2] == 4 else (test_bgra[:, :, 0] > 10)

keep_mask = np.ones((443, 1280), dtype=bool)
# TM1 near symbol bottom right [340:390, 335:380]
keep_mask[340:395, 335:385] = False
# TM2 near HARA top right [160:200, 1210:1255]
keep_mask[160:205, 1210:1255] = False

def compute_iou(mask1, mask2):
    intersection = np.logical_and(mask1, mask2).sum()
    union = np.logical_or(mask1, mask2).sum()
    if union == 0:
        return 1.0
    return float(intersection) / float(union)

# Let's inspect optimal binarization threshold for original
for thresh in [200, 215, 225, 235, 240]:
    sym_gt = (gray_orig[:, :380] < thresh) & keep_mask[:, :380]
    sym_pred = (alpha_test[:, :380] > 128) & keep_mask[:, :380]
    
    hari_gt = (gray_orig[140:300, 380:780] < thresh) & keep_mask[140:300, 380:780]
    hari_pred = (alpha_test[140:300, 380:780] > 128) & keep_mask[140:300, 380:780]
    
    hara_gt = (gray_orig[140:300, 780:1250] < thresh) & keep_mask[140:300, 780:1250]
    hara_pred = (alpha_test[140:300, 780:1250] > 128) & keep_mask[140:300, 780:1250]
    
    print(f"Thresh {thresh} -> Symbol IoU: {compute_iou(sym_gt, sym_pred):.4f}, HARI IoU: {compute_iou(hari_gt, hari_pred):.4f}, HARA IoU: {compute_iou(hara_gt, hara_pred):.4f}")
