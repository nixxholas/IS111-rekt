def extract_functions(python_filename, output_filename):
    file = open(python_filename, 'r')

    res = []
    curr_name = None
    curr_def = []
    ignore_line = False
    for line in file:
        line = line.rstrip()

        # If the line starts the comments
        if line.startswith('"""') and not line.endswith('"""'):
            ignore_line = not ignore_line

        if ignore_line:
            if line.startswith('def'):
                if curr_name is not None:
                    res.append((curr_name, curr_def))
                curr_name = line
                curr_def = []
            else:
                curr_def.append(line)

    output = open(output_filename, 'w')
    for i in range(len(res)):
        func = res[i]
        output.write(str(i + 1) + '. ' + func[0] + '\n')

        for line in func[1]:
            output.write('\t' + line + '\n')

        output.write('\n')


extract_functions('python_script.py', 'python_script_sorted.py')
