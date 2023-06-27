from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'
START_NUM = 1
LAST_NUM = 100


def determine_task_and_answer():
    num1 = randint(START_NUM, LAST_NUM)
    num2 = randint(START_NUM, LAST_NUM)

    correct_answer = gcd(num1, num2)

    task = str(num1) + ' ' + str(num2)
    return task, str(correct_answer)
