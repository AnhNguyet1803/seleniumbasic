# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')

driver.get("http://www.python.org")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)

cookie = {'name': 'foo', 'value': 'abc'}
driver.add_cookie(cookie)
# driver.delete_cookie()
# driver.delete_all_cookies()

# # And now output all the available cookies for the current URL
# driver.get_cookie()
# driver.get_cookies()

# driver.close()
