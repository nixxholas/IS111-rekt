def find_seat(seat):
    seating_plan = {}

    with open('seating_plan.txt') as seating_plan_doc:
        for line in seating_plan_doc:
            cols = line.rstrip().split(',')
            seat = (cols[0], cols[1])
            if seat not in seating_plan.keys():
                seating_plan[seat] = cols[2]

    if seat in seating_plan.keys():
        return seating_plan[seat]
    else:
        return None


seat = (input('Enter a letter (from A to E) :'), input('Enter a seat number (from 1 to 25) :'))
name = find_seat(seat)

if name is not None:
    print('The person seated at the seat', seat[0] + seat[1], 'is', name)
