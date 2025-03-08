
from selenium.webdriver.common.by import By

from feature.pages.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_id="input-email"
    password_field_id="input-password"
    login_buttin_xpath="//input[@value='Login']"
    warning_message_xpath="//div[@id='account-login']/div[1]"

    def enter_email_address(self,email_address):
        self.driver.find_element(By.ID,self.email_address_field_id).send_keys(email_address)
    
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_field_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_buttin_xpath).click()
    
    def display_status_of_warning_message(self,expected_warning):
        return self.driver.find_element(By.XPATH,self.warning_message_xpath).text.__contains__(expected_warning)
