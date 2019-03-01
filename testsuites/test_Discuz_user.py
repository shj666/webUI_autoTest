from selenium import webdriver
from unittest import TestCase
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_user_homepage import HomePage
from pageobjects.base import BasePage
import unittest
import selenium
import time
from ddt import ddt,data,unpack
@ddt
class DiscuzUser(BaseTestCase):

    @data(['haotest'])
    @unpack
    def test_discuzuser_search(self,expect):

        basepage = BasePage(self.driver)
        basepage.open_url("http://127.0.0.1/forum.php")

        home_page = HomePage(self.driver)

        home_page.search('shj1','123456')#用户登录

        home_page.searchhaotest('haotest')#搜索haotest帖子

        home_page.submit()#验证帖子标题和期望的一致

        home_page.tuichu()#用户退出

        result = home_page.submit()
        self.assertEqual(result, expect, msg=result)


