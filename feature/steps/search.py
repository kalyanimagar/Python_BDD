from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from feature.pages import searchPage
from feature.pages.searchPage import SearchPage
from feature.pages.HomePage import HomePage

@given(u'Open home page')
def step_impl(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")

@when(u'Enter valid product in search box')
def step_impl(context):
    context.HomePage=HomePage(context.driver)
    context.HomePage.enter_product_in_serach_box("HP")

@when(u'click on Search button')
def step_impl(context):
    context.HomePage=HomePage(context.driver)
    context.HomePage.click_on_search_button()

@then(u'Valid product should get listed in search results')
def step_impl(context):
    context.searchPage=searchPage(context.driver)
    assert context.searchPage.verify_valid_product_is_displayed()

@when(u'Enter invalid product in search box')
def step_impl(context):
    context.HomePage=HomePage(context.driver)
    context.HomePage.enter_product_in_serach_box("1234")

@then(u'Proper validation message should be displayed')
def step_impl(context):
    expecetd_text="There is no product that matches the search criteria."
    context.searchPage=searchPage(context.driver)
    assert context.searchPage.verify_proper_message_id_dispayed(expecetd_text)

@when(u'Dont enter any product in search box')
def step_impl(context):
    context.HomePage=HomePage(context.driver)
    context.HomePage.enter_product_in_serach_box("")