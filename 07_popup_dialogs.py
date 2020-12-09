import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)

element = driver.find_element_by_xpath("//button[text()='Click for JS Alert']")
element.click()

# alert = driver.switch_to_alert()
alert = driver.switch_to.alert
alert.accept()

time.sleep(3)
element = driver.find_element_by_xpath("//button[text()='Click for JS Confirm']")
element.click()

# alert = driver.switch_to_alert()
alert = driver.switch_to.alert
alert.dismiss()

time.sleep(3)
element = driver.find_element_by_xpath("//button[text()='Click for JS Prompt']")
element.click()

# alert = driver.switch_to_alert()
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(3)

driver.close()
