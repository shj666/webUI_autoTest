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
    home_page_a_search_loc = (By.LINK_TEXT, '默认版块')  # 默认版块
    time.sleep(1)
    home_page_input_search3_loc = (By.CSS_SELECTOR,'.o input')
    time.sleep(1)
    home_page_a_search1_loc = (By.LINK_TEXT,'删除')
    time.sleep(1)
    home_page_button_search5_loc = (By.NAME,'modsubmit')
    home_page_a_search2_loc = (By.LINK_TEXT, '管理中心')
    time.sleep(1)
    home_page_input_search4_loc = (By.XPATH,'//input[@type="password"]')  # 管理中心用户名
    time.sleep(1)
    home_page_input_search5_loc = (By.NAME, 'submit')  # 管理中心提交
    time.sleep(1)
    home_page_a_search3_loc = (By.ID,'header_forum')#点击论坛
    time.sleep(1)
    home_page_a_search4_loc = (By.LINK_TEXT, '添加新版块')  # 添加新版块
    time.sleep(1)
    home_page_input_search6_loc = (By.NAME, 'editsubmit')  # 提交
    time.sleep(1)
    home_page_a_search5_loc = (By.LINK_TEXT, '退出')  # 管理退出
    time.sleep(1)
    home_page_a_search11_loc = (By.LINK_TEXT, '退出')  # 管理退出
    time.sleep(1)
    home_page_input_search7_loc = (By.ID, 'ls_username')  # 用户名
    time.sleep(1)
    home_page_input_search8_loc = (By.ID, 'ls_password')  # 密码
    time.sleep(1)
    home_page_button_search2_loc = (By.CSS_SELECTOR, '.fastlg_l button')  # 登录
    time.sleep(1)
    home_page_a_search6_loc = (By.LINK_TEXT, '新版块名称')  # 点击新版块
    time.sleep(1)
    home_page_input_search9_loc = (By.NAME, 'subject')  # 帖子标题
    time.sleep(1)
    home_page_textarea_search_loc = (By.NAME, 'message')  # 帖子内容
    time.sleep(1)
    home_page_button_search3_loc = (By.CSS_SELECTOR, '.pnpost button')  # 发帖子
    time.sleep(1)
    home_page_textarea_search2_loc = (By.ID, 'fastpostmessage')  # 回复内容
    time.sleep(1)
    home_page_button_search4_loc = (By.CSS_SELECTOR, '.pnpost button')  # 发送回复
    time.sleep(1)
    home_page_a_search7_loc = (By.PARTIAL_LINK_TEXT, '退出')  # 退出
    time.sleep(1)









    def search(self,username,password):
        self.sendkeys(username,*self.home_page_input_search1_loc)
        self.sendkeys(password, *self.home_page_input_search2_loc)
        self.click(*self.home_page_button_search_loc)
        time.sleep(2)
        self.click(*self.home_page_a_search_loc)
    def delete(self):
        self.click(*self.home_page_input_search3_loc)
        self.click(*self.home_page_a_search1_loc)
        self.click(*self.home_page_button_search5_loc)
    def companycenter(self,password2):
        self.click(*self.home_page_a_search2_loc)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sendkeys(password2, *self.home_page_input_search4_loc)
        #self.sendkeys(username, *self.home_page_input_search1_loc)
        self.click(*self.home_page_input_search5_loc)
        self.click(*self.home_page_a_search3_loc)
    def create(self):
        self.driver.switch_to.frame(0)
        self.click(*self.home_page_a_search4_loc)
        self.click(*self.home_page_input_search6_loc)
    def guanliout(self):
        self.driver.switch_to.parent_frame()
        self.click(*self.home_page_a_search5_loc)
        self.click(*self.home_page_a_search11_loc)
    def yonghulogin(self,username3,password3):
        self.sendkeys(username3, *self.home_page_input_search7_loc)
        self.sendkeys(password3, *self.home_page_input_search8_loc)
        self.click(*self.home_page_button_search2_loc)
    def newfatie(self,head3,content3):
        self.click(*self.home_page_a_search6_loc)
        self.sendkeys(head3, *self.home_page_input_search9_loc)
        self.sendkeys(content3, *self.home_page_textarea_search_loc)
        self.click(*self.home_page_button_search3_loc)
        time.sleep(15)
    def newhuifu(self,huifunew):
        self.sendkeys(huifunew, *self.home_page_textarea_search2_loc)
        self.click(*self.home_page_button_search4_loc)
        self.click(*self.home_page_a_search7_loc)


