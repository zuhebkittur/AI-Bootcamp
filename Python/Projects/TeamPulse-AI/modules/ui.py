import streamlit as st

from modules.analytics import (
    get_total_chats,
    get_total_emails,
    get_request_handled_minutes,
    get_client_minutes,
    get_client_utilization,
    get_total_utilization,
    get_training_minutes,
    get_office_hour_minutes,
    get_total_minutes,
    get_other_minutes
)

from modules.charts import (
    create_task_minutes_chart,
    create_task_distribution_chart
)

from modules.insights import (
    generate_ai_insights
)

from modules.score import (
    calculate_productivity_score
)


# ==========================================================
# Productivity Score
# ==========================================================

def show_productivity_score(df):

    productivity_score = calculate_productivity_score(
        get_total_utilization(df),
        get_client_utilization(df),
        get_request_handled_minutes(df),
        get_training_minutes(df)
    )

    st.subheader("🔥 Productivity Score")

    col1, col2 = st.columns([1, 3])

    with col1:

        st.metric(
            "Today's Score",
            f"{productivity_score}/100"
        )

    with col2:

        if productivity_score >= 90:
            st.success("🟢 Excellent Productivity")

        elif productivity_score >= 75:
            st.warning("🟡 Good Productivity")

        else:
            st.error("🔴 Needs Improvement")

    st.divider()


# ==========================================================
# KPI Cards
# ==========================================================

def show_kpi_cards(df):

    st.subheader("📊 Productivity Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💬 Total Chats",
            get_total_chats(df)
        )

    with col2:
        st.metric(
            "📧 Total Emails",
            get_total_emails(df)
        )

    with col3:
        st.metric(
            "⏱ Request Minutes",
            get_request_handled_minutes(df)
        )

    with col4:
        st.metric(
            "🤝 Client Minutes",
            get_client_minutes(df)
        )

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            "📊 Client Utilization",
            f"{get_client_utilization(df)}%"
        )

    with col6:
        st.metric(
            "📈 Total Utilization",
            f"{get_total_utilization(df)}%"
        )

    with col7:
        st.metric(
            "🎓 Training",
            get_training_minutes(df)
        )

    with col8:
        st.metric(
            "🏢 Office Hours",
            get_office_hour_minutes(df)
        )

    st.divider()


# ==========================================================
# Overall Productivity
# ==========================================================

def show_overall_productivity(df):

    st.subheader("⏳ Overall Productivity")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🕒 Total Minutes Worked",
            get_total_minutes(df)
        )

    with col2:

        st.metric(
            "📝 Other Minutes",
            get_other_minutes(df)
        )

    st.divider()


# ==========================================================
# Charts
# ==========================================================

def show_charts(df):

    st.subheader("📈 Productivity Analytics")

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            create_task_minutes_chart(df),
            use_container_width=True
        )

    with col2:

        st.plotly_chart(
            create_task_distribution_chart(df),
            use_container_width=True
        )

    st.divider()


# ==========================================================
# AI Insights
# ==========================================================

def show_ai_insights(df):

    st.subheader("🤖 AI Productivity Insights")

    insights = generate_ai_insights(df)

    for insight in insights:
        st.info(insight)

    st.divider()


# ==========================================================
# Activity Table
# ==========================================================

def show_activity_table(df):

    st.subheader("📋 Activity Timeline")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()