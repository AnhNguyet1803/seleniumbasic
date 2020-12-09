import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(3)

driver.switch_to.frame("mce_0_ifr")
driver.switch_to.default_content()

# driver.switch_to_frame("mce_0_ifr")
# driver.switch_to_default_content()

driver.close()
