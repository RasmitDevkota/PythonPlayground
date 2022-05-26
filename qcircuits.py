import numpy as np
from matplotlib import pyplot as plt

np.seterr('raise')

f = open("./qresults.txt", "r")
data = [line.strip().replace("\t", " ").split(" ") for line in f.readlines()]

vectors = [[float(result[0].split("+")[0]), float(result[0].split("+")[1][:-1])] for result in data]
states = [result[1][1:-1] for result in data]
probabilities = [float(result[2][:-1]) for result in data]

sums = []
answers = []

for state in states:
    sums.append((int(state[0]) + int(state[1]) + int(state[2]) + int(state[3]) + int(state[4])))
    answers.append(int(state[-3]) * 4 + int(state[-2]) * 2 + int(state[-1]))

plt.plot(sums, answers, "o")
plt.show()
