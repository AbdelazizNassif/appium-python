from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def locate_element(self, by, locator):
        self.wait.until(EC.visibility_of_element_located((by, locator)))
        return self.driver.find_element(by, locator)

    def swipe_horizontal_w3c(self, start_x, end_x, y, duration=800):
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(start_x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration / 1000)  # duration in seconds
        actions.pointer_action.move_to_location(end_x, y)
        actions.pointer_action.pointer_up()
        actions.perform()

    def swipe_vertical_w3c(self, y_start, y_end, duration=800):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        start_x = width // 2
        start_y = int(height * y_start)
        end_y = int(height * y_end)
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration / 1000)  # in seconds
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()
