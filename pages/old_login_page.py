# from base.selenium_driver import SeleniumDriver
# from selenium.webdriver.common.by import By
#
#
# class LoginPage(SeleniumDriver):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     # Locators
#     _login_link = "//a[@href='https://courses.letskodeit.com/login']"
#     _email_input = "email"
#     _password_input = "password"
#     _login_submit = '//input[@type="submit"]'
#
#     def get_login_link(self):
#         return self.driver.find_element(By.XPATH, self._login_link)
#
#     def get_email_input(self):
#         return self.driver.find_element(By.ID, self._email_input)
#
#     def get_password_input(self):
#         return self.driver.find_element(By.ID, self._password_input)
#
#     def get_login_submit(self):
#         return self.driver.find_element(By.XPATH, self._login_submit)
#
#     def click_login_link(self):
#         self.get_login_link().click()
#
#     def enter_email(self, email):
#         self.get_email_input().send_keys(email)
#
#     def enter_password(self, password):
#         self.get_password_input().send_keys(password)
#
#     def click_login_submit(self):
#         self.get_login_submit().click()
#
#     def login(self, username, password):
#         self.click_login_link()
#         self.enter_email("sjaguarsf@gmail.com")
#         self.enter_password("sanfranciscocasper")
#         self.click_login_submit()
