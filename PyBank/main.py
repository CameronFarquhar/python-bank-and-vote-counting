import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

# def function_data(data):
    
#     total_months = str(data[0])

#     total_budget = int(data[1])

with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    months = list(csvreader)

    print(len(months))

    # total_budget = [1]
    
    # # function_data() = [0]

    # for row in csvreader:

    #      if total_budget > total_budget + int(row[1]):

    #         total_budget = biggest

    #         print(int(biggest))

