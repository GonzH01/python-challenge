# Importing necessary modules
import os
import csv

# Initializing variables for financial analysis
total_months_count = 0
net_profit_loss = 0
monthly_profit_changes = []
report_dates = []

# Path to the input CSV file
csv_file_path = os.path.join('Resources', 'budget_data.csv')

# Processing the CSV file
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Skipping the header row
    next(csv_reader)

    # Initializing variables with the first row of data
    first_row = next(csv_reader)
    total_months_count = 1
    net_profit_loss = int(first_row[1])
    previous_month_profit = int(first_row[1])

    # Iterating through each row in the CSV
    for row in csv_reader:
        # Tracking total months and net profit/loss
        total_months_count += 1
        current_month_profit = int(row[1])
        net_profit_loss += current_month_profit

        # Calculating monthly profit change and storing it
        profit_change = current_month_profit - previous_month_profit
        monthly_profit_changes.append(profit_change)
        report_dates.append(row[0])

        # Updating the previous month's profit for the next iteration
        previous_month_profit = current_month_profit

# Calculating average profit change, greatest increase, and greatest decrease
average_profit_change = round(sum(monthly_profit_changes) / len(monthly_profit_changes), 2)
greatest_profit_increase = max(monthly_profit_changes)
greatest_profit_decrease = min(monthly_profit_changes)

# Identifying the dates for greatest increase and decrease
greatest_increase_date = report_dates[monthly_profit_changes.index(greatest_profit_increase)]
greatest_decrease_date = report_dates[monthly_profit_changes.index(greatest_profit_decrease)]

# Printing the financial analysis report
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months_count}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_profit_decrease})")

# Writing the results to a text file
output_file_path = os.path.join('analysis', 'results.txt')
with open(output_file_path, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-------------------------------\n")
    text_file.write(f"Total Months: {total_months_count}\n")
    text_file.write(f"Total: ${net_profit_loss}\n")
    text_file.write(f"Average Change: ${average_profit_change}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_profit_decrease})\n")
