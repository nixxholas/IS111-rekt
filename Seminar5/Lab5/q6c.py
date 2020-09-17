### Q6 More on Lists
## c)
# Write your code below:
##############################################################
def get_non_common_strings(str_list1, str_list2):
    final_list = []

    for w in str_list1:
        if w not in str_list2: final_list.append(w)
    for w in str_list2:
        if w not in str_list1: final_list.append(w)

    return final_list


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()
