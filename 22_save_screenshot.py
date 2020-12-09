from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()
