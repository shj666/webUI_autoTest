from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(7)
    driver.get("https://mail.163.com/")
    driver.switch_to.frame(0)
    mail=driver.find_element_by_name("email")
    mail.send_keys("5455565")
    password=driver.find_element_by_name("password")
    password.send_keys("1856165")
    denglu=driver.find_element_by_id("dologin")
    denglu.click()
finally:
    quit()