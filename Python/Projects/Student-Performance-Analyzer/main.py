import os
import pandas as pd
current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "student_data.csv")
df = pd.read_csv(csv_path)
print(df)

#Task 1
# Print:
# Head
# Shape
# Info
# Describe
print("=" * 50)
print("TASK 1")
print("=" * 50)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Task 2
# Create a new column:
# Total = Math + Science + English
print("=" * 50)
print("TASK 2")
print("=" * 50)

df["Total"] = df["Math"] + df["Science"] + df["English"]
print(df["Total"])

# Task 3
# Create another column:
# Average = Total / 3
print("=" * 50)
print("TASK 3")
print("=" * 50)
print(f"Average : {df["Total"] / 3}")

df["Average"] = df["Total"] / 3
print(df["Average"])

# Task 4
print("=" * 50)
print("TASK 4")
print("=" * 50)

def result(avg):
    if avg >= 40:
        return "Pass"
    else:
        return "Fail"

df["Result"] = df["Average"].apply(result)
print(df)

# Task 5
# Task 5 – Statistics
# Find:
#  Highest Total Marks
#  Lowest Total Marks
#  Average Marks of the Class

print("=" * 50)
print("TASK 5")
print("=" * 50)

print(f"Highest Total Marks : {df["Total"].max()}")
print(f"Lowest Total Marks : {df["Total"].min()}")
print(f"Average Marks of the Class : {df["Total"].mean()}")


# Task 6 – Filter Data
# Show:
#  Only Bangalore students
#  Only students from Delhi
#  Students whose Average > 85
#  Students who Failed
print("=" * 50)
print("Task 6 – Filter Data")
print("=" * 50)


print(
    df[
        df["City"] == "Bangalore"
    ][
        ["Student", "City"]
    ]
)

print(
    df[
        df["City"] == "Delhi"
    ][
        ["Student", "City"]
    ]
)

print(
    df[
        df["Average"] > 85
    ][  
        ["Student", "Average"]
    ]
)

print(
    df[
        df["Average"] < 40
    ][  
        ["Student", "Average"]
    ]
    
)

# Task 7
# Sort the data by:
# Highest Total Marks
# Highest Average
# Student Name (A–Z)
print("=" * 50)
print("Task 7")
print("=" * 50)


print(
    df.sort_values("Total", ascending=False)[
        ["Student", "Total"]
    ]
)

print(
    df.sort_values("Average", ascending=False)[
        ["Student", "Average"]
    ]
)

print(
    df.sort_values("Student")[
        ["Student", "Total", "City"]
    ]
)

# Task 8 – Top Performers
# Show:
#  Top 3 Students
#  Bottom 3 Students
print("=" * 50)
print("Task 8")
print("=" * 50)


print(
    df.sort_values("Total").head(3)[
        ["Student", "Total"]
    ]
)

print(
    df.sort_values("Total").tail(3)[
        ["Student", "Total"]
    ]
)

# Task 9 – Group By
# Find:
#  Average Marks by City
#  Number of Students in each City
#  Highest Average in each City

print("=" * 50)
print("Task 9 – Group By")
print("=" * 50)

average_marks_by_city = df.groupby("City")["Average"].mean()
for City, Average in average_marks_by_city.items():
    print(f"{City:<12} : {Average:.2f}")

students_per_city = df.groupby("City").size()
for city, count in students_per_city.items():
    print(f"{city:<12} : {count}")

highest_avg_each_city = df.groupby("City")["Average"].max()
for City, Average in highest_avg_each_city.items():
    print(f"{City:<12} : {Average:.2f}")
