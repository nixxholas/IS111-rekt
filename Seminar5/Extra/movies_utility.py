def get_average_duration(movie_list):
    return 0.0 if len(movie_list) == 0 else (sum(m[2] for m in movie_list) / len(movie_list))


def get_num_movies_of_genre(movie_list, genre, count=0):
    if len(movie_list) > 0 and movie_list[-1][1] == genre: count += 1
    return count if len(movie_list) == 0 else get_num_movies_of_genre(movie_list[:-1], genre, count)
