import os
import csv


total_months = 0

csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

# Loop through all the rows in the csv
    for row in csvreader:

        total_months = total_months + 1

print("Financial Analysis")
print("------------------------------------------------------------------")
print("Total Months" + ":" + (total_months))
