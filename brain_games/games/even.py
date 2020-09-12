"""Игра 1. Проверка на четность."""


import random
from brain_games.games import logic


def generate_question_answer_pair():
    num = random.randint(0, 100)
    ans = "yes" if num % 2 == 0 else "no"
    fun = str(num)
    return fun, ans


def even():
    logic.greeting()
    print('Answer "yes" if number even otherwise answer "no".\n')
    logic.run_game(generate_question_answer_pair)
