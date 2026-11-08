#!/usr/bin/env python3
"""Generate the Sakhi mascot cast: animals drawn as people.

Each character stands upright on two legs, wears everyday Indian clothing
(saree, kurta, doctor's coat) and carries a prop tied to the app feature
they guide. All six share one body template so the cast looks consistent;
only the head, colours, outfit and prop change.

Run from the repository root:

    python3 tools/generate_characters.py

Writes one SVG per character into assets/characters/ plus a lineup.svg.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "characters"

W, H = 240, 320
INK = "#3b2a20"  # outline / facial-feature colour shared by the cast


# --------------------------------------------------------------------------
# Shared pieces
# --------------------------------------------------------------------------

def eyes(y=92, dx=18, cx=120, size=7):
    out = []
    for x in (cx - dx, cx + dx):
        out.append(f'<ellipse cx="{x}" cy="{y}" rx="{size}" ry="{size + 1}" fill="#fff"/>')
        out.append(f'<circle cx="{x + 1}" cy="{y + 1}" r="{size - 2.5}" fill="{INK}"/>')
        out.append(f'<circle cx="{x + 2.5}" cy="{y - 1.5}" r="1.6" fill="#fff"/>')
    return "\n".join(out)


def cheeks(y=108, dx=30, cx=120):
    return "\n".join(
        f'<ellipse cx="{x}" cy="{y}" rx="7" ry="4.5" fill="#f28b82" opacity=".55"/>'
        for x in (cx - dx, cx + dx)
    )


def smile(y=112, w=9, cx=120):
    return (f'<path d="M{cx - w} {y} Q{cx} {y + w} {cx + w} {y}" fill="none" '
            f'stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')


def bindi(y=72, color="#d62839"):
    return f'<circle cx="120" cy="{y}" r="3.2" fill="{color}"/>'


def legs(fur, sandal):
    return f"""
<rect x="100" y="240" width="16" height="56" rx="8" fill="{fur}"/>
<rect x="124" y="240" width="16" height="56" rx="8" fill="{fur}"/>
<ellipse cx="106" cy="297" rx="15" ry="6" fill="{sandal}"/>
<ellipse cx="134" cy="297" rx="15" ry="6" fill="{sandal}"/>"""


def arm(side, sleeve, fur, pose="down"):
    """side: 'l' or 'r'. pose: 'down', 'up' (raised, waving) or 'hold' (bent, forward)."""
    sx = 90 if side == "l" else 150
    s = -1 if side == "l" else 1
    if pose == "down":
        ex, ey, hx, hy = sx + 12 * s, 196, sx + 10 * s, 226
    elif pose == "up":
        ex, ey, hx, hy = sx + 22 * s, 140, sx + 30 * s, 118
    else:  # hold
        ex, ey, hx, hy = sx + 14 * s, 194, sx - 2 * s, 210
    return f"""
<path d="M{sx} 160 Q{ex} {ey - 10} {ex} {ey}" fill="none" stroke="{sleeve}" stroke-width="20" stroke-linecap="round"/>
<path d="M{ex} {ey} L{hx} {hy}" fill="none" stroke="{fur}" stroke-width="13" stroke-linecap="round"/>
<circle cx="{hx}" cy="{hy}" r="10" fill="{fur}"/>"""


def hand_xy(side, pose):
    sx = 90 if side == "l" else 150
    s = -1 if side == "l" else 1
    return {"down": (sx + 10 * s, 226), "up": (sx + 30 * s, 118),
            "hold": (sx - 2 * s, 210)}[pose]


def saree(main, pallu, border):
    return f"""
<path d="M86 150 Q120 138 154 150 L170 290 Q120 300 70 290 Z" fill="{main}"/>
<path d="M72 279 Q120 290 168 279 L170 290 Q120 300 70 290 Z" fill="{border}"/>
<path d="M88 150 Q118 146 152 158 L166 262 Q156 268 146 262 L98 172 Z" fill="{pallu}"/>
<path d="M146 262 Q156 268 166 262" fill="none" stroke="{border}" stroke-width="5"/>"""


def kurta(main, accent, pants):
    return f"""
