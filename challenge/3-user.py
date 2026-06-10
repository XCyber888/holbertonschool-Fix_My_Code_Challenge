#!/usr/bin/env python3
"""
User class implementation with fixed password validation
"""

class User:
    def __init__(self):
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def is_valid_password(self, password):
        if password is None or self.__password is None:
            return False
        return self.__password == password

if __name__ == "__main__":
    user = User()
    user.password = "root"
    if not user.is_valid_password("root"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("Test User")
