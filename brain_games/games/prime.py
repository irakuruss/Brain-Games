from random import randint


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def determine_num_and_answer():
    START_NUM = 1
    LAST_NUM = 1000
    num = randint(START_NUM, LAST_NUM)
    correct_answer = 'yes' if is_prime(num) else 'no'

    return num, correct_answer


def is_prime(num):
    if num < 2:
        return False

    divider = 1

    for i in range(1, (num // 2 + 1)):
        if num % i == 0:
            divider += 1

    if divider > 2:
        return False
    else:
        return True
