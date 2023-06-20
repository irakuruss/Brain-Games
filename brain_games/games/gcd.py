from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def determine_num_and_answer():
    START_NUM = 1
    LAST_NUM = 100
    num1 = randint(START_NUM, LAST_NUM)
    num2 = randint(START_NUM, LAST_NUM)

    correct_answer = gcd(num1, num2)

    nums = str(num1) + ' ' + str(num2)
    return nums, str(correct_answer)
