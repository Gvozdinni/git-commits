import random


def generate_progression(start_num, step_num):
    return [_ for _ in range(start_num, 20, step_num)]


def make_question(progression):
    random_marker = random.randint(0, len(progression) - 1)
    place_marker = progression[random_marker]
    progression[random_marker] = '..'
    numbers_string = ' '.join(map(str, progression))
    return (numbers_string,
            place_marker)
