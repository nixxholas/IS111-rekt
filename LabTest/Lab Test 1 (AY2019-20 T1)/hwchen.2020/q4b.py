# Name: Nicholas Chen
# Email ID: hwchen.2020

import itertools
import q4a


def get_seating_arrangement(female_list, male_list, must_list, cannot_list):
    # Divide and conquer strategy
    people_list = female_list
    people_list.extend(male_list)

    permutations = list(itertools.permutations(people_list))
    for perm in permutations:
        cur_p = list(perm)
        valid_perm = True
        must_female = True if perm[0] in male_list else False

        for i in range(1, len(cur_p)):
            # If the current index must be female and its not in the female list or if
            # the current index must be male and its not in the male list
            if (must_female and cur_p[i] not in female_list) or (not must_female and cur_p[i] not in male_list):
                # Invalid permutation.
                valid_perm = False
                break
            else:
                # Always flip
                must_female = not must_female

        if valid_perm and q4a.check_seating_arrangement(cur_p, must_list, cannot_list): return cur_p

    return None
