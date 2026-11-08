import streamlit as st
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
import re
import difflib
import json

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
    font-size: 13.5px !important;
    font-weight: 500 !important;
    color: #94a3b8 !important;
    padding: 10px 14px !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
    display: flex !important;
    align-items: center !important;
    min-height: 42px !important;
    height: 42px !important;
    box-sizing: border-box !important;
    margin-bottom: 2px !important;
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

/* Executive Stadium Metric Cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #0c1322 0%, #121c33 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    padding: 16px 18px !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4) !important;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease, box-shadow 0.25s ease !important;
    overflow: hidden !important;
    position: relative !important;
    min-height: 125px !important;
    height: 125px !important;
    max-height: 125px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    box-sizing: border-box !important;
}

[data-testid="stMetricLabel"] {
    min-height: 24px !important;
    display: flex !important;
    align-items: center !important;
}

[data-testid="stMetricValue"] {
    min-height: 44px !important;
    display: flex !important;
    align-items: center !important;
}

[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 4px; height: 100%;
    background: linear-gradient(180deg, #f59e0b, #d97706);
    opacity: 0.8;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-4px) !important;
    border-color: rgba(245, 158, 11, 0.5) !important;
    box-shadow: 0 18px 38px rgba(0, 0, 0, 0.65), 0 0 20px rgba(245, 158, 11, 0.2) !important;
}

[data-testid="stMetricLabel"] p {
    font-size: 12px !important;
    font-weight: 700 !important;
    color: #94a3b8 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

[data-testid="stMetricValue"] div {
    font-family: 'Teko', sans-serif !important;
    font-size: 38px !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
    line-height: 1.1 !important;
}

/* Tables & Dataframes */
[data-testid="stTable"], [data-testid="stDataFrame"] {
    background: #0d1424 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 14px !important;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
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
    grid-template-columns: repeat(auto-fit, minmax(135px, 1fr));
    gap: 14px;
    margin: 20px 0 30px 0;
    align-items: stretch;
}

.trophy-card {
    background: linear-gradient(145deg, #0d1527 0%, #111e38 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px;
    padding: 16px 12px;
    text-align: center;
    position: relative;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.35s ease, box-shadow 0.35s ease;
    overflow: hidden;
    height: 250px !important;
    min-height: 250px !important;
    max-height: 250px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    align-items: center !important;
    box-sizing: border-box !important;
}

.trophy-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #f59e0b, transparent);
    opacity: 0.5;
    transition: opacity 0.35s ease;
}

.trophy-card:hover::before {
    opacity: 1;
}

.trophy-card:hover {
    transform: translateY(-6px) scale(1.02);
    border-color: rgba(245, 158, 11, 0.6);
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7), 0 0 25px rgba(245, 158, 11, 0.3);
}

.trophy-count-pill {
    position: absolute;
    top: 14px;
    right: 14px;
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #0b0f19;
    font-weight: 800;
    font-size: 13px;
    padding: 3px 10px;
    border-radius: 20px;
    box-shadow: 0 3px 10px rgba(245, 158, 11, 0.4);
    letter-spacing: 0.5px;
    animation: trophyBadgePulse 3s infinite ease-in-out;
}

@keyframes trophyBadgePulse {
    0%, 100% { box-shadow: 0 3px 10px rgba(245, 158, 11, 0.4); }
    50% { box-shadow: 0 4px 18px rgba(245, 158, 11, 0.75); }
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
    width: 100%;
    max-width: 330px;
    min-height: 500px;
    height: auto;
    margin: 0 auto;
    background: linear-gradient(165deg, #182235 0%, #0c1220 50%, #070b14 100%);
    border-radius: 26px;
    padding: 22px 20px;
    border: 2px solid #f59e0b;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 25px rgba(245, 158, 11, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.3);
    color: #ffffff;
    font-family: 'Outfit', sans-serif;
    text-align: center;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.4s ease;
    overflow: hidden;
}

.fut-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 50% 30%, rgba(245, 158, 11, 0.15), transparent 60%);
    pointer-events: none;
    transition: opacity 0.4s ease;
}

/* Holographic dynamic light shimmer sweep */
.fut-card::after {
    content: '';
    position: absolute;
    top: -100%;
    left: -100%;
    width: 300%;
    height: 300%;
    background: linear-gradient(115deg, transparent 20%, rgba(255, 215, 0, 0.08) 35%, rgba(255, 255, 255, 0.22) 45%, transparent 60%);
    transform: rotate(25deg);
    transition: transform 0.75s ease;
    pointer-events: none;
}

.fut-card:hover::after {
    transform: rotate(25deg) translate(28%, 28%);
}

.fut-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 35px 80px rgba(0, 0, 0, 0.95), 0 0 40px rgba(245, 158, 11, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.5);
    border-color: #fbbf24;
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
    margin: 12px auto;
    border-radius: 50%;
    border: 3px solid #f59e0b;
    box-shadow: 0 0 25px rgba(245, 158, 11, 0.35), 0 10px 25px rgba(0, 0, 0, 0.7);
    overflow: hidden;
    background: #090e18;
    position: relative;
    z-index: 2;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.4s ease;
}

.fut-card:hover .fut-avatar-ring {
    transform: scale(1.04);
    box-shadow: 0 0 35px rgba(245, 158, 11, 0.6), 0 12px 30px rgba(0, 0, 0, 0.85);
    border-color: #fef08a;
}

.fut-avatar-ring img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    transition: transform 0.5s ease;
}

.fut-card:hover .fut-avatar-ring img {
    transform: scale(1.05);
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
    padding: 6px 4px;
    border-radius: 10px;
    transition: background 0.25s ease, transform 0.25s ease;
}

.fut-stat-box:hover {
    background: rgba(245, 158, 11, 0.15);
    transform: translateY(-2px);
}

.fut-stat-val {
    font-family: 'Teko', sans-serif;
    font-size: 26px;
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

/* Master Scorecard Dossier */
.scorecard-dossier {
    background: linear-gradient(145deg, #090f1d 0%, #111a30 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.scorecard-dossier:hover {
    border-color: rgba(245, 158, 11, 0.35);
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.75), 0 0 30px rgba(245, 158, 11, 0.15);
}

.scorecard-hero {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 16px;
    margin-bottom: 20px;
}

.milestone-badge-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
}

.milestone-tile {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 14px;
    padding: 14px 16px;
    text-align: center;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease, background 0.25s ease, box-shadow 0.25s ease;
}

.milestone-tile:hover {
    transform: translateY(-4px) scale(1.02);
    border-color: #f59e0b;
    background: rgba(245, 158, 11, 0.08);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.milestone-val {
    font-family: 'Teko', sans-serif;
    font-size: 32px;
    font-weight: 700;
    line-height: 1;
    color: #f8fafc;
}

.milestone-lbl {
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top: 4px;
}

.accolade-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: #fef08a;
    font-size: 12px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 20px;
    margin-right: 8px;
    margin-bottom: 8px;
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

/* Broadcast Cap & MVP Award Cards */
.award-card {
    background: linear-gradient(145deg, #0c1322 0%, #121d33 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.55);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease;
}

.award-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    transition: opacity 0.3s ease;
}

.award-card.orange::before {
    background: linear-gradient(90deg, #f97316, #f59e0b, #eab308);
}
.award-card.purple::before {
    background: linear-gradient(90deg, #8b5cf6, #a855f7, #d946ef);
}
.award-card.mvp::before {
    background: linear-gradient(90deg, #0ea5e9, #38bdf8, #06b6d4);
}

.award-card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.75), 0 0 30px rgba(245, 158, 11, 0.2);
}

.award-card.orange:hover {
    border-color: rgba(249, 115, 22, 0.5);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.75), 0 0 30px rgba(249, 115, 22, 0.3);
}
.award-card.purple:hover {
    border-color: rgba(168, 85, 247, 0.5);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.75), 0 0 30px rgba(168, 85, 247, 0.3);
}
.award-card.mvp:hover {
    border-color: rgba(56, 189, 248, 0.5);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.75), 0 0 30px rgba(56, 189, 248, 0.3);
}

.award-badge-ribbon {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
}

.award-avatar-ring {
    width: 105px;
    height: 105px;
    margin: 8px auto 14px auto;
    border-radius: 50%;
    overflow: hidden;
    background: #070b14;
    position: relative;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
    transition: transform 0.3s ease;
}

.award-card:hover .award-avatar-ring {
    transform: scale(1.06);
}

.award-avatar-ring img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
}

/* Top 50 Greatest Players - Hall of Fame Podium Cards */
.podium-card {
    background: linear-gradient(145deg, #0c1424 0%, #131e36 100%);
    border-radius: 22px;
    padding: 24px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease;
}

.podium-card.gold {
    border: 2px solid #f59e0b;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(245, 158, 11, 0.25);
}
.podium-card.silver {
    border: 2px solid #cbd5e1;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(203, 213, 225, 0.15);
}
.podium-card.bronze {
    border: 2px solid #d97706;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(217, 119, 6, 0.2);
}

.podium-card:hover {
    transform: translateY(-8px) scale(1.03);
}
.podium-card.gold:hover {
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(245, 158, 11, 0.45);
}
.podium-card.silver:hover {
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(203, 213, 225, 0.35);
}
.podium-card.bronze:hover {
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 35px rgba(217, 119, 6, 0.4);
}

.podium-rank-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 12px;
}

.podium-avatar-ring {
    width: 95px;
    height: 95px;
    margin: 8px auto 14px auto;
    border-radius: 50%;
    overflow: hidden;
    position: relative;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
    transition: transform 0.3s ease;
}

.podium-card:hover .podium-avatar-ring {
    transform: scale(1.06);
}

.podium-avatar-ring img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
}

/* All-Time Greatest IPL Playing XI - Broadcast Board */
.dream11-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 18px;
    margin: 25px 0 35px 0;
}

.dream11-player-card {
    background: linear-gradient(150deg, #0d1527 0%, #121c33 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 22px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.55);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
}

.dream11-player-card:hover {
    transform: translateY(-6px) scale(1.02);
    border-color: #f59e0b;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.75), 0 0 25px rgba(245, 158, 11, 0.25);
}

.dream11-squad-no {
    position: absolute;
    top: 14px;
    left: 14px;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #f8fafc;
    font-family: 'Teko', sans-serif;
    font-size: 18px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
}

.dream11-captain-tag {
    position: absolute;
    top: 14px;
    right: 14px;
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #0b0f19;
    font-weight: 900;
    font-size: 11px;
    letter-spacing: 1px;
    padding: 3px 9px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(245, 158, 11, 0.5);
    animation: trophyBadgePulse 3s infinite ease-in-out;
}

.dream11-avatar-ring {
    width: 95px;
    height: 95px;
    margin: 8px auto 12px auto;
    border-radius: 50%;
    overflow: hidden;
    border: 2px solid #f59e0b;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
    background: #080d18;
    transition: transform 0.3s ease;
}

.dream11-player-card:hover .dream11-avatar-ring {
    transform: scale(1.08);
}

.dream11-avatar-ring img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
}

/* ==========================================
   INTERACTIVE 3D FLIP ARCHITECTURE (10/10 SPRING PHYSICS)
   ========================================== */
.fifa-flip-toggle {
    display: none !important;
}

.fifa-flip-card-wrapper {
    perspective: 1400px;
    width: 100%;
    max-width: 335px;
    margin: 15px auto 25px auto;
}

.fifa-flip-box {
    display: block;
    width: 100%;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
}

.fifa-flip-inner {
    position: relative;
    width: 100%;
    min-height: 535px;
    height: 535px;
    transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    transform-style: preserve-3d;
    cursor: pointer;
}

.fifa-flip-toggle:checked + .fifa-flip-box .fifa-flip-inner {
    transform: rotateY(180deg);
}

.fifa-front, .fifa-back {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0; left: 0;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 26px;
    overflow: hidden;
    box-sizing: border-box;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85);
}

.fifa-front {
    transform: rotateY(0deg) translateZ(1px);
    z-index: 2;
}

.fifa-back {
    transform: rotateY(180deg) translateZ(1px);
    z-index: 1;
}

/* Ensure all child elements forward clicks cleanly to label */
.fifa-flip-inner *, .dream11-flip-inner * {
    pointer-events: none;
}

/* Card faces inside 3D Flip System */
.fifa-front.fut-card,
.fifa-back.tier-card {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
    height: 100% !important;
    min-height: 100% !important;
    border-radius: 26px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    cursor: pointer !important;
}

/* ==========================================
   THE FOUR TIERS CARD DESIGN SYSTEM (Image 1)
   ========================================== */
.tier-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 18px;
    margin: 25px 0 35px 0;
}

.tier-card {
    position: relative;
    width: 100%;
    max-width: 275px;
    min-height: 480px;
    height: 480px;
    border-radius: 20px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.7);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease;
    font-family: 'Outfit', sans-serif;
    margin: 0 auto;
    cursor: pointer;
}

.tier-card:hover {
    transform: translateY(-8px) scale(1.02);
}

