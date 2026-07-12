import os
import pandas as pd


# ============================
# Load CSV File
# ============================

current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "running_data.csv")

df = pd.read_csv(csv_path)


# ============================
# Running Data Analyzer
# ============================

print("=" * 50)
print("🏃 RUNNING DATA ANALYZER")
print("=" * 50)

# Dataset Information
print(f"📊 Total Runs          : {len(df)}")
print(f"📏 Average Distance    : {df['Distance_km'].mean():.2f} km")
print(f"🏆 Longest Run         : {df['Distance_km'].max()} km")
print(f"🔥 Total Calories      : {df['Calories'].sum()} kcal")
print(f"❤️ Average Heart Rate : {df['Heart_Rate'].mean():.2f} bpm")

print("=" * 50)

# Distance by Runner
print("🏅 TOTAL DISTANCE BY RUNNER")
print("-" * 50)

distance_by_runner = df.groupby("Runner")["Distance_km"].sum()

for runner, distance in distance_by_runner.items():
    print(f"{runner:<10} : {distance} km")

print("=" * 50)

# Average Pace
print("⚡ AVERAGE PACE BY RUNNER")
print("-" * 50)

pace_by_runner = df.groupby("Runner")["Pace_min_per_km"].mean()

for runner, pace in pace_by_runner.items():
    print(f"{runner:<10} : {pace:.2f} min/km")

print("=" * 50)

# Longest Runs
print("🏃 TOP LONGEST RUNS")
print("-" * 50)

print(
    df.sort_values("Distance_km", ascending=False)[
        ["Runner", "Distance_km", "Calories"]
    ]
)

print("=" * 50)

# Bangalore Runners
print("📍 RUNS IN BANGALORE")
print("-" * 50)

print(
    df[df["City"] == "Bangalore"][
        ["Runner", "Distance_km", "Calories"]
    ]
)

print("=" * 50)

# Runs Greater Than 10 KM
print("🏅 RUNS GREATER THAN 10 KM")
print("-" * 50)

print(
    df[df["Distance_km"] > 10][
        ["Runner", "Distance_km", "Calories"]
    ]
)

print("=" * 50)

# Best Runner
top_runner = distance_by_runner.idxmax()
top_distance = distance_by_runner.max()

print(f"🥇 TOP RUNNER          : {top_runner}")
print(f"🏆 TOTAL DISTANCE      : {top_distance} km")

print("=" * 50)

# Save Report
output_path = os.path.join(current_folder, "running_analysis.csv")
df.to_csv(output_path, index=False)

print(f"✅ Report saved successfully!")
print(f"📂 File: {output_path}")

print("=" * 50)