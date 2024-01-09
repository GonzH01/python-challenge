# Importing necessary modules
import os
import csv

# Creating a path to the election data CSV file
election_data_csv_path = os.path.join('Resources', 'election_data.csv')

# Initializing variables and lists for storing data
total_votes_count = 0
candidate_votes_count = {}
percentage_votes_list = []

# Processing the CSV file
with open(election_data_csv_path) as election_csv_file:
    csv_reader = csv.reader(election_csv_file, delimiter=',')
    next(csv_reader)  # Skipping the header row

    # Looping through each row of the CSV file
    for row in csv_reader:
        total_votes_count += 1
        candidate_name = row[2]

        # Recording each candidate's vote count
        if candidate_name not in candidate_votes_count:
            candidate_votes_count[candidate_name] = 1
        else:
            candidate_votes_count[candidate_name] += 1

# Calculating vote percentages and identifying the winner
winning_candidate = max(candidate_votes_count, key=candidate_votes_count.get)
winning_candidate_votes = candidate_votes_count[winning_candidate]

for candidate, votes in candidate_votes_count.items():
    percentage = round((votes / total_votes_count) * 100, 3)
    percentage_votes_list.append(f"{candidate}: {percentage}% ({votes})")

# Printing election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes_count}")
print("--------------------------")
print('\n'.join(percentage_votes_list))
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Writing results to a text file
results_text_file_path = os.path.join('analysis', 'results.txt')
with open(results_text_file_path, "w") as results_text_file:
    results_text_file.write("Election Results\n")
    results_text_file.write("--------------------------\n")
    results_text_file.write(f"Total Votes: {total_votes_count}\n")
    results_text_file.write("--------------------------\n")
    results_text_file.write('\n'.join(percentage_votes_list) + "\n")
    results_text_file.write("--------------------------\n")
    results_text_file.write(f"Winner: {winning_candidate}\n")
    results_text_file.write("--------------------------\n")
