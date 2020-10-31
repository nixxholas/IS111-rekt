# write your solution here
def reverse(map):
    new_map = {}

    for key in map.keys():
        if map[key] in new_map.keys():
            new_map[map[key]].append(key)
        else:
            new_map[map[key]] = [key]

    return new_map
