"""Generate the hero SVGs for the profile README designs.

Usage: python3 gen_svgs.py designs   (from the repository root)
Writes designs/<design>/assets/*.svg, and assets/label.svg for the live profile.
"""
import hashlib
import os
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, Inter, sans-serif"
BOLD = ' font-weight="700"'
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'JetBrains Mono', monospace"


def write(design, name, svg):
    d = os.path.join(OUT, design, "assets")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "w") as f:
        f.write(svg)


# ---------------------------------------------------------------- label

def barcode(x0, y0, width, height, seed):
    h = hashlib.sha256(seed.encode()).digest() * 8
    bars, x, i = [], x0, 0
    while x < x0 + width - 6:
        w = 2 + h[i] % 4
        gap = 2 + h[i + 1] % 3
        bars.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{height}"/>')
        x += w + gap
        i += 2
    return "\n    ".join(bars)


def label_svg():
    ink = "#1f2328"
    paper = "#fffdf7"
    muted = "#6e7781"
    red = "#c62828"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="440" viewBox="0 0 860 440" role="img" aria-label="Shipping label: Akhileshwar Reddy, backend engineer, Bangalore, India">
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; }}
    .cap {{ font: 700 11px {SANS}; letter-spacing: 2px; fill: {muted}; }}
    .stamp {{ transform-box: fill-box; transform-origin: center; opacity: 0;
             animation: thump .7s cubic-bezier(.2,.9,.3,1.2) .8s forwards; }}
    @keyframes thump {{
      0%   {{ opacity: 0;   transform: rotate(-12deg) scale(1.8); }}
      70%  {{ opacity: .9;  transform: rotate(-12deg) scale(.94); }}
      100% {{ opacity: .85; transform: rotate(-12deg) scale(1); }}
    }}
  </style>
  <rect x="1.5" y="1.5" width="857" height="437" rx="14" fill="{paper}" stroke="{ink}" stroke-width="3"/>

  <!-- header band -->
  <path d="M1.5 70 V15.5 a14 14 0 0 1 14 -14 H844.5 a14 14 0 0 1 14 14 V70 Z" fill="{ink}"/>
  <text x="28" y="47" class="sans" font-size="28" font-weight="800" letter-spacing="6" fill="{paper}">PRIORITY</text>
  <text x="832" y="44" class="mono" font-size="14" text-anchor="end" letter-spacing="1" fill="{paper}">BACKEND ENGINEER · RUBY ON RAILS</text>

  <!-- from / to -->
  <line x1="430" y1="70" x2="430" y2="170" stroke="{ink}" stroke-width="2"/>
  <line x1="0" y1="170" x2="860" y2="170" stroke="{ink}" stroke-width="2"/>
  <text x="28" y="98" class="cap">FROM</text>
  <text x="28" y="130" class="sans" font-size="24" font-weight="700" fill="{ink}">Akhileshwar Reddy</text>
  <text x="28" y="154" class="sans" font-size="16" fill="{ink}">Bangalore, India</text>
  <text x="456" y="98" class="cap">TO</text>
  <text x="456" y="140" class="sans" font-size="28" font-weight="700" fill="{ink}">Production</text>

  <!-- routing box + contents -->
  <line x1="200" y1="170" x2="200" y2="330" stroke="{ink}" stroke-width="2"/>
  <line x1="0" y1="330" x2="860" y2="330" stroke="{ink}" stroke-width="2"/>
  <text x="100" y="262" class="sans" font-size="76" font-weight="800" text-anchor="middle" fill="{ink}">6+</text>
  <text x="100" y="296" class="sans" font-size="15" font-weight="700" letter-spacing="5" text-anchor="middle" fill="{ink}">YEARS</text>

  <text x="226" y="198" class="cap">CONTENTS</text>
  <text x="226" y="222" class="sans" font-size="17" fill="{ink}">Ruby on Rails services for logistics and HR/benefits SaaS</text>
  <text x="226" y="256" class="cap">PACKED WITH</text>
  <text x="226" y="278" class="mono" font-size="14" fill="{ink}">RUBY · RAILS · POSTGRESQL · REDIS · SIDEKIQ · NODE.JS</text>
  <text x="226" y="304" class="cap">SHIPS VIA</text>
  <text x="226" y="324" class="mono" font-size="14" fill="{ink}" dy="-2">DOCKER · GCP · AWS · GITLAB CI/CD · CLAUDE CODE</text>

  <!-- barcode + delivery -->
  <g fill="{ink}">
    {barcode(28, 348, 520, 52, "AkhileshwarReddy")}
  </g>
  <text x="28" y="422" class="mono" font-size="13" letter-spacing="3" fill="{ink}">GITHUB.COM/AKHILESHWARREDDY</text>
  <line x1="580" y1="330" x2="580" y2="438" stroke="{ink}" stroke-width="2"/>
  <text x="604" y="358" class="cap">DELIVER TO</text>
  <text x="604" y="384" class="mono" font-size="14" fill="{ink}">linkedin.com/in/</text>
  <text x="604" y="404" class="mono" font-size="14" fill="{ink}">akhileshwarreddy</text>

  <!-- stamp -->
  <g class="stamp">
    <rect x="698" y="88" width="146" height="66" rx="10" fill="none" stroke="{red}" stroke-width="4"/>
    <rect x="705" y="95" width="132" height="52" rx="6" fill="none" stroke="{red}" stroke-width="1.5"/>
    <text x="771" y="116" class="sans" font-size="11" font-weight="800" letter-spacing="3" text-anchor="middle" fill="{red}">SHIPPED FROM</text>
    <text x="771" y="138" class="sans" font-size="16" font-weight="800" letter-spacing="2" text-anchor="middle" fill="{red}">BANGALORE</text>
  </g>
