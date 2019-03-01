from selenium import webdriver
from unittest import TestCase
from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_toupiao_homepage import HomePage
from pageobjects.base import BasePage
import unittest
import selenium
import time
class DiscuzToupiao(BaseTestCase):
    def test_discuztoupiao_search(self):

        basepage = BasePage(self.driver)
        basepage.open_url("http://127.0.0.1/forum.php")

        home_page = HomePage(self.driver)

        home_page.search('admin','shj1996')#登录

        home_page.toupiao('11111111111111111','5555555555555555','6666666666666666','7777777777777')

        home_page.huoqu()