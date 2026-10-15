import re
import subprocess
import cv2
import numpy as np

def get_paths(fpath):
    with open(fpath) as f:
        return re.findall(r'<path[^>]*d="([^"]+)"[^>]*>', f.read())

# Symbol geometric paths:
arch_d = 'M 189.5 149.5 A 60 60 0 0 1 309.5 149.5 L 309.5 263.0 L 249.5 203.0 L 189.5 263.0 Z'
tri_d = 'M 249.5 211.0 L 126.0 337.5 L 241.5 337.5 L 241.5 303.0 L 205.0 303.0 L 249.5 258.5 L 294.0 303.0 L 257.5 303.0 L 257.5 337.5 L 373.0 337.5 Z'

p_hari = get_paths('design-assets/hari_clean_8x.svg')[:4]
p_a1 = get_paths('design-assets/a1_clean_8x.svg')[0]
p_hara = get_paths('design-assets/hara_clean_8x.svg')[:4]
p_a2 = get_paths('design-assets/a2_clean_8x.svg')[0]
p_l2 = get_paths('design-assets/l2_8x_smooth.svg')

# Gradients (separate for Arch, Triangle, and A triangles):
defs_dark = '''  <defs>
    <!-- Arch gradient: bright crimson at top to dark maroon at bottom -->
    <linearGradient id="arch-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#DB1E4D" />
      <stop offset="25%" stop-color="#C31D47" />
      <stop offset="50%" stop-color="#98203F" />
      <stop offset="75%" stop-color="#6C1E34" />
      <stop offset="100%" stop-color="#3E1E2A" />
    </linearGradient>
    <!-- Triangle gradient: brighter crimson near apex, darker maroon toward bottom feet -->
    <linearGradient id="tri-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E21448" />
      <stop offset="25%" stop-color="#D31D4A" />
      <stop offset="50%" stop-color="#B02448" />
      <stop offset="75%" stop-color="#88203D" />
      <stop offset="100%" stop-color="#661C32" />
    </linearGradient>
    <!-- Crimson triangles inside A letters: vertical gradient (inverted for negative y scale) -->
    <linearGradient id="a-tri-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4D1526" />
      <stop offset="100%" stop-color="#A02446" />
    </linearGradient>
  </defs>'''

# 1. logo-symbol.svg: viewBox="120 82 258 264"
sym_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 82 258 264" width="258" height="264">
{defs_dark}
  <g id="symbol">
    <path id="symbol-arch" d="{arch_d}" fill="url(#arch-grad)" />
    <path id="symbol-triangle" d="{tri_d}" fill="url(#tri-grad)" />
  </g>
</svg>'''

# 2. logo-wordmark.svg: viewBox="397 195 725 152"
wordmark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="397 195 725 152" width="725" height="152">
{defs_dark}
  <g id="wordmark-hari" transform="translate(380, 305) scale(0.0125, -0.0125)" fill="#1B1B1B">
    {''.join(f'<path d="{p}"/>' for p in p_hari)}
  </g>
  <g id="a1-tri" transform="translate(380, 305) scale(0.0125, -0.0125)" fill="url(#a-tri-grad)">
    <path d="{p_a1}" />
  </g>
  <g id="wordmark-hara" transform="translate(740, 305) scale(0.0125, -0.0125)" fill="#6C6C6C">
    {''.join(f'<path d="{p}"/>' for p in p_hara)}
  </g>
  <g id="a2-tri" transform="translate(740, 305) scale(0.0125, -0.0125)" fill="url(#a-tri-grad)">
    <path d="{p_a2}" />
  </g>
  <g id="line-2" transform="translate(400, 342) scale(0.0125, -0.0125)" fill="#111111">
    {''.join(f'<path d="{p}"/>' for p in p_l2)}
  </g>
</svg>'''

# 3. logo-full.svg: viewBox="120 82 1002 265"
full_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 82 1002 265" width="1002" height="265">
{defs_dark}
  <g id="symbol">
    <path id="symbol-arch" d="{arch_d}" fill="url(#arch-grad)" />
    <path id="symbol-triangle" d="{tri_d}" fill="url(#tri-grad)" />
  </g>
  <g id="wordmark-hari" transform="translate(380, 305) scale(0.0125, -0.0125)" fill="#1B1B1B">
    {''.join(f'<path d="{p}"/>' for p in p_hari)}
  </g>
  <g id="a1-tri" transform="translate(380, 305) scale(0.0125, -0.0125)" fill="url(#a-tri-grad)">
    <path d="{p_a1}" />
  </g>
  <g id="wordmark-hara" transform="translate(740, 305) scale(0.0125, -0.0125)" fill="#6C6C6C">
    {''.join(f'<path d="{p}"/>' for p in p_hara)}
  </g>
  <g id="a2-tri" transform="translate(740, 305) scale(0.0125, -0.0125)" fill="url(#a-tri-grad)">
    <path d="{p_a2}" />
  </g>
  <g id="line-2" transform="translate(400, 342) scale(0.0125, -0.0125)" fill="#111111">
    {''.join(f'<path d="{p}"/>' for p in p_l2)}
  </g>
</svg>'''

# 4. logo-full-light.svg: viewBox="120 82 1002 265"
# Charcoal and #111111 -> #F6F3EE, Grey -> #B9B9B9, Crimson gradients unchanged
full_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 82 1002 265" width="1002" height="265">
{defs_dark}
  <g id="symbol">
    <path id="symbol-arch" d="{arch_d}" fill="url(#arch-grad)" />
    <path id="symbol-triangle" d="{tri_d}" fill="url(#tri-grad)" />
  </g>
  <g id="wordmark-hari" transform="translate(380, 305) scale(0.0125, -0.0125)" fill="#F6F3EE">
    {''.join(f'<path d="{p}"/>' for p in p_hari)}
  </g>
  <g id="a1-tri" transform="translate(380, 305) scale(0.0125, -0.0125)" fill="url(#a-tri-grad)">
    <path d="{p_a1}" />
  </g>
  <g id="wordmark-hara" transform="translate(740, 305) scale(0.0125, -0.0125)" fill="#B9B9B9">
    {''.join(f'<path d="{p}"/>' for p in p_hara)}
  </g>
  <g id="a2-tri" transform="translate(740, 305) scale(0.0125, -0.0125)" fill="url(#a-tri-grad)">
    <path d="{p_a2}" />
  </g>
  <g id="line-2" transform="translate(400, 342) scale(0.0125, -0.0125)" fill="#F6F3EE">
    {''.join(f'<path d="{p}"/>' for p in p_l2)}
  </g>
</svg>'''

# Write SVGs to public/brand/
with open('public/brand/logo-symbol.svg', 'w') as f:
    f.write(sym_svg)
with open('public/brand/logo-wordmark.svg', 'w') as f:
    f.write(wordmark_svg)
with open('public/brand/logo-full.svg', 'w') as f:
    f.write(full_svg)
with open('public/brand/logo-full-light.svg', 'w') as f:
    f.write(full_light_svg)

print("Saved all 4 SVGs in public/brand/.")
