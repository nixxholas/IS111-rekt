def process_numbers(input_filename, output_filename):
    # Modify the code below.
    with open(input_filename) as input_file:
        incoming_data = input_file.readlines()

    with open(output_filename, 'w') as output_file:
        groups = 0
        # Make sure u have an initial never higher than any possible value.
        max_avg = -float('inf')
        # Loop every line
        for line in incoming_data:
            # Since we're in the line, split the numbers by groups
            line_groups = line.rstrip().split('#')
            # Let the main output know how many groups there are in the line first
            groups += len(line_groups)

            # Print the result first
            output_line = str(len(line_groups)) + ': '

            # Loop every group
            for i in range(len(line_groups)):
                # Split all the numbers in the groups
                numbers = line_groups[i].split(' ')
                avg = 0

                for number in numbers:
                    try:
                        avg += float(number)
                    except ValueError:
                        print('Non-float value detected and ignored.')

                avg /= len(numbers)
                if avg > max_avg:
                    max_avg = avg
                output_line += str(avg)
                if i + 1 != len(line_groups):
                    output_line += '#'

            output_file.write(output_line + '\n')

        output_file.write('Total number of groups: ' + str(groups) + '\n')
        output_file.write('Maximum Average: ' + str(max_avg))
    pass
