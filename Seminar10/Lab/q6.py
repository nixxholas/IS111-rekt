def extract_functions(python_filename, output_filename):
    file = open(python_filename, 'r')

    res = []
    curr_name = None
    curr_def = []
    is_within_comment = False
    for line in file:
        line = line.rstrip()

        # If the line starts the comments
        if line.lstrip().startswith('"""'):
            # Begin scanning
            is_within_comment = not is_within_comment

            if is_within_comment:
                # Skip and ignore the first three quotes
                line = line.lstrip()[3:]
                # Ensure that the current line is not empty else just skip it.
                if line != '' and not line.endswith('"""'):
                    curr_def.append('\t' + line)
                # If this is the only line to scan through, we need to set is_within_comment for subsequent flow
                elif line != '' and line.endswith('"""'):
                    is_within_comment = False  # Reset
                    curr_def.append('\t' + line[:-3])
        # If we're still in comments
        elif is_within_comment:
            if line.endswith('"""'):
                is_within_comment = False  # Reset
                curr_def.append(line[:-3])
            else:
                curr_def.append(line)
        # When the line is a function definition
        elif line.lstrip().startswith('def'):
            # If its not empty, we have to push the previously populated function over and reset.
            if curr_name is not None:
                res.append((curr_name, curr_def))
            curr_name = line
            curr_def = []

    # After processing the file, we have to make sure the last accessed data is also populated into the output as well.
    if curr_name is not None:
        res.append((curr_name, curr_def))

    output = open(output_filename, 'w')
    for i in range(len(res)):
        func = res[i]
        output.write(str(i + 1) + '. ' + func[0] + '\n')

        for line in func[1]:
            output.write(line + '\n')

        output.write('\n')


extract_functions('python_script.py', 'python_script_sorted.py')
