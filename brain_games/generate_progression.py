import random


def make_question():
    start_num = random.randint(1, 3)
    step_num = random.randint(1, 3)
    random_numbers = [_ for _ in range(start_num, 20, step_num)]
    random_marker = random.randint(0, len(random_numbers) - 1)
    random_numbers[random_marker] = '..'
    numbers_string = ' '.join(map(str, random_numbers))
    answer = random_marker * step_num + start_num
    return numbers_string, answer