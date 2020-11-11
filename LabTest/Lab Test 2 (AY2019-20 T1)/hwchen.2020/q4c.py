# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

from q4b import get_relation_through_link

def get_relation(family_dict, p1, p2):
    # Modify the code below.
    current_pt = p1
    cur_path = []
    res = [p1]

    banned_paths = []  # (B, C)
    attempt = 0
    while current_pt != p2:
        if attempt > 1:
            attempt = 0
            current_pt = p1

            if len(cur_path) == 1:
                banned_paths.append((p1, cur_path[0]))
            elif len(cur_path) > 1:
                banned_paths.append((cur_path[len(cur_path) - 2], cur_path[len(cur_path) - 1]))
            cur_path = []

        for key in family_dict:
            if key[0] == current_pt and key[1] != p1 and key not in banned_paths:
                attempt = 0
                cur_path.append(key[1])
                current_pt = key[1]
                if current_pt == p2:
                    res += cur_path
                    break
        attempt += 1

    return get_relation_through_link(family_dict, res)
