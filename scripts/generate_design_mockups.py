#!/usr/bin/env python3
from pathlib import Path

OUT = Path('assets/design_mockups')
OUT.mkdir(parents=True, exist_ok=True)


def write_svg(path: Path, content: str) -> None:
    path.write_text(content)


def style_a() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
<rect width="1600" height="900" fill="#0F1115"/>
<rect x="20" y="20" width="1560" height="70" rx="12" fill="#171A21"/>
<text x="40" y="64" fill="#E8ECF3" font-size="28" font-family="Arial" font-weight="700">ROOKIE QUEST: RINGMASTER — WEEKLY COMMAND CENTER</text>
<rect x="20" y="110" width="410" height="770" rx="14" fill="#171A21"/>
<rect x="450" y="110" width="610" height="770" rx="14" fill="#171A21"/>
<rect x="1080" y="110" width="500" height="770" rx="14" fill="#171A21"/>
<text x="40" y="150" fill="#4DA3FF" font-size="26" font-family="Arial" font-weight="700">Inbox / Alerts</text>
<text x="470" y="150" fill="#4DA3FF" font-size="26" font-family="Arial" font-weight="700">Show Booking Board</text>
<text x="1100" y="150" fill="#4DA3FF" font-size="26" font-family="Arial" font-weight="700">Finance + World Rank</text>
<rect x="35" y="180" width="380" height="52" rx="10" fill="#232734"/><text x="50" y="212" fill="#FFB020" font-size="18" font-family="Arial">Contract expiring: Jax Storm (14d)</text>
<rect x="35" y="245" width="380" height="52" rx="10" fill="#232734"/><text x="50" y="277" fill="#FF5C5C" font-size="18" font-family="Arial">Morale dip: Rhea Vale</text>
<rect x="35" y="310" width="380" height="52" rx="10" fill="#232734"/><text x="50" y="342" fill="#37D67A" font-size="18" font-family="Arial">Sponsorship offer received</text>
<rect x="470" y="185" width="570" height="70" rx="10" fill="#232734"/><text x="490" y="228" fill="#E8ECF3" font-size="24" font-family="Arial">1. Opening Promo</text>
<rect x="470" y="269" width="570" height="70" rx="10" fill="#232734"/><text x="490" y="312" fill="#E8ECF3" font-size="24" font-family="Arial">2. Tag Match</text>
<rect x="470" y="353" width="570" height="70" rx="10" fill="#232734"/><text x="490" y="396" fill="#E8ECF3" font-size="24" font-family="Arial">3. Main Event</text>
<rect x="1100" y="180" width="460" height="86" rx="10" fill="#232734"/><text x="1120" y="214" fill="#A7B0C0" font-size="18" font-family="Arial">Cash</text><text x="1120" y="248" fill="#E8ECF3" font-size="28" font-family="Arial">$1,240,000</text>
<rect x="1100" y="282" width="460" height="86" rx="10" fill="#232734"/><text x="1120" y="316" fill="#A7B0C0" font-size="18" font-family="Arial">World Rank</text><text x="1120" y="350" fill="#E8ECF3" font-size="28" font-family="Arial">#7</text>
<text x="40" y="850" fill="#A7B0C0" font-size="18" font-family="Arial">Style A: Broadcast Executive (Recommended)</text>
</svg>'''


def style_b() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
<rect width="1600" height="900" fill="#140D0D"/>
<rect x="40" y="40" width="1520" height="820" rx="24" fill="#1E1212" stroke="#5E2B2B"/>
<text x="80" y="105" fill="#F5D7A1" font-size="52" font-family="Arial" font-weight="700">RINGMASTER // FIGHT POSTER NOIR</text>
<text x="80" y="160" fill="#D9C3A0" font-size="30" font-family="Arial">Dramatic, gritty, premium PPV tone</text>
<rect x="80" y="230" width="680" height="590" rx="16" fill="#2A1616" stroke="#7A3B3B"/>
<rect x="840" y="230" width="680" height="590" rx="16" fill="#2A1616" stroke="#7A3B3B"/>
<text x="110" y="275" fill="#F1B96E" font-size="30" font-family="Arial" font-weight="700">FEUD TIMELINE</text>
<text x="870" y="275" fill="#F1B96E" font-size="30" font-family="Arial" font-weight="700">MAIN CARD</text>
<text x="110" y="845" fill="#D9C3A0" font-size="20" font-family="Arial">Style B: Fight Poster Noir</text>
</svg>'''


def style_c() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
<rect width="1600" height="900" fill="#EDF1F7"/>
<rect x="20" y="20" width="1560" height="70" rx="12" fill="#FFFFFF" stroke="#D4DCE8"/>
<text x="40" y="64" fill="#1D2A3A" font-size="28" font-family="Arial" font-weight="700">RINGMASTER — MODERN SPORTS APP</text>
<rect x="20" y="110" width="500" height="210" rx="12" fill="#FFFFFF" stroke="#D4DCE8"/>
<rect x="540" y="110" width="500" height="210" rx="12" fill="#FFFFFF" stroke="#D4DCE8"/>
<rect x="1060" y="110" width="520" height="210" rx="12" fill="#FFFFFF" stroke="#D4DCE8"/>
<text x="40" y="150" fill="#6B7A90" font-size="20" font-family="Arial">Audience</text><text x="40" y="225" fill="#1D2A3A" font-size="54" font-family="Arial">1.24M</text>
<text x="560" y="150" fill="#6B7A90" font-size="20" font-family="Arial">Revenue</text><text x="560" y="225" fill="#1D2A3A" font-size="54" font-family="Arial">$422k</text>
<text x="1080" y="150" fill="#6B7A90" font-size="20" font-family="Arial">Rank</text><text x="1080" y="225" fill="#1D2A3A" font-size="54" font-family="Arial">#11</text>
<rect x="20" y="350" width="1560" height="530" rx="12" fill="#FFFFFF" stroke="#D4DCE8"/>
<text x="40" y="395" fill="#1D2A3A" font-size="30" font-family="Arial" font-weight="700">Roster Intelligence</text>
<text x="40" y="850" fill="#6B7A90" font-size="20" font-family="Arial">Style C: Modern Sports App (high readability / console-safe)</text>
</svg>'''


def main() -> None:
    write_svg(OUT / 'style_a_broadcast_executive.svg', style_a())
    write_svg(OUT / 'style_b_fight_poster_noir.svg', style_b())
    write_svg(OUT / 'style_c_modern_sports_app.svg', style_c())
    print('Generated SVG mockups in assets/design_mockups/')


if __name__ == '__main__':
    main()
