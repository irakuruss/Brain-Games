import prompt


ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULES)
    for _ in range(ROUNDS):
        task, correct_answer = game.determine_task_and_answer()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            continue
        game_over(answer, correct_answer, user_name)
        break
    else:
        print(f'Congratulations, {user_name}!')


def game_over(answer, correct_answer, user_name):
    print(f"'{answer}' is wrong answer ;(. Correct "
          f"answer was '{correct_answer}'")
    print(f"Let's try again, {user_name}!")
