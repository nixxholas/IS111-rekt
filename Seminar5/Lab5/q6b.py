### Q6 More on Lists
## b)
# Write your code below:
##############################################################
def get_larger_numbers(num_list1, num_list2):
    for n in num_list1:
        is_big = True  # Always assume n is bigger
        for n2_num in num_list2:
            if n < n2_num:
                is_big = False  # Not bigger, mark for removal
                break
        if not is_big: num_list1.remove(n)

    return num_list1


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()
