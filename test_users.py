import pytest
import users

#test login
#test if user login successfully
def user_login():
    user_login = users.User()
    return user_login

def test_user_login():
    assert users.User('kahenyaa@gmail.com','qwerty').user_login() == "Login Successful"


#test if user login is not successfull
def user_login_not_successful():
    user_login_not_successful = users.User()
    return user_login_not_successful

def test_user_login_not_successfull():
    assert users.User('kahenyaa@gmail.com','qwerty1').user_login() == "Error Login In"



#test if user registration successful
def user_register():
    user_register = users.Create_user().create()
    return user_register

def test_user_register():
    assert users.Create_user('tuntu','kinya','testemails@gmail.com','password','+254700419377').create() == "Error creating account"



#test if user registration is not successful
def user_register_fail():
    user_register = users.Create_user().create()
    return user_register

def test_user_register_fail():
    assert users.Create_user('john','kahenya','kahenyaa@gmail.com','qwerty','+254700419377').create() == "Error creating account"

    