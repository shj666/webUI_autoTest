from selenium import webdriver
import time

driver = webdriver.Chrome(".\chromedriver.exe")

driver.implicitly_wait(10)
driver.get("https://home.baidu.com")
#assert "百度一下" in driver.title
lxpage=driver.find_element_by_link_text("联系我们")
lxpage.click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
email=driver.find_elements_by_class_name("mail-content-text")
for i in email:
    str=i.text
    if "@" in str:
     print(str)

driver.quit()