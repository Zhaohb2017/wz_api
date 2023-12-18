import unittest
from test_case.monitoring import ServiceCollection


def return_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(ServiceCollection))
    return suite  # 返回子套件