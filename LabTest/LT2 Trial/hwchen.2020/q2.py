def get_reversed_list(num_list):
    # Flip first
    num_list = num_list[::-1]

    for i in range(len(num_list)):
        if num_list[i] != 0:
            num_list[i] *= -1

    # Modify the code below.
    return num_list
