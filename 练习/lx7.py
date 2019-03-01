from selenium import webdriver
import time

driver = webdriver.Chrome(".\chromedriver.exe")
try:
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    #assert "百度一下" in driver.title
    clink= driver.find_elements_by_tag_name("a")
    #print("-----",clink.text)
    for i in clink:
        print(i.text)

finally:
    driver.quit()


