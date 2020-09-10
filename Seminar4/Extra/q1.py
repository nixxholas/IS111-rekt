import math


def print_square_2(n):  # n is a +ve odd number >= 5
    mid = math.floor(n / 2)

    for j in range(0, n):  # Loop vertically
        # Print horizontally
        # The first or the last is always a complete print.
        if j == 0 or j == (n - 1):
            for i in range(0, n):
                if i == (n - 1):
                    print("*")
                else:
                    print("*", end='')
        else:
            for i in range(0, n):
                if i == 0:
                    print("*", end='')
                elif i == (n - 1):
                    print("*")
                else:
                    if i == j or j == (n - 1) - i:
                        print("*", end='')
                    else:
                        print(" ", end='')


def print_square_1(n):  # n is a +ve odd number >= 5
    # Prints out an n x n square using asterisks that's divided into four small squares
    mid = math.floor(n / 2)
    for j in range(0, n):  # Loop vertically
        # Print horizontally
        if j == 0 or j == (n - 1) or j == mid:
            for i in range(0, n):
                if i == (n - 1):
                    print("*")
                else:
                    print("*", end='')
        else:
            # print("*" * n) TODO: Overhaul flow with this
            for i in range(0, n):
                if i == 0 or i == mid:
                    print("*", end='')
                elif i == (n - 1):
                    print("*")
                else:
                    print(" ", end='')


# print_square_1(int(input("Enter the size of the square: ")))
print_square_2(int(input("Enter the size of the square: ")))
