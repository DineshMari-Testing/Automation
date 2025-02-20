from selenium import webdriver
from behave import *


@given('I launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=webdriver.ChromeService("C:\Software\chromedriver-win64\chromedriver-win64/chromedriver.exe"))


@given('I launch browser')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('I check logo is there')
def step_impl(context):



@when('I launch my application')
def step_impl(context):



@when('Enter username and password')
def step_impl(context):


@then('close the browser')
def step_impl(context):
    context.driver.close()

