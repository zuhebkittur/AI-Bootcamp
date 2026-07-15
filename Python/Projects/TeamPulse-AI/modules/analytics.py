import pandas as pd

from modules.constants import (
    PROCESSING_CHAT,
    PROCESSING_EMAIL,
    OFFICE_HOURS,
    TRAINING,
    OTHERS,
    CHAT_EMAIL_CLARIFICATION
)


# ==========================================
# Helper Functions
# ==========================================

def get_minutes_by_task(df, task_name):
    """
    Calculate total minutes for a given task.

    Parameters:
        df (DataFrame): Productivity data
        task_name (str): Task name

    Returns:
        int: Total minutes
    """

    return df[
        df["Task"] == task_name
    ]["Total Minutes"].sum()


# ==========================================
# Chat Analytics
# ==========================================

def get_total_chats(df):
    """
    Count total Processing Chat tasks.
    """

    return len(
        df[df["Task"] == PROCESSING_CHAT]
    )


# ==========================================
# Email Analytics
# ==========================================

def get_total_emails(df):
    """
    Count total Processing Email tasks.
    """

    return len(
        df[df["Task"] == PROCESSING_EMAIL]
    )


# ==========================================
# Request Handled Minutes
# ==========================================

def get_request_handled_minutes(df):
    """
    Processing Chat Minutes +
    Processing Email Minutes
    """

    chat_minutes = get_minutes_by_task(
        df,
        PROCESSING_CHAT
    )

    email_minutes = get_minutes_by_task(
        df,
        PROCESSING_EMAIL
    )

    return chat_minutes + email_minutes


# ==========================================
# Office Hour Minutes
# ==========================================

def get_office_hour_minutes(df):
    """
    Office Hour Minutes
    """

    return get_minutes_by_task(
        df,
        OFFICE_HOURS
    )


# ==========================================
# Training Minutes
# ==========================================

def get_training_minutes(df):
    """
    Training Minutes
    """

    return get_minutes_by_task(
        df,
        TRAINING
    )


# ==========================================
# Other Minutes
# ==========================================

def get_other_minutes(df):
    """
    Other Minutes
    """

    return get_minutes_by_task(
        df,
        OTHERS
    )


# ==========================================
# Client Minutes
# ==========================================

def get_client_minutes(df):
    """
    Client Minutes

    Office Hours +
    Chat/Email Clarification
    """

    office_minutes = get_minutes_by_task(
        df,
        OFFICE_HOURS
    )

    clarification_minutes = get_minutes_by_task(
        df,
        CHAT_EMAIL_CLARIFICATION
    )

    return office_minutes + clarification_minutes


# ==========================================
# Total Minutes
# ==========================================

def get_total_minutes(df):
    """
    Total Minutes
    """

    return df["Total Minutes"].sum()


# ==========================================
# Client Utilization
# ==========================================

def get_client_utilization(df):
    """
    Client Utilization Percentage
    """

    total_minutes = get_total_minutes(df)

    if total_minutes == 0:
        return 0

    client_minutes = get_client_minutes(df)

    utilization = (
        client_minutes / total_minutes
    ) * 100

    return round(utilization, 2)


# ==========================================
# Total Utilization
# ==========================================

def get_total_utilization(df, office_minutes=540):
    """
    Total Utilization Percentage

    office_minutes = 9 Hours
    """

    total_minutes = get_total_minutes(df)

    utilization = (
        total_minutes / office_minutes
    ) * 100

    return round(utilization, 2)