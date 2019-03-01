from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1/forum.php")
name=driver.find_element_by_name("username")
name.send_keys("admin")
password=driver.find_element_by_name("password")
password.send_keys("shj1996")
denglu=driver.find_element_by_css_selector(".fastlg_l button")
denglu.click()
time.sleep(1)
moren = driver.find_element_by_css_selector(".fl_tb a")
moren.click()
xuan=driver.find_element_by_css_selector(".o input")
xuan.click()
time.sleep(1)
delete=driver.find_element_by_link_text("删除")
delete.click()
time.sleep(1)
xuan = driver.find_element_by_css_selector(".o button")
xuan.click()
time.sleep(1)
guanli=driver.find_element_by_link_text("管理中心")
guanli.click()
time.sleep(1)
mima=driver.find_element_by_xpath("//input[@name='admin_password']")
mima.send_keys("shj1996")
driver.switch_to.window(driver.current_window_handle)
tijiao=driver.find_element_by_xpath("//input[@value='提交']")
tijiao.click()
time.sleep(1)
luntang=driver.find_element_by_partial_link_text("论坛")
luntang.click()
chuqu=driver.find_element_by_css_selector(".uinfo a")
chuqu.click()





