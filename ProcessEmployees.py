'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv


# open the file
employee_file = open('employee_data.csv', 'r')
csvfile = csv.reader(employee_file, delimiter=',')

next(csvfile)


# create an empty dictionary
employee_dict = {}

# use a loop to iterate through the csv file
for record in csvfile:
    name = record[1] + ' ' + record[2]
    department = record[3]
    title = record[4]
    salary = record[5]

    new_salary = float(salary) * 1.1

    # check if the employee fits the search criteria
    if department == "Marketing" and title == "Manager":
        employee_dict = {"Manager Name": name, "Current Salary": new_salary}
        print(employee_dict)


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout
for k, v in employee_dict:
    print(f"Manager Name: {k} Current Salary: {v}")
