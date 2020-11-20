import random
import string
import pyperclip

class User:
    """
    Creates a user class that generates new intances of the User.
    """

    user_list = []

    def __init__(self, username, password):

        """
        This function method gets to define the properties of the user. That's their username and password.
        """

        self.username = username
        self.password = password

    def save_users(self):
        """
        save_users method saves new users into user_list
        """

        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        """
        delete_user method deletes a saved user account
        """
        User.user_list.remove(self)



    
class Credentials():
    """
    Credentials class to help create new objects of credentials
    """
    credentials_list = []

    @classmethod
    def user_verification(cls, username, password):
        """
        user verification method verifies whether is in the user_list 
        """
        x_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                x_user == user.username
        return x_user


    def __init__(self, account, usernames, password):
        """
        this function method defines user credentials
        """
        self.account = account
        self.usernames = usernames
        self.password = password

    def save_attributes(self):
        """
        save details method stores a new credential into the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method deletes saved credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credentials(cls, account):
        """
        Method that takes in an account name and returns a credential that matches that account name
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credentials(account)
        pyperclip.copy(found_credentials.password)    


    @classmethod
    def credentials_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns the credentials
        """
        return cls.credentials_list

    def generate_password(length): #Generate a random password string of letters, digits and special character"
        password = string.ascii_uppercase + string.ascii_lowercase + "!@#$%&*"
        result_str = ''.join(random.choice(password) for i in range(length))
        return result_str    