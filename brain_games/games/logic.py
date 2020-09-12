"""Общая логика всех игр."""

import prompt


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = ask_question('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name


def ask_question(question):
    user_answer = prompt.string(question)
    return user_answer


def run_game(fun):
    name = welcome_user()

    for i in range(3):
        question, correct_answer = fun

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
