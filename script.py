results_file = open("results.txt", "r")

total = 0
count = 0

for line in results_file.readlines():
    if "<PIL." in line:
        total += float(line.split(" ")[-1])
        count += 1

average_score = total/count

print(total)
print(count)
print(average_score)
