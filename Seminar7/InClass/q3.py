def print_triangle(ch, num_rows):
    if num_rows % 2 == 0: exit()

    spacing = num_rows - 1
    chars = 1
    for i in range(0, num_rows):
        print((' ' * spacing) + (ch * chars))
        spacing -= 1
        chars += 2


def print_frame(ch, num_rows, num_cols):
    for i in range(0, num_rows):
        if i == 0 or i == num_rows - 1:
            print(ch * num_cols)
        else:
            print(ch + (" " * (num_cols - 2)) + ch)

