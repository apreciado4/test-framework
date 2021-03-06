"""
Base Page class implmentation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits Basepage class

        :param driver:
        """
        super(BasePage, self).__init__(driver)
        self.util = Util()

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title
        :param title_to_verify: Title on the page that needs to be verified
        :return:
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get the page title")
            print_stack()
            return False
