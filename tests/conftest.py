"""
@package base

Webdriver Factory Class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_webdriver_instance()
"""
import logging

import pytest
from selenium import webdriver
from utilities import selenium_logger as slogger

from pages.home.login_page import LoginPage


class WebDriverFactory:
    log = slogger.selenium_logger(logging.DEBUG)

    def __init__(self, browser) -> None:
        """
        Initiates WebdriverFactory
        :param browser Select which browser to test on
        """
        self.browser = browser
        self.base_url = "https://courses.letskodeit.com/"

    """
        Set Chrome driver and edge environment based on OS
        chromedriver = "C/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
    """

    def get_webdriver_instance(self) -> webdriver:
        """
        Get Webdriver Instance based on the browser configuration
        :return: selenium.webdriver instance
        """
        if self.browser == "chrome":
            # Set Chrome Dricver
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "safari":
            driver = webdriver.Safari()
        else:
            driver = webdriver.Chrome()

        # Setting Driver Implicit Time Out for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with URL
        driver.get(self.base_url)
        # Log Browser, OS, Version
        self.log.info(f"{'##'*50}\n\n"
                      f"Selenium Testing {self.base_url} :: Browser - {driver.capabilities['browserName']} :: "
                      f"Version :: {driver.capabilities['browserVersion']} :: platform :: {driver.capabilities['platformName']}")

        return driver


@pytest.fixture(scope="class")
def cls_resource(request, browser, os_type):
    print("\n--------------PYTEST SETUP-----------------")

    webdriver_factory = WebDriverFactory(browser)
    driver = webdriver_factory.get_webdriver_instance()
    base_url = webdriver_factory.base_url
    driver.implicitly_wait(3)
    login_process = LoginPage(driver)
    login_process.login("sjaguarsf@gmail.com", "sanfranciscocasper")

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.base_url = base_url

    yield driver, base_url
    print("---------------------PYTEST TEARDOWN----------------")
    driver.quit()


@pytest.fixture()
def resource():
    print("\n-----------------SETUP-----------------")
    yield
    print("\n------------------TEARDOWN---------------")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of OS, operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
