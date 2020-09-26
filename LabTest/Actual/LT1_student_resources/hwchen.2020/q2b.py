# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def get_max_of_min(list_of_num_tuples):
    # Replace the code below with your implementation.
    # Note: You’re NOT allowed to use either min()or max()to solve this problem.

    # Each tuple contains 3 integer numbers and the function returns the maximum of maximum
    # values in these tuples
    max_of_min = None

    for t in list_of_num_tuples:
        # Obtain the smallest of the current tuple
        smallest = t[0] if t[0] < t[1] and t[0] < t[2] else t[1] if t[1] < t[0] and t[1] < t[2] else t[2]

        # Either the biggest min is currently none or is smaller than smallest
        if max_of_min is None or max_of_min < smallest:
            max_of_min = smallest
    
    return max_of_min
