import random

EXERCISE = 'What number is missing in the progression?'


def generate_question():
    progression, random_marker, answer = random_progression()
    progression[random_marker] = '..'
    numbers_string = ' '.join(map(str, progression))
    question = f'{numbers_string}'
    return question, answer


def random_progression():
    start_num = random.randint(1, 3)
    step_num = random.randint(1, 4)
    progression = [_ for _ in range(start_num, 20, step_num)]
    random_marker = random.randint(0, len(progression) - 1)
    answer = progression[random_marker]
    return progression, random_marker, answer