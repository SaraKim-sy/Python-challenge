import os
import csv

file_path = os.path.join('Resources', 'budget_data.csv')
with open(file_path) as data:
    csvreader = csv.reader(data)
    next(csvreader, None)
    first_row = next(csvreader)
    previous_row = int(first_row[1])

    total_months = 0
    total_months += 1

    net_total_profit_losses = 0
    net_total_profit_losses += int(first_row[1])

    changes = []
    change = 0
    

    for row in csvreader:
        total_months = total_months + 1
        net_total_profit_losses += int(row[1])
        change = int(row[1]) - previous_row
        changes.append(change)
        previous_row = int(row[1])

    average_changes = round(sum(changes) / len(changes), 2)
    

    print(total_months)
    print(net_total_profit_losses)
    print(average_changes)