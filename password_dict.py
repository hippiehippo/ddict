"""
Contains a list of common passwords and provides an interface to change them according to the user profile data.
"""

common_passwords = [
    '123456',
    '123456789',
    'qwerty',
    '12345678',
    '111111',
    '1234567890',
    '1234567',
    'password',
    '123123',
    '987654321',
    'qwertyuiop',
    'mynoob',
    '123321',
    '666666',
    '18atcskd2w',
    '7777777',
    '1q2w3e4r',
    '654321',
    '555555',
    '3rjs1la7qe',
    'google',
    '1q2w3e4r5t',
    '123qwe',
    'zxcvbnm',
    '1q2w3e',
    '{name}123123',
    '%d%m%Y',
    '{name}%Y',
    '\%d',
]


def GetPasswords(user):
    """
    Returns a list of passwords based on the user profile.

    :param user: user profile from which to take data
    :return: a list of password strings
    """

    return [user.format_password(template) for template in common_passwords]
