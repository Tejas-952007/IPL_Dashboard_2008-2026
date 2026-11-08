import sys

new_app_code = r'''import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import plotly.io as pio
import base64
import os
import wikipedia

# ==========================================
# 🎨 LUXURY IPL CHAMPIONSHIP DESIGN SYSTEM
# ==========================================
# Official Franchise Brand Colors
IPL_TEAM_COLORS = {
    'Mumbai Indians': '#004BA0',
    'Chennai Super Kings': '#F9CD05',
    'Kolkata Knight Riders': '#3A225D',
    'Royal Challengers Bengaluru': '#C8102E',
    'Royal Challengers Bangalore': '#C8102E',
    'Delhi Capitals': '#004C97',
    'Delhi Daredevils': '#004C97',
    'Rajasthan Royals': '#EA1A85',
    'Sunrisers Hyderabad': '#F26522',
    'Deccan Chargers': '#002B49',
    'Punjab Kings': '#DD1F2D',
    'Kings XI Punjab': '#DD1F2D',
    'Gujarat Titans': '#1B2133',
    'Lucknow Super Giants': '#00A3E0',
    'Rising Pune Supergiant': '#D11D4E',
    'Rising Pune Supergiants': '#D11D4E',
    'Gujarat Lions': '#E04F16',
    'Pune Warriors India': '#2F9BE3',
    'Kochi Tuskers Kerala': '#6C2D82',
}

# Global Plotly Theme - Athletic Stadium Night
custom_template = pio.templates["plotly_dark"]
custom_template.layout.paper_bgcolor = "rgba(0,0,0,0)"
custom_template.layout.plot_bgcolor = "rgba(0,0,0,0)"
custom_template.layout.font.family = "Plus Jakarta Sans, Outfit, sans-serif"
custom_template.layout.font.color = "#cbd5e1"
custom_template.layout.title.font.color = "#f8fafc"
custom_template.layout.title.font.size = 20
custom_template.layout.title.font.family = "Outfit, sans-serif"
custom_template.layout.colorway = ['#38bdf8', '#f59e0b', '#10b981', '#f472b6', '#818cf8', '#fbbf24', '#34d399']
custom_template.layout.xaxis.gridcolor = "rgba(255, 255, 255, 0.06)"
custom_template.layout.yaxis.gridcolor = "rgba(255, 255, 255, 0.06)"
custom_template.layout.hoverlabel.bgcolor = "#0f172a"
custom_template.layout.hoverlabel.font.color = "#ffffff"
custom_template.layout.hoverlabel.bordercolor = "#f59e0b"
pio.templates.default = custom_template

st.set_page_config(
    page_title="IPL Analytics 2008-2026 | Premier Cricket Intelligence",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-End Anti-Generic Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Teko:wght@500;600;700&display=swap');

/* Global Reset & Typography */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #e2e8f0;
}

/* Atmospheric Stadium Night Background */
.stApp {
    background: radial-gradient(ellipse 120% 80% at 50% -10%, #152238 0%, #070a12 85%);
    color: #f8fafc;
}

/* Headings with Athletic Typography */
h1, h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px !important;
    color: #f8fafc !important;
}

h1 {
    font-size: 2.2rem !important;
}

h2 {
    font-size: 1.6rem !important;
    margin-top: 1.5rem !important;
    border-left: 4px solid #f59e0b;
    padding-left: 12px;
}

h3 {
    font-size: 1.25rem !important;
    color: #e2e8f0 !important;
}

/* Custom Metric Cards */
[data-testid="stMetric"] {
    background: #0d1424 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 14px !important;
    padding: 16px 20px !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4) !important;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease !important;
    position: relative;
    overflow: hidden;
}

[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #f59e0b 0%, #38bdf8 100%);
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    border-color: rgba(245, 158, 11, 0.4) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6) !important;
}

[data-testid="stMetricLabel"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    color: #94a3b8 !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Outfit', sans-serif !important;
    font-size: 26px !important;
    font-weight: 800 !important;
    color: #f8fafc !important;
}

/* Sidebar Customization */
[data-testid="stSidebar"] {
    background: #090e18 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

[data-testid="stSidebar"] .stRadio > div {
    gap: 4px;
}

[data-testid="stSidebar"] .stRadio label {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    color: #94a3b8 !important;
    padding: 8px 12px;
    border-radius: 8px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255, 255, 255, 0.05);
    color: #f8fafc !important;
}

/* Styled Inputs, Selectboxes & Sliders */
div[data-baseweb="select"] > div {
    background: #0d1424 !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
    font-weight: 500;
}

div[data-baseweb="select"] > div:hover {
    border-color: #f59e0b !important;
}

/* Primary Action Buttons */
.stButton > button {
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
    color: #0b0f19 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    font-size: 14px !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3) !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(245, 158, 11, 0.5) !important;
    filter: brightness(1.08);
}

/* Custom Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: transparent;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 4px;
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #94a3b8 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 10px 20px !important;
    transition: all 0.2s ease !important;
}

.stTabs [aria-selected="true"] {
    color: #f59e0b !important;
    border-bottom: 2px solid #f59e0b !important;
    background: rgba(245, 158, 11, 0.08) !important;
}

/* Tables & Dataframes */
[data-testid="stTable"], [data-testid="stDataFrame"] {
    background: #0d1424 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    overflow: hidden;
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #f59e0b, #10b981) !important;
    border-radius: 10px;
}

/* Hero Header Banner */
.ipl-hero {
    position: relative;
    background: linear-gradient(135deg, #0e172a 0%, #172554 50%, #0e172a 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 35px 30px;
    margin-bottom: 30px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: space-between;
    align-items: center;
    overflow: hidden;
}

.ipl-hero::after {
    content: '';
    position: absolute;
    top: 0; right: 0; width: 40%; height: 100%;
    background: radial-gradient(circle at 80% 50%, rgba(245, 158, 11, 0.15), transparent 70%);
    pointer-events: none;
}

.ipl-hero-content {
    position: relative;
    z-index: 2;
    max-width: 650px;
}

.ipl-badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245, 158, 11, 0.15);
    border: 1px solid rgba(245, 158, 11, 0.4);
    color: #fbbf24;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
}

.ipl-hero h1 {
    font-size: 38px !important;
    font-weight: 900 !important;
    color: #ffffff !important;
    margin: 0 0 10px 0 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.ipl-hero p {
    font-size: 16px;
    color: #94a3b8;
    margin: 0;
    line-height: 1.6;
}

/* Championship Trophy Cards Grid */
.trophy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 16px;
    margin: 20px 0 30px 0;
}

.trophy-card {
    background: #0d1424;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 18px 16px;
    text-align: center;
    position: relative;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}

.trophy-card:hover {
    transform: translateY(-4px);
    border-color: rgba(245, 158, 11, 0.5);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
}

.trophy-count-pill {
    position: absolute;
    top: 12px;
    right: 12px;
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #000;
    font-weight: 800;
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(245, 158, 11, 0.4);
}

/* High-End FIFA / Ultimate Team Player Trading Card */
.fut-card-wrapper {
    perspective: 1000px;
    display: flex;
    justify-content: center;
    margin: 25px auto 35px auto;
}

.fut-card {
    position: relative;
    width: 330px;
    height: 520px;
    background: linear-gradient(165deg, #1e293b 0%, #0b0f19 55%, #080c14 100%);
    border-radius: 26px;
    padding: 20px;
    border: 2px solid #f59e0b;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 25px rgba(245, 158, 11, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    color: #ffffff;
    font-family: 'Outfit', sans-serif;
    text-align: center;
    transition: transform 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.35s ease;
    overflow: hidden;
}

.fut-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 50% 30%, rgba(245, 158, 11, 0.12), transparent 60%);
    pointer-events: none;
}

.fut-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 35px 80px rgba(0, 0, 0, 0.9), 0 0 35px rgba(245, 158, 11, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.4);
}

.fut-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    position: relative;
    z-index: 2;
}

.fut-ovr {
    font-family: 'Teko', sans-serif;
    font-size: 54px;
    font-weight: 700;
    line-height: 0.9;
    color: #fef08a;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
}

.fut-pos-badge {
    font-size: 12px;
    font-weight: 800;
    color: #cbd5e1;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.fut-league-badge {
    background: rgba(245, 158, 11, 0.2);
    border: 1px solid rgba(245, 158, 11, 0.5);
    color: #fbbf24;
    font-size: 13px;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 8px;
    letter-spacing: 1px;
}

.fut-avatar-ring {
    width: 175px;
    height: 175px;
    margin: 10px auto;
    border-radius: 50%;
    border: 3px solid #f59e0b;
    box-shadow: 0 0 25px rgba(245, 158, 11, 0.35), 0 10px 25px rgba(0, 0, 0, 0.7);
    overflow: hidden;
    background: #090e18;
    position: relative;
    z-index: 2;
}

.fut-avatar-ring img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
}

.fut-player-name {
    font-size: 24px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #ffffff;
    margin: 12px 0 4px 0;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
    position: relative;
    z-index: 2;
}

.fut-team-tag {
    font-size: 12px;
    font-weight: 600;
    color: #f59e0b;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
}

.fut-stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    background: rgba(13, 20, 36, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 10px 8px;
    position: relative;
    z-index: 2;
}

.fut-stat-box {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.fut-stat-val {
    font-family: 'Teko', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #f8fafc;
    line-height: 1;
}

.fut-stat-lbl {
    font-size: 10px;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 0.8px;
}

/* Versus Arena Match Banner */
.versus-arena-card {
    background: linear-gradient(135deg, #0d1424 0%, #152238 50%, #0d1424 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 25px 20px;
    margin: 25px 0 35px 0;
    display: flex;
    justify-content: space-around;
    align-items: center;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    position: relative;
}

.arena-team-box {
    text-align: center;
    width: 38%;
}

.arena-team-logo {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: contain;
    background: rgba(255, 255, 255, 0.04);
    padding: 10px;
    border: 2px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
    margin-bottom: 12px;
}

.arena-vs-divider {
    width: 15%;
    text-align: center;
}

.arena-vs-text {
    font-family: 'Teko', sans-serif;
    font-size: 44px;
    font-weight: 700;
    color: #f59e0b;
    letter-spacing: 2px;
}

/* Tactical Phase Blueprint Cards */
.tactical-blueprint {
    background: #0d1424;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 24px;
    margin-top: 25px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

/* Responsive Media Queries */
@media (max-width: 768px) {
    .ipl-hero {
        flex-direction: column;
        text-align: center;
        padding: 25px 20px;
    }
    .ipl-hero h1 {
        font-size: 28px !important;
    }
    .versus-arena-card {
        flex-direction: column;
        gap: 20px;
        padding: 25px 15px;
    }
    .arena-team-box, .arena-vs-divider {
        width: 100% !important;
    }
    .fut-card {
        width: 290px;
        height: 480px;
        transform: scale(0.95);
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# ⚡ CACHED DATA & ASSET UTILITIES
# ==========================================
@st.cache_data(ttl=86400)
def get_team_logo_base64(team_name):
    fallback = f"https://ui-avatars.com/api/?name={team_name.replace(' ', '+')}&background=0D1424&color=f59e0b&size=150&bold=true"
    try:
        search_query = f"{team_name} cricket"
        if team_name in ["Deccan Chargers", "Gujarat Lions", "Kochi Tuskers Kerala", "Pune Warriors India"]:
            search_query = team_name
            
        page = wikipedia.page(search_query, auto_suggest=True)
        logo_url = None
        for img in page.images:
            if "logo" in img.lower():
                logo_url = img
                break
        if not logo_url:
            for img in page.images:
                if img.lower().endswith((".png", ".svg")):
                    logo_url = img
                    break
        if logo_url:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            r = requests.get(logo_url, headers=headers, timeout=5)
            if r.status_code == 200:
                encoded = base64.b64encode(r.content).decode('utf-8')
                mime = "image/svg+xml" if logo_url.lower().endswith(".svg") else "image/png"
                if logo_url.lower().endswith((".jpg", ".jpeg")): mime = "image/jpeg"
                return f"data:{mime};base64,{encoded}"
    except Exception:
        pass
    return fallback

@st.cache_data(ttl=86400)
def fetch_wiki_data(query, is_player=False):
    try:
        headers = {'User-Agent': 'IPLAnalyticsDashboard/2.0 (tejas@example.com)'}
        clean_query = query
        if is_player:
            parts = query.split()
            if len(parts[0]) <= 2 and len(parts) > 1:
                clean_query = " ".join(parts[1:])
        search_term = clean_query + " cricketer" if is_player else clean_query
        
        search_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={search_term}&utf8=&format=json'
        r1 = requests.get(search_url, headers=headers, timeout=5).json()
        search_results = r1.get('query', {}).get('search', [])
        if not search_results:
            return '', ''
        title = search_results[0]['title']
        
        url = f'https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages|extracts&exintro=1&explaintext=1&pithumbsize=500&format=json'
        r2 = requests.get(url, headers=headers, timeout=5).json()
        pages = r2.get('query', {}).get('pages', {})
        for page_id, page in pages.items():
            if page_id != '-1':
                img_url = page.get('thumbnail', {}).get('source', '')
                ext = page.get('extract', '')
                img_base64 = ''
                if img_url:
                    r_img = requests.get(img_url, headers=headers, timeout=5)
                    if r_img.status_code == 200:
                        encoded = base64.b64encode(r_img.content).decode('utf-8')
                        mime = "image/jpeg"
                        if img_url.lower().endswith(".png"): mime = "image/png"
                        img_base64 = f"data:{mime};base64,{encoded}"
                return img_base64 if img_base64 else img_url, ext
    except Exception:
        pass
    return '', ''

def get_base64_image(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as img_file:
                ext = os.path.splitext(file_path)[1].lower()
                mime = "image/png" if ext == ".png" else "image/jpeg"
                return f"data:{mime};base64," + base64.b64encode(img_file.read()).decode()
    except Exception:
        pass
    return None

@st.cache_data
def load_data():
    try:
        matches = pd.read_csv('matches.csv')
        deliveries = pd.read_csv('deliveries.csv')
        
        # Normalize columns across different Kaggle/Cricsheet export versions
        if 'batter' in deliveries.columns:
            deliveries.rename(columns={'batter': 'batsman'}, inplace=True)
        if 'result_margin' in matches.columns and 'result' in matches.columns:
            matches['win_by_runs'] = matches.apply(lambda row: row['result_margin'] if row['result'] == 'runs' else 0, axis=1)
            matches['win_by_wickets'] = matches.apply(lambda row: row['result_margin'] if row['result'] == 'wickets' else 0, axis=1)
        if 'method' in matches.columns:
            matches['dl_applied'] = matches['method'].apply(lambda x: 1 if pd.notna(x) and x != 'NA' else 0)
            
        deliveries.replace('NA', np.nan, inplace=True)
        matches.replace('NA', np.nan, inplace=True)
        
        # Standardize Team Names
        team_mapping = {
            'Rising Pune Supergiant': 'Rising Pune Supergiants',
            'Pune Warriors': 'Pune Warriors India',
            'Delhi Daredevils': 'Delhi Capitals',
            'Deccan Chargers': 'Sunrisers Hyderabad',
            'Kings XI Punjab': 'Punjab Kings',
            'Royal Challengers Bangalore': 'Royal Challengers Bengaluru'
        }
        matches['team1'] = matches['team1'].replace(team_mapping)
        matches['team2'] = matches['team2'].replace(team_mapping)
        matches['winner'] = matches['winner'].replace(team_mapping)
        matches['toss_winner'] = matches['toss_winner'].replace(team_mapping)
        
        deliveries['batting_team'] = deliveries['batting_team'].replace(team_mapping)
        deliveries['bowling_team'] = deliveries['bowling_team'].replace(team_mapping)
        
        return matches, deliveries
    except FileNotFoundError:
        st.error("Data files (matches.csv or deliveries.csv) not found. Please run download_actual_data.py first.")
        return pd.DataFrame(), pd.DataFrame()

matches, deliveries = load_data()

if matches.empty or deliveries.empty:
    st.stop()

# Helper for Plotly Bar Charts with authentic team color mapping
def plot_plotly_bar(df, x, y, title, color_col=None, text_format=True):
    is_team_col = (color_col in ['team', 'Team', 'winner', 'Winner', 'batting_team']) or (x in ['team', 'Team', 'winner', 'Winner', 'batting_team'])
    color_map = IPL_TEAM_COLORS if is_team_col else None
    
    fig = px.bar(
        df, 
        x=x, 
        y=y, 
        title=title, 
        color=color_col if color_col else (x if is_team_col else None),
        color_discrete_map=color_map,
        color_discrete_sequence=['#f59e0b', '#38bdf8', '#10b981', '#f472b6'] if not is_team_col else None,
        text_auto=text_format
    )
    fig.update_layout(
        xaxis_title=x.replace('_', ' ').title(), 
        yaxis_title=y.replace('_', ' ').title(),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    fig.update_traces(textposition='outside')
    return fig


# ==========================================
# 🧭 SIDEBAR NAVIGATION
# ==========================================
st.sidebar.markdown(
    """
    <div style="text-align: center; padding: 10px 0 15px 0;">
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Indian_Premier_League_Official_Logo.svg/1200px-Indian_Premier_League_Official_Logo.svg.png" width="130" style="filter: drop-shadow(0 4px 12px rgba(245, 158, 11, 0.3));">
        <div style="font-family: 'Outfit'; font-weight: 800; font-size: 18px; color: #f8fafc; margin-top: 10px; letter-spacing: 0.5px;">IPL ANALYTICS</div>
        <div style="font-size: 11px; font-weight: 700; color: #f59e0b; letter-spacing: 1.5px; text-transform: uppercase;">2008 – 2026 Season Archives</div>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio("Navigation", [
    "Overview & Season Analysis", 
    "Team Analysis", 
    "Player Analysis", 
    "Player Profile (FIFA Card)",
    "Venue Analysis",
    "Toss Analysis",
    "Match & Head-to-Head Analysis",
    "Advanced Analytics",
    "AI Match Strategy Generator",
    "Season Records & Awards",
    "All-Time IPL Records",
    "Top 50 Greatest Players",
    "Greatest Team of All Time",
    "📸 Iconic IPL Moments"
])


# ==========================================
# 📊 PAGE 1: OVERVIEW & SEASON ANALYSIS
# ==========================================
if page == "Overview & Season Analysis":
    st.markdown(
        """
        <div class="ipl-hero">
            <div class="ipl-hero-content">
                <div class="ipl-badge-pill">🏆 Official League Intelligence</div>
                <h1>IPL Premier Analytics (2008–2026)</h1>
                <p>Explore nineteen seasons of cricket history, championship dynasties, run-scoring trends, and bowling records powered by granular ball-by-ball analysis.</p>
            </div>
            <div style="display: flex; gap: 15px; align-items: center;">
                <div style="text-align: center; background: rgba(0,0,0,0.4); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 14px; padding: 15px 22px;">
                    <div style="font-family: 'Teko'; font-size: 42px; font-weight: 700; color: #f59e0b; line-height: 1;">19</div>
                    <div style="font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">Seasons</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Calculate Tournament High-Level KPIs
    total_matches = matches.shape[0]
    total_runs = deliveries['total_runs'].sum()
    total_sixes = (deliveries['batsman_runs'] == 6).sum()
    total_fours = (deliveries['batsman_runs'] == 4).sum()
    
    w_df = deliveries.dropna(subset=['player_dismissed'])
    w_df = w_df[w_df['dismissal_kind'] != 'run out']
    total_wickets = w_df.shape[0]
    
    most_wins_team = matches['winner'].value_counts().index[0]
    most_wins_count = matches['winner'].value_counts().iloc[0]
    
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Matches", f"{total_matches:,}")
    c2.metric("Total Runs Scored", f"{total_runs:,}")
    c3.metric("Bowler Wickets", f"{total_wickets:,}")
    c4.metric("Total Sixes (6s)", f"{total_sixes:,}")
    c5.metric("Most Successful Team", most_wins_team, f"{most_wins_count} Wins")
    
    st.header("🏆 IPL Championship Dynasties")
    st.markdown("Dynamic title distribution calculated from all season finals (2008 to 2026):")
    
    # Calculate dynamic season champions
    matches_sorted = matches.copy()
    matches_sorted['date'] = pd.to_datetime(matches_sorted['date'])
    matches_sorted = matches_sorted.sort_values('date')
    season_finals = matches_sorted.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']]
    
    # Accurate title tally
    title_tally = season_finals['winner'].value_counts().reset_index()
    title_tally.columns = ['Team', 'Titles Won']
    
    # Display Trophy Showcase Cards
    st.markdown('<div class="trophy-grid">', unsafe_allow_html=True)
    trophy_cols = st.columns(len(title_tally))
    for idx, row in title_tally.iterrows():
        team_n = row['Team']
        titles_n = row['Titles Won']
        team_seasons = season_finals[season_finals['winner'] == team_n]['season'].tolist()
        seasons_str = ", ".join([str(s) for s in team_seasons])
        
        with trophy_cols[idx]:
            logo_img = get_team_logo_base64(team_n)
            st.markdown(f"""
            <div class="trophy-card">
                <div class="trophy-count-pill">🏆 x{titles_n}</div>
                <img src="{logo_img}" style="width: 70px; height: 70px; object-fit: contain; margin: 10px 0 12px 0;">
                <div style="font-family: 'Outfit'; font-weight: 800; font-size: 15px; color: #fff; line-height: 1.2;">{team_n}</div>
                <div style="font-size: 11px; color: #94a3b8; margin-top: 6px;">{seasons_str}</div>
            </div>
            """, unsafe_allow_html=True)
            
    # Chart with exact franchise branding colors
    fig_champs = plot_plotly_bar(title_tally, 'Team', 'Titles Won', "IPL Championship Titles Won (All-Time)")
    st.plotly_chart(fig_champs, use_container_width=True, theme=None)
    
    st.markdown("---")
    st.header("📈 Season Evolution: Total Runs & Wickets")
    
    season_stats = matches[['id', 'season']].merge(deliveries, left_on='id', right_on='match_id')
    runs_per_season = season_stats.groupby('season')['total_runs'].sum().reset_index()
    wickets_per_season = season_stats.dropna(subset=['player_dismissed']).groupby('season')['player_dismissed'].count().reset_index(name='wickets')
    
    r_col, w_col = st.columns(2)
    with r_col:
        fig_runs = px.bar(runs_per_season, x='season', y='total_runs', text='total_runs', title="Runs Scored per Season", color_discrete_sequence=['#f59e0b'])
        fig_runs.update_traces(textposition='outside')
        fig_runs.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Runs")
        st.plotly_chart(fig_runs, use_container_width=True, theme=None)
        
    with w_col:
        fig_wkts = px.bar(wickets_per_season, x='season', y='wickets', text='wickets', title="Wickets Taken per Season", color_discrete_sequence=['#38bdf8'])
        fig_wkts.update_traces(textposition='outside')
        fig_wkts.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Wickets")
        st.plotly_chart(fig_wkts, use_container_width=True, theme=None)


# ==========================================
# 🛡️ PAGE 2: TEAM ANALYSIS
# ==========================================
elif page == "Team Analysis":
    st.title("🛡️ Franchise Deep Dive & Performance")
    
    all_teams_list = sorted([str(t) for t in matches['team1'].dropna().unique() if str(t).strip()])
    team = st.selectbox("Select Franchise", all_teams_list, index=all_teams_list.index('Mumbai Indians') if 'Mumbai Indians' in all_teams_list else 0)
    
    team_matches = matches[(matches['team1'] == team) | (matches['team2'] == team)]
    wins = team_matches[team_matches['winner'] == team].shape[0]
    total_m = team_matches.shape[0]
    losses = total_m - wins
    win_pct = round((wins / total_m * 100), 2) if total_m > 0 else 0
    
    team_logo = get_team_logo_base64(team)
    brand_color = IPL_TEAM_COLORS.get(team, '#f59e0b')
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #0d1424 0%, #17233d 100%); border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); border-left: 6px solid {brand_color}; padding: 25px 30px; margin: 20px 0 30px 0; display: flex; align-items: center; gap: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="width: 100px; height: 100px; background: rgba(0,0,0,0.3); border-radius: 50%; padding: 12px; display: flex; align-items: center; justify-content: center; border: 2px solid {brand_color};">
            <img src="{team_logo}" style="max-width: 100%; max-height: 100%; object-fit: contain;">
        </div>
        <div>
            <div style="font-family: 'Outfit'; font-size: 32px; font-weight: 900; color: #fff; text-transform: uppercase; letter-spacing: 0.5px;">{team}</div>
            <div style="font-size: 15px; color: #94a3b8; font-weight: 500; margin-top: 4px;">Historical Record: <span style="color: #10b981; font-weight: 700;">{wins} Wins</span> | <span style="color: #ef4444; font-weight: 700;">{losses} Losses</span> ({win_pct}% Win Rate)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Matches Contested", total_m)
    col2.metric("Total Victories", wins)
    col3.metric("Win Conversion %", f"{win_pct}%")
    
    team_del_bat = deliveries[deliveries['batting_team'] == team]
    team_runs = team_del_bat['total_runs'].sum()
    
    team_del_bowl = deliveries[deliveries['bowling_team'] == team]
    team_wickets = team_del_bowl.dropna(subset=['player_dismissed'])
    team_wickets = team_wickets[team_wickets['dismissal_kind'] != 'run out'].shape[0]
    team_catches = team_del_bowl[team_del_bowl['dismissal_kind'] == 'caught'].shape[0]
    
    col4, col5, col6 = st.columns(3)
    col4.metric("Franchise Runs Scored", f"{team_runs:,}")
    col5.metric("Bowler Wickets Taken", f"{team_wickets:,}")
    col6.metric("Total Catches Taken", f"{team_catches:,}")
    
    st.header("🏆 All-Time Franchise Wins Leaderboard")
    win_counts = matches['winner'].value_counts().reset_index()
    win_counts.columns = ['Team', 'Wins']
    fig_all_wins = plot_plotly_bar(win_counts.head(10), 'Team', 'Wins', 'Top 10 Most Successful Franchises (Matches Won)')
    st.plotly_chart(fig_all_wins, use_container_width=True, theme=None)


# ==========================================
# ⭐ PAGE 3: PLAYER ANALYSIS
# ==========================================
elif page == "Player Analysis":
    st.title("⭐ Individual Mastery & Bat/Ball Contenders")
    
    t1, t2, t3 = st.tabs(["🏏 Batting Leaders", "🎯 Bowling Leaders", "🧤 Safe Hands (Fielding)"])
    
    with t1:
        st.header("Top Run Scorers (Orange Cap Titans)")
        batsman_stats = deliveries.groupby('batsman')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False)
        st.plotly_chart(plot_plotly_bar(batsman_stats.head(10), 'batsman', 'batsman_runs', 'All-Time Highest Run Scorers in IPL History'), use_container_width=True, theme=None)
        
    with t2:
        st.header("Top Wicket Takers (Purple Cap Kings)")
        bowler_stats = deliveries.dropna(subset=['player_dismissed'])
        bowler_stats = bowler_stats[bowler_stats['dismissal_kind'] != 'run out']
        wickets_df = bowler_stats.groupby('bowler').size().reset_index(name='wickets').sort_values('wickets', ascending=False)
        st.plotly_chart(plot_plotly_bar(wickets_df.head(10), 'bowler', 'wickets', 'All-Time Highest Wicket Takers in IPL History'), use_container_width=True, theme=None)
        
    with t3:
        st.header("Most Catches (Elite Fielders)")
        catches_df = deliveries[deliveries['dismissal_kind'] == 'caught'].groupby('fielder').size().reset_index(name='catches').sort_values('catches', ascending=False)
        st.plotly_chart(plot_plotly_bar(catches_df.head(10), 'fielder', 'catches', 'All-Time Most Catches by Fielders'), use_container_width=True, theme=None)


# ==========================================
# 🃏 PAGE 4: PLAYER PROFILE (ULTIMATE CARD)
# ==========================================
elif page == "Player Profile (FIFA Card)":
    st.title("🃏 Premier Player Profile (Ultimate Team Card)")
    st.markdown("Statistical player scouting card with dynamically computed FIFA/Ultimate Team T20 overall rating.")
    
    all_players = pd.concat([deliveries['batsman'], deliveries['bowler']]).dropna().unique()
    sorted_players = sorted(all_players)
    default_idx = sorted_players.index('V Kohli') if 'V Kohli' in sorted_players else 0
    player = st.selectbox("Search & Inspect Player", sorted_players, index=default_idx)
    
    # Calculate Authentic Granular Stats
    b_df = deliveries[deliveries['batsman'] == player]
    runs = b_df['batsman_runs'].sum()
    balls_faced = b_df.shape[0] - (b_df['extras_type'] == 'wides').sum() if 'extras_type' in b_df.columns else b_df.shape[0]
    sr = round((runs / balls_faced) * 100, 2) if balls_faced > 0 else 0
    outs = deliveries[deliveries['player_dismissed'] == player].shape[0]
    avg = round(runs / outs, 2) if outs > 0 else runs
    
    bowl_df = deliveries[deliveries['bowler'] == player]
    w_df_p = bowl_df.dropna(subset=['player_dismissed'])
    wickets = w_df_p[w_df_p['dismissal_kind'] != 'run out'].shape[0]
    
    runs_conceded = bowl_df['total_runs'].sum() - (bowl_df[bowl_df['extras_type'] == 'legbyes']['total_runs'].sum() if 'extras_type' in bowl_df.columns else 0)
    balls_bowled = bowl_df.shape[0]
    eco = round((runs_conceded / balls_bowled) * 6, 2) if balls_bowled > 0 else 0
    catches = deliveries[(deliveries['fielder'] == player) & (deliveries['dismissal_kind'] == 'caught')].shape[0]
    
    # Determine Dominant Franchise for this player
    player_teams = deliveries[deliveries['batsman'] == player]['batting_team'].value_counts()
    if player_teams.empty:
        player_teams = deliveries[deliveries['bowler'] == player]['bowling_team'].value_counts()
    primary_team = player_teams.index[0] if not player_teams.empty else "IPL Legend"
    
    # Context-Aware Role & Realistic Overall Rating Algorithm
    if balls_bowled >= 150 and balls_faced >= 250:
        role = "ALL-ROUNDER"
        pos_badge = "ALL"
    elif wickets >= 40 or (balls_bowled > balls_faced * 1.5):
        role = "PACE / SPIN BOWLER"
        pos_badge = "BWL"
    elif player in ['MS Dhoni', 'KD Karthik', 'RR Pant', 'Q de Kock', 'KL Rahul', 'SV Samson', 'WP Saha']:
        role = "WICKETKEEPER BATTER"
        pos_badge = "WK-BAT"
    else:
        role = "TOP-ORDER BATSMAN"
        pos_badge = "BAT"
        
    # Calculate balanced rating on a 70-98 scale
    bat_score = (min(runs, 8000) / 8000) * 45 + (min(sr, 160) / 160) * 30 + (min(avg, 45) / 45) * 25
    bowl_score = (min(wickets, 200) / 200) * 50 + (max(0, 10 - eco) / 4) * 30 + (min(catches, 100) / 100) * 20
    
    if pos_badge in ["BAT", "WK-BAT"]:
        base_ovr = int(72 + (bat_score / 100) * 25)
    elif pos_badge == "BWL":
        base_ovr = int(72 + (bowl_score / 100) * 25)
    else: # ALL
        base_ovr = int(70 + ((bat_score * 0.5 + bowl_score * 0.5) / 100) * 27)
        
    overall = min(99, max(74, base_ovr))
    
    # Elite Hall-of-Famer Benchmarks
    legends_benchmark = {
        'V Kohli': 96, 'MS Dhoni': 95, 'RG Sharma': 94, 'AB de Villiers': 96,
        'CH Gayle': 95, 'SK Raina': 94, 'DA Warner': 95, 'SL Malinga': 96,
        'JJ Bumrah': 96, 'SP Narine': 95, 'Rashid Khan': 95, 'AD Russell': 94,
        'KL Rahul': 92, 'B Kumar': 91, 'YS Chahal': 92, 'RA Jadeja': 93
    }
    if player in legends_benchmark:
        overall = legends_benchmark[player]
        
    # Fetch Local or Wikipedia Player Cutout Image
    local_images = {
        'V Kohli': get_base64_image('V_Kohli.jpg'),
        'MS Dhoni': get_base64_image('MS_Dhoni.jpg'),
        'RG Sharma': get_base64_image('RG_Sharma.jpg')
    }
    img_url = local_images.get(player)
    if not img_url:
        wiki_img, _ = fetch_wiki_data(player, is_player=True)
        img_url = wiki_img if wiki_img else f'https://ui-avatars.com/api/?name={player.replace(" ", "+")}&background=0D1424&color=f59e0b&size=250&font-size=0.33&bold=true'
        
    # Render Elevated FIFA / Ultimate Card
    card_html = f"""
    <div class="fut-card-wrapper">
        <div class="fut-card">
            <div class="fut-top-bar">
                <div style="text-align: left;">
                    <div class="fut-ovr">{overall}</div>
                    <div class="fut-pos-badge">{pos_badge}</div>
                </div>
                <div class="fut-league-badge">IPL ELITE</div>
            </div>
            
            <div class="fut-avatar-ring">
                <img src="{img_url}" alt="{player}">
            </div>
            
            <div class="fut-player-name">{player}</div>
            <div class="fut-team-tag">{primary_team}</div>
            
            <div class="fut-stats-grid">
                <div class="fut-stat-box">
                    <span class="fut-stat-val">{int(runs)}</span>
                    <span class="fut-stat-lbl">RUNS</span>
                </div>
                <div class="fut-stat-box">
                    <span class="fut-stat-val">{int(wickets)}</span>
                    <span class="fut-stat-lbl">WKTS</span>
                </div>
                <div class="fut-stat-box">
                    <span class="fut-stat-val">{avg}</span>
                    <span class="fut-stat-lbl">AVG</span>
                </div>
                <div class="fut-stat-box">
                    <span class="fut-stat-val">{sr}</span>
                    <span class="fut-stat-lbl">SR</span>
                </div>
                <div class="fut-stat-box">
                    <span class="fut-stat-val">{eco}</span>
                    <span class="fut-stat-lbl">ECON</span>
                </div>
                <div class="fut-stat-box">
                    <span class="fut-stat-val">{catches}</span>
                    <span class="fut-stat-lbl">CATCH</span>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Advanced Statistical Breakdown
    if st.checkbox("Show Advanced Career Analytics & Season Trajectory", value=True):
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Top 5 Favourite Opponents (Runs)")
            bat_vs_team = b_df.groupby('bowling_team')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False).head(5)
            if not bat_vs_team.empty:
                fig1 = plot_plotly_bar(bat_vs_team, 'bowling_team', 'batsman_runs', f"Runs Scored Against Opponents ({player})", color_col='bowling_team')
                st.plotly_chart(fig1, use_container_width=True, theme=None)
            else:
                st.info("No batting dismissal or run data available.")
                
        with c2:
            st.subheader("Bowling Dismissal Profile & Ball Dynamics")
            if wickets > 0:
                dismissal_wkts = w_df_p['dismissal_kind'].value_counts().reset_index()
                dismissal_wkts.columns = ['Dismissal Kind', 'Wickets']
                fig_diss = px.pie(dismissal_wkts, values='Wickets', names='Dismissal Kind', hole=0.45, title="Dismissal Breakdown (Mode of Out)", color_discrete_sequence=['#f59e0b', '#38bdf8', '#10b981', '#f472b6'])
                fig_diss.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig_diss, use_container_width=True, theme=None)
            else:
                st.info("No bowling figures recorded for this player.")
                
        st.markdown("---")
        st.subheader("📈 Season-by-Season Career Growth")
        b_season = pd.merge(b_df, matches[['id', 'season']], left_on='match_id', right_on='id')
        bowl_season = pd.merge(bowl_df, matches[['id', 'season']], left_on='match_id', right_on='id')
        
        gc1, gc2 = st.columns(2)
        with gc1:
            if not b_season.empty:
                bat_growth = b_season.groupby('season')['batsman_runs'].sum().reset_index()
                fig_bat_growth = px.bar(bat_growth, x='season', y='batsman_runs', text='batsman_runs', title=f"Runs per Season ({player})", color_discrete_sequence=['#f59e0b'])
                fig_bat_growth.update_traces(textposition='outside')
                fig_bat_growth.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Runs")
                st.plotly_chart(fig_bat_growth, use_container_width=True, theme=None)
            else:
                st.info("No batting growth data available.")
                
        with gc2:
            wkt_season = bowl_season.dropna(subset=['player_dismissed'])
            wkt_season = wkt_season[wkt_season['dismissal_kind'] != 'run out']
            if not wkt_season.empty:
                bowl_growth = wkt_season.groupby('season')['player_dismissed'].count().reset_index()
                bowl_growth.columns = ['season', 'wickets']
                fig_bowl_growth = px.bar(bowl_growth, x='season', y='wickets', text='wickets', title=f"Wickets per Season ({player})", color_discrete_sequence=['#38bdf8'])
                fig_bowl_growth.update_traces(textposition='outside')
                fig_bowl_growth.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Wickets")
                st.plotly_chart(fig_bowl_growth, use_container_width=True, theme=None)
            else:
                st.info("No bowling growth data available.")


# ==========================================
# 🏟️ PAGE 5: VENUE ANALYSIS
# ==========================================
elif page == "Venue Analysis":
    st.title("🏟️ Stadium Intelligence & Pitch Behaviors")
    
    all_venues = sorted([str(v) for v in matches['venue'].dropna().unique() if str(v).strip()])
    selected_venue = st.selectbox("Select Cricket Stadium", all_venues)
    
    if selected_venue:
        wiki_img, wiki_desc = fetch_wiki_data(selected_venue, is_player=False)
        st.subheader(selected_venue)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            if wiki_img:
                st.image(wiki_img, use_container_width=True)
            else:
                st.info("Stadium architectural photo not available in directory.")
        with col2:
            if wiki_desc:
                st.write(wiki_desc)
            else:
                st.write("A premier international cricket stadium hosting high-intensity T20 clashes with typical boundary dimensions between 65 to 78 meters.")
            venue_matches = matches[matches['venue'] == selected_venue]
            st.metric("Total IPL Clashes Hosted", venue_matches.shape[0])
            
    st.markdown("---")
    venue_counts = matches['venue'].value_counts().reset_index()
    venue_counts.columns = ['Venue', 'Matches']
    st.plotly_chart(plot_plotly_bar(venue_counts.head(10), 'Venue', 'Matches', 'Top 10 Most Frequently Used IPL Stadiums'), use_container_width=True, theme=None)
    
    st.header("Highest Scoring Grounds (Average Match Runs)")
    venue_runs = matches[['id', 'venue']].merge(deliveries, left_on='id', right_on='match_id')
    avg_runs_venue = venue_runs.groupby(['venue', 'match_id'])['total_runs'].sum().reset_index()
    avg_runs_venue = avg_runs_venue.groupby('venue')['total_runs'].mean().reset_index().sort_values('total_runs', ascending=False)
    st.plotly_chart(plot_plotly_bar(avg_runs_venue.head(10), 'venue', 'total_runs', 'Average Total Runs per Match by Stadium'), use_container_width=True, theme=None)


# ==========================================
# 🪙 PAGE 6: TOSS ANALYSIS
# ==========================================
elif page == "Toss Analysis":
    st.title("🪙 Toss Impact & Strategic Decisions")
    
    col1, col2 = st.columns(2)
    with col1:
        toss_decision = matches['toss_decision'].value_counts()
        fig = px.pie(values=toss_decision.values, names=toss_decision.index, title="Toss Decision Preferences (Bat vs Field)", color_discrete_sequence=['#38bdf8', '#f59e0b'])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True, theme=None)
        
    with col2:
        matches['toss_win_match_win'] = matches['toss_winner'] == matches['winner']
        toss_impact = matches['toss_win_match_win'].value_counts()
        fig2 = px.pie(values=toss_impact.values, names=['Toss Winner Won', 'Toss Winner Lost'], title="Toss Winner Match Conversion Rate", color_discrete_sequence=['#10b981', '#ef4444'])
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True, theme=None)


# ==========================================
# ⚔️ PAGE 7: MATCH & HEAD-TO-HEAD
# ==========================================
elif page == "Match & Head-to-Head Analysis":
    st.title("⚔️ Franchise Rivalries & Head-to-Head Arena")
    
    col1, col2 = st.columns(2)
    teams_list = sorted([str(t) for t in matches['team1'].dropna().unique() if str(t).strip()])
    t1 = col1.selectbox("Franchise A", teams_list, index=teams_list.index('Mumbai Indians') if 'Mumbai Indians' in teams_list else 0)
    t2 = col2.selectbox("Franchise B", teams_list, index=teams_list.index('Chennai Super Kings') if 'Chennai Super Kings' in teams_list else 1)
    
    if t1 != t2:
        h2h = matches[((matches['team1'] == t1) & (matches['team2'] == t2)) | ((matches['team1'] == t2) & (matches['team2'] == t1))]
        if not h2h.empty:
            wins = h2h['winner'].value_counts()
            fig = px.pie(
                values=wins.values, 
                names=wins.index, 
                title=f"Head-to-Head Encounters: {t1} vs {t2} ({h2h.shape[0]} Matches)",
                color=wins.index,
                color_discrete_map=IPL_TEAM_COLORS
            )
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig, use_container_width=True, theme=None)
        else:
            st.info("No recorded historical matches between these two franchises.")
            
    st.header("Largest Victories by Run Margin")
    big_runs = matches.sort_values('win_by_runs', ascending=False)[['season', 'winner', 'win_by_runs', 'team1', 'team2']].head(5)
    st.dataframe(big_runs, hide_index=True, use_container_width=True)


# ==========================================
# 📊 PAGE 8: ADVANCED ANALYTICS
# ==========================================
elif page == "Advanced Analytics":
    st.title("📊 Phase-Wise Match Dynamics & Scoring Tempo")
    
    def get_phase(over):
        if over <= 6: return "Powerplay (Overs 1-6)"
        elif over <= 15: return "Middle Overs (Overs 7-15)"
        else: return "Death Overs (Overs 16-20)"
        
    deliveries_copy = deliveries.copy()
    deliveries_copy['phase'] = deliveries_copy['over'].apply(get_phase)
    phase_runs = deliveries_copy.groupby('phase')['total_runs'].sum().reset_index()
    
    fig = px.bar(
        phase_runs, 
        x='phase', 
        y='total_runs', 
        title="Total Runs Accumulated by Match Phase (All-Time)", 
        color='phase',
        color_discrete_sequence=['#38bdf8', '#f59e0b', '#ef4444'],
        text_auto=True
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(fig, use_container_width=True, theme=None)


# ==========================================
# 🧠 PAGE 9: AI MATCH STRATEGY GENERATOR
# ==========================================
elif page == "AI Match Strategy Generator":
    st.title("🧠 AI Match Strategy & Pitch Tactical Engine")
    st.markdown("Generate venue-specific tactical field blueprints, pitch behavior analysis, and head-to-head tactical previews.")
    
    col1, col2, col3 = st.columns(3)
    all_venues = sorted([str(v) for v in matches['venue'].dropna().unique() if str(v).strip()])
    all_teams = sorted([str(t) for t in matches['team1'].dropna().unique() if str(t).strip()])
    
    stadium = col1.selectbox("Select Match Venue", all_venues)
    t1 = col2.selectbox("Team 1", all_teams, index=all_teams.index('Mumbai Indians') if 'Mumbai Indians' in all_teams else 0)
    t2 = col3.selectbox("Team 2", all_teams, index=all_teams.index('Chennai Super Kings') if 'Chennai Super Kings' in all_teams else 1)
    
    if t1 == t2:
        st.warning("Please choose two distinct franchises for the tactical clash.")
    elif st.button("Generate Tactical Battle Plan 🚀"):
        logo_t1 = get_team_logo_base64(t1)
        logo_t2 = get_team_logo_base64(t2)
        
        st.markdown(f"""
        <div class="versus-arena-card">
            <div class="arena-team-box">
                <img class="arena-team-logo" src="{logo_t1}">
                <div style="font-family: 'Outfit'; font-size: 22px; font-weight: 800; color: #38bdf8;">{t1}</div>
            </div>
            <div class="arena-vs-divider">
                <div class="arena-vs-text">VS</div>
                <div style="font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase;">Match Clash</div>
            </div>
            <div class="arena-team-box">
                <img class="arena-team-logo" src="{logo_t2}">
                <div style="font-family: 'Outfit'; font-size: 22px; font-weight: 800; color: #f59e0b;">{t2}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        m_venue = matches[matches['venue'] == stadium]
        d_venue = deliveries[deliveries['match_id'].isin(m_venue['id'])]
        
        # 1. Expected First Innings Score
        if not d_venue.empty:
            inn1 = d_venue[d_venue['inning'] == 1].groupby('match_id')['total_runs'].sum()
            avg_score = int(inn1.mean()) if pd.notna(inn1.mean()) else "N/A"
        else:
            avg_score = "N/A"
            
        # 2. Batting First vs Chasing
        bat_first = m_venue[m_venue['win_by_runs'] > 0].shape[0]
        chasing = m_venue[m_venue['win_by_wickets'] > 0].shape[0]
        tot = bat_first + chasing
        bat_first_pct = round((bat_first / tot) * 100, 1) if tot > 0 else 0
        chasing_pct = round((chasing / tot) * 100, 1) if tot > 0 else 0
        
        toss_dec = "Bowl First (Chasing bias)" if chasing_pct > bat_first_pct else "Bat First (Defend total)"
        if chasing_pct == bat_first_pct: toss_dec = "Neutral (Conditions open)"
        
        # 3. Spin vs Pace
        known_spinners = {'Rashid Khan', 'YS Chahal', 'SP Narine', 'R Ashwin', 'RA Jadeja', 'A Mishra', 'PP Chawla', 'Kuldeep Yadav', 'CV Varun', 'Mujeeb Ur Rahman', 'Imran Tahir', 'Harbhajan Singh', 'R Bishnoi', 'Washington Sundar', 'AR Patel'}
        v_wkts = d_venue.dropna(subset=['player_dismissed'])
        v_wkts = v_wkts[v_wkts['dismissal_kind'] != 'run out']
        spin_wkts = v_wkts[v_wkts['bowler'].isin(known_spinners)].shape[0]
        total_v_wkts = v_wkts.shape[0]
        pace_wkts = total_v_wkts - spin_wkts
        spin_pct = round((spin_wkts / total_v_wkts) * 100, 1) if total_v_wkts > 0 else 0
        pace_pct = round((pace_wkts / total_v_wkts) * 100, 1) if total_v_wkts > 0 else 0
        
        st.subheader(f"🏟️ Stadium Insights: {stadium}")
        sc1, sc2, sc3, sc4 = st.columns(4)
        sc1.metric("Avg 1st Inn Score", avg_score)
        sc2.metric("Batting First Win %", f"{bat_first_pct}%")
        sc3.metric("Chasing Win %", f"{chasing_pct}%")
        sc4.metric("Toss Tactical Call", toss_dec)
        
        st.markdown("---")
        st.subheader("🎯 Pitch Behavior (Pace vs Spin Breakdown)")
        if total_v_wkts > 0:
            st.progress(pace_pct / 100)
            st.markdown(f"**⚡ Pace Bowlers:** {pace_pct}% Wickets | **🌀 Spinners:** {spin_pct}% Wickets")
            
        # Tactical Pitch Blueprint
        if pace_pct > 60:
            p_type = "Pace & Carry (Hard Surface)"
            b_line = "Hard Length / Back of a Length (Target off-stump channel)"
            c_theme = "#38bdf8"
            pp_field = "1 Slip, 1 Gully, Deep Third Man. Keep mid-off up to tempt the drive."
            mid_field = "Deep Square Leg for the pull, Sweeper Cover. Pace variations."
            dth_field = "Fine Leg inside circle, Deep Mid-wicket, Long-on, Long-off. Wide Yorkers."
            capt_plan = "Deploy strike pacers in 2-over burst spells to maximize early swing."
        elif spin_pct > 40:
            p_type = "Dry & Turning (Spin Trap)"
            b_line = "Good Length / Fuller (Tempt batsman forward with drift)"
            c_theme = "#f59e0b"
            pp_field = "1 Slip, Mid-on up. Introduce spin early inside powerplay."
            mid_field = "Deep Mid-wicket, Long-on, Sweeper Cover. Constrict strike rotation."
            dth_field = "Long-on, Long-off, Deep Square Leg. Fire flat into leg-stump."
            capt_plan = "Ring the infield with catching fielders and starve boundaries."
        else:
            p_type = "True & Balanced Batting Track"
            b_line = "Varied Lengths (Cutters, Slower bouncers, Wide yorkers)"
            c_theme = "#10b981"
            pp_field = "Standard ring setup. Keep third man on boundary."
            mid_field = "Deep Cover, Deep Mid-wicket. Restrict big boundary pockets."
            dth_field = "Protect straight boundaries. Long-on, Long-off, Deep Point."
            capt_plan = "Bowl defensively to batsman's cold zones and rely on change of pace."
            
        st.markdown(f"""
        <div class="tactical-blueprint" style="border-top: 4px solid {c_theme};">
            <div style="font-family: 'Outfit'; font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 16px;">
                Pitch Profile: <span style="color: {c_theme};">{p_type}</span>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
                <div style="background: rgba(0,0,0,0.3); border-left: 4px solid {c_theme}; padding: 16px; border-radius: 10px;">
                    <div style="font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase;">🎯 Target Bowling Corridor</div>
                    <div style="font-size: 15px; font-weight: 700; color: #fff; margin-top: 4px;">{b_line}</div>
                </div>
                <div style="background: rgba(0,0,0,0.3); border-left: 4px solid #10b981; padding: 16px; border-radius: 10px;">
                    <div style="font-size: 11px; font-weight: 800; color: #94a3b8; text-transform: uppercase;">💡 Captain's Blueprint</div>
                    <div style="font-size: 14px; color: #cbd5e1; margin-top: 4px;">{capt_plan}</div>
                </div>
            </div>
            
            <div style="font-size: 13px; font-weight: 800; color: #f8fafc; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">⏱️ Phase-by-Phase Field Placements</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 14px; border-radius: 10px;">
                    <div style="color: #38bdf8; font-weight: 800; font-size: 13px; text-transform: uppercase;">Powerplay (Overs 1-6)</div>
                    <div style="color: #cbd5e1; font-size: 13px; margin-top: 4px;">{pp_field}</div>
                </div>
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 14px; border-radius: 10px;">
                    <div style="color: #f59e0b; font-weight: 800; font-size: 13px; text-transform: uppercase;">Middle Overs (Overs 7-15)</div>
                    <div style="color: #cbd5e1; font-size: 13px; margin-top: 4px;">{mid_field}</div>
                </div>
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); padding: 14px; border-radius: 10px;">
                    <div style="color: #ef4444; font-weight: 800; font-size: 13px; text-transform: uppercase;">Death Overs (Overs 16-20)</div>
                    <div style="color: #cbd5e1; font-size: 13px; margin-top: 4px;">{dth_field}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 🏆 PAGE 10: SEASON RECORDS & AWARDS
# ==========================================
elif page == "Season Records & Awards":
    st.title("🏆 IPL Season Honors & Cap Winners")
    
    seasons = sorted(matches['season'].dropna().unique(), reverse=True)
    selected_season = st.selectbox("Select Season", seasons)
    
    season_matches = matches[matches['season'] == selected_season]
    season_deliveries = deliveries[deliveries['match_id'].isin(season_matches['id'])]
    
    col1, col2, col3 = st.columns(3)
    
    # Orange Cap
    if not season_deliveries.empty:
        orange_cap = season_deliveries.groupby('batsman')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False).iloc[0]
        col1.markdown(f"### 🏏 Orange Cap\n**{orange_cap['batsman']}**\n\n**{int(orange_cap['batsman_runs'])}** Runs")
        o_img, _ = fetch_wiki_data(orange_cap['batsman'], is_player=True)
        if o_img: col1.image(o_img, width=150)
        
    # Purple Cap
    if not season_deliveries.empty:
        bowl_st = season_deliveries.dropna(subset=['player_dismissed'])
        bowl_st = bowl_st[bowl_st['dismissal_kind'] != 'run out']
        if not bowl_st.empty:
            purple_cap = bowl_st.groupby('bowler').size().reset_index(name='wickets').sort_values('wickets', ascending=False).iloc[0]
            col2.markdown(f"### 🎯 Purple Cap\n**{purple_cap['bowler']}**\n\n**{purple_cap['wickets']}** Wickets")
            p_img, _ = fetch_wiki_data(purple_cap['bowler'], is_player=True)
            if p_img: col2.image(p_img, width=150)
            
    # MVP
    if not season_matches.empty and 'player_of_match' in season_matches.columns:
        pom_counts = season_matches['player_of_match'].value_counts()
        if not pom_counts.empty:
            best_p = pom_counts.index[0]
            col3.markdown(f"### ⭐ MVP (Most POM)\n**{best_p}**\n\n**{pom_counts.iloc[0]}** Awards")
            m_img, _ = fetch_wiki_data(best_p, is_player=True)
            if m_img: col3.image(m_img, width=150)
            
    st.markdown("---")
    st.subheader(f"Top 5 Run Scorers in {selected_season}")
    st.dataframe(season_deliveries.groupby('batsman')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False).head(5), hide_index=True, use_container_width=True)


# ==========================================
# 📜 PAGE 11: ALL-TIME IPL RECORDS
# ==========================================
elif page == "All-Time IPL Records":
    st.title("📜 All-Time IPL Historical Records (2008–2026)")
    st.markdown("Complete statistical record book spanning all nineteen editions of the tournament.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🛡️ Team Records", "🏏 Batting Records", "🎯 Bowling Records", "🧤 Fielding & Extras"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Highest Team Innings Totals")
            t_scores = deliveries.groupby(['match_id', 'batting_team'])['total_runs'].sum().reset_index()
            st.dataframe(t_scores.sort_values('total_runs', ascending=False).head(5)[['batting_team', 'total_runs']], hide_index=True, use_container_width=True)
            
            st.subheader("Largest Run Margins of Victory")
            st.dataframe(matches.sort_values('win_by_runs', ascending=False).head(5)[['winner', 'win_by_runs', 'season']], hide_index=True, use_container_width=True)
        with c2:
            st.subheader("Lowest Totals (Completed/Defended)")
            st.dataframe(t_scores[t_scores['total_runs'] >= 45].sort_values('total_runs', ascending=True).head(5)[['batting_team', 'total_runs']], hide_index=True, use_container_width=True)
            
            st.subheader("Most Franchise Match Wins")
            st.dataframe(matches['winner'].value_counts().head(5).reset_index(), hide_index=True, use_container_width=True)
            
    with tab2:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("Most Career Runs")
            runs = deliveries.groupby('batsman')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False)
            st.dataframe(runs.head(8), hide_index=True, use_container_width=True)
            
            st.subheader("Most Career Sixes (6s)")
            sixes = deliveries[deliveries['batsman_runs'] == 6].groupby('batsman').size().reset_index(name='sixes').sort_values('sixes', ascending=False)
            st.dataframe(sixes.head(5), hide_index=True, use_container_width=True)
        with c2:
            st.subheader("Highest Individual Scores")
            hs = deliveries.groupby(['match_id', 'batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False)
            st.dataframe(hs.head(5)[['batsman', 'batsman_runs']], hide_index=True, use_container_width=True)
            
            st.subheader("Most Centuries (100+)")
            hundreds = hs[hs['batsman_runs'] >= 100].groupby('batsman').size().reset_index(name='hundreds').sort_values('hundreds', ascending=False)
            st.dataframe(hundreds.head(5), hide_index=True, use_container_width=True)
        with c3:
            st.subheader("Highest Strike Rate (Min 500 Balls)")
            bf = deliveries[~deliveries['extras_type'].isin(['wides'])].groupby('batsman').size().reset_index(name='balls') if 'extras_type' in deliveries.columns else deliveries.groupby('batsman').size().reset_index(name='balls')
            sr_df = pd.merge(runs, bf, on='batsman')
            sr_df = sr_df[sr_df['balls'] >= 500]
            sr_df['strike_rate'] = round((sr_df['batsman_runs'] / sr_df['balls']) * 100, 2)
            st.dataframe(sr_df.sort_values('strike_rate', ascending=False).head(5)[['batsman', 'strike_rate']], hide_index=True, use_container_width=True)
            
    with tab3:
        c1, c2 = st.columns(2)
        b_wkts = deliveries.dropna(subset=['player_dismissed'])
        b_wkts = b_wkts[b_wkts['dismissal_kind'] != 'run out']
        with c1:
            st.subheader("Most Career Wickets")
            wkt_all = b_wkts.groupby('bowler').size().reset_index(name='wickets').sort_values('wickets', ascending=False)
            st.dataframe(wkt_all.head(8), hide_index=True, use_container_width=True)
        with c2:
            st.subheader("Best Economy Rate (Min 500 Balls)")
            b_bowled = deliveries.groupby('bowler').size().reset_index(name='balls')
            runs_c = deliveries.groupby('bowler')['total_runs'].sum().reset_index(name='runs')
            eco_df = pd.merge(b_bowled[b_bowled['balls'] >= 500], runs_c, on='bowler')
            eco_df['economy'] = round((eco_df['runs'] / eco_df['balls']) * 6, 2)
            st.dataframe(eco_df.sort_values('economy', ascending=True).head(5)[['bowler', 'economy']], hide_index=True, use_container_width=True)
            
    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Most Catches by Fielders")
            catches = deliveries[deliveries['dismissal_kind'] == 'caught'].groupby('fielder').size().reset_index(name='catches').sort_values('catches', ascending=False)
            st.dataframe(catches.head(8), hide_index=True, use_container_width=True)
        with c2:
            st.subheader("Most Run Outs Effected")
            runouts = deliveries[deliveries['dismissal_kind'] == 'run out'].groupby('fielder').size().reset_index(name='run_outs').sort_values('run_outs', ascending=False)
            st.dataframe(runouts.head(8), hide_index=True, use_container_width=True)


# ==========================================
# 🌟 PAGE 12: TOP 50 GREATEST PLAYERS
# ==========================================
elif page == "Top 50 Greatest Players":
    st.title("🌟 Hall of Fame: Top 50 Greatest IPL Players")
    st.markdown("Statistical composite ranking balancing all-time runs, wickets, and match impact across 19 seasons.")
    
    bat_st = deliveries.groupby('batsman')['batsman_runs'].sum().reset_index()
    b_wkts = deliveries.dropna(subset=['player_dismissed'])
    b_wkts = b_wkts[b_wkts['dismissal_kind'] != 'run out']
    wkt_st = b_wkts.groupby('bowler').size().reset_index(name='wickets')
    
    bat_st.columns = ['player', 'runs']
    wkt_st.columns = ['player', 'wickets']
    
    all_p = pd.merge(bat_st, wkt_st, on='player', how='outer').fillna(0)
    all_p['composite_score'] = (all_p['runs'] * 1.0) + (all_p['wickets'] * 25.0)
    all_p = all_p.sort_values('composite_score', ascending=False).reset_index(drop=True)
    
    # Top 3 Podium Cards
    p1, p2, p3 = st.columns(3)
    top3 = all_p.head(3)
    
    medals = [("🥇 Rank 1", "#f59e0b"), ("🥈 Rank 2", "#cbd5e1"), ("🥉 Rank 3", "#d97706")]
    for i, col in enumerate([p1, p2, p3]):
        row_p = top3.iloc[i]
        p_name = row_p['player']
        p_img, _ = fetch_wiki_data(p_name, is_player=True)
        if not p_img: p_img = f"https://ui-avatars.com/api/?name={p_name.replace(' ', '+')}&background=0D1424&color=f59e0b"
        
        with col:
            st.markdown(f"""
            <div style="background: #0d1424; border: 2px solid {medals[i][1]}; border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <div style="font-family: 'Outfit'; font-weight: 800; font-size: 16px; color: {medals[i][1]};">{medals[i][0]}</div>
                <img src="{p_img}" style="width: 85px; height: 85px; border-radius: 50%; object-fit: cover; margin: 10px 0; border: 2px solid {medals[i][1]};">
                <div style="font-family: 'Outfit'; font-size: 20px; font-weight: 800; color: #fff;">{p_name}</div>
                <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">{int(row_p['runs']):,} Runs | {int(row_p['wickets'])} Wickets</div>
                <div style="font-family: 'Teko'; font-size: 24px; font-weight: 700; color: {medals[i][1]}; margin-top: 6px;">Impact Index: {int(row_p['composite_score']):,}</div>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("---")
    st.subheader("Top 50 Comprehensive Leaderboard")
    all_p['Rank'] = np.arange(1, len(all_p) + 1)
    st.dataframe(all_p.head(50)[['Rank', 'player', 'runs', 'wickets', 'composite_score']], hide_index=True, use_container_width=True)


# ==========================================
# 👑 PAGE 13: GREATEST TEAM OF ALL TIME
# ==========================================
elif page == "Greatest Team of All Time":
    st.title("👑 Greatest All-Time IPL Playing XI")
    st.markdown("The consensus ultimate lineup of destructive openers, elite anchors, game-finishing all-rounders, and lethal pace-spin attack.")
    
    team_data = {
        "Position": ["1. Opener", "2. Opener", "3. Top Order", "4. Middle Order", "5. Finisher & Wk", "6. All-Rounder", "7. All-Rounder", "8. Mystery Spinner", "9. Leg-Spinner", "10. Death Bowling King", "11. Pace Spearhead"],
        "Legendary Player": ["Virat Kohli", "Chris Gayle", "Suresh Raina", "AB de Villiers", "MS Dhoni (Captain & WK)", "Andre Russell", "Kieron Pollard", "Sunil Narine", "Rashid Khan", "Lasith Malinga", "Jasprit Bumrah"],
        "Franchise Dynasty": ["RCB", "KKR / RCB / PBKS", "CSK", "RCB / DD", "CSK", "KKR", "MI", "KKR", "SRH / GT", "MI", "MI"],
        "Specialty Role": ["Anchor & Aggressor (8000+ Runs)", "Universal Boss (Most 6s)", "Mr. IPL (Peak Reliability)", "360° Genius (Strike Rate Monster)", "Master Finisher & Strategist", "Explosive Fast-Bowling Finisher", "Power Finisher & Big-Match Clutch", "Economy Machine & Pinch Hitter", "T20 Googly Magician", "Yorker Searing Legend", "Clutch Precision Pace"]
    }
    st.table(pd.DataFrame(team_data))


# ==========================================
# 📸 PAGE 14: ICONIC IPL MOMENTS GALLERY
# ==========================================
elif page == "📸 Iconic IPL Moments":
    st.markdown(
        """
        <div style="text-align: center; margin: 20px 0 35px 0;">
            <div class="ipl-badge-pill">📸 Visual League Archives</div>
            <h1 style="color: #fff; font-size: 38px; font-weight: 900; margin: 0; text-transform: uppercase; letter-spacing: 1px;">Iconic IPL Moments</h1>
            <p style="color: #94a3b8; font-size: 16px; margin-top: 6px;">Relive the passion, the celebrations, and the glorious champions of the world's biggest cricket stage.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    img_folder = "IMAGE "
    if not os.path.exists(img_folder):
        for candidate in ["IMAGE", "image", "Images", "images"]:
            if os.path.exists(candidate):
                img_folder = candidate
                break
                
    valid_exts = ('.png', '.jpg', '.jpeg', '.webp')
    if os.path.exists(img_folder):
        img_files = [f for f in os.listdir(img_folder) if f.lower().endswith(valid_exts)]
    else:
        img_files = []
        
    if not img_files:
        st.info("No gallery images found in the IMAGE directory.")
    else:
        gallery_html = """
        <style>
            .ipl-gallery {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                gap: 18px;
                padding: 10px 0;
            }
            .ipl-gallery-item {
                position: relative;
                border-radius: 14px;
                overflow: hidden;
                border: 1px solid rgba(255,255,255,0.08);
                box-shadow: 0 8px 25px rgba(0,0,0,0.5);
                transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
                height: 290px;
                background: #090e18;
            }
            .ipl-gallery-item:hover {
                transform: translateY(-5px);
                border-color: #f59e0b;
                box-shadow: 0 15px 35px rgba(245,158,11,0.3);
            }
            .ipl-gallery-img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: transform 0.4s ease, filter 0.4s ease;
            }
            .ipl-gallery-item:hover .ipl-gallery-img {
                transform: scale(1.05);
                filter: brightness(0.7);
            }
            .ipl-gallery-caption {
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                padding: 16px;
                background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 100%);
                color: #fff;
            }
            .ipl-caption-title {
                font-family: 'Outfit', sans-serif;
                font-size: 15px;
                font-weight: 800;
                color: #fef08a;
                margin: 0;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
        </style>
        <div class="ipl-gallery">
        """
        for img_name in sorted(img_files):
            img_p = os.path.join(img_folder, img_name)
            img_b64 = get_base64_image(img_p)
            if img_b64:
                title_clean = os.path.splitext(img_name)[0].replace('_', ' ').replace('-', ' ').title()
                gallery_html += f"""
                <div class="ipl-gallery-item">
                    <img class="ipl-gallery-img" src="{img_b64}">
                    <div class="ipl-gallery-caption">
                        <p class="ipl-caption-title">{title_clean}</p>
                    </div>
                </div>
                """
        gallery_html += "</div>"
        st.markdown(gallery_html, unsafe_allow_html=True)
'''

with open("/home/tejas/ipl/app.py", "w") as f:
    f.write(new_app_code)

print("Successfully wrote new app.py!")

