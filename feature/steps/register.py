import datetime
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from feature.pages.AccountSuccessPage import AccountSuccessPage
from feature.pages.HomePage import HomePage
from feature.pages.RegisterPage import RegisterPage


@given('Naviagte to Register page')
def step_impl(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.HomePage=HomePage(context.driver)
    context.HomePage.click_on_my_account()
    context.HomePage.click_on_register_button()

@when('Enter below details in all mandatory fields')
def step_impl(context):
    for data in context.table:
        context.RegisterPage=RegisterPage(context.driver)
        context.RegisterPage.enter_first_name(data["first_name"])
        context.RegisterPage.enter_last_name(data["last_name"])
        # timestamp=datetime.date().strftime("%Y_%m_%d_%H_%M_%S")
        email_id="kal626ya@gmail.com"
        context.RegisterPage.enter_email_id(email_id)
        context.RegisterPage.enter_telephone(data["telephone"])
        context.RegisterPage.enter_password(data["password"])
        context.RegisterPage.enter_confirm_password(data["confirm_password"])
        context.RegisterPage.check_policy_agree_checkbox()

@when('Enter details in all fields')
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    context.RegisterPage.enter_first_name("kalyani")
    context.RegisterPage.enter_last_name("Magar")
    # timestamp=datetime.date().strftime("%Y_%m_%d_%H_%M_%S")
    email_id="kal626ytya@gmail.com"
    context.RegisterPage.enter_email_id(email_id)
    context.RegisterPage.enter_telephone("395934875")
    context.RegisterPage.enter_password("12345")
    context.RegisterPage.enter_confirm_password("12345")
    context.RegisterPage.check_yes_check()
    context.RegisterPage.check_policy_agree_checkbox()
    
@when('Click on Continue button')
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    context.RegisterPage.click_on_continue_button()

@then('Account should get registered')
def step_impl(context):
    expected_text='Your Account Has Been Created!'
    context.AccountSuccessPage=AccountSuccessPage(context.driver)
    assert context.AccountSuccessPage.display_status_of_account_created(expected_text)

@when('Enter details in all fields and enter dupliacte email address in email field')
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    context.RegisterPage.enter_first_name("kalyani")
    context.RegisterPage.enter_last_name("Magar")
    # timestamp=datetime.date().strftime("%Y_%m_%d_%H_%M_%S")
    email_id="kal@gmail.com"
    context.RegisterPage.enter_email_id(email_id)
    context.RegisterPage.enter_telephone("395934875")
    context.RegisterPage.enter_password("12345")
    context.RegisterPage.enter_confirm_password("12345")
    context.RegisterPage.check_yes_check()
    context.RegisterPage.check_policy_agree_checkbox()
    

@when("Enter details in all fields and dont enter email address in email field")
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    context.RegisterPage.enter_first_name("kalyani")
    context.RegisterPage.enter_last_name("Magar")
    # timestamp=datetime.date().strftime("%Y_%m_%d_%H_%M_%S")
    email_id="kal66a@gmail.com"
    context.RegisterPage.enter_email_id("")
    context.RegisterPage.enter_telephone("39594875")
    context.RegisterPage.enter_password("12345")
    context.RegisterPage.enter_confirm_password("12345")
    context.RegisterPage.check_yes_check()
    context.RegisterPage.check_policy_agree_checkbox()

@then('proper warning message informing about missing emailshould get dispalyed')
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    expected_warning="E-Mail Address does not appear to be valid!"
    assert context.RegisterPage.display_warning_for_missing_email(expected_warning)

@then('proper warning message informing about duplicate account should get dispalyed')
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    expected_warning="Warning: E-Mail Address is already registered!"
    assert context.RegisterPage.display_warning_for_duplicate_account(expected_warning)

@when('Dont enter details in any fields')
def step_impl(context):
    context.RegisterPage=RegisterPage(context.driver)
    context.RegisterPage.enter_first_name("")
    context.RegisterPage.enter_last_name("")
    # timestamp=datetime.date().strftime("%Y_%m_%d_%H_%M_%S")
    email_id="kal66ya@gmail.com"
    context.RegisterPage.enter_email_id("")
    context.RegisterPage.enter_telephone("")
    context.RegisterPage.enter_password("")
    context.RegisterPage.enter_confirm_password("")

@then('proper warning message for mandatory fields should get displayed')
def step_impl(context):
    first_name_warning="First Name must be between 1 and 32 characters!"
    last_name_warning="Last Name must be between 1 and 32 characters!"
    email_warning="E-Mail Address does not appear to be valid!"
    telephone_warning="Telephone must be between 3 and 32 characters!"
    password_warning="Password must be between 4 and 20 characters!"
    context.RegisterPage=RegisterPage(context.driver)
    
    assert context.RegisterPage.verify_status_for_misisng_all_fields(first_name_warning,last_name_warning,email_warning,telephone_warning,password_warning)