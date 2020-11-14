with open('q6-basic.txt') as imported_file:
    line_outputs = []
    for line in imported_file:
        line_output = []
        # A 1 ,A 2 ,...,A n @B 1 ,B 2 ,...,B n #<check value>
        cols = line.rstrip().split('@')
        set_a = cols[0].split(',')
        set_b = cols[1].split('#')[0].split(',')
        check_val = cols[1].split('#')[1]

        max_index = len(set_a) if len(set_a) > len(set_b) else len(set_b)
        for i in range(max_index):
            # If the current index does not exceed set_a and set_b's indexes and if their multiplication result
            # is more than or equal to check_value,
            if (i + 1 <= len(set_a)) and (i + 1 <= len(set_b)) and int(set_a[i]) * int(set_b[i]) >= int(check_val):
                line_output.append(int(set_a[i]) * int(set_b[i]))  # We add it in
            # Else if the current index exceeds set_a but not set_b's indexes,
            elif (i + 1 > len(set_a)) and (i + 1 <= len(set_b)):
                # We check to see if the number at set_b's index of i is more than or equal to check_val
                if int(set_b[i]) >= int(check_val):
                    line_output.append(int(set_b[i]))  # We add it in
            # Else if the current index exceeds set_a but not set_a's indexes,
            elif (i + 1 > len(set_b)) and (i + 1 <= len(set_a)):
                # We check to see if the number at set_a's index of i is more than or equal to check_val
                if int(set_a[i]) >= int(check_val):
                    line_output.append(int(set_a[i]))  # We add it in

        line_outputs.append(line_output)

    with open('output.txt', 'w') as output_file:
        for line in line_outputs:
            output_file.write(str(line) + '\n')
