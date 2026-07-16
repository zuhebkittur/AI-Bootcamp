import streamlit as st
import pandas as pd


# ==========================================================
# Sidebar Filters
# ==========================================================

def show_filters(df):

    # st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Filters")

    # Ensure Processing Date is datetime
    df["Processing Date"] = pd.to_datetime(df["Processing Date"])

    min_date = df["Processing Date"].min().date()
    max_date = df["Processing Date"].max().date()

    # ==========================================================
    # Date Range
    # ==========================================================

    from_date = st.sidebar.date_input(
        "📅 From Date",
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )

    to_date = st.sidebar.date_input(
        "📅 To Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )

    # ==========================================================
    # Task Filter
    # ==========================================================

    # tasks = sorted(df["Task"].dropna().unique())

    # selected_task = st.sidebar.selectbox(
    #     "📋 Task",
    #     ["All"] + tasks
    # )
    selected_task = "All"

    return (
        from_date,
        to_date,
        selected_task
    )


# ==========================================================
# Apply Filters
# ==========================================================

def apply_filters(
    df,
    from_date,
    to_date,
    selected_task
):

    filtered_df = df.copy()

    filtered_df["Processing Date"] = pd.to_datetime(
        filtered_df["Processing Date"]
    )

    filtered_df = filtered_df[
        (
            filtered_df["Processing Date"].dt.date >= from_date
        )
        &
        (
            filtered_df["Processing Date"].dt.date <= to_date
        )
    ]

    if selected_task != "All":

        filtered_df = filtered_df[
            filtered_df["Task"] == selected_task
        ]

    return filtered_df