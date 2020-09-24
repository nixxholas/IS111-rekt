def get_average_duration(movie_list):
    if len(movie_list) == 0: return 0.0

    total_duration = 0.0
    for m in movie_list:
        total_duration += m[2]

    return total_duration / len(movie_list)