from selenium.webdriver.common.by import By

from feature.pages import searchPage
from feature.pages.BasePage import BasePage

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
    
    my_account_link_text="My Account"
    login_btn_link_text="Login"
    serach_box_name="search"
    serach_button_xpath="//div[@id='search']//button"
    register_button_link_text="Register"
    
    def click_on_my_account(self):
        self.driver.find_element(By.LINK_TEXT,self.my_account_link_text).click()

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_btn_link_text).click()

    def enter_product_in_serach_box(self,product_name):
        self.driver.find_element(By.NAME,self.serach_box_name).send_keys(product_name)
    
    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.serach_button_xpath).click()
        
    
    def click_on_register_button(self):
        self.driver.find_element(By.LINK_TEXT,self.register_button_link_text).click()
