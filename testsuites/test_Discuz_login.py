from selenium import webdriver
from unittest import TestCase
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_homepage import HomePage
from pageobjects.base import BasePage
import unittest
import selenium
import time
class DiscuzLogin(BaseTestCase):
    def test_Discuzlogin_search(self):

        basepage = BasePage(self.driver)
        basepage.open_url("http://127.0.0.1/forum.php")

        home_page = HomePage(self.driver)

        home_page.search('admin','shj1996')#登录

        home_page.shuru('我的第一个帖子！！！！','好海奥，感觉人生已经到达了巅峰！！！！')#写并发帖子
        home_page.huifu("老哥，稳啊！墙都不服就服你！！！！！")#回复帖子
        home_page.tuichu()#退出
if __name__ =='__maim__':
     unittest.main()


