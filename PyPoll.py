# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on populare vote
import datetime
now = datetime.datetime.now()
import random
print("The time right now is ", now)
# Assign a variable for the file to load and the path
file_to_load= "resources\election_results.csv"
#impot the CSV file and OS modules
import os
import csv  
# Add the file name variable that refrences the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join( "analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the hearder row
    headers = next(file_reader)
    print(headers)
    


