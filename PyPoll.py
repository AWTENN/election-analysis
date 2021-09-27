#What Data do we need?
#Total Number of Votes Cast
#Complete list of Candidates who received Votes
#The % of votes each candidate won
#The total # of votes each candidate won
#The winner of the election based on popular vote
import os
import csv
voting_file = os.path.join("election_results.csv")
with open(voting_file) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row)
#This file is to perform data analysis on voting results
#Creating a TXT file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
 #   txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")


