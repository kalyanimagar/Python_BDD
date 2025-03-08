from selenium.webdriver.common.by import By

from feature.pages.BasePage import BasePage

class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
    
    valid_product_link_text="HP LP3065"
    no_product_message_xpath="//input[@id='button-search']//following-sibling::p"

    def verify_valid_product_is_displayed(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_product_link_text).is_displayed()
    
    def verify_proper_message_id_dispayed(self,expecetd_text):
        return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text.__eq__(expecetd_text)

    
