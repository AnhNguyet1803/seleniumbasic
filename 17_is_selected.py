# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.practice.geeksforgeeks.org/")

# get element
element = driver.find_element_by_link_text("Courses")

# print value
print(element.is_selected())

driver.close()
