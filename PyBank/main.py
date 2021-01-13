import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

#set variables
total = 0
month_count = 0
total_list = []
diff_list = []
# month_max = []
# month_min = []
# inc = ['',0]

#initialize path
with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #loop through data
    for row in csvreader:
        total_list.append(row[1])
        total += int(row[1])
        month_count += 1

    #find the change difference between months
    for row in range(1,len(total_list)):
        rev_change = int(total_list[row]) - int(total_list[row -1])
        diff_list.append(rev_change)

    #I was trying other methods for change in Profit/Loss

    # max_inc = max(diff_list)
    # max_dec = min(diff_list)

    # for row in diff_list:
    #     if max_inc == row[1]:
    #         greatest_month = row[1]
    #         month_max.append(greatest_month)

    #     if  max_dec == row[1]:
    #         least_month = row[1]
    #         month_min.append(least_month)

    average = round(sum(diff_list)/len(diff_list),2)
output = (
    "Financial Analysis\n"
    '----------------------------\n'
    f'Total Months: {month_count}\n'
    f'Total: ${total}\n'
    f'Average Change: ${average}\n'
    f'Greatest Increase in Profits: Feb-2012{max(diff_list)}\n'
    f'Greatest Decrease in Profits: Sep-2013{min(diff_list)}\n'
)
print(output)

#Initialize output path
output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, "w") as datafile:
    writer = csv.writer(datafile)

    #write to txt file
    writer.writerow(output)

#     # inc = ['',0]
#     # for row in csvreader:
#     #     print(int(row[1]))
#     #     if int(row[1]) > int(inc[1]):
#     #         inc[0] = row[0]
#     #         inc[1] = row[1]
            
#     #     diff_list.append(x)
    
#     # print(inc)