from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")
time.sleep(1)
driver.execute_script("window.alert('8589181d9gergddv')")
time.sleep(2)
driver.switch_to.alert.accept()