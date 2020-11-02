# Q1a Substitution Cipher
# write your code below
def encrypt(my_dict, msg):
    msg_c = list(msg)
    for i in range(len(msg_c)):
        if msg_c[i] in my_dict:
            msg_c[i] = my_dict[msg[i]]

    return "".join(msg_c)

