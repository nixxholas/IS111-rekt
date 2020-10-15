seq = []
val = 0
while val >= 0:
    val = int(input('Enter an integer: '))

    if val > 0 and (val % 2) != 0:
        seq.append(val)

print()
print("Thanks!")
print("The odd positive integers you have entered are the following: ")
res = ''
while len(seq) > 0:
    res += str(seq.pop(0)) + ', '
print(res[:-2])
