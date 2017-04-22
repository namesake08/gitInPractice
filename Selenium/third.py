import time
from selenium import webdriver

driver = webdriver.Chrome("/home/viacheslav/mycode/Selenium/chromedriver")
driver.implicitly_wait(3)
driver.maximize_window()
# navigate to the application home page
driver.get('http://www.rozumnemisto.org/')

# get the search textbox
search_field = driver.find_element_by_id("project")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Ку")
#search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
city = driver.find_elements_by_id("ui-id-1")
city.submit()

# get the number of elements found
print ("Found " + str(len(lists)) + "searches:")
 
# iterate through each element and print the text that is
# name of the search
i=0
for listitem in lists:
   print (listitem)
   i=i+1
   if(i>10):
      break



ids = driver.find_elements_by_xpath('//*[@id]')
for i in ids:
	print(i.get_attribute('id'))

time.sleep(3)
driver.close()