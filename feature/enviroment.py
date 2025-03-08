
# from selenium import webdriver
# from behave import *

# def before_scenario(context,driver):
#     context.driver=webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.get("https://tutorialsninja.com/demo/")

# def after_scenario(context,driver):
#     context.driver.quit()

def after_step(context,step):
    if step.status=='failed':
        allure.attach(context.driver.get_screenshot_as_png(),name="failed_scr",attachment_type=AttachmentType.PNG)