import unittest
from tests.home.test_login import TestLogin
from tests.courses.test_register_multiple_courses import TestRegisterMultiCourses

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRegisterMultiCourses)

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
