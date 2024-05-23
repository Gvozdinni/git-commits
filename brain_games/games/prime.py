import random

EXERCISE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    random_num = random.randint(1, 108)
    question = f'{random_num}'
    answer = checkout_answer(random_num)
    return question, answer


def generate_prime_number(random_num):
    prime_num_array = [2, 3, 5, 7, 11, 13, 17, 19, 23,
                       29, 31, 37, 41, 43, 47, 53, 61,
                       71, 73, 79, 83, 89, 97, 101, 103, 107, ]
    return random_num in prime_num_array


def checkout_answer(random_num):
    if generate_prime_number(random_num) is True:
        return 'yes'
    elif generate_prime_number(random_num) is False:
        return 'no'
