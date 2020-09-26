# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def trace_contacts_2(patient, history, m, n):
    """
    m is a positive integer indicating how many days a person is infectious but
    asymptomatic
    n is a positive integer indicating how many days it takes for a person to develop
    symptoms from the day he catches the virus
    """
    possibly_infected = []
    # Store infection day count for easy math
    infected_trace_list = []

    # We first traverse the patient,
    for h in history:
        # If the patient is involved and if the day met was more than or equal to
        # 2 days after catching the virus and if its not on the day of developing
        # symptoms just to be sure..
        if (patient == h[0] or h[1] == patient) and (-(m + 1) < h[2] < 0):
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
                    # the day they met was n - m -1 days after the infected was infected
                    # and before the previously infected developed symptoms
                    infected_trace_list[i] + (n - m - 1) < h[2] < infected_trace_list[i] + n):
                # This dude is infected too.
                another_infected = h[0] if h[0] != possibly_infected[i] else h[1]
                if another_infected not in possibly_infected:
                    possibly_infected.append(another_infected)
                    infected_trace_list.append(h[2])

        # Always increment after checking
        i += 1

    return possibly_infected
