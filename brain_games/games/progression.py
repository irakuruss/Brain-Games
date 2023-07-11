from random import randint, choice


GAME_RULES = 'What number is missing in the progression?'
START_NUM = 1
LAST_NUM = 100
MIN_LENGTH = 5
MAX_LENGTH = 10


def determine_progressions_terms(start_num, last_num, min_length, max_length):
    difference = randint(start_num, last_num)
    initial_term = randint(start_num, last_num)
    progression_length = randint(min_length, max_length)
    progression = list(range(initial_term, progression_length * difference
                             + initial_term, difference))
    return progression


def determine_task_and_answer():
    progression = determine_progressions_terms(START_NUM, LAST_NUM,
                                               MIN_LENGTH, MAX_LENGTH)
    correct_answer = choice(progression)
    task = ' '.join(
        '..' if number == correct_answer else str(number)
        for number in progression
    )
    return task, str(correct_answer)
