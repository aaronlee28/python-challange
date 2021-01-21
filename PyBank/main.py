#import CSV file
import os
import csv 
csvpath = os.path.join("Resources", "pybank.csv")

#List to store data
total_months = []
pnl = []
months = []
total_difference = []
average_change = []
avgchangedec = []
greatest_increase = []
greatest_increase_date = ""
greatest_decrease = []
greatest_decrease_date = ""

# csv reader delimiter
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



    #read the header row first 
    csv_header = next(csvreader)
    

    #zeroes
    num_rows = 0
    total = 0
    #for loop 
    for row in csvreader:

        #Total Months
        num_rows += 1

        #list of months 
        months.append(row[0])

        #Total profit and loss 
        pnl.append(int(row[1]))
        total = sum(pnl)

    #average difference 
    for x in range(1,len(pnl)):
        total_difference.append(pnl[x]-pnl[x-1])    
    sumtotaldiff = sum(total_difference)
    avgchangedec = sumtotaldiff / len(pnl)
    average_change = "{:.2f}".format(avgchangedec) 
    
    #greatest increase in profits 
    greatest_increase = max(pnl)
    greatest_increase_date = str(months[pnl.index(max(pnl))])

    #greatest decrease in profits 
    greatest_decrease = min(pnl)
    greatest_decrease_date = str(months[pnl.index(min(pnl))])

# label every print 
fa = ("Financial Analysis")
dash = ("-------------------------------------------------")
tm = (f"Total Months: {num_rows}")
t = (f"Total:${total}")
ac = (f"Average change: ${average_change}")
giip = (f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
gdip = (f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print Everything 
print(fa)
print(dash)
print(tm)
print(t)
print(ac)
print(giip)
print(gdip)

#  compile print 
txtwrite = (fa,dash,tm,t,ac,giip,gdip)

# write to txt file 
output_path = os.path.join("analysis","analysis.txt")
with open(output_path, "w") as tfile:
    for a in txtwrite:
        tfile.write(a)
        tfile.write("\n")


