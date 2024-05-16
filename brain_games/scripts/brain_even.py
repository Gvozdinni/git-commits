import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        random_num = random.randint(1, 100)
        print(f'Question: {random_num}')
        user_answer = prompt.string('Your answer: ')

        if random_num % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        if user_answer == answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}."
                  f"\nLet's try again, {name}!")
            break
    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
