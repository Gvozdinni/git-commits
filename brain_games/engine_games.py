from brain_games import cli


def start_game(game):
    name = cli.welcome_user()
    print(game.EXERCISE)
    x = 0
    while x < 3:
        question, answer = game.generate_question()
        get_question(question)
        user_answer = get_user_answer()
        if user_answer == str(answer):
            print_correct()
            x += 1
            continue
        elif user_answer != str(answer):
            print_answer(user_answer, name, answer)
            break
    else:
        print_congratulate(name)


def get_question(x):
    print(f'Question: {x}')


def get_user_answer():
    user_answer = input('Your answer: ')
    return user_answer


def print_answer(user_answer, name, answer):
    print(f"""{user_answer} is wrong answer ;(. Correct answer was {answer}.
Let's try again, {name}!""")


def print_correct():
    print('Correct!')


def print_congratulate(name):
    print(f'Congratulations, {name}!')
