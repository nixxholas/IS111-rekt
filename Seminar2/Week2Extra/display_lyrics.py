# Recursion via string arrays
def traverse_lines(lyricArr, line=0):
    # Always print first,
    print(lyricArr[line])
    # Increment the pointer
    line += 1
    # Recurse if there are still more lines to output, else leave.
    return traverse_lines(lyricArr, line) if line < len(lyricArr) else exit()


# New recursion
def traverse_lines_v2(lyricArr):
    # Always print first.
    print(lyricArr[0])
    # Pop the first element / the element that was printed above.
    del lyricArr[0]
    # Recurse again.
    return traverse_lines(lyricArr)
