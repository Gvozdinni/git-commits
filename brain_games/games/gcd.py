import random
import math

EXERCISE = 'Find the greatest common divisor of given numbers.'


def generate_question():
    ran_num1 = random.randint(1, 100)
    ran_num2 = random.randint(1, 100)
    question = f'{ran_num1} {ran_num2}'
    answer = math.gcd(ran_num2, ran_num1)
    return question, answer
