def print_message_with_separators(msg, sep):
    for i in range(0, len(msg)):
        print(msg[i], end=sep) if i < (len(msg) - 1) else print(msg[i], end='')


print_message_with_separators(input("Enter your desired message: "), input("Entire your desired separator: "))