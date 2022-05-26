"""
self.check_point.markFinal("TestName", result, "Message"
"""
import logging
from traceback import print_stack

from base.selenium_driver import SeleniumDriver
import utilities.selenium_logger as slogger


class TestStatus(SeleniumDriver):
    log = slogger.selenium_logger(logging.INFO)

    def __init__(self, driver):
        """
        Initiates a CheckPoint class
        :param driver: 
        """
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(f"#### VERIFICATION SUCCESSFUL  ::  {result_message}  ::")
                else:
                    self.result_list.append("FAIL")
                    self.log.info(f"#### VERIFICATION FAILED  ::  {result_message}  ::")
                    self.screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.info(f"#### VERIFICATION FAILED  :: {result_message}  ::")
                self.screenshot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.info("#### Exception Occurred !!!")
            self.screenshot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        :param result: Boolean of result (passed test or not)
        :param result_message: Enter a message if failed
        :return:
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        :param test_name:
        :param result:
        :param result_message:
        :return:
        """
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(f"::  {test_name}  ::   ### TEST FAILED ###")
            self.result_list.clear()
            assert True is False
        else:
            self.log.info(f"::  {test_name}  ::  ### TEST SUCCESSFUL ###")
            self.result_list.clear()
            assert True is True

