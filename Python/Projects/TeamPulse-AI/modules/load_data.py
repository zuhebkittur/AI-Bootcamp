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

    return df