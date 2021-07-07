import os
import csv

votes = 0
most_votes = 0
candidates = {}
percent = {}


csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    #loop through all the rows in the csv
    for row in csvreader:

        votes = votes + 1

        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name]+1
        else:
            candidates[candidate_name] = 1

print("")
print("")
print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {votes}")
print("---------------------------------------")
print("")
for key, value in candidates.items():
    if value> most_votes:
        candidate_name = key
        most_votes = value
    percent[key] = round((value / votes) * 100,2)

    print(f"{key} : {percent[key]}% ({value})")
print("")
print("---------------------------------------")
print(f"Winner: {candidate_name}")
print("---------------------------------------")
print("")

f = open('Pypollmain.txt', 'w')
print("", file=f)
print("",file=f)
print("Election Results",file=f)
print("---------------------------------------",file=f)
print(f"Total Votes: {votes}",file=f)
print("---------------------------------------",file=f)
print("",file=f)
for key, value in candidates.items():
    if value> most_votes:
        candidate_name = key
        most_votes = value
    percent[key] = round((value / votes) * 100,2)

    print(f"{key} : {percent[key]}% ({value})",file=f)
print("",file=f)
print("---------------------------------------",file=f)
print(f"Winner: {candidate_name}",file=f)
print("---------------------------------------",file=f)
print("",file=f)