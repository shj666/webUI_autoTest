from selenium import webdriver
import os

dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://www.python.org")
assert "Python" in driver.title