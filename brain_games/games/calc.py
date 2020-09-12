"""Игра 2. Калькулятор."""


from brain_games.games import logic
from brain_games.games import calc_fun


def calc():
    logic.greeting()
    print('What is the result of the expression?\n')
    logic.run_game(calc_fun.generate_question_answer_pair_calc())
