import os
from selenium import webdriver
dir = os.path.dirname(__file__)
ie_driver_path = dir + "\IEDriverServer.exe"
driver = webdriver.Ie(ie_driver_path)
driver.get("http://www.python.org")
assert "Python" in driver.title