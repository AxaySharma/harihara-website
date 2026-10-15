const fs = require('fs');
const { Resvg } = require('@resvg/resvg-js');
const { execSync } = require('child_process');

// Load Montserrat Regular (400) and Medium (500)
const fontReg = fs.readFileSync('node_modules/@fontsource/montserrat/files/montserrat-latin-400-normal.woff');
const fontMed = fs.readFileSync('node_modules/@fontsource/montserrat/files/montserrat-latin-500-normal.woff');

// We have the ground truth binary mask in design-assets/l2_gt.png
// Let's create l2_gt.png first
execSync(`python3 -c "
import cv2
orig = cv2.imread('design-assets/logo-original.jpg')
gray_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
crop = gray_orig[305:342, 400:1115]
t, bin_crop = cv2.threshold(crop, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imwrite('design-assets/l2_gt.png', bin_crop)
"`);

const gtPng = fs.readFileSync('design-assets/l2_gt.png');

// In node, we can test parameters and compute IoU using PNG pixel buffers!
const { PNG } = require('pngjs'); // Let's check if pngjs or sharp or python is available
