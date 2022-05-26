import numpy as np

data_txt = open("./lapdata.txt", "r")

data = [line.replace("      ", ",").replace("  ", "").replace("\n", "").split(",") for line in data_txt.readlines()]

data_txt.close()

data_csv = open("./lapdata.csv", "w")

for drip in data:
    drip_num = drip[0]

    overall_time_raw = drip[1].split(":")
    overall_time = float(overall_time_raw[0]) * 60 + float(overall_time_raw[1])

    drip_time_raw = drip[2].split(":")
    print(drip_time_raw)
    drip_time = float(drip_time_raw[0]) * 60 + float(drip_time_raw[1])

    data_csv.write(f"{drip_num},{drip_time},{overall_time}\n")

data_csv.close()
