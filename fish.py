import numpy as np
from scipy import ndimage

u = np.array([
    [100,100,100,100,100],
    [100,0,0,0,100],
    [100,0,0,0,100],
    [100,0,0,0,100],
    [100,100,100,100,100]
])

fishArray = u

M, N = np.shape(fishArray)

for i in range(0, M):
    for j in range(0, N):
        if not(i == 0 or i == M - 1 or j == 0 or j == N - 1):
            average = (u[i-1][j] + u[i+1][j] + u[i][j-1] + u[i][j+1])/4

            fishArray[i][j] = average

print(fishArray)

v = np.array([
    [100,100,100,100,100],
    [100,0,0,0,100],
    [100,0,0,0,100],
    [100,0,0,0,100],
    [100,100,100,100,100]
])

k = np.array([
    [0, 0.25, 0],
    [0.25, 0, 0.25],
    [0, 0.25, 0]
])

print(ndimage.convolve(v, k, mode='constant', cval=100.0))
