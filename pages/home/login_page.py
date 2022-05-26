import time

import utilities.selenium_logger as slogger
from pages.home.navigation_page import NavigationPage
import logging
from base.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    log = slogger.selenium_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation = NavigationPage(driver)

    # Locators
    # _login_link = "//a[@href='https://courses.letskodeit.com/login']"
    _login_link_safari = ["//a[text()='Sign In']", "xpath"]
    _login_link = ["//a[contains(text(),'Sign In')]/parent::div", "xpath"]
    _verify_login = ["h1", "tag"]
    _logout_link = ["//a[contains(text(),'Logout')]", "xpath"]
    _verify_logout = ['//span[text()="Your username or password is invalid. Please try again."]', "xpath"]
    _email_input = ["email", "id"]
    _password_input = ["password", "id"]
    _login_submit = ['//input[@type="submit"]::div', "xpath"]
    _close_pop_up = ['img[name="cp_close_image-2"]', "xpath"]
    _verify_title = "My Courses"

    def click_login_link(self):
        self.element_click(*self._login_link)

    def enter_email(self, email):
        self.element_keys(email, *self._email_input)

    def enter_password(self, password):
        self.element_keys(password, *self._password_input)

    def click_login_submit(self):
        # Cannot click element on Safari
        # self.element_click(self._login_submit, locator_type="xpath")
        self.element_keys(Keys.RETURN, *self._password_input)

    def login(self, username, password):
        time.sleep(2)
        self.click_login_link()
        # self.clear_input()
        time.sleep(2)
        self.enter_email(username)
        time.sleep(2)
        self.enter_password(password)
        self.click_login_submit()
        time.sleep(2)

    def logout(self):
        self.implicit_wait(2)
        self.navigation.click_user_settings()
        self.element_click(*self._logout_link)

    def verify_login_successful(self):
        result = self.is_element_present(*self._verify_login)
        return result

    def verify_login_failure(self):
        result = self.is_element_present(*self._verify_logout)
        return result

    def verify_login_title(self):
        return self.verify_page_title(self._verify_title)

    # def clear_input(self):
    #     email_input = self.get_element(locator=self._email_input)
    #     email_input.clear()
    #     password_input = self.get_element(locator=self._password_input)
    #     password_input.clear()
