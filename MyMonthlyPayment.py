
#requesting users login information 
print("Here we will need the link to the login page on the website you make payments on ")
url = input("Enter the url of the login page: ")
username = input("Username used to login: ")
password = input("Password used to login: ")
# >>add submit<< 

#using user input, website is requested
import requests
from bs4 import BeautifulSoup
page = requests.get(url)

#>>try later<<
#import forms from django
#class URLInput:
#    input_type: 'url'
#    template_name: 'django/forms/widgets/url.html'
