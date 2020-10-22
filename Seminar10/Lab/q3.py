data = []
file = open('temperatures.txt', 'r')

for line in file:
    person_dat = line.rstrip().split('\t')

    name = person_dat.pop(0)
    minimum, maximum = 0.0, 0.0
    while len(person_dat) > 0:
        cur = float(person_dat.pop())
        if (cur < minimum and cur < maximum) or minimum == 0:
            minimum = cur
        elif (cur > minimum and cur > maximum) or maximum == 0:
            maximum = cur

    print(name + ": " + str(minimum) + ', ' + str(maximum))

