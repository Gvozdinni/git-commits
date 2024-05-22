#!/usr/bin/env python3
from brain_games.R import generate_prime_number
import random
import prompt
from brain_games.right_answer import checkout_answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count < 3:
        random_num = random.randint(1, 100000)
        print(f'Question: {random_num}')
        answer = generate_prime_number(random_num)
        user_answer = prompt.string('Your answer: ')
        right_answer = checkout_answer(user_answer)

        if (answer is True and user_answer == 'yes') or\
                (answer is False and user_answer == 'no'):
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was "
                  f"{right_answer}.\nLet's try again, {name}!")
            break
    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
