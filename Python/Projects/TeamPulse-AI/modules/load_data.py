import os
import pandas as pd


def load_data():

    current_folder = os.path.dirname(__file__)
    project_folder = os.path.dirname(current_folder)

    excel_path = os.path.join(
        project_folder,
        "data",
        "productivity_tracker.xlsx"
    )

    df = pd.read_excel(excel_path)

    # Convert Processing Date
    df["Processing Date"] = pd.to_datetime(
        df["Processing Date"],
        dayfirst=True
    )

    # Convert Total Time
    df["Total Time"] = pd.to_timedelta(
        df["Total Time"].astype(str)
    )

    # Total Minutes
    df["Total Minutes"] = (
        df["Total Time"]
        .dt.total_seconds() / 60
    ).astype(int)

    return df