from random import randint


GAME_RULES = 'What is the result of the expression?'


def determine_task_and_answer():
    START_NUM = 1
    LAST_NUM = 100
    num1 = randint(START_NUM, LAST_NUM)
    num2 = randint(START_NUM, LAST_NUM)
    math_operations = ['+', '-', '*']
    operation = math_operations[randint(0, len(math_operations) - 1]
    task = str(num1) + ' ' + str(operation) + ' ' + str(num2)
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    return task, str(correct_answer)
