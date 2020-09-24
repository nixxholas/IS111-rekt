def get_unique_titles(book_list):
    final_list = []

    for b in book_list:
        if b[0] not in final_list:
            final_list.append(b[0])

    return final_list


def get_titles_and_counts(book_list):
    final_list = {}

    for b in book_list:
        if b[0] not in final_list:
            final_list[b[0]] = b[3]
        else:
            final_list[b[0]] += b[3]

    return final_list


print(get_unique_titles([("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5),
                         ("Intro to Programming", "Ed-3", "hardcover", 4)]))
print(get_titles_and_counts(
    [("Intro to Programming", "Ed-2", "paperback", 2), ("Intro to Python", "Ed-1", "paperback", 5),
     ("Intro to Programming", "Ed-3", "hardcover", 4), ("Intro to Python", "Ed-3", "hardcover", 3)]))
