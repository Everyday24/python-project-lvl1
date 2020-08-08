"""Знакомство."""

import prompt


def welcome_user():
    """User`s name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

extend-ignore =
# we need print() several times
WPS421
