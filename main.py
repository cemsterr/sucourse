__author__ = 'cemsaglam'

from selenium import webdriver

browser = webdriver.PhantomJS() # phantomJS is used as a headless browser
link = "https://login.sabanciuniv.edu/cas/login?service=https%3A%2F%2Fsucourse.sabanciuniv.edu%2Fsakai-login-tool%2Fcontainer"
# link to connect

try:
    browser.get(link) # open up the authentication page

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

    # For debugging:
    # prints current link and page title
    print browser.current_url
    print browser.title

    navbar = browser.find_element_by_css_selector("#topnav") # get the top navigation bar
    courses = navbar.find_elements_by_tag_name("li") # all the class names are now in the list "courses"

    coursenames = list()
    for c in courses:
        print c.text
        coursenames.append(c.text)
    # a list of strings now contains the course names, for ease of usage

    print "***"

    baselink = "https://sucourse.sabanciuniv.edu/portal/site/" # course names will be attacked from here
    for i in range(1, len(coursenames)):

        print "What's new in {}?".format(coursenames[i])
        courselink = baselink + coursenames[i]  # prepares the link to connect to
        browser.get(courselink)                 # connect to the courselink
        # print browser.current_url

        tab = browser.find_elements_by_css_selector(".toolMenuLink ") # get the tabs section

        for t in tab: # for each course, check each tab and print if there's an unread section
            span = t.find_element_by_tag_name("span")
            tabname = span.text
            # color red means there's an unread notification
            if span.get_attribute("style") == u'color: red;' or span.get_attribute("style") == u'color: red; ':
                print("\tNew: {}".format(tabname))

        print("\n")
        browser.back() # go back to the previous page

    # closes the browser
    browser.close()
    print("That's all folks")
except:
    print("Something went wrong. Check internet connection.")
