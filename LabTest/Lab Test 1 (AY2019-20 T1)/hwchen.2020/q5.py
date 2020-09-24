# Name: Nicholas Chen
# Email ID: hwchen.2020

def transform(str1, str2):
    # Have the answer string here as well.
    res = [str1]

    # Generate a dynamic map to see which is character is supposed to traverse to where.
    for i in range(len(str2)):
        # Always cross check against the latest string we're manipulating from 'res'
        mapping = (res[len(res) - 1].index(str2[i]), i)

        # If we need to move,
        if mapping[0] != mapping[1]:
            # Obtain the amount we need to move.
            movement_amt = mapping[0] - mapping[1]

            # If we're moving down
            if movement_amt > 0:
                # We keep moving till we hit mapping[1], which is str2's position for that specific character.
                for j in range(mapping[0], mapping[1], -1):
                    # Manipulate this list for the new step it has to take. Always take the last one.
                    new_str = list(res[len(res) - 1])

                    prev_spot = new_str[j]
                    target_spot = new_str[j - 1]

                    new_str[j - 1] = prev_spot
                    new_str[j] = target_spot

                    res.append("".join(new_str))
            else:
                # Else we're moving up
                for j in range(mapping[0], mapping[1]):
                    # Manipulate this list for the new step it has to take. Always take the last one.
                    new_str = list(res[len(res) - 1])

                    prev_spot = new_str[j]
                    target_spot = new_str[j + 1]

                    new_str[j + 1] = prev_spot
                    new_str[j] = target_spot

                    res.append("".join(new_str))

    return res
