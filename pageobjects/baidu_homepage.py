from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
class HomePage(BasePage):
    home_page_input_search_loc = (By.ID,'kw')
    home_page_button_search_loc = (By.ID, 'su')


    def search(self,content):
        self.sendkeys(content,*self.home_page_input_search_loc)
        self.click(*self.home_page_button_search_loc)
