def get_average_duration(movie_list):
    return 0.0 if len(movie_list) == 0 else (sum(m[2] for m in movie_list) / len(movie_list))


def get_num_movies_of_genre(movie_list, genre, count=0):
    if len(movie_list) > 0 and movie_list[-1][1] == genre: count += 1
    return count if len(movie_list) == 0 else get_num_movies_of_genre(movie_list[:-1], genre, count)


def get_title_of_longest_movie(movie_list, longest_title='', duration=0):
    if len(movie_list) == 0:
        return longest_title
    else:
        if movie_list[-1][2] > duration:
            longest_title = movie_list[-1][0]
            duration = movie_list[-1][2]
        return get_title_of_longest_movie(movie_list[:-1], longest_title, duration)


def get_movies_with_keyword(movie_list, keyword):
    movie_list_with_keyword = []
    for i in range(0, len(movie_list)):
        if keyword in movie_list[i][0]: movie_list_with_keyword.append(movie_list[i])

    return movie_list_with_keyword
