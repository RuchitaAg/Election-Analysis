import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_results.txt")

# Initialise total vote count and candidate options list:
total_votes = 0
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Initialise variables for declaring winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    header = next(file_reader)
    #print(header)

# To print rows from the CSV file
    for row in file_reader:
        #print(row)
        total_votes +=1

        # Get candidates name:
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add to the candidate options list
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
   
            # Begin tracking total votes for each candidate.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:

    election_summary = (
        f"Election Results\n"
        f"-----------------------------------------------------\n"
        f"total votes: {total_votes:,}\n"
        f"-----------------------------------------------------\n")

    #print eclection summary to terminal:
    print(election_summary, end=" ")

    #print election summary to the text file
    txt_file.write(election_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.

    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes)*100

        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: recieved {vote_percentage:.1f}% of vote ({votes:,})\n")
    
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
    
        # Save the candidate results to the text file.
        txt_file.write(candidate_results)

        # Loop through total votes and candidate names to identify winner
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"----------------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------------------------------\n")
  
    print(winning_candidate_summary)

    # Input winning summary in text file
    txt_file.write(winning_candidate_summary)
    