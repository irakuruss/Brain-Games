import prompt


attemps = 3


def structure(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.game_rules)
    for _ in range(attemps):
        num, correct_answer = game.determine_num_and_answer()
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            continue
        game_over(answer, correct_answer, user_name)
        break
    else:
        print(f'Congratulations, {user_name}!')


def game_over(answer, correct_answer, user_name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
    print(f"Let's try again, {user_name}!")

