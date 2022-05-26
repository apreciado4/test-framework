from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

from utilities.util import Util


@pytest.mark.usefixtures("cls_resource", "resource")
class TestRegisterCourses(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, cls_resource):
        self.register_courses = RegisterCoursesPage(self.driver)
        self.login_process = LoginPage(self.driver)
        self.test_status = TestStatus(self.driver)
        self.util = Util()

    @pytest.mark.order(3)
    def test_invalid_enrollment(self):
        # Test Search for class
        self.register_courses.enter_course_name("JavaScript for beginners")
        self.driver.implicitly_wait(3)
        result1 = self.register_courses.verify_page_title("All Courses")
        self.test_status.mark(result1, "Verify Page Title is 'All Courses'")
        result2 = self.register_courses.verify_header_course_title("JavaScript for beginners")
        self.test_status.mark(result2, "Verify Course Title Link is Present")

        # Test selecting class to enroll after search
        self.register_courses.select_course_to_enroll("JavaScript for beginners")
        result3 = self.register_courses.verify_course_is_present("JavaScript for beginners")
        self.test_status.mark(result3, "Verify Course Title is Present")

        # Test input of credit card information and error result
        self.register_courses.enroll_course("4716631843904011", "02/28", "169")
        result4 = self.register_courses.verify_enroll_failed()
        self.test_status.mark_final("Test Invalid Enrollment", result4, "Verify Invalid Enrollment")

