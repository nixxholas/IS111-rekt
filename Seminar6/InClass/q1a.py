from statistics import mean


def get_larger_values(values):
    avg = mean(values)

    for v in values:
        if v < avg:
            values.remove(v)

    return values


print(get_larger_values([2.5, 3.5, 5.5, 1.0]))
