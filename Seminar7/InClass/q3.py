def print_triangle(ch, num_rows):
    if num_rows % 2 == 0: exit()

    spacing = num_rows - 1
    chars = 1
    for i in range(0, num_rows):
        print((' ' * spacing) + (ch * chars))
        spacing -= 1
        chars += 2