<rect x="99" y="236" width="18" height="52" rx="7" fill="{pants}"/>
<rect x="123" y="236" width="18" height="52" rx="7" fill="{pants}"/>
<path d="M86 150 Q120 138 154 150 L164 252 Q120 262 76 252 Z" fill="{main}"/>
<path d="M78 244 Q120 254 162 244 L164 252 Q120 262 76 252 Z" fill="{accent}"/>
<path d="M108 146 L120 170 L132 146" fill="none" stroke="{accent}" stroke-width="5" stroke-linejoin="round"/>
<line x1="120" y1="170" x2="120" y2="210" stroke="{accent}" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round"/>"""


def dupatta(color):
    return f"""
<path d="M92 150 Q120 176 148 150 L158 158 Q120 194 82 158 Z" fill="{color}"/>
<path d="M150 154 Q166 200 160 246 L148 246 Q152 204 142 160 Z" fill="{color}"/>"""


def svg(title, desc, *parts):
    body = "\n".join(parts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">{title}</title>
<desc id="d">{desc}</desc>
<ellipse cx="120" cy="304" rx="64" ry="8" fill="#000" opacity=".12"/>
{body}
</svg>
"""


# --------------------------------------------------------------------------
# Characters
# --------------------------------------------------------------------------

def dr_ganga():
    """Elephant doctor - AI symptom checker."""
    fur, dark = "#a7b0bb", "#8a94a0"
    head = f"""
<ellipse cx="72" cy="96" rx="32" ry="38" fill="{dark}"/>
<ellipse cx="168" cy="96" rx="32" ry="38" fill="{dark}"/>
<ellipse cx="74" cy="98" rx="20" ry="26" fill="#e6b8c0"/>
<ellipse cx="166" cy="98" rx="20" ry="26" fill="#e6b8c0"/>
<circle cx="120" cy="92" r="46" fill="{fur}"/>
<path d="M110 104 Q106 132 112 146 Q118 156 128 148" fill="none" stroke="{fur}" stroke-width="18" stroke-linecap="round"/>
<path d="M104 140 l-8 6" stroke="#fffaf0" stroke-width="5" stroke-linecap="round"/>
<path d="M136 140 l8 6" stroke="#fffaf0" stroke-width="5" stroke-linecap="round"/>
{eyes(y=88, dx=20)}
<path d="M90 76 q8 -6 16 -2 M134 74 q8 -4 16 2" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
{cheeks(y=106, dx=32)}
{bindi(y=66)}
<g fill="none" stroke="#5a4636" stroke-width="2.5">
  <circle cx="102" cy="88" r="11"/><circle cx="138" cy="88" r="11"/><path d="M113 88 h14"/>
</g>"""
    coat = """
<path d="M86 150 Q120 138 154 150 L170 290 Q120 300 70 290 Z" fill="#2a9d8f"/>
<path d="M72 279 Q120 290 168 279 L170 290 Q120 300 70 290 Z" fill="#e9c46a"/>
<path d="M84 150 Q100 144 112 148 L110 264 L80 262 Z" fill="#fdfdfd"/>
<path d="M156 150 Q140 144 128 148 L130 264 L160 262 Z" fill="#fdfdfd"/>
<path d="M112 148 L104 176 M128 148 L136 176" stroke="#d9dde2" stroke-width="3"/>
<rect x="136" y="196" width="16" height="12" rx="2" fill="#d9dde2"/>
<path d="M140 196 v-6 M146 196 v-8" stroke="#2a6fdb" stroke-width="2.5" stroke-linecap="round"/>"""
    stetho = f"""
<path d="M106 150 Q100 200 120 204 Q140 200 134 150" fill="none" stroke="#344" stroke-width="3.5"/>
<circle cx="120" cy="208" r="7" fill="#c0c7cf" stroke="#344" stroke-width="2.5"/>"""
    hx, hy = hand_xy("r", "down")
    hx, hy = hx - 6, hy + 22
    clip = f"""
<rect x="{hx - 4}" y="{hy - 32}" width="26" height="34" rx="3" fill="#c8a27a"/>
<rect x="{hx - 1}" y="{hy - 28}" width="20" height="26" rx="2" fill="#fff"/>
<path d="M{hx + 3} {hy - 20} h12 M{hx + 3} {hy - 14} h12 M{hx + 3} {hy - 8} h8" stroke="#2a9d8f" stroke-width="2" stroke-linecap="round"/>
<path d="M{hx + 6} {hy - 25} h6" stroke="#d62839" stroke-width="3"/><path d="M{hx + 9} {hy - 28} v6" stroke="#d62839" stroke-width="3"/>"""
    return svg(
        "Dr. Ganga the Elephant",
        "An elephant woman doctor in a teal saree, white coat and round glasses, wearing a stethoscope and holding a clipboard.",
        legs(fur, "#7b4b2a"), coat, arm("l", "#fdfdfd", fur, "up"),
        clip, arm("r", "#fdfdfd", fur, "down"), stetho, head,
    )


def mira():
    """Mynah bird - voice assistant."""
    fur, beak = "#3d3a4b", "#f4b400"
    head = f"""
<path d="M112 46 q6 -18 18 -14 q-8 6 -6 16 Z" fill="{fur}"/>
<circle cx="120" cy="92" r="44" fill="{fur}"/>
<ellipse cx="102" cy="90" rx="13" ry="12" fill="{beak}"/>
<ellipse cx="138" cy="90" rx="13" ry="12" fill="{beak}"/>
{eyes(y=90, dx=18)}
<path d="M106 104 Q120 98 134 104 L120 126 Z" fill="#f59e0b"/>
<path d="M108 106 Q120 112 132 106" fill="none" stroke="#c2410c" stroke-width="2"/>
{cheeks(y=110, dx=30)}
{bindi(y=64, color="#f4b400")}"""
    waves = """
<g fill="none" stroke="#2a9d8f" stroke-width="4" stroke-linecap="round">
  <path d="M176 82 q8 10 0 20"/><path d="M188 74 q14 18 0 36"/><path d="M200 66 q20 26 0 52"/>
</g>"""
    hx, hy = hand_xy("l", "hold")
    phone = f"""
<rect x="{hx - 9}" y="{hy - 22}" width="20" height="34" rx="4" fill="#263238"/>
<rect x="{hx - 6}" y="{hy - 18}" width="14" height="24" rx="2" fill="#80cbc4"/>
<circle cx="{hx + 1}" cy="{hy - 6}" r="4" fill="#fff"/>
<rect x="{hx}" y="{hy - 8}" width="2" height="4" rx="1" fill="#2a9d8f"/>"""
    return svg(
        "Mira the Mynah",
        "A mynah bird woman in a green saree with a yellow border, speaking cheerfully into a phone with sound waves around her.",
        legs(beak, "#7b4b2a"), saree("#2e7d32", "#66bb6a", "#f4b400"),
        arm("r", "#2e7d32", fur, "down"), arm("l", "#66bb6a", fur, "hold"), phone,
        head, waves,
    )


def champa():
    """Hen - pregnancy and mother-child care (ASHA-style health worker)."""
    fur, comb = "#fff4e0", "#e63946"
    head = f"""
<path d="M104 54 q-2 -18 10 -16 q2 -14 14 -8 q10 -6 12 8 q10 2 4 16 Z" fill="{comb}"/>
<circle cx="120" cy="92" r="44" fill="{fur}"/>
{eyes(y=88, dx=17)}
<path d="M110 100 L130 100 L120 116 Z" fill="#f59e0b"/>
<path d="M115 116 q5 14 10 0" fill="{comb}"/>
{cheeks(y=104, dx=30)}
{bindi(y=68)}"""
    hx, hy = hand_xy("r", "down")
    bag = f"""
<path d="M150 160 L{hx} {hy - 22}" stroke="#7b4b2a" stroke-width="4"/>
<rect x="{hx - 18}" y="{hy - 24}" width="36" height="30" rx="6" fill="#fff"/>
<rect x="{hx - 18}" y="{hy - 24}" width="36" height="9" rx="4" fill="#c2185b"/>
<path d="M{hx - 7} {hy - 4} h14 M{hx} {hy - 11} v14" stroke="{comb}" stroke-width="5"/>"""
    belly = '<path d="M100 196 Q122 182 140 198 Q144 226 120 234 Q100 228 100 196 Z" fill="#f48fb1" opacity=".35"/>'
    heart = """<path d="M58 120 c-6 -8 -18 -2 -12 8 l12 12 l12 -12 c6 -10 -6 -16 -12 -8 Z" fill="#e63946"/>"""
    return svg(
        "Champa the Hen",
        "A motherly hen health worker in a pink saree, carrying a first-aid bag and waving warmly.",
        legs("#f59e0b", "#7b4b2a"), saree("#ec407a", "#c2185b", "#ffd54f"), belly,
        arm("l", "#c2185b", fur, "up"), arm("r", "#ec407a", fur, "down"), bag,
        head, heart,
    )


def chiku():
    """Palm squirrel - facility finder."""
    fur, light = "#a0714f", "#e8cfb4"
    tail = f"""
<path d="M150 260 Q214 250 206 170 Q200 110 168 120 Q196 150 176 196 Q164 226 146 236 Z" fill="{fur}"/>
<path d="M162 240 Q196 226 194 172" fill="none" stroke="{light}" stroke-width="6" stroke-linecap="round"/>"""
    head = f"""
<path d="M86 64 L82 30 L108 52 Z" fill="{fur}"/><path d="M154 64 L158 30 L132 52 Z" fill="{fur}"/>
<path d="M89 58 L87 38 L102 51 Z" fill="#e6a0a8"/><path d="M151 58 L153 38 L138 51 Z" fill="#e6a0a8"/>
<circle cx="120" cy="92" r="44" fill="{fur}"/>
<path d="M110 50 v22 M120 48 v24 M130 50 v22" stroke="{light}" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="120" cy="110" rx="26" ry="20" fill="{light}"/>
{eyes(y=88, dx=19)}
<ellipse cx="120" cy="104" rx="5" ry="4" fill="{INK}"/>
<path d="M114 118 h12 v6 h-12 Z" fill="#fff" stroke="{INK}" stroke-width="1.5"/>
{cheeks(y=108, dx=32)}"""
    hx, hy = hand_xy("l", "up")
    pin = f"""
<path d="M{hx} {hy - 54} a18 18 0 0 1 18 18 c0 14 -18 30 -18 30 s-18 -16 -18 -30 a18 18 0 0 1 18 -18 Z" fill="#e63946"/>
<circle cx="{hx}" cy="{hy - 36}" r="7" fill="#fff"/>"""
    satchel = """
<path d="M94 152 L150 230" stroke="#5d4037" stroke-width="5"/>
<rect x="138" y="222" width="30" height="24" rx="5" fill="#8d6e63"/>
<rect x="138" y="222" width="30" height="9" rx="4" fill="#6d4c41"/>"""
    return svg(
        "Chiku the Squirrel",
        "A palm squirrel man in a mustard kurta with a satchel, raising a red map pin to show the way to the nearest clinic.",
        tail, legs(fur, "#4e342e"), kurta("#f2b134", "#b5651d", "#fff8e1"), satchel,
        arm("r", "#f2b134", fur, "down"), arm("l", "#f2b134", fur, "up"), pin, head,
    )


def bhoomi():
    """Rabbit - nutrition scanner."""
    fur = "#efe9e4"
    head = f"""
<ellipse cx="102" cy="34" rx="12" ry="34" fill="{fur}" transform="rotate(-10 102 60)"/>
<ellipse cx="140" cy="34" rx="12" ry="34" fill="{fur}" transform="rotate(12 140 60)"/>
<ellipse cx="102" cy="36" rx="6" ry="24" fill="#f4a6b8" transform="rotate(-10 102 60)"/>
<ellipse cx="140" cy="36" rx="6" ry="24" fill="#f4a6b8" transform="rotate(12 140 60)"/>
<circle cx="120" cy="96" r="42" fill="{fur}"/>
{eyes(y=92, dx=17)}
<path d="M115 104 h10 l-5 6 Z" fill="#e57399"/>
<path d="M120 110 v5 M120 115 q-6 6 -11 2 M120 115 q6 6 11 2" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
<path d="M90 106 h-18 M90 112 l-16 4 M150 106 h18 M150 112 l16 4" stroke="#b0a49a" stroke-width="1.8" stroke-linecap="round"/>
{cheeks(y=110, dx=28)}
{bindi(y=72)}"""
    apron = """
<path d="M100 166 h40 l8 82 q-28 8 -56 0 Z" fill="#fff8e1"/>
<path d="M100 166 q20 -16 40 0" fill="none" stroke="#fff8e1" stroke-width="4"/>
<path d="M110 196 h20 v16 h-20 Z" fill="none" stroke="#8bc34a" stroke-width="2.5"/>"""
    hx, hy = hand_xy("r", "hold")
    basket = f"""
<path d="M{hx - 26} {hy - 8} q26 -40 52 0" fill="none" stroke="#8d6e63" stroke-width="4"/>
<circle cx="{hx - 12}" cy="{hy - 10}" r="9" fill="#43a047"/>
<circle cx="{hx + 2}" cy="{hy - 14}" r="9" fill="#e53935"/>
<path d="M{hx + 8} {hy - 6} l16 -18" stroke="#fb8c00" stroke-width="7" stroke-linecap="round"/>
<path d="M{hx + 22} {hy - 26} l4 -6 M{hx + 24} {hy - 22} l7 -2" stroke="#43a047" stroke-width="3" stroke-linecap="round"/>
<path d="M{hx - 28} {hy - 8} h56 l-6 24 h-44 Z" fill="#c69c6d"/>
<path d="M{hx - 24} {hy} h48 M{hx - 20} {hy + 8} h40" stroke="#a1785a" stroke-width="2"/>"""
    return svg(
        "Bhoomi the Rabbit",
        "A rabbit woman in an orange saree and cream apron, carrying a basket of fresh greens, tomatoes and carrots.",
        legs(fur, "#7b4b2a"), saree("#ef6c00", "#ffa726", "#2e7d32"), apron,
        arm("l", "#ffa726", fur, "up"), arm("r", "#ef6c00", fur, "hold"), basket, head,
    )


def tara():
    """Tigress - SOS and safety."""
    fur, white = "#f08c2e", "#fff6ea"
    head = f"""
<circle cx="84" cy="56" r="15" fill="{fur}"/><circle cx="156" cy="56" r="15" fill="{fur}"/>
<circle cx="84" cy="56" r="8" fill="{INK}"/><circle cx="156" cy="56" r="8" fill="{INK}"/>
<circle cx="120" cy="92" r="46" fill="{fur}"/>
<path d="M120 46 l-6 14 h12 Z M106 50 l-2 14 l8 -10 Z M134 50 l2 14 l-8 -10 Z" fill="{INK}"/>
<path d="M74 84 l14 4 l-14 6 Z M166 84 l-14 4 l14 6 Z M76 104 l12 0 l-10 6 Z M164 104 l-12 0 l10 6 Z" fill="{INK}"/>
<ellipse cx="120" cy="114" rx="28" ry="20" fill="{white}"/>
{eyes(y=88, dx=19)}
<path d="M113 104 h14 l-7 7 Z" fill="#e57399"/>
<path d="M120 111 v4 M120 115 q-6 6 -11 1 M120 115 q6 6 11 1" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
{cheeks(y=106, dx=34)}
{bindi(y=72)}"""
    hx, hy = hand_xy("l", "up")
    badge = f"""
<circle cx="{hx}" cy="{hy - 24}" r="18" fill="#d62839" stroke="#fff" stroke-width="3"/>
<text x="{hx}" y="{hy - 19}" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="#fff" text-anchor="middle">SOS</text>"""
    whistle = """
<path d="M120 150 L120 176" stroke="#ffd54f" stroke-width="2"/>
<rect x="112" y="176" width="18" height="10" rx="5" fill="#ffd54f"/>"""
    return svg(
        "Tara the Tigress",
        "A brave tigress woman in a maroon kurta and red dupatta with a whistle, holding up a red SOS button.",
        legs(fur, "#3e2723"), kurta("#7b1e3a", "#ffd54f", "#2b2d42"), dupatta("#d62839"),
        whistle, arm("r", "#7b1e3a", fur, "down"), arm("l", "#7b1e3a", fur, "up"), badge, head,
    )


CAST = {
    "dr_ganga_elephant": dr_ganga,
    "mira_mynah": mira,
    "champa_hen": champa,
    "chiku_squirrel": chiku,
    "bhoomi_rabbit": bhoomi,
    "tara_tigress": tara,
}


def strip_outer(markup):
    """Return the inner content of a character SVG for embedding in the lineup."""
    start = markup.index("</desc>") + len("</desc>")
    return markup[start:markup.rindex("</svg>")]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    groups = []
    for i, (slug, make) in enumerate(CAST.items()):
        markup = make()
        (OUT / f"{slug}.svg").write_text(markup, encoding="utf-8")
        groups.append(f'<g transform="translate({i * W} 0)">{strip_outer(markup)}</g>')
    lineup = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W * len(CAST)} {H}" '
              f'width="{W * len(CAST)}" height="{H}" role="img" aria-label="The Sakhi cast">\n'
              + "\n".join(groups) + "\n</svg>\n")
    (OUT / "lineup.svg").write_text(lineup, encoding="utf-8")
    print(f"Wrote {len(CAST) + 1} files to {OUT}")


if __name__ == "__main__":
    main()
