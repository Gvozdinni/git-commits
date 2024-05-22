#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    correct_answers_count = 0
    while correct_answers_count < 3:
        random_num1 = random.randint(30, 99)
        random_num2 = random.randint(1, 30)
        random_sign = random.choice(['+', '-', '*'])
        print(f'Question: {random_num1} {random_sign} {random_num2}')
        user_answer = prompt.string('Your answer: ')
        match random_sign:
            case '+':
                answer = random_num1 + random_num2
            case '-':
                answer = random_num1 - random_num2
            case '*':
                answer = random_num1 * random_num2
        if int(user_answer) == answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was "
                  f"{answer}.\nLet's try again, {name}!")
            break

    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
