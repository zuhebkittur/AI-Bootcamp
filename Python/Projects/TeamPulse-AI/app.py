import streamlit as st

# ==========================================================
# Import Modules
# ==========================================================

from modules.load_data import load_data

from modules.dashboard import (
    show_header,
    show_sidebar
)

from modules.ui import (
    show_productivity_score,
    show_kpi_cards,
    show_overall_productivity,
    show_charts,
    show_ai_insights,
    show_activity_table
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="TeamPulse AI",
    page_icon="🚀",
    layout="wide"
)

# ==========================================================
# Load Data
# ==========================================================

df = load_data()

# ==========================================================
# Header & Sidebar
# ==========================================================

show_sidebar()

show_header()

# ==========================================================
# Productivity Score
# ==========================================================

show_productivity_score(df)

# ==========================================================
# KPI Cards
# ==========================================================

show_kpi_cards(df)

# ==========================================================
# Overall Productivity
# ==========================================================

show_overall_productivity(df)

# ==========================================================
# Charts
# ==========================================================

show_charts(df)

# ==========================================================
# AI Insights
# ==========================================================

show_ai_insights(df)

# ==========================================================
# Activity Timeline
# ==========================================================

show_activity_table(df)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "🚀 TeamPulse AI v1.0 | Built by Zuheb using Python, Streamlit & Plotly"
)