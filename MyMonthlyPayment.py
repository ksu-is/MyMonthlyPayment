
from selenium import webdriver
driver = webdriver.Chrome(executable_path = r"C:\\Users\\miley\\OneDrive- Kennesaw State University\\" +
    "Spring '20\\App Dev\\ProjectDemos\\Project Topic\\test\\chromedriver_win32")
from selenium.webdriver.common.keys import Keys

chromedriver = r"C:\\Users\\miley\\OneDrive- Kennesaw State University\\" +
   "Spring '20\\App Dev\\ProjectDemos\\Project Topic\\test\\chromedriver_win32"
page = webdriver.Chrome(chromedriver)


# request user login information and automatically enter information 
print("Here we will need the link to the login page on the website you make payments on ")

# User enters the website URL
website_url = input("Enter the url of the login page: ")
driver.get(website_url)

# User enters their username for the website URL provided prior
user_id = input("Username used to login: ")
site_user = driver.find_element_by_id(user_id)
site_user.send_keys(user_id)

# User enters their password 
user_password = input("Password used to login: ")
site_password = driver.find_element_by_id("password")
password = selenium.send_keys(user_password)

# submit login
driver.find_element_by_id("Login").submit()

# login authentication
authentication = "hhtp://" + user_username + user_password + website_url
driver.get(authentication + "/")


