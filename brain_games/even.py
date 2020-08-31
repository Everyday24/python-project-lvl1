"""Игра 1. Проверка на четность. Логика."""

import prompt
import random


def ask_question(question):
    user_answer = prompt.string(question)
    return user_answer


def generate_question_answer_pair():
    num = random.randint(0, 100)
    ans = "yes" if num % 2 == 0 else "no"
    return str(num), ans


def run_game():
    name = ask_question('May I have your name? ')
    print('Hello, {0}!\n'.format(name))

    for i in range(3):
        question, correct_answer = generate_question_answer_pair()
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
