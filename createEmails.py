import sys
import re


filename = input("Please enter File name: ")
print("You entered: " + filename)

domain = input("Please enter Company domain: eg magento.com: ")
print("You entered: " + domain)

typeofemail = input("Type of email: 1- name@domain 2-name.surname@domain 3-firstlettersurname@domain: ")
print("You entered: " + typeofemail)


file = open(filename, 'r') 
lines = file.readlines() 
output_name = domain.replace('.','')+"_emails.txt"
output = open(output_name, "w")

for employee in lines:
    fulldomain="@"+domain
    employeeFirstName=re.split("[^a-zA-Z]*", employee)[0]
    employeeLastname=re.split("[^a-zA-Z]*", employee)[1]

    if typeofemail == '1':
        email = employeeFirstName+fulldomain

    if typeofemail == '2':
        email = employeeFirstName+'.'+employeeLastname+fulldomain

    if typeofemail == '3':
        email = employeeFirstName[0]+employeeLastname+fulldomain

    print(email, file=output) 

