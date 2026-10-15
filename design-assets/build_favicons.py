import subprocess
from PIL import Image
import numpy as np

# 1. Render high-res square symbol from favicon.svg using resvg
subprocess.run(['node', '-e', '''
const fs = require('fs');
const { Resvg } = require('@resvg/resvg-js');
const svg = fs.readFileSync('public/favicon.svg');
const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 512 } });
fs.writeFileSync('design-assets/fav_512.png', resvg.render().asPng());
'''], check=True)

sym_512 = Image.open('design-assets/fav_512.png').convert('RGBA')

# 2. favicon.png (32 px)
fav_32 = sym_512.resize((32, 32), Image.Resampling.LANCZOS)
fav_32.save('public/favicon.png')
print('Generated public/favicon.png (32x32)')

# 3. favicon.ico (16, 32, 48)
fav_16 = sym_512.resize((16, 16), Image.Resampling.LANCZOS)
fav_48 = sym_512.resize((48, 48), Image.Resampling.LANCZOS)
fav_48.save('public/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print('Generated public/favicon.ico (16, 32, 48)')

# 4. apple-touch-icon.png (180 px on #F6F3EE)
# Paper background #F6F3EE = (246, 243, 238)
bg_apple = Image.new('RGBA', (180, 180), (246, 243, 238, 255))
# Scale symbol to sit with comfortable padding inside 180x180 (e.g., 140x140 centered)
sym_apple = sym_512.resize((140, 140), Image.Resampling.LANCZOS)
bg_apple.paste(sym_apple, (20, 20), sym_apple)
bg_apple.convert('RGB').save('public/apple-touch-icon.png')
print('Generated public/apple-touch-icon.png (180x180 on #F6F3EE)')

# 5. og-default.png (1200 x 630) from the new full lockup
# Paper background #F6F3EE
bg_og = Image.new('RGBA', (1200, 630), (246, 243, 238, 255))
# Full lockup 2400 wide rendered down to fit nicely in 1200x630 (e.g. width ~ 860px)
full_img = Image.open('public/brand/logo-full.png').convert('RGBA')
aspect = full_img.height / full_img.width
target_w = 860
target_h = int(target_w * aspect)
full_resized = full_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
pos_x = (1200 - target_w) // 2
pos_y = (630 - target_h) // 2
bg_og.paste(full_resized, (pos_x, pos_y), full_resized)
bg_og.convert('RGB').save('public/og-default.png')
print('Generated public/og-default.png (1200x630 on #F6F3EE)')
