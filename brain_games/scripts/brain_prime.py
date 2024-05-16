
from brain_games.R import R
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count < 3:
        random_num = random.randint(1, 107)
        print(f'Question: {random_num}')
        array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61, 71, 73, 79, 83, 89, 97, 101, 103, 107,]
        answer = R(random_num, array)
        user_answer = prompt.string('Your answer: ')
        if user_answer == 'yes':
            right_answer = 'no'
        elif user_answer == 'no':
            right_answer = 'yes'

        if (answer == True and user_answer == 'yes') or (answer == False and user_answer == 'no'):
            print('Correct!')
            correct_answers_count += 1
        else:
            correct_answers_count = 0
            print(f"{user_answer} is wrong answer ;(. Correct answer was {right_answer}.\nLet's try again, {name}!")

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
            main()