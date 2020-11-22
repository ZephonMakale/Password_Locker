import unittest #Imports the unittest module.
from user import User  #Imports the user class.
from user import Credentials


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

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Users class behaviours.
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("gmail", "Zephon Makale", "1234xyz")
    
    def test_init(self):
        """
        test_init: test case to test if the object is initialized properly.
        """
        self.assertEqual(self.new_credentials.account, "gmail")
        self.assertEqual(self.new_credentials.usernames, "Zephon Makale")
        self.assertEqual(self.new_credentials.passwords, "1234xyz")

    def save_credential_test(self):
        """
        test_save_credential test case tests if the user object is saved into the credentials list.
        """

        self.new_credentials.save_attributes()
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
        """
        test_save_multiple_accounts to check if we can save multiple credentials objects
        to our credentials_list
        """
        self.new_credentials.save_attributes()
        test_credential = Credentials("Instagram", "@zephonmakale", "123456")
        test_credential.save_attributes()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove a contact from our credential list
        """

        self.new_credentials.save_attributes()
        test_credential = Credentials("Instagram", "@zephonmakale", "123456")
        test_credential.save_attributes()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials(self):
        """
        test to check if we can find a credential by account name and display information of the credential
        """
        self.new_credentials.save_attributes()
        test_credential = Credentials("Instagram", "@zephonmakale", "123456")
        test_credential.save_attributes()

        found_credential = Credentials.find_credentials("Instagram")

        self.assertEqual(found_credential.account, test_credential.account)

    def test_credential_exists(self):
        """
        test to check if we can return a boolean, if we don't find the credential
        """
        self.new_credentials.save_attributes()
        test_credential = Credentials("Instagram", "@zephonmakale", "123456" )
        test_credential.save_attributes()

        credential_exist = Credentials.credentials_exist("Instagram")
        self.assertTrue(credential_exist)

    def test_display_all_credentials(self):
        """
        method that returns a list of all credentials saved by the user
        """

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
        
if __name__ == '__main__':
    unittest.main()
