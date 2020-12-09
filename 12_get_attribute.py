# import webdriver
import time

from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.maximize_window()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# get href attribute
print(element.get_attribute('href'))

time.sleep(3)
driver.close()
