import random


def generate_question_answer_pair_calc():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)

    sign = random.choice('-+*')
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