/* Tier Specific Themes */
/* 1. STANDARD */
.tier-card.tier-standard {
    border: 2px solid #64748b;
    background: #1e293b;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(100, 116, 139, 0.25);
}
.tier-card.tier-standard .tier-header-strip {
    background: linear-gradient(90deg, #334155, #64748b, #334155);
    color: #cbd5e1;
}
.tier-card.tier-standard .tier-lower-body {
    background: linear-gradient(180deg, #1e3a5f 0%, #0f172a 100%);
}
.tier-card.tier-standard .tier-bottom-strip {
    background: #3b82f6;
    color: #ffffff;
}

/* 2. RARE */
.tier-card.tier-rare {
    border: 2px solid #cbd5e1;
    background: #0f172a;
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.7), 0 0 25px rgba(203, 213, 225, 0.3);
}
.tier-card.tier-rare .tier-header-strip {
    background: linear-gradient(90deg, #94a3b8, #f1f5f9, #94a3b8);
    color: #0f172a;
}
.tier-card.tier-rare .tier-lower-body {
    background: linear-gradient(180deg, #1c2419 0%, #0d130e 100%);
}
.tier-card.tier-rare .tier-bottom-strip {
    background: #eab308;
    color: #0f172a;
}

/* 3. EPIC */
.tier-card.tier-epic {
    border: 2px solid #a855f7;
    background: #180928;
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(168, 85, 247, 0.4);
}
.tier-card.tier-epic .tier-header-strip {
    background: linear-gradient(90deg, #7e22ce, #c084fc, #7e22ce);
    color: #ffffff;
}
.tier-card.tier-epic .tier-lower-body {
    background: linear-gradient(180deg, #4c0519 0%, #1a0208 100%);
}
.tier-card.tier-epic .tier-bottom-strip {
    background: #e11d48;
    color: #ffffff;
}

/* 4. ICON */
.tier-card.tier-icon {
    border: 2px solid #f59e0b;
    background: #1a1202;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 35px rgba(245, 158, 11, 0.45);
}
.tier-card.tier-icon .tier-header-strip {
    background: linear-gradient(90deg, #b45309, #fde047, #b45309);
    color: #0b0f19;
}
.tier-card.tier-icon .tier-lower-body {
    background: linear-gradient(180deg, #580c1f 0%, #20040b 100%);
}
.tier-card.tier-icon .tier-bottom-strip {
    background: linear-gradient(90deg, #b91c1c, #dc2626);
    color: #ffffff;
}

/* Internal Card Components for 4 Tiers */
.tier-header-strip {
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    text-align: center;
    padding: 7px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.4);
}

.tier-upper-body {
    background: #f5f0e8;
    color: #0f172a;
    padding: 14px 16px 18px 16px;
    clip-path: polygon(0 0, 100% 0, 100% 90%, 0 100%);
    position: relative;
    z-index: 2;
}

.tier-upper-player {
    font-size: 17px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    line-height: 1.1;
    color: #0f172a;
}

.tier-upper-team {
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #64748b;
    margin-top: 3px;
}

.tier-lower-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 10px 16px;
    position: relative;
    text-align: center;
    overflow: hidden;
}

.tier-watermark-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 110px;
    opacity: 0.08;
    pointer-events: none;
    user-select: none;
}

.tier-big-num {
    font-family: 'Teko', sans-serif;
    font-size: 80px;
    font-weight: 700;
    line-height: 0.85;
    color: #ffffff;
    text-shadow: 0 3px 12px rgba(0, 0, 0, 0.7);
    position: relative;
    z-index: 2;
}

.tier-card.tier-icon .tier-big-num {
    color: #fbbf24;
    text-shadow: 0 0 20px rgba(245, 158, 11, 0.5);
}

.tier-metric-label {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #94a3b8;
    text-transform: uppercase;
    margin-top: 2px;
}

.tier-sub-stats {
    font-size: 11px;
    font-weight: 700;
    color: #cbd5e1;
    letter-spacing: 0.8px;
    margin-top: 6px;
}

.tier-role-pill {
    background: rgba(0, 0, 0, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #f8fafc;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 12px;
    margin-top: 10px;
}

.tier-bottom-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 18px;
    font-family: 'Teko', sans-serif;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* Playing XI 3D Flip System */
.dream11-flip-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 20px;
    margin: 25px 0 35px 0;
}

.dream11-flip-box {
    perspective: 1400px;
    width: 100%;
    height: 480px;
    margin: 0 auto;
    display: block;
    cursor: pointer;
    user-select: none;
}

.dream11-flip-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.85s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.6s ease;
    transform-style: preserve-3d;
    cursor: pointer;
}

.flip-checkbox-input:checked + .dream11-flip-box .dream11-flip-inner,
.dream11-flip-box.is-flipped .dream11-flip-inner {
    transform: rotateY(180deg);
}

.dream11-face {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0; left: 0;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 20px;
    overflow: hidden;
    box-sizing: border-box;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.75);
}

.dream11-front {
    transform: rotateY(0deg) translateZ(1px);
    z-index: 2;
}

.dream11-back {
    transform: rotateY(180deg) translateZ(1px);
    z-index: 1;
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


def render_html(html_str):
    """Renders raw HTML safely in Streamlit without triggering Markdown indented code block (<pre><code>) conversion."""
    lines = [line.strip() for line in html_str.split("\n") if line.strip()]
    st.markdown("\n".join(lines), unsafe_allow_html=True)


# ==========================================
# 🖼️ BULLETPROOF MULTI-TIER IMAGE ENGINE
# ==========================================
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

# User's Curated High-Res Wallpapers & Photos
LOCAL_PLAYER_IMAGES = {
    'V Kohli': get_base64_image('/home/tejas/ipl/IMAGE /18.jpeg') or get_base64_image('/home/tejas/ipl/V_Kohli.jpg'),
    'MS Dhoni': get_base64_image('/home/tejas/ipl/IMAGE /2026 Chennai IPL MSD WALLPAPER.jpeg') or get_base64_image('/home/tejas/ipl/MS_Dhoni.jpg'),
    'RG Sharma': get_base64_image('/home/tejas/ipl/IMAGE /Wallpaper ❤️12000 T20 runs for Rohit Sharma.jpeg') or get_base64_image('/home/tejas/ipl/RG_Sharma.jpg'),
    'B Kumar': get_base64_image('/home/tejas/ipl/IMAGE /Bhuvi♥️.jpeg'),
    'HH Pandya': get_base64_image('/home/tejas/ipl/IMAGE /hardik pandya wallpaper hd Mumbai Indians.jpeg'),
    'KL Rahul': get_base64_image('/home/tejas/ipl/IMAGE /Man of the moment KL Rahul 🙌🏻💙❤️.jpeg'),
    'RR Pant': get_base64_image('/home/tejas/ipl/IMAGE /Rishabh Pant.jpeg'),
    'Shubman Gill': get_base64_image('/home/tejas/ipl/IMAGE /Shubhman gill wallpaper 📍.jpeg'),
    'V Suryavanshi': get_base64_image('/home/tejas/ipl/IMAGE /vebhav Suryavanshi.jpeg')
}

# Verified Local IPL Brand Logo
IPL_LOGO_BASE64 = get_base64_image('/home/tejas/ipl/ipl_logo.png')

OFFICIAL_TEAM_LOGOS = {
    "Mumbai Indians": "https://thumb.wikimedia.org/wikipedia/en/thumb/c/cd/Mumbai_Indians_Logo.svg/330px-Mumbai_Indians_Logo.svg.png",
    "Chennai Super Kings": "https://thumb.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/330px-Chennai_Super_Kings_Logo.svg.png",
    "Kolkata Knight Riders": "https://thumb.wikimedia.org/wikipedia/en/thumb/4/4c/Kolkata_Knight_Riders_Logo.svg/330px-Kolkata_Knight_Riders_Logo.svg.png",
    "Royal Challengers Bengaluru": "https://thumb.wikimedia.org/wikipedia/en/thumb/d/d4/Royal_Challengers_Bengaluru_Logo.svg/330px-Royal_Challengers_Bengaluru_Logo.svg.png",
    "Royal Challengers Bangalore": "https://thumb.wikimedia.org/wikipedia/en/thumb/d/d4/Royal_Challengers_Bengaluru_Logo.svg/330px-Royal_Challengers_Bengaluru_Logo.svg.png",
    "Delhi Capitals": "https://thumb.wikimedia.org/wikipedia/en/thumb/2/2f/Delhi_Capitals.svg/330px-Delhi_Capitals.svg.png",
    "Delhi Daredevils": "https://thumb.wikimedia.org/wikipedia/en/thumb/2/2f/Delhi_Capitals.svg/330px-Delhi_Capitals.svg.png",
    "Rajasthan Royals": "https://thumb.wikimedia.org/wikipedia/en/thumb/5/5c/This_is_the_logo_for_Rajasthan_Royals%2C_a_cricket_team_playing_in_the_Indian_Premier_League_%28IPL%29.svg/330px-This_is_the_logo_for_Rajasthan_Royals%2C_a_cricket_team_playing_in_the_Indian_Premier_League_%28IPL%29.svg.png",
    "Sunrisers Hyderabad": "https://thumb.wikimedia.org/wikipedia/en/thumb/5/51/Sunrisers_Hyderabad_Logo.svg/330px-Sunrisers_Hyderabad_Logo.svg.png",
    "Deccan Chargers": get_base64_image('/home/tejas/ipl/deccan_chargers.png') or "https://upload.wikimedia.org/wikipedia/en/a/a6/HyderabadDeccanChargers.png",
    "Gujarat Titans": "https://thumb.wikimedia.org/wikipedia/en/thumb/0/09/Gujarat_Titans_Logo.svg/330px-Gujarat_Titans_Logo.svg.png",
    "Punjab Kings": "https://thumb.wikimedia.org/wikipedia/en/thumb/d/d4/Punjab_Kings_Logo.svg/330px-Punjab_Kings_Logo.svg.png",
    "Kings XI Punjab": "https://thumb.wikimedia.org/wikipedia/en/thumb/d/d4/Punjab_Kings_Logo.svg/330px-Punjab_Kings_Logo.svg.png",
    "Lucknow Super Giants": "https://thumb.wikimedia.org/wikipedia/en/thumb/3/34/Lucknow_Super_Giants_Logo.svg/330px-Lucknow_Super_Giants_Logo.svg.png",
    "Rising Pune Supergiant": "https://upload.wikimedia.org/wikipedia/en/9/9a/Rising_Pune_Supergiant.png",
    "Rising Pune Supergiants": "https://upload.wikimedia.org/wikipedia/en/9/9a/Rising_Pune_Supergiant.png",
    "Gujarat Lions": "https://upload.wikimedia.org/wikipedia/en/c/c4/Gujarat_Lions.png",
    "Pune Warriors India": "https://thumb.wikimedia.org/wikipedia/en/thumb/4/4a/Pune_Warriors_India_IPL_Logo.png/330px-Pune_Warriors_India_IPL_Logo.png",
    "Kochi Tuskers Kerala": "https://thumb.wikimedia.org/wikipedia/en/thumb/9/96/Kochi_Tuskers_Kerala_Logo.svg/330px-Kochi_Tuskers_Kerala_Logo.svg.png",
}

PLAYER_WIKI_MAP = {
    'V Kohli': 'Virat_Kohli',
    'MS Dhoni': 'MS_Dhoni',
    'RG Sharma': 'Rohit_Sharma',
    'AB de Villiers': 'AB_de_Villiers',
    'DA Warner': 'David_Warner_(cricketer)',
    'CH Gayle': 'Chris_Gayle',
    'SK Raina': 'Suresh_Raina',
    'JJ Bumrah': 'Jasprit_Bumrah',
    'SP Narine': 'Sunil_Narine',
    'Rashid Khan': 'Rashid_Khan_(cricketer)',
    'AD Russell': 'Andre_Russell',
    'KL Rahul': 'KL_Rahul',
    'RR Pant': 'Rishabh_Pant',
    'HH Pandya': 'Hardik_Pandya',
    'RA Jadeja': 'Ravindra_Jadeja',
    'B Kumar': 'Bhuvneshwar_Kumar',
    'YS Chahal': 'Yuzvendra_Chahal',
    'Shubman Gill': 'Shubman_Gill',
    'SV Samson': 'Sanju_Samson',
    'SA Yadav': 'Suryakumar_Yadav',
    'SS Iyer': 'Shreyas_Iyer',
    'KD Karthik': 'Dinesh_Karthik',
    'F du Plessis': 'Faf_du_Plessis',
    'GJ Maxwell': 'Glenn_Maxwell',
    'SL Malinga': 'Lasith_Malinga',
    'DJ Bravo': 'Dwayne_Bravo',
    'KA Pollard': 'Kieron_Pollard',
    'S Dhawan': 'Shikhar_Dhawan',
    'Yuvraj Singh': 'Yuvraj_Singh',
    'G Gambhir': 'Gautam_Gambhir',
    'Harbhajan Singh': 'Harbhajan_Singh',
    'R Ashwin': 'Ravichandran_Ashwin',
    'Mohammed Shami': 'Mohammed_Shami',
    'Mohammed Siraj': 'Mohammed_Siraj',
    'Arshdeep Singh': 'Arshdeep_Singh',
    'Kuldeep Yadav': 'Kuldeep_Yadav',
    'CV Varun': 'Varun_Chakravarthy',
    'Ruturaj Gaikwad': 'Ruturaj_Gaikwad',
    'YBK Jaiswal': 'Yashasvi_Jaiswal',
    'Rinku Singh': 'Rinku_Singh',
    'Tilak Varma': 'Tilak_Varma',
    'Shivam Dube': 'Shivam_Dube',
    'H Klaasen': 'Heinrich_Klaasen',
    'DA Miller': 'David_Miller_(cricketer,_born_1989)',
    'Q de Kock': 'Quinton_de_Kock',
    'JC Buttler': 'Jos_Buttler',
    'TA Boult': 'Trent_Boult',
    'K Rabada': 'Kagiso_Rabada',
    'HV Patel': 'Harshal_Patel',
    'R Bishnoi': 'Ravi_Bishnoi',
    'PP Chawla': 'Piyush_Chawla',
    'A Mishra': 'Amit_Mishra',
    'SR Watson': 'Shane_Watson',
    'BB McCullum': 'Brendon_McCullum',
    'MK Pandey': 'Manish_Pandey',
    'AT Rayudu': 'Ambati_Rayudu',
    'V Sehwag': 'Virender_Sehwag',
    'PA Patel': 'Parthiv_Patel',
    'M Vijay': 'Murali_Vijay',
    'UT Yadav': 'Umesh_Yadav',
    'Ishan Kishan': 'Ishan_Kishan',
    'Sandeep Sharma': 'Sandeep_Sharma',
    'Mohit Sharma': 'Mohit_Sharma_(cricketer,_born_1991)',
    'Deepak Chahar': 'Deepak_Chahar',
    'Rahul Chahar': 'Rahul_Chahar',
    'T Natarajan': 'T._Natarajan',
    'Umran Malik': 'Umran_Malik',
    'Avesh Khan': 'Avesh_Khan',
    'Prasidh Krishna': 'Prasidh_Krishna',
    'Krunal Pandya': 'Krunal_Pandya',
    'Axar Patel': 'Axar_Patel',
    'Washington Sundar': 'Washington_Sundar',
    'Nitish Rana': 'Nitish_Rana',
    'Venkatesh Iyer': 'Venkatesh_Iyer',
    'Abhishek Sharma': 'Abhishek_Sharma_(cricketer,_born_2000)',
    'Travis Head': 'Travis_Head',
    'Mitchell Marsh': 'Mitchell_Marsh',
    'Marcus Stoinis': 'Marcus_Stoinis',
    'Nicholas Pooran': 'Nicholas_Pooran',
    'Sam Curran': 'Sam_Curran',
    'Liam Livingstone': 'Liam_Livingstone',
    'Phil Salt': 'Phil_Salt_(cricketer)',
    'Rajat Patidar': 'Rajat_Patidar',
    'Rahul Tripathi': 'Rahul_Tripathi',
    'Jitesh Sharma': 'Jitesh_Sharma',
    'Prithvi Shaw': 'Prithvi_Shaw',
    'Mayank Agarwal': 'Mayank_Agarwal',
    'Devdutt Padikkal': 'Devdutt_Padikkal',
    'Ajinkya Rahane': 'Ajinkya_Rahane',
    'WP Saha': 'Wriddhiman_Saha'
}

PLAYER_OFFICIAL_ROLES = {
    # Top-Order & Openers
    'V Kohli': 'TOP-ORDER ANCHOR & OPENER',
    'RG Sharma': 'OPENER & AGGRESSIVE STROKEMAKER',
    'Shubman Gill': 'OPENER & CLASSICAL STROKEMAKER',
    'DA Warner': 'EXPLOSIVE TOP-ORDER OPENER',
    'CH Gayle': 'UNIVERSE BOSS / POWER OPENER',
    'F du Plessis': 'TOP-ORDER AGGRESSIVE OPENER',
    'S Dhawan': 'TOP-ORDER PROLIFIC OPENER',
    'Ruturaj Gaikwad': 'OPENER & ANCHOR',
    'YBK Jaiswal': 'FEARLESS ATTACKING OPENER',
    'G Gambhir': 'TOP-ORDER FIGHTER & ANCHOR',
    'V Sehwag': 'DESTRUCTIVE POWER OPENER',
    'BB McCullum': 'ULTRA-AGGRESSIVE OPENER',
    'M Vijay': 'TOP-ORDER CLASSICAL OPENER',
    'V Suryavanshi': 'YOUTH PRODIGY / TOP-ORDER BATTER',
    'Abhishek Sharma': 'EXPLOSIVE POWERPLAY OPENER',
    'Travis Head': 'HEADACHE / ULTRA-POWER OPENER',
    'Prithvi Shaw': 'POWERPLAY ATTACKING OPENER',
    'Devdutt Padikkal': 'TOP-ORDER STROKEMAKER',
    'Mayank Agarwal': 'AGGRESSIVE TOP-ORDER BATTER',
    'Ajinkya Rahane': 'TOP-ORDER STABILIZER & ANCHOR',
    
    # Wicketkeeper-Batters & Finishers
    'MS Dhoni': 'WK-LEGENDARY FINISHER & CAPTAIN',
    'RR Pant': 'WK-MIDDLE ORDER / GAME CHANGER',
    'KL Rahul': 'WK-TOP ORDER / ANCHOR',
    'SV Samson': 'WK-TOP ORDER / STROKEMAKER',
    'KD Karthik': 'WK-DEATH OVERS FINISHER',
    'Q de Kock': 'WK-EXPLOSIVE TOP-ORDER BATTER',
    'JC Buttler': 'WK-OPENER / MATCH-WINNER',
    'H Klaasen': 'WK-DESTRUCTIVE MIDDLE FINISHER',
    'Nicholas Pooran': 'WK-POWER HITTER & FINISHER',
    'Ishan Kishan': 'WK-OPENER / POCKET DYNAMO',
    'WP Saha': 'WK-SPECIALIST & POWERPLAY HITTER',
    'PA Patel': 'WK-PINCH OPENER',
    'Jitesh Sharma': 'WK-LOWER ORDER FINISHER',
    'Phil Salt': 'WK-AGGRESSIVE POWERPLAY OPENER',
    
    # Middle-Order Batters & Finishers
    'AB de Villiers': 'MR. 360° / GENIUS MIDDLE-ORDER',
    'SK Raina': 'MR. IPL / MIDDLE-ORDER MAESTRO',
    'SA Yadav': '360° MIDDLE-ORDER DYNAMO',
    'SS Iyer': 'MIDDLE-ORDER ANCHOR & CAPTAIN',
    'Tilak Varma': 'MIDDLE-ORDER STABILIZER',
    'MK Pandey': 'MIDDLE-ORDER STROKEMAKER',
    'AT Rayudu': 'VERSATILE MIDDLE-ORDER BATTER',
    'Rinku Singh': 'DESIGNATED CLUTCH FINISHER',
    'DA Miller': 'KILLER MILLER / CLUTCH FINISHER',
    'Rajat Patidar': 'MIDDLE-ORDER SPIN DESTROYER',
    'Rahul Tripathi': 'INTENT-DRIVEN TOP/MIDDLE BATTER',
    'Nitish Rana': 'ATTACKING MIDDLE-ORDER BATTER',
    'Shimron Hetmyer': 'DEATH OVERS POWER FINISHER',
    'Rahul Tewatia': 'ICEMAN CLUTCH FINISHER',
    
    # All-Rounders (Pace & Spin)
    'A Flintoff': 'FAST-BOWLING ALL-ROUNDER & HARD HITTER',
    'Andrew Flintoff': 'FAST-BOWLING ALL-ROUNDER & HARD HITTER',
    'A Symonds': 'POWER-HITTING ALL-ROUNDER & OFF-SPIN',
    'JH Kallis': 'LEGENDARY BATTING ALL-ROUNDER',
    'AC Gilchrist': 'WK-LEGENDARY POWERPLAY OPENER & CAPTAIN',
    'ML Hayden': 'FEARLESS POWERPLAY OPENER',
    'B Lee': '150+ KM/H EXPRESS FAST BOWLER',
    'SK Warne': 'LEGENDARY LEG-SPINNER & CAPTAIN',
    'M Muralitharan': 'LEGENDARY OFF-SPIN WIZARD',
    'KC Sangakkara': 'WK-CLASSICAL TOP-ORDER BATTER',
    'DPMD Jayawardene': 'CLASSICAL MIDDLE-ORDER MASTER',
    'ST Jayasuriya': 'MATARA MARAUDER / POWER OPENER & SPINNER',
    'DW Steyn': 'EXPRESS OUTSWING SPEEDSTER',
    'SE Marsh': 'INAUGURAL ORANGE CAP / TOP-ORDER ANCHOR',
    'MEK Hussey': 'MR. CRICKET / TOP-ORDER MASTER',
    'Sohail Tanvir': 'INAUGURAL PURPLE CAP / LEFT-ARM PACER',
    'Shahid Afridi': 'BOOM BOOM / LEG-SPIN ALL-ROUNDER',
    'Shoaib Akhtar': 'RAWALPINDI EXPRESS / FAST BOWLER',
    'Kamran Akmal': 'WK-OPENER / AGGRESSIVE STROKEMAKER',
    'KP Pietersen': 'EXPLOSIVE TOP/MIDDLE-ORDER BATTER',
    'JA Morkel': 'POWER HITTER & SEAM ALL-ROUNDER',
    'CH Morris': 'DEATH OVERS YORKER & POWER FINISHER',
    'RN ten Doeschate': 'BATTING ALL-ROUNDER',
    'HH Pandya': 'FAST-BOWLING ALL-ROUNDER & FINISHER',
    'RA Jadeja': 'SPIN-BOWLING ALL-ROUNDER & FINISHER',
    'AD Russell': 'DESTRUCTIVE POWER FINISHER & PACER',
    'SP Narine': 'MYSTERY SPINNER & PINCH OPENER',
    'GJ Maxwell': 'SPIN ALL-ROUNDER / 360° HITTER',
    'DJ Bravo': 'DEATH-OVERS PACER & ALL-ROUNDER',
    'KA Pollard': 'GIANT FINISHER & MEDIUM PACER',
    'SR Watson': 'SEAM-BOWLING POWER ALL-ROUNDER',
    'Yuvraj Singh': 'MIDDLE-ORDER ICON & SLOW LEFT-ARM',
    'Axar Patel': 'SPIN-BOWLING ALL-ROUNDER',
    'Marcus Stoinis': 'POWER ALL-ROUNDER & FINISHER',
    'Sam Curran': 'SEAM-BOWLING ALL-ROUNDER',
    'Shivam Dube': 'SPIN SMASHER & MEDIUM PACER',
    'Washington Sundar': 'OFF-SPIN ALL-ROUNDER',
    'Krunal Pandya': 'SPIN ALL-ROUNDER',
    'Mitchell Marsh': 'SEAM-BOWLING POWER ALL-ROUNDER',
    'Venkatesh Iyer': 'TOP-ORDER BATTER & SEAM ALL-ROUNDER',
    'Liam Livingstone': 'POWER HITTER & DUAL-SPIN ALL-ROUNDER',
    
    # Fast Bowlers (Pacers)
    'JJ Bumrah': 'FAST BOWLER / YORKER SPEARHEAD',
    'B Kumar': 'FAST BOWLER / SWING KING',
    'SL Malinga': 'LEGENDARY YORKER KING / PACER',
    'Mohammed Shami': 'SEAM SPEARHEAD & WICKET TAKER',
    'Mohammed Siraj': 'AGGRESSIVE SEAM & SWING PACER',
    'Arshdeep Singh': 'LEFT-ARM DEATH OVERS PACER',
    'TA Boult': 'LEFT-ARM POWERPLAY SWING PACER',
    'K Rabada': 'EXPRESS FAST BOWLER',
    'HV Patel': 'SLOWER-BALL & DEATH SPECIALIST',
    'Mitchell Starc': 'LEFT-ARM EXPRESS PACER',
    'UT Yadav': 'EXPRESS OUTSWING PACER',
    'Sandeep Sharma': 'SWING & DEATH VARIATIONS PACER',
    'Mohit Sharma': 'KNUCKLE-BALL & BACK-OF-HAND PACER',
    'Deepak Chahar': 'POWERPLAY INSWING PACER',
    'T Natarajan': 'YORKER SPECIALIST PACER',
    'Umran Malik': '150+ KM/H EXPRESS PACER',
    'Avesh Khan': 'HIT-THE-DECK EXPRESS PACER',
    'Prasidh Krishna': 'HIGH-BOUNCE EXPRESS PACER',
    
    # Spinners
    'YS Chahal': 'LEG-SPIN WIZARD & ALL-TIME LEADER',
    'Rashid Khan': 'AFGHAN T20 LEG-SPIN PHENOM',
    'Kuldeep Yadav': 'LEFT-ARM CHINAMAN WRIST SPINNER',
    'CV Varun': 'MYSTERY CARROM-BALL SPINNER',
    'R Ashwin': 'TACTICAL OFF-SPINNER / CARROM BALL',
    'Harbhajan Singh': 'TURBANATOR / OFF-SPIN TITAN',
    'R Bishnoi': 'FAST-ARM ACTION GOOGLY SPINNER',
    'A Mishra': 'CLASSICAL LEG-BREAK SPINNER',
    'PP Chawla': 'VETERAN LEG-BREAK BOWLER',
    'Rahul Chahar': 'QUICK-ARM LEG-SPINNER'
}

def get_player_role(player, b_df, bowl_df, deliveries_df):
    if player in PLAYER_OFFICIAL_ROLES:
        return PLAYER_OFFICIAL_ROLES[player]
        
    stumpings = deliveries_df[(deliveries_df['fielder'] == player) & (deliveries_df['dismissal_kind'] == 'stumped')].shape[0]
    first_balls = b_df.groupby('match_id')['over'].min()
    avg_entry_over = first_balls.mean() if not first_balls.empty else 20.0
    
    balls_faced = len(b_df)
    runs = b_df['batsman_runs'].sum()
    balls_bowled = len(bowl_df)
    w_df = bowl_df.dropna(subset=['player_dismissed'])
    wickets = w_df[w_df['dismissal_kind'] != 'run out'].shape[0]
    
    if stumpings >= 1:
        if avg_entry_over <= 4.0: return "WK-OPENER / TOP-ORDER BATTER"
        elif avg_entry_over >= 11.0: return "WK-FINISHER & MIDDLE-ORDER"
        else: return "WICKETKEEPER-BATTER"
        
    if balls_bowled >= 150 and balls_faced >= 150 and runs >= 400 and wickets >= 15:
        return "ALL-ROUNDER"
        
    if balls_bowled >= balls_faced * 1.5 or wickets >= 20 or (balls_bowled >= 120 and balls_faced < 100):
        return "SPECIALIST BOWLER"
        
    if avg_entry_over <= 3.5:
        return "TOP-ORDER BATTER / OPENER"
    elif avg_entry_over <= 11.5:
        return "MIDDLE-ORDER BATTER"
    else:
        return "FINISHER / POWER HITTER"

def get_player_country_flag(player):
    # Comprehensive Verified Country & Flag Registry for all Overseas IPL Players (2008 - 2026)
    overseas_map = {
        # 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENGLAND (ENG)
        'A Flintoff': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Andrew Flintoff': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'KP Pietersen': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Kevin Pietersen': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'BA Stokes': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Ben Stokes': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'JC Buttler': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Jos Buttler': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'J Archer': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'JC Archer': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Jofra Archer': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'SM Curran': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Sam Curran': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'MM Ali': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Moeen Ali': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'LS Livingstone': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Liam Livingstone': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'EJG Morgan': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Eoin Morgan': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'JM Bairstow': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Jonny Bairstow': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'HC Brook': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Harry Brook': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'CR Woakes': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Chris Woakes': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'CJ Jordan': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Chris Jordan': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'MA Wood': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Mark Wood': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'JJ Roy': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Jason Roy': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'AD Hales': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Alex Hales': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'LJ Wright': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Luke Wright': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'PD Collingwood': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Paul Collingwood': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'AD Mascarenhas': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Dimitri Mascarenhas': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'OA Shah': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Owais Shah': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'RS Bopara': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Ravi Bopara': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'GR Napier': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Graham Napier': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'MJ Lumb': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Michael Lumb': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'SR Patel': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Samit Patel': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'DJ Willey': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'David Willey': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'TS Mills': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Tymal Mills': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'RJW Topley': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Reece Topley': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'TK Curran': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Tom Curran': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'WG Jacks': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Will Jacks': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'PD Salt': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Phil Salt': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'T Banton': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Tom Banton': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'DJ Malan': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Dawid Malan': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'GHS Garton': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'George Garton': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'RJ Gleeson': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Richard Gleeson': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'L Wood': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Luke Wood': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'AU Rashid': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Adil Rashid': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'JE Root': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Joe Root': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'J Overton': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Jamie Overton': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'T Kohler-Cadmore': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Tom Kohler-Cadmore': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'JW Dernbach': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Jade Dernbach': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'LE Plunkett': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Liam Plunkett': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'MH Yardy': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Michael Yardy': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'SCJ Broad': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Stuart Broad': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'IR Bell': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Ian Bell': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',
        'Gus Atkinson': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG', 'Brydon Carse': '🏴󠁧󠁢󠁥󠁮󠁧󠁿 ENG',

        # 🇦🇺 AUSTRALIA (AUS)
        'DA Warner': '🇦🇺 AUS', 'David Warner': '🇦🇺 AUS', 'GJ Maxwell': '🇦🇺 AUS', 'Glenn Maxwell': '🇦🇺 AUS',
        'SPD Smith': '🇦🇺 AUS', 'Steve Smith': '🇦🇺 AUS', 'PJ Cummins': '🇦🇺 AUS', 'Pat Cummins': '🇦🇺 AUS',
        'MA Starc': '🇦🇺 AUS', 'Mitchell Starc': '🇦🇺 AUS', 'MP Stoinis': '🇦🇺 AUS', 'Marcus Stoinis': '🇦🇺 AUS',
        'TM Head': '🇦🇺 AUS', 'Travis Head': '🇦🇺 AUS', 'SR Watson': '🇦🇺 AUS', 'Shane Watson': '🇦🇺 AUS',
        'AC Gilchrist': '🇦🇺 AUS', 'Adam Gilchrist': '🇦🇺 AUS', 'RT Ponting': '🇦🇺 AUS', 'Ricky Ponting': '🇦🇺 AUS',
        'ML Hayden': '🇦🇺 AUS', 'Matthew Hayden': '🇦🇺 AUS', 'B Lee': '🇦🇺 AUS', 'Brett Lee': '🇦🇺 AUS',
        'MEK Hussey': '🇦🇺 AUS', 'Michael Hussey': '🇦🇺 AUS', 'Mike Hussey': '🇦🇺 AUS', 'DJ Hussey': '🇦🇺 AUS', 'David Hussey': '🇦🇺 AUS',
        'SE Marsh': '🇦🇺 AUS', 'Shaun Marsh': '🇦🇺 AUS', 'MG Johnson': '🇦🇺 AUS', 'Mitchell Johnson': '🇦🇺 AUS',
        'AJ Finch': '🇦🇺 AUS', 'Aaron Finch': '🇦🇺 AUS', 'CA Lynn': '🇦🇺 AUS', 'Chris Lynn': '🇦🇺 AUS',
        'MR Marsh': '🇦🇺 AUS', 'Mitchell Marsh': '🇦🇺 AUS', 'JR Hazlewood': '🇦🇺 AUS', 'Josh Hazlewood': '🇦🇺 AUS',
        'NM Coulter-Nile': '🇦🇺 AUS', 'Nathan Coulter-Nile': '🇦🇺 AUS', 'JP Faulkner': '🇦🇺 AUS', 'James Faulkner': '🇦🇺 AUS',
        'A Symonds': '🇦🇺 AUS', 'Andrew Symonds': '🇦🇺 AUS', 'BJ Hodge': '🇦🇺 AUS', 'Brad Hodge': '🇦🇺 AUS',
        'GB Hogg': '🇦🇺 AUS', 'Brad Hogg': '🇦🇺 AUS', 'SK Warne': '🇦🇺 AUS', 'Shane Warne': '🇦🇺 AUS',
        'CL White': '🇦🇺 AUS', 'Cameron White': '🇦🇺 AUS', 'MC Henriques': '🇦🇺 AUS', 'Moises Henriques': '🇦🇺 AUS',
        'GJ Bailey': '🇦🇺 AUS', 'George Bailey': '🇦🇺 AUS', 'DT Christian': '🇦🇺 AUS', 'Dan Christian': '🇦🇺 AUS', 'Daniel Christian': '🇦🇺 AUS',
        'DP Nannes': '🇦🇺 AUS', 'Dirk Nannes': '🇦🇺 AUS', 'JP Behrendorff': '🇦🇺 AUS', 'Jason Behrendorff': '🇦🇺 AUS',
        'JA Richardson': '🇦🇺 AUS', 'Jhye Richardson': '🇦🇺 AUS', 'KW Richardson': '🇦🇺 AUS', 'Kane Richardson': '🇦🇺 AUS',
        'RP Meredith': '🇦🇺 AUS', 'Riley Meredith': '🇦🇺 AUS', 'DR Sams': '🇦🇺 AUS', 'Daniel Sams': '🇦🇺 AUS',
        'NW Ellis': '🇦🇺 AUS', 'Nathan Ellis': '🇦🇺 AUS', 'TH David': '🇦🇺 AUS', 'Tim David': '🇦🇺 AUS',
        'MS Wade': '🇦🇺 AUS', 'Matthew Wade': '🇦🇺 AUS', 'C Green': '🇦🇺 AUS', 'Cameron Green': '🇦🇺 AUS',
        'SH Johnson': '🇦🇺 AUS', 'Spencer Johnson': '🇦🇺 AUS', 'J Fraser-McGurk': '🇦🇺 AUS', 'Jake Fraser-McGurk': '🇦🇺 AUS',
        'BCJ Cutting': '🇦🇺 AUS', 'Ben Cutting': '🇦🇺 AUS', 'SW Tait': '🇦🇺 AUS', 'Shaun Tait': '🇦🇺 AUS',
        'JL Pattinson': '🇦🇺 AUS', 'James Pattinson': '🇦🇺 AUS', 'DE Bollinger': '🇦🇺 AUS', 'Doug Bollinger': '🇦🇺 AUS',
        'BW Hilfenhaus': '🇦🇺 AUS', 'Ben Hilfenhaus': '🇦🇺 AUS', 'PM Siddle': '🇦🇺 AUS', 'Peter Siddle': '🇦🇺 AUS',
        'CJ McKay': '🇦🇺 AUS', 'Clint McKay': '🇦🇺 AUS', 'JW Hastings': '🇦🇺 AUS', 'John Hastings': '🇦🇺 AUS',
        'CJ Green': '🇦🇺 AUS', 'Chris Green': '🇦🇺 AUS', 'BJ Dwarshuis': '🇦🇺 AUS', 'Ben Dwarshuis': '🇦🇺 AUS',
        'SA Abbott': '🇦🇺 AUS', 'Sean Abbott': '🇦🇺 AUS', 'AC Agar': '🇦🇺 AUS', 'Ashton Agar': '🇦🇺 AUS',
        'A Zampa': '🇦🇺 AUS', 'Adam Zampa': '🇦🇺 AUS', 'AJ Turner': '🇦🇺 AUS', 'Ashton Turner': '🇦🇺 AUS',
        'DJM Short': '🇦🇺 AUS', 'D\'Arcy Short': '🇦🇺 AUS', 'TL Birt': '🇦🇺 AUS', 'Travis Birt': '🇦🇺 AUS',
        'AC Blizzard': '🇦🇺 AUS', 'Aiden Blizzard': '🇦🇺 AUS', 'LA Pomersbach': '🇦🇺 AUS', 'Luke Pomersbach': '🇦🇺 AUS',
        'CJ Ferguson': '🇦🇺 AUS', 'Callum Ferguson': '🇦🇺 AUS', 'AJ Tye': '🇦🇺 AUS', 'Andrew Tye': '🇦🇺 AUS',
        'AC Voges': '🇦🇺 AUS', 'Adam Voges': '🇦🇺 AUS', 'AA Noffke': '🇦🇺 AUS', 'Ashley Noffke': '🇦🇺 AUS',
        'MJ Clarke': '🇦🇺 AUS', 'Michael Clarke': '🇦🇺 AUS', 'SM Harwood': '🇦🇺 AUS', 'Shane Harwood': '🇦🇺 AUS',
        'DS Lehmann': '🇦🇺 AUS', 'Darren Lehmann': '🇦🇺 AUS', 'B Geeves': '🇦🇺 AUS', 'Brett Geeves': '🇦🇺 AUS',
        'BR Dunk': '🇦🇺 AUS', 'Ben Dunk': '🇦🇺 AUS', 'BR Rohrer': '🇦🇺 AUS', 'Ben Rohrer': '🇦🇺 AUS',
        'CA Ingram': '🇦🇺 AUS', 'NJ Maddinson': '🇦🇺 AUS', 'Nic Maddinson': '🇦🇺 AUS', 'NJ Rimmington': '🇦🇺 AUS',
        'Nathan Rimmington': '🇦🇺 AUS', 'DJ Thornely': '🇦🇺 AUS', 'Dominic Thornely': '🇦🇺 AUS',

        # 🇿🇦 SOUTH AFRICA (SA)
        'AB de Villiers': '🇿🇦 SA', 'F du Plessis': '🇿🇦 SA', 'Faf du Plessis': '🇿🇦 SA',
        'Q de Kock': '🇿🇦 SA', 'Quinton de Kock': '🇿🇦 SA', 'K Rabada': '🇿🇦 SA', 'Kagiso Rabada': '🇿🇦 SA',
        'DA Miller': '🇿🇦 SA', 'David Miller': '🇿🇦 SA', 'DW Steyn': '🇿🇦 SA', 'Dale Steyn': '🇿🇦 SA',
        'JH Kallis': '🇿🇦 SA', 'Jacques Kallis': '🇿🇦 SA', 'I Tahir': '🇿🇦 SA', 'Imran Tahir': '🇿🇦 SA',
        'CH Morris': '🇿🇦 SA', 'Chris Morris': '🇿🇦 SA', 'A Nortje': '🇿🇦 SA', 'Anrich Nortje': '🇿🇦 SA',
        'L Ngidi': '🇿🇦 SA', 'Lungi Ngidi': '🇿🇦 SA', 'M Jansen': '🇿🇦 SA', 'Marco Jansen': '🇿🇦 SA',
        'H Klaasen': '🇿🇦 SA', 'Heinrich Klaasen': '🇿🇦 SA', 'AK Markram': '🇿🇦 SA', 'Aiden Markram': '🇿🇦 SA',
        'T Stubbs': '🇿🇦 SA', 'Tristan Stubbs': '🇿🇦 SA', 'G Coetzee': '🇿🇦 SA', 'Gerald Coetzee': '🇿🇦 SA',
        'N Burger': '🇿🇦 SA', 'Nandre Burger': '🇿🇦 SA', 'D Brevis': '🇿🇦 SA', 'Dewald Brevis': '🇿🇦 SA',
        'HE van der Dussen': '🇿🇦 SA', 'Rassie van der Dussen': '🇿🇦 SA', 'M Morkel': '🇿🇦 SA', 'Morne Morkel': '🇿🇦 SA',
        'JA Morkel': '🇿🇦 SA', 'Albie Morkel': '🇿🇦 SA', 'JEC Duminy': '🇿🇦 SA', 'JP Duminy': '🇿🇦 SA',
        'HH Gibbs': '🇿🇦 SA', 'Herschelle Gibbs': '🇿🇦 SA', 'GC Smith': '🇿🇦 SA', 'Graeme Smith': '🇿🇦 SA',
        'MV Boucher': '🇿🇦 SA', 'Mark Boucher': '🇿🇦 SA', 'M Ntini': '🇿🇦 SA', 'Makhaya Ntini': '🇿🇦 SA',
        'SM Pollock': '🇿🇦 SA', 'Shaun Pollock': '🇿🇦 SA', 'RE van der Merwe': '🇿🇦 SA', 'Roelof van der Merwe': '🇿🇦 SA',
        'WD Parnell': '🇿🇦 SA', 'Wayne Parnell': '🇿🇦 SA', 'RE Levi': '🇿🇦 SA', 'Richard Levi': '🇿🇦 SA',
        'RJ Peterson': '🇿🇦 SA', 'Robin Peterson': '🇿🇦 SA', 'AC Thomas': '🇿🇦 SA', 'Alfonso Thomas': '🇿🇦 SA',
        'DJ Jacobs': '🇿🇦 SA', 'Davy Jacobs': '🇿🇦 SA', 'J Theron': '🇿🇦 SA', 'Rusty Theron': '🇿🇦 SA',
        'F Behardien': '🇿🇦 SA', 'Farhaan Behardien': '🇿🇦 SA', 'BE Hendricks': '🇿🇦 SA', 'Beuran Hendricks': '🇿🇦 SA',
        'D Wiese': '🇿🇦 SA', 'David Wiese': '🇿🇦 SA', 'T Shamsi': '🇿🇦 SA', 'Tabraiz Shamsi': '🇿🇦 SA',
        'CJ Dala': '🇿🇦 SA', 'Junior Dala': '🇿🇦 SA', 'D Pretorius': '🇿🇦 SA', 'Dwaine Pretorius': '🇿🇦 SA',
        'SSB Magala': '🇿🇦 SA', 'Sisanda Magala': '🇿🇦 SA', 'L Williams': '🇿🇦 SA', 'Lizaad Williams': '🇿🇦 SA',
        'K Maphaka': '🇿🇦 SA', 'Kwena Maphaka': '🇿🇦 SA', 'A Nel': '🇿🇦 SA', 'Andre Nel': '🇿🇦 SA',
        'MN van Wyk': '🇿🇦 SA', 'Morne van Wyk': '🇿🇦 SA', 'LL Tsotsobe': '🇿🇦 SA', 'Lonwabo Tsotsobe': '🇿🇦 SA',
        'CK Langeveldt': '🇿🇦 SA', 'Charl Langeveldt': '🇿🇦 SA', 'R McLaren': '🇿🇦 SA', 'Ryan McLaren': '🇿🇦 SA',
        'T Henderson': '🇿🇦 SA', 'Tyron Henderson': '🇿🇦 SA', 'RD Rickelton': '🇿🇦 SA', 'Ryan Rickelton': '🇿🇦 SA',
        'Donovan Ferreira': '🇿🇦 SA', 'D Ferreira': '🇿🇦 SA',

        # 🌴 WEST INDIES (WI)
        'CH Gayle': '🌴 WI', 'Chris Gayle': '🌴 WI', 'AD Russell': '🌴 WI', 'Andre Russell': '🌴 WI',
        'SP Narine': '🌴 WI', 'Sunil Narine': '🌴 WI', 'KA Pollard': '🌴 WI', 'Kieron Pollard': '🌴 WI',
        'DJ Bravo': '🌴 WI', 'Dwayne Bravo': '🌴 WI', 'SO Hetmyer': '🌴 WI', 'Shimron Hetmyer': '🌴 WI',
        'N Pooran': '🌴 WI', 'Nicholas Pooran': '🌴 WI', 'SD Hope': '🌴 WI', 'Shai Hope': '🌴 WI',
        'R Powell': '🌴 WI', 'Rovman Powell': '🌴 WI', 'JO Holder': '🌴 WI', 'Jason Holder': '🌴 WI',
        'AS Joseph': '🌴 WI', 'Alzarri Joseph': '🌴 WI', 'R Shepherd': '🌴 WI', 'Romario Shepherd': '🌴 WI',
        'AJ Hosein': '🌴 WI', 'Akeal Hosein': '🌴 WI', 'O Smith': '🌴 WI', 'Odean Smith': '🌴 WI',
        'FA Allen': '🌴 WI', 'Fabian Allen': '🌴 WI', 'DC Drakes': '🌴 WI', 'Dominic Drakes': '🌴 WI',
        'KR Mayers': '🌴 WI', 'Kyle Mayers': '🌴 WI', 'OC McCoy': '🌴 WI', 'Obed McCoy': '🌴 WI',
        'E Lewis': '🌴 WI', 'Evin Lewis': '🌴 WI', 'LMP Simmons': '🌴 WI', 'Lendl Simmons': '🌴 WI',
        'DR Smith': '🌴 WI', 'Dwayne Smith': '🌴 WI', 'DJG Sammy': '🌴 WI', 'Darren Sammy': '🌴 WI',
        'CR Brathwaite': '🌴 WI', 'Carlos Brathwaite': '🌴 WI', 'MN Samuels': '🌴 WI', 'Marlon Samuels': '🌴 WI',
        'S Chanderpaul': '🌴 WI', 'Shivnarine Chanderpaul': '🌴 WI', 'RR Sarwan': '🌴 WI', 'Ramnaresh Sarwan': '🌴 WI',
        'BC Lara': '🌴 WI', 'Brian Lara': '🌴 WI', 'FH Edwards': '🌴 WI', 'Fidel Edwards': '🌴 WI',
        'JE Taylor': '🌴 WI', 'Jerome Taylor': '🌴 WI', 'KA Roach': '🌴 WI', 'Kemar Roach': '🌴 WI',
        'R Rampaul': '🌴 WI', 'Ravi Rampaul': '🌴 WI', 'S Badree': '🌴 WI', 'Samuel Badree': '🌴 WI',
        'AR Nurse': '🌴 WI', 'Ashley Nurse': '🌴 WI', 'KMA Paul': '🌴 WI', 'Keemo Paul': '🌴 WI',
        'O Thomas': '🌴 WI', 'Oshane Thomas': '🌴 WI', 'SE Rutherford': '🌴 WI', 'Sherfane Rutherford': '🌴 WI',
        'J Charles': '🌴 WI', 'Johnson Charles': '🌴 WI', 'AB Barath': '🌴 WI', 'Adrian Barath': '🌴 WI',
        'DM Bravo': '🌴 WI', 'Darren Bravo': '🌴 WI', 'K Santokie': '🌴 WI', 'Krishmar Santokie': '🌴 WI',
        'JL Carter': '🌴 WI', 'K Pierre': '🌴 WI', 'Khary Pierre': '🌴 WI', 'S Cottrell': '🌴 WI', 'Sheldon Cottrell': '🌴 WI',
        'Shamar Joseph': '🌴 WI',

        # 🇳🇿 NEW ZEALAND (NZ)
        'KS Williamson': '🇳🇿 NZ', 'Kane Williamson': '🇳🇿 NZ', 'TA Boult': '🇳🇿 NZ', 'Trent Boult': '🇳🇿 NZ',
        'BB McCullum': '🇳🇿 NZ', 'Brendon McCullum': '🇳🇿 NZ', 'LH Ferguson': '🇳🇿 NZ', 'Lockie Ferguson': '🇳🇿 NZ',
        'DP Conway': '🇳🇿 NZ', 'Devon Conway': '🇳🇿 NZ', 'MJ Santner': '🇳🇿 NZ', 'Mitchell Santner': '🇳🇿 NZ',
        'TG Southee': '🇳🇿 NZ', 'Tim Southee': '🇳🇿 NZ', 'LRPL Taylor': '🇳🇿 NZ', 'Ross Taylor': '🇳🇿 NZ',
        'MJ Guptill': '🇳🇿 NZ', 'Martin Guptill': '🇳🇿 NZ', 'CJ Anderson': '🇳🇿 NZ', 'Corey Anderson': '🇳🇿 NZ',
        'C de Grandhomme': '🇳🇿 NZ', 'Colin de Grandhomme': '🇳🇿 NZ', 'JDS Neesham': '🇳🇿 NZ', 'Jimmy Neesham': '🇳🇿 NZ',
        'KA Jamieson': '🇳🇿 NZ', 'Kyle Jamieson': '🇳🇿 NZ', 'DJ Mitchell': '🇳🇿 NZ', 'Daryl Mitchell': '🇳🇿 NZ',
        'GD Phillips': '🇳🇿 NZ', 'Glenn Phillips': '🇳🇿 NZ', 'FH Allen': '🇳🇿 NZ', 'Finn Allen': '🇳🇿 NZ',
        'AF Milne': '🇳🇿 NZ', 'Adam Milne': '🇳🇿 NZ', 'MJ Henry': '🇳🇿 NZ', 'Matt Henry': '🇳🇿 NZ',
        'SC Kuggeleijn': '🇳🇿 NZ', 'Scott Kuggeleijn': '🇳🇿 NZ', 'IS Sodhi': '🇳🇿 NZ', 'Ish Sodhi': '🇳🇿 NZ',
        'R Ravindra': '🇳🇿 NZ', 'Rachin Ravindra': '🇳🇿 NZ', 'MG Bracewell': '🇳🇿 NZ', 'Michael Bracewell': '🇳🇿 NZ',
        'DL Vettori': '🇳🇿 NZ', 'Daniel Vettori': '🇳🇿 NZ', 'JDP Oram': '🇳🇿 NZ', 'Jacob Oram': '🇳🇿 NZ',
        'SP Fleming': '🇳🇿 NZ', 'Stephen Fleming': '🇳🇿 NZ', 'SB Styris': '🇳🇿 NZ', 'Scott Styris': '🇳🇿 NZ',
        'NL McCullum': '🇳🇿 NZ', 'Nathan McCullum': '🇳🇿 NZ', 'JEC Franklin': '🇳🇿 NZ', 'James Franklin': '🇳🇿 NZ',
        'JD Ryder': '🇳🇿 NZ', 'Jesse Ryder': '🇳🇿 NZ', 'KD Mills': '🇳🇿 NZ', 'Kyle Mills': '🇳🇿 NZ',
        'C Munro': '🇳🇿 NZ', 'Colin Munro': '🇳🇿 NZ', 'DAJ Bracewell': '🇳🇿 NZ', 'Doug Bracewell': '🇳🇿 NZ',
        'SB Doull': '🇳🇿 NZ', 'Simon Doull': '🇳🇿 NZ', 'L Woodcock': '🇳🇿 NZ', 'Luke Woodcock': '🇳🇿 NZ',

        # 🇦🇫 AFGHANISTAN (AFG)
        'Rashid Khan': '🇦🇫 AFG', 'Mohammad Nabi': '🇦🇫 AFG', 'Mujeeb Ur Rahman': '🇦🇫 AFG',
        'Noor Ahmad': '🇦🇫 AFG', 'Fazalhaq Farooqi': '🇦🇫 AFG', 'R Gurbaz': '🇦🇫 AFG', 'Rahmanullah Gurbaz': '🇦🇫 AFG',
        'Naveen-ul-Haq': '🇦🇫 AFG', 'A Omarzai': '🇦🇫 AFG', 'Azmatullah Omarzai': '🇦🇫 AFG',
        'G Naib': '🇦🇫 AFG', 'Gulbadin Naib': '🇦🇫 AFG', 'AM Ghazanfar': '🇦🇫 AFG', 'Allah Ghazanfar': '🇦🇫 AFG',
        'Qais Ahmad': '🇦🇫 AFG', 'Zahir Khan': '🇦🇫 AFG', 'Waqar Salamkheil': '🇦🇫 AFG',

        # 🇱🇰 SRI LANKA (SL)
        'SL Malinga': '🇱🇰 SL', 'Lasith Malinga': '🇱🇰 SL', 'M Muralitharan': '🇱🇰 SL', 'Muttiah Muralitharan': '🇱🇰 SL',
        'KC Sangakkara': '🇱🇰 SL', 'Kumar Sangakkara': '🇱🇰 SL', 'DPMD Jayawardene': '🇱🇰 SL', 'Mahela Jayawardene': '🇱🇰 SL',
        'ST Jayasuriya': '🇱🇰 SL', 'Sanath Jayasuriya': '🇱🇰 SL', 'TM Dilshan': '🇱🇰 SL', 'Tillakaratne Dilshan': '🇱🇰 SL',
        'WPUJC Vaas': '🇱🇰 SL', 'Chaminda Vaas': '🇱🇰 SL', 'KMDN Kulasekara': '🇱🇰 SL', 'Nuwan Kulasekara': '🇱🇰 SL',
        'MF Maharoof': '🇱🇰 SL', 'Farveez Maharoof': '🇱🇰 SL', 'AD Mathews': '🇱🇰 SL', 'Angelo Mathews': '🇱🇰 SL',
        'NLTC Perera': '🇱🇰 SL', 'Thisara Perera': '🇱🇰 SL', 'PWH de Silva': '🇱🇰 SL', 'Wanindu Hasaranga': '🇱🇰 SL',
        'M Pathirana': '🇱🇰 SL', 'Matheesha Pathirana': '🇱🇰 SL', 'M Theekshana': '🇱🇰 SL', 'Maheesh Theekshana': '🇱🇰 SL',
        'PVD Chameera': '🇱🇰 SL', 'Dushmantha Chameera': '🇱🇰 SL', 'D Madushanka': '🇱🇰 SL', 'Dilshan Madushanka': '🇱🇰 SL',
        'PBB Rajapaksa': '🇱🇰 SL', 'Bhanuka Rajapaksa': '🇱🇰 SL', 'N Thushara': '🇱🇰 SL', 'Nuwan Thushara': '🇱🇰 SL',
        'C Karunaratne': '🇱🇰 SL', 'Chamika Karunaratne': '🇱🇰 SL', 'I Udana': '🇱🇰 SL', 'Isuru Udana': '🇱🇰 SL',
        'A Dananjaya': '🇱🇰 SL', 'Akila Dananjaya': '🇱🇰 SL', 'SMSM Senanayake': '🇱🇰 SL', 'Sachithra Senanayake': '🇱🇰 SL',
        'BAW Mendis': '🇱🇰 SL', 'Ajantha Mendis': '🇱🇰 SL', 'CRD Fernando': '🇱🇰 SL', 'Dilhara Fernando': '🇱🇰 SL',
        'KDK Vithanage': '🇱🇰 SL', 'MDKJ Perera': '🇱🇰 SL', 'Kusal Perera': '🇱🇰 SL', 'CK Kapugedera': '🇱🇰 SL',
        'Chamara Kapugedera': '🇱🇰 SL', 'S Prasanna': '🇱🇰 SL', 'Seekkuge Prasanna': '🇱🇰 SL', 'BMAJ Mendis': '🇱🇰 SL',
        'Jeevan Mendis': '🇱🇰 SL', 'M Pushpakumara': '🇱🇰 SL', 'Malinda Pushpakumara': '🇱🇰 SL', 'E Malinga': '🇱🇰 SL',

        # 🇵🇰 PAKISTAN (PAK)
        'Shoaib Akhtar': '🇵🇰 PAK', 'Shahid Afridi': '🇵🇰 PAK', 'Sohail Tanvir': '🇵🇰 PAK',
        'Kamran Akmal': '🇵🇰 PAK', 'Umar Gul': '🇵🇰 PAK', 'Misbah-ul-Haq': '🇵🇰 PAK',
        'Mohammad Asif': '🇵🇰 PAK', 'Salman Butt': '🇵🇰 PAK', 'Younis Khan': '🇵🇰 PAK',
        'Mohammad Hafeez': '🇵🇰 PAK', 'Shoaib Malik': '🇵🇰 PAK', 'Azhar Mahmood': '🇵🇰 PAK',

        # 🇧🇩 BANGLADESH (BAN)
        'Shakib Al Hasan': '🇧🇩 BAN', 'Mustafizur Rahman': '🇧🇩 BAN', 'Mashrafe Mortaza': '🇧🇩 BAN',
        'Tamim Iqbal': '🇧🇩 BAN', 'Mohammad Ashraful': '🇧🇩 BAN', 'Abdur Razzak': '🇧🇩 BAN',
        'Litton Das': '🇧🇩 BAN', 'Taskin Ahmed': '🇧🇩 BAN', 'Tanzim Hasan Sakib': '🇧🇩 BAN',

        # 🇿🇼 ZIMBABWE (ZIM)
        'Brendan Taylor': '🇿🇼 ZIM', 'Tatenda Taibu': '🇿🇼 ZIM', 'Ray Price': '🇿🇼 ZIM',
        'Sikandar Raza': '🇿🇼 ZIM',

        # 🇳🇱 NETHERLANDS (NED)
        'RN ten Doeschate': '🇳🇱 NED', 'Ryan ten Doeschate': '🇳🇱 NED', 'Paul van Meekeren': '🇳🇱 NED',

        # 🇮🇪 IRELAND (IRE)
        'J Little': '🇮🇪 IRE', 'Joshua Little': '🇮🇪 IRE', 'Paul Stirling': '🇮🇪 IRE',

        # 🇺🇸 USA
        'Ali Khan': '🇺🇸 USA', 'Saurabh Netravalkar': '🇺🇸 USA',

        # 🇳🇦 NAMIBIA (NAM)
        'David Wiese': '🇳🇦 NAM'
    }
    
    # 1. Direct match
    if player in overseas_map:
        return overseas_map[player]
        
    # 2. Check alias
    if 'LEGEND_ALIASES' in globals() and player in LEGEND_ALIASES:
        resolved = LEGEND_ALIASES[player]
        if resolved in overseas_map:
            return overseas_map[resolved]
            
    # Default to India for Indian domestic/national players
    return '🇮🇳 IND'

def get_player_tier_and_meta(player, runs, wickets, overall, matches_df=None, deliveries_df=None):
    """Dynamically determines the Four-Tier classification (ICON, EPIC, RARE, STANDARD) based on analysis."""
    debut_season = 2018
    if deliveries_df is not None and matches_df is not None:
        try:
            p_matches = deliveries_df[(deliveries_df['batsman'] == player) | (deliveries_df['bowler'] == player)]['match_id'].unique()
            if len(p_matches) > 0:
                seasons = matches_df[matches_df['id'].isin(p_matches)]['season'].dropna()
                if not seasons.empty:
                    debut_season = int(seasons.min())
        except Exception:
            pass

    icon_legends = {
        'V Kohli', 'MS Dhoni', 'RG Sharma', 'AB de Villiers', 'CH Gayle', 'SK Raina',
        'DA Warner', 'SL Malinga', 'JJ Bumrah', 'SP Narine'
    }
    epic_stars = {
        'Rashid Khan', 'AD Russell', 'KA Pollard', 'KL Rahul', 'YS Chahal', 'B Kumar',
        'RA Jadeja', 'S Dhawan', 'SV Samson', 'SA Yadav', 'HH Pandya', 'F du Plessis'
    }
    
    if player in icon_legends or overall >= 93 or runs >= 4800 or wickets >= 130 or (runs >= 3000 and wickets >= 50):
        return {
            'tier': 'ICON',
            'badge': '👑 ICON',
            'class': 'tier-icon',
            'color': '#f59e0b',
            'salary': '15.0 - 18.0 CR',
            'debut': debut_season,
            'header_bg': 'linear-gradient(90deg, #b45309, #fde047, #b45309)',
            'watermark': '🏏'
        }
    elif player in epic_stars or overall >= 86 or runs >= 2500 or wickets >= 70 or (runs >= 1500 and wickets >= 30):
        return {
            'tier': 'EPIC',
            'badge': '⚡ EPIC',
            'class': 'tier-epic',
            'color': '#a855f7',
            'salary': '8.0 - 14.0 CR',
            'debut': debut_season,
            'header_bg': 'linear-gradient(90deg, #7e22ce, #c084fc, #7e22ce)',
            'watermark': '🧤' if runs > wickets else '⚾'
        }
    elif overall >= 76 or runs >= 1000 or wickets >= 35:
        return {
            'tier': 'RARE',
            'badge': '⭐ RARE',
            'class': 'tier-rare',
            'color': '#cbd5e1',
            'salary': '2.5 - 7.5 CR',
            'debut': debut_season,
            'header_bg': 'linear-gradient(90deg, #94a3b8, #f1f5f9, #94a3b8)',
            'watermark': '🏏' if runs > wickets else '⚾'
        }
    else:
        return {
            'tier': 'STANDARD',
            'badge': '🛡️ STANDARD',
            'class': 'tier-standard',
            'color': '#64748b',
            'salary': '0.2 - 2.0 CR',
            'debut': debut_season,
            'header_bg': 'linear-gradient(90deg, #334155, #64748b, #334155)',
            'watermark': '⚾'
        }

def generate_player_avatar_svg(name, team='IPL'):
    parts = name.split()
    initials = (parts[0][0] + parts[-1][0]).upper() if len(parts) > 1 else name[:2].upper()
    team_colors = {
        'Chennai Super Kings': ('#F9CD05', '#004BA0'),
        'Mumbai Indians': ('#004BA0', '#D1AB3E'),
        'Kolkata Knight Riders': ('#3A225D', '#D4AF37'),
        'Royal Challengers Bengaluru': ('#C8102E', '#000000'),
        'Royal Challengers Bangalore': ('#C8102E', '#000000'),
        'Delhi Capitals': ('#004C97', '#EA1A85'),
        'Rajasthan Royals': ('#EA1A85', '#004BA0'),
        'Sunrisers Hyderabad': ('#F26522', '#000000'),
        'Punjab Kings': ('#DD1F2D', '#D4AF37'),
        'Gujarat Titans': ('#1B2133', '#1B6A97'),
        'Lucknow Super Giants': ('#00A3E0', '#FF8200')
    }
    c1, c2 = team_colors.get(team, ('#1e293b', '#0f172a'))
    short_team = ''.join([w[0] for w in team.split() if w[0].isupper()])[:4]
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
      <defs>
        <radialGradient id="bg" cx="50%" cy="35%" r="60%">
          <stop offset="0%" stop-color="{c1}" />
          <stop offset="100%" stop-color="{c2}" />
        </radialGradient>
      </defs>
      <circle cx="100" cy="100" r="96" fill="url(#bg)" stroke="#f59e0b" stroke-width="4"/>
      <circle cx="100" cy="72" r="26" fill="#ffffff" opacity="0.25" />
      <path d="M55 155 C55 115, 145 115, 145 155 Z" fill="#ffffff" opacity="0.25" />
      <text x="100" y="108" font-family="'Outfit', sans-serif" font-weight="900" font-size="44" fill="#ffffff" text-anchor="middle" letter-spacing="1">{initials}</text>
      <rect x="55" y="150" width="90" height="22" rx="11" fill="rgba(0,0,0,0.6)" stroke="#f59e0b" stroke-width="1.5" />
      <text x="100" y="165" font-family="'Outfit', sans-serif" font-weight="800" font-size="11" fill="#f59e0b" text-anchor="middle" letter-spacing="1">{short_team}</text>
    </svg>"""
    encoded = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    return f'data:image/svg+xml;base64,{encoded}'

@st.cache_data(ttl=86400)
def get_team_logo(team_name):
    if team_name in OFFICIAL_TEAM_LOGOS:
        return OFFICIAL_TEAM_LOGOS[team_name]
    try:
        slug = team_name.replace(' ', '_')
        headers = {'User-Agent': 'IPLAnalyticsDashboard/2.0 (contact: tejas.ingle@example.com)'}
        url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{slug}'
        r = requests.get(url, headers=headers, timeout=3)
        if r.status_code == 200:
            thumb = r.json().get('thumbnail', {}).get('source')
            if thumb: return thumb
    except Exception:
        pass
    return generate_player_avatar_svg(team_name, team_name)

# Legacy alias for compatibility
def get_team_logo_base64(team_name):
    return get_team_logo(team_name)

# ==========================================
# 🌟 USER'S 423-PLAYER JERSEY DATASET & FULL NAME ENGINE
# ==========================================
PLAYER_FULL_NAME_MAP = {
    'V Kohli': 'Virat Kohli',
    'RG Sharma': 'Rohit Sharma',
    'MS Dhoni': 'MS Dhoni',
    'AB de Villiers': 'AB de Villiers',
    'CH Gayle': 'Chris Gayle',
    'DA Warner': 'David Warner',
    'SK Raina': 'Suresh Raina',
    'JJ Bumrah': 'Jasprit Bumrah',
    'B Kumar': 'Bhuvneshwar Kumar',
    'RA Jadeja': 'Ravindra Jadeja',
    'KL Rahul': 'KL Rahul',
    'RR Pant': 'Rishabh Pant',
    'HH Pandya': 'Hardik Pandya',
    'KA Pollard': 'Kieron Pollard',
    'SL Malinga': 'Lasith Malinga',
    'SP Narine': 'Sunil Narine',
    'DJ Bravo': 'Dwayne Bravo',
    'SR Watson': 'Shane Watson',
    'YS Chahal': 'Yuzvendra Chahal',
    'SV Samson': 'Sanju Samson',
    'Shubman Gill': 'Shubman Gill',
    'Rashid Khan': 'Rashid Khan',
    'Mohammed Shami': 'Mohammed Shami',
    'Mohammed Siraj': 'Mohammed Siraj',
    'Arshdeep Singh': 'Arshdeep Singh',
    'R Ashwin': 'Ravichandran Ashwin',
    'Harbhajan Singh': 'Harbhajan Singh',
    'G Gambhir': 'Gautam Gambhir',
    'Yuvraj Singh': 'Yuvraj Singh',
    'KD Karthik': 'Dinesh Karthik',
    'RV Uthappa': 'Robin Uthappa',
    'AT Rayudu': 'Ambati Rayudu',
    'A Nehra': 'Ashish Nehra',
    'Z Khan': 'Zaheer Khan',
    'IK Pathan': 'Irfan Pathan',
    'YK Pathan': 'Yusuf Pathan',
    'SS Iyer': 'Shreyas Iyer',
    'JC Buttler': 'Jos Buttler',
    'Q de Kock': 'Quinton de Kock',
    'F du Plessis': 'Faf du Plessis',
    'GJ Maxwell': 'Glenn Maxwell',
    'TA Boult': 'Trent Boult',
    'K Rabada': 'Kagiso Rabada',
    'A Ashish Reddy': 'Ashish Reddy',
    'R Parag': 'Riyan Parag',
    'YBK Jaiswal': 'Yashasvi Jaiswal',
    'SA Yadav': 'Suryakumar Yadav',
    'Tilak Varma': 'Tilak Varma',
    'Ishan Kishan': 'Ishan Kishan',
    'A Flintoff': 'Andrew Flintoff',
    'KP Pietersen': 'Kevin Pietersen',
    'AC Gilchrist': 'Adam Gilchrist',
    'ML Hayden': 'Matthew Hayden',
    'B Lee': 'Brett Lee',
    'SK Warne': 'Shane Warne',
    'M Muralitharan': 'Muttiah Muralitharan',
    'KC Sangakkara': 'Kumar Sangakkara',
    'DPMD Jayawardene': 'Mahela Jayawardene',
    'ST Jayasuriya': 'Sanath Jayasuriya',
    'DW Steyn': 'Dale Steyn',
    'JH Kallis': 'Jacques Kallis',
    'SE Marsh': 'Shaun Marsh',
    'MEK Hussey': 'Michael Hussey',
    'Sohail Tanvir': 'Sohail Tanvir',
    'Shahid Afridi': 'Shahid Afridi',
    'Shoaib Akhtar': 'Shoaib Akhtar',
    'Kamran Akmal': 'Kamran Akmal',
    'V Sehwag': 'Virender Sehwag',
    'SR Tendulkar': 'Sachin Tendulkar',
    'BA Stokes': 'Ben Stokes',
    'SM Curran': 'Sam Curran',
    'MM Ali': 'Moeen Ali',
    'LS Livingstone': 'Liam Livingstone',
    'EJG Morgan': 'Eoin Morgan',
    'JM Bairstow': 'Jonny Bairstow',
    'HC Brook': 'Harry Brook',
    'CR Woakes': 'Chris Woakes',
    'CJ Jordan': 'Chris Jordan',
    'MA Wood': 'Mark Wood',
    'JJ Roy': 'Jason Roy',
    'AD Hales': 'Alex Hales',
    'PD Salt': 'Phil Salt',
    'Phil Salt': 'Phil Salt',
    'WG Jacks': 'Will Jacks',
    'J Fraser-McGurk': 'Jake Fraser-McGurk',
    'Travis Head': 'Travis Head',
    'TM Head': 'Travis Head',
    'H Klaasen': 'Heinrich Klaasen',
    'Heinrich Klaasen': 'Heinrich Klaasen',
    'PJ Cummins': 'Pat Cummins',
    'Pat Cummins': 'Pat Cummins',
    'MA Starc': 'Mitchell Starc',
    'Mitchell Starc': 'Mitchell Starc',
    'MP Stoinis': 'Marcus Stoinis',
    'Marcus Stoinis': 'Marcus Stoinis',
    'A Symonds': 'Andrew Symonds',
    'BJ Hodge': 'Brad Hodge',
    'GB Hogg': 'Brad Hogg',
    'BB McCullum': 'Brendon McCullum',
    'KS Williamson': 'Kane Williamson',
    'LH Ferguson': 'Lockie Ferguson',
    'DP Conway': 'Devon Conway',
    'MJ Santner': 'Mitchell Santner',
    'TG Southee': 'Tim Southee',
    'LRPL Taylor': 'Ross Taylor',
    'MJ Guptill': 'Martin Guptill',
    'CJ Anderson': 'Corey Anderson',
    'C de Grandhomme': 'Colin de Grandhomme',
    'JDS Neesham': 'Jimmy Neesham',
    'KA Jamieson': 'Kyle Jamieson',
    'DJ Mitchell': 'Daryl Mitchell',
    'GD Phillips': 'Glenn Phillips',
    'FH Allen': 'Finn Allen',
    'AF Milne': 'Adam Milne',
    'R Ravindra': 'Rachin Ravindra',
    'DL Vettori': 'Daniel Vettori',
    'SP Fleming': 'Stephen Fleming',
    'SB Styris': 'Scott Styris',
    'A Nortje': 'Anrich Nortje',
    'L Ngidi': 'Lungi Ngidi',
    'M Jansen': 'Marco Jansen',
    'AK Markram': 'Aiden Markram',
    'T Stubbs': 'Tristan Stubbs',
    'G Coetzee': 'Gerald Coetzee',
    'N Burger': 'Nandre Burger',
    'D Brevis': 'Dewald Brevis',
    'M Morkel': 'Morne Morkel',
    'JA Morkel': 'Albie Morkel',
    'JEC Duminy': 'JP Duminy',
    'HH Gibbs': 'Herschelle Gibbs',
    'GC Smith': 'Graeme Smith',
    'MV Boucher': 'Mark Boucher',
    'M Ntini': 'Makhaya Ntini',
    'SM Pollock': 'Shaun Pollock',
    'CH Morris': 'Chris Morris',
    'I Tahir': 'Imran Tahir',
    'Shakib Al Hasan': 'Shakib Al Hasan',
    'Mustafizur Rahman': 'Mustafizur Rahman',
    'Mohammad Nabi': 'Mohammad Nabi',
    'Mujeeb Ur Rahman': 'Mujeeb Ur Rahman',
    'Noor Ahmad': 'Noor Ahmad',
    'Fazalhaq Farooqi': 'Fazalhaq Farooqi',
    'Naveen-ul-Haq': 'Naveen-ul-Haq',
    'R Gurbaz': 'Rahmanullah Gurbaz',
    'PWH de Silva': 'Wanindu Hasaranga',
    'M Pathirana': 'Matheesha Pathirana',
    'M Theekshana': 'Maheesh Theekshana',
    'AD Mathews': 'Angelo Mathews',
    'NLTC Perera': 'Thisara Perera',
    'WPUJC Vaas': 'Chaminda Vaas',
    'KMDN Kulasekara': 'Nuwan Kulasekara',
    'TM Dilshan': 'Tillakaratne Dilshan',
    'RN ten Doeschate': 'Ryan ten Doeschate',
    'J Little': 'Joshua Little',
    'Sikandar Raza': 'Sikandar Raza',
    'Ali Khan': 'Ali Khan',
    'A Badoni': 'Ayush Badoni',
    'A Manohar': 'Abhinav Manohar',
    'A Mishra': 'Amit Mishra',
    'A Mithun': 'Abhimanyu Mithun',
    'A Mukund': 'Abhinav Mukund',
    'A Raghuvanshi': 'Angkrish Raghuvanshi',
    'A Singh': 'Arshdeep Singh',
    'A Tomar': 'Ankit Tomar',
    'AA Bilakhia': 'Azhar Bilakhia',
    'AA Chavan': 'Ankeet Chavan',
    'AA Jhunjhunwala': 'Abhishek Jhunjhunwala',
    'AA Kazi': 'Abrar Kazi',
    'AA Kulkarni': 'Arshin Kulkarni',
    'AB Agarkar': 'Ajit Agarkar',
    'AB Barath': 'Adrian Barath',
    'AB Dinda': 'Ashok Dinda',
    'AB McDonald': 'Andrew McDonald',
    'AC Blizzard': 'Aiden Blizzard',
    'AC Thomas': 'Alfonso Thomas',
    'AC Voges': 'Adam Voges',
    'AD Mascarenhas': 'Dimitri Mascarenhas',
    'AD Russell': 'Andre Russell',
    'AG Murtaza': 'Ali Murtaza',
    'AG Paunikar': 'Amit Paunikar',
    'AJ Finch': 'Aaron Finch',
    'AJ Hosein': 'Akeal Hosein',
    'AJ Turner': 'Ashton Turner',
    'AJ Tye': 'Andrew Tye',
    'AL Menaria': 'Ashok Menaria',
    'AM Nayar': 'Abhishek Nayar',
    'AM Rahane': 'Ajinkya Rahane',
    'AN Ahmed': 'Abu Nechim',
    'AP Dole': 'Aditya Dole',
    'AP Majumdar': 'Anustup Majumdar',
    'AP Tare': 'Aditya Tare',
    'AR Bawne': 'Ankit Bawne',
    'AR Patel': 'Axar Patel',
    'AS Joseph': 'Alzarri Joseph',
    'AS Rajpoot': 'Ankit Rajpoot',
    'AS Raut': 'Abhishek Raut',
    'AS Yadav': 'Suryakumar Yadav',
    'AT Carey': 'Alex Carey',
    'Avesh Khan': 'Avesh Khan',
    'Azhar Mahmood': 'Azhar Mahmood',
    'B Akhil': 'Balachandra Akhil',
    'B Chipli': 'Bharat Chipli',
    'B Indrajith': 'Baba Indrajith',
    'B Laughlin': 'Ben Laughlin',
    'B Sai Sudharsan': 'Sai Sudharsan',
    'B Sumanth': 'Bodhapati Sumanth',
    'BA Bhatt': 'Bhargav Bhatt',
    'BB Sran': 'Barinder Sran',
    'BC Lara': 'Brian Lara',
    'BE Hendricks': 'Beuran Hendricks',
    'BJ Rohrer': 'Ben Rohrer',
    'BK Kumar': 'Bhuvneshwar Kumar',
    'BR Dunk': 'Ben Dunk',
    'BR Sharath': 'BR Sharath',
    'BW Hilfenhaus': 'Ben Hilfenhaus',
    'C Munro': 'Colin Munro',
    'CA Lynn': 'Chris Lynn',
    'CJ Ferguson': 'Callum Ferguson',
    'CJ Green': 'Chris Green',
    'CJ McKay': 'Clint McKay',
    'CK Kapugedera': 'Chamara Kapugedera',
    'CK Langeveldt': 'Charl Langeveldt',
    'CL White': 'Cameron White',
    'CM Gautam': 'CM Gautam',
    'CR Brathwaite': 'Carlos Brathwaite',
    'CV Varun': 'Varun Chakaravarthy',
    'D Brevis': 'Dewald Brevis',
    'D Ferreira': 'Donovan Ferreira',
    'D Kalyankrishna': 'Doddapaneni Kalyankrishna',
    'D Madushanka': 'Dilshan Madushanka',
    'D Padikkal': 'Devdutt Padikkal',
    'D Pretorius': 'Dwaine Pretorius',
    'D Salunkhe': 'Dinesh Salunkhe',
    'D Wiese': 'David Wiese',
    'DA Miller': 'David Miller',
    'DAJ Bracewell': 'Doug Bracewell',
    'DB Das': 'Debabrata Das',
    'DB Ravi Teja': 'Dwaraka Ravi Teja',
    'DE Bollinger': 'Doug Bollinger',
    'DH Yagnik': 'Dishant Yagnik',
    'DJ Bravo': 'Dwayne Bravo',
    'DJ Harris': 'Daniel Harris',
    'DJ Hooda': 'Deepak Hooda',
    'DJ Hussey': 'David Hussey',
    'DJ Jacobs': 'Davy Jacobs',
    'DJ Malan': 'Dawid Malan',
    'DJ Thornely': 'Dominic Thornely',
    'DJ Willey': 'David Willey',
    'DJG Sammy': 'Darren Sammy',
    'DL Chahar': 'Deepak Chahar',
    'DL Vettori': 'Daniel Vettori',
    'DM Bravo': 'Darren Bravo',
    'DNT Zondo': 'Khaya Zondo',
    'DP Conway': 'Devon Conway',
    'DP Nannes': 'Dirk Nannes',
    'DPMD Jayawardene': 'Mahela Jayawardene',
    'DR Martyn': 'Damien Martyn',
    'DR Sams': 'Daniel Sams',
    'DR Smith': 'Dwayne Smith',
    'DS Kulkarni': 'Dhawal Kulkarni',
    'DS Lehmann': 'Darren Lehmann',
    'DT Christian': 'Dan Christian',
    'DT Patil': 'Dinesh Patil',
    'DW Steyn': 'Dale Steyn',
    'E Lewis': 'Evin Lewis',
    'EJG Morgan': 'Eoin Morgan',
    'F du Plessis': 'Faf du Plessis',
    'FA Allen': 'Fabian Allen',
    'FB Alam': 'Fawad Alam',
    'FH Allen': 'Finn Allen',
    'FH Edwards': 'Fidel Edwards',
    'FY Fazal': 'Faiz Fazal',
    'G Coetzee': 'Gerald Coetzee',
    'G Gambhir': 'Gautam Gambhir',
    'GC Smith': 'Graeme Smith',
    'GD Phillips': 'Glenn Phillips',
    'GH Vihari': 'Hanuma Vihari',
    'GHS Garton': 'George Garton',
    'GJ Bailey': 'George Bailey',
    'GJ Maxwell': 'Glenn Maxwell',
    'GR Napier': 'Graham Napier',
    'GS Sandhu': 'Gurinder Sandhu',
    'H Das': 'Halhadar Das',
    'H Klaasen': 'Heinrich Klaasen',
    'Harbhajan Singh': 'Harbhajan Singh',
    'Harmeet Singh': 'Harmeet Singh',
    'HC Brook': 'Harry Brook',
    'HE van der Dussen': 'Rassie van der Dussen',
    'HF Gurney': 'Harry Gurney',
    'HH Gibbs': 'Herschelle Gibbs',
    'HH Pandya': 'Hardik Pandya',
    'HM Amla': 'Hashim Amla',
    'HV Patel': 'Harshal Patel',
    'I Malhotra': 'Ishan Malhotra',
    'I Sharma': 'Ishant Sharma',
    'I Sodhi': 'Ish Sodhi',
    'I Tahir': 'Imran Tahir',
    'I Udana': 'Isuru Udana',
    'IC Pandey': 'Ishwar Pandey',
    'IK Pathan': 'Irfan Pathan',
    'IR Bell': 'Ian Bell',
    'IS Sodhi': 'Ish Sodhi',
    'J Arunkumar': 'Jagadeesh Arunkumar',
    'J Botha': 'Johan Botha',
    'J Charles': 'Johnson Charles',
    'J Fraser-McGurk': 'Jake Fraser-McGurk',
    'J Little': 'Joshua Little',
    'J Overton': 'Jamie Overton',
    'J Suchith': 'Jagadeesha Suchith',
    'J Syed Mohammad': 'Jamaluddin Syed Mohammad',
    'J Theron': 'Rusty Theron',
    'J Yadav': 'Jayant Yadav',
    'JA Morkel': 'Albie Morkel',
    'JA Richardson': 'Jhye Richardson',
    'JC Archer': 'Jofra Archer',
    'JC Buttler': 'Jos Buttler',
    'JD Ryder': 'Jesse Ryder',
    'JD Unadkat': 'Jaydev Unadkat',
    'JDP Oram': 'Jacob Oram',
    'JDS Neesham': 'Jimmy Neesham',
    'JE Root': 'Joe Root',
    'JE Taylor': 'Jerome Taylor',
    'JEC Duminy': 'JP Duminy',
    'JEC Franklin': 'James Franklin',
    'JH Kallis': 'Jacques Kallis',
    'JJ Bumrah': 'Jasprit Bumrah',
    'JJ Roy': 'Jason Roy',
    'JJ van der Wath': 'Johan van der Wath',
    'JL Denly': 'Joe Denly',
    'JL Pattinson': 'James Pattinson',
    'JM Bairstow': 'Jonny Bairstow',
    'JM Kemp': 'Justin Kemp',
    'JO Holder': 'Jason Holder',
    'JP Behrendorff': 'Jason Behrendorff',
    'JP Duminy': 'JP Duminy',
    'JP Faulkner': 'James Faulkner',
    'JR Hazlewood': 'Josh Hazlewood',
    'JR Hopes': 'James Hopes',
    'JW Dernbach': 'Jade Dernbach',
    'JW Hastings': 'John Hastings',
    'K Goel': 'Karan Goel',
    'K Gowtham': 'Krishnappa Gowtham',
    'K Kartikeya': 'Kumar Kartikeya',
    'K Maphaka': 'Kwena Maphaka',
    'K Rabada': 'Kagiso Rabada',
    'K Santokie': 'Krishmar Santokie',
    'K Upadhyay': 'Kshmal Upadhyay',
    'KA Jamieson': 'Kyle Jamieson',
    'KA Pollard': 'Kieron Pollard',
    'KA Roach': 'Kemar Roach',
    'KB Arun Karthik': 'Arun Karthik',
    'KC Cariappa': 'KC Cariappa',
    'KC Sangakkara': 'Kumar Sangakkara',
    'KD Karthik': 'Dinesh Karthik',
    'KD Mills': 'Kyle Mills',
    'KH Pandya': 'Krunal Pandya',
    'KJ Abbott': 'Kyle Abbott',
    'KK Ahmed': 'Khaleel Ahmed',
    'KK Cooper': 'Kevon Cooper',
    'KK Nair': 'Karun Nair',
    'KL Nagarkoti': 'Kamlesh Nagarkoti',
    'KL Rahul': 'KL Rahul',
    'KM Asif': 'KM Asif',
    'KM Jadhav': 'Kedar Jadhav',
    'KMA Paul': 'Keemo Paul',
    'KMDN Kulasekara': 'Nuwan Kulasekara',
    'KP Appanna': 'KP Appanna',
    'KP Pietersen': 'Kevin Pietersen',
    'KR Mayers': 'Kyle Mayers',
    'KS Bharat': 'KS Bharat',
    'KS Williamson': 'Kane Williamson',
    'KV Sharma': 'Karn Sharma',
    'KW Richardson': 'Kane Richardson',
    'Kuldeep Yadav': 'Kuldeep Yadav',
    'L Ablish': 'Love Ablish',
    'L Balaji': 'Lakshmipathy Balaji',
    'L Ngidi': 'Lungi Ngidi',
    'L Ronchi': 'Luke Ronchi',
    'L Wood': 'Luke Wood',
    'LA Carseldine': 'Lee Carseldine',
    'LA Pomersbach': 'Luke Pomersbach',
    'LE Plunkett': 'Liam Plunkett',
    'LH Ferguson': 'Lockie Ferguson',
    'LJ Wright': 'Luke Wright',
    'LMP Simmons': 'Lendl Simmons',
    'LPC Silva': 'Chamara Silva',
    'LR Shukla': 'Laxmi Ratan Shukla',
    'LRPL Taylor': 'Ross Taylor',
    'LS Livingstone': 'Liam Livingstone',
    'M Ashwin': 'Murugan Ashwin',
    'M Jansen': 'Marco Jansen',
    'M Kartik': 'Murali Kartik',
    'M Klinger': 'Michael Klinger',
    'M Manhas': 'Mithun Manhas',
    'M Morkel': 'Morne Morkel',
    'M Muralitharan': 'Muttiah Muralitharan',
    'M Ntini': 'Makhaya Ntini',
    'M Pathirana': 'Matheesha Pathirana',
    'M Prasidh Krishna': 'Prasidh Krishna',
    'M Rawat': 'Mahesh Rawat',
    'M Shahrukh Khan': 'Shahrukh Khan',
    'M Siddharth': 'Manimaran Siddharth',
    'M Theekshana': 'Maheesh Theekshana',
    'M Vijay': 'Murali Vijay',
    'M Vohra': 'Manan Vohra',
    'M de Lange': 'Marchant de Lange',
    'MA Agarwal': 'Mayank Agarwal',
    'MA Khote': 'Musavir Khote',
    'MA Starc': 'Mitchell Starc',
    'MA Wood': 'Mark Wood',
    'MC Henriques': 'Moises Henriques',
    'MC Juneja': 'Manpreet Juneja',
    'MD Mishra': 'Mohnish Mishra',
    'MDKJ Perera': 'Kusal Perera',
    'MEK Hussey': 'Michael Hussey',
    'MF Maharoof': 'Farveez Maharoof',
    'MG Bracewell': 'Michael Bracewell',
    'MG Johnson': 'Mitchell Johnson',
    'MJ Clarke': 'Michael Clarke',
    'MJ Guptill': 'Martin Guptill',
    'MJ Henry': 'Matt Henry',
    'MJ Lumb': 'Michael Lumb',
    'MJ McClenaghan': 'Mitchell McClenaghan',
    'MJ Santner': 'Mitchell Santner',
    'MK Pandey': 'Manish Pandey',
    'MK Tiwary': 'Manoj Tiwary',
    'ML Hayden': 'Matthew Hayden',
    'MM Ali': 'Moeen Ali',
    'MM Patel': 'Munaf Patel',
    'MN Samuels': 'Marlon Samuels',
    'MN van Wyk': 'Morne van Wyk',
    'MP Stoinis': 'Marcus Stoinis',
    'MR Marsh': 'Mitchell Marsh',
    'MS Bisla': 'Manvinder Bisla',
    'MS Dhoni': 'MS Dhoni',
    'MS Gony': 'Manpreet Gony',
    'MS Wade': 'Matthew Wade',
    'MV Boucher': 'Mark Boucher',
    'Mayank Dagar': 'Mayank Dagar',
    'Mohammad Asif': 'Mohammad Asif',
    'Mohammad Hafeez': 'Mohammad Hafeez',
    'Mohammad Nabi': 'Mohammad Nabi',
    'Mohammed Shami': 'Mohammed Shami',
    'Mohammed Siraj': 'Mohammed Siraj',
    'Mohit Sharma': 'Mohit Sharma',
    'Mujeeb Ur Rahman': 'Mujeeb Ur Rahman',
    'Mustafizur Rahman': 'Mustafizur Rahman',
    'N Burger': 'Nandre Burger',
    'N Pooran': 'Nicholas Pooran',
    'N Rana': 'Nitish Rana',
    'N Saini': 'Navdeep Saini',
    'N Thushara': 'Nuwan Thushara',
    'NA Saini': 'Navdeep Saini',
    'ND Doshi': 'Nayan Doshi',
    'NJ Maddinson': 'Nic Maddinson',
    'NL McCullum': 'Nathan McCullum',
    'NLTC Perera': 'Thisara Perera',
    'NM Coulter-Nile': 'Nathan Coulter-Nile',
    'NS Naik': 'Nikhil Naik',
    'NV Ojha': 'Naman Ojha',
    'NW Ellis': 'Nathan Ellis',
    'Naveen-ul-Haq': 'Naveen-ul-Haq',
    'Nitish Rana': 'Nitish Rana',
    'OA Shah': 'Owais Shah',
    'OC McCoy': 'Obed McCoy',
    'OF Smith': 'Odean Smith',
    'P Awana': 'Parvinder Awana',
    'P Chopra': 'Prashant Chopra',
    'P Dogra': 'Paras Dogra',
    'P Dubey': 'Pravin Dubey',
    'P Kumar': 'Praveen Kumar',
    'P Negi': 'Pawan Negi',
    'P Parameswaran': 'Prasanth Parameswaran',
    'P Ray Barman': 'Prayas Ray Barman',
    'P Sahu': 'Pardeep Sahu',
    'P Simran Singh': 'Prabhsimran Singh',
    'P Suyal': 'Pawan Suyal',
    'PA Patel': 'Parthiv Patel',
    'PA Reddy': 'Akshath Reddy',
    'PC Valthaty': 'Paul Valthaty',
    'PD Collingwood': 'Paul Collingwood',
    'PD Salt': 'Phil Salt',
    'PJ Cummins': 'Pat Cummins',
    'PJ Sangwan': 'Pradeep Sangwan',
    'PK Garg': 'Priyam Garg',
    'PM Siddle': 'Peter Siddle',
    'PN Mankad': 'Prerak Mankad',
    'PP Chawla': 'Piyush Chawla',
    'PP Ojha': 'Pragyan Ojha',
    'PR Shah': 'Pinal Shah',
    'PV Tambe': 'Pravin Tambe',
    'PVD Chameera': 'Dushmantha Chameera',
    'PWH de Silva': 'Wanindu Hasaranga',
    'Prabhsimran Singh': 'Prabhsimran Singh',
    'Prasidh Krishna': 'Prasidh Krishna',
    'Prithvi Shaw': 'Prithvi Shaw',
    'Q de Kock': 'Quinton de Kock',
    'R Ashwin': 'Ravichandran Ashwin',
    'R Bhatia': 'Rajat Bhatia',
    'R Bishnoi': 'Ravi Bishnoi',
    'R Dhawan': 'Rishi Dhawan',
    'R Dravid': 'Rahul Dravid',
    'R Gurbaz': 'Rahmanullah Gurbaz',
    'R McLaren': 'Ryan McLaren',
    'R Parag': 'Riyan Parag',
    'R Powell': 'Rovman Powell',
    'R Rampaul': 'Ravi Rampaul',
    'R Ravindra': 'Rachin Ravindra',
    'R Sanjay Yadav': 'Sanjay Yadav',
    'R Sharma': 'Rahul Sharma',
    'R Shepherd': 'Romario Shepherd',
    'R Shukla': 'Rahul Shukla',
    'R Tewatia': 'Rahul Tewatia',
    'R Vinay Kumar': 'Vinay Kumar',
    'RA Bawa': 'Raj Bawa',
    'RA Jadeja': 'Ravindra Jadeja',
    'RA Tripathi': 'Rahul Tripathi',
    'RD Chahar': 'Rahul Chahar',
    'RD Gaikwad': 'Ruturaj Gaikwad',
    'RD Rickelton': 'Ryan Rickelton',
    'RE Levi': 'Richard Levi',
    'RE van der Merwe': 'Roelof van der Merwe',
    'RG More': 'Ronit More',
    'RG Sharma': 'Rohit Sharma',
    'RJ Gleeson': 'Richard Gleeson',
    'RJ Harris': 'Ryan Harris',
    'RJ Peterson': 'Robin Peterson',
    'RJW Topley': 'Reece Topley',
    'RK Bhui': 'Ricky Bhui',
    'RK Singh': 'Rinku Singh',
    'RM Patidar': 'Rajat Patidar',
    'RN ten Doeschate': 'Ryan ten Doeschate',
    'RP Meredith': 'Riley Meredith',
    'RP Singh': 'RP Singh',
    'RR Bhatkal': 'Raju Bhatkal',
    'RR Pant': 'Rishabh Pant',
    'RR Powar': 'Ramesh Powar',
    'RR Raje': 'Rohan Raje',
    'RR Rossouw': 'Rilee Rossouw',
    'RR Sarwan': 'Ramnaresh Sarwan',
    'RS Bopara': 'Ravi Bopara',
    'RS Gavaskar': 'Rohan Gavaskar',
    'RS Hangargekar': 'Rajvardhan Hangargekar',
    'RT Ponting': 'Ricky Ponting',
    'RV Gomez': 'Raiphi Gomez',
    'RV Patel': 'Ripal Patel',
    'RV Uthappa': 'Robin Uthappa',
    'RW Price': 'Ray Price',
    'Rahul Chahar': 'Rahul Chahar',
    'Rahul Tewatia': 'Rahul Tewatia',
    'Rahul Tripathi': 'Rahul Tripathi',
    'Rajat Patidar': 'Rajat Patidar',
    'Rashid Khan': 'Rashid Khan',
    'Ravi Bishnoi': 'Ravi Bishnoi',
    'Rinku Singh': 'Rinku Singh',
    'Riyan Parag': 'Riyan Parag',
    'Rohit Sharma': 'Rohit Sharma',
    'Ruturaj Gaikwad': 'Ruturaj Gaikwad',
    'S Anirudha': 'Anirudha Srikkanth',
    'S Aravind': 'Sreenath Aravind',
    'S Badree': 'Samuel Badree',
    'S Badrinath': 'Subramaniam Badrinath',
    'S Chanderpaul': 'Shivnarine Chanderpaul',
    'S Dhawan': 'Shikhar Dhawan',
    'S Dube': 'Shivam Dube',
    'S Gopal': 'Shreyas Gopal',
    'S Joseph': 'Shamar Joseph',
    'S Kaul': 'Siddharth Kaul',
    'S Ladda': 'Sarabjit Ladda',
    'S Lamichhane': 'Sandeep Lamichhane',
    'S Midhun': 'S Midhun',
    'S Nadeem': 'Shahbaz Nadeem',
    'S Narwal': 'Sumit Narwal',
    'S Rana': 'Sachin Rana',
    'S Randiv': 'Suraj Randiv',
    'S Rutherford': 'Sherfane Rutherford',
    'S Sandeep Warrier': 'Sandeep Warrier',
    'S Sohal': 'Sunny Sohal',
    'S Sreesanth': 'Sreesanth',
    'S Sriram': 'Sridharan Sriram',
    'S Tyagi': 'Sudeep Tyagi',
    'S Vidyut': 'Sivaramakrishnan Vidyut',
    'SA Abbott': 'Sean Abbott',
    'SA Yadav': 'Suryakumar Yadav',
    'SB Bangar': 'Sanjay Bangar',
    'SB Jakati': 'Shadab Jakati',
    'SB Joshi': 'Sunil Joshi',
    'SB Styris': 'Scott Styris',
    'SC Ganguly': 'Sourav Ganguly',
    'SC Kuggeleijn': 'Scott Kuggeleijn',
    'SD Chitnis': 'Siddhesh Chitnis',
    'SD Hope': 'Shai Hope',
    'SE Bond': 'Shane Bond',
    'SE Marsh': 'Shaun Marsh',
    'SE Rutherford': 'Sherfane Rutherford',
    'SG Bhati': 'Subhranshu Senapati',
    'SH Johnson': 'Spencer Johnson',
    'SI Mahmood': 'Sajid Mahmood',
    'SJ Srivastava': 'Shalabh Srivastava',
    'SK Raina': 'Suresh Raina',
    'SK Trivedi': 'Siddharth Trivedi',
    'SK Warne': 'Shane Warne',
    'SL Malinga': 'Lasith Malinga',
    'SM Curran': 'Sam Curran',
    'SM Harwood': 'Shane Harwood',
    'SM Katich': 'Simon Katich',
    'SM Pollock': 'Shaun Pollock',
    'SMSM Senanayake': 'Sachithra Senanayake',
    'SN Khan': 'Sarfaraz Khan',
    'SN Thakur': 'Shardul Thakur',
    'SO Hetmyer': 'Shimron Hetmyer',
    'SP Fleming': 'Stephen Fleming',
    'SP Goswami': 'Shreevats Goswami',
    'SP Jackson': 'Sheldon Jackson',
    'SP Narine': 'Sunil Narine',
    'SPD Smith': 'Steve Smith',
    'SR Tendulkar': 'Sachin Tendulkar',
    'SR Watson': 'Shane Watson',
    'SS Cottrell': 'Sheldon Cottrell',
    'SS Iyer': 'Shreyas Iyer',
    'SS Tiwary': 'Saurabh Tiwary',
    'ST Jayasuriya': 'Sanath Jayasuriya',
    'STR Binny': 'Stuart Binny',
    'SV Samson': 'Sanju Samson',
    'SW Billings': 'Sam Billings',
    'SW Tait': 'Shaun Tait',
    'Sachin Tendulkar': 'Sachin Tendulkar',
    'Sai Sudharsan': 'Sai Sudharsan',
    'Sameer Rizvi': 'Sameer Rizvi',
    'Sandeep Sharma': 'Sandeep Sharma',
    'Sanju Samson': 'Sanju Samson',
    'Shahbaz Ahmed': 'Shahbaz Ahmed',
    'Shahid Afridi': 'Shahid Afridi',
    'Shakib Al Hasan': 'Shakib Al Hasan',
    'Shivam Dube': 'Shivam Dube',
    'Shoaib Akhtar': 'Shoaib Akhtar',
    'Shreyas Gopal': 'Shreyas Gopal',
    'Shreyas Iyer': 'Shreyas Iyer',
    'Shubman Gill': 'Shubman Gill',
    'Sikandar Raza': 'Sikandar Raza',
    'Simarjeet Singh': 'Simarjeet Singh',
    'Sohail Tanvir': 'Sohail Tanvir',
    'Sunil Narine': 'Sunil Narine',
    'Suresh Raina': 'Suresh Raina',
    'Suryakumar Yadav': 'Suryakumar Yadav',
    'Suyash Sharma': 'Suyash Sharma',
    'Swapnil Singh': 'Swapnil Singh',
    'T Banton': 'Tom Banton',
    'T Henderson': 'Tyron Henderson',
    'T Kohler-Cadmore': 'Tom Kohler-Cadmore',
    'T Natarajan': 'T Natarajan',
    'T Shamsi': 'Tabraiz Shamsi',
    'T Stubbs': 'Tristan Stubbs',
    'T Taibu': 'Tatenda Taibu',
    'T Thushara': 'Thilan Thushara',
    'TA Boult': 'Trent Boult',
    'TD Paine': 'Tim Paine',
    'TG Southee': 'Tim Southee',
    'TH David': 'Tim David',
    'TK Curran': 'Tom Curran',
    'TL Suman': 'Tirumalasetti Suman',
    'TM Dilshan': 'Tillakaratne Dilshan',
    'TM Head': 'Travis Head',
    'TR Birt': 'Travis Birt',
    'TS Mills': 'Tymal Mills',
    'UT Yadav': 'Umesh Yadav',
    'Umar Gul': 'Umar Gul',
    'Umran Malik': 'Umran Malik',
    'V Kohli': 'Virat Kohli',
    'V Pratap Singh': 'Veer Pratap Singh',
    'V Sehwag': 'Virender Sehwag',
    'V Shankar': 'Vijay Shankar',
    'VR Aaron': 'Varun Aaron',
    'VRV Singh': 'VRV Singh',
    'VS Malik': 'Vikramjeet Malik',
    'VVS Laxman': 'VVS Laxman',
    'Vaibhav Arora': 'Vaibhav Arora',
    'Varun Chakaravarthy': 'Varun Chakaravarthy',
    'Venkatesh Iyer': 'Venkatesh Iyer',
    'Vijay Shankar': 'Vijay Shankar',
    'Virender Sehwag': 'Virender Sehwag',
    'Virat Kohli': 'Virat Kohli',
    'Vishnu Vinod': 'Vishnu Vinod',
    'W Jaffer': 'Wasim Jaffer',
    'WA Mota': 'Wilkin Mota',
    'WD Parnell': 'Wayne Parnell',
    'WG Jacks': 'Will Jacks',
    'WP Saha': 'Wriddhiman Saha',
    'WPUJC Vaas': 'Chaminda Vaas',
    'Washington Sundar': 'Washington Sundar',
    'Y Nagar': 'Yogesh Nagar',
    'Y Prithvi Raj': 'Yarra Prithvi Raj',
    'Y Venugopal Rao': 'Yalaka Venugopal Rao',
    'YA Abdulla': 'Yusuf Abdulla',
    'YBK Jaiswal': 'Yashasvi Jaiswal',
    'YK Pathan': 'Yusuf Pathan',
    'YS Chahal': 'Yuzvendra Chahal',
    'Yash Dayal': 'Yash Dayal',
    'Yashasvi Jaiswal': 'Yashasvi Jaiswal',
    'Yudhvir Singh': 'Yudhvir Singh',
    'Yuvraj Singh': 'Yuvraj Singh',
    'Z Khan': 'Zaheer Khan'
}

LEGEND_ALIASES = PLAYER_FULL_NAME_MAP

def get_player_full_name(player_code):
    return PLAYER_FULL_NAME_MAP.get(player_code, player_code)

def get_player_search_label(player_code):
    full = PLAYER_FULL_NAME_MAP.get(player_code, player_code)
    if full != player_code:
        return f"{full} ({player_code})"
    return player_code

MARQUEE_SEARCH_PRIORITY = {
    'V Kohli': 100, 'RG Sharma': 99, 'MS Dhoni': 98, 'JJ Bumrah': 97,
    'AB de Villiers': 96, 'CH Gayle': 95, 'DA Warner': 94, 'SK Raina': 93,
    'RA Jadeja': 92, 'KL Rahul': 91, 'RR Pant': 90, 'HH Pandya': 89,
    'SL Malinga': 88, 'SP Narine': 87, 'YS Chahal': 86, 'Rashid Khan': 85,
    'A Flintoff': 84, 'A Ashish Reddy': 80
}

def fuzzy_search_players(query, options, cutoff=0.48):
    """
    Intelligent fuzzy player search:
    - Handles case-insensitivity, partial matching, first/last names.
    - Highly tolerant to typos (e.g. 'kholi' -> Virat Kohli, 'sharama' -> Rohit Sharma, 
      'bumra' -> Jasprit Bumrah, 'flintof' -> Andrew Flintoff, 'dhony' -> MS Dhoni, etc.).
    - Preserves best-ranked matches at the top.
    """
    query = query.strip().lower()
    if not query:
        return sorted(options)
    
    q_tokens = [tok for tok in query.replace('-', ' ').replace('.', ' ').split() if tok]
    if not q_tokens:
        return sorted(options)
    
    # Tier 1: Substring match on ALL tokens (e.g. 'virat kohli', 'v kohli', 'rohit')
    exact_all = [opt for opt in options if all(tok in opt.lower() for tok in q_tokens)]
    if exact_all:
        def exact_rank(opt):
            opt_clean = opt.lower().replace('(', ' ').replace(')', ' ')
            words = opt_clean.split()
            word_match_count = sum(1 for tok in q_tokens if tok in words)
            starts_with = 1 if any(words and words[0].startswith(tok) for tok in q_tokens) else 0
            marquee_b = 0
            for code, p_rank in MARQUEE_SEARCH_PRIORITY.items():
                if f'({code})' in opt or opt == code or PLAYER_FULL_NAME_MAP.get(code, '') in opt:
                    marquee_b = p_rank
                    break
            return (word_match_count, starts_with, marquee_b, -len(opt))
            
        exact_all.sort(key=exact_rank, reverse=True)
        return exact_all

    # Tier 2: Token-by-token fuzzy ratio
    scored = []
    for opt in options:
        opt_clean = opt.lower().replace('(', ' ').replace(')', ' ').replace('-', ' ')
        opt_words = [w for w in opt_clean.split() if w]
        
        tok_scores = []
        for q_tok in q_tokens:
            best_tok_score = 0.0
            for w in opt_words:
                r = difflib.SequenceMatcher(None, q_tok, w).ratio()
                if (len(q_tok) >= 3 and q_tok in w) or (len(w) >= 3 and w in q_tok):
                    r = max(r, 0.88)
                if r > best_tok_score:
                    best_tok_score = r
            tok_scores.append(best_tok_score)
            
        full_r = difflib.SequenceMatcher(None, query, opt_clean).ratio()
        avg_tok_score = sum(tok_scores) / len(tok_scores) if tok_scores else 0
        overall_score = max(avg_tok_score, full_r)
        
        if any(len(tok) >= 3 and tok in opt_clean for tok in q_tokens):
            overall_score = max(overall_score, 0.75)
            
        if overall_score >= cutoff:
            marquee_tiebreaker = 0.0
            for code, p_rank in MARQUEE_SEARCH_PRIORITY.items():
                if f'({code})' in opt or opt == code:
                    marquee_tiebreaker = p_rank * 0.001
                    break
            scored.append((opt, overall_score + marquee_tiebreaker))
            
    scored.sort(key=lambda x: x[1], reverse=True)
    if scored:
        return [x[0] for x in scored[:40]]
        
    closest = difflib.get_close_matches(query, options, n=20, cutoff=0.30)
    return closest if closest else sorted(options)

def clean_tok(s):
    return re.sub(r'[^a-zA-Z0-9]', '', str(s)).lower()

USER_PLAYER_DATASET_PATHS = {}
players_dir = '/home/tejas/ipl/players'
if os.path.exists(players_dir):
    for root, dirs, files in os.walk(players_dir):
        for f in files:
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                full_path = os.path.join(root, f)
                base = os.path.splitext(f)[0]
                if base.lower().endswith(('.jpeg', '.jpg', '.png')):
                    base = os.path.splitext(base)[0]
                parts = base.split('_')
                if len(parts) >= 2 and len(parts[-1]) <= 6:
                    raw_name = ' '.join(parts[:-1])
                else:
                    raw_name = ' '.join(parts)
                c_tok = clean_tok(raw_name)
                USER_PLAYER_DATASET_PATHS[raw_name.lower()] = full_path
                USER_PLAYER_DATASET_PATHS[c_tok] = full_path
                USER_PLAYER_DATASET_PATHS[base.lower()] = full_path

def find_user_dataset_image(player_name):
    name_to_check = LEGEND_ALIASES.get(player_name, player_name)
    c_tok = clean_tok(name_to_check)
    if c_tok in USER_PLAYER_DATASET_PATHS:
        return USER_PLAYER_DATASET_PATHS[c_tok]
    if name_to_check.lower() in USER_PLAYER_DATASET_PATHS:
        return USER_PLAYER_DATASET_PATHS[name_to_check.lower()]
    orig_tok = clean_tok(player_name)
    if orig_tok in USER_PLAYER_DATASET_PATHS:
        return USER_PLAYER_DATASET_PATHS[orig_tok]
    parts = name_to_check.split()
    if len(parts) >= 2:
        last = parts[-1].lower()
        init = parts[0][0].lower()
        for k, path in USER_PLAYER_DATASET_PATHS.items():
            k_parts = k.split()
            if len(k_parts) >= 2 and k_parts[-1] == last and k_parts[0].startswith(init):
                return path
    return None

@st.cache_data(ttl=86400)
def get_player_image_and_bio(player_name, team_name='IPL'):
    # Tier 0: User's Curated 423-Player Dataset in Authentic Team Jerseys (Top Priority)
    user_img_path = find_user_dataset_image(player_name)
    if user_img_path:
        b64 = get_base64_image(user_img_path)
        if b64:
            return b64, ""

    # Tier 1: Local Curated Wallpapers & Photos in IMAGE/
    if player_name in LOCAL_PLAYER_IMAGES and LOCAL_PLAYER_IMAGES[player_name]:
        return LOCAL_PLAYER_IMAGES[player_name], ""
    clean_p = player_name.replace(' ', '_')
    for ext in ['.jpg', '.jpeg', '.png']:
        cand = f"/home/tejas/ipl/IMAGE /{clean_p}{ext}"
        if os.path.exists(cand):
            b64 = get_base64_image(cand)
            if b64: return b64, ""
        
    # Tier 2: Wikipedia REST API with STRICT Cricket Verification
    wiki_slug = PLAYER_WIKI_MAP.get(player_name)
    if not wiki_slug:
        parts = player_name.split()
        if len(parts) == 2 and len(parts[0]) > 2:
            wiki_slug = player_name.replace(' ', '_')
            
    if wiki_slug:
        try:
            headers = {'User-Agent': 'IPLAnalyticsDashboard/2.0 (contact: tejas.ingle@example.com)'}
            url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_slug}'
            r = requests.get(url, headers=headers, timeout=3)
            if r.status_code == 200:
                data = r.json()
                desc = data.get('description', '')
                extract = data.get('extract', '')
                thumb = data.get('thumbnail', {}).get('source')
                
                # CRITICAL VERIFICATION: Must explicitly be verified as a cricketer
                full_text = (desc + ' ' + extract).lower()
                is_cricketer = any(kw in full_text for kw in ['cricket', 'cricketer', 'batsman', 'bowler', 'ipl', 'wicket-keeper', 'all-rounder'])
                
                if is_cricketer and thumb:
                    return thumb, extract
        except Exception:
            pass
            
    # Tier 3: Custom SVG Team Jersey Avatar (Guaranteed Authentic Identity)
    svg_avatar = generate_player_avatar_svg(player_name, team_name)
    return svg_avatar, ""

def fetch_wiki_data(query, is_player=False):
    if is_player:
        return get_player_image_and_bio(query)
    try:
        headers = {'User-Agent': 'IPLAnalyticsDashboard/2.0 (contact: tejas.ingle@example.com)'}
        slug = query.split(',')[0].strip().replace(' ', '_')
        url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{slug}'
        r = requests.get(url, headers=headers, timeout=3)
        if r.status_code == 200:
            d = r.json()
            return d.get('thumbnail', {}).get('source', ''), d.get('extract', '')
    except Exception:
        pass
    return '', 

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
            # Deccan Chargers is kept distinct as 2009 Champion franchise (SRH = 2016)
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
        color_discrete_sequence=['#f59e0b', '#38bdf8', '#10b981', '#f472b6', '#a855f7'] if not is_team_col else None,
        text_auto=text_format
    )
    fig.update_layout(
        font={'family': 'Outfit, sans-serif', 'color': '#f8fafc'},
        title={'font': {'size': 18, 'family': 'Outfit, sans-serif', 'color': '#ffffff'}},
        xaxis_title=x.replace('_', ' ').title(), 
        yaxis_title=y.replace('_', ' ').title(),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        hoverlabel={'bgcolor': '#090e18', 'bordercolor': '#f59e0b', 'font': {'family': 'Outfit, sans-serif', 'color': '#ffffff'}},
        margin=dict(t=50, b=40, l=40, r=40),
        transition={'duration': 400, 'easing': 'cubic-in-out'}
    )
    fig.update_xaxes(showgrid=False, linecolor='rgba(255,255,255,0.1)', tickfont={'size': 11, 'color': '#94a3b8'})
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.06)', linecolor='rgba(255,255,255,0.1)', tickfont={'size': 11, 'color': '#94a3b8'})
    fig.update_traces(textposition='outside', marker_line_width=0, opacity=0.92)
    return fig


# ==========================================
# 🧭 SIDEBAR NAVIGATION
# ==========================================
sidebar_logo_src = IPL_LOGO_BASE64 or "https://documents.iplt20.com/ipl/assets/images/ipl-logo-new-old.png"
st.sidebar.markdown(
    f"""
    <div style="text-align: center; padding: 10px 0 15px 0;">
        <img src="{sidebar_logo_src}" width="130" style="filter: drop-shadow(0 4px 12px rgba(245, 158, 11, 0.3));">
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
    
    # Display Trophy Showcase Cards in a unified, equal-height responsive grid
    all_trophy_cards = []
    for idx, row in title_tally.iterrows():
        team_n = row['Team']
        titles_n = row['Titles Won']
        team_seasons = season_finals[season_finals['winner'] == team_n]['season'].tolist()
        seasons_str = ", ".join([str(s) for s in team_seasons])
        logo_img = get_team_logo_base64(team_n)
        team_color = IPL_TEAM_COLORS.get(team_n, '#f59e0b')
        t_card = f"""
        <div class="trophy-card" style="border-top: 3px solid {team_color};">
            <div class="trophy-count-pill" style="box-shadow: 0 3px 12px {team_color}88;">🏆 x{titles_n}</div>
            <div style="width: 58px; height: 58px; margin: 4px auto 6px auto; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <img src="{logo_img}" style="max-width: 100%; max-height: 100%; object-fit: contain; filter: drop-shadow(0 4px 10px {team_color}66);">
            </div>
            <div style="font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 13.5px; color: #fff; line-height: 1.25; min-height: 38px; display: flex; align-items: center; justify-content: center; text-align: center; width: 100%;">{team_n}</div>
            <div style="font-size: 11px; font-weight: 600; color: #fbbf24; letter-spacing: 0.3px; line-height: 1.35; min-height: 34px; display: flex; align-items: center; justify-content: center; text-align: center; width: 100%;">{seasons_str}</div>
        </div>
        """
        all_trophy_cards.append(t_card)
        
    grid_html = f'<div class="trophy-grid">{"".join(all_trophy_cards)}</div>'
    render_html(grid_html)
            
    # Chart with exact franchise branding colors
    fig_champs = plot_plotly_bar(title_tally, 'Team', 'Titles Won', "IPL Championship Titles Won (All-Time)")
    st.plotly_chart(fig_champs, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
    
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
        st.plotly_chart(fig_runs, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
        
    with w_col:
        fig_wkts = px.bar(wickets_per_season, x='season', y='wickets', text='wickets', title="Wickets Taken per Season", color_discrete_sequence=['#38bdf8'])
        fig_wkts.update_traces(textposition='outside')
        fig_wkts.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Wickets")
        st.plotly_chart(fig_wkts, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})


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
    st.plotly_chart(fig_all_wins, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})


# ==========================================
# ⭐ PAGE 3: PLAYER ANALYSIS
# ==========================================
elif page == "Player Analysis":
    st.title("⭐ Individual Mastery & Bat/Ball Contenders")
    
    t1, t2, t3 = st.tabs(["🏏 Batting Leaders", "🎯 Bowling Leaders", "🧤 Safe Hands (Fielding)"])
    
    with t1:
        st.header("Top Run Scorers (Orange Cap Titans)")
        batsman_stats = deliveries.groupby('batsman')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False)
        st.plotly_chart(plot_plotly_bar(batsman_stats.head(10), 'batsman', 'batsman_runs', 'All-Time Highest Run Scorers in IPL History'), use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
        
    with t2:
        st.header("Top Wicket Takers (Purple Cap Kings)")
        bowler_stats = deliveries.dropna(subset=['player_dismissed'])
        bowler_stats = bowler_stats[bowler_stats['dismissal_kind'] != 'run out']
        wickets_df = bowler_stats.groupby('bowler').size().reset_index(name='wickets').sort_values('wickets', ascending=False)
        st.plotly_chart(plot_plotly_bar(wickets_df.head(10), 'bowler', 'wickets', 'All-Time Highest Wicket Takers in IPL History'), use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
        
    with t3:
        st.header("Most Catches (Elite Fielders)")
        catches_df = deliveries[deliveries['dismissal_kind'] == 'caught'].groupby('fielder').size().reset_index(name='catches').sort_values('catches', ascending=False)
        st.plotly_chart(plot_plotly_bar(catches_df.head(10), 'fielder', 'catches', 'All-Time Most Catches by Fielders'), use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})


# ==========================================
# 🃏 PAGE 4: PLAYER PROFILE & ELITE SCORECARD
# ==========================================
elif page == "Player Profile (FIFA Card)":
    st.title("🃏 Premier Player Profile & Career Dossier")
    st.markdown("Ultimate Team T20 card paired with a complete, comprehensive match scorecard dossier.")
    
    all_players = pd.concat([deliveries['batsman'], deliveries['bowler']]).dropna().unique()
    sorted_players = sorted(all_players)
    
    # 🔍 Full Name & Surname Smart Search Registry
    display_to_raw = {}
    for p_code in sorted_players:
        disp_label = get_player_search_label(p_code)
        display_to_raw[disp_label] = p_code

    col_search, col_dropdown = st.columns([1, 1.2], gap="medium")
    with col_search:
        search_kw = st.text_input(
            "🔍 Search Player",
            placeholder="Type player name, surname, or typo (e.g. kholi, boomrah, flintof)...",
            key="p_search_keyword"
        ).strip()

    if search_kw:
        filtered_options = fuzzy_search_players(search_kw, list(display_to_raw.keys()))
        if not filtered_options or filtered_options == sorted(list(display_to_raw.keys())):
            st.info(f"💡 No direct match for '{search_kw}'. Browse from all players:")
            filtered_options = sorted(list(display_to_raw.keys()))
    else:
        filtered_options = sorted(list(display_to_raw.keys()))

    # Sync with session state
    curr_raw = st.session_state.get('selected_player_code', 'V Kohli')
    curr_disp = get_player_search_label(curr_raw)
    default_sel_idx = 0
    if search_kw and filtered_options:
        # User entered a query, prioritize the top closest match immediately!
        default_sel_idx = 0
    elif curr_disp in filtered_options:
        default_sel_idx = filtered_options.index(curr_disp)

    with col_dropdown:
        chosen_label = st.selectbox(
            "Search & Inspect Player",
            filtered_options,
            index=default_sel_idx,
            help="Type first name, surname, or IPL short code to inspect player career dossier."
        )
        player = display_to_raw.get(chosen_label, curr_raw)
        st.session_state['selected_player_code'] = player
    
    # 1. Batting Metrics
    b_df = deliveries[deliveries['batsman'] == player]
    runs = b_df['batsman_runs'].sum()
    balls_faced = b_df.shape[0] - (b_df['extras_type'] == 'wides').sum() if 'extras_type' in b_df.columns else b_df.shape[0]
    sr = round((runs / balls_faced) * 100, 2) if balls_faced > 0 else 0
    outs = deliveries[deliveries['player_dismissed'] == player].shape[0]
    avg = round(runs / outs, 2) if outs > 0 else runs
    
    # Milestones
    match_runs = b_df.groupby('match_id')['batsman_runs'].sum()
    hs = int(match_runs.max()) if not match_runs.empty else 0
    fifties = int(((match_runs >= 50) & (match_runs < 100)).sum())
    hundreds = int((match_runs >= 100).sum())
    fours = int((b_df['batsman_runs'] == 4).sum())
    sixes = int((b_df['batsman_runs'] == 6).sum())
    boundary_runs = (fours * 4) + (sixes * 6)
    boundary_pct = round((boundary_runs / runs * 100), 1) if runs > 0 else 0
    innings_batted = b_df['match_id'].nunique()
    
    # 2. Bowling Metrics
    bowl_df = deliveries[deliveries['bowler'] == player]
    w_df_p = bowl_df.dropna(subset=['player_dismissed'])
    wickets = w_df_p[w_df_p['dismissal_kind'] != 'run out'].shape[0]
    
    runs_conceded = bowl_df['total_runs'].sum() - (bowl_df[bowl_df['extras_type'] == 'legbyes']['total_runs'].sum() if 'extras_type' in bowl_df.columns else 0)
    balls_bowled = bowl_df.shape[0]
    eco = round((runs_conceded / balls_bowled) * 6, 2) if balls_bowled > 0 else 0
    catches = deliveries[(deliveries['fielder'] == player) & (deliveries['dismissal_kind'] == 'caught')].shape[0]
    innings_bowled = bowl_df['match_id'].nunique()
    
    # Best Bowling Figures
    if wickets > 0:
        wkts_pm = w_df_p[w_df_p['dismissal_kind'] != 'run out'].groupby('match_id').size().rename('wkts')
        runs_pm = bowl_df.groupby('match_id')['total_runs'].sum().rename('runs')
        m_bowl = pd.concat([wkts_pm, runs_pm], axis=1).fillna({'wkts': 0})
        best_b = m_bowl.sort_values(by=['wkts', 'runs'], ascending=[False, True]).iloc[0]
        bbf_str = f"{int(best_b['wkts'])}/{int(best_b['runs'])}"
    else:
        bbf_str = "-"
    best_bowl_str = bbf_str
        
    # Player of the match awards
    pom_count = (matches['player_of_match'] == player).sum()
    
    # Primary Franchise
    p_teams = deliveries[deliveries['batsman'] == player]['batting_team'].value_counts()
    if p_teams.empty:
        p_teams = deliveries[deliveries['bowler'] == player]['bowling_team'].value_counts()
    primary_team = p_teams.index[0] if not p_teams.empty else "IPL Legend"
    
    # Context-Aware Granular Cricket Role
    detailed_role = get_player_role(player, b_df, bowl_df, deliveries)
    if 'WK' in detailed_role or 'WICKETKEEPER' in detailed_role or 'KEEPER' in detailed_role:
        pos_badge = "WK-BATTER"
    elif 'ALL-ROUNDER' in detailed_role:
        pos_badge = "ALL-ROUNDER"
    elif 'PACER' in detailed_role or 'FAST BOWLER' in detailed_role:
        pos_badge = "PACER"
    elif 'SPIN' in detailed_role or 'SPINNER' in detailed_role:
        pos_badge = "SPINNER"
    elif 'BOWLER' in detailed_role:
        pos_badge = "BOWLER"
    elif 'OPENER' in detailed_role or 'TOP-ORDER' in detailed_role:
        pos_badge = "OPENER"
    elif 'FINISHER' in detailed_role:
        pos_badge = "FINISHER"
    else:
        pos_badge = "BATTER"
        
    # Calibrated Authentic Overall Rating (64 to 97)
    legends_benchmark = {
        'V Kohli': 96, 'MS Dhoni': 95, 'RG Sharma': 94, 'AB de Villiers': 96,
        'CH Gayle': 95, 'SK Raina': 94, 'DA Warner': 95, 'SL Malinga': 96,
        'JJ Bumrah': 96, 'SP Narine': 95, 'Rashid Khan': 95, 'AD Russell': 94,
        'KL Rahul': 92, 'B Kumar': 91, 'YS Chahal': 92, 'RA Jadeja': 93
    }
    
    if player in legends_benchmark:
        overall = legends_benchmark[player]
    else:
        # Batting scale
        if runs >= 5000:
            bat_r = 89 + (min(runs - 5000, 4500) / 4500) * 6
        elif runs >= 3000:
            bat_r = 83 + ((runs - 3000) / 2000) * 6
        elif runs >= 1500:
            bat_r = 76 + ((runs - 1500) / 1500) * 7
        elif runs >= 500:
            bat_r = 69 + ((runs - 500) / 1000) * 7
        else:
            bat_r = 62 + (runs / 500) * 7
        
        if runs >= 300:
            if sr >= 150: bat_r += 2
            elif sr <= 110: bat_r -= 2
            if avg >= 36: bat_r += 2
            elif avg <= 20: bat_r -= 2

        # Bowling scale
        if wickets >= 150:
            bowl_r = 89 + (min(wickets - 150, 60) / 60) * 6
        elif wickets >= 90:
            bowl_r = 83 + ((wickets - 90) / 60) * 7
        elif wickets >= 45:
            bowl_r = 76 + ((wickets - 45) / 45) * 7
        elif wickets >= 20:
            bowl_r = 69 + ((wickets - 20) / 25) * 7
        else:
            bowl_r = 62 + (wickets / 20) * 7
            
        if wickets >= 15:
            if eco <= 7.2: bowl_r += 2
            elif eco >= 9.2: bowl_r -= 2

        if pos_badge in ['BATTER', 'OPENER', 'FINISHER', 'WK-BATTER']:
            overall = int(round(bat_r))
        elif pos_badge in ['BOWLER', 'PACER', 'SPINNER']:
            overall = int(round(bowl_r))
        else: # ALL-ROUNDER
            overall = int(round(max(bat_r, bowl_r) * 0.65 + min(bat_r, bowl_r) * 0.35 + 2))
            
        overall = min(96, max(64, overall))
    
    # Tier classification & authentic country flag from analysis
    tier_meta = get_player_tier_and_meta(player, runs, wickets, overall, matches, deliveries)
    country_flag = get_player_country_flag(player)
    
    # 6 Authentic FIFA Attributes calculated from match dataset
    fifa_bat = min(99, max(35, int((avg * 1.05) + (sr * 0.35)))) if runs > 100 else 35
    fifa_bow = min(99, max(30, int((wickets * 0.45) + max(0, (11 - eco)) * 5.0))) if balls_bowled >= 60 else 30
    fifa_pac = 92 if ('PACER' in detailed_role or 'FAST' in detailed_role) else (78 if 'SPIN' in detailed_role else (88 if boundary_pct > 60 else 84))
    fifa_ref = min(98, max(70, 80 + int(catches * 0.22) + (5 if 'WK' in detailed_role else 0)))
    fifa_cat = min(98, max(65, 75 + int(catches * 0.25)))
    fifa_thr = 88 if ('OPENER' in detailed_role or 'ALL-ROUNDER' in detailed_role) else 85
    short_name = player.split()[-1].upper()
    
    # Bulletproof Multi-Tier Image Resolver
    img_url, wiki_bio = get_player_image_and_bio(player, primary_team)
    
    # 2-COLUMN LUXURY LAYOUT: 3D FLIP CARD ON LEFT, DOSSIER ON RIGHT
    col_card, col_dossier = st.columns([1, 1.4], gap="large")
    
    with col_card:
        player_chk_id = f"fifaFlip_{abs(hash(player)) % 1000000}"
        
        # Primary Metric Logic for Back Face based on player's true role
        is_bowler_metric = (pos_badge in ["BOWLER", "PACER", "SPINNER"]) or (
            pos_badge == "ALL-ROUNDER" and (wickets >= 40 and runs < 600)
        ) or (runs < 200 and wickets >= 15)

        if is_bowler_metric:
            primary_metric_val = int(wickets)
            primary_metric_lbl = "CAREER WICKETS"
            avg_bowl = round(runs_conceded / wickets, 1) if wickets > 0 else 0.0
            primary_sub_stat = f"ECON {eco:.2f} &bull; {avg_bowl} AVG"
            stat_item_1 = f"🏏 Runs: <strong>{int(runs)}</strong>"
            stat_item_2 = f"🎯 BBF: <strong>{bbf_str}</strong>"
            stat_item_3 = f"⚡ Econ: <strong>{eco:.2f}</strong>"
        else:
            primary_metric_val = int(runs)
            primary_metric_lbl = "CAREER RUNS"
            primary_sub_stat = f"AVG {avg:.1f} &bull; SR {sr:.1f}"
            stat_item_1 = f"🏏 50s/100s: <strong>{fifties}/{hundreds}</strong>"
            stat_item_2 = f"🚀 6s: <strong>{sixes}</strong>"
            if wickets >= 10:
                stat_item_3 = f"🎯 Wkts: <strong>{wickets} ({bbf_str})</strong>"
            else:
                stat_item_3 = f"🎯 Best: <strong>{hs}</strong>"
        
        card_html = f"""
        <div class="fifa-flip-card-wrapper">
            <input type="checkbox" id="{player_chk_id}" class="fifa-flip-toggle">
            <label for="{player_chk_id}" class="fifa-flip-box">
                <div class="fifa-flip-inner">
                    <!-- 1. FRONT FACE: FIFA ULTIMATE TEAM SHIELD (Image 2) -->
                    <div class="fifa-front fut-card {tier_meta['class']}" style="border: 2px solid {tier_meta['color']};">
                        <div class="fut-top-bar">
                            <div style="text-align: left;">
                                <div class="fut-ovr" style="color: {tier_meta['color']};">{overall}</div>
                                <div class="fut-pos-badge">{pos_badge}</div>
                                <div style="font-size: 11px; font-weight: 700; color: #cbd5e1; margin-top: 2px;">{country_flag}</div>
                            </div>
                            <div style="background: {tier_meta['header_bg']}; color: #0b0f19; font-size: 11px; font-weight: 900; padding: 4px 10px; border-radius: 12px; letter-spacing: 1px; box-shadow: 0 2px 8px rgba(0,0,0,0.5);">
                                {tier_meta['badge']}
                            </div>
                        </div>
                        
                        <div class="fut-avatar-ring" style="border: 3px solid {tier_meta['color']};">
                            <img src="{img_url}" alt="{player}">
                        </div>
                        
                        <div class="fut-player-name" style="font-size: 24px; font-weight: 900; margin-top: 4px; letter-spacing: 1px; color: #fff;">{short_name}</div>
                        <div class="fut-team-tag" style="color: {tier_meta['color']}; margin-bottom: 8px;">{primary_team}</div>
                        
                        <div class="fut-stats-grid" style="grid-template-columns: repeat(2, 1fr); gap: 6px; padding: 10px 14px; background: rgba(13, 20, 36, 0.92); border: 1px solid rgba(255,255,255,0.1);">
                            <div class="fut-stat-box" style="flex-direction: row; justify-content: space-between; padding: 4px 12px;">
                                <span class="fut-stat-val" style="font-size: 22px; color: {tier_meta['color']};">{fifa_bat}</span>
                                <span class="fut-stat-lbl" style="font-size: 12px; font-weight: 800;">BAT</span>
                            </div>
                            <div class="fut-stat-box" style="flex-direction: row; justify-content: space-between; padding: 4px 12px;">
                                <span class="fut-stat-val" style="font-size: 22px; color: {tier_meta['color']};">{fifa_bow}</span>
                                <span class="fut-stat-lbl" style="font-size: 12px; font-weight: 800;">BOW</span>
                            </div>
                            <div class="fut-stat-box" style="flex-direction: row; justify-content: space-between; padding: 4px 12px;">
                                <span class="fut-stat-val" style="font-size: 22px; color: {tier_meta['color']};">{fifa_pac}</span>
                                <span class="fut-stat-lbl" style="font-size: 12px; font-weight: 800;">PAC</span>
                            </div>
                            <div class="fut-stat-box" style="flex-direction: row; justify-content: space-between; padding: 4px 12px;">
                                <span class="fut-stat-val" style="font-size: 22px; color: {tier_meta['color']};">{fifa_ref}</span>
                                <span class="fut-stat-lbl" style="font-size: 12px; font-weight: 800;">REF</span>
                            </div>
                            <div class="fut-stat-box" style="flex-direction: row; justify-content: space-between; padding: 4px 12px;">
                                <span class="fut-stat-val" style="font-size: 22px; color: {tier_meta['color']};">{fifa_cat}</span>
                                <span class="fut-stat-lbl" style="font-size: 12px; font-weight: 800;">CAT</span>
                            </div>
                            <div class="fut-stat-box" style="flex-direction: row; justify-content: space-between; padding: 4px 12px;">
                                <span class="fut-stat-val" style="font-size: 22px; color: {tier_meta['color']};">{fifa_thr}</span>
                                <span class="fut-stat-lbl" style="font-size: 12px; font-weight: 800;">THR</span>
                            </div>
                        </div>
                        
                        <div style="font-size: 11px; font-weight: 800; color: {tier_meta['color']}; margin-top: 10px; letter-spacing: 0.5px; text-transform: uppercase;">
                            ⚡ CLICK CARD TO FLIP 🔄
                        </div>
                    </div>
                    
                    <!-- 2. BACK FACE: 4-TIER ARCHIVE DOSSIER (Image 1) -->
                    <div class="fifa-back tier-card {tier_meta['class']}">
                        <div class="tier-header-strip">{tier_meta['tier']} EDITION</div>
                        
                        <div class="tier-upper-body">
                            <div class="tier-upper-player">{player}</div>
                            <div class="tier-upper-team">{primary_team}</div>
                        </div>
                        
                        <div class="tier-lower-body">
                            <div class="tier-watermark-icon">{tier_meta['watermark']}</div>
                            
                            <div class="tier-big-num">{primary_metric_val}</div>
                            <div class="tier-metric-label">{primary_metric_lbl}</div>
                            
                            <div class="tier-sub-stats">
                                {primary_sub_stat}
                            </div>
                            
                            <div class="tier-role-pill">{detailed_role}</div>
                            
                            <div style="display: flex; justify-content: space-around; width: 100%; margin-top: 14px; font-size: 11px; color: #cbd5e1; font-weight: 600;">
                                <div>{stat_item_1}</div>
                                <div>{stat_item_2}</div>
                                <div>{stat_item_3}</div>
                            </div>
                        </div>
                        
                        <div class="tier-bottom-strip">
                            <div>DEBUT: {tier_meta['debut']}</div>
                            <div>SALARY: {tier_meta['salary']}</div>
                        </div>
                    </div>
                </div>
            </label>
        </div>
        """
        render_html(card_html)
        
    with col_dossier:
        accolades_html = ""
        if pom_count > 0:
            accolades_html += f'<span class="accolade-pill">⭐ {pom_count}x Player of the Match</span>'
        if runs >= 5000:
            accolades_html += '<span class="accolade-pill">👑 5000+ Runs Club</span>'
        if wickets >= 100:
            accolades_html += '<span class="accolade-pill">🎯 100+ Wickets Club</span>'
        if sixes >= 150:
            accolades_html += '<span class="accolade-pill">🚀 Maximums King (150+ Sixes)</span>'
            
        dossier_html = f"""
        <div class="scorecard-dossier">
            <div class="scorecard-hero">
                <div>
                    <div style="font-family: 'Outfit'; font-size: 26px; font-weight: 900; color: #fff; text-transform: uppercase;">
                        {player} <span style="font-size: 14px; color: #f59e0b; font-weight: 700;">• {detailed_role}</span>
                    </div>
                    <div style="font-size: 13px; color: #94a3b8; margin-top: 3px;">Franchise: <strong style="color: #fff;">{primary_team}</strong></div>
                </div>
                <div style="text-align: right;">
                    <div style="font-family: 'Teko'; font-size: 38px; color: #f59e0b; line-height: 1;">OVR {overall}</div>
                    <div style="font-size: 11px; color: #94a3b8; font-weight: 700; text-transform: uppercase;">T20 Index</div>
                </div>
            </div>
            
            <div style="margin-bottom: 16px;">
                {accolades_html}
            </div>
            
            <div style="font-size: 12px; font-weight: 800; color: #f8fafc; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🏏 Batting Milestone Dossier</div>
            <div class="milestone-badge-grid">
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #38bdf8;">{innings_batted}</div>
                    <div class="milestone-lbl">Innings</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #f59e0b;">{hs}</div>
                    <div class="milestone-lbl">Highest Score</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #10b981;">{hundreds}</div>
                    <div class="milestone-lbl">Centuries (100)</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #fbbf24;">{fifties}</div>
                    <div class="milestone-lbl">Fifties (50)</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #f472b6;">{sixes}</div>
                    <div class="milestone-lbl">Sixes (6s)</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #34d399;">{fours}</div>
                    <div class="milestone-lbl">Fours (4s)</div>
                </div>
            </div>
            
            <div style="font-size: 12px; font-weight: 800; color: #f8fafc; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">🎯 Bowling & Pressure Impact</div>
            <div class="milestone-badge-grid">
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #38bdf8;">{innings_bowled}</div>
                    <div class="milestone-lbl">Innings Bowled</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #ef4444;">{bbf_str}</div>
                    <div class="milestone-lbl">Best Bowling (BBF)</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #f59e0b;">{eco}</div>
                    <div class="milestone-lbl">Economy Rate</div>
                </div>
                <div class="milestone-tile">
                    <div class="milestone-val" style="color: #10b981;">{catches}</div>
                    <div class="milestone-lbl">Catches in Field</div>
                </div>
            </div>
            
            <div style="background: rgba(0,0,0,0.35); border-radius: 14px; padding: 16px 18px; border: 1px solid rgba(255,255,255,0.08); margin-top: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; margin-bottom: 6px;">
                    <span style="color: #94a3b8; font-weight: 600;">Boundary Contribution:</span>
                    <strong style="color: #fef08a; font-family: 'Outfit'; font-size: 15px;">{boundary_pct}% ({boundary_runs:,} runs in 4s & 6s)</strong>
                </div>
                <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.08); border-radius: 3px; overflow: hidden; margin-bottom: 12px;">
                    <div style="width: {min(100, boundary_pct)}%; height: 100%; background: linear-gradient(90deg, #f59e0b, #ef4444); border-radius: 3px;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; margin-bottom: 6px;">
                    <span style="color: #94a3b8; font-weight: 600;">Career Strike Velocity:</span>
                    <strong style="color: #38bdf8; font-family: 'Outfit'; font-size: 15px;">{sr} SR ({balls_faced:,} legal balls faced)</strong>
                </div>
                <div style="width: 100%; height: 6px; background: rgba(255,255,255,0.08); border-radius: 3px; overflow: hidden;">
                    <div style="width: {min(100, (sr / 180) * 100)}%; height: 100%; background: linear-gradient(90deg, #38bdf8, #10b981); border-radius: 3px;"></div>
                </div>
            </div>
        </div>
        """
        render_html(dossier_html)
        
    st.markdown("---")
    st.subheader("📈 In-Depth Career Trajectory & Visualizations")
    tab_opp, tab_wkt, tab_growth, tab_scorecard = st.tabs(["⚔️ Favourite Opponents", "🎯 Dismissal Breakdown", "📊 Season Growth", "📋 Match-by-Match Scorecards"])
    
    with tab_opp:
        bat_vs_team = b_df.groupby('bowling_team')['batsman_runs'].sum().reset_index().sort_values('batsman_runs', ascending=False).head(6)
        if not bat_vs_team.empty:
            fig1 = plot_plotly_bar(bat_vs_team, 'bowling_team', 'batsman_runs', f"Runs Scored Against Opponents ({player})", color_col='bowling_team')
            st.plotly_chart(fig1, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
        else:
            st.info("No recorded batting data for opponent breakdown.")
            
    with tab_wkt:
        if wickets > 0:
            dismissal_wkts = w_df_p['dismissal_kind'].value_counts().reset_index()
            dismissal_wkts.columns = ['Dismissal Kind', 'Wickets']
            fig_diss = px.pie(dismissal_wkts, values='Wickets', names='Dismissal Kind', hole=0.45, title="Wickets by Mode of Dismissal", color_discrete_sequence=['#f59e0b', '#38bdf8', '#10b981', '#f472b6'])
            fig_diss.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_diss, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
        else:
            st.info("No bowling figures recorded for this player.")
            
    with tab_growth:
        b_season = pd.merge(b_df, matches[['id', 'season']], left_on='match_id', right_on='id')
        bowl_season = pd.merge(bowl_df, matches[['id', 'season']], left_on='match_id', right_on='id')
        gc1, gc2 = st.columns(2)
        with gc1:
            if not b_season.empty:
                bat_growth = b_season.groupby('season')['batsman_runs'].sum().reset_index()
                fig_bat_growth = px.bar(bat_growth, x='season', y='batsman_runs', text='batsman_runs', title="Runs Scored per Season", color_discrete_sequence=['#f59e0b'])
                fig_bat_growth.update_traces(textposition='outside')
                fig_bat_growth.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Runs")
                st.plotly_chart(fig_bat_growth, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
            else:
                st.info("No batting growth data available.")
        with gc2:
            wkt_season = bowl_season.dropna(subset=['player_dismissed'])
            wkt_season = wkt_season[wkt_season['dismissal_kind'] != 'run out']
            if not wkt_season.empty:
                bowl_growth = wkt_season.groupby('season')['player_dismissed'].count().reset_index()
                bowl_growth.columns = ['season', 'wickets']
                fig_bowl_growth = px.bar(bowl_growth, x='season', y='wickets', text='wickets', title="Wickets Taken per Season", color_discrete_sequence=['#38bdf8'])
                fig_bowl_growth.update_traces(textposition='outside')
                fig_bowl_growth.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="Wickets")
                st.plotly_chart(fig_bowl_growth, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
            else:
                st.info("No bowling growth data available.")
                
    with tab_scorecard:
        st.subheader(f"📋 Official Match Innings Scorecards — {player}")
        st.caption("Granular ball-by-ball innings ledger, batting strike velocities, dismissals, and bowling economy.")
        
        # Player match IDs
        p_match_ids = set(b_df['match_id'].unique()).union(set(bowl_df['match_id'].unique()))
        player_matches_meta = matches[matches['id'].isin(p_match_ids)].copy().sort_values('season')
        p_seasons = sorted(list(player_matches_meta['season'].dropna().unique()), reverse=True)
        
        sc_col1, sc_col2 = st.columns([1, 2])
        with sc_col1:
            selected_p_season = st.selectbox("Filter Matches by Season", ["All Seasons"] + p_seasons, key=f"psc_{player}")
            
        filtered_m = player_matches_meta.copy()
        if selected_p_season != "All Seasons":
            filtered_m = filtered_m[filtered_m['season'] == selected_p_season]
            
        filtered_m = filtered_m.sort_values(by=['date', 'id'], ascending=False).reset_index(drop=True)
        
        # Build scorecard rows
        scorecard_rows = []
        for _, m_row in filtered_m.iterrows():
            mid = m_row['id']
            date_str = str(m_row.get('date', ''))[:10]
            
            # Batting
            b_m = b_df[b_df['match_id'] == mid]
            if not b_m.empty:
                r_scored = int(b_m['batsman_runs'].sum())
                balls_f = int(b_m.shape[0] - (b_m['extras_type'] == 'wides').sum() if 'extras_type' in b_m.columns else b_m.shape[0])
                fours_cnt = int((b_m['batsman_runs'] == 4).sum())
                sixes_cnt = int((b_m['batsman_runs'] == 6).sum())
                sr_val = round((r_scored / balls_f) * 100, 1) if balls_f > 0 else 0.0
                
                # dismissal
                diss = deliveries[(deliveries['match_id'] == mid) & (deliveries['player_dismissed'] == player)]
                if not diss.empty:
                    d_row = diss.iloc[0]
                    dk = d_row['dismissal_kind']
                    bw = d_row['bowler']
                    fl = d_row['fielder']
                    if dk == 'bowled': d_text = f"b {bw}"
                    elif dk == 'caught': d_text = f"c {fl} b {bw}" if pd.notna(fl) else f"c & b {bw}"
                    elif dk == 'lbw': d_text = f"lbw b {bw}"
                    elif dk == 'run out': d_text = f"run out ({fl})" if pd.notna(fl) else "run out"
                    elif dk == 'stumped': d_text = f"st {fl} b {bw}"
                    else: d_text = f"{dk} b {bw}"
                else:
                    d_text = "not out"
                bat_str = f"{r_scored} ({balls_f}b, {fours_cnt}x4, {sixes_cnt}x6, SR {sr_val})"
            else:
                r_scored, balls_f = 0, 0
                d_text = "DNB"
                bat_str = "DNB"
                
            # Bowling
            bw_m = bowl_df[bowl_df['match_id'] == mid]
            if not bw_m.empty:
                leg_b = int(bw_m.shape[0] - (bw_m['extras_type'].isin(['wides', 'noballs']) if 'extras_type' in bw_m.columns else 0).sum())
                overs_str = f"{leg_b // 6}.{leg_b % 6}"
                r_conc = int(bw_m['total_runs'].sum() - (bw_m[bw_m['extras_type'] == 'legbyes']['total_runs'].sum() if 'extras_type' in bw_m.columns else 0))
                wkts_cnt = int(bw_m.dropna(subset=['player_dismissed'])[bw_m.dropna(subset=['player_dismissed'])['dismissal_kind'] != 'run out'].shape[0])
                eco_val = round((r_conc / leg_b) * 6, 2) if leg_b > 0 else 0.0
                bowl_str = f"{wkts_cnt}/{r_conc} ({overs_str} ov, Eco {eco_val})"
            else:
                bowl_str = "DNB"
                
            mom_award = "⭐ MoM" if m_row.get('player_of_match') == player else "-"
            winner_str = str(m_row.get('winner', 'No Result'))
            
            scorecard_rows.append({
                'Season': m_row.get('season', ''),
                'Date': date_str,
                'Match': f"{m_row.get('team1')} vs {m_row.get('team2')}",
                'Batting Performance': bat_str,
                'Dismissal': d_text,
                'Bowling Figures': bowl_str,
                'Winner': winner_str,
                'Award': mom_award
            })
            
        if scorecard_rows:
            sc_df = pd.DataFrame(scorecard_rows)
            s_runs = sum([int(x.split()[0]) for x in sc_df['Batting Performance'] if x != 'DNB'])
            s_wkts = sum([int(x.split('/')[0]) for x in sc_df['Bowling Figures'] if x != 'DNB' and '/' in x])
            m_c1, m_c2, m_c3, m_c4 = st.columns(4)
            m_c1.metric("Matches in View", len(sc_df))
            m_c2.metric("Total Runs", f"{s_runs:,}")
            m_c3.metric("Total Wickets", s_wkts)
            m_c4.metric("MoM Honors", (sc_df['Award'] == '⭐ MoM').sum() if 'Award' in sc_df.columns else 0)
            
            st.dataframe(sc_df, hide_index=True, use_container_width=True)
        else:
            st.info("No match scorecards found for this player in this selection.")
            
    # ==========================================
    # 💎 THE FOUR TIERS SHOWCASE (Image 1)
    # ==========================================
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; margin: 35px 0 20px 0;">
            <div class="ipl-badge-pill">💎 Elite Collectibles System</div>
            <h2 style="font-family: 'Outfit'; font-size: 32px; font-weight: 900; color: #ffffff; margin: 0; text-transform: uppercase; letter-spacing: 1px;">The Four Tiers</h2>
            <p style="color: #94a3b8; font-size: 15px; margin-top: 6px;">Authentic statistical tier classification derived from 19 editions of IPL performance benchmarks.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    four_tiers_html = """
    <div class="tier-grid">
        <!-- 1. STANDARD: JASPRIT BUMRAH (Debut 2013) -->
        <div class="tier-card tier-standard" onclick="this.classList.toggle('flipped')">
            <div class="tier-header-strip">STANDARD</div>
            <div class="tier-upper-body">
                <div class="tier-upper-player">JASPRIT BUMRAH</div>
                <div class="tier-upper-team">MUMBAI INDIANS</div>
            </div>
            <div class="tier-lower-body">
                <div class="tier-watermark-icon">⚾</div>
                <div class="tier-big-num">3</div>
                <div class="tier-metric-label">WICKETS</div>
                <div class="tier-sub-stats">ECON 10.0 &bull; AVG 23.3</div>
                <div class="tier-role-pill">FAST BOWLER</div>
            </div>
            <div class="tier-bottom-strip">
                <div>2013</div>
                <div>0.2 CR</div>
            </div>
        </div>
        
        <!-- 2. RARE: MS DHONI (Championship 2010) -->
        <div class="tier-card tier-rare" onclick="this.classList.toggle('flipped')">
            <div class="tier-header-strip">RARE</div>
            <div class="tier-upper-body">
                <div class="tier-upper-player">MS DHONI</div>
                <div class="tier-upper-team">CHENNAI SUPER KINGS</div>
            </div>
            <div class="tier-lower-body">
                <div class="tier-watermark-icon">🧤</div>
                <div class="tier-big-num">287</div>
                <div class="tier-metric-label">RUNS</div>
                <div class="tier-sub-stats">AVG 31.9 &bull; SR 136.7</div>
                <div class="tier-role-pill">WICKETKEEPER BATTER</div>
            </div>
            <div class="tier-bottom-strip">
                <div>2010</div>
                <div>6.0 CR</div>
            </div>
        </div>
        
        <!-- 3. EPIC: AB DE VILLIERS (2019 Season) -->
        <div class="tier-card tier-epic" onclick="this.classList.toggle('flipped')">
            <div class="tier-header-strip">EPIC</div>
            <div class="tier-upper-body">
                <div class="tier-upper-player">AB DE VILLIERS ✈️</div>
                <div class="tier-upper-team">ROYAL CHALLENGERS BANGALORE</div>
            </div>
            <div class="tier-lower-body">
                <div class="tier-watermark-icon">🧤</div>
                <div class="tier-big-num">442</div>
                <div class="tier-metric-label">RUNS</div>
                <div class="tier-sub-stats">AVG 44.2 &bull; SR 154.0</div>
                <div class="tier-role-pill">WICKETKEEPER BATTER</div>
            </div>
            <div class="tier-bottom-strip">
                <div>2019</div>
                <div>11.0 CR</div>
            </div>
        </div>
        
        <!-- 4. ICON: VIRAT KOHLI (Peak 2013 Era) -->
        <div class="tier-card tier-icon" onclick="this.classList.toggle('flipped')">
            <div class="tier-header-strip">★ ICON ★</div>
            <div class="tier-upper-body">
                <div class="tier-upper-player">VIRAT KOHLI</div>
                <div class="tier-upper-team">ROYAL CHALLENGERS BANGALORE</div>
            </div>
            <div class="tier-lower-body">
                <div class="tier-watermark-icon">🏏</div>
                <div class="tier-big-num">634</div>
                <div class="tier-metric-label">RUNS</div>
                <div class="tier-sub-stats">AVG 45.3 &bull; SR 138.7</div>
                <div class="tier-role-pill">TOP ORDER BATTER</div>
            </div>
            <div class="tier-bottom-strip">
                <div>2013</div>
                <div>8.2 CR</div>
            </div>
        </div>
    </div>
    """
    render_html(four_tiers_html)


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
    st.plotly_chart(plot_plotly_bar(venue_counts.head(10), 'Venue', 'Matches', 'Top 10 Most Frequently Used IPL Stadiums'), use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
    
    st.header("Highest Scoring Grounds (Average Match Runs)")
    venue_runs = matches[['id', 'venue']].merge(deliveries, left_on='id', right_on='match_id')
    avg_runs_venue = venue_runs.groupby(['venue', 'match_id'])['total_runs'].sum().reset_index()
    avg_runs_venue = avg_runs_venue.groupby('venue')['total_runs'].mean().reset_index().sort_values('total_runs', ascending=False)
    st.plotly_chart(plot_plotly_bar(avg_runs_venue.head(10), 'venue', 'total_runs', 'Average Total Runs per Match by Stadium'), use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})


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
        st.plotly_chart(fig, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
        
    with col2:
        matches['toss_win_match_win'] = matches['toss_winner'] == matches['winner']
        toss_impact = matches['toss_win_match_win'].value_counts()
        fig2 = px.pie(values=toss_impact.values, names=['Toss Winner Won', 'Toss Winner Lost'], title="Toss Winner Match Conversion Rate", color_discrete_sequence=['#10b981', '#ef4444'])
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig2, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})


# ==========================================
# ⚔️ PAGE 7: MATCH & HEAD-TO-HEAD
# ==========================================
elif page == "Match & Head-to-Head Analysis":
    st.title("⚔️ Match Center, Scorecards & Head-to-Head Arena")
    
    tab_scorecard, tab_h2h = st.tabs(["🏟️ Official Match Scorecard Center", "⚔️ Franchise Head-to-Head Arena"])
    
    with tab_scorecard:
        st.subheader("🏟️ Complete Match Scorecard & Ball-by-Ball Summary")
        st.caption("Inspect comprehensive innings-by-innings scorecards from any IPL match played between 2008 and 2026.")
        
        all_seasons = sorted(list(matches['season'].dropna().unique()), reverse=True)
        col_s, col_m = st.columns([1, 2])
        
        with col_s:
            sel_s = st.selectbox("Select Season", all_seasons, index=0, key="match_center_season")
            
        season_matches = matches[matches['season'] == sel_s].copy()
        season_matches = season_matches.sort_values(by=['date', 'id'], ascending=False)
        
        # Build nice label for each match
        match_options = []
        match_map = {}
        for _, m_row in season_matches.iterrows():
            m_id = m_row['id']
            d_str = str(m_row.get('date', ''))[:10]
            m_type = f" ({m_row['match_type']})" if pd.notna(m_row.get('match_type')) and str(m_row.get('match_type')).lower() != 'nan' else ""
            label = f"{d_str}: {m_row['team1']} vs {m_row['team2']}{m_type} (Match #{m_id})"
            match_options.append(label)
            match_map[label] = m_id
            
        with col_m:
            sel_match_label = st.selectbox("Select Match to View Scorecard", match_options, key="match_center_match")
            
        if match_options:
            selected_mid = match_map[sel_match_label]
            m_info = matches[matches['id'] == selected_mid].iloc[0]
            m_deliveries = deliveries[deliveries['match_id'] == selected_mid]
            
            # Match Header Banner
            winner_disp = m_info.get('winner', 'No Result')
            if pd.notna(m_info.get('result_margin')) and pd.notna(m_info.get('result')):
                res_detail = f"{winner_disp} won by {int(m_info['result_margin'])} {m_info['result']}"
            elif pd.notna(m_info.get('win_by_runs')) and m_info['win_by_runs'] > 0:
                res_detail = f"{winner_disp} won by {int(m_info['win_by_runs'])} runs"
            elif pd.notna(m_info.get('win_by_wickets')) and m_info['win_by_wickets'] > 0:
                res_detail = f"{winner_disp} won by {int(m_info['win_by_wickets'])} wickets"
            else:
                res_detail = f"{winner_disp} won" if pd.notna(winner_disp) else "Match Tied / NR"
                
            toss_info = f"Toss: {m_info.get('toss_winner', '')} won toss & chose to {m_info.get('toss_decision', '')}"
            pom_info = f"⭐ Player of the Match: {m_info.get('player_of_match', 'N/A')}"
            venue_info = f"🏟️ {m_info.get('venue', '')}, {m_info.get('city', '')} | 📅 {str(m_info.get('date', ''))[:10]}"
            
            t1_logo = f'<img src="{OFFICIAL_TEAM_LOGOS.get(m_info["team1"], "")}" style="width:36px; height:36px; object-fit:contain; vertical-align:middle; margin-right:8px;">' if OFFICIAL_TEAM_LOGOS.get(m_info["team1"]) else ""
            t2_logo = f'<img src="{OFFICIAL_TEAM_LOGOS.get(m_info["team2"], "")}" style="width:36px; height:36px; object-fit:contain; vertical-align:middle; margin-left:8px;">' if OFFICIAL_TEAM_LOGOS.get(m_info["team2"]) else ""
            
            banner_html = f"""
            <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border: 1px solid rgba(245, 158, 11, 0.4); border-radius: 16px; padding: 20px; margin: 15px 0 25px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                    <div style="font-family: 'Outfit'; font-size: 22px; font-weight: 800; color: #fff;">
                        {t1_logo}{m_info['team1']} <span style="color: #f59e0b; margin: 0 8px;">VS</span> {m_info['team2']}{t2_logo}
                    </div>
                    <div style="background: rgba(245, 158, 11, 0.15); border: 1px solid #f59e0b; padding: 6px 14px; border-radius: 20px; font-weight: 700; color: #fbbf24; font-size: 14px;">
                        {res_detail}
                    </div>
                </div>
                <div style="margin-top: 12px; display: flex; gap: 20px; flex-wrap: wrap; font-size: 13px; color: #94a3b8; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px;">
                    <div>{venue_info}</div>
                    <div>{toss_info}</div>
                    <div style="color: #38bdf8; font-weight: 700;">{pom_info}</div>
                </div>
            </div>
            """
            render_html(banner_html)
            
            # Innings tabs
            innings_available = sorted(m_deliveries['inning'].unique())
            inn_tabs = st.tabs([f"Innings {inn}" for inn in innings_available])
            
            for idx, inn in enumerate(innings_available):
                with inn_tabs[idx]:
                    inn_df = m_deliveries[m_deliveries['inning'] == inn]
                    bat_team = inn_df['batting_team'].iloc[0]
                    bowl_team = inn_df['bowling_team'].iloc[0]
                    total_r = inn_df['total_runs'].sum()
                    wkts = inn_df.dropna(subset=['player_dismissed']).shape[0]
                    legal_b = inn_df.shape[0] - (inn_df['extras_type'].isin(['wides', 'noballs']) if 'extras_type' in inn_df.columns else 0).sum()
                    ov_str = f"{legal_b // 6}.{legal_b % 6}"
                    rr = round((total_r / legal_b) * 6, 2) if legal_b > 0 else 0.0
                    
                    # Extras
                    wides = (inn_df['extras_type'] == 'wides').sum() if 'extras_type' in inn_df.columns else 0
                    noballs = (inn_df['extras_type'] == 'noballs').sum() if 'extras_type' in inn_df.columns else 0
                    legbyes = inn_df[inn_df['extras_type'] == 'legbyes']['total_runs'].sum() if 'extras_type' in inn_df.columns else 0
                    byes = inn_df[inn_df['extras_type'] == 'byes']['total_runs'].sum() if 'extras_type' in inn_df.columns else 0
                    total_extras = inn_df['extra_runs'].sum()
                    
                    st.markdown(f"### 🏏 {bat_team} — **{total_r}/{wkts}** ({ov_str} ov, RR: {rr})")
                    
                    # Batting scorecard table
                    batters_data = []
                    for b in inn_df['batsman'].unique():
                        b_sub = inn_df[inn_df['batsman'] == b]
                        r = int(b_sub['batsman_runs'].sum())
                        bf = int(b_sub.shape[0] - (b_sub['extras_type'] == 'wides').sum() if 'extras_type' in b_sub.columns else b_sub.shape[0])
                        fours = int((b_sub['batsman_runs'] == 4).sum())
                        sixes = int((b_sub['batsman_runs'] == 6).sum())
                        sr_rate = round((r / bf) * 100, 1) if bf > 0 else 0.0
                        
                        # dismissal text
                        diss_sub = inn_df[inn_df['player_dismissed'] == b]
                        if not diss_sub.empty:
                            d_row = diss_sub.iloc[0]
                            dk = d_row['dismissal_kind']
                            bw = d_row['bowler']
                            fl = d_row['fielder']
                            if dk == 'bowled': d_desc = f"b {bw}"
                            elif dk == 'caught': d_desc = f"c {fl} b {bw}" if pd.notna(fl) else f"c & b {bw}"
                            elif dk == 'lbw': d_desc = f"lbw b {bw}"
                            elif dk == 'run out': d_desc = f"run out ({fl})" if pd.notna(fl) else "run out"
                            elif dk == 'stumped': d_desc = f"st {fl} b {bw}"
                            else: d_desc = f"{dk} b {bw}"
                        else:
                            d_desc = "not out"
                            
                        batters_data.append({
                            'Batter': b,
                            'Dismissal': d_desc,
                            'Runs': r,
                            'Balls': bf,
                            '4s': fours,
                            '6s': sixes,
                            'Strike Rate': sr_rate
                        })
                        
                    st.dataframe(pd.DataFrame(batters_data), hide_index=True, use_container_width=True)
                    
                    st.markdown(f"<div style='font-size: 13px; color: #94a3b8; margin: 8px 0;'><b>Extras:</b> {total_extras} (w {wides}, nb {noballs}, lb {legbyes}, b {byes}) | <b>Total:</b> {total_r}/{wkts} ({ov_str} ov)</div>", unsafe_allow_html=True)
                    
                    # Bowling scorecard table
                    st.markdown(f"#### 🎯 Bowling — {bowl_team}")
                    bowlers_data = []
                    for bw in inn_df['bowler'].unique():
                        bw_sub = inn_df[inn_df['bowler'] == bw]
                        legal_bowled = int(bw_sub.shape[0] - (bw_sub['extras_type'].isin(['wides', 'noballs']) if 'extras_type' in bw_sub.columns else 0).sum())
                        o_str = f"{legal_bowled // 6}.{legal_bowled % 6}"
                        r_conceded = int(bw_sub['total_runs'].sum() - (bw_sub[bw_sub['extras_type'] == 'legbyes']['total_runs'].sum() if 'extras_type' in bw_sub.columns else 0))
                        w_taken = int(bw_sub.dropna(subset=['player_dismissed'])[bw_sub.dropna(subset=['player_dismissed'])['dismissal_kind'] != 'run out'].shape[0])
                        e_rate = round((r_conceded / legal_bowled) * 6, 2) if legal_bowled > 0 else 0.0
                        
                        # Maidens count
                        maidens = 0
                        for ov_num in bw_sub['over'].unique():
                            ov_del = bw_sub[bw_sub['over'] == ov_num]
                            if ov_del['total_runs'].sum() == 0 and ov_del.shape[0] >= 6:
                                maidens += 1
                                
                        bowlers_data.append({
                            'Bowler': bw,
                            'Overs': o_str,
                            'Maidens': maidens,
                            'Runs Conceded': r_conceded,
                            'Wickets': w_taken,
                            'Economy': e_rate
                        })
                        
                    st.dataframe(pd.DataFrame(bowlers_data), hide_index=True, use_container_width=True)
                    
    with tab_h2h:
        st.subheader("⚔️ Head-to-Head Encounter Statistics")
        col1, col2 = st.columns(2)
        teams_list = sorted([str(t) for t in matches['team1'].dropna().unique() if str(t).strip()])
        t1 = col1.selectbox("Franchise A", teams_list, index=teams_list.index('Mumbai Indians') if 'Mumbai Indians' in teams_list else 0, key="h2h_t1")
        t2 = col2.selectbox("Franchise B", teams_list, index=teams_list.index('Chennai Super Kings') if 'Chennai Super Kings' in teams_list else 1, key="h2h_t2")
        
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
                st.plotly_chart(fig, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})
            else:
                st.info("No recorded historical matches between these two franchises.")
                
        st.markdown("---")
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
    st.plotly_chart(fig, use_container_width=True, theme=None, config={'displayModeBar': False, 'responsive': True})


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
        p_name = orange_cap['batsman']
        p_team = season_deliveries[season_deliveries['batsman'] == p_name]['batting_team'].iloc[0]
        o_img, _ = get_player_image_and_bio(p_name, p_team)
        with col1:
            render_html(f"""
            <div class="award-card orange">
                <div class="award-badge-ribbon" style="background: rgba(249, 115, 22, 0.15); border: 1px solid rgba(249, 115, 22, 0.4); color: #fb923c;">
                    🏏 Orange Cap Winner
                </div>
                <div class="award-avatar-ring" style="border: 2px solid #f97316;">
                    <img src="{o_img}" alt="{p_name}">
                </div>
                <div style="font-family: 'Outfit'; font-size: 20px; font-weight: 800; color: #fff;">{p_name}</div>
                <div style="font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-top: 2px;">{p_team}</div>
                <div style="font-family: 'Teko'; font-size: 38px; font-weight: 700; color: #fb923c; line-height: 1; margin-top: 8px;">{int(orange_cap['batsman_runs']):,} Runs</div>
            </div>
            """)
        
    # Purple Cap
    if not season_deliveries.empty:
        bowl_st = season_deliveries.dropna(subset=['player_dismissed'])
        bowl_st = bowl_st[bowl_st['dismissal_kind'] != 'run out']
        if not bowl_st.empty:
            purple_cap = bowl_st.groupby('bowler').size().reset_index(name='wickets').sort_values('wickets', ascending=False).iloc[0]
            b_name = purple_cap['bowler']
            b_team = season_deliveries[season_deliveries['bowler'] == b_name]['bowling_team'].iloc[0]
            p_img, _ = get_player_image_and_bio(b_name, b_team)
            with col2:
                render_html(f"""
                <div class="award-card purple">
                    <div class="award-badge-ribbon" style="background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.4); color: #c084fc;">
                        🎯 Purple Cap Winner
                    </div>
                    <div class="award-avatar-ring" style="border: 2px solid #a855f7;">
                        <img src="{p_img}" alt="{b_name}">
                    </div>
                    <div style="font-family: 'Outfit'; font-size: 20px; font-weight: 800; color: #fff;">{b_name}</div>
                    <div style="font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-top: 2px;">{b_team}</div>
                    <div style="font-family: 'Teko'; font-size: 38px; font-weight: 700; color: #c084fc; line-height: 1; margin-top: 8px;">{purple_cap['wickets']} Wickets</div>
                </div>
                """)
            
    # MVP
    if not season_matches.empty and 'player_of_match' in season_matches.columns:
        pom_counts = season_matches['player_of_match'].value_counts()
        if not pom_counts.empty:
            best_p = pom_counts.index[0]
            m_img, _ = get_player_image_and_bio(best_p, "IPL")
            with col3:
                render_html(f"""
                <div class="award-card mvp">
                    <div class="award-badge-ribbon" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8;">
                        ⭐ Season MVP
                    </div>
                    <div class="award-avatar-ring" style="border: 2px solid #38bdf8;">
                        <img src="{m_img}" alt="{best_p}">
                    </div>
                    <div style="font-family: 'Outfit'; font-size: 20px; font-weight: 800; color: #fff;">{best_p}</div>
                    <div style="font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase; margin-top: 2px;">Most Player of Match</div>
                    <div style="font-family: 'Teko'; font-size: 38px; font-weight: 700; color: #38bdf8; line-height: 1; margin-top: 8px;">{pom_counts.iloc[0]} Awards</div>
                </div>
                """)
            
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
    
    podium_meta = [
        ("🥇 Rank 1 - GOAT Legend", "gold", "#f59e0b", "rgba(245, 158, 11, 0.15)"),
        ("🥈 Rank 2 - All-Time Titan", "silver", "#cbd5e1", "rgba(203, 213, 225, 0.15)"),
        ("🥉 Rank 3 - Elite Master", "bronze", "#d97706", "rgba(217, 119, 6, 0.15)")
    ]
    
    for i, col in enumerate([p1, p2, p3]):
        row_p = top3.iloc[i]
        p_name = row_p['player']
        p_img, _ = get_player_image_and_bio(p_name, "IPL")
        rank_label, p_class, p_color, bg_tint = podium_meta[i]
        
        with col:
            render_html(f"""
            <div class="podium-card {p_class}">
                <div class="podium-rank-badge" style="background: {bg_tint}; border: 1px solid {p_color}; color: {p_color};">
                    {rank_label}
                </div>
                <div class="podium-avatar-ring" style="border: 2px solid {p_color};">
                    <img src="{p_img}" alt="{p_name}">
                </div>
                <div style="font-family: 'Outfit'; font-size: 22px; font-weight: 800; color: #fff; margin-top: 4px;">{p_name}</div>
                <div style="font-size: 12px; font-weight: 600; color: #94a3b8; margin-top: 4px;">
                    🏏 {int(row_p['runs']):,} Runs &bull; 🎯 {int(row_p['wickets'])} Wkts
                </div>
                <div style="font-family: 'Teko'; font-size: 36px; font-weight: 700; color: {p_color}; margin-top: 6px; line-height: 1;">
                    Impact Index: {int(row_p['composite_score']):,}
                </div>
            </div>
            """)
            
    st.markdown("---")
    st.subheader("Top 50 Comprehensive Leaderboard")
    all_p['Rank'] = np.arange(1, len(all_p) + 1)
    st.dataframe(all_p.head(50)[['Rank', 'player', 'runs', 'wickets', 'composite_score']], hide_index=True, use_container_width=True)


# ==========================================
# 👑 PAGE 13: GREATEST TEAM OF ALL TIME
# ==========================================
elif page == "Greatest Team of All Time":
    st.markdown(
        """
        <div class="ipl-hero">
            <div class="ipl-hero-content">
                <div class="ipl-badge-pill">👑 Hall of Fame Lineup</div>
                <h1>Greatest All-Time IPL Playing XI</h1>
                <p>The consensus ultimate 11-man championship squad: lethal boundary hitters, clutch match finishers, world-class mystery spin, and pinpoint yorker death bowlers.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    dream_squad = [
        {"no": 1, "name": "Virat Kohli", "role": "Opening Anchor & Aggressor", "dynasty": "Royal Challengers Bengaluru", "stat": "8,000+ Runs (All-Time #1)", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": False, "legacy": "All-time leading IPL run-scorer with 8 centuries and an unmatched 973 runs in a single season."},
        {"no": 2, "name": "Chris Gayle", "role": "Universal Power Opener", "dynasty": "RCB / PBKS / KKR", "stat": "357 Sixes & 175* Record", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": False, "legacy": "The most destructive opener in T20 history with the highest individual score (175* off 66) and 6 centuries."},
        {"no": 3, "name": "Suresh Raina", "role": "Mr. IPL & Top-Order Spine", "dynasty": "Chennai Super Kings", "stat": "5,528 Runs & 4x Titles", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": False, "legacy": "First player to cross 5,000 IPL runs. The backbone of CSK's 4 championship campaigns."},
        {"no": 4, "name": "AB de Villiers", "role": "360° Genius & Modern Innovator", "dynasty": "Royal Challengers Bengaluru", "stat": "151.7 Strike Rate & 5,162 Runs", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": False, "legacy": "360-degree boundary machine with 251 sixes and 40+ fifty-plus scores at superhuman strike rates."},
        {"no": 5, "name": "MS Dhoni", "role": "Master Finisher & Captain, WK", "dynasty": "Chennai Super Kings", "stat": "5x Champion Captain & 250+ Matches", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": True, "legacy": "The ultimate T20 strategist, 5x champion captain, and ice-cool finisher with 5,000+ runs and 140+ dismissals."},
        {"no": 6, "name": "Andre Russell", "role": "Explosive Fast-Bowling Finisher", "dynasty": "Kolkata Knight Riders", "stat": "174.0 Career Strike Rate", "color": "#a855f7", "tier": "EPIC", "tier_class": "tier-epic", "captain": False, "legacy": "Highest strike rate in IPL history with lethal lower-order power and 100+ clutch wickets."},
        {"no": 7, "name": "Kieron Pollard", "role": "Clutch Finisher & Big-Match Legend", "dynasty": "Mumbai Indians", "stat": "5x Champion & 3,400+ Runs", "color": "#a855f7", "tier": "EPIC", "tier_class": "tier-epic", "captain": False, "legacy": "Heart of Mumbai Indians' dynasty with 223 sixes and unforgettable match-winning finals knocks."},
        {"no": 8, "name": "Sunil Narine", "role": "Mystery Spinner & Pinch Hitter", "dynasty": "Kolkata Knight Riders", "stat": "180+ Wkts & 6.7 Economy", "color": "#a855f7", "tier": "EPIC", "tier_class": "tier-epic", "captain": False, "legacy": "3x IPL champion MVP who revolutionized opening batting and strangled every batting unit for a decade."},
        {"no": 9, "name": "Rashid Khan", "role": "T20 Leg-Spin Wizard", "dynasty": "GT / SRH", "stat": "140+ Wkts & 6.6 Economy", "color": "#a855f7", "tier": "EPIC", "tier_class": "tier-epic", "captain": False, "legacy": "Unplayable googlies and pinpoint precision across powerplay and middle overs with unmatched economy."},
        {"no": 10, "name": "Lasith Malinga", "role": "Yorker Searing Death Legend", "dynasty": "Mumbai Indians", "stat": "170 Wickets & 4x Titles", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": False, "legacy": "The gold standard of T20 bowling with lethal toe-crushing yorkers and 170 wickets at an average of 19.8."},
        {"no": 11, "name": "Jasprit Bumrah", "role": "All-Phase Precision Pacer", "dynasty": "Mumbai Indians", "stat": "165+ Wkts & 7.3 Economy", "color": "#f59e0b", "tier": "ICON", "tier_class": "tier-icon", "captain": False, "legacy": "The modern fast-bowling GOAT, unhittable in death overs and lethal in powerplays for Mumbai Indians."}
    ]
    
    st.info("💡 **Interactive 3D Cards**: Click on any player card below to **3D Flip** and reveal their all-time tactical legacy and dossier!")
    
    cards_html = '<div class="dream11-flip-grid">'
    for p in dream_squad:
        p_img, _ = get_player_image_and_bio(p['name'], p['dynasty'])
        cap_badge = '<div class="dream11-captain-tag">👑 CAPTAIN & WK</div>' if p['captain'] else ''
        cards_html += f"""
        <div>
            <input type="checkbox" id="dream11_check_{p['no']}" class="flip-checkbox-input">
            <label for="dream11_check_{p['no']}" class="dream11-flip-box">
                <div class="dream11-flip-inner">
                    <!-- FRONT FACE: TIER CARD -->
                    <div class="dream11-face dream11-front dream11-player-card {p['tier_class']}" style="border: 2px solid {p['color']};">
                        <div class="dream11-squad-no">{p['no']}</div>
                        <div style="position: absolute; top: 12px; right: 12px; font-size: 10px; font-weight: 900; background: {p['color']}; color: #0b0f19; padding: 3px 8px; border-radius: 10px; letter-spacing: 0.5px;">
                            {p['tier']}
                        </div>
                        {cap_badge}
                        <div class="dream11-avatar-ring" style="border-color: {p['color']}; margin-top: 14px;">
                            <img src="{p_img}" alt="{p['name']}">
                        </div>
                        <div style="font-family: 'Outfit'; font-size: 18px; font-weight: 900; color: #fff; line-height: 1.1; margin-top: 4px;">{p['name']}</div>
                        <div style="font-size: 11px; font-weight: 700; color: {p['color']}; text-transform: uppercase; letter-spacing: 0.5px; margin: 4px 0;">{p['dynasty']}</div>
                        <div style="display: inline-block; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 4px 10px; font-size: 11px; color: #cbd5e1; font-weight: 600; margin-top: 4px;">
                            {p['role']}
                        </div>
                        <div style="font-family: 'Teko'; font-size: 22px; font-weight: 700; color: {p['color']}; margin-top: 8px;">
                            {p['stat']}
                        </div>
                        <div style="font-size: 10px; font-weight: 700; color: #f59e0b; margin-top: 6px; letter-spacing: 0.5px; text-transform: uppercase;">
                            🔄 CLICK CARD TO FLIP
                        </div>
                    </div>
                    
                    <!-- BACK FACE: LEGACY DOSSIER (Image 1) -->
                    <div class="dream11-face dream11-back tier-card {p['tier_class']}">
                        <div class="tier-header-strip">★ {p['tier']} EDITION ★</div>
                        <div class="tier-upper-body" style="padding: 10px 14px 14px 14px;">
                            <div class="tier-upper-player" style="font-size: 16px;">{p['name']}</div>
                            <div class="tier-upper-team">{p['dynasty']}</div>
                        </div>
                        <div class="tier-lower-body" style="padding: 10px 14px;">
                            <div class="tier-watermark-icon">🏏</div>
                            <div style="font-family: 'Teko'; font-size: 26px; font-weight: 700; color: {p['color']}; line-height: 1;">TACTICAL LEGACY</div>
                            <p style="font-size: 12px; color: #e2e8f0; line-height: 1.45; margin: 8px 0; font-weight: 500;">
                                {p['legacy']}
                            </p>
                            <div class="tier-role-pill" style="margin-top: 4px;">{p['role']}</div>
                        </div>
                        <div class="tier-bottom-strip">
                            <div>ORDER: #{p['no']}</div>
                            <div>ALL-TIME XI</div>
                        </div>
                    </div>
                </div>
            </label>
        </div>
        """
    cards_html += '</div>'
    render_html(cards_html)
    
    st.markdown("---")
    st.subheader("Tactical Lineup & Squad Specifications")
    st.dataframe(pd.DataFrame(dream_squad)[['no', 'name', 'role', 'dynasty', 'stat']].rename(columns={
        'no': 'Batting Order', 'name': 'Player', 'role': 'Tactical Role', 'dynasty': 'Franchise History', 'stat': 'Marquee Career Metric'
    }), hide_index=True, use_container_width=True)


# ==========================================
# 📸 PAGE 14: ICONIC IPL MOMENTS GALLERY
# ==========================================
elif page == "📸 Iconic IPL Moments":
    st.markdown(
        """<div style="text-align: center; margin: 15px 0 25px 0;">
            <div class="ipl-badge-pill">🏛️ THE OFFICIAL ARCHIVE</div>
            <h1 style="color: #fff; font-size: 34px; font-weight: 900; margin: 8px 0; text-transform: uppercase; letter-spacing: 1.5px;">IPL Iconic Moments</h1>
            <p style="color: #94a3b8; font-size: 15px; margin: 0 auto; max-width: 780px;">The moments that made history — explore 19 seasons (2008–2026) of historic batting masterpieces, legendary last-ball thrillers, and visual league archives.</p>
        </div>""",
        unsafe_allow_html=True
    )

    tab_archive, tab_gallery = st.tabs(["📜 Historical Archive (2008–2026)", "🖼️ Visual Wallpapers & Photo Gallery"])

    with tab_archive:
        moments_file = '/home/tejas/ipl/ipl_iconic_moments_2008_2026.json'
        archive_data = []
        if os.path.exists(moments_file):
            try:
                with open(moments_file, 'r', encoding='utf-8') as mf:
                    archive_data = json.load(mf)
            except Exception:
                archive_data = []

        if not archive_data:
            st.info("Archive moments dataset loading...")
        else:
            # Summary Metrics Strip
            m_c1, m_c2, m_c3, m_c4 = st.columns(4)
            with m_c1:
                st.metric("Total Moments", len(archive_data))
            with m_c2:
                st.metric("Seasons Covered", f"{min(m['season'] for m in archive_data)}–{max(m['season'] for m in archive_data)}")
            with m_c3:
                st.metric("Essential Immortals", sum(1 for m in archive_data if m.get('importance') == 'Essential'))
            with m_c4:
                st.metric("Top 50 Ranked", "50 Moments")

            st.markdown("<hr style='border: none; border-top: 1px solid rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)

            # Filter Controls
            all_seasons = sorted(list({m['season'] for m in archive_data}))
            all_categories = sorted(list({cat for m in archive_data for cat in m.get('category', [])}))
            
            f_col1, f_col2, f_col3, f_col4 = st.columns([1.2, 1.5, 1.2, 1.8], gap="small")
            with f_col1:
                sel_season = st.selectbox("Season", ["All Seasons"] + [str(s) for s in all_seasons], key="mom_season")
            with f_col2:
                sel_cat = st.selectbox("Category", ["All Categories"] + all_categories, key="mom_cat")
            with f_col3:
                sel_imp = st.selectbox("Importance", ["All Ratings", "Essential", "Major", "Notable"], key="mom_imp")
            with f_col4:
                mom_search = st.text_input("🔍 Search Moment, Player, or Team", placeholder="e.g. Rinku, Dhoni, Malinga, 262...", key="mom_search_kw").strip().lower()

            # Filter data
            filtered_moments = archive_data
            if sel_season != "All Seasons":
                filtered_moments = [m for m in filtered_moments if str(m['season']) == sel_season]
            if sel_cat != "All Categories":
                filtered_moments = [m for m in filtered_moments if sel_cat in m.get('category', [])]
            if sel_imp != "All Ratings":
                filtered_moments = [m for m in filtered_moments if m.get('importance') == sel_imp]
            if mom_search:
                filtered_moments = [
                    m for m in filtered_moments
                    if mom_search in m['title'].lower() 
                    or mom_search in m['description'].lower() 
                    or any(mom_search in p.lower() for p in m.get('players', []))
                    or any(mom_search in t.lower() for t in m.get('teams', []))
                ]

            st.caption(f"Showing {len(filtered_moments)} of {len(archive_data)} iconic moments")

            # Render Cards (Zero indentation in HTML string to prevent code block parsing)
            for m in filtered_moments:
                imp = m.get('importance', 'Notable')
                border_c = '#ef4444' if imp == 'Essential' else ('#f59e0b' if imp == 'Major' else '#38bdf8')
                bg_badge = '#ef4444' if imp == 'Essential' else ('#f59e0b' if imp == 'Major' else '#0284c7')
                cats_badges = "".join([f'<span style="background: rgba(255,255,255,0.06); color: #cbd5e1; padding: 2px 8px; border-radius: 8px; font-size: 11px; margin-right: 5px;">{c}</span>' for c in m.get('category', [])])
                teams_str = " vs ".join(m.get('teams', []))

                card_content = (
                    f'<div style="background: #0d1527; border: 1px solid rgba(255,255,255,0.08); border-left: 4px solid {border_c}; border-radius: 12px; padding: 18px 20px; margin-bottom: 16px;">'
                    f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">'
                    f'<div><span style="background: rgba(245,158,11,0.15); color: #f59e0b; padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 700;">🏆 {m["season"]} IPL</span> '
                    f'<span style="background: rgba(255,255,255,0.08); color: #94a3b8; padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 600;">{m["match_stage"]}</span></div>'
                    f'<span style="background: {bg_badge}; color: #fff; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 800; text-transform: uppercase;">{imp}</span>'
                    f'</div>'
                    f'<h3 style="color: #f8fafc; font-size: 18px; font-weight: 800; margin: 4px 0 6px 0;">{m["title"]}</h3>'
                    f'<div style="color: #94a3b8; font-size: 13px; margin-bottom: 10px;">📅 {m["date"]} &bull; 📍 {m["venue"]} &bull; 🏏 {teams_str}</div>'
                    f'<div style="background: rgba(0,0,0,0.35); border-radius: 8px; padding: 8px 12px; color: #38bdf8; font-family: monospace; font-size: 13px; margin-bottom: 12px; border: 1px solid rgba(56,189,248,0.2);">🎯 {m["match_score"]}</div>'
                    f'<p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 0 0 10px 0;">{m["description"]}</p>'
                    f'<div style="background: rgba(245,158,11,0.05); border-left: 2px solid #f59e0b; padding: 6px 10px; margin-bottom: 12px; color: #fde68a; font-size: 13px;"><strong>Why Iconic:</strong> {m["why_iconic"]}</div>'
                    f'<div style="margin-bottom: 12px;">{cats_badges}</div>'
                    f'<div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 10px; display: flex; gap: 16px; flex-wrap: wrap;">'
                    f'<a href="{m["video_url"]}" target="_blank" style="color: #f59e0b; text-decoration: none; font-size: 13px; font-weight: 700;">📺 Watch Official Highlights &rarr;</a>'
                    f'<a href="{m["scorecard_url"]}" target="_blank" style="color: #38bdf8; text-decoration: none; font-size: 13px; font-weight: 700;">📊 ESPNcricinfo Scorecard &rarr;</a>'
                    f'<a href="{m["article_url"]}" target="_blank" style="color: #a78bfa; text-decoration: none; font-size: 13px; font-weight: 700;">📰 Match Report &rarr;</a>'
                    f'</div>'
                    f'</div>'
                )
                st.markdown(card_content, unsafe_allow_html=True)

    with tab_gallery:
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
            style_css = """<style>
.ipl-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px; padding: 10px 0; }
.ipl-gallery-item { position: relative; border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 6px 20px rgba(0,0,0,0.5); transition: transform 0.3s ease, border-color 0.3s ease; height: 280px; background: #090e18; }
.ipl-gallery-item:hover { transform: translateY(-5px); border-color: #f59e0b; box-shadow: 0 12px 30px rgba(245,158,11,0.25); }
.ipl-gallery-img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease; }
.ipl-gallery-item:hover .ipl-gallery-img { transform: scale(1.04); }
.ipl-gallery-caption { position: absolute; bottom: 0; left: 0; width: 100%; padding: 12px 14px; background: linear-gradient(to top, rgba(7,10,19,0.95) 0%, rgba(7,10,19,0.7) 60%, transparent 100%); box-sizing: border-box; }
.ipl-caption-title { font-size: 14px; font-weight: 700; color: #fef08a; margin: 0; text-transform: uppercase; letter-spacing: 0.5px; }
</style>"""
            
            gallery_items = []
            for img_name in sorted(img_files):
                img_p = os.path.join(img_folder, img_name)
                img_b64 = get_base64_image(img_p)
                if img_b64:
                    title_clean = os.path.splitext(img_name)[0].replace('_', ' ').replace('-', ' ').title()
                    item = (
                        f'<div class="ipl-gallery-item">'
                        f'<img class="ipl-gallery-img" src="{img_b64}" alt="{title_clean}" loading="lazy">'
                        f'<div class="ipl-gallery-caption"><p class="ipl-caption-title">{title_clean}</p></div>'
                        f'</div>'
                    )
                    gallery_items.append(item)
                    
            full_gallery = f'{style_css}<div class="ipl-gallery">{"".join(gallery_items)}</div>'
            st.markdown(full_gallery, unsafe_allow_html=True)
