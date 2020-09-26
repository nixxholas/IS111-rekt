# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def trace_contacts(patient, history):
    """
    Suppose person P caught the virus 7 days before Day 0 and if he develops symptoms
    on September 20, he must have caught the virus on exactly 13 september.

    This dude starts to infect other people he meets 2 days after he catches the virus
    (15 September onwards)
    For 5 days he is infectious and asymptomatic. (Can't see symptoms)
    Once he starts to develop symptoms, he stops meeting people and will not infect more.

    patient = name of person
    History = List of tuples that stores meeting history of people in the community.

    0: the name
    1: the other person's name (always different from 0)
    2: day of meeting
    """
    possibly_infected = []
    # Store infection day count for easy math
    infected_trace_list = []

    # We first traverse the patient,
    for h in history:
        # If the patient is involved and if the day met was more than or equal to
        # 2 days after catching the virus and if its not on the day of developing
        # symptoms just to be sure..
        if (patient == h[0] or h[1] == patient) and (-6 < h[2] < 0):
            # Then it means this person is infected.
            infected = h[0] if h[0] != patient else h[1]
            # Add into infectious list
            if infected not in possibly_infected:
                # Store the day the virus was caught as well
                possibly_infected.append(infected)
                infected_trace_list.append(h[2])

    # Define an iterator to iterate the newly possibly infected individuals.
    i = 0
    # Also check the infected people.
    while i < len(possibly_infected):
        # Trace the history once again, relevant to them and not relating to jason.
        # And if the
        for h in history:
            # If the infected met with someone who's not the patient and if
            if (h[0] == possibly_infected[i] and h[1] != patient) or (
                    h[1] == possibly_infected[i] and h[0] != patient) and (
                    # the day they met was the following day after the infected was infected,
                    h[2] > (infected_trace_list[i] + 1)):
                # This dude is infected too.
                another_infected = h[0] if h[0] != possibly_infected[i] else h[1]
                # Ensure this person is already not in the infected list.
                if another_infected not in possibly_infected:
                    # Add in along with the traceable day
                    possibly_infected.append(another_infected)
                    infected_trace_list.append(h[2])

        # Always increment after checking
        i += 1

    return possibly_infected
