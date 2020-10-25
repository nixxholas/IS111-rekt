import string
from random import shuffle

file = open('talk.txt', 'r')

# Read every sentence in the file
for line in file:
    line = line.strip()
    word_arr = line.split(' ')

    # Iterate every sentence word by word
    for i in range(len(word_arr)):
        # Ensure the word is more than 2 characters before performing any manipulation.
        if len(word_arr[i]) > 2:
            front = word_arr[i][0]
            back = word_arr[i][len(word_arr[i] - 1)]
            back_iter = len(word_arr[i] - 2)
            while word_arr[i][back_iter] not in string.ascii_letters:
                back_iter -= 1
            mid = word_arr[i][1:len(word_arr[i]) - 2]
            shuffle(list(mid))

