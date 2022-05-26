import logging

import utilities.selenium_logger as slogger
from base.base_page import BasePage


class NavigationPage(BasePage):
    log = slogger.selenium_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    _my_courses = ["//a[contains(text(),'MY COURSES')]", "xpath"]
    _all_courses = ["//a[contains(text(),'ALL COURSES')]", "xpath"]
    _user_settings_icon = ["//img[contains(@src, 'default-user-profile-pic')]/parent::button", "xpath"]
    _my_account = ["//a[contains(text(),'My Account')]", "xpath"]

    def navigate_to_my_courses(self):
        self.element_click(*self._my_courses)

    def navigate_to_all_courses(self):
        self.element_click(*self._all_courses)

    def click_user_settings(self):
        self.element_click(*self._user_settings_icon)

    def navigate_to_my_account(self):
        self.click_user_settings()
        self.implicit_wait(2)
        self.element_click(*self._my_account)
