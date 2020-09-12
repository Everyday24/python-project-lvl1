"""Игра 2. Калькулятор."""


import random
from brain_games.games import logic


def random_ex():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    sign = random.choice('-+*')
    return num_1, num_2, sign


def generate_question_answer_pair_calc():
    num_1, num_2, sign = random_ex()
    if sign == '+':
        correct_answer = num_1 + num_2
        question = f'{num_1} + {num_2}'
    elif sign == '-':
        correct_answer = num_1 - num_2
        question = f'{num_1} - {num_2}'
    else:
        correct_answer = num_1 * num_2
        question = f'{num_1} * {num_2}'

    correct_answer = str(correct_answer)

    return question, correct_answer


def calc():
    logic.greeting()
    print('What is the result of the expression?\n')
    logic.run_game(generate_question_answer_pair_calc)
