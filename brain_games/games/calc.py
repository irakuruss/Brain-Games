from random import randint


game_rules = 'What is the result of the expression?'


def determine_num_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
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
