import operator
import random

EXERCISE = 'What is the result of the expression?'


def express_result(random_num1, random_num2, random_sign):
    match random_sign:
        case '+':
            answer = operator.add(random_num1, random_num2)
        case '-':
            answer = operator.sub(random_num1, random_num2)
        case '*':
            answer = operator.mul(random_num1, random_num2)
    return answer


def generate_question():
    random_num1 = random.randint(30, 99)
    random_num2 = random.randint(1, 30)
    random_sign = random.choice(['+', '-', '*'])
    question = f'{random_num1} {random_sign} {random_num2}'
    answer = express_result(random_num1, random_num2, random_sign)
    return question, answer
