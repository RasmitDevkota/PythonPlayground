import numpy as np

f = open("eventassignments_seniors.csv", "r")

events = [line.strip().split(",") for line in f.readlines()]

teammates = {

}

for event in events:
    event_name = event[0]
    event_members = event[1:]

    for member in event_members:
        if member in list(teammates.keys()):
            member_events = list(teammates[member])
            member_events.append(event_name)

            teammates[member] = member_events
        else:
            teammates[member] = [event_name]

print(teammates)

f.close()

f = open("eventassignments_seniors_formatted.csv", "a")

f.write("Event Assignments,\n")

for teammate in teammates.keys():
    f.write(teammate)
    f.write(",")
    f.write(",".join(list(teammates[teammate])))
    f.write(",\n")

print("Done!")
