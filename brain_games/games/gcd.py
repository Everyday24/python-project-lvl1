"""Игра 3. Наибольший общий делитель."""


import math
import random
from brain_games.games import logic


def random_ex():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    return num_1, num_2


def generate_question_answer_pair_gcd():
    num_1, num_2 = random_ex()
    question = f"{num_1} {num_2}"
    correct_answer = math.gcd(num_1, num_2)
    correct_answer = str(correct_answer)
    return question, correct_answer


def gcd():
    logic.greeting()
    print('Find the greatest common divisor of given numbers.\n')
    logic.run_game(generate_question_answer_pair_gcd)
