"""
Generate a placeholder hero background image for the TPA Index website.
This creates an abstract globe/network visualization in IMF blue tones.
Replace with an actual high-quality photo (e.g., shipping container port,
globe, WTO headquarters) for the final site.

Run once: python3 assets/make_hero.py
Requires: pip install Pillow numpy
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import math

W, H = 1600, 900

img = Image.new("RGB", (W, H), (0, 36, 70))
draw = ImageDraw.Draw(img)

rng = np.random.default_rng(42)

# Background gradient
for y in range(H):
    t = y / H
    r = int(0   + t * 10)
    g = int(36  + t * 30)
    b = int(70  + t * 50)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Grid lines (latitude/longitude feel)
for lon in range(0, W, W // 18):
    draw.line([(lon, 0), (lon, H)], fill=(0, 76, 151, 40), width=1)
for lat in range(0, H, H // 10):
    draw.line([(0, lat), (W, lat)], fill=(0, 76, 151, 40), width=1)

# Node dots (cities / countries)
n_nodes = 80
nodes_x = rng.integers(60, W - 60, n_nodes)
nodes_y = rng.integers(40, H - 40, n_nodes)
# Weight some nodes heavier (major economies)
for i in range(n_nodes):
    r = int(rng.integers(2, 6))
    draw.ellipse(
        [(nodes_x[i] - r, nodes_y[i] - r),
         (nodes_x[i] + r, nodes_y[i] + r)],
        fill=(174, 203, 223, 180)
    )

# Trade flow arcs
for _ in range(120):
    i, j = rng.choice(n_nodes, 2, replace=False)
    x1, y1 = int(nodes_x[i]), int(nodes_y[i])
    x2, y2 = int(nodes_x[j]), int(nodes_y[j])
    alpha = int(rng.integers(15, 55))
    draw.line([(x1, y1), (x2, y2)], fill=(0, 113, 188, alpha), width=1)

# Soft glow overlay
img = img.filter(ImageFilter.GaussianBlur(radius=1))

img.save("assets/hero-bg.jpg", quality=90)
print("Hero background saved to assets/hero-bg.jpg")
print("Replace with a real photo for the final site.")
