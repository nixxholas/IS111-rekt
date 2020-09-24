# Name: Nicholas Chen
# Email ID: hwchen.2020

def check_seating_arrangement(arrangement, must_list, cannot_list):
    # Check the must list first.
    if len(must_list) > 0:
        # For every tuple in must_list
        for t in must_list:
            # Ensure they sit beside each other - standard index method
            if not ((arrangement.index(t[0]) - arrangement.index(t[1])) == 1 or (
                    arrangement.index(t[0]) - arrangement.index(t[1])) == -1 or (
                            # Perform a 'on the edge' scenario where they sit at index 0 and last index
                            arrangement.index(t[0]) - arrangement.index(t[1]) == (len(arrangement) - 1)) or (
                            arrangement.index(t[0]) - arrangement.index(t[1]) == -(len(arrangement) - 1))):
                return False

    # Check the cannot list first.
    if len(cannot_list) > 0:
        # For every tuple in cannot_list
        for t in cannot_list:
            # Ensure they do NOT sit beside each other - standard index method
            if (arrangement.index(t[0]) - arrangement.index(t[1])) == 1 or (
                    arrangement.index(t[0]) - arrangement.index(t[1])) == -1 or (
                    # Perform a 'on the edge' scenario where they do NOT sit at index 0 and last index
                    arrangement.index(t[0]) - arrangement.index(t[1]) == (len(arrangement) - 1)) or (
                    arrangement.index(t[0]) - arrangement.index(t[1]) == -(len(arrangement) - 1)):
                return False

    return True
