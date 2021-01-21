# Define everything
emp_id = []
name = [] 
first_name = []
last_name = []
dob = []
ssn = []
states = []


# Import file
import os
import csv 
import datetime

states_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

csvpath = os.path.join("Resources", "pyboss.csv")
# CSV Reader Delimiter
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)


    for row in csvreader:
        csv_header = ("Emp ID","First Name","Last Name","DOB","SSN","State")
        
        # Employee ID 
        emp_id.append(row[0])


        # Split First Name 
        name_split = row[1].split(" ")
        first_name_str = (name_split[0])
        first_name.append(first_name_str)

        # Split Last Name 
        last_name_str = (name_split[1])
        last_name.append(last_name_str)
        
        # Convert date 
        dobdate = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m-%d-%Y')
        dob.append(dobdate)

    
        # Social Security Number 
        ssn_split = row[3].split("-")
        star = ("***-**-")
        ssnlast4 = ssn_split[2]
        ssnfinal = (star)+(ssnlast4)
        ssn.append(ssnfinal)
    
        # US States
        sta = states_dict[row[4]]
        states = states + [sta]


# Zip Final Print Out 
finalprintout = zip(emp_id,first_name,last_name,dob,ssn,states)

# Write to CSV File 
output_path = os.path.join("analysis","pyboss.csv")
with open(output_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(finalprintout)

