from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


dir = os.path.dirname(__file__)#获取当前文件夹#
chrome_driver_path = dir + "\chromedriver.exe"#驱动路径#
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.yahoo.com")
assert "Yahoo" in driver.title

element = driver.find_element_by_name('p')
element.send_keys("seleniumhp" + Keys.RETURN)
driver.quit()