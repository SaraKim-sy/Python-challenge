import os
import csv

# Path to collect data from the Resources folder
file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Path to export a text file with the results
output_path = os.path.join('PyBank', 'Analysis', 'financial_analysis.txt')

# Read in the CSV file
with open(file_path) as file:
    csvreader = csv.reader(file)
    next(csvreader, None)
    first_row = next(csvreader)
    previous_row = first_row

    total_months = 0
    total_months += 1

    net_total_profit_losses = 0
    net_total_profit_losses += int(first_row[1])
    
    # Creat a list to store changes
    changes = []
    change = 0

    # Creat a dictionary to store changes : dates
    changes_dates_dict = {}
    

    for row in csvreader:
        # Add 1 every row to calculate the total number of months
        total_months = total_months + 1

        # Add the amount of profit/losses for each month to calculate the net total over the entire period
        net_total_profit_losses += int(row[1])
        change = int(row[1]) - int(previous_row[1])
        changes.append(change)
        changes_dates_dict[change] = row[0]
        previous_row = row

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    average_changes = round(sum(changes) / len(changes), 2)

    # Find the greatest increase in profits (date and amount) over the entire period
    greatest_increase_in_profits_amt = max(changes)
    greatest_increase_in_profits_date = changes_dates_dict[greatest_increase_in_profits_amt]

    # Find the greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_in_profits_amt = min(changes)
    greatest_decrease_in_profits_date = changes_dates_dict[greatest_decrease_in_profits_amt]

    # Print out the Financial Analysis to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit_losses}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase_in_profits_date} (${greatest_increase_in_profits_amt})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits_date} (${greatest_decrease_in_profits_amt})")

    # Export a text file with the results
    with open(output_path, 'w') as outputfile:
        outputfile.write("Financial Analysis\n")
        outputfile.write("----------------------------\n")
        outputfile.write(f"Total Months: {total_months}\n")
        outputfile.write(f"Total: ${net_total_profit_losses}\n")
        outputfile.write(f"Average Change: ${average_changes}\n")
        outputfile.write(f"Greatest Increase in Profits: {greatest_increase_in_profits_date} (${greatest_increase_in_profits_amt})\n")
        outputfile.write(f"Greatest Decrease in Profits: {greatest_decrease_in_profits_date} (${greatest_decrease_in_profits_amt})\n")