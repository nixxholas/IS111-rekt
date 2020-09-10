def pad_message(msg, width):
    return (((width - len(msg)) * " ") + msg) if len(msg) < width else msg[:width]


print(pad_message("IS111 Lab 5", 20))
print(pad_message("IS111 Lab 5", 8))
print(pad_message("hello", 20))
print(pad_message("python programming", 20))
print(pad_message("Hello World! I enjoy programming in Python.", 20))