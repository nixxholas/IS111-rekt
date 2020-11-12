def count_high_temperatures(temperatures):
    res = []
    for temp in temperatures:
        if temp > 37.5:
            res.append(temp)

    return len(res)
