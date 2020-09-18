def get_average_duration(movie_list):
    return 0.0 if len(movie_list) == 0 else (sum(m[2] for m in movie_list) / len(movie_list))
