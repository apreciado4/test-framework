"""
Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.get_unique_name()
"""
import logging
import random
import string
import time
import traceback

import utilities.selenium_logger as slogger


class Util(object):
    log = slogger.selenium_logger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        :param sec:
        :param info:
        :return:
        """
        if info is not None:
            self.log.info(f"Wait :: '{sec}' seconds for {info}")
            try:
                time.sleep(sec)
            except InterruptedError:
                traceback.print_stack()

    def get_alpha_numeric(self, length, alpha_type="letters"):
        """
        Get random string of characters
        :param length: Length of string, number of characters string should have
        :param alpha_type: Type of characters string should have. Default is letters
        Provide lower/upper/digits for different types
        :return:
        """
        alpha_num = ""
        if alpha_type == "lower":
            case = string.ascii_lowercase
        elif alpha_type == "upper":
            case = string.ascii_uppercase
        elif alpha_type == "digits":
            case = string.digits
        elif alpha_type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count=10, case="lower"):
        """
        Get a Unique Name
        :param case:
        :param char_count:
        :return:
        """
        return self.get_alpha_numeric(char_count, case)

    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of vaild email ids
        :param list_size: Number of email IDs. Default is 5 email in a list
        :param item_length: It should be a list containing number of items equal to list size
                            This determines the length of each item in the list
        :return:
        """
        unique_name_list = []
        for num in range(0, list_size):
            unique_name_list.append(self.get_unique_name(char_count=item_length[num]))
        return unique_name_list

    def verify_text_contains(self, actual_text, expected_text):
        """
        Vrify actual text contains expected text string
        :param actual_text:  Actual Text
        :param expected_text: Expected Text
        :return:
        """
        self.log.info(f"Actual Text From Application Web UI --> :: {actual_text}")
        self.log.info(f"Expected Text From Application Web UI --> :: {expected_text}")
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS TEXT!!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAIN TEXT !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify text match
        :param actual_text:
        :param expected_text:
        :return:
        """
        self.log.info(f"Actual text From Application Web UI --> :: {actual_text}")
        self.log.info(f"Expected text From Application Web UI --> :: {expected_text}")
        if actual_text.lower() == expected_text.lower():
            self.log.info("### VERIFICATION TEXT MATCHED")
            return True
        else:
            self.log.info("### VERIFICATION TEXT DOES NOT MATCH")
            return False

    def verify_list_match(self, expected_list, actual_list):
        """
        Verifies that lists match
        :param expected_list:
        :param actual_list:
        :return:
        """
        self.log.info(f"Actual List from application Web UI --> :: {actual_list}")
        self.log.info(f"Expected List from application Web UI --> :: {expected_list}")
        # if functools.reduce(lambda x, y: x and y,
        #                     map(lambda p, q: p.lower() == q.lower(), actual_list, expected_list),
        #                     True):
        length = len(expected_list)
        for num in range(0, length):
            if expected_list[num] not in actual_list:
                self.log.info("### VERIFICATION LISTS MATCHED")
                return True
            else:
                self.log.info("### VERIFICATION LIST NOT MATCHED")
                return False
