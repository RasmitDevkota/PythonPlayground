import numpy as np
from numpy.linalg import inv

np.seterr('raise')

f = open("./qmatrix.txt", "r")
matrix = [line.strip().split(",") for line in f.readlines()]
matrix = np.array([[(int(float(entry.split("+")[0]))) for entry in row] for row in matrix])

np.savetxt('./qmatrix_formatted.txt', matrix, fmt="%i ")

# f = open("./qmatrix_formatted.txt", "w")
#
# for row in matrix:
#     for entry in row:
#         f.write(str(entry) + "  ")
#
#     f.write("\n")

print(matrix)

q0 = np.array([1, 0])
q1 = np.array([0, 1])

qc = np.kron(q1, q0)
qc = np.kron(qc, q1)

print(qc)

result = np.matmul(matrix, qc)
print(result)

check = np.matmul(inv(matrix), result)
check = check.astype(np.int_)
print(check)

prepared_states = np.array([1, 0, 1, 0, 1, 0, 1, 0])
desired_states = np.array([1, 0, 0, 1, 0, 1, 1, 0])

operation_matrix = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
])

result = np.matmul(operation_matrix, prepared_states)
print(result)
print(desired_states)

i = np.array([
    [1, 0],
    [0, 1],
])

x = np.array([
    [0, 1],
    [1, 0],
])

cx = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

swap = np.array([
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])

a = np.kron(i, cx)
b = np.kron(i, np.matmul(cx, np.kron(i, x)))
c = np.matmul(a, b)

# icx cx ix

composed_operation_matrix = np.kron(i, x)
print(composed_operation_matrix)

np.savetxt('./qmatrix_formatted.txt', composed_operation_matrix, fmt="%i ")
