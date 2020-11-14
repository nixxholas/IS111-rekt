def get_family_members(head):
    res = [head[0]]

    if len(head) > 1:
        for i in range(len(head[1]) - 1, -1, -1):
            descendant = head[1][i]
            res += get_family_members(descendant)

    return res


def traverse_children(head):
    res = [head[0]]
    return res