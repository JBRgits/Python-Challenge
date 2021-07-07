import os
import csv

total_p_and_l = 0
current_month = 0
last_month = 0
total_months = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 999999999


csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    #loop through all the rows in the csv
    for row in csvreader:

        total_p_and_l = total_p_and_l + int(row[1])

        total_months = total_months + 1

        current_month = int(row[1])

        if total_months > 1:

            change = current_month - last_month
            total_change = total_change + change
            average_change = total_change/(total_months-1)

            if change > greatest_increase:
                greatest_increase = change
                grt_inc_date = str(row[0])

            if change < greatest_decrease:
                greatest_decrease = change
                grt_dec_date = str(row[0])

        last_month = int(row[1])

print("")
print("")
print("Financial Analysis")
print("-------------------------------------------------------------------")
print("")
print("")
print(f"Total Months: {total_months}")
print(f"Total: ${total_p_and_l}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {grt_inc_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {grt_dec_date} (${greatest_decrease})")
print("")
print("")
print("------------------------------------------------------------------")


f = open('Pybankmain.txt','w')
print("",file =f)
print("",file = f)
print("Financial Analysis",file = f)
print("-------------------------------------------------------------------",file=f)
print("",file=f)
print("",file=f)
print(f"Total Months: {total_months}",file=f)
print(f"Total: ${total_p_and_l}",file=f)
print(f"Average Change: ${average_change:.2f}",file=f)
print(f"Greatest Increase in Profits: {grt_inc_date} (${greatest_increase})",file=f)
print(f"Greatest Decrease in Profits: {grt_dec_date} (${greatest_decrease})",file=f)
print("",file=f)
print("",file=f)
print("------------------------------------------------------------------",file=f)

