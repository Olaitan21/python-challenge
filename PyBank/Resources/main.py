
import os
import csv


pyBank_csv = os.path.join(',,', "Resources",'budget_data.csv')



total_month = 0
month_of_change = []
net_change_list = []
greatest_increase =["",0]
greatest_decrease =["", 99999999999999999]
total_net = 0


with open(pyBank_csv) as CSvfile:
    csv_reader = csv.reader(csvfile, delimiter =',')

  # Read the header row first (skip the step if ther is now header)
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_month = total_month + 1
    total_net =total_net +int(first_row[1])
    prev_net =int(first_row[1])

   # Read each row of data after the header
    for row in csvreader:
       total_month =total_month + 1
       total_net = total_net + int(first_row[1])
       total_net = int(first_row[1])
       prev_net =int(first_row[1])
       net_change_list = net_change_list + [net_change]
       month_of_change = month_of_change + [row[0]]
       if net_change > greatest_increse[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = net_change
       if net_change < greatest_decrease[1]:
           greatest_decease[0] = row[0]
           greatest_decaase[1]=net_change


net_monthly_average = sum(net_change_list)/len(net_change_list)
print("Financial Anaalysis")
print(f"Total Months:{total_month}")
print(f"Total: ${total_net}")
print(f"Average Cange: ${net_monthly_average}")
print(f"Greatest_Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})")
print(f"Greatest_Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[0]})")


output=(f"\nFiancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total:${Total_net}\n"
    f"Average Change: ${net_monthly_average}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n"
with open("output.txt", 'w')as txt_file:
    txt_file.write(output)
 

 



