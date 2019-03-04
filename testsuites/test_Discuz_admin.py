from selenium import webdriver
from unittest import TestCase
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_admin_homepage import HomePage
from pageobjects.base import BasePage
import unittest
import selenium
import time
class DiscuzAdmin(BaseTestCase):
    def test_discuzadmin_search(self):

        basepage = BasePage(self.driver)
        basepage.open_url("http://127.0.0.1/forum.php")

        home_page = HomePage(self.driver)

        home_page.search('admin','shj1996')#登录
        self.assertEqual(self.driver.title, "【新提醒】 默认版块 - Discuz! Board - Powered by Discuz!")

        home_page.delete()#进入默认板块，删除帖子


        home_page.companycenter('shj1996')#进入版块管理(管理中心--论坛)
        self.assertEqual(self.driver.title, "Discuz! Board 管理中心 - 论坛 - 版块管理")

        home_page.create()#创建新的版块

        home_page.guanliout()#管理员退出
        self.assertEqual(self.driver.title, "论坛 - Powered by Discuz!")

        home_page.yonghulogin('shj1','123456')#普通用户登录
        self.assertEqual(self.driver.title, "【新提醒】 论坛 - Discuz! Board - Powered by Discuz!")

        home_page.newfatie('我的第二个帖.','符合符合华为覅黑发黑丝的开发商地多喝点客服端')#在新的版块下发帖
        self.assertEqual(self.driver.title, "【新提醒】 我的第二个帖.- 新版块名称 - Discuz! Board - Powered by Discuz!")
        home_page.newhuifu('大老牛逼，秒天秒地秒空气')#回复帖子





if __name__ =='__maim__':
     unittest.main()


