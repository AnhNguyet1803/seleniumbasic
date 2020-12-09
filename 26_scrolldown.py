# import webdriver
# import time
import time

from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

time.sleep(3)

driver.close()
