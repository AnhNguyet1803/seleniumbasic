# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_id("gsc-i-id1")

# get rect
print(element.rect)

driver.close()
