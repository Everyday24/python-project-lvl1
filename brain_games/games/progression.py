"""Игра 4. Арифметическая прогрессия."""


import random
from brain_games.games import logic


def random_ex():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(1, 10)
    num_3 = random.randint(0, 9)
    return num_1, num_2, num_3


def generate_question_answer_pair_progression():
    start, step, n = random_ex()
    stop = start + step * 9 + 1
    b = list(range(start, stop, step))
    correct_answer = str(b[n])
    b[n] = '..'
    question = (' '.join(str(x) for x in b))
    return question, correct_answer


def progression():
    logic.greeting()
    print('What number is missing in the progression?\n')
    logic.run_game(generate_question_answer_pair_progression)
