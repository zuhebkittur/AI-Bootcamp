import streamlit as st


# ==========================================================
# Sidebar Filters
# ==========================================================

def show_filters(df):
    """
    Display sidebar filters and return the selected values.
    """

    st.sidebar.markdown("---")
    st.sidebar.subheader("🎛 Filters")

    # Date Filter
    dates = sorted(df["Processing Date"].dropna().unique())

    selected_date = st.sidebar.selectbox(
        "📅 Select Date",
        options=["All"] + list(dates)
    )

    # Week Filter
    weeks = sorted(df["Week"].dropna().unique())

    selected_week = st.sidebar.selectbox(
        "📆 Select Week",
        options=["All"] + list(weeks)
    )

    # Task Filter
    tasks = sorted(df["Task"].dropna().unique())

    selected_task = st.sidebar.selectbox(
        "📋 Select Task",
        options=["All"] + list(tasks)
    )

    return selected_date, selected_week, selected_task


# ==========================================================
# Apply Filters
# ==========================================================

def apply_filters(
    df,
    selected_date,
    selected_week,
    selected_task
):
    """
    Filter dataframe based on selected filters.
    """

    filtered_df = df.copy()

    if selected_date != "All":
        filtered_df = filtered_df[
            filtered_df["Processing Date"] == selected_date
        ]

    if selected_week != "All":
        filtered_df = filtered_df[
            filtered_df["Week"] == selected_week
        ]

    if selected_task != "All":
        filtered_df = filtered_df[
            filtered_df["Task"] == selected_task
        ]

    return filtered_df