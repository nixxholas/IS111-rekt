# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
def get_daily_spending(filename, start_day, end_day, month, year):
    # Build the transaction data first into a date traceable dictionary.
    transactions = {}
    with open(filename) as input_file:
        for line in input_file:
            cols = line.rstrip().split('|')

            # Store the dd/mm/yyyy as a tuple for easy key traversal
            date = cols[0].split('/')
            date_tup = (int(date[0]), int(date[1]), int(date[2]))

            # Store the data
            if date_tup in transactions:
                transactions[date_tup].append((int(cols[1]), cols[2]))
            else:
                transactions[date_tup] = [(int(cols[1]), cols[2])]

    # Build the tuples we need.
    date_tuples_to_track = []
    for i in range(start_day, end_day + 1):
        date_tuples_to_track.append((i, month, year))

    res = []
    # Track and store the results
    for date_tuple in date_tuples_to_track:
        cur_date_total = 0
        if date_tuple in transactions.keys():
            for tx in transactions[date_tuple]:
                cur_date_total += tx[0]
        res.append(cur_date_total)

    # Write your code here.
    return res

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    n = 0

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 3, 5, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 3, 5, 10, 2020)
    print("Expected : [13500, 31520, 100]")
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 6, 7, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 6, 7, 10, 2020)
    print("Expected : [0, 0]")
    print(f"Actual   : {result}")
    print()

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 2, 6, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 2, 6, 10, 2020)
    print("Expected : [0, 13500, 31520, 100, 0]")
    print(f"Actual   : {result}")
    print()

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('spending_file.txt', 1, 2, 1, 2020)")
    result = get_daily_spending('spending_file.txt', 1, 2, 1, 2020)
    print("Expected : [1200, 0]")
    print(f"Actual   : {result}")
    print()
    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('spending_file.txt', 1, 10, 2, 2020)")
    result = get_daily_spending('spending_file.txt', 1, 10, 2, 2020)
    print("Expected : [50, 0, 0, 0, 0, 0, 0, 0, 0, 80]")
    print(f"Actual   : {result}")
    print()
    
    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('empty.txt', 2, 6, 10, 2020)")
    result = get_daily_spending('empty.txt', 2, 6, 10, 2020)
    print("Expected : [0, 0, 0, 0, 0]")
    print(f"Actual   : {result}")
    print()

    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('empty.txt', 2, 2, 11, 2020)")
    result = get_daily_spending('empty.txt', 2, 2, 11, 2020)
    print("Expected : [0]")
    print(f"Actual   : {result}")
    print()