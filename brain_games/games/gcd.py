from random import randint
from math import gcd


game_rules = 'Find the greatest common divisor of given numbers.'


def determine_num_and_answer():
    num1, num2 = randint(1, 100), randint(1, 100)

    correct_answer = gcd(num1, num2)

    nums = str(num1) + ' ' + str(num2)
    return nums, str(correct_answer)
