import numpy as np

# 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours)
print(hours.shape, hours.ndim, hours.size, hours.dtype)

# 2
print(hours[2:3][0])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

# 3
temperatures = np.array((
    (12, 14, 13, 15),
    (11, 13, 16, 17),
    (10, 12, 15, 18),
))

print(temperatures.shape, temperatures.ndim, temperatures.size)
print(temperatures[1, 2])
print(temperatures[0, :])
print(temperatures[:, -1])
print(temperatures[:2, 1:])

mid = temperatures[:2, 1:3]
print(mid, mid.shape)

# 4
matrix = np.arange(1, 26).reshape(5, 5)

s1 = matrix[:3]
print(s1, s1.shape)

s2 = matrix[-2:]
print(s2, s2.shape)

s3 = matrix[:, :2]
print(s3, s3.shape)

s4 = matrix[1:4, 2:5]
print(s4, s4.shape)

s5 = matrix[-2:, -2:]
print(s5, s5.shape)

# 5
vector = np.array((10, 20, 30, 40, 50))
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# без .copy() поменяется исходный массив hours, т.к. будет ссылка на те же данные
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix)
print(matrix)

# 6
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print(numbers.shape, table.shape, transposed.shape)