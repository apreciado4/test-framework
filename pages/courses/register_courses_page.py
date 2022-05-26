import time

import utilities.selenium_logger as slogger
import logging
from base.base_page import BasePage
from utilities.util import Util
from selenium.webdriver.common.keys import Keys


class RegisterCoursesPage(BasePage):

    log = slogger.selenium_logger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super(RegisterCoursesPage, self).__init__(driver)
        self.driver = driver

    # Locators
    _search_box = ["//input[@id='search']", "xpath"]
    _search_submit = ["//button[@type='submit']", "xpath"]
    _course_title = ["// h4[contains(text(), '{0}')]", "xpath"]
    # _course = ["//*[@href='/courses/javascript-for-beginners']/parent::div", "xpath"]
    _course = ["//h4[contains(text(), '{0}')]/ancestor::div[@class='zen-course-list']", "xpath"]
    _all_courses = ["//a[@href='/courses']", "xpath"]
    _enroll_button = ["//button[text()='Enroll in Course']", "xpath"]
    _cc_num = ["cardnumber", "name"]
    # Only Use next Line without iFrames
    # _cc_num = ["//*[@id='card-number']/div/input", "xpath"]
    _cc_exp = ["exp-date", "name"]
    # Only Use next Line without iFrames
    # _cc_exp = ["//*[@id='card-expiry']/div/input", "xpath"]
    _cc_cvv = ["cvc", "name"]
    # Only Use next Line without iFrames
    # _cc_cvv = ["//*[@id='card-cvc']/div/input", "xpath"]
    _element_present = ["//*[contains(text(), '{0}')]", "xpath"]
    _submit_enroll = ["button.zen-subscribe.sp-buy", "css"]
    _enroll_error_message = ["div.has-error.card-errors span", "css"]

    _cc_num_iframe = ["#card-number > div > iframe", "css"]
    _cc_exp_iframe = ["#card-expiry > div > iframe", "css"]
    _cc_cvv_iframe = ["#card-cvc > div > iframe", "css"]

    def click_all_courses_button(self):
        self.element_click(*self._all_courses)

    def send_course_name(self, name):
        self.element_keys(name, *self._search_box)

    def click_search_submit(self):
        self.element_click(*self._search_submit)

    def get_course_title(self, name):
        return self.get_text(locator=self._course_title[0].format(name), locator_type=self._course_title[1])

    def enter_course_name(self, name):
        """
        Goes to All Courses Page and inputs name of course you are looking for
        :String name: Takes in the name of the course you are looking for
        :return:
        """
        self.implicit_wait(3)
        self.click_all_courses_button()
        self.implicit_wait(2)
        self.send_course_name(name)
        self.implicit_wait(1)
        self.click_search_submit()
        self.implicit_wait(2)

    def verify_header_course_title(self, name):
        return self.util.verify_text_contains(self.get_course_title(name), name)

    def click_course_button(self, name=""):
        # self.element_click(*self._course)
        self.element_click(locator=self._course[0].format(name), locator_type=self._course[1])

    def click_enroll_button(self):
        self.scroll_browser("up")
        self.implicit_wait(2)
        self.element_click(*self._enroll_button)

    def select_course_to_enroll(self, full_course_name):
        self.click_course_button(full_course_name)
        self.implicit_wait(5)
        self.click_enroll_button()
        self.implicit_wait(2)

    def verify_course_is_present(self, name):
        return self.is_element_present(self._element_present[0].format(name), self._element_present[1])

    def enter_card_num(self, num):
        # Use when not using iFrame
        # self.element_keys(num, *self._cc_num)
        self.implicit_wait(2)
        self.switch_to_frame()
        self.switch_to_frame(self.get_element(*self._cc_num_iframe))
        self.implicit_wait(1)
        self.element_keys(num, *self._cc_num)
        self.switch_to_default_content()
        self.implicit_wait(1)

    def enter_card_exp(self, exp):
        # Only use next line when not using iFrames
        # self.element_keys(exp, *self._cc_exp)
        self.switch_to_frame(self.get_element(*self._cc_exp_iframe))
        self.implicit_wait(1)
        self.element_keys(exp, *self._cc_exp)
        self.switch_to_default_content()
        self.implicit_wait(1)

    def enter_card_cvv(self, cvv):
        # Only use next line when not using iFrames
        # self.element_keys(cvv, *self._cc_cvv)
        self.switch_to_frame(self.get_element(*self._cc_cvv_iframe))
        self.implicit_wait(1)
        self.element_keys(cvv, *self._cc_cvv)
        self.switch_to_default_content()
        self.implicit_wait(1)

    def click_enroll_submit_button(self):
        self.element_click(*self._submit_enroll)

    def enter_credit_card_info(self, num, exp, cvv):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)

    def enroll_course(self, num="", exp="", cvv=""):
        self.scroll_browser("down")
        self.enter_credit_card_info(num, exp, cvv)
        self.click_enroll_submit_button()
        self.implicit_wait(3)

    def verify_enroll_failed(self):
        return self.is_element_present(*self._enroll_error_message)




