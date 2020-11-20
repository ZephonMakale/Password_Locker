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
    
