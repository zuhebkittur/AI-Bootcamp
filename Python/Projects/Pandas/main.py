# import os

# print(os.getcwd())
# import pandas as pd

# df = pd.read_csv("employees.csv")

# print(df)
import os
import pandas as pd

current_folder = os.path.dirname(__file__)

csv_path = os.path.join(current_folder, "employees.csv")

df = pd.read_csv(csv_path)

print(df)