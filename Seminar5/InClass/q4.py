def get_avg_len(strings):
    # obtain the sum of all string chars and get the avg
    return sum(map(len, strings)) / len(strings) if len(strings) > 0 else 0


print(get_avg_len(["C", "Java", "Python", "PHP"]))
print(get_avg_len([]))