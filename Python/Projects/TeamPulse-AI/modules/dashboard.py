import streamlit as st


def show_header():

    st.title("🚀 TeamPulse AI")

    st.caption(
        "Personal Productivity Intelligence Dashboard"
    )

    st.divider()


def show_sidebar():

    with st.sidebar:

        st.title("🚀 TeamPulse AI")

        st.markdown("---")

        st.subheader("👤 Employee")

        st.success("Zuheb")

        st.markdown("---")

        st.info("📅 Date : 15-Jul-2026")

        st.info("📆 Week : 1")

        st.success("🟢 Connected")

        st.markdown("---")

        st.caption("Version 1.0")