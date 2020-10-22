def create_num_file(output_file, n):
    file = open(output_file, 'w')
    for i in range(0, n + 1, 2):
        file.write(str(i) + '\n')


create_num_file('q1b_test-1.txt', 10)