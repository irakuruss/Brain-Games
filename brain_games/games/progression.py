from random import randint


game_rules = 'What number is missing in the progression?'


def determine_num_and_answer():
    step = randint(1, 50)
    first_num = randint(1, 100)
    sequence_length = randint(5, 9)
    missing_position = randint(5, sequence_length)
    subsequence = []
    i = first_num
    for _ in range(sequence_length):
        subsequence.append(i)
        i += step
    missing_num = subsequence.pop(missing_position-1)
    subsequence.insert(missing_position-1, '..')
    nums = ''
    for i in range(sequence_length):
        nums += str(subsequence[i]) + ' '
    nums = nums.strip()
    return nums, str(missing_num)
