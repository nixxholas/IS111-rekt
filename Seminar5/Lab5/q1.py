## Q1 Initials
# Write your code below:
##############################

meeting_pop = int(input("How many people will attend the meeting? "))
participants = []

while len(participants) < meeting_pop:
    participants.append(input("Participant " + str(len(participants) + 1) + " "))

initials = []
for p in participants:
    initial = ''
    p_split = p.split(' ')
    for p_seg in p_split:
        if p_seg[0] != ' ': initial += p_seg[0]
    initials.append(initial)

print("The initials of the participants are as follows:")
for i in initials:
    print(i)