</svg>
"""


def label_ai_svg():
    ink = "#1f2328"
    paper = "#fffdf7"
    muted = "#6e7781"
    claude = "#d97757"
    claude_ink = "#b4532f"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="480" viewBox="0 0 860 480" role="img" aria-label="Shipping label: Akhileshwar Reddy, backend engineer, Bangalore, India. 6+ years of Ruby on Rails services for logistics and HR/benefits SaaS, built with AI-assisted development using Claude Code.">
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; }}
    .cap {{ font: 700 11px {SANS}; letter-spacing: 2px; fill: {muted}; }}
    .sticker {{ transform-box: fill-box; transform-origin: center; opacity: 0;
               animation: thump .7s cubic-bezier(.2,.9,.3,1.2) .8s forwards; }}
    .spark {{ transform-box: fill-box; transform-origin: center; animation: spin 6s linear 1.5s infinite; }}
    @keyframes thump {{
      0%   {{ opacity: 0; transform: rotate(-10deg) scale(1.8); }}
      70%  {{ opacity: 1; transform: rotate(-10deg) scale(.94); }}
      100% {{ opacity: 1; transform: rotate(-10deg) scale(1); }}
    }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  </style>
  <rect x="1.5" y="1.5" width="857" height="477" rx="14" fill="{paper}" stroke="{ink}" stroke-width="3"/>

  <!-- header band -->
  <path d="M1.5 70 V15.5 a14 14 0 0 1 14 -14 H844.5 a14 14 0 0 1 14 14 V70 Z" fill="{ink}"/>
  <text x="28" y="47" class="sans" font-size="28" font-weight="800" letter-spacing="6" fill="{paper}">EXPRESS</text>
  <text x="832" y="44" class="mono" font-size="14" text-anchor="end" letter-spacing="1" fill="{paper}">BACKEND ENGINEER · RAILS · <tspan fill="{claude}">AI-ASSISTED</tspan></text>

  <!-- from / to -->
  <line x1="430" y1="70" x2="430" y2="170" stroke="{ink}" stroke-width="2"/>
  <line x1="0" y1="170" x2="860" y2="170" stroke="{ink}" stroke-width="2"/>
  <text x="28" y="98" class="cap">FROM</text>
  <text x="28" y="130" class="sans" font-size="24" font-weight="700" fill="{ink}">Akhileshwar Reddy</text>
  <text x="28" y="154" class="sans" font-size="16" fill="{ink}">Bangalore, India</text>
  <text x="456" y="98" class="cap">TO</text>
  <text x="456" y="140" class="sans" font-size="28" font-weight="700" fill="{ink}">Production</text>

  <!-- routing box + contents -->
  <line x1="200" y1="170" x2="200" y2="386" stroke="{ink}" stroke-width="2"/>
  <line x1="0" y1="386" x2="860" y2="386" stroke="{ink}" stroke-width="2"/>
  <text x="100" y="290" class="sans" font-size="76" font-weight="800" text-anchor="middle" fill="{ink}">6+</text>
  <text x="100" y="324" class="sans" font-size="15" font-weight="700" letter-spacing="5" text-anchor="middle" fill="{ink}">YEARS</text>

  <text x="226" y="198" class="cap">CONTENTS</text>
  <text x="226" y="222" class="sans" font-size="17" fill="{ink}">Ruby on Rails services for logistics and HR/benefits SaaS</text>
  <text x="226" y="252" class="cap">PACKED WITH</text>
  <text x="226" y="274" class="mono" font-size="14" fill="{ink}">RUBY · RAILS · POSTGRESQL · REDIS · SIDEKIQ · NODE.JS</text>
  <text x="226" y="302" class="cap">SHIPS VIA</text>
  <text x="226" y="324" class="mono" font-size="14" fill="{ink}">DOCKER · GCP · AWS · GITLAB CI/CD</text>
  <rect x="212" y="334" width="636" height="44" rx="8" fill="{claude}" fill-opacity=".10" stroke="{claude}" stroke-opacity=".5"/>
  <text x="226" y="352" class="cap" style="fill: {claude_ink}">BUILT WITH AI</text>
  <text x="226" y="371" class="mono" font-size="14" font-weight="700" fill="{claude_ink}">CLAUDE CODE · AI-ASSISTED DEVELOPMENT</text>

  <!-- barcode + delivery -->
  <g fill="{ink}">
    {barcode(28, 402, 520, 44, "AkhileshwarReddy")}
  </g>
  <text x="28" y="466" class="mono" font-size="13" letter-spacing="3" fill="{ink}">GITHUB.COM/AKHILESHWARREDDY</text>
  <line x1="580" y1="386" x2="580" y2="478" stroke="{ink}" stroke-width="2"/>
  <text x="604" y="412" class="cap">DELIVER TO</text>
  <text x="604" y="438" class="mono" font-size="14" fill="{ink}">linkedin.com/in/</text>
  <text x="604" y="458" class="mono" font-size="14" fill="{ink}">akhileshwarreddy</text>

  <!-- AI sticker -->
  <g class="sticker">
    <circle cx="790" cy="120" r="44" fill="{claude}"/>
    <circle cx="790" cy="120" r="38" fill="none" stroke="{paper}" stroke-width="1.5" stroke-dasharray="3 4"/>
    <text x="790" y="104" class="spark" font-size="16" text-anchor="middle" fill="{paper}">✻</text>
    <text x="790" y="130" class="sans" font-size="24" font-weight="800" text-anchor="middle" fill="{paper}">AI</text>
    <text x="790" y="146" class="sans" font-size="9" font-weight="800" letter-spacing="2" text-anchor="middle" fill="{paper}">ASSISTED</text>
  </g>
</svg>
"""


