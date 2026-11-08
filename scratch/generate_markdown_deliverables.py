# -*- coding: utf-8 -*-
"""
Generates the comprehensive Markdown Deliverables document
covering Deliverable A, B, C, D, and E.
"""

import json

with open('/home/tejas/ipl/ipl_iconic_moments_2008_2026.json', 'r', encoding='utf-8') as f:
    moments = json.load(f)

# Sort moments
moments.sort(key=lambda x: (x['season'], x['id']))

# Compile Top 50 Moments based on historical weight
# Ranking criteria: Historical impact (30%), Uniqueness (25%), Importance to IPL history (20%), Emotional significance (15%), Fan recognition (10%)
essential_ids_priority = [
    # Tier 1 - Top 10 immortal foundational moments
    "IPL-2008-001", # McCullum 158*
    "IPL-2013-001", # Gayle 175*
    "IPL-2023-001", # Rinku Singh 5 sixes
    "IPL-2019-001", # Malinga last-ball slower yorker 2019 final
    "IPL-2023-002", # Jadeja 6 & 4 at 1:35 AM 2023 final
    "IPL-2016-001", # Kohli 973 runs & 4 tons with stitches
    "IPL-2008-004", # Warne & RR inaugural championship
    "IPL-2014-001", # Corey Anderson 95* & Tare 6 (190 in 14.3 ov)
    "IPL-2020-001", # Tewatia 5 sixes in Sharjah chase
    "IPL-2026-001", # RCB maiden IPL title 2026

    # Tier 2 - Ranks 11-25
    "IPL-2018-002", # Watson 117* bleeding knee final
    "IPL-2020-002", # Double Super Over MI vs KXIP
    "IPL-2024-002", # PBKS 262 chase vs KKR world record
    "IPL-2024-001", # SRH 287/3 all-time record
    "IPL-2012-002", # Bisla 89 & KKR maiden title
    "IPL-2013-003", # MI maiden title 2013 under Rohit
    "IPL-2017-002", # Johnson defends 11 (MI win by 1 run vs RPS)
    "IPL-2010-003", # Dhoni mid-off trap for Pollard, CSK maiden title
    "IPL-2010-002", # Dhoni helmet punch in Dharamsala
    "IPL-2014-002", # Suresh Raina 87 off 25 balls
    "IPL-2014-003", # Manish Pandey 94 & KKR 200 chase final
    "IPL-2018-001", # Bravo 68 & Jadhav one-legged six vs MI
    "IPL-2012-001", # Albie Morkel 28-run over vs Kohli
    "IPL-2015-001", # AB 133* & Kohli 82* 215 partnership
    "IPL-2017-001", # RCB 49 all out at Eden Gardens

    # Tier 3 - Ranks 26-40
    "IPL-2009-005", # Deccan Chargers fairytale worst-to-first title
    "IPL-2016-004", # Ben Cutting & SRH maiden title vs RCB
    "IPL-2024-003", # Yash Dayal defends 17 vs Dhoni to send RCB to playoffs
    "IPL-2021-001", # Jadeja 37-run over off Harshal Patel
    "IPL-2022-001", # Hardik Pandya leads GT to debut title
    "IPL-2010-001", # Yusuf Pathan 37-ball 100 vs MI
    "IPL-2019-005", # Andre Russell 2019 rampage (48* off 13)
    "IPL-2009-003", # Manish Pandey first Indian century
    "IPL-2011-001", # Chris Gayle RCB debut 102*
    "IPL-2019-002", # Ashwin Mankad of Buttler
    "IPL-2013-002", # David Miller 101*(38) chase for KXIP
    "IPL-2018-003", # Rashid Khan Q2 all-round masterclass
    "IPL-2023-003", # Shubman Gill 890 runs & 129 in Q2
    "IPL-2025-002", # Delhi Capitals maiden title
    "IPL-2026-002", # Kohli 82* in 2026 Final

    # Tier 4 - Ranks 41-50
    "IPL-2011-003", # CSK defend title back-to-back
    "IPL-2009-001", # Kumble 5/5 in Cape Town
    "IPL-2019-003", # Alzarri Joseph 6/12 on debut
    "IPL-2008-002", # Sohail Tanvir 6/14
    "IPL-2024-004", # Starc spell & KKR 3rd title
    "IPL-2021-002", # Faf 86 & CSK 4th title
    "IPL-2022-002", # Tewatia 2 sixes off final 2 balls vs PBKS
    "IPL-2026-003", # Rohit & Dhoni grand farewell tributes
    "IPL-2013-004", # Rohit Sharma appointed MI captain
    "IPL-2012-004"  # Sunil Narine 24 wickets MVP debut
]

moments_dict = {m['id']: m for m in moments}

top50_moments = []
for idx, mid in enumerate(essential_ids_priority[:50], 1):
    if mid in moments_dict:
        top50_moments.append((idx, moments_dict[mid]))

print(f"Top 50 compiled: {len(top50_moments)} moments.")
