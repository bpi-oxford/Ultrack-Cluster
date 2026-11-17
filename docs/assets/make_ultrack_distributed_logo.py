"""Ultrack-Distributed mark for the CBIAS deck: the official ultrack logo (royerlab/ultrack docs, ultrack_no_bkg.svg,
rendered to assets/ultrack_logo.png) with "Distributed" appended and its two arrows extended underneath. The extension
is drawn in alternating sections -- original colour = even time windows, lighter tint = odd windows -- echoing
Ultrack-Cluster's solve order (even windows first, then each odd window once its neighbours finish).

Geometry measured on the 1200 x 471 render: blue line rows 291-324, navy line rows 410-443, arrowheads beyond x 1105;
"ultrack" x-height is 171 px (rows 64-235, baseline 235), so "Distributed" is set in Inter SemiBold (closest installed
match to the ultrack lettering) sized to that x-height on the same baseline.

Usage: python3 docs/assets/make_ultrack_distributed_logo.py   (writes docs/assets/ultrack_distributed_logo.png)

ultrack_logo_source.png = royerlab/ultrack docs/source/_static/ultrack_no_bkg.svg rendered at 1200 px wide
(ultrack is BSD-3-Clause; the ultrack logo belongs to its authors, used here with attribution).
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

A = Path(__file__).resolve().parent   # docs/assets: reads ultrack_logo_source.png, writes ultrack_distributed_logo.png
FONT = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"   # closest installed match to the ultrack lettering
BLUE, NAVY = (29, 122, 233), (22, 45, 80)                 # the logo's own two colours
TINT = {BLUE: (150, 196, 246), NAVY: (120, 134, 158)}      # odd-window tint of each
CUT, LINES = 1105, ((291, 325, BLUE), (410, 444, NAVY))


def main():
    logo = Image.open(A / "ultrack_logo_source.png").convert("RGBA")
    W, H = logo.size
    left, heads = logo.crop((0, 0, CUT, H)), logo.crop((CUT, 0, W, H))
    hp = heads.load()                                       # keep only the arrowheads: clear the sliver of "k"
    for yy in range(250):
        for xx in range(heads.size[0]):
            hp[xx, yy] = (0, 0, 0, 0)
    # size so the lowercase x-height matches ultrack's (171 px: rows 64-235 of the 471-px render)
    fx = ImageFont.truetype(FONT, 1000).getbbox("x")
    font = ImageFont.truetype(FONT, round(1000 * 171 / (fx[3] - fx[1])))
    word = "Distributed"
    bb = font.getbbox(word)                                 # (x0, y0, x1, y1) of the inked text
    gap = 70
    ext = (bb[2] - bb[0]) + gap + 40
    PAD = 40                                                # headroom: i-dots and D sit above the "l" top
    out = Image.new("RGBA", (CUT + ext + (W - CUT), H + PAD), (0, 0, 0, 0))
    out.paste(left, (0, PAD))
    d = ImageDraw.Draw(out)
    base = font.getbbox("x")[3]                             # baseline offset of the x glyph
    d.text((CUT + gap - bb[0], PAD + 235 - base), word, font=font, fill=NAVY + (255,))   # baseline on ultrack's
    n_sec = 4                                                                       # alternating window sections
    xs = np.linspace(CUT, CUT + ext, n_sec + 1).round().astype(int)
    for y0, y1, col in LINES:
        for k in range(n_sec):
            c = col if k % 2 else TINT[col]                 # the original logo part plays window 0 (even)
            d.rectangle((xs[k], PAD + y0, xs[k + 1] - 1, PAD + y1 - 1), fill=c + (255,))
    out.paste(heads, (CUT + ext, PAD), heads)
    out.save(A / "ultrack_distributed_logo.png")
    print("wrote", A / "ultrack_distributed_logo.png", out.size)


if __name__ == "__main__":
    main()
