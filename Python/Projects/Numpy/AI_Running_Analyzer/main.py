import numpy as np
runners = np.array([
    [5, 400, 145, 10],
    [7, 550, 155, 11],
    [10, 780, 165, 13],
    [8, 620, 160, 12],
    [6, 480, 150, 10]
])

runner_names = np.array([
    "Rahul",
    "Priya",
    "Zuheb",
    "Amit",
    "Neha"
])

print(runners)
print(np.shape)
print(runners.ndim)
print(runners.size)
print(runners.dtype)

distance = runners[:,0]
calories = runners[:,1]
heart_rate = runners[:,2]
speed = runners[:,3]

print(distance)
print(calories)
print(heart_rate)
print(speed)

# Average Distance
# Average Heart Rate
# Average Speed
# Total Calories
# Maximum Distance
# Minimum Distance
# Maximum Calories
# Minimum Calories

print(f"Average Distance : {np.mean(distance):.2f} km")
print(f"Average Heart Rate : {np.mean(heart_rate):.2f} BPM")
print(f"Average Speed : {np.mean(speed):.2f} km/h")
print(f"Total Calories : {np.sum(calories)}")
print(f"Maximum Distance : {np.max(distance)} km")
print(f"Minimum Distance : {np.min(distance)} km")
print(f"Maximum Calories : {np.max(calories)}")
print(f"Minimum Calories : {np.min(calories)}")

# The runner with the longest distance
# The runner with the highest calories
# The runner with the highest heart rate
# The runner with the highest speed


best_runner = np.argmax(distance)
runner = runners[best_runner]

print("=" * 40)
print("BEST RUNNER")
print("=" * 40)

print(f"Name         : {runner_names[best_runner]}")
print(f"Distance     : {runner[0]} km")
print(f"Calories     : {runner[1]}")
print(f"Heart Rate   : {runner[2]} BPM")
print(f"Speed        : {runner[3]} km/h")