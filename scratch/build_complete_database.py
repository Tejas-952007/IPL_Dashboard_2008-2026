# -*- coding: utf-8 -*-
import json
import os

all_moments = []

def add_m(m):
    all_moments.append(m)

# 2008
add_m({
    "id": "IPL-2008-001", "season": 2008, "title": "Brendon McCullum's 158* Ignites the IPL Era",
    "date": "2008-04-18", "match_stage": "League (Match 1)", "teams": ["Kolkata Knight Riders", "Royal Challengers Bangalore"],
    "venue": "M Chinnaswamy Stadium, Bengaluru", "players": ["Brendon McCullum", "Sourav Ganguly", "Zaheer Khan", "Praveen Kumar"],
    "match_score": "KKR 222/3 (20.0) beat RCB 82 (15.1) by 140 runs",
    "description": "On the opening night of the Indian Premier League, New Zealand batter Brendon McCullum transformed T20 cricket into an overnight global spectacle. Wearing gold and black armor for Kolkata Knight Riders, McCullum launched an unsparing assault against RCB's bowling attack, smoking 10 boundaries and 13 colossal sixes to finish 158 not out off just 73 balls. He reached his hundred in 53 balls, sending shockwaves through the sporting universe and establishing the IPL as the most exhilarating tournament on earth.",
    "why_iconic": "It was the explosive catalyst that permanently validated the IPL business model and athletic promise on day one, erasing any lingering skepticism about franchise cricket.",
    "historical_significance": "Single-handedly ignited the global franchise T20 revolution; remains the benchmark opening match performance in world cricket history.",
    "franchise": "Kolkata Knight Riders", "related_players": ["Brendon McCullum", "Sourav Ganguly", "Rahul Dravid", "Ricky Ponting"],
    "category": ["FIRSTS & MILESTONES", "UNBELIEVABLE BATTING", "IPL RECORD-BREAKING MOMENTS"],
    "importance": "Essential",
    "video_url": "https://www.iplt20.com/video/14986/ipl-2008-match-1-rcb-vs-kkr-brendon-mccullum-158",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/royal-challengers-bangalore-vs-kolkata-knight-riders-1st-match-335982/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/mccullums-158-the-night-the-ipl-was-born-559132",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["iplt20.com", "ESPNcricinfo", "BCCI"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2008-002", "season": 2008, "title": "Sohail Tanvir's Unorthodox 6/14 Record Spell",
    "date": "2008-05-04", "match_stage": "League (Match 24)", "teams": ["Rajasthan Royals", "Chennai Super Kings"],
    "venue": "Sawai Mansingh Stadium, Jaipur", "players": ["Sohail Tanvir", "Parthiv Patel", "Stephen Fleming", "Albie Morkel"],
    "match_score": "CSK 109 (19.0) lost to RR 110/2 (14.2) by 8 wickets",
    "description": "Pakistani left-arm pacer Sohail Tanvir unveiled his wrong-footed delivery stride to rip through Chennai Super Kings. Grabbing 6 wickets for just 14 runs in 4 overs of swing bowling, Tanvir dismissed Parthiv Patel and Stephen Fleming on consecutive deliveries in the first over before finishing off the tail. The spell stood unbroken as the all-time best bowling figures in IPL history for over 11 years.",
    "why_iconic": "Set an unbelievable individual bowling standard in a tournament perceived to be purely a batter's playground.",
    "historical_significance": "Sealed Tanvir's Purple Cap campaign (22 wickets) and powered Shane Warne's Rajasthan Royals toward their inaugural championship.",
    "franchise": "Rajasthan Royals", "related_players": ["Sohail Tanvir", "Shane Warne", "MS Dhoni"],
    "category": ["LEGENDARY BOWLING", "IPL RECORD-BREAKING MOMENTS", "FIRSTS & MILESTONES"],
    "importance": "Major",
    "video_url": "https://www.iplt20.com/video/28532/ipl-2008-match-24-rr-vs-csk-sohail-tanvir-6-14",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/rajasthan-royals-vs-chennai-super-kings-24th-match-336005/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/tanvir-s-six-shoots-down-chennai-348633",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["ESPNcricinfo", "iplt20.com"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2008-003", "season": 2008, "title": "The Sreesanth & Harbhajan Slapgate Flashpoint",
    "date": "2008-04-25", "match_stage": "League (Match 10)", "teams": ["Kings XI Punjab", "Mumbai Indians"],
    "venue": "PCA Stadium, Mohali", "players": ["Harbhajan Singh", "S Sreesanth", "Shaun Pollock", "Yuvraj Singh"],
    "match_score": "KXIP 182/6 (20.0) beat MI 116/9 (20.0) by 66 runs",
    "description": "In one of the most controversial incidents in Indian cricket history, Mumbai Indians stand-in skipper Harbhajan Singh slapped Kings XI Punjab pacer Sreesanth during post-match handshakes. Live broadcast cameras captured Sreesanth in tears on the pitch while comforted by Punjab captain Yuvraj Singh, igniting a national media storm, a high-level BCCI inquiry, and an 11-match tournament ban for Harbhajan.",
    "why_iconic": "First major off-field crisis in the newly formed IPL, exposing the raw emotional stakes and tribal intensity between international teammates.",
    "historical_significance": "Triggered stringent BCCI and IPL player conduct regulations and code-of-conduct enforcement across all franchises.",
    "franchise": "Mumbai Indians", "related_players": ["Harbhajan Singh", "S Sreesanth", "Yuvraj Singh"],
    "category": ["CONTROVERSIES", "EMOTIONAL MOMENTS"],
    "importance": "Major",
    "video_url": "Direct video not found (Broadcast disciplinary hearing and footage archived by BCCI)",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/kings-xi-punjab-vs-mumbai-indians-10th-match-335991/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/harbhajan-banned-for-rest-of-ipl-347895",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["BCCI Disciplinary Committee", "ESPNcricinfo"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2008-004", "season": 2008, "title": "Shane Warne's Underdog Rajasthan Royals Win Inaugural Title",
    "date": "2008-06-01", "match_stage": "Final", "teams": ["Rajasthan Royals", "Chennai Super Kings"],
    "venue": "DY Patil Stadium, Navi Mumbai", "players": ["Shane Warne", "Yusuf Pathan", "Sohail Tanvir", "MS Dhoni", "Albie Morkel"],
    "match_score": "CSK 163/5 (20.0) lost to RR 164/7 (20.0) by 3 wickets (last-ball thriller)",
    "description": "Shane Warne captain-coached the lowest-budget, least-fancied Rajasthan Royals to the inaugural IPL championship in a nerve-shredding last-ball finish. After Yusuf Pathan produced an all-round masterclass (3/22 with ball, 56 off 39 with bat), Royals needed 1 run off the final delivery. Sohail Tanvir clipped Lakshmipathy Balaji through midwicket to scamper the championship run, triggering wild ecstasy as Warne and his band of young domestic heroes lifted the trophy.",
    "why_iconic": "Proved that tactical brilliance, underdog camaraderie, and uncapped talent could triumph over big-money galacticos.",
    "historical_significance": "Shane Warne cemented his legacy as one of the greatest cricket captains in history; established the IPL's foundational meritocratic ethos.",
    "franchise": "Rajasthan Royals", "related_players": ["Shane Warne", "Yusuf Pathan", "Sohail Tanvir", "Swapnil Asnodkar", "MS Dhoni"],
    "category": ["PLAYOFF & FINAL DRAMA", "FRANCHISE LEGACY", "LAST-BALL THRILLERS"],
    "importance": "Essential",
    "video_url": "https://www.iplt20.com/video/14995/ipl-2008-final-rr-vs-csk-match-highlights",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/chennai-super-kings-vs-rajasthan-royals-final-336040/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/warne-leads-rajasthan-to-glory-353683",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["iplt20.com", "ESPNcricinfo"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2008-005", "season": 2008, "title": "Lakshmipathy Balaji Bowls First Hat-Trick in IPL History",
    "date": "2008-05-10", "match_stage": "League (Match 31)", "teams": ["Chennai Super Kings", "Kings XI Punjab"],
    "venue": "MA Chidambaram Stadium, Chepauk, Chennai", "players": ["Lakshmipathy Balaji", "Irfan Pathan", "Piyush Chawla", "VRV Singh"],
    "match_score": "CSK 181/4 (20.0) beat KXIP 163/9 (20.0) by 18 runs",
    "description": "CSK seamer Lakshmipathy Balaji carved his name into tournament folklore by registering the first-ever hat-trick in IPL history. Defending 27 runs in the final over, Balaji removed Irfan Pathan (caught by Graeme Smith), Piyush Chawla (caught at long-off), and VRV Singh (caught behind) across three consecutive deliveries, finishing with 5 for 24 amid thunderous applause from the Chepauk faithful.",
    "why_iconic": "First official hat-trick etched in IPL record books, sparking an enduring Chepauk love affair with local heroes.",
    "historical_significance": "Broke psychological ground for Indian domestic pacers in high-pressure death overs.",
    "franchise": "Chennai Super Kings", "related_players": ["Lakshmipathy Balaji", "MS Dhoni", "Irfan Pathan"],
    "category": ["FIRSTS & MILESTONES", "LEGENDARY BOWLING"],
    "importance": "Major",
    "video_url": "https://www.iplt20.com/video/28550/ipl-2008-balaji-first-ipl-hat-trick",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/chennai-super-kings-vs-kings-xi-punjab-31st-match-336012/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/balaji-hat-trick-sinks-punjab-350352",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["ESPNcricinfo", "iplt20.com"], "verification_status": "Verified"
})

