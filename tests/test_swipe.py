import pytest
import time

from pages.bottom_nav_menu import BottomNav


class TestSwipe:

    def test_swipe_horizontal(self, driver):
        bottom_nav_menu = BottomNav(driver)
        swipe_page_actions = bottom_nav_menu.click_swipe_option()
        assert swipe_page_actions.get_first_box_text() == "FULLY OPEN SOURCE"
        assert swipe_page_actions.is_first_box_displayed() == True
        swipe_page_actions.swipe_right()
        assert swipe_page_actions.get_second_box_text() == "GREAT COMMUNITY"
        assert swipe_page_actions.is_second_box_displayed() == True
        swipe_page_actions.swipe_right()
        assert swipe_page_actions.get_third_box_text() == "JS.FOUNDATION"
        assert swipe_page_actions.is_third_box_displayed() == True

    def test_swipe_vertical(self, driver):
        bottom_nav_menu = BottomNav(driver)
        swipe_page_actions = bottom_nav_menu.click_swipe_option()
        swipe_page_actions.swipe_bottom(0.3, 0.1)
        swipe_page_actions.swipe_bottom(0.8, 0.1)
        swipe_page_actions.swipe_bottom(0.8, 0.1)
        assert swipe_page_actions.is_logo_displayed() == True
        assert swipe_page_actions.get_bottom_text() == "You found me!!!"