def label_combo_svg():
    ink = "#1f2328"
    paper = "#fffdf7"
    muted = "#6e7781"
    claude = "#d97757"
    claude_ink = "#b4532f"
    red = "#c62828"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="480" viewBox="0 0 860 480" role="img" aria-label="Shipping label: Akhileshwar Reddy, backend engineer, Bangalore, India. 6+ years of Ruby on Rails services for logistics and HR/benefits SaaS, built with AI-assisted development using Claude Code.">
  <style>
    .sans {{ font-family: {SANS}; }}
    .mono {{ font-family: {MONO}; }}
    .cap {{ font: 700 11px {SANS}; letter-spacing: 2px; fill: {muted}; }}
    .stamp {{ transform-box: fill-box; transform-origin: center; opacity: 0;
             animation: thump .7s cubic-bezier(.2,.9,.3,1.2) .8s forwards; }}
    @keyframes thump {{
      0%   {{ opacity: 0;   transform: rotate(-12deg) scale(1.8); }}
      70%  {{ opacity: .9;  transform: rotate(-12deg) scale(.94); }}
      100% {{ opacity: .85; transform: rotate(-12deg) scale(1); }}
    }}
  </style>
  <rect x="1.5" y="1.5" width="857" height="477" rx="14" fill="{paper}" stroke="{ink}" stroke-width="3"/>

  <!-- header band -->
  <path d="M1.5 70 V15.5 a14 14 0 0 1 14 -14 H844.5 a14 14 0 0 1 14 14 V70 Z" fill="{ink}"/>
  <text x="28" y="47" class="sans" font-size="28" font-weight="800" letter-spacing="6" fill="{paper}">EXPRESS</text>
  <text x="832" y="44" class="mono" font-size="14" text-anchor="end" letter-spacing="1" fill="{paper}">BACKEND ENGINEER · RAILS · <tspan fill="{claude}">AI-ASSISTED</tspan></text>

  <!-- from / to -->
  <line x1="430" y1="70" x2="430" y2="170" stroke="{ink}" stroke-width="2"/>
  <line x1="0" y1="170" x2="860" y2="170" stroke="{ink}" stroke-width="2"/>
  <text x="28" y="98" class="cap">FROM</text>
  <text x="28" y="130" class="sans" font-size="24" font-weight="700" fill="{ink}">Akhileshwar Reddy</text>
  <text x="28" y="154" class="sans" font-size="16" fill="{ink}">Bangalore, India</text>
  <text x="456" y="98" class="cap">TO</text>
  <text x="456" y="140" class="sans" font-size="28" font-weight="700" fill="{ink}">Production</text>

  <!-- routing box + contents -->
  <line x1="200" y1="170" x2="200" y2="386" stroke="{ink}" stroke-width="2"/>
  <line x1="0" y1="386" x2="860" y2="386" stroke="{ink}" stroke-width="2"/>
  <text x="100" y="290" class="sans" font-size="76" font-weight="800" text-anchor="middle" fill="{ink}">6+</text>
  <text x="100" y="324" class="sans" font-size="15" font-weight="700" letter-spacing="5" text-anchor="middle" fill="{ink}">YEARS</text>

  <text x="226" y="198" class="cap">CONTENTS</text>
  <text x="226" y="222" class="sans" font-size="17" fill="{ink}">Ruby on Rails services for logistics and HR/benefits SaaS</text>
  <text x="226" y="252" class="cap">PACKED WITH</text>
  <text x="226" y="274" class="mono" font-size="14" fill="{ink}">RUBY · RAILS · POSTGRESQL · REDIS · SIDEKIQ · NODE.JS</text>
  <text x="226" y="302" class="cap">SHIPS VIA</text>
  <text x="226" y="324" class="mono" font-size="14" fill="{ink}">DOCKER · GCP · AWS · GITLAB CI/CD</text>
  <rect x="212" y="334" width="636" height="44" rx="8" fill="{claude}" fill-opacity=".10" stroke="{claude}" stroke-opacity=".5"/>
  <text x="226" y="352" class="cap" style="fill: {claude_ink}">BUILT WITH AI</text>
  <text x="226" y="371" class="mono" font-size="14" font-weight="700" fill="{claude_ink}">CLAUDE CODE · AI-ASSISTED DEVELOPMENT</text>

  <!-- barcode + delivery -->
  <g fill="{ink}">
    {barcode(28, 402, 520, 44, "AkhileshwarReddy")}
  </g>
  <text x="28" y="466" class="mono" font-size="13" letter-spacing="3" fill="{ink}">GITHUB.COM/AKHILESHWARREDDY</text>
  <line x1="580" y1="386" x2="580" y2="478" stroke="{ink}" stroke-width="2"/>
  <text x="604" y="412" class="cap">DELIVER TO</text>
  <text x="604" y="438" class="mono" font-size="14" fill="{ink}">linkedin.com/in/</text>
  <text x="604" y="458" class="mono" font-size="14" fill="{ink}">akhileshwarreddy</text>

  <!-- stamp -->
  <g class="stamp">
    <rect x="698" y="88" width="146" height="66" rx="10" fill="none" stroke="{red}" stroke-width="4"/>
    <rect x="705" y="95" width="132" height="52" rx="6" fill="none" stroke="{red}" stroke-width="1.5"/>
    <text x="771" y="116" class="sans" font-size="11" font-weight="800" letter-spacing="3" text-anchor="middle" fill="{red}">SHIPPED FROM</text>
    <text x="771" y="138" class="sans" font-size="16" font-weight="800" letter-spacing="2" text-anchor="middle" fill="{red}">BANGALORE</text>
  </g>
