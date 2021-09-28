# election-analysis
## Challenege Overview
I am doing an election Audit for a local election in Colorado for Congress. I am trying to determine the amount of votes and percentage of votes for each county and candidate.

Here is the list of tasks I did for this audit:
1. Find the total number of votes
2. Find the list of candidates for this vote
3. Find the number of votes  and percentage of votes for each county. 
4. Determine the county with the largest number of votes.
5. Find the number of votes  and percentage of votes for each candidate.
6. Determine the winner of the election based on vote count and percentage of votes.
## Resources
- Data used: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.60
 ## Challenge Results
Here is the Analysis of the election data:
- There were 369,111 votes cast in this election.
- Counties
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
  - Denver has the largest number of votes with 306,055 which is 82.8% of the total votes.
- Candidates:
  - Charles Casper Stockham
  - Dianna DeGette
  - Raymon Anthony Doane
- Results
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Dianna DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- WINNER
  - The winner of this election is Dianna Degette with 73.8% of the vote and 272,892 number of votes.
 ## Challenge Summary
 Members of the 3rd Precinct of the Colorado Election Commission, I believe the python script that I have used to provide the data for this election can be used in any election.
 We can use this script for much larger elections, for example, a presidential election by changing all of the county info variables to state variables and change county to     state for all of the text write coding.
 If we wanted to dig deeper we could keep the code for the counties and add in state info coding so that we can find what county of what state voted for which candidate. We could also change the script to say the percentage of state votes and county votes per candidate to obtain more precise measures of what votes are for who depending on county/precinct in each state.
