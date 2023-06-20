from random import randint


GAME_RULES = 'What number is missing in the progression?'


def find_progressions_terms():
    START_NUM = 1
    LAST_NUM = 100
    START_PROGRESSION = 5
    END_PROGRESSION = 10
    step = randint(START_NUM, LAST_NUM)
    first_num = randint(START_NUM, LAST_NUM)
    progression_length = randint(START_PROGRESSION, END_PROGRESSION)
    missing_position = randint(START_PROGRESSION, progression_length)
    progression = []
    i = first_num
    for _ in range(progression_length):
        progression.append(str(i))
        i += step
    return progression, missing_position


def determine_task_and_answer():
    progression, missing_position = find_progressions_terms()
    missing_num = progression.pop(missing_position - 1)
    progression.insert(missing_position - 1, '..')
    progression_string = ' '.join(progression)
    return progression_string, str(missing_num)
