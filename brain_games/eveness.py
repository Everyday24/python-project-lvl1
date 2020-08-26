"""Игра 1. Логика."""

from random import randint

import prompt

from brain_games import cli


def is_even():
    """Проверка на четность."""
    name = cli.welcome_user()
    counter = 0
    while counter < 3:
        num = randint(0, 100)
        print('Question: {0}'.format(num))
        if num % 2 == 0:
            cor_ans = 'yes'
        else:
            cor_ans = 'no'
        u_ans = prompt.string('Your answer: ')
        if u_ans == cor_ans:
            print('Correct!')
            counter += 1
        else:
            print("'{0}' is wrong answer ;(. Correct \
                  answer was '{1}'".format(u_ans, cor_ans))
            print("Let's try again, {0}!".format(name))
    print('Congratulations, {0}!'.format(name))