</svg>
"""


# ---------------------------------------------------------------- terminal

GREEN, FG, DIM, BLUE, WHITE, CLAUDE = "#3fb950", "#c9d1d9", "#8b949e", "#79c0ff", "#f0f6fc", "#d97757"

TERMINAL_SCRIPT = [
    ("cmd", "whoami"),
    ("out", [("Akhileshwar Reddy", WHITE, True), (" · backend engineer · Bangalore, India", FG, False)]),
    ("cmd", "cat about.txt"),
    ("out", [("6+ years building Ruby on Rails services for logistics and HR/benefits SaaS.", FG, False)]),
    ("cmd", "tree ~/stack"),
    ("out", [("├── ", DIM, False), ("code   ", BLUE, False), ("ruby · rails · node.js", FG, False)]),
    ("out", [("├── ", DIM, False), ("data   ", BLUE, False), ("postgresql · redis · sidekiq", FG, False)]),
    ("out", [("├── ", DIM, False), ("infra  ", BLUE, False), ("docker · gcp · aws · gitlab-ci/cd", FG, False)]),
    ("out", [("└── ", DIM, False), ("tools  ", BLUE, False), ("claude-code", FG, False)]),
    ("cmd", "ls ~/companies"),
    ("out", [("easyship  rootquotient  plansource  mountblue  snovasys", FG, False)]),
]

TERMINAL_AI_SCRIPT = [
    ("cmd", "whoami"),
    ("out", [("Akhileshwar Reddy", WHITE, True), (" · backend engineer · Bangalore, India", FG, False)]),
    ("cmd", 'claude "summarize my work"'),
    ("think", 1.6),
    ("ans", [("● ", CLAUDE, False), ("6+ years building Ruby on Rails services for logistics and HR/benefits SaaS.", FG, False)]),
    ("ans", [("● ", CLAUDE, False), ("Builds with  ", BLUE, False), ("ruby · rails · node.js · postgresql · redis · sidekiq", FG, False)]),
    ("ans", [("● ", CLAUDE, False), ("Ships with   ", BLUE, False), ("docker · gcp · aws · gitlab-ci/cd", FG, False)]),
    ("ans", [("● ", CLAUDE, False), ("Codes with   ", BLUE, False), ("claude-code", CLAUDE, True), (" · AI-assisted development", FG, False)]),
    ("cmd", "ls ~/companies"),
    ("out", [("easyship  rootquotient  plansource  mountblue  snovasys", FG, False)]),
]

TERMINAL_ARIA = ("Terminal: Akhileshwar Reddy, backend engineer in Bangalore, India. 6+ years building Ruby on Rails "
                 "services for logistics and HR/benefits SaaS. Stack: Ruby, Rails, Node.js, PostgreSQL, Redis, Sidekiq, "
                 "Docker, GCP, AWS, GitLab CI/CD, Claude Code. Companies: Easyship, RootQuotient, PlanSource, MountBlue, Snovasys.")


def terminal_svg(script=TERMINAL_SCRIPT, title="akhileshwar@bangalore: ~"):
    ch, lh, x0, y0 = 9.4, 25, 26, 78
    t, per_char, parts, defs, line = 0.5, 0.055, [], [], 0
    for i, (kind, content) in enumerate(script):
        y = y0 + line * lh
        nxt = script[i + 1][0] if i + 1 < len(script) else None
        if kind == "cmd":
            n = len(content)
            steps = ";".join(f"{k * ch:.1f}" for k in range(n + 1)) + f";{(n + 1) * ch:.1f}"
            dur = per_char * (n + 1)
            defs.append(
                f'<clipPath id="c{i}"><rect x="{x0 + 2 * ch:.1f}" y="{y - 18}" width="0" height="{lh}">'
                f'<animate attributeName="width" values="{steps}" calcMode="discrete" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"/>'
                f"</rect></clipPath>"
            )
            parts.append(
                f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
                f'<text x="{x0}" y="{y}" fill="{GREEN}">$</text>'
                f'<text x="{x0 + 2 * ch:.1f}" y="{y}" fill="{WHITE}" clip-path="url(#c{i})">{escape(content)}</text></g>'
            )
            t += dur + 0.35
            line += 1
        elif kind == "think":
            # spinner occupies the next line, then the answer replaces it
            parts.append(
                f'<text x="{x0 + 2 * ch:.1f}" y="{y}" opacity="0" xml:space="preserve">'
                f'<tspan fill="{CLAUDE}">✻<animate attributeName="opacity" values="1;.25;1" dur=".8s" repeatCount="indefinite"/></tspan>'
                f'<tspan fill="{DIM}"> Thinking…</tspan>'
                f'<set attributeName="opacity" to="1" begin="{t:.2f}s"/>'
                f'<set attributeName="opacity" to="0" begin="{t + content:.2f}s" fill="freeze"/></text>'
            )
            t += content
        else:
            indent = 2 * ch if kind == "ans" else 0
            spans = "".join(
                f'<tspan fill="{c}"{BOLD if b else ""}>{escape(s)}</tspan>' for s, c, b in content
            )
            if kind == "ans":
                # stream the answer in word by word, like a model response
                full = "".join(s for s, _, _ in content)
                ends = [k for k in range(1, len(full) + 1) if k == len(full) or (full[k] == " " and full[k - 1] != " ")]
                steps = "0;" + ";".join(f"{k * ch:.1f}" for k in ends) + f";{(len(full) + 1) * ch:.1f}"
                dur = 0.07 * (len(ends) + 1)
                defs.append(
                    f'<clipPath id="c{i}"><rect x="{x0 + indent:.1f}" y="{y - 18}" width="0" height="{lh}">'
                    f'<animate attributeName="width" values="{steps}" calcMode="discrete" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"/>'
                    f"</rect></clipPath>"
                )
                parts.append(
                    f'<text x="{x0 + indent:.1f}" y="{y}" xml:space="preserve" clip-path="url(#c{i})">{spans}</text>'
                )
                t += dur + 0.1
            else:
                parts.append(
                    f'<text x="{x0 + indent:.1f}" y="{y}" opacity="0" xml:space="preserve">{spans}'
                    f'<set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/></text>'
                )
                t += 0.12
            if nxt == "cmd":
                t += 0.45
            line += 1
    y = y0 + line * lh
    parts.append(
        f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
        f'<text x="{x0}" y="{y}" fill="{GREEN}">$</text>'
        f'<rect x="{x0 + 2 * ch:.1f}" y="{y - 15}" width="9" height="19" fill="{FG}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" begin="{t:.2f}s" repeatCount="indefinite"/></rect></g>'
    )
    height = y + 32
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="{height}" viewBox="0 0 860 {height}" role="img" aria-label="{TERMINAL_ARIA}">
  <defs>{''.join(defs)}</defs>
  <rect x="0.5" y="0.5" width="859" height="{height - 1}" rx="12" fill="#161b22" stroke="#30363d"/>
  <path d="M0.5 40 V12.5 a12 12 0 0 1 12 -12 H847.5 a12 12 0 0 1 12 12 V40 Z" fill="#1f252d"/>
  <line x1="0.5" y1="40" x2="859.5" y2="40" stroke="#30363d"/>
  <circle cx="24" cy="20" r="6.5" fill="#ff5f57"/><circle cx="46" cy="20" r="6.5" fill="#febc2e"/><circle cx="68" cy="20" r="6.5" fill="#28c840"/>
  <text x="430" y="25" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{DIM}">{escape(title)}</text>
  <g font-family="{MONO}" font-size="15.5">
    {chr(10).join('    ' + p for p in parts).strip()}
  </g>
</svg>
"""


