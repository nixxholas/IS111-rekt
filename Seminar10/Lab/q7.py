import string
import re
from random import shuffle

file = open('talk.txt', 'r')

# Read every sentence in the file
for line in file:
    line = line.strip()
    # word_arr = line.split(' ')
    word_arr = re.split('[;, ]', line)

    # Iterate every sentence word by word
    for i in range(len(word_arr)):
        # Ensure the word is more than 2 characters before performing any manipulation.
        if len(word_arr[i]) > 2 and not word_arr[i].isnumeric():
            # Always stash the first character safely and permanently
            front = word_arr[i][0]
            # Take the last character of the word and stash it first.
            back = word_arr[i][-1]
            """
            Iterate the back of the word to ensure we obtain anything if its a non char.
            # Scenario 1: Nicholas'
            # Scenario 2: Brother's
            # Scenario 3: Hello!!!
            # Scenario 4: Hello
            """

            # This covers
            back_compliant = back in string.ascii_letters and word_arr[i][-2] != "'"
            if not back_compliant
                back_iter = len(word_arr[i]) - 2
                while word_arr[i][back_iter] not in string.ascii_letters:
                    back = word_arr[i][back_iter] + back
                    back_iter -= 1
            mid = word_arr[i][1:len(word_arr[i]) - 2]
            shuffle(list(mid))
            print(front + mid + back)

