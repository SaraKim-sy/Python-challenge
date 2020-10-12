import os
import csv

# Path to collect data from the Resources folder
file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(file_path) as data:
    csvreader = csv.reader(data)
    next(csvreader, None)
    first_row = next(csvreader)
    previous_row = first_row

    total_months = 0
    total_months += 1

    net_total_profit_losses = 0
    net_total_profit_losses += int(first_row[1])
    
    # creat a list to store changes
    changes = []
    change = 0

    # creat a list to store dates
    dates = []
    

    for row in csvreader:
        total_months = total_months + 1
        net_total_profit_losses += int(row[1])
        change = int(row[1]) - int(previous_row[1])
        changes.append(change)
        dates.append(row[0])
        previous_row = row

    average_changes = round(sum(changes) / len(changes), 2)
    greatest_increase_in_profits_amt = max(changes)
    greatest_increase_in_profits_date = dates[changes.index(greatest_increase_in_profits_amt)]
    greatest_decrease_in_profits_amt = min(changes)
    greatest_decrease_in_profits_date = dates[changes.index(greatest_decrease_in_profits_amt)]

    # print out the analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit_losses}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase_in_profits_date} (${greatest_increase_in_profits_amt})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits_date} (${greatest_decrease_in_profits_amt})")

