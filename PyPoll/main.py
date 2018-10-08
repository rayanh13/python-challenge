"""PyPoll Solution"""

import os
import csv

file_to_load = 'election_data.csv'
file_to_output = 'election_data_output.txt'

# Placeholders for contents
tem_voters_id = []
tem_county = []
tem_candidate = []


# Read the csv file and convert it to a list of dictionaries 
with open(file_to_load, newline="") as new_data:
    reader = csv.reader(new_data, delimiter=",")
    header = next(reader)
    for row in reader:
        tem_voters_id.append(row[0])
        tem_county.append(row[1])
        tem_candidate.append(row[2])

# Find he total number of votes cast
total_len_candidate = len(tem_voters_id)
#print(total_len_candidate)

# Find a complete list of candidates who received votes
# Candidate name is equal to 'Khan'
total_votes_khan = tem_candidate.count('Khan')
total_votes_khan_percentage = total_votes_khan/total_len_candidate

# Candidate name is equal to 'Correy'
total_votes_correy = tem_candidate.count('Correy')
total_votes_correy_percentage = total_votes_correy/total_len_candidate

# Candidate name is equal to 'Li'
total_votes_li = tem_candidate.count('Li')
total_votes_li_percentage = total_votes_li/total_len_candidate

# Candidate name is equal to 'O'Tooley'
total_votes_otooley = tem_candidate.count("O'Tooley")
total_votes_otooley_percentage = total_votes_otooley/total_len_candidate

# The winner of the election based on popular vote
#candidates = {total_votes_khan,total_votes_correy,total_votes_li,total_votes_otooley}
#winner = max(candidates)
#winner_name = winner.index[tem_candidate]
#print(winner_name, 'wins')
if total_votes_khan > max(total_votes_correy,total_votes_li,total_votes_otooley):
    winner_name = "Khan"

if total_votes_correy > max(total_votes_khan,total_votes_li,total_votes_otooley):
    winner_name = "Correy"

if total_votes_li > max(total_votes_khan,total_votes_correy,total_votes_otooley):
    winner_name = "Li"

if total_votes_otooley > max(total_votes_khan,total_votes_correy,total_votes_li):
    winner_name = "O'Tooley"

# Printing results to terminal
print("Election Results")
print("--------------------------------------------")
print("Total Votes: " + str(total_len_candidate))
print("--------------------------------------------")
print("Khan: " + "{:.3%}".format(total_votes_khan_percentage) + " " + "(" + str(total_votes_khan) + ")")
print("Correy: " + "{:.3%}".format(total_votes_correy_percentage) + " " + "(" + str(total_votes_correy) + ")")
print("Li: " + "{:.3%}".format(total_votes_li_percentage) + " " + "(" + str(total_votes_li) + ")")
print("O'Tooley: " + "{:.3%}".format(total_votes_otooley_percentage) + " " + "(" + str(total_votes_otooley) + ")")
print("--------------------------------------------")
print("Winner: " + str(winner_name))
print("--------------------------------------------")

# Write all of the election data to csv
with open(file_to_output, "a") as datafile:
    datafile.write("Election Results" + "\n")
    datafile.write("--------------------------------------------" + "\n")
    datafile.write("Total Votes: " + str(total_len_candidate) + "\n")
    datafile.write("--------------------------------------------" + "\n")
    datafile.write("Khan: " + "{:.3%}".format(total_votes_khan_percentage) + " " + "(" + str(total_votes_khan) + ")" + "\n")
    datafile.write("Correy: " + "{:.3%}".format(total_votes_correy_percentage) + " " + "(" + str(total_votes_correy) + ")" + "\n")
    datafile.write("Li: " + "{:.3%}".format(total_votes_li_percentage) + " " + "(" + str(total_votes_li) + ")" + "\n")
    datafile.write("O'Tooley: " + "{:.3%}".format(total_votes_otooley_percentage) + " " + "(" + str(total_votes_otooley) + ")" + "\n")
    datafile.write("--------------------------------------------" + "\n")
    datafile.write("Winner: " + str(winner_name) + "\n")
    datafile.write("--------------------------------------------" + "\n")
