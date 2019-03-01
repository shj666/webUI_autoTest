from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    home_page_input_search1_loc = (By.ID, 'ls_username')  # 用户名
    time.sleep(1)
    home_page_input_search2_loc = (By.ID, 'ls_password')  # 密码
    time.sleep(1)
    home_page_button_search1_loc = (By.CSS_SELECTOR, '.fastlg_l button')  # 登录
    time.sleep(1)
    home_page_button_search2_loc = (By.XPATH, '//button[@id="scbar_btn"]')  # 点击搜索按钮
    time.sleep(1)
    home_page_input_search3_loc = (By.XPATH, '//input[@name="srchtxt"]')  # 找到搜索框
    time.sleep(1)
    home_page_button_search3_loc = (By.XPATH, '//button[@id="scform_submit"]')  # 点击搜索
    time.sleep(1)
    home_page_a_search1_loc = (By.CSS_SELECTOR, '.xs3 strong font')  # 点击帖子
    time.sleep(1)
    home_page_span_search1_loc = (By.CSS_SELECTOR, '.ts span')  # 点击
    time.sleep(1)
    home_page_a_search2_loc = (By.LINK_TEXT, '退出')  # 点击帖子
    time.sleep(1)




    def search(self, username, password):
        self.sendkeys(username, *self.home_page_input_search1_loc)
        self.sendkeys(password, *self.home_page_input_search2_loc)
        self.click(*self.home_page_button_search1_loc)

    def searchhaotest(self,sousuo):
        self.sendkeys(sousuo, *self.home_page_input_search3_loc)
        time.sleep(1)
        self.click(*self.home_page_button_search2_loc)
    def submit(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.home_page_a_search1_loc)
        m = self.driver.find_element_by_css_selector('.xs3 strong font')
        return m.text

    def tuichu(self):
        self.click(*self.home_page_a_search2_loc)

