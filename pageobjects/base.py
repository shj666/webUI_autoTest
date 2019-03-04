from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os.path
logger = Logger(logger='BasePage').getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        logger.info("后退")
    def forward(self):
        self.driver.forward()
        logger.info("前进")
    def open_url(self,url):
        self.driver.get(url)
    def quit_browser(self):
        self.driver.quit()
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭网页")
        except Exception as e:
            pass
            logger.error("关闭网页失败%s"%e)
            self.get_windows_img()
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到元素%s"%loc)
        except:

            logger.info("%s页面元素未找到%s元素"%(self,loc))
            self.get_windows_img()
    def sendkeys(self,text,*loc):
        el = self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容"+text)
        except Exception as e:
            logger.error("关闭网页失败%s" % e)
            self.get_windows_img()
    def clear(self,*loc):
        el = self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除成功")
        except Exception as e:
            logger.error("清除失败%s" % e)
            self.get_windows_img()
    def text(self,*loc):
        el = self.find_element(*loc)
        try:
            print(el.text)
            logger.info("获取成功")
        except Exception as e:
            logger.error("获取失败%s"% e)
            self.get_windows_img()

    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("点击成功")
        except Exception as e:
            logger.error("点击失败%s" % e)
            self.get_windows_img()

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath(".")) + '/screenshorts/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("get_windows_img")
        except:
            self.get_windows_img()
            logger.error("not get_windows_img")

    def write_assert(self,*loc):
        el = self.find_element(*loc)
        try:
            el.text
            logger.info("增加断言成功")
        except Exception as e:
            logger.error("增加断言失败%s" % e)
            self.get_windows_img()






