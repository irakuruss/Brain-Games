from random import randint


game_rules = 'What is the result of the expression?'


def determine_num_and_answer():
    START_NUM = 1
    LAST_NUM = 100
    num1 = randint(START_NUM, LAST_NUM)
    num2 = randint(START_NUM, LAST_NUM)
    math_operations = ['+', '-', '*']
    operation = math_operations[randint(0, 2)]
    num = str(num1) + ' ' + str(operation) + ' ' + str(num2)
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    return num, str(correct_answer)
