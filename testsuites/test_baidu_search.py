from selenium import webdriver
from unittest import TestCase
from testsuites.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage
from pageobjects.base import BasePage
import unittest
import selenium
class BaiduSearch(BaseTestCase):
    def test_baidu_search(self):

        basepage = BasePage(self.driver)
        basepage.open_url("https://www.baidu.com")


        home_page = HomePage(self.driver)
        home_page.search('selenium')
if __name__ =='__maim__':
     unittest.main()


