from selenium.webdriver.common.by import By
from pages.bottom_nav_menu import BottomNav


class TestLogin:

    def test_login_to_app(self, driver):
        bottom_nav_menu = BottomNav(driver)
        login_page_actions = bottom_nav_menu.click_login_option()
        success_login_model = login_page_actions.login("ali@email.com", "123456789")
        assert success_login_model.get_login_success_header() == "Success"
        assert success_login_model.get_login_success_message() == "You are logged in!"
