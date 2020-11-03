## Q5a Word Counts
# write your code below
def count_words_in_file(file_name):
    count_dict = {}

    with open(file_name) as file:
        # It's always a good practice to load line by line to prevent memory overflow.
        for line in file:
            line = line.rstrip().split(' ')
            for word in line:
                word = word.lower()
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1

    return count_dict

