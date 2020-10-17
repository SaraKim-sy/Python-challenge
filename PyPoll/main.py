# Modules
import os
import csv

# Path to collect data from the Resources folder
file_path = os.path.join('Resources', 'election_data.csv')

# Path to export a text file with the results
output_path = os.path.join('Analysis', 'election_results.txt')

# Read in the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    # Store the header row
    csv_header = next(file)
    
    # Set variable to count the total number of votes cast
    total_votes = 0

    # List and Dictionary to store data
    candidates_voted = []
    candidates_dict = {}

    for row in csvreader:
        # Add 1 every row to calculate the total number of votes cast
        total_votes = total_votes + 1

        # Store all the candidates each voter voted in the list
        candidates_voted.append(row[2])

    # Count the total number of votes each candidate won
    for candidate in candidates_voted:
        if candidate not in candidates_dict:
            candidates_dict[candidate] = 1
        else:
            candidates_dict[candidate] += 1

    # Sort the dictionary by value(the number of votes) in descending order
    candidates_sorted = sorted(candidates_dict.items(), key=lambda x:x[1], reverse=True)

    # Find the winner
    winner = candidates_sorted[0][0]

# Print out the Election Results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(candidates_sorted)):
    # Each candidate's name 
    name = candidates_sorted[i][0]
    # The total number of votes each candidate won
    votes_num = candidates_sorted[i][1]
    # Calculate the percentage of votes each candidate won
    votes_percent = round(votes_num/total_votes*100, 3)
    print(f"{name}: {votes_percent}% ({votes_num})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Export a text file with the results
with open(output_path, 'w') as outputfile:
    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("-------------------------\n")
    for i in range(len(candidates_sorted)):
        name = candidates_sorted[i][0]
        votes_num = candidates_sorted[i][1]
        votes_percent = round(votes_num/total_votes*100, 3)
        outputfile.write(f"{name}: {votes_percent}% ({votes_num})\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("-------------------------\n")
