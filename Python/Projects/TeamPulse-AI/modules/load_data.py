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

    # Convert Total Time to Timedelta
    df["Total Time"] = pd.to_timedelta(df["Total Time"].astype(str))

    # Create a new column with total minutes
    df["Total Minutes"] = (
        df["Total Time"].dt.total_seconds() / 60
    ).astype(int)

    return df