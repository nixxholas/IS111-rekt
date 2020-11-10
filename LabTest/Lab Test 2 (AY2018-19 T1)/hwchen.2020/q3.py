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
    target_month = int(month.split('/')[0])  # Get the target month in INT
    target_year = int(month.split('/')[1])  # Get the target year in INT
    for datum in dataset:  # Loop every tx
        datum_month = int(datum[0].split('/')[0])  # Take the tx's MM
        datum_year = int(datum[0].split('/')[2])  # Take the tx's YYYY

        if datum_month == target_month and datum_year == target_year:  # Compare.
            total += float(datum[1][1:])  # Add since its within the target month and year.

    return total

