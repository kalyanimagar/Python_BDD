from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.configReader import readConfiguration
from feature.pages.AccountPage import AccountPage
from feature.pages.HomePage import HomePage
from feature.pages.LoginPage import LoginPage

@given("Launch login page")
def step_impl(context):
    url= readConfiguration("basic info","url")
    browser=readConfiguration("basic info","browser")
    if browser=='Chrome':
        context.driver=webdriver.Chrome()
    elif browser=="firefox":
        context.driver=webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get(url)
    homepage=HomePage(context.driver)
    homepage.click_on_my_account()
    homepage.click_on_login_option()

@when(u'Enter valid username as "{email_id}" and password as "{password}"')
def step_impl(context,email_id,password):
   context.loginPage=LoginPage(context.driver)
   context.loginPage.enter_email_address(email_id)
   context.loginPage.enter_password(password)

@when("click on login button")
def step_impl(context):
    context.loginPage=LoginPage(context.driver)
    context.loginPage.click_on_login_button()
    
@then(u'User looged in successfully')
def step_impl(context):
   context.accountPage=AccountPage(context.driver)
   assert context.accountPage.display_status_of_edit_your_account_option()

@when(u'Enter invalid username as "{email_id}" and password as "{password}"')
def step_impl(context,email_id,password):
    context.loginPage=LoginPage(context.driver)
    context.loginPage.enter_email_address(email_id)
    context.loginPage.enter_password(password)

@then(u'proper warning message should be displayed')
def step_impl(context):
    context.loginPage=LoginPage(context.driver)
    expected_warning="Warning: No match for E-Mail Address and/or Password."
    assert context.loginPage.display_status_of_warning_message(expected_warning)

@when(u'Enter valid username as "{email_id}" and invalid password as "{password}"')
def step_impl(context,email_id,password):
    context.loginPage=LoginPage(context.driver)
    context.loginPage.enter_email_address(email_id)
    context.loginPage.enter_password(password)

@when(u'Enter invalid username as "{email_id}" and inpassword as "{password}"')
def step_impl(context,email_id,password):
    context.loginPage=LoginPage(context.driver)
    context.loginPage.enter_email_address(email_id)
    context.loginPage.enter_password(password)

@when(u'Dont enter email and password')
def step_impl(context):
    context.loginPage=LoginPage(context.driver)
    context.loginPage.enter_email_address("")
    context.loginPage.enter_password("")
