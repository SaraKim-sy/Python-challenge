# Modules
import os
import csv

# Path to collect data from the Resources folder
file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Path to export a text file with the results
output_path = os.path.join('PyBank', 'Analysis', 'financial_analysis.txt')

# Read in the CSV file
with open(file_path) as file:
    csvreader = csv.reader(file)

    # Store the header row
    csv_header = next(file)
    
    # Store the first row and set it as the previous row to use it for calculating changes for each month
    first_row = next(csvreader)
    previous_row = first_row

    # Set variable to count the total number of months & add 1 to it for the first month
    total_months = 0
    total_months += 1

    # Set variable to calculate the net total amount of Profit/Losses & add net profit/loss of the first month 
    net_total_profit_losses = 0
    net_total_profit_losses += int(first_row[1])
    
    # Set variable to calculate changes for each month
    change = 0

    # Creat a dictionary to store dates(key) and change(value)
    date_change_dict = {}
    

    for row in csvreader:
        # Add 1 every row to calculate the total number of months
        total_months = total_months + 1

        # Add the amount of profit/losses for each month to calculate the net total over the entire period
        net_total_profit_losses += int(row[1])

        # Calculate changes for each month 
        change = int(row[1]) - int(previous_row[1])
        
        # Store the date and the change in the dictionary
        date_change_dict[row[0]] = change

        # Set the current row as the previous row for next month
        previous_row = row

    # Calculate the average of the changes in "Profit/Losses" over the entire period
    changes = list(date_change_dict.values())
    average_changes = round(sum(changes) / len(changes), 2)

    # Sort the dictionary by value(change amount) in descending order
    date_change_sorted = sorted(date_change_dict.items(), key=lambda x:x[1], reverse=True)

    # Find the greatest increase in profits (date and amount) over the entire period
    greatest_increase_amt = date_change_sorted[0][1]
    greatest_increase_date = date_change_sorted[0][0]

    # Find the greatest decrease in losses (date and amount) over the entire period
    greatest_decrease_amt = date_change_sorted[-1][1]
    greatest_decrease_date = date_change_sorted[-1][0]

    # Print out the Financial Analysis to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_profit_losses}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})")


    # Export a text file with the results
    with open(output_path, 'w') as outputfile:
        outputfile.write("Financial Analysis\n")
        outputfile.write("----------------------------\n")
        outputfile.write(f"Total Months: {total_months}\n")
        outputfile.write(f"Total: ${net_total_profit_losses}\n")
        outputfile.write(f"Average Change: ${average_changes}\n")
        outputfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})\n")
        outputfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})\n")
