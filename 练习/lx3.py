import os
from selenium import webdriver

dir = os.path.dirname(__file__)
firefox_driver_path = dir + "\geckodriver.exe"
driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.get("http://www.python.org")
assert "Python" in driver.title