import asyncio
import numpy as np
from numpy import average
from numpy import var
from scipy.stats import kurtosis
from scipy.stats import probplot
from scipy.stats import loggamma
from matplotlib import pyplot as plt

np.seterr('raise')

f = open("./DJIA.csv", "r")
data = [line.strip() for line in f.readlines()]

data.pop(0)
data.pop(0)

data = [datum.split(",") for datum in data]
data = filter((lambda datum: datum[1] != "."), data)
data = [[datum[0], float(datum[1])] for datum in data]

dates = [datum[0] for datum in data]
prices = [datum[1] for datum in data]
rounded_prices = [round(datum[1]) for datum in data]
_, price_counts = np.unique(prices, return_counts=True)

global_average = average(prices)
global_variance = var(prices)
global_kurtosis = kurtosis(prices)

print(global_average, global_variance, global_kurtosis)

max_peak_strength = [0, 0, 0]
peak_strengths = []

def normal_dist(x, mean, sd):
    if sd == 0:
        print("Standard deviation cannot be equal to 0")

        return None
    else:
        prob_density = (np.pi * sd) * np.exp(-0.5 * ((x - mean) / sd) ** 2)

        return prob_density

async def calculate_distros(i):
    final_result = [0, 0, 0]

    for j in range(min(i, len(prices) - i + 1)):
        local_sample = []

        for k in range(-j, j + 1):
            local_sample.append(prices[k])

        if len(local_sample) < 30:
            continue

        local_sample_average = average(local_sample)
        local_sample_variance = var(local_sample)

        local_peak_strength = 0

        for k in range(len(local_sample)):
            local_peak_strength += abs(prices[k] - normal_dist(prices[k], local_sample_average, local_sample_variance ** 2))

        if local_peak_strength < max_peak_strength[2] or max_peak_strength[2] == 0:
            max_peak_strength[0], max_peak_strength[1], max_peak_strength[2] = i, j, local_peak_strength
            final_result[0], final_result[1], final_result[2] = i, j, local_peak_strength

        peak_strengths.append([i, j, local_peak_strength])

    print("Task #" + str(i) + " finished with result: " + str(final_result))

def main():
    for i in range(len(prices)):
        print("Task #" + str(i) + " started")

        asyncio.run(calculate_distros(i))

main()

print(max_peak_strength)

hist = plt.hist(prices, bins=500)
plt.show()

figure = plt.figure()
plot = figure.add_subplot(111)
npp = probplot(prices, dist=loggamma, sparams=(global_average ** 2/global_variance, global_variance/global_average), plot=plot)
# plt.show()
