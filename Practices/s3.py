import sys

for i in range(sys.maxsize**100):
    print(i)
    i -= 1
