### Q6 More on Lists
## a)
# Write your code below:
##############################################################
def get_all_combinations(str_list, num_list):
    """
    Takes in two lists, str_list containing a sequence of strings and num_list containing a sequence of integers,
    with both lists containing different sizes.

    Returns a list of tuples.

    For example, get_all_combinations(["a", "b"], [1, 2, 3]) should return
    [("a", 1), ("a", 2), ("a", 3), ("b", 1), ("b", 2), ("b", 3)].
    """
    res = []
    for s in str_list:
        for n in num_list:
            res.append((s, n))

    return res


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_all_combinations(["a", "b"], [1, 2, 3])
print("Expected: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]")
print("Actual  : " + str(r_list))
print()