# ---------------------------------------------------------------- metro

def metro_svg(dark):
    p = dict(
        bg="#161b22" if dark else "#fbfaf6",
        border="#30363d" if dark else "#e4dfd3",
        ink="#e6edf3" if dark else "#1f2328",
        muted="#9198a1" if dark else "#6e7781",
        station="#0d1117" if dark else "#ffffff",
        zone="#ffffff08" if dark else "#00000005",
        zline="#3d444d" if dark else "#c9c3b4",
    )
    ship, req, asy = "#fc6d26", "#cc342d", "#8250df"
    ship_d = "M110 120 H430 V250"
    req_d = "M110 250 H750"
    asy_d = "M430 250 L510 330 H670 L750 250"

    def stop(x, y, color, name, dx=0, dy=-20, anchor="middle"):
        return (f'<circle cx="{x}" cy="{y}" r="8" fill="{p["station"]}" stroke="{color}" stroke-width="4"/>'
                f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" class="st">{name}</text>')

    def hub(x, y, name, dx=0, dy=-24, anchor="middle", sub=None):
        s = (f'<rect x="{x - 15}" y="{y - 15}" width="30" height="30" rx="15" fill="{p["station"]}" stroke="{p["ink"]}" stroke-width="4"/>'
             f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" class="st hub">{name}</text>')
        if sub:
            s += f'<text x="{x + dx}" y="{y + dy + 17}" text-anchor="{anchor}" class="sub">{sub}</text>'
        return s

    def train(path, color, dur, begin):
        return (f'<circle r="5" fill="{color}" stroke="{p["station"]}" stroke-width="2">'
                f'<animateMotion path="{path}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite" rotate="auto"/></circle>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="460" viewBox="0 0 860 460" role="img" aria-label="Metro map of Akhileshwar Reddy's stack: a ship line from Claude Code through GitLab CI/CD and Docker, a request line from client through Rails and Node.js to PostgreSQL, and an async line through Redis and Sidekiq, all running in a GCP / AWS zone.">
  <style>
    text {{ font-family: {SANS}; fill: {p["ink"]}; }}
    .st {{ font-size: 14px; font-weight: 600; }}
    .hub {{ font-size: 15px; font-weight: 800; }}
    .sub {{ font-size: 12px; fill: {p["muted"]}; }}
    .cap {{ font-size: 11px; font-weight: 700; letter-spacing: 2px; fill: {p["muted"]}; }}
  </style>
  <rect x="1" y="1" width="858" height="458" rx="16" fill="{p["bg"]}" stroke="{p["border"]}" stroke-width="2"/>

  <text x="32" y="48" font-size="22" font-weight="800" letter-spacing="1">AKHILESHWAR REDDY</text>
  <text x="32" y="70" class="cap">SYSTEM MAP · BACKEND ENGINEER · BANGALORE, INDIA</text>

  <rect x="280" y="196" width="538" height="176" rx="18" fill="{p["zone"]}" stroke="{p["zline"]}" stroke-width="1.5" stroke-dasharray="6 6"/>
  <text x="590" y="222" text-anchor="middle" class="cap">ZONE · GCP / AWS</text>

  <g fill="none" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">
    <path d="{ship_d}" stroke="{ship}"/>
    <path d="{req_d}" stroke="{req}"/>
    <path d="{asy_d}" stroke="{asy}"/>
  </g>
  <text x="200" y="241" text-anchor="middle" class="sub">HTTP</text>

  {train(ship_d, p["ink"], 7, 0)}
  {train(req_d, p["ink"], 6, 1.5)}
  {train(asy_d, p["ink"], 6.5, 3)}

  {stop(110, 120, ship, "Claude Code")}
  {stop(270, 120, ship, "GitLab CI/CD")}
  {stop(430, 120, ship, "Docker", dx=18, dy=5, anchor="start")}
  {stop(110, 250, req, "Client", dy=32)}
  {stop(510, 330, asy, "Redis", dy=32)}
  {stop(670, 330, asy, "Sidekiq", dy=32)}
  {hub(430, 250, "Rails", dx=-24, dy=40, anchor="end", sub="+ Node.js services")}
  {hub(750, 250, "PostgreSQL", dy=-28)}

  <g transform="translate(32 414)">
    <line x1="0" y1="0" x2="28" y2="0" stroke="{ship}" stroke-width="8" stroke-linecap="round"/>
    <text x="38" y="5" class="sub">Ship line</text>
    <line x1="120" y1="0" x2="148" y2="0" stroke="{req}" stroke-width="8" stroke-linecap="round"/>
    <text x="158" y="5" class="sub">Request line</text>
    <line x1="258" y1="0" x2="286" y2="0" stroke="{asy}" stroke-width="8" stroke-linecap="round"/>
    <text x="296" y="5" class="sub">Async line</text>
  </g>
  <text x="828" y="419" text-anchor="end" class="sub">6+ years · Ruby on Rails for logistics and HR/benefits SaaS</text>
</svg>
"""


write("label", "label.svg", label_svg())
write("terminal", "terminal.svg", terminal_svg())
write("metro", "metro-light.svg", metro_svg(dark=False))
write("metro", "metro-dark.svg", metro_svg(dark=True))
write("label-ai", "label-ai.svg", label_ai_svg())
write("terminal-ai", "terminal-ai.svg", terminal_svg(TERMINAL_AI_SCRIPT, "akhileshwar@bangalore: ~ — claude"))
# the live design, used by the profile README
write("..", "label.svg", label_combo_svg())
print("ok")
