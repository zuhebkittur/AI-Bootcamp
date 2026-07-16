import streamlit as st


# ==========================================================
# Header
# ==========================================================

def show_header():

    st.title("🚀 TeamPulse AI")

    st.caption(
        "Personal Productivity Intelligence Dashboard"
    )

    st.divider()


# ==========================================================
# Sidebar
# ==========================================================

def show_sidebar(
    employee_name,
    current_date,
    current_time,
    current_week,
    total_records
):

    with st.sidebar:

        st.title("🚀 TeamPulse AI")

        st.markdown("---")

        st.subheader("👤 Employee")

        st.success(employee_name)

        st.markdown("---")

        st.info(f"📅 Date : {current_date}")

        st.info(f"🕒 Time : {current_time}")

        st.info(f"📆 Week : {current_week}")

        st.info(f"📊 Records : {total_records}")

        st.success("🟢 Connected")

        st.markdown("---")

        st.caption("Version 1.0")