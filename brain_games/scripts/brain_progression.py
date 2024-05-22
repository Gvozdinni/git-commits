#!/usr/bin/env python3
import random
import prompt
from brain_games.generate_progression import make_question, generate_progression


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    correct_answers_count = 0
    while correct_answers_count < 3:
        start_num = random.randint(1, 3)
        step_num = random.randint(1, 3)
        progression = generate_progression(start_num, step_num)
        question, place_marker = make_question(progression)
        print('What number is missing in the progression?')
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        answer = place_marker * step_num + start_num
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
