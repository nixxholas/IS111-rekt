def count_high_temperatures(temperatures):
    count = 0
    for temp in temperatures:
        if temp > 37.5:
            count += 1
    return count



