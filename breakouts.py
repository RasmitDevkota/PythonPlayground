import numpy as np

def breakouts_09292021():
    f = open("eventassignments_final.csv", "r")

    teammates = [line.strip().split(",") for line in f.readlines()]

    event_counts = {
        "A&P": 0,
        "Ast": 0,
        "Cell": 0,
        "DD": 0,
        "DP": 0,
        "EC": 0,
        "GG": 0,
        "Orn": 0,
        "RS": 0,
        "R&M": 0,
        "ChL": 0,
        "Code": 0,
        "DB": 0,
        "For": 0,
        "IAT": 0,
        "WFL": 0
    }

    event_members = {
        "A&P": [],
        "Ast": [],
        "Cell": [],
        "DD": [],
        "DP": [],
        "EC": [],
        "GG": [],
        "Orn": [],
        "RS": [],
        "R&M": [],
        "ChL": [],
        "Code": [],
        "DB": [],
        "For": [],
        "IAT": [],
        "WFL": []
    }

    for teammate in teammates:
        for i in range(16):
            event_i = list(event_counts.keys())[i]

            if event_i in teammate:
                event_counts[event_i] = event_counts[event_i] + 1

    event_overlap = np.zeros((16, 16))

    for teammate in teammates:
        for i in range(16):
            event_i = list(event_counts.keys())[i]

            if event_i in teammate:
                event_counts[event_i] = event_counts[event_i] + 1

                for j in range(16):
                    event_j = list(event_counts.keys())[j]

                    if event_i != event_j and event_j in teammate:
                        event_overlap[i][j] = event_overlap[i][j] + 1

    event_overlap_list = []

    for i in range(16):
        event_i = list(event_counts.keys())[i]

        for j in range(16):
            if i != j and event_overlap[i][j] > 0:
                event_j = list(event_counts.keys())[j]

                overlap_count = int(event_overlap[i][j])

                overlap = "{} and {} - {}".format(event_i, event_j, overlap_count)
                reverse_overlap = "{} and {} - {}".format(event_j, event_i, overlap_count)

                if reverse_overlap not in event_overlap_list:
                    event_overlap_list.append(overlap)

    event_overlap_list = sorted(event_overlap_list, key=lambda overlap: overlap.split(" - ")[1], reverse=True)

    event_assignments_final = open("eventassignments_final_formatted.csv", "a")

    for i in range(16):
        event_i = list(event_counts.keys())[i]

        for teammate in teammates:
            if event_i in teammate:
                event_members_list = list(event_members[event_i])
                event_members_list.append(teammate[0])

                event_members[event_i] = event_members_list

        event_assignments_final.write(event_i)
        event_assignments_final.write(",")
        event_assignments_final.write(",".join(list(event_members[event_i])))
        event_assignments_final.write(",\n")

    event_assignments_final.close()

    print(event_counts)
    print(event_overlap)
    print("\n".join(event_overlap_list))
    print("Average Overlap:", np.average(event_overlap) * 256 / (256 - 16))

def breakouts_09152021():
    f = open("eventassignments_old.csv", "r")

    teammates = [line.strip().split(",") for line in f.readlines()]

    min_members = 6
    max_members = 10

    event_counts = {
        "A&P": 0,
        "Ast": 0,
        "Cell": 0,
        "DD": 0,
        "DP": 0,
        "EC": 0,
        "GG": 0,
        "Orn": 0,
        "RS": 0,
        "R&M": 0,
        "ChL": 0,
        "Code": 0,
        "DB": 0,
        "For": 0,
        "IAT": 0,
        "WFL": 0
    }

    event_overlap = np.zeros((16, 16))

    for teammate in teammates:
        for i in range(16):
            event_i = list(event_counts.keys())[i]

            if event_i in teammate:
                event_counts[event_i] = event_counts[event_i] + 1

                for j in range(16):
                    event_j = list(event_counts.keys())[j]

                    if event_i != event_j and event_j in teammate:
                        event_overlap[i][j] = event_overlap[i][j] + 1

    event_overlap_list = []

    for i in range(16):
        event_i = list(event_counts.keys())[i]

        for j in range(16):
            if i != j and event_overlap[i][j] > 0:
                event_j = list(event_counts.keys())[j]

                overlap_count = int(event_overlap[i][j])

                overlap = "{} and {} - {}".format(event_i, event_j, overlap_count)
                reverse_overlap = "{} and {} - {}".format(event_j, event_i, overlap_count)

                if reverse_overlap not in event_overlap_list:
                    event_overlap_list.append(overlap)

    event_overlap_list = sorted(event_overlap_list, key=lambda overlap: overlap.split(" - ")[1], reverse=True)

    print(event_counts)
    print(event_overlap)
    print("\n".join(event_overlap_list))
    print("Average Overlap:", np.average(event_overlap) * 256 / (256-16))

    session1_events = {
        "A&P": "",
        "Ast": "",
        "Cell": "",
        "DD": "",
        "DP": "",
        "EC": "",
        "GG": "",
        "Orn": "",
        "RS": "",
        "R&M": "",
        "ChL": "",
        "Code": "",
        "DB": "",
        "For": "",
        "IAT": "",
        "WFL": ""
    }

    for teammate in teammates:
        event_1 = teammate[1]

        if event_1 in session1_events.keys():
            session1_events[event_1] = session1_events[event_1] + (", " if len(session1_events[event_1]) > 0 else "") + teammate[0]

    print(session1_events)

    session1_event_counts = []

    for i in range(16):
        session1_event_counts.append([list(session1_events.keys())[i], sum([0 if name == "" else 1 for name in list(session1_events.values())[i].split(", ")])])

    session1_event_counts = sorted(session1_event_counts, key=lambda event: event[1])

    print(session1_event_counts)

    session2_events = {
        "A&P": "",
        "Ast": "",
        "Cell": "",
        "DD": "",
        "DP": "",
        "EC": "",
        "GG": "",
        "Orn": "",
        "RS": "",
        "R&M": "",
        "ChL": "",
        "Code": "",
        "DB": "",
        "For": "",
        "IAT": "",
        "WFL": ""
    }

    for teammate in teammates:
        event_2 = teammate[2]

        if event_2 in session2_events.keys():
            session2_events[event_2] = session2_events[event_2] + (", " if len(session2_events[event_2]) > 0 else "") + teammate[0]

    print(session2_events)

    session2_event_counts = []

    for i in range(16):
        session2_event_counts.append([list(session2_events.keys())[i], sum([0 if name == "" else 1 for name in list(session2_events.values())[i].split(", ")])])

    session2_event_counts = sorted(session2_event_counts, key=lambda event: event[1])

    print(session2_event_counts)

breakouts_09292021()
