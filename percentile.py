points = [3, 4, 10]
data = [5, 10, 4, 6, 7, 2, 3, 4, 5, 7]

def percentile(x, data):
    count = 0.5

    for i in data:
        if i < x:
            count += 1

    return 100 * count / len(data)

for i in points:
    print(percentile(i, data))
