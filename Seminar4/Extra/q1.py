def print_square_1(n):  # n is a +ve odd number >= 5
    # Prints out an n x n square using asterisks that's divided into four small squares
    mid = n / 2
    for n in range(0, n):  # Loop vertically
        # Print horizontally
        if n == 0 or n == n or n == mid:
            for i in range(0, n): print("*", end='')
