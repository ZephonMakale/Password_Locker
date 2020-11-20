import unittest
from user import User


class TestClass(unittest, TestCase):
    """
    Test class that defines test cases for the Users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_users = User("Zephon Makale", "1234xyz") #Create User object
    
    