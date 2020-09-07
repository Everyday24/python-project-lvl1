"""Игра 1. Проверка на четность. Логика."""

import prompt
import random


def greeting():
    print('Welcome to the Brain Games!')

def welcome_user():
    name = ask_question('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name

def ask_question(question):
    user_answer = prompt.string(question)
    return user_answer


def generate_question_answer_pair():
    num = random.randint(0, 100)
    ans = "yes" if num % 2 == 0 else "no"
    fun = str(num)
    return fun, ans

def generate_question_answer_pair_calc():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)

    simb = random.choice('-+*')
    if simb == '+':
        correct_answer = num_1 + num_2
        question = f'{num_1} + {num_2}'
    elif simb == '-':
        correct_answer = num_1 - num_2
        question = f'{num_1} - {num_2}'
    else:
        correct_answer = num_1 * num_2
        question = f'{num_1} * {num_2}'

    correct_answer = str(correct_answer)

    return question, correct_answer


def calc():
    greeting()
    print('What is the result of the expression?\n')
    run_game()

def even():
    greeting()
    print('Answer "yes" if number even otherwise answer "no".\n')
    run_game()

def run_game():
    name = welcome_user()

    for i in range(3):
        question, correct_answer = generate_question_answer_pair_calc()

        question = f"Question: {question}\nYour answer: "
        user_answer = ask_question(question)
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
