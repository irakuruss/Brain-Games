from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUM = 1
LAST_NUM = 1000


def determine_task_and_answer():
    task = randint(START_NUM, LAST_NUM)
    correct_answer = 'yes' if is_prime(task) else 'no'
    return task, correct_answer


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1

    return True
