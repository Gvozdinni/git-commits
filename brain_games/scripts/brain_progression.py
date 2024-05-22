#!/usr/bin/env python3
import random
import prompt
from brain_games.generate_progression import make_question


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    correct_answers_count = 0
    while correct_answers_count < 3:
        print('What number is missing in the progression?')
        print(f'Question: {make_question()}')
        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == make_question():
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was "
                  f"{make_question()}.\nLet's try again, {name}!")
            break
    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
