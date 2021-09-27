#What Data do we need?
#Total Number of Votes Cast
#Complete list of Candidates who received Votes
#The % of votes each candidate won
#The total # of votes each candidate won
#The winner of the election based on popular vote
import os
import csv
voting_file = os.path.join("election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(voting_file) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
#Addto the toal vote count
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
 election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
 print(election_results, end="")
 txt_file.write(election_results)
 
 for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
       # print(f"{candidate_name} received {vote_percentage:.1f}% of the vote.")
    #   print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(candidate_results)
        txt_file.write(candidate_results)
 winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
 print(winning_candidate_summary)
 txt_file.write(winning_candidate_summary)
#Print Total Votes
#print(candidate_votes)
    #for row in file_reader:
    #    print(row)
#This file is to perform data analysis on voting results
#Creating a TXT file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
 #   txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
