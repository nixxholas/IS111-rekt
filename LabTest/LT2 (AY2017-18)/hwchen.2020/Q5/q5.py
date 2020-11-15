def get_family_members(head):
    res = [head[0]]

    cur_layer = head[1]
    while len(cur_layer) > 0:
        new_layer = []
        for cur_layer_head in cur_layer:
            res.append(cur_layer_head[0])
            if len(cur_layer_head[1]) > 0:
                new_layer += cur_layer_head[1]
        cur_layer = new_layer

    return res


def traverse_children(head):
    res = [head[0]]
    return res
