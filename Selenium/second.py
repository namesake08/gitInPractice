import time
from selenium import webdriver

driver = webdriver.Chrome("/home/viacheslav/mycode/Selenium/chromedriver")
driver.get("http://www.rozumnemisto.org/index/projects_about")
print(driver.title)
time.sleep(5)

try:
	driver.find_element_by_id('connect')
	print('Test Pass: ID found')

except Exception as e:
	print("Exception found", format(e))

driver.close()