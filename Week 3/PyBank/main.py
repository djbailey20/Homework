import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# csvpath = "C:\Users\shado\Documents\LearnPython\Day3\Stu_CerealCleaner\Resources\cereal.csv"
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    netProfitLosses = 0
    months = 0
    previousValue = 867884
    monthIncrease = ""
    increase = 0
    monthDecrease = ""
    decrease = 0
    totalChange = 0

    for row in csvreader:
        netProfitLosses = int(row[1])+netProfitLosses
        if (increase < int(row[1])-previousValue):
            increase = int(row[1])-previousValue
            monthIncrease = row[0]
        if (decrease > int(row[1])-previousValue):
            decrease = int(row[1])-previousValue
            monthDecrease = row[0]
        totalChange = totalChange+int(row[1])-previousValue
        print(totalChange)
        months = months + 1
        previousValue = int(row[1])

    print(f"Total Months: {months}")
    print(f"Total: ${netProfitLosses}")
    print(f"Average Change: ${round(totalChange/(months-1),2)}")
    print(f"Greatest Increase in Profits: {monthIncrease} (${increase})")
    print(f"Greatest Decrease in Profits: {monthDecrease} (${decrease})")

    f = open('info.txt', 'w')
    f.write(f"Total Months: {months}\n")
    f.write(f"Total: ${netProfitLosses}\n")
    f.write(f"Average Change: ${round(totalChange/months)}\n")
    f.write(f"Greatest Increase in Profits: {monthIncrease} (${increase})\n")
    f.write(f"Greatest Decrease in Profits: {monthDecrease} (${decrease})\n")
    f.close()
