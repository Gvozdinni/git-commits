import random
import prompt



def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    correct_answers_count = 0
    while correct_answers_count < 3:
        start_num = random.randint(1, 10)
        step_num = random.randint(2, 5)
        random_numbers = [_ for _ in range(start_num, 20, step_num)]
        random_numbers[2] = '..'
        print(f'What number is missing in the progression? {random_numbers}')
        user_answer = prompt.string('Your answer: ')
        answer = 2 * step_num + start_num
        if int(user_answer) == answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            correct_answers_count = 0
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}.\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
