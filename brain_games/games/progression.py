import random

EXERCISE = 'What number is missing in the progression?'


def generate_question():
    start_num = random.randint(1, 3)
    step_num = random.randint(1, 4)
    progression = [_ for _ in range(start_num, 20, step_num)]
    random_marker = random.randint(0, len(progression) - 1)
    place_marker = progression[random_marker]
    progression[random_marker] = '..'
    numbers_string = ' '.join(map(str, progression))
    question = f'{numbers_string}'
    answer = place_marker
    return question, answer
