import numpy as np

# ages = [22, 25, 30, 35, 40]

# array = np.array(ages)

# print(type(ages))
# print(type(array))
# print(array.dtype)

# heights = [5.6, 5.8, 6.1, 5.9]
# array_heights = np.array(heights)
# print(type(heights))
# print(type(array_heights))
# print(array_heights.dtype)

# cities = ["Bangalore", "Delhi", "Pune", "Mumbai"]
# cities_array = np.array(cities)
# print(type(cities))
# print(type(cities_array))
# print(cities_array.dtype)

# mixed = [100, "AI", 95.5]
# mixed_array = np.array(mixed)
# print(type(mixed))
# print(type(mixed_array))
# print(mixed_array.dtype)
# print(mixed_array)

# import numpy as np

# marks = np.array([80, 90, 75, 88, 95])

# print(marks)

# print(type(marks))

# print(marks.dtype)

# print(marks.shape)

# print(marks.ndim)

# print(marks.size)

# print(len(marks))



# import numpy as np

# marks = np.array([
#     [85, 90, 78],
#     [95, 88, 92],
#     [92, 85, 88]
# ])

# print(marks)

# print(type(marks))

# print(marks.dtype)

# print(marks.shape)

# print(marks.ndim)

# print(marks.size)

# print(len(marks))

import numpy as np

np.random.seed(1)
print(np.random.randint(1,10,5))

np.random.seed(42)
print(np.random.randint(1,10,5))

np.random.seed(100)
print(np.random.randint(1,10,5))
