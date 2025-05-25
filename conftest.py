import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# todo: take screenshot on fail
# todo: pipeline or run on device farm
# todo: user composition instead of inheritance
# todo: run multi tests in sequence
# todo: add more methods on base page


@pytest.fixture(scope="class")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Pixel XL"
    options.automation_name = "UiAutomator2"
    options.platform_version = "13"
    #  com.wdiodemoapp/com.wdiodemoapp.MainActivity}
    options.app = "C:\\Users\\dell\\PycharmProjects\\appium-tutuorial\\app\\test-app.apk"
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()


