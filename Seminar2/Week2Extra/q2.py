# Loop method
def print_square(symbol, size):
    '''
    In Python, a string can be “multiplied by” an integer, which gives a new string that repeats the original string
    multiple times. Try the following code to understand how this works:
    '''
    currLine = 0

    # While current line does not exceed the size
    while currLine < size:
        # If we're at the first line or last line
        if (currLine == 0) or ((currLine + 1) == size):
            print(symbol * size)
        else:
            print(symbol + (" " * (size - 2)) + symbol)

        currLine += 1

# Recursion method
def print_square_v2(symbol, size, currLine = 0):
    if currLine < size:
        # If we're at the first line or last line
        if (currLine == 0) or ((currLine + 1) == size):
            print(symbol * size)
        else:
            print(symbol + (" " * (size - 2)) + symbol)

        currLine += 1
        print_square_v2(symbol, size, currLine)


# print_square(input("Enter the symbol of the square: "), int(input("Enter the size of the square: ")))
print_square_v2(input("Enter the symbol of the square: "), int(input("Enter the size of the square: ")))