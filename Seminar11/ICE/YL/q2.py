# write your answer here
words = {}

user_input = ' '
while user_input != '':
    user_input = input("Enter the word >")
    if user_input != '':
        if user_input in words.keys():
            words[user_input] += 1
        else:
            words[user_input] = 1

query_input = ' '
while query_input != '':
    query_input = input("Enter query word >")
    if query_input != '':
        if query_input in words:
            print(words[query_input])
            print()
        else:
            print("Not found.")

print("Bye bye")
