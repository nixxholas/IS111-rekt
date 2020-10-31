# write your solution here
def reverse(map):
    new_map = {}

    # Loop the keys within the existing map
    for key in map.keys():
        # Get the value of the key
        value = map[key]
        # If the value exists as a key in new_map,
        if value in new_map.keys():
            # It means there already contains a value.
            # We push more into the value.
            new_map[value].append(key)
        else:
            # Else, we create a new key and value.
            new_map[value] = [key]

    return new_map
