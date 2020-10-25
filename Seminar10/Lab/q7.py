import string
import random
import re

file = open('talk.txt', 'r')

sentences = []
# Read every sentence in the file
for line in file:
    line = line.strip()
    # word_arr = line.split(' ')
    word_arr = re.split('[ ]', line)

    # Iterate every sentence word by word
    for i in range(len(word_arr)):
        # Ensure the word is more than 3 characters before performing any manipulation.
        if len(word_arr[i]) > 3 and not word_arr[i].isnumeric():
            # Always stash the first character safely and permanently
            front = word_arr[i][0]
            # Take the last character of the word and stash it first.
            back = word_arr[i][-1]
            """
            Iterate the back of the word to ensure we obtain anything if its a non char.
                Scenario 1: Nicholas'
                Scenario 2: Brother's
                Scenario 3: Hello!!!
                Scenario 4: Hello
            """
            # This covers all scenarios, since it ensures that the last character is either in ascii letters
            back_compliant = back in string.ascii_letters and word_arr[i][-2] != "'"
            # If the back-end characters do not comply,
            if not back_compliant:
                # Continue iterating backwards to look for all the characters till the last character we need to swap
                # around with
                back_iter = len(word_arr[i]) - 2
                while word_arr[i][back_iter] not in string.ascii_letters:
                    back = word_arr[i][back_iter] + back
                    back_iter -= 1
            mid = ''.join(random.sample(word_arr[i][len(front):len(word_arr[i]) - len(back)],
                                        len(word_arr[i][len(front):len(word_arr[i]) - len(back)])))
            word_arr[i] = "".join(front + mid + back)

    sentences.append(" ".join(word_arr))

print(sentences)
