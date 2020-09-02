def gradual_print(text):
    for i in range(0, len(text)):
        print(text[:i+1])


def reverse_gradual_print(text):
    for i in range(0, len(text)):
        print(text[:len(text) - i])


msg = input("Enter a message: ")
gradual_print(msg)
reverse_gradual_print(msg)