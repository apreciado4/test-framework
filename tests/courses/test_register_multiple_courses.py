from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.login_page import LoginPage
from pages.home.navigation_page import NavigationPage
from utilities.test_status import TestStatus
from utilities.read_data import get_cvs_data
from ddt import ddt, data, unpack
import unittest
import pytest

from utilities.util import Util
from halo import Halo


@pytest.mark.usefixtures("cls_resource", "resource")
@ddt
class TestRegisterMultiCourses(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, cls_resource):
        self.register_courses = RegisterCoursesPage(self.driver)
        self.login_process = LoginPage(self.driver)
        self.navigation = NavigationPage(self.driver)
        self.test_status = TestStatus(self.driver)
        self.util = Util()

    def setUp(self) -> None:
        self.navigation.navigate_to_all_courses()

    @pytest.mark.order(1)
    @Halo(text="Testing Invalid Enrollment", spinner='dots')
    # @data(("JavaScript for beginners", "4716631843904011", "02/28", "169"), ("Learn Python 3 from scratch", "4716631843904011", "02/28", "169"))
    @data(*get_cvs_data("test_data.csv"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv):
        # Test Search for class
        self.register_courses.enter_course_name(course_name)
        self.driver.implicitly_wait(3)
        result1 = self.register_courses.verify_page_title("All Courses")
        self.test_status.mark(result1, "Verify Page Title is 'All Courses'")
        result2 = self.register_courses.verify_header_course_title(course_name)
        self.test_status.mark(result2, "Verify Course Title Link is Present")

        # Test selecting class to enroll after search
        self.register_courses.select_course_to_enroll(course_name)
        result3 = self.register_courses.verify_course_is_present(course_name)
        self.test_status.mark(result3, "Verify Course Title is Present")

        # Test input of credit card information and error result
        self.register_courses.enroll_course(cc_num, cc_exp, cc_cvv)
        result4 = self.register_courses.verify_enroll_failed()
        self.test_status.mark_final("Test Invalid Enrollment", result4, "Verify Invalid Enrollment")

        # # Reset For Multiple Tests
        # self.register_courses.click_all_courses_button()
