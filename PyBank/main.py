#!/usr/bin/env python
# coding: utf-8
import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")
budget_info = {} #Made an empty dictionary to store information from the csv so I don't have to keep it open

#opening CSV file and storing info in the dictionary 
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        budget_info[row[0]] = int(row[1])
        

#calculating the information needed for the output, and storing them into dictionaries for ease of accesss
dates = list(budget_info.keys())
total_months = len(dates) #stores the total number of months
total = 0 #stores the net total
for date in dates:
    total += budget_info[date]
#made a dictionary to store the difference in profit/loss compared to each month before
differences_dict = {}
for i in range(1, len(dates)):
    current_val = budget_info[dates[i]]
    previous_val = budget_info[dates[i - 1]]
    differences_dict[dates[i]] = (current_val - previous_val)
    
#store the biggest change and the smallest change then loop throught the dictionary to find it    
maxchange = max(differences_dict.values())
minchange = min(differences_dict.values())
for items in differences_dict.items():
    if(items[1] == maxchange):
        maxprofit = (items[0], items[1])
    elif(items[1] == minchange):
        minprofit = (items[0], items[1])
    
#store values from the differences and take the average of it to get average change manually
values = list(differences_dict.values())
average = round(sum(values) / len(values), 2)


#Storing strings so I can write to a text file and also print them out
str1 = "Financial Analysis"
str2 = "-------------------------"
str3 = f"Total Months: {total_months}"
str4 = f"Total: ${total}"
str5 = f"Average Change: ${average}"
str6 = f"Greatest Increase in Profits: {maxprofit[0]} (${maxprofit[1]})" 
str7 = f"Greatest Decrease in Profits: {minprofit[0]} (${minprofit[1]})" 


#Writing strings to terminal and also writing to text file
file = open("Analysis/PyBankOutput.txt","w")
file.write(str1 + "\n")
print(str1)
file.write(str2 + "\n")
print(str2)
file.write(str3 + "\n")
print(str3)
file.write(str4 + "\n")
print(str4)
file.write(str5 + "\n")
print(str5)
file.write(str6 + "\n")
print(str6)
file.write(str7 + "\n")
print(str7)
file.close()