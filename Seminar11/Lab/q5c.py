from q5a import count_words_in_file

file = 'spam_sms.txt'
my_dict = count_words_in_file(file)
# Sorted top words collection. Front being biggest, back being smallest.
stw = []


def sorted_insert(item):
    if len(stw) == 0:
        stw.append(item)
    else:
        for i in range(len(stw)):
            # If the current stw word has less count than item and that they are not equal,
            if item[1] > stw[i][1] and stw[i][0] != item[0]:
                # Add.
                stw.insert(i, item)

                # If there's more than 10, remove the smallest
                if len(stw) > 10:
                    stw.pop()

                # Always abort upon succession
                return
            elif i == (len(stw) - 1) and stw[i][0] != item[0] and len(stw) < 10:
                stw.append(item)
                # Always abort upon succession
                return


# Let's do insertion sort
for word in my_dict:
    sorted_insert((word, my_dict[word]))

print(stw)
