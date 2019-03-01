from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngin
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        #broswer = BrowserEngin()
        #self.driver =broswer.open_browser()
        self.driver = webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()