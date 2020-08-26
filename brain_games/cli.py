"""Знакомство."""

import prompt


def welcome_user():
    """
    Имя пользователя.

    Returns:
        name.
        """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
