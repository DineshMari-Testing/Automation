import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver (Ensure you have chromedriver.exe in PATH)
chrome_driver_path = "D:\Selenium\chromedriver-win64\chromedriver-win64/chromedriver.exe"
# Create a Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://accounts.truckrr.com/")
driver.maximize_window()
print(driver.title)
time.sleep(2)

username=driver.find_element(By.ID,"Username")
username.send_keys("demotruckrr@gmail.com")

password=driver.find_element(By.ID,"Password")
password.send_keys("Demo@123")


but=driver.find_element(By.NAME,"button").click()
sleep(1)

# Close the browser
driver.quit()
