import os
import csv

# Path to collect data from the Resources folder
file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Path to export a text file with the results
output_path = os.path.join('PyPoll', 'Analysis', 'election_results.txt')

# Read in the CSV file
with open(file_path) as file:
    csvreader = csv.reader(file)
    next(csvreader, None)
    first_row = next(csvreader)

    total_votes = 0

    candidates_voted = []

    candidates_dict = {}

    for row in csvreader:
        # Add 1 every row to calculate the total number of votes cast
        total_votes = total_votes + 1
        candidates_voted.append(row[2])
        
    for candidate in candidates_voted:
        if candidate not in candidates_dict:
            candidates_dict[candidate] = 1
        else:
            candidates_dict[candidate] += 1

    candidates_dict_sorted = sorted(candidates_dict.items(), key=lambda x:x[1], reverse=True)
    winner = list(sorted(candidates_dict.items(), key=lambda x:x[1], reverse=True)[0])[0]

    print(candidates_dict_sorted)
'''
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates_dict_sorted:
    print(f"{candidate}: {round(candidates_dict_sorted[candidate]/total_votes*100, 5)}% ({candidates_dict_sorted[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
'''