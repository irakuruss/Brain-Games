from random import randint


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def determine_num_and_answer():
    num = randint(1, 1000)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return num, correct_answer

