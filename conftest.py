import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


# todo: pipeline or run on device farm
# todo: user composition instead of inheritance

@pytest.fixture(scope="class")
def driver(request):
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """This fixture takes screenshot of failed test cases"""
    # Execute the test
    outcome = yield
    result = outcome.get_result()
    # Check if the test has failed
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup_driver")  # Access the browser fixture
        if driver:
            timestamp = time.strftime("%Y_%m_%d_%H:%M:%S")
            screenshot_filename = f"{item.name}_{timestamp}.png"
            screenshot_path = './screenshots/' + screenshot_filename
            driver.save_screenshot(screenshot_path)
