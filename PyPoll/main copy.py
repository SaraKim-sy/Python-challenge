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
    previous_row = first_row

    total_votes = 0
    total_votes += 1

    candidates = []
    candidates.append(first_row[2])
    candidates_voted = []

    candidates_dict = {}
    candidates_dict[first_row[2]] = 1

    for row in csvreader:
        # Add 1 every row to calculate the total number of votes cast
        total_votes = total_votes + 1

        candidates_voted.append(row[2])
        
        if (row[2] != previous_row[2]) and (row[2] not in candidates):
            candidates.append(row[2])
        previous_row = row

        
    for candidate in candidates_voted:
        if candidate not in candidates_dict:
            candidates_dict[candidate] = 1
        else:
            candidates_dict[candidate] += 1

    winner = list(sorted(candidates_dict.items(), key=lambda x:x[1],reverse=True)[0])[0]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {round(candidates_dict[candidate]/total_votes*100, 5)}% ({candidates_dict[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
