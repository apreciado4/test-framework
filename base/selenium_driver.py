import logging
import os
import time
from traceback import print_stack

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote import webelement

import utilities.selenium_logger as slogger


class SeleniumDriver:
    log = slogger.selenium_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, result_message):
        """
        Takes screenshot of the current open web page
        :param result_message:
        :return:
        """
        file_name = f"{result_message}_{round(time.time() * 1000)}.png"
        screenshot_directory = "../screenshots/"
        relative_filename = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)  # PWD
        destination_file = os.path.join(current_directory, relative_filename)  # PWD../screenshots/filename
        destination_directory = os.path.join(current_directory, screenshot_directory)  # PWD../screenshots

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info(f"Screenshot saved to directory:  {destination_file}")
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def implicit_wait(self, sec):
        self.driver.implicitly_wait(sec)

    def get_title(self):
        title = None
        try:
            title = self.driver.title
            self.log.info(f"Title of Website found ::  {title}")
        except:
            self.log.info("Title of Website not found")
        return title

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get "Text  of an element
        :param locator:
        :param locator_type:
        :param element:
        :param info:
        :return:
        """
        try:
            if locator:
                self.log.info("In Locator Condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug(f"After finding element, size is {len(text)}")
            if len(text) == 0:
                text = element.get_attribute("innerText")
                if len(text) != 0:
                    self.log.info(f"Getting text on element :: {info}")
                    self.log.info(f"The text is :: {text}")
                    text = text.strip()
        except:
            self.log.error(f"Failed to get text on element {info}")
            print_stack()
            text = None
        return text

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id") -> webelement.WebElement:
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f"Element Found with locator: {locator}, using locator type: {locator_type}")
        except:
            self.log.info(f"Element not found with locator: {locator}, , using locator type: {locator_type}")
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Get List of elements
        :param locator:
        :param locator_type:
        :return:
        """
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info(f"Element list found with locator:  {locator}, and locatorType: {locator_type}")
        except:
            self.log.info(f"Element list NOT found with locator: {locator}, and locatorType: {locator_type}")
        return elements

    def element_click(self, locator="", locator_type="id", element=None):
        """
        Click on element
        :param locator:
        :param locator_type:
        :param element: Can pass in element directly
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.driver.implicitly_wait(5)
            element.click()
            self.log.info(f"Clicked on the element with: {locator}   locator type: {locator_type}")
            self.driver.implicitly_wait(3)
        except:
            self.log.info(f"Cannot click on the element with: {locator}    locator type: {locator_type}")
            print_stack()

    def element_keys(self, keys, locator="", locator_type="id", element=None):
        """
        Send Keys to Element
        :param keys: Keys to send to element
        :param locator: Locator to find element
        :param locator_type: Type of locator to find element
        :param element: Can Pass in Element Directly
        :return:
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.driver.implicitly_wait(5)
            element.send_keys(keys)
            self.log.info(f"Sent Keys to element with locator: {locator}  locatorType: {locator_type}")
            self.driver.implicitly_wait(3)
        except:
            self.log.info(f"Cannot Send Keys to element with locator: {locator}  locatorType: {locator_type}")
            print_stack()

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if Element is displayed
        :param locator:
        :param locator_type:
        :param element:
        :return:
        """
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info(f"Element is displayed with locator: {locator}, locator_type: {locator_type}")
            else:
                self.log.info(f"Element is NOT displayed with locator: {locator}, locator_type: {locator_type}")
            return is_displayed
        except:
            print("Element Not Found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def scroll_browser(self, direction="up"):
        """
        Scroll up or down
        :param direction: "up" or "down
        :return:
        """
        if direction.lower() == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -600);")

        if direction.lower() == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 600);")

    def switch_to_frame(self, id="", name="", element=None, index=None):
        """
        Switch to iframe using element locator inside iFrame
        :param id: id of the iframe
        :param name: name of the iframe
        :param index: index of the iframe
        :return: None
        """

        if id:
            self.driver.switch_to.frame(id)
            self.log.info(f"Switch to frame with id: {id}")
        if name:
            self.driver.switch_to.frame(name)
            self.log.info(f"Switch to frame with name: {name}")
        if index:
            self.log.info("Switch to frame with index:")
            self.log.info(str(index))
            self.driver.switch_to.frame(index)
        if element:
            self.driver.switch_to.frame(element)

    def switch_to_by_index(self, locator="", locator_type="xpath"):
        """
        Get iframe index using element locator inside iframe
        :param locator: Locator of Element
        :param locator_type: Locator Type to find the element
        :return: Index of iFrame
        """
        result = False
        try:
            iframe_list = self.get_element_list("//iframe", locator_type="xpath")
            self.log.info(f"Length of iFrame list :: {len(iframe_list)} ::")
            for num in range(len(iframe_list)):
                self.switch_to_frame(index=iframe_list[i])
                result = self.is_element_present(locator, locator_type)
                if result:
                    self.log.info(f"iFrame index is :: {num}")
                    break
                self.switch_to_default_content()
            return result
        except:
            self.log.debug("iFrame index not found")

    def switch_to_default_content(self):
        """
        Switch to default content
        :return:
        """
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator="", locator_type=""):
        """
        Get value of the attribute of element
        :param attribute: attribute whose value to find
        :param element: Element whose attribute need to find
        :param locator: Locator of the element
        :param locator_type: Locator type to find the element
        :return: Value of the attribute
        """
        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
            value = element.get_attribute()
            return value

    def is_enabled(self, locator, locator_type="id", info="") -> bool:
        """
        Check if element is enabled
        :param locator: Locator of the element to check
        :param locator_type: Type of the locator (xpath, etc..)
        :param info: Information about the element, label/name of the element
        :return: boolean
        """
        element = self.get_element(locator=locator, locator_type=locator_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info(f"Attribute value from Application Web UI --> :: {value}")
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info(f"Element :: '{info}' :: is enabled")
            else:
                self.log.info(f"Element :: '{info}' :: is not enabled")
        except:
            self.log.error(f"Element :: {info} :: state could not be found")
        return enabled
