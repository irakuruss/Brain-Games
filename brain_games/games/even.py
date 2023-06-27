from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUMBER = 1
LAST_NUMBER = 1000


def determine_task_and_answer():
    task = randint(START_NUMBER, LAST_NUMBER)
    correct_answer = 'yes' if is_even(task) else 'no'
    return task, correct_answer


def is_even(task):
    return task % 2 == 0
