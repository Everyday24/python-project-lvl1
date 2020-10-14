"""Игра 5. Простое ли число?"""


import random
from brain_games.games import logic


def generate_question_answer_pair_prime():
    num = random.randint(2, 100)
    for i in range(2, num):
        if num % i == 0:
            ans = "no"
            break
        else:
            ans = "yes"
    fun = str(num)
    return fun, ans


def prime():
    logic.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    logic.run_game(generate_question_answer_pair_prime)
