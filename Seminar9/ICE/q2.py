seq = []
val = 0
while val >= 0:
    val = int(input('Enter an integer: '))

    if val > 0 and (val % 2) != 0:
        seq.append(val)

print()
print("Thanks!")
print("The odd positive integers you have entered are the following: ")
# Merging combination via string lists
str(seq)
print()

# seq = ''
# val = 0
# while val >= 0:
#     val = int(input('Enter an integer: '))
#
#     if val > 0 and (val % 2) != 0:
#         seq += str(val) + ', '
#
# print()
# print("Thanks!")
# print("The odd positive integers you have entered are the following: ")
# print(seq[:-2])