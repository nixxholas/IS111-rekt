import copy

def get_all_permutations(letters):
    permutations = set()
    permutations.add(letters)

    letters = list(letters)
    for fixed_index in range(len(letters)):
        cur_word = copy.deepcopy(letters)
        if fixed_index > 0:
            cur_word.insert(0, cur_word.pop(fixed_index))

        for i in range(1, len(letters) - 1):
            permutations.add("".join(cur_word))
            if i + 1 < len(letters):
                cur_word.insert(i + 1, cur_word.pop(i))
            else:
                break

        if fixed_index > 0:
            for i in range(fixed_index, -1, -1):
                permutations.add("".join(cur_word))
                if i - 1 >= 0:
                    cur_word.insert(i - 1, cur_word.pop(i))
                else:
                    break

    return list(permutations)


def get_permutation_count(word):
    p = 0

    for i in range(len(word), 0, -1):
        if p == 0:
            p = i
        else:
            p *= i

    return p