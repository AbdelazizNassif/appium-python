from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SuccessLogin(BasePage):

    # Locators
    LOGIN_SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@text, 'logged')]")
    LOGIN_SUCCESS_HEADER = (By.XPATH, "//*[@text='Success']")

    # Actions
    def get_login_success_message(self):
        return self.locate_element(*self.LOGIN_SUCCESS_MESSAGE).text

    def get_login_success_header(self):
        return self.locate_element(*self.LOGIN_SUCCESS_HEADER).text
