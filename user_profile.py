"""
This module contains classes to help represent the user profile in the system.
"""
import datetime

class Profile(object):
    def __init__(self, name, birthdate_string):
        """

        :param name: the user's name
        :param birthdate_string: in a %d/%m/%Y format
        """
        self.name = name
        self.birthdate = datetime.datetime.strptime(birthdate_string, '%d/%m/%Y')

    def format_password(self, password_template):
        """
        creates a password based on the template provided using the user information.

        :param password_template: a string to be formatted into password.
        :return: the formatted password.
        """

        return '%'.join(
            [self.birthdate.strftime(part).format(**self.__dict__) for part in password_template.split('\%')]
        )
