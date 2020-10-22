file = open('transactions.txt', 'r')
output_file = open('transactions-output-1.txt', 'w')

for line in file:
    tx = line.rstrip().split('\t')

    if float(tx[2][1:]) > 30:
        output_file.write(line)
