import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.get("https://www.reddit.com")
driver.execute_script("window.open()")

# driver.close() # close windows
# TH có 1 tab close tab close window


print(driver.window_handles)
# driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[1])

# driver.execute_script("window.open(https://www.youtube.com)")
driver.get("https://www.youtube.com")
time.sleep(1)
# driver.switch_to_window(driver.window_handles[0])
driver.switch_to.window(driver.window_handles[0])

driver.get("https://python.org")

time.sleep(3)
driver.close()
driver.quit()
# quit all tab