# 2009
add_m({
    "id": "IPL-2009-001", "season": 2009, "title": "Anil Kumble's Mesmerizing 5 for 5 in Cape Town",
    "date": "2009-04-18", "match_stage": "League (Match 2)", "teams": ["Royal Challengers Bangalore", "Rajasthan Royals"],
    "venue": "Newlands, Cape Town, South Africa", "players": ["Anil Kumble", "Ravindra Jadeja", "Yusuf Pathan", "Shane Warne"],
    "match_score": "RCB 133/8 (20.0) beat RR 58 (15.1) by 75 runs",
    "description": "On the opening weekend of IPL 2009 in South Africa, 38-year-old Indian leg-spin icon Anil Kumble produced one of the most economical and destructive spells in world T20 history. Defending a modest 133, Kumble bowled 3.1 overs, conceded just 5 runs, and captured 5 wickets, dismantling defending champions Rajasthan Royals for a humiliating 58.",
    "why_iconic": "A masterclass in classical leg-spin on foreign bouncy turf, proving experience and precision conquer raw hitting.",
    "historical_significance": "Remains one of the most economical 5-wicket hauls in professional T20 cricket history; sparked Kumble's appointment as RCB captain.",
    "franchise": "Royal Challengers Bangalore", "related_players": ["Anil Kumble", "Kevin Pietersen", "Shane Warne"],
    "category": ["LEGENDARY BOWLING", "IPL RECORD-BREAKING MOMENTS"],
    "importance": "Essential",
    "video_url": "https://www.iplt20.com/video/28555/ipl-2009-kumble-5-for-5-vs-rr",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2009-374163/rajasthan-royals-vs-royal-challengers-bangalore-2nd-match-392182/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/kumble-five-shreds-rajasthan-399342",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["ESPNcricinfo", "iplt20.com"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2009-002", "season": 2009, "title": "Rohit Sharma's Match-Winning Hat-Trick Against Mumbai Indians",
    "date": "2009-05-06", "match_stage": "League (Match 32)", "teams": ["Deccan Chargers", "Mumbai Indians"],
    "venue": "SuperSport Park, Centurion, South Africa", "players": ["Rohit Sharma", "Abhishek Nayar", "Harbhajan Singh", "JP Duminy"],
    "match_score": "DC 145/6 (20.0) beat MI 126/8 (20.0) by 19 runs",
    "description": "Before Rohit Sharma became Mumbai Indians' legendary trophy-winning skipper, he destroyed them with the ball in Centurion. Bowling off-breaks for Deccan Chargers, Rohit dismissed Abhishek Nayar and Harbhajan Singh on the final two balls of the 16th over, and then had set batter JP Duminy caught behind on the first ball of the 18th over to complete a sensational hat-trick (4/6 in 2 overs).",
    "why_iconic": "One of the most astonishing twists in IPL folklore - a future batting immortal securing a hat-trick against his future empire.",
    "historical_significance": "Revitalized Deccan Chargers' campaign on their road to the 2009 championship.",
    "franchise": "Deccan Chargers", "related_players": ["Rohit Sharma", "Adam Gilchrist", "Sachin Tendulkar"],
    "category": ["LEGENDARY BOWLING", "UNEXPECTED COMEBACKS", "FIRSTS & MILESTONES"],
    "importance": "Major",
    "video_url": "https://www.iplt20.com/video/28565/ipl-2009-rohit-sharma-hat-trick-vs-mi",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2009-374163/deccan-chargers-vs-mumbai-indians-32nd-match-392213/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/rohit-hat-trick-seals-chargers-win-400898",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["ESPNcricinfo", "iplt20.com"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2009-003", "season": 2009, "title": "Manish Pandey Becomes First Indian Centurion in IPL History",
    "date": "2009-05-21", "match_stage": "League (Match 56)", "teams": ["Royal Challengers Bangalore", "Deccan Chargers"],
    "venue": "SuperSport Park, Centurion, South Africa", "players": ["Manish Pandey", "Jacques Kallis", "RP Singh", "Adam Gilchrist"],
    "match_score": "RCB 170/4 (20.0) beat DC 158/6 (20.0) by 12 runs",
    "description": "Nineteen-year-old Nainital-born prodigy Manish Pandey scripted history at Centurion by becoming the first Indian batter to score an IPL century. Opening the innings alongside Jacques Kallis for RCB in a virtual knockout clash, Pandey struck 10 fours and 4 sixes in an imperious 114 not out off 73 balls, booking Bangalore's playoff ticket.",
    "why_iconic": "Broke the barrier where only overseas megastars had registered hundreds, proving Indian domestic youth could dominate on foreign soil.",
    "historical_significance": "A watershed milestone that accelerated the emergence of uncapped Indian talent onto the global stage.",
    "franchise": "Royal Challengers Bangalore", "related_players": ["Manish Pandey", "Anil Kumble", "Rahul Dravid"],
    "category": ["FIRSTS & MILESTONES", "UNBELIEVABLE BATTING", "PLAYER LEGACY"],
    "importance": "Essential",
    "video_url": "https://www.iplt20.com/video/28570/ipl-2009-manish-pandey-first-indian-ipl-century",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2009-374163/deccan-chargers-vs-royal-challengers-bangalore-56th-match-392237/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/pandey-dazzles-with-first-indian-century-405494",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["iplt20.com", "ESPNcricinfo"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2009-004", "season": 2009, "title": "Adam Gilchrist's 85 off 35 Semi-Final Blitzkrieg",
    "date": "2009-05-22", "match_stage": "Semi-Final 1", "teams": ["Deccan Chargers", "Delhi Daredevils"],
    "venue": "SuperSport Park, Centurion, South Africa", "players": ["Adam Gilchrist", "Dirk Nannes", "Gautam Gambhir", "Virender Sehwag"],
    "match_score": "DD 153/8 (20.0) lost to DC 154/4 (17.4) by 6 wickets",
    "description": "Facing table-toppers Delhi Daredevils in the semi-final, Deccan Chargers captain Adam Gilchrist launched one of the most ferocious counter-attacking blitzes in playoff history. Chasing 154, Gilchrist battered Dirk Nannes and Ashish Nehra, racing to a 17-ball half-century and finishing with 85 off 35 balls (10 fours, 5 sixes) to blow Delhi out of the competition inside the powerplay.",
    "why_iconic": "The ultimate exhibition of fearless captaincy and intimidating strokeplay on a big knockout stage.",
    "historical_significance": "Propelled Deccan Chargers into the final after finishing bottom of the table in 2008.",
    "franchise": "Deccan Chargers", "related_players": ["Adam Gilchrist", "Dirk Nannes", "Virender Sehwag"],
    "category": ["PLAYOFF & FINAL DRAMA", "UNBELIEVABLE BATTING"],
    "importance": "Major",
    "video_url": "https://www.iplt20.com/video/28575/ipl-2009-gilchrist-85-vs-delhi-semifinal",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2009-374163/delhi-daredevils-vs-deccan-chargers-1st-semi-final-392238/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/gilchrist-blitz-takes-deccan-to-final-405625",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["ESPNcricinfo", "iplt20.com"], "verification_status": "Verified"
})
add_m({
    "id": "IPL-2009-005", "season": 2009, "title": "Deccan Chargers Crown Fairytale Worst-to-First Title",
    "date": "2009-05-24", "match_stage": "Final", "teams": ["Deccan Chargers", "Royal Challengers Bangalore"],
    "venue": "Wanderers Stadium, Johannesburg, South Africa", "players": ["Adam Gilchrist", "Anil Kumble", "Pragyan Ojha", "Herschelle Gibbs", "RP Singh"],
    "match_score": "DC 143/6 (20.0) beat RCB 137/9 (20.0) by 6 runs",
    "description": "In an exhilarating, low-scoring Johannesburg final, Adam Gilchrist's Deccan Chargers completed the ultimate redemption arc. After RCB captain Anil Kumble produced an inspired spell (4/16) to restrict Chargers to 143, Pragyan Ojha (3/28) and RP Singh snared crucial breakthroughs in the chase. Needing 15 off the final over, RP Singh kept his nerve to secure a 6-run victory, crowning Deccan Chargers champions just 12 months after finishing rock-bottom in 2008.",
    "why_iconic": "The definitive 'worst-to-first' fairytale in franchise cricket, showing resilience and tactical turnaround under pressure.",
    "historical_significance": "Cemented Adam Gilchrist's leadership stature and gave the Hyderabad franchise their first IPL crown.",
    "franchise": "Deccan Chargers", "related_players": ["Adam Gilchrist", "Anil Kumble", "Herschelle Gibbs", "RP Singh", "Pragyan Ojha"],
    "category": ["PLAYOFF & FINAL DRAMA", "FRANCHISE LEGACY", "UNEXPECTED COMEBACKS"],
    "importance": "Essential",
    "video_url": "https://www.iplt20.com/video/14998/ipl-2009-final-dc-vs-rcb-match-highlights",
    "scorecard_url": "https://www.espncricinfo.com/series/indian-premier-league-2009-374163/deccan-chargers-vs-royal-challengers-bangalore-final-392239/full-scorecard",
    "article_url": "https://www.espncricinfo.com/story/deccan-chargers-crowned-ipl-champions-405822",
    "image_url": "https://www.iplt20.com/assets/images/ipl-logo-new-old.png",
    "sources": ["iplt20.com", "ESPNcricinfo"], "verification_status": "Verified"
})

print(f"Moments generated so far: {len(all_moments)}")
