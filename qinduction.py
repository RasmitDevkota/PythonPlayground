import numpy as np

np.seterr('raise')

f = open("./qresults.txt", "r")
data = [line.strip().replace("\t", " ").split(" ") for line in f.readlines()]

vectors = [[float(result[0].split("+")[0]), float(result[0].split("+")[1][:-1])] for result in data]
states = [result[1][1:-1] for result in data]
probabilities = [float(result[2][:-1]) for result in data]

state_groups = [0 for i in range(0, len(str(states[0])))]

for i in range(0, len(str(states[0]))):
    match_groups = [0 for i in range(0, len(str(states[0])))]

    for state in states:
        for j in range(0, len(str(states[0]))):
            if not i == j:
                index = 2 * int(state[i]) + int(state[j])

                match_groups[index] = match_groups[index] + 1

    state_groups[i] = match_groups

print(state_groups)
