def get_average_duration(movie_list):
    if len(movie_list) == 0: return 0.0

    total_duration = 0.0
    for m in movie_list:
        total_duration += m[2]

    return total_duration / len(movie_list)


def get_num_movies_of_genre(movie_list, genre):
    count = 0

    # Title, Genre, Duration
    for m in movie_list:
        if m[1] == genre: count += 1

    return count


def get_title_of_longest_movie(movie_list):
    if len(movie_list) == 0: return ""
    longest = movie_list[0]

    for i in range(1, len(movie_list)):
        if longest[2] < movie_list[i][2]:
            longest = movie_list[i]

    return longest[0]


def get_movies_with_keyword(movie_list, keyword):
    movies = []

    for m in movie_list:
        if keyword in m[0]: movies.append(m)

    return movies
