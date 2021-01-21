# import CSV file
import os
import csv 
csvpath = os.path.join("Resources", "pypoll.csv")

# List to store data
khan_count = []
correy = []
li = []
otooley = []
votersid = []
county = []
candidate = []
winner = "" 
        
# Zeroes         
num_rows = 0

# CSV reader delimiter
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)

    # Print(f"CSV Header: {csv_header}")

    # For row 
    for row in csvreader: 

        # Total votes
        num_rows += 1

        # Assign row 
        votersid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Count Khan
khan_count = candidate.count('Khan')

# Khan percent 
khan_decimal = (khan_count / num_rows) * 100 
khan_percent = "{:.3f}".format(khan_decimal) 

# Count Correy
correy_count = candidate.count('Correy')

# Correy Percent 
correy_decimal = (correy_count / num_rows) * 100 
correy_percent = "{:.3f}".format(correy_decimal) 

# Count Li
li_count = candidate.count('Li')

# Li percent 
li_decimal = (li_count / num_rows) * 100 
li_percent = "{:.3f}".format(li_decimal) 

# Count O'Tooley
otooley_count = candidate.count("O'Tooley")

# O'Tooley percent 
otooley_decimal = (otooley_count / num_rows) * 100 
otooley_percent = "{:.3f}".format(otooley_decimal) 

# Label every print 
er = ("Election Results")
dash = ("---------------------------")
tv = (f"Total Votes: {num_rows}")
dash2 = ("---------------------------")
kp = (f"Khan: {khan_percent}% ({khan_count})")
cp = (f"Correy: {correy_percent}% ({correy_count})")
lp = (f"Li: {li_percent}% ({li_count})")
op = (f"O'Tooley: {otooley_percent}% ({otooley_count})")
dash3 = ("---------------------------")
w = ("Winnner: Khan")
dash4 = ("---------------------------")

# Print everything 
print(er)
print(dash)
print(tv)
print(dash2)
print(kp)
print(cp)
print(lp)
print(op)
print(dash3)
print(w)
print(dash4)

# Compile print 
txtwrite = (er,dash,tv,dash2,kp,cp,lp,op,dash3,w,dash4)

# Write to txt file 
output_path = os.path.join("analysis","analysis.txt")
with open(output_path, "w") as tfile:
    for a in txtwrite:
        tfile.write(a)
        tfile.write("\n")
