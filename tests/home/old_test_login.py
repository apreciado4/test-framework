# import time
# from pages.login_page import LoginPage
# import unittest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
#
# # class TestLogin(unittest.TestCase):
# #     def test_valid_login(self):
#         base_url = "https://letskodeit.com"
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         driver.implicitly_wait(3)
#         driver.get(base_url)
#
#         login_process = LoginPage(driver)
#         login_process.login("sjaguarsf@gmail.com", "sanfranciscocasper")
#
#         try:
#             successful_login = True
#             driver.find_element(By.TAG_NAME, "h1")
#         except NoSuchElementException:
#             successful_login = False
#
#         print(f"Successful Login?     ::  {successful_login}  ::")
#         assert successful_login
