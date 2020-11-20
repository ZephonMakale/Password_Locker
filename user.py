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
    
    def __init__(self, account, usernames, password):
        """
        this function method defines user credentials
        """