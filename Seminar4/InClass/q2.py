msg = input("Enter a message :")

for i in range(0, len(msg)):
    print(msg[i], end='-') if i < len(msg) - 1 else print(msg[i], end='')