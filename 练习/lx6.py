from selenium import webdriver
import os
import time

#dir = os.path.dirname(__file__)
#chrome_driver_path = dir +"\chromedriver.exe"
#driver = webdriver.Chrome(chrome_driver_path)
driver = webdriver.Chrome("./chromdriver.exe")
try:
    driver.implicitly_wait(10)
    driver.get("https://www.baidu.com")
    #assert "Baidu" in driver.title
    print("百度首页已打开",driver.title)
    element=driver.find_element_by_id("kw")
    element.send_keys("java")
    element.submit()
    num=driver.find_element_by_class_name("nums")
    print("---------",num.text)
    wait_seconds=10


    driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(num.text.replace("\n","$"),wait_seconds))
    time.sleep(wait_seconds)



finally:
    driver.quit()