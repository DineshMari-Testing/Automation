import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *


@given('launch browser')
def launch_browser(context):
    print("Launching browser...")
    context.chrome_driver_path = r"D:/Selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    service = Service(context.chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()


@when('launch truckrr one browser')
def launch_application(context):
    print("Opening Truckrr login page...")
    context.driver.get("https://accounts.truckrr.com/")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Page loaded successfully.")


@when(u'Enter "{username}" and "{password}"')
def enter_credentials(context, username, password):
    driver = context.driver

    print(f"Entering username: {username}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Username"))).send_keys(username)

    print("Entering password...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Password"))).send_keys(password)

    print("Clicking login button...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='button']"))).click()
    print("Login button clicked.")


@when('skip two step verification page')
def skip_verification(context):
    try:
        print("Checking for Skip button...")
        skip_button = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Skip']")))
        skip_button.click()
        print("Skipped two-step verification.")
    except:
        print("Skip button not found, continuing...")


@when('Need to add customer')
def add_customer(context):
    driver = context.driver  # Ensure driver is accessed from context
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//li[@id='tis-customer']//a[@class='text-nowrap d-flex align-items-center']//*[name()='svg']"))
    ).click()


@when('click add customer to add')
def customer_butt(context):
    driver = context.driver  # Get driver from context
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='shipperAdd']"))
    )
    add_button.click()


@when('Entering customer details')
def enter_fields(context):
    driver = context.driver
    Dropdown = context.dropdown# Ensure driver is accessed from context

    # Handle alert if it appears
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print("No alert found, proceeding...")


    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='shipperNoGSTnumber']"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,"shipper-name")).sendkeys("Kishore"))
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='shipper-state']"))
    )
    select = Select(dropdown)
    select.select_by_visible_text("Tamil Nadu")

    
@then('close browser')
def close_browser(context):
    print("Closing browser...")
    context.driver.quit()
