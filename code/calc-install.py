from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
import os
import time

# Parameters
DEVICE_NAME = "My Phone"
PLATFORM_VERSION = "11"

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

APP_PATH = PATH( "../apps/Calc.apk" )

print(APP_PATH)

# Desired Capabilities

desired_cap  = {
    "deviceName": DEVICE_NAME,
    "platformName": "Android",       
    "udid": "emulator-5554",        
    "platformVersion":  PLATFORM_VERSION,
    "automationName": "UiAutomator2",    
    "app": APP_PATH,    
    "noReset": "true"
}

# CONNECT TO APPIUM
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

# Test case to test addition operation
def test_add_operation():     
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2").click()
    print("Pressing 2")
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()
    print("Pressing Plus")
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_4").click()
    print("Pressing 4")
    driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()
    print("Pressing Equal")
    result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text
    print("Result", result)
    #print(result)
    
def tearDown():
    # Close is not working with appium so I've used quit
    driver.quit()

# Execute Code

test_add_operation()
time.sleep(10)
tearDown()