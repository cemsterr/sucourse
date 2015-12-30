__author__ = 'cemsaglam'

from selenium import webdriver

browser = webdriver.PhantomJS()
link = "https://login.sabanciuniv.edu/cas/login?service=https%3A%2F%2Fsucourse.sabanciuniv.edu%2Fsakai-login-tool%2Fcontainer"
# link to connect

browser.get(link)

username = "" # user fills input fields
password = ""

# parameters are sent over using Selenium and PhantomJS
userfield = browser.find_element_by_name("username")
userfield.send_keys(username)
passfield = browser.find_element_by_name("password")
passfield.send_keys(password)
# fills in name and password credentials

submitbutton = browser.find_element_by_name("submit")
submitbutton.click()

# prints current link and page title
print browser.current_url
print browser.title

# closes the browser
browser.close()


# To ignore:
'''
Test:
driver = webdriver.PhantomJS()
driver.get("http://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id('search_button_homepage').click()
print driver.current_url
driver.quit
'''
