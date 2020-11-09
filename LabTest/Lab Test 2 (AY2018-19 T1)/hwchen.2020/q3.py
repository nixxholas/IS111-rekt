#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.
def load_file(file_name):
    transactions = []
    with open(file_name) as raw_txs:
        for tx in raw_txs:
            transactions.append(tx.rstrip().split('\t'))
    return transactions

# End of your additional functions.

def get_total_transactions_in_month(trans_file, month):
    # Modify the code below
    dataset = load_file(trans_file)

    total = 0.0
    target_month = int(month.split('/')[0])
    target_year = int(month.split('/')[1])
    for datum in dataset:
        datum_month = int(datum[0].split('/')[0])
        datum_year = int(datum[0].split('/')[2])

        if datum_month == target_month and datum_year == target_year:
            total += float(datum[1][1:])

    return total

