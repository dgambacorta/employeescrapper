import sys
import re


filename = input("Please enter File name: ")
print("You entered: " + filename)

domain = input("Please enter Company domain: eg magento.com: ")
print("You entered: " + domain)

typeofemail = input("Type of email: 1- name@domain 2-name.surname@domain 3-firstlettersurname@domain: ")
print("You entered: " + typeofemail)

googleCalendar = input("Google Calendar: yes/no ")
print("You entered: " + googleCalendar)

file = open(filename, 'r') 
lines = file.readlines() 
output_name = domain.replace('.','')+"_emails.txt"
output = open(output_name, "w")

if googleCalendar == 'yes' or googleCalendar == 'y':
        output_name_gcalendar = domain.replace('.','')+"gc.txt"
        output_gcalendar = open(output_name_gcalendar, "w")

for employee in lines:
    fulldomain="@"+domain
    if(re.split("[^a-zA-Z]*", employee)[0]):
        employeeFirstName=re.split("[^a-zA-Z]*", employee)[0].lower()
        employeeLastname=re.split("[^a-zA-Z]*", employee)[1].lower()

    if typeofemail == '1':
        email = employeeFirstName+fulldomain

    if typeofemail == '2':
        email = employeeFirstName+'.'+employeeLastname+fulldomain

    if typeofemail == '3':
        email = employeeFirstName[0]+employeeLastname+fulldomain

    print(email, file=output) 

    if googleCalendar == 'yes' or googleCalendar == 'y':
        gcalendaremail = "https://calendar.google.com/calendar/u/3/r?cid="+email.lower()
        print(gcalendaremail, file=output_gcalendar)





