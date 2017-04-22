import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import keys

class DemoRMLogin(unittest.TestCase):

	def setUp(self):
		self.driver = wevdriver.Chrome("/home/viacheslav/mycode/Selenium/chromedriver")

	def test_login_in_rm (self):
		driver = self.driver
		driver.get("http://www.rozumnemisto.org/")
		self.assertIn("Home")