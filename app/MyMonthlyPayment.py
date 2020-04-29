import selenium
from selenium import webdriver
driver = webdriver.Chrome(executable_path = r"C:\\Users\\miley\\OneDrive- Kennesaw State University\\" +
    "Spring '20\\App Dev\\ProjectDemos\\Project Topic\\test\\chromedriver_win32\\chromedriver.exe")
from selenium.webdriver.common.keys import Keys

chromedriver = r"C:\\Users\\miley\\OneDrive- Kennesaw State University\\",
"Spring '20\\App Dev\\ProjectDemos\\Project Topic\\test\\chromedriver_win32\\chromedriver.exe"



# request user login information and automatically enter information 
print("Here we will need the link to the login page on the website you make payments on ")

# User enters the website URL
website_url = input("Enter the url of the login page: ")
driver.get(website_url)

# User enters their username for the website URL provided prior
user_id = input("Username used to login: ")
username = driver.find_element_by_xpath("//form[@id = user_id]/input[1]")
username.send_keys(user_id)

# User enters their password 
password = input("Password used to login: ")
site_password = driver.find_element_by_xpath("//form[@name = password]/input[1]")
site_password.send_keys(site_password)

# submit login
login = driver.find_element_by_xpath('continue').submit()

# login authentication
authentication = "hhtp://" + user_id + password + website_url
driver.get(authentication + "/")


# Wait
driver.implicitly_wait(10) #seconds

# List of bill payments due
bills_due = []

#adding amounts due to list and totaling payments together
amount_search = driver.find_element_by_xpath('amountDue')

bills_due.append(amount_search)
total_due = sum(bills_due)


print("$", total_due)






