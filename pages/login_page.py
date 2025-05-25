from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.success_login_modal import SuccessLogin


class LoginPage(BasePage):

    # Locators
    USERNAME_FIELD = (By.XPATH, "//*[contains(@content-desc, 'input-email')]")
    PASSWORD_FIELD = (By.XPATH, "//*[contains(@content-desc, 'input-password')]")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@text, 'LOGIN')]")

    # Actions
    def login(self,  username, password):
        self.locate_element(*self.USERNAME_FIELD).send_keys(username)
        self.locate_element(*self.PASSWORD_FIELD).send_keys(password)
        self.locate_element(*self.LOGIN_BUTTON).click()
        return SuccessLogin(self.driver)
