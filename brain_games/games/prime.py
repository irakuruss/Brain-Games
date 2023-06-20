from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def determine_task_and_answer():
    START_NUM = 1
    LAST_NUM = 1000
    task = randint(START_NUM, LAST_NUM)
    correct_answer = 'yes' if is_prime(task) else 'no'

    return task, correct_answer


def is_prime(task):
    if task < 2:
        return False

    divider = 1

    for i in range(1, (task // 2 + 1)):
        if task % i == 0:
            divider += 1

    if divider > 2:
        return False
    else:
        return True
