import unittest

from test_suite import SuiteCompilation


def return_suite():
    suite = unittest.TestSuite()
    suite.addTests(SuiteCompilation.return_suite())
    return suite  # 返回子套件