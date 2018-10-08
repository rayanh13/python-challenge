"""PyBank Solution"""

import os
import csv

file_to_load = 'budget_data.csv'
file_to_output = 'budget_data_output.txt'

# Placeholders for contents
profit_losses = []
tem_full_dates = []
tem_month_dates = []
tem_year_dates = []
monthly_change = []

# Read the csv file and convert it to a list of dictionaries 
with open(file_to_load, newline="") as new_data:
    reader = csv.reader(new_data, delimiter=",")
    header = next(reader)
    for row in reader:
        dates = row[0].split("-")
        tem_month_dates.append(dates[0])
        tem_year_dates.append(dates[1])
        tem_full_dates.append(row[0])
        profit_losses.append(row[1])

        # Find the total number of months included in the dataset
        total_months = len(tem_month_dates)

        # Calculate the total net amount of "Profit/Losses" over the entire period
        total_profit_losses = 0
        for x in range(total_months):
            total_profit_losses = total_profit_losses + int(profit_losses[x])

        # Calculate the change by period
        y = 0
        b = 0
        for y in range(total_months):
            if y == 0:
                change = 0
            else:
                change = int(profit_losses[y]) - int(profit_losses[b])
                b = b + 1
        
        monthly_change.append(change)

# The average change in "Profit/Losses" between months over the entire period
total_change = sum(monthly_change)
sub_total_months = len(monthly_change) - 1
average_change = total_change / sub_total_months
tem_average_change = round(average_change,2)
#print(total_change)
#print(sub_total_months)
#print(average_change)

# The greatest increase in profits (date and amount) over the entire period
max_profit_losses = max(monthly_change)
max_index = monthly_change.index(max_profit_losses)
max_dates = tem_full_dates[max_index]

# The greatest decrease in losses (date and amount) over the entire period
min_profit_losses = min(monthly_change)
min_index = monthly_change.index(min_profit_losses)
min_dates = tem_full_dates[min_index]


# Printing results to terminal
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_losses))
print("Average Change: $" + str(tem_average_change))
print("Greatest Increase in Profits: " + str(max_dates) + " " + "($" + str(max_profit_losses) + ")")
print("Greatest Decrease in Profits: " + str(min_dates) + " " + "($" + str(min_profit_losses) + ")")

# Write all of the results data to csv
with open(file_to_output, "a") as datafile:
    datafile.write("Financial Analysis" + "\n")
    datafile.write("--------------------------------------------" + "\n")
    datafile.write("Total Months: " + str(total_months) + "\n")
    datafile.write("Total: $" + str(total_profit_losses) + "\n")
    datafile.write("Average Change: $" + str(tem_average_change) + "\n")
    datafile.write("Greatest Increase in Profits: " + str(max_dates) + " " + "($" + str(max_profit_losses) + ")" + "\n")
    datafile.write("Greatest Decrease in Profits: " + str(min_dates) + " " + "($" + str(min_profit_losses) + ")" + "\n")