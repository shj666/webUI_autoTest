from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    home_page_input_search1_loc = (By.ID,'ls_username')#用户名
    time.sleep(1)
    home_page_input_search2_loc = (By.ID,'ls_password')#密码
    time.sleep(1)
    home_page_button_search1_loc = (By.CSS_SELECTOR,'.fastlg_l button')#登录
    time.sleep(1)
    home_page_a_search1_loc = (By.LINK_TEXT, '默认版块')  # 默认版块
    time.sleep(1)
    home_page_a_search2_loc = (By.ID,'newspecial')#点发帖
    time.sleep(1)
    home_page_a_search3_loc = (By.LINK_TEXT, '发起投票')  # 点发起投票
    time.sleep(1)
    home_page_input_search3_loc = (By.NAME, 'subject')  # 投票标题
    time.sleep(1)
    home_page_input_search4_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(1) input')  # 投票选项
    time.sleep(1)
    home_page_input_search5_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(2) input')  # 投票选项
    time.sleep(1)
    home_page_input_search6_loc = (By.CSS_SELECTOR, '.mbm p:nth-child(3) input')  # 投票选项
    time.sleep(1)
    home_page_button_search2_loc = (By.NAME, 'topicsubmit')  # 发起投票
    time.sleep(1)
    home_page_input_search7_loc = (By.ID, 'option_1')  # 选择投票
    time.sleep(1)
    home_page_button_search3_loc = (By.NAME, 'pollsubmit')  # 提交
    time.sleep(1)
    home_page_label_search1_loc = (By.XPATH,'//form[@id="poll"]/div[2]/table/tbody/tr[1]')#1
    time.sleep(1)
    home_page_label_search2_loc = (By.XPATH, '//form[@id="poll"]/div[2]/table/tbody/tr[2]/td[2]')
    time.sleep(1)
    home_page_label_search3_loc = (By.XPATH, '//form[@id="poll"]/div[2]/table/tbody/tr[3]/td[1]/label')#2
    time.sleep(1)
    home_page_label_search4_loc = (By.XPATH, '//form[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')
    time.sleep(1)
    home_page_label_search5_loc = (By.XPATH, '//form[@id="poll"]/div[2]/table/tbody/tr[5]/td[1]/label')#3
    time.sleep(1)
    home_page_label_search6_loc = (By.XPATH, '//form[@id="poll"]/div[2]/table/tbody/tr[6]/td[2]')
    time.sleep(1)
    home_page_span_search_loc = (By.ID,'thread_subject')
    time.sleep(1)







    def search(self,username,password):
        self.sendkeys(username,*self.home_page_input_search1_loc)
        self.sendkeys(password, *self.home_page_input_search2_loc)
        self.click(*self.home_page_button_search1_loc)
        self.click(*self.home_page_a_search1_loc)
    def toupiao(self,head,select1,select2,select3):
        self.click(*self.home_page_a_search2_loc)
        self.click(*self.home_page_a_search3_loc)
        self.sendkeys(head, *self.home_page_input_search3_loc)
        self.sendkeys(select1, *self.home_page_input_search4_loc)
        self.sendkeys(select2, *self.home_page_input_search5_loc)
        self.sendkeys(select3, *self.home_page_input_search6_loc)
        self.click(*self.home_page_button_search2_loc)
        self.click(*self.home_page_input_search7_loc)
        self.click(*self.home_page_button_search3_loc)

    def huoqu(self):
         self.text(*self.home_page_label_search1_loc)
         self.text(*self.home_page_label_search2_loc)
         self.text(*self.home_page_label_search3_loc)
         self.text(*self.home_page_label_search4_loc)
         self.text(*self.home_page_label_search5_loc)
         self.text(*self.home_page_label_search6_loc)
         self.text(*self.home_page_span_search_loc)