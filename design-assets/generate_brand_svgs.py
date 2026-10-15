import re
import subprocess
import cv2
import numpy as np

def extract_paths(svg_path):
    with open(svg_path) as f:
        content = f.read()
    return re.findall(r'<path[^>]*d="([^"]+)"[^>]*>', content)

sym_paths = extract_paths('design-assets/otsu_sym.svg')
hari_paths = extract_paths('design-assets/otsu_hari.svg')
hara_paths = extract_paths('design-assets/otsu_hara_clean.svg')
a1_paths = extract_paths('design-assets/otsu_a1.svg')
a2_paths = extract_paths('design-assets/otsu_a2.svg')
l2_paths = extract_paths('design-assets/l2_temp.svg')

# Gradients (identical for dark and light):
defs = '''  <defs>
    <linearGradient id="arch-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E21545" />
      <stop offset="30%" stop-color="#DA1A49" />
      <stop offset="65%" stop-color="#AC1C40" />
      <stop offset="100%" stop-color="#781833" />
    </linearGradient>
    <linearGradient id="tri-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#981B3B" />
      <stop offset="35%" stop-color="#C42048" />
      <stop offset="70%" stop-color="#962744" />
      <stop offset="100%" stop-color="#701F36" />
    </linearGradient>
    <linearGradient id="a-tri-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#D01A45" />
      <stop offset="100%" stop-color="#7A1230" />
    </linearGradient>
  </defs>'''

# 1. logo-symbol.svg: viewBox="120 82 258 264"
sym_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 82 258 264" width="258" height="264">
{defs}
  <g id="symbol" transform="translate(0, 443) scale(0.025, -0.025)">
    <path d="{sym_paths[0]}" fill="url(#arch-grad)" />
    <path d="{sym_paths[1]}" fill="url(#tri-grad)" />
  </g>
</svg>'''

# 2. logo-wordmark.svg: viewBox="397 195 725 152"
wordmark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="397 195 725 152" width="725" height="152">
{defs}
  <g id="wordmark-hari" transform="translate(0, 443) scale(0.025, -0.025)" fill="#1B1B1B">
    {''.join(f'<path d="{p}"/>' for p in hari_paths)}
  </g>
  <g id="a1-tri" transform="translate(0, 443) scale(0.025, -0.025)" fill="url(#a-tri-grad)">
    <path d="{a1_paths[0]}" />
  </g>
  <g id="wordmark-hara" transform="translate(0, 443) scale(0.025, -0.025)" fill="#7B7B7B">
    {''.join(f'<path d="{p}"/>' for p in hara_paths)}
  </g>
  <g id="a2-tri" transform="translate(0, 443) scale(0.025, -0.025)" fill="url(#a-tri-grad)">
    <path d="{a2_paths[0]}" />
  </g>
  <g id="line-2" transform="translate(400, 342) scale(0.025, -0.025)" fill="#1B1B1B">
    {''.join(f'<path d="{p}"/>' for p in l2_paths)}
  </g>
</svg>'''

# 3. logo-full.svg: viewBox="120 82 1002 265"
full_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 82 1002 265" width="1002" height="265">
{defs}
  <g id="symbol" transform="translate(0, 443) scale(0.025, -0.025)">
    <path d="{sym_paths[0]}" fill="url(#arch-grad)" />
    <path d="{sym_paths[1]}" fill="url(#tri-grad)" />
  </g>
  <g id="wordmark-hari" transform="translate(0, 443) scale(0.025, -0.025)" fill="#1B1B1B">
    {''.join(f'<path d="{p}"/>' for p in hari_paths)}
  </g>
  <g id="a1-tri" transform="translate(0, 443) scale(0.025, -0.025)" fill="url(#a-tri-grad)">
    <path d="{a1_paths[0]}" />
  </g>
  <g id="wordmark-hara" transform="translate(0, 443) scale(0.025, -0.025)" fill="#7B7B7B">
    {''.join(f'<path d="{p}"/>' for p in hara_paths)}
  </g>
  <g id="a2-tri" transform="translate(0, 443) scale(0.025, -0.025)" fill="url(#a-tri-grad)">
    <path d="{a2_paths[0]}" />
  </g>
  <g id="line-2" transform="translate(400, 342) scale(0.025, -0.025)" fill="#1B1B1B">
    {''.join(f'<path d="{p}"/>' for p in l2_paths)}
  </g>
</svg>'''

# 4. logo-full-light.svg: charcoal -> #F6F3EE, grey -> #B9B9B9, crimson unchanged
full_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 82 1002 265" width="1002" height="265">
{defs}
  <g id="symbol" transform="translate(0, 443) scale(0.025, -0.025)">
    <path d="{sym_paths[0]}" fill="url(#arch-grad)" />
    <path d="{sym_paths[1]}" fill="url(#tri-grad)" />
  </g>
  <g id="wordmark-hari" transform="translate(0, 443) scale(0.025, -0.025)" fill="#F6F3EE">
    {''.join(f'<path d="{p}"/>' for p in hari_paths)}
  </g>
  <g id="a1-tri" transform="translate(0, 443) scale(0.025, -0.025)" fill="url(#a-tri-grad)">
    <path d="{a1_paths[0]}" />
  </g>
  <g id="wordmark-hara" transform="translate(0, 443) scale(0.025, -0.025)" fill="#B9B9B9">
    {''.join(f'<path d="{p}"/>' for p in hara_paths)}
  </g>
  <g id="a2-tri" transform="translate(0, 443) scale(0.025, -0.025)" fill="url(#a-tri-grad)">
    <path d="{a2_paths[0]}" />
  </g>
  <g id="line-2" transform="translate(400, 342) scale(0.025, -0.025)" fill="#F6F3EE">
    {''.join(f'<path d="{p}"/>' for p in l2_paths)}
  </g>
</svg>'''

# Write to public/brand/
with open('public/brand/logo-symbol.svg', 'w') as f:
    f.write(sym_svg)
with open('public/brand/logo-wordmark.svg', 'w') as f:
    f.write(wordmark_svg)
with open('public/brand/logo-full.svg', 'w') as f:
    f.write(full_svg)
with open('public/brand/logo-full-light.svg', 'w') as f:
    f.write(full_light_svg)

print("Saved all 4 SVGs in public/brand/.")
