def generate_ai_insights(df):

    insights = []

    # Total Utilization
    total_minutes = df["Total Minutes"].sum()

    if total_minutes >= 480:
        insights.append("🟢 Excellent productivity today.")
    elif total_minutes >= 360:
        insights.append("🟡 Good productivity. There's room for improvement.")
    else:
        insights.append("🔴 Productivity is below the expected working hours.")

    # Training
    training_minutes = df[
        df["Task"] == "Training"
    ]["Total Minutes"].sum()

    if training_minutes == 0:
        insights.append(
            "📚 No training completed today."
        )
    else:
        insights.append(
            f"🎓 Training completed for {training_minutes} minutes."
        )

    # Email vs Chat
    email_minutes = df[
        df["Task"] == "Processing Email"
    ]["Total Minutes"].sum()

    chat_minutes = df[
        df["Task"] == "Processing Chat"
    ]["Total Minutes"].sum()

    if email_minutes > chat_minutes:
        insights.append(
            "📧 More time was spent handling emails than chats."
        )
    elif chat_minutes > email_minutes:
        insights.append(
            "💬 More time was spent handling chats than emails."
        )

    return insights