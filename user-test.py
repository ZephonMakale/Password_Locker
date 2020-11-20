import unittest #Imports the unittest module.
from user import User  #Imports the user class.


class TestUser(unittest.TestCase): # Creates a subclass known as TestUser.
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

    def test_init(self):
        """
        test_init: test case to test if the object is initialized properly.
        """

        self.assertEqual(self.new_users.username, "Zephon Makale")
        self.assertEqual(self.new_users.password, "1234xyz")
    
    def test_save_users(self):
        """
        test_save_users test case tests if the user object is saved into the user list.
        """

        self.new_users.save_users() # saving the new user
        self.assertEqual(len(User.user_list), 1)

    
if __name__ == '__main__':
    unittest.main()
