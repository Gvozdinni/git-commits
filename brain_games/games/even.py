import random

EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_check(random_num):
    if random_num % 2 == 0:
        answer = 'yes'
        return answer
    else:
        answer = 'no'
        return answer


def generate_question():
    random_num = random.randint(1, 100)
    question = f'{random_num}'
    answer = even_check(random_num)
    return question, answer
