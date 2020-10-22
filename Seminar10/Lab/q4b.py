import datetime

file = open('transactions.txt', 'r')
output_file = open('transactions-output-2.txt', 'w')
month_year = []
month_total = []
range_data = []

for line in file:
    tx = line.rstrip().split('\t')
    curr_dt = tx[0][3:]

    if len(month_year) > 0:
        if curr_dt in month_year:
            range_data[month_year.index(curr_dt)].append(tx)
            month_total[month_year.index(curr_dt)] += float(tx[2][1:])
        else:
            # Iterate every month year we have from oldest to latest
            for i in range(len(month_year)):
                # diff = (datetime.datetime.strptime(month_year[i], '%m-%Y').total_seconds() - datetime.datetime.strptime(curr_dt, '%m-%Y').total_seconds())
                # If we've reached the end means we're at the latest date
                # and if a month year is finally newer than curr_dt, we slot it in right there.
                if (datetime.datetime.strptime(month_year[i], '%m-%Y') - datetime.datetime.strptime(curr_dt, '%m-%Y')).total_seconds() > 0 and len(month_year) > i + 1:
                    month_year.insert(i + 1, curr_dt)
                    month_total.insert(i + 1, float(tx[2][1:]))
                    range_data.insert(i + 1, [tx])
                    break
                else:
                    month_year.append(curr_dt)
                    month_total.append(float(tx[2][1:]))
                    range_data.append([tx])
                    break
    else:
        month_year.append(curr_dt)
        month_total.append(float(tx[2][1:]))
        range_data.append([tx])

for i in range(len(month_year)):
    print(month_year[i] + ': total transaction amount is $' + str(month_total[i]))

    for item in range_data[i]:
        print('\t' + item[1] + '\t' + item[2])
    print()

