# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on populare vote
# Assign a variable for the file to load and the path
file_to_load= "resources\election_results.csv"
#impot the CSV file and OS modules
import os
import csv  
# Add the file name variable that refrences the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join( "analysis", "election_analysis.txt")
# Add the vote counter before the with open statement 
total_votes = 0
# Add cadidate options and candidate voter list and dictionary 
candidate_options = []
candidate_votes= {}
# Winning count and winning percentage tacker
winning_cadidate= ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the hearder row
    headers = next(file_reader)
    print(headers)
#Print each row in the CSV file
    for row in file_reader:
     total_votes += 1
     candidate_name = row[2]
# If the candidate does not match a candidate listed in the cadidate options list
     if candidate_name not in candidate_options:
# Add cadidate name to the candidate options list
        candidate_options.append(candidate_name)
# Add the cadidate vote count
        candidate_votes[candidate_name] = 0
# Add vote to cadidate coumt
     candidate_votes[candidate_name]+= 1
# Save the results to our text file
with open (file_to_save,"w") as txt_file:
 # print the final vote count to the terinaml
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,} \n"
        f"---------------------------\n")
 # Save the final vote count to the text file
    txt_file.write(election_results)
    print(election_results, end="")

    # Determine the percentage of votes for each cadidate by looping though the counts
    # 1. Iterate through the cadidate list
    for candidate_name in candidate_votes:
        #retrieve vote couldnt of a cadidate
        vote = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(vote)/float(total_votes)*100
        # Assign canidate results variable  to print each cadidat, their voter count, and percentage to terminal
        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n" )
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count
        if (vote> winning_count) and (vote_percentage>winning_percentage):
        # 2. if true set winning count = to vote and winning_ percentage = to vote percentage
            winning_count = vote
            winning_percentage = vote_percentage
        # 3. Set winning candidate = the candidiate name
            winning_cadidate = candidate_name
            winning_candidate_summary = (
                f"------------------------------------------ \n"
                f"Winner: {winning_cadidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

