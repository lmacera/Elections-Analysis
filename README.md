# Elections-Analysis
#Election_Analysis
## Project Overview
Steve and Tom, two employees of the Colorado Board of Elections, have asked for our assistance with completing the following tasks for the election audit of a local congressional election.
1. Calculate the total number of votes cast.
2. Get a complete list of counties that received votes in the election.
3. Calculate the number of votes in each county.
4. calculate the percentage of votes for each county.
5. Determine the winning county of the election based on voter turnout.
6. Get a complete list of candidates who received votes.
7. Calculate the percentage of votes each candidate won.
8. Calculate the percentage of votes each candidate won
9. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results
Using VS code and Python our team was able to analyze the election_results.csv to find the below results:
- There were 369,711 total votes cast in the election
- the counties included in the election are
	- Jefferson
	- Denver
	- Arapahoe
- The county results were
	- Jefferson county received 10.5% of the vote and had 38,855 number of votes
- Denver county received 82.8%% of the vote and had 306,055 number of votes
- Arapahoe county received 6.7% of the vote and had 24,801 number of votes
- The largest County turnout was:
- Denver county, receiving 82.8% of the vote and had 306,055 number of votes
- The candidates are:
 	 - Charles Casper Stockham
  - Diana DeGette
 	 - Raymon Anthony Doane
- The candidate results were:
  	- Charles Casper Stockham received 23.0% of the vote and had 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and had 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and had 11,606 number of votes.
- The winner of the election was:
- Diana DeGette, who received 73.8% of the vote and had 272,892 number of votes.

With VS code and Python our team was able to analysis approximately 400,000 rows of raw election data by creating lists and dictionaries. Using these lists and dictionaries we filtered through the data using For Loops, conditional statements, and indexing to assign variables and perform mathematical calculations. The below images demonstrate just a few of these items pulled from our code.
### List and Dictionary Creation
![ List and Dictionary Example]( https://github.com/lmacera/Elections-Analysis/blob/main/Resources%202/List%20and%20Dictionary%20Example.PNG )


### For Loop

![ For Loop Example]( https://github.com/lmacera/Elections-Analysis/blob/main/Resources%202/For%20Loop%20Example.PNG )

### Conditional statement

![ If Statement Example]( https://github.com/lmacera/Elections-Analysis/blob/main/Resources%202/If%20Statement%20Example.PNG )

### Final Election Results

![Final Election Results Text File]( https://github.com/lmacera/Elections-Analysis/blob/main/Resources%202/Final%20Election%20Results%20Text%20File.PNG )

## Election-Audit Summary

Based off the information our team was able to pull for the Colorado Board of Elections it is our team’s suggestion that the scrip be used to analyze further election data. The scrip can and should be modified for further analysis on other election data. Assuming the Colorado Elections Board can obtain more data results on these elections, it would be beneficial for the board to consider modifying the Elections-Analysis script to include information on, populations in each county and the voting methods in each county. Following similar procedures as above the scrips can be modified to include lists and dictionaries to present data on the populations in each county. For example, we could find what the total population of Jefferson County is and what percentage of the Jefferson county population actually cast a vote in the election. Similarly, the Elections-Analysis script can be modified to determine the most popular methods of voting in a county. Using similar methods mentioned above, the script can be modified to filter results for each county to find the most popular method of voting in each county. For example, it would be beneficial to determine if out largest county, Denver, had more mail in voters or in person voters. These modifications would not only increase the efficiency for the Board to analyze the data of each election, but also help them determine how to structure elections to increase voter turnout. 

o
