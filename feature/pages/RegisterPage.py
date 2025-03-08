from selenium.webdriver.common.by import By

from feature.pages.BasePage import BasePage

class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
    
    first_name_id="input-firstname"
    last_name_id="input-lastname"
    email_field_id="input-email"
    telephone_field_id="input-telephone"
    pass_field_id="input-password"
    confirm_password_id="input-confirm"
    policy_agree_xpath="//input[@name='agree']"
    yes_check_xpath="//label[normalize-space()='Yes']"
    continue_button_xpath="//input[@value='Continue']"
    missing_email_warning_xpath="//div[@class='text-danger']"
    duplicate_email_xpath="//div[@id='account-register']/div[1]"
    missing_first_name_warning_xpath="//input[@id='input-firstname']/following-sibling::div"
    missing_last_name_warning_xpath="//input[@id='input-lastname']/following-sibling::div"
    missing_email_id_warning_xpath="//input[@id='input-email']/following-sibling::div"
    missing_telephone_xpath="//input[@id='input-telephone']/following-sibling::div"
    missing_password_xpath="//input[@id='input-telephone']/following-sibling::div"


    def enter_first_name(self,first_name):
        self.driver.find_element(By.ID,self.first_name_id).send_keys(first_name)
    
    def enter_last_name(self,last_name):
        self.driver.find_element(By.ID,self.last_name_id).send_keys(last_name)
    
    def enter_email_id(self,email_id):
        self.driver.find_element(By.ID,self.email_field_id).send_keys(email_id)
    
    def enter_telephone(self,telephone):
        self.driver.find_element(By.ID,self.telephone_field_id).send_keys(telephone)
    
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.pass_field_id).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.ID,self.confirm_password_id).send_keys(confirm_password)
    
    def check_policy_agree_checkbox(self):
        self.driver.find_element(By.XPATH,self.policy_agree_xpath).click()
    
    def check_yes_check(self):
        self.driver.find_element(By.XPATH,self.yes_check_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()
    
    def display_warning_for_missing_email(self,expected_warning):
        return self.driver.find_element(By.XPATH,self.missing_email_warning_xpath).text.__eq__(expected_warning)

    def display_warning_for_duplicate_account(self,expected_warning):
        return self.driver.find_element(By.XPATH,self.duplicate_email_xpath).text.__eq__(expected_warning)
    
    def verify_status_for_misisng_all_fields(self,expected_warning):
        first_name_status= self.driver.find_element(By.XPATH,self.missing_first_name_warning_xpath).text.__contains__(expected_warning)
        last_name_status= self.driver.find_element(By.XPATH,self.missing_last_name_warning_xpath).text.__contains__(expected_warning)
        email_id_status= self.driver.find_element(By.XPATH,self.missing_email_id_warning_xpath).text.__contains__(expected_warning)
        telephone_status= self.driver.find_element(By.XPATH,self.missing_telephone_xpath).text.__contains__(expected_warning)
        password_status= self.driver.find_element(By.XPATH,self.missing_password_xpath).text.__contains__(expected_warning)

        if first_name_status and last_name_status and email_id_status and telephone_status and password_status:
            return True
        else:
            False