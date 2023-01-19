from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
import os
import time

# Parameters
DEVICE_NAME = "My Phone"
PLATFORM_VERSION = "8.1.0"
APP_PACK = "com.android.calculator2"
APP_ACT = "com.android.calculator2.Calculator"
UID = "192.XXX.XXX.XXX:5555" 


# Desired Capabilities

desired_cap  = {
    "deviceName": DEVICE_NAME,
    "platformName": "Android",       
    "udid": UID,        
    "platformVersion":  PLATFORM_VERSION,
    "automationName": "UiAutomator2",    
    "appPackage": APP_PACK,
    "appActivity": APP_ACT,
    "noReset": "true"
}

# CONNECT TO APPIUM Server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

# Test case to test addition operation
def test_add_operation():     
    driver.find_element(AppiumBy.ID, "com.android.calculator2:id/digit_2").click()
    print("Pressing 2")
    driver.find_element(AppiumBy.ID, "com.android.calculator2:id/op_add").click()
    print("Pressing Plus")
    driver.find_element(AppiumBy.ID, "com.android.calculator2:id/digit_4").click()
    print("Pressing 4")
    driver.find_element(AppiumBy.ID, "com.android.calculator2:id/eq").click()
    print("Pressing Equal")
    result = driver.find_element(AppiumBy.ID, "com.android.calculator2:id/result").text
    print("Result", result)    
    
def tearDown():
    # Close is not working with Appium
    driver.quit()

# Execute Code

test_add_operation()
time.sleep(10)
tearDown()