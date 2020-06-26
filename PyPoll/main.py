#!/usr/bin/env python
# coding: utf-8
import os
import csv


filepath = os.path.join("Resources", "election_data.csv")



#used a dictionary to store candidate info by candidates as keys and the number of votes as values
candidate_info = {}
total_votes = 0
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        #this checks if the candidate is already in the dictionary, as we need to reference it in order to add 1 vote
        if candidate in candidate_info:
            candidate_info[candidate] += 1
        else:
            candidate_info[candidate] = 1




#strings is a list that holds all the strings, so we can print it and also write it to a txt file
strings = ["Election Results", "----------------------", f"Total Votes: {total_votes}", "----------------------"]
for candidate, count in candidate_info.items():
    stringtoAdd = f"{candidate}: {round(((count/total_votes) * 100),3)}% ({count})"
    strings.append(stringtoAdd)
sorted_dict = sorted(candidate_info.items(), key = lambda keyval: keyval[1], reverse = True)
strings.append("----------------------")
stringtoAdd = f"Winner: {sorted_dict[0][0]}"
strings.append(stringtoAdd)
strings.append("----------------------")



#opening a new file in write mode that doesn't exist will create it
#I printed each string to the terminal, as well as write it with a newline character at the end of each txt file row
file = open("Analysis/PyPollOutput.txt","w")
for string in strings:
    print(string)
    file.write(string + "\n")
file.close()