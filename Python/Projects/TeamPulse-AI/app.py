import streamlit as st
from datetime import datetime

# ==========================================================
# Import Modules
# ==========================================================

from modules.load_data import load_data

from modules.dashboard import (
    show_header,
    show_sidebar
)
from modules.filters import (
    show_filters,
    apply_filters
)
import inspect
from modules import filters


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
# Dashboard Information
# ==========================================================

employee_name = "Zuheb"

current_date = datetime.now().strftime("%d-%b-%Y")

current_time = datetime.now().strftime("%I:%M %p")

current_week = df["Week"].max()

total_records = len(df)

# ==========================================================
# Sidebar
# ==========================================================

show_sidebar(
    employee_name,
    current_date,
    current_time,
    current_week,
    total_records
)

# ==========================================================
# Filters
# ==========================================================

from_date, to_date, selected_task = show_filters(df)

filtered_df = apply_filters(
    df=df,
    from_date=from_date,
    to_date=to_date,
    selected_task=selected_task
)

# ==========================================================
# Header
# ==========================================================

show_header()

# ==========================================================
# Productivity Score
# ==========================================================

show_productivity_score(filtered_df)

# ==========================================================
# KPI Cards
# ==========================================================

show_kpi_cards(filtered_df)

# ==========================================================
# Overall Productivity
# ==========================================================

show_overall_productivity(filtered_df)

# ==========================================================
# Charts
# ==========================================================

show_charts(filtered_df)

# ==========================================================
# AI Insights
# ==========================================================

show_ai_insights(filtered_df)

# ==========================================================
# Activity Timeline
# ==========================================================

show_activity_table(filtered_df)

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "🚀 TeamPulse AI v1.0 | Built by Zuheb using Python, Pandas & Streamlit"
)