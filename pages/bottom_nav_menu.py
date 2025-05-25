from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.swipe_page import SwipePage


class BottomNav(BasePage):
    # Locators
    LOGIN_OPTION = (By.XPATH, "//*[@text='Login']")
    SWIPE_OPTION = (By.XPATH, "//*[contains(@content-desc, 'Swipe')]")

    # Actions
    def click_login_option(self):
        self.locate_element(*self.LOGIN_OPTION).click()
        return LoginPage(self.driver)

    def click_swipe_option(self):
        self.locate_element(*self.SWIPE_OPTION).click()
        return SwipePage(self.driver)
