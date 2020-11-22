#!/usr/bin/env python3.8
from user import User
from user import Credentials


def create_new_user(username,password):
    """
    create new user function creates a new user with a username and pssword
    """
    new_user = User(username,password)
    return new_user

def save_users(user):
    """
    save users function saves a new user to the program
    """
    user.save_users()

def display_user():
    """
    display user function displays existing user in the program
    """
    return User.display_user()

def login_user(username, password):
    confirm_user = Credentials.user_verification(username, password)
    return confirm_user

def create_new_credential(account, usernames, passwords):
    new_credential = Credentials(account, usernames, passwords)
    return new_credential

def save_credential(credentials):
    credentials.save_attributes()

def display_all_account_details():
    return Credentials.display_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def find_credentials(account):
    return Credentials.find_credentials(account)

def check_credentials(account):
    return Credentials.credentials_exist(account)

def generate_passwords():
    generated_password = Credentials.generate_password(None)
    return generated_password

def copy_password(account):
    return Credentials.copy_password(account)

def branch():
    print("Hey, welcome to your accounts password locker...\n Please enter one of the following.\n ca ---Create a new account \n li ---Have an account \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("Username: ")
        while True:
            print("tp - To type your own password:\ngp - To generate random password")
            Your_choice_password = input().lower().strip()
            if Your_choice_password == 'tp':
                password = input("Enter your password: \n")
                break
            elif Your_choice_password == 'gp':
                password = generate_passwords()
                break
            else:
                print("Invalid password, please try again")

        save_users(create_new_user(username, password))
        print("*"*85)
        print(f"Hello {username}, Your account has been succesfully created! Your password is: {password}")
        print("*"*85)

    elif short_code == "li":
        print("*"*50)
        print("Enter your user name and your password to log in: ")
        print('*' * 50)
        username = input("Username: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome to your passord locker manager")
            print('\n')
        else:
            print("You need to create an account first!")
    while True:
        print("Use these short codes: \n cc - Create a new credential account \n dc - Display credential \n fc - Find a credential \n gp - Generate a random password \n dc - Delete credential \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create new credential")
            print("."*20)
            print("Account name ...")
            account = input().lower()
            print("Your account username")
            usernames = input()
            while True:
                print("tp - To type your own password if you already have an account: \n gp - To generate random password")
                Your_choice_password = input().lower().strip()
                if Your_choice_password == 'tp':
                    passwords = input("Enter your own password\n")
                    break
                elif Your_choice_password == 'gp':
                    password = generate_passwords()
                    break
                else:
                    print("Invalid pssword please try again")
            save_credential(create_new_credential(account, usernames, passwords))
            print('\n')
            print(f"Account credential for: {account} - Username: {usernames} - Password: {passwords} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_all_account_details():
                print("Here is your accounts list: ")

                print('*' * 30)
                print('_'* 30)
                for account in display_all_account_details():
                    print(f"Account: {account.account}\nUsername: {username}\nPassword: {password} ")
                    print('-'*30)
                    print('*'*30)
            else:
                print("You have not saved any credentials ...")
        elif short_code == "fc":
            print("Enter the account name")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"Account name: {search_credential.account}")
                print('_' * 50)
                print(f"Username: {search_credential.usernames} Password: {search_credential.passwords}")
                print('_' * 50)
            else:
                print("The credential you entered doesn't exist")
                print('\n')
        elif short_code == "dc":
            print("Type account name of the credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your saved credentials for: {search_credential.account} is succesfully deleted!")
                print('\n')
            else:
                print("The credential you want to delete does not exist")
        
        elif short_code == 'gp':
            password = generate_passwords()
            print(f"{password} has been succesful generated")
        elif short_code == 'ex':
            print("Thank you for using password locker!")
            break
        else:
            print("Wrong login...")

    else:
        print("Kindly enter a valid input")

if __name__ == '__main__':
    branch()
                    