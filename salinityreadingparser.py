import numpy as np

readings_csv = open("./readings.csv", "r")

readings = (np.array([line.replace("\n", "").split(",") for line in readings_csv.readlines()]).T)[1::]

readings_csv.close()

readings = [[(reading[l].split("= ")[1] if "=" in reading[l] else "") if l > 0 else reading[l] for l in range(len(reading))] for reading in readings]

readings = [list(filter(lambda value: not value == "", reading)) for reading in readings]

readings = list(filter(lambda reading: not reading == [] and not reading[0] == "", readings))

for r in range(len(readings)):
    ml_params = readings[r][0].split("/")

    ml_normalsaline = float(ml_params[0])
    ml_water = float(ml_params[1])

    ppm = round(ml_normalsaline/(ml_normalsaline + ml_water) * 0.009 * 1000000, 3)

    readings[r][0] = str(ppm)

print(readings)

readings_formatted_csv = open("./readings_formatted.csv", "w")

readings_formatted_csv.write(",,".join(["Voltage,True Salinity,Detected Salinity,Absolute Error,% Error" for _ in range(len(readings))]) + "\n")

for v in range(1, len(max(readings, key=len)), 2):
    for r in range(len(readings)):
        reading = readings[r]

        readings_formatted_csv.write(reading[v] if v < len(reading) - 1 else "")
        readings_formatted_csv.write(",")
        readings_formatted_csv.write(reading[0] if v < len(reading) - 1 else "")
        readings_formatted_csv.write(",")
        readings_formatted_csv.write(reading[v + 1] if v < len(reading) - 1 else "")
        readings_formatted_csv.write(",")
        readings_formatted_csv.write(str(float(reading[v + 1]) - float(reading[0])) if v < len(reading) - 1 else "")
        readings_formatted_csv.write(",")
        readings_formatted_csv.write(str(round((float(reading[v + 1]) - float(reading[0]))/float(reading[0]) * 100, 3)) + "%" if v < len(reading) - 1 and not reading[0] == "0.0" else "")
        readings_formatted_csv.write(",," if r < len(readings) - 1 else "\n")

readings_formatted_csv.close()

readings_combined_formatted_csv = open("./readings_combined_formatted.csv", "w")

readings_combined_formatted_csv.write("Voltage,True Salinity,Detected Salinity,Absolute Error,% Error\n")

for r in range(len(readings)):
    reading = readings[r]

    for v in range(1, len(max(readings, key=len)), 2):
        if v < len(reading) - 1:
            readings_combined_formatted_csv.write(reading[v])
            readings_combined_formatted_csv.write(",")
            readings_combined_formatted_csv.write(reading[0])
            readings_combined_formatted_csv.write(",")
            readings_combined_formatted_csv.write(reading[v + 1])
            readings_combined_formatted_csv.write(",")
            readings_combined_formatted_csv.write(str(float(reading[v + 1]) - float(reading[0])))
            readings_combined_formatted_csv.write(",")
            readings_combined_formatted_csv.write(str(round((float(reading[v + 1]) - float(reading[0]))/float(reading[0]) * 100, 3)) + "%" if not reading[0] == "0.0" else "")
            readings_combined_formatted_csv.write("\n")

readings_combined_formatted_csv.close()

print(readings)
