## Q1b Substitution Cipher
# write your code below
def decrypt(my_dict, encrypted_msg):
    msg = list(encrypted_msg)

    for i in range(len(msg)):
        if msg[i] in my_dict:
            msg[i] = my_dict[msg[i]]

    return "".join(msg)

