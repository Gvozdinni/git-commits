import random
import prompt



def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    correct_answers_count = 0
    while correct_answers_count < 3:
        start_num = random.randint(1, 3)
        step_num = random.randint(1, 3)
        random_numbers = [_ for _ in range(start_num, 20, step_num)]
        random_marker = random.randint(0, len(random_numbers) - 1)
        random_numbers[random_marker] = '..'
        numbers_string = ' '.join(map(str, random_numbers))
        print(f'What number is missing in the progression? {numbers_string}')
        user_answer = prompt.string('Your answer: ')
        answer = (random_marker) * step_num + start_num
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
