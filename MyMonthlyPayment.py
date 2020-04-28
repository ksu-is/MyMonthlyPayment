
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys

chromedriver = 'D:\\chromedriver.exe'
page = webdriver.Chrome(chromedriver)
# request user login information and automatically enter information 
print("Here we will need the link to the login page on the website you make payments on ")
website_url = input("Enter the url of the login page: ")
driver.get(website_url)
user_id = input("Username used to login: ")
site_username = driver.find_element_by_id(user_id)
site_username.send_keys(user_username)
user_password = input("Password used to login: ")
site_password = driver.find_element_by_id("password")
password = selenium.send_keys(user_password)
driver.find_element_by_id("Login").submit()
authentication = "hhtp://" + user_username + user_password + website_url
driver.get(authentication + "/")


from bs4 import BeautifulSoup
import requests
import csv
# (url needed)
soup = BeautifulSoup(source, 'lxml')
payment = soup.find_all('due')
total_payments = int("payment") + 


total_due = print("$", str(total_payments))
















#>>try later<<
#import forms from django
#class URLInput:
#    input_type: 'url'
#    template_name: 'django/forms/widgets/url.html'
