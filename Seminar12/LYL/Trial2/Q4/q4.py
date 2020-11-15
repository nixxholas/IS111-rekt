def process_numbers(input_filename, output_filename):
    line_data = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.rstrip()) == 0:
                line_data.append((0, []))
            else:
                groups = line.rstrip().split('#')
                group_count = len(groups)

                group_averages = []
                for group in groups:
                    total_val = 0.0
                    values = group.split(' ')

                    for val in values:
                        if val != '' and (type(val) == int or float):
                            total_val += float(val)

                    group_averages.append(total_val/len(values))

                line_data.append((group_count, group_averages))

    total_groups = 0
    max_avg = 0.0
    with open(output_filename, 'w') as output_file:
        for line_datum in line_data:
            total_groups += line_datum[0]
            avg_output = ''

            for avg in line_datum[1]:
                if avg > max_avg:
                    max_avg = avg
                avg_output += str(avg) + '#'

            output_file.write(str(line_datum[0]) + ': ' + avg_output[:len(avg_output) - 1] + '\n')

        output_file.write('Total number of groups: ' + str(total_groups) + '\n')
        output_file.write('Maximum average: ' + (str(max_avg) if max_avg != 0 else 'N/A'))


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False