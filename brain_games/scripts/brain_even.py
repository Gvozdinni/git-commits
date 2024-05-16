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
        if random_num % 2 == 0 and user_answer == 'yes':
            answer = 'yes'
        elif random_num % 2 != 0 and user_answer == 'no':
            answer = 'no'

        if user_answer == answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\nLet's try again, {name}!")

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()





