import random

EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return random_number % 2 == 0


def even_check(random_num):
    if is_even(random_num):
        return 'yes'
    else:
        return 'no'


def generate_question():
    random_num = random.randint(1, 100)
    question = f'{random_num}'
    answer = even_check(random_num)
    return question, answer
