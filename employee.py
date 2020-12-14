from linkedin_scraper import Person, actions, Company
import time
from selenium import webdriver
from urllib.parse import urlparse
import sys
import re



email = 'xxxxx';  
password = 'xxxxx';


target = 'targets.txt'

file1 = open(target, 'r') 
Lines = file1.readlines() 

for url in Lines:
    browser = webdriver.Chrome()
    browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    email_element = browser.find_element_by_id("username")
    email_element.send_keys(email)
    pass_element = browser.find_element_by_id("password")
    pass_element.send_keys(password)
    pass_element.submit()
    time.sleep(3)
    output_name = urlparse(url).path.split('/')[2]
    output = open(output_name, "w")   
    

    browser.get(url)
    #browser.maximize_window()
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)
    list_css = "org-people-profiles-module__profile-list"
    results_list = browser.find_element_by_class_name(list_css)
    results_li = results_list.find_elements_by_tag_name("li")
    for res in results_li:
        test = browser.find_element_by_css_selector(".org-people-profile-card__profile-title.t-black.lt-line-clamp.lt-line-clamp--single-line.ember-view")
        name = (res.text.split("\n") or [""])[0].strip()
        print (name)
        if name != 'Miembro de LinkedIn' and name != '':
            print(name, file=output) 
    browser.quit()

    output.close()



filename = output_name

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