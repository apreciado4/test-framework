import unittest

import pytest

from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
from halo import Halo


@pytest.mark.usefixtures("cls_resource", "resource")
class TestLogin(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, cls_resource) -> None:
        self.login_process = LoginPage(self.driver)
        self.test_status = TestStatus(self.driver)

    @Halo(text="Testing Valid Login", spinner='dots')
    @pytest.mark.order(2)
    def test_valid_login(self):
        self.login_process.login("sjaguarsf@gmail.com", "sanfranciscocasper")
        self.driver.implicitly_wait(3)
        result_1 = self.login_process.verify_login_title()
        self.test_status.mark(result_1, "Title is correct")
        result_2 = self.login_process.verify_login_successful()
        self.test_status.mark_final("test_valid_login", result_2, "Login was successful")
        # print(f"Successful Login?     ::  {successful_login}  ::")
        # assert successful_login

    @Halo(text="Testing Invalid Login", spinner='dots')
    @pytest.mark.order(1)
    def test_invalid_login(self):
        self.login_process.logout()
        self.login_process.login("fakeemail@gmail.com", "fakepassword")
        self.driver.implicitly_wait(3)
        failed_login = self.login_process.verify_login_failure()

        print(f"Failed Login?     ::  {failed_login}  ::")
        assert failed_login
