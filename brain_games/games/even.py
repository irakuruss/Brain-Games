from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def determine_num_and_answer():
    START_NUMBER = 1
    LAST_NUMBER = 1000
    num = randint(START_NUMBER, LAST_NUMBER)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
