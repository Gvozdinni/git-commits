import random
import prompt
import math


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    correct_answers_count = 0
    while correct_answers_count < 3:
        ran_num1 = random.randint(1, 100)
        ran_num2 = random.randint(1, 100)
        print(f'Question: {ran_num1} {ran_num2} ')
        user_answer = prompt.string('Your answer: ')
        answer = math.gcd(ran_num2, ran_num1)
        if int(user_answer) == answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\nLet's try again, {name}!")
            break
    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

