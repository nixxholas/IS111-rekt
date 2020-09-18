def compute_avg_height(details):
    # First and foremost, splits the strings up by every individual's data first.
    people_details = details.split(', ')
    dataset = []  # The tuple that stores all data in the proper format.

    for p in people_details:
        kvp = p.split(":")
        if len(kvp) > 1:  # If there's any height data, truncate, cleanup and push.
            dataset.append((kvp[0], float(kvp[1].replace(" ", "")[:-1])))
        else:
            dataset.append((kvp[0], 0.0))

    return sum(p[1] for p in dataset)


print(compute_avg_height("Jonathan Li:1.75m, Lim, Josephine : 1.59m , George Khoo:   1.7 m"))