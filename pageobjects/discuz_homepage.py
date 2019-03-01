from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    home_page_input_search1_loc = (By.ID,'ls_username')#用户名
    time.sleep(1)
    home_page_input_search2_loc = (By.ID,'ls_password')#密码
    time.sleep(1)
    home_page_button_search_loc = (By.CSS_SELECTOR,'.fastlg_l button')#登录
    time.sleep(1)
    home_page_a_search_loc = (By.CSS_SELECTOR,'.bm_c h2 a')#默认版块
    time.sleep(1)
    home_page_input_search3_loc = (By.NAME, 'subject')#帖子标题
    time.sleep(1)
    home_page_textarea_search4_loc = (By.NAME, 'message')#帖子内容
    time.sleep(1)
    home_page_button_search5_loc = (By.CSS_SELECTOR, '.pnpost button')#发帖子
    time.sleep(1)
    home_page_textarea_search6_loc = (By.ID,'fastpostmessage')#回复内容
    time.sleep(1)
    home_page_button_search7_loc = (By.CSS_SELECTOR, '.pnpost button')#发送回复
    time.sleep(1)
    home_page_a_search8_loc = (By.PARTIAL_LINK_TEXT,'退出')  # 退出
    time.sleep(1)




    def search(self,username,password):
        self.sendkeys(username,*self.home_page_input_search1_loc)
        self.sendkeys(password, *self.home_page_input_search2_loc)
        self.click(*self.home_page_button_search_loc)
        self.click(*self.home_page_a_search_loc)
    def shuru(self,head,content):
        self.sendkeys(head, *self.home_page_input_search3_loc)
        self.sendkeys(content, *self.home_page_textarea_search4_loc)
        self.click(*self.home_page_button_search5_loc)
    def huifu(self,huifucontent):
        self.sendkeys(huifucontent, *self.home_page_textarea_search6_loc)
        self.click(*self.home_page_button_search7_loc)
    def tuichu(self):
        self.click(*self.home_page_a_search8_loc)
