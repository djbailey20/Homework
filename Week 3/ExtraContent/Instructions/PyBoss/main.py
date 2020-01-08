import os
import csv
import datetime
csvpath = os.path.join("employee_data.csv")
newDict = {}
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
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
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
# csvpath = "C:\Users\shado\Documents\LearnPython\Day3\Stu_CerealCleaner\Resources\cereal.csv"
with open(csvpath, newline='') as csvfile, open('output.csv', 'w', newline="") as csvout:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    filewriter = csv.writer(csvout, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(
        ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    for row in csvreader:
        name = row[1].split()
        ssn = row[3].split('-')
        date = datetime.datetime.strptime(
            str(row[2]), '%Y-%m-%d').strftime('%m/%d/%Y')
        filewriter.writerow([str(row[0]), name[0], name[1],
                             str(date), f"***-**-{ssn[2]}", states[row[4]]])
