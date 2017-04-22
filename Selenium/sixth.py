import time
from selenium.chrome.webdriver import WebDriver


driver = WebDriver("/home/viacheslav/mycode/Selenium/chromedriver")
driver.get('http://www.rozumnemisto.org/')
driver.implicitly_wait(3)
driver.maximize_window()

login_registration_field = driver.find_element_by_partial_link_text("Вхід/Реєстрація")
login_registration_field.click()
driver.implicitly_wait(3)

registration_field = driver.find_element_by_partial_link_text("/accounts/signup/")
registration_field.click()
driver.implicitly_wait(3)

time.sleep(3)
driver.close()