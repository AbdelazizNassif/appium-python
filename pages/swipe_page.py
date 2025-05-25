from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.success_login_modal import SuccessLogin


class SwipePage(BasePage):

    # Locators
    FIRST_BOX = (By.XPATH, "//*[contains(@text, 'OPEN SOURCE')]")
    SECOND_BOX = (By.XPATH, "//*[contains(@text, 'GREAT')]")
    THIRD_BOX = (By.XPATH, "//*[contains(@text, 'JS')]")

    WDIO_LOGO = (By.XPATH, "//*[contains(@content-desc, 'WebdriverIO logo')]")
    BOTTOM_TEXT = (By.XPATH, "//*[contains(@text, 'found')]")

    # horizontal scroll methods
    def swipe_right(self):
        self.swipe_horizontal_w3c(200, 20, 1500)

    def get_first_box_text(self):
        return self.locate_element(*self.FIRST_BOX).text

    def is_first_box_displayed(self):
        return self.locate_element(*self.FIRST_BOX).is_displayed()

    def get_second_box_text(self):
        return self.locate_element(*self.SECOND_BOX).text

    def is_second_box_displayed(self):
        return self.locate_element(*self.SECOND_BOX).is_displayed()

    def get_third_box_text(self):
        return self.locate_element(*self.THIRD_BOX).text

    def is_third_box_displayed(self):
        return self.locate_element(*self.THIRD_BOX).is_displayed()

    # vertical scroll methods
    def swipe_bottom(self, pos1, pos2):
        self.swipe_vertical_w3c(pos1, pos2)

    def is_logo_displayed(self):
        return self.locate_element(*self.WDIO_LOGO).is_displayed()

    def get_bottom_text(self):
        return self.locate_element(*self.BOTTOM_TEXT).text

