def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def devide(a: int, b: int) -> int:
    return a / b

def is_operator(character, ops) -> bool:
    for op in ops:
        if character == op:
            return True
    return False

def count_ops(string: str, ops):
    count = 0
    string = string.split()
    nums = [arg for arg in string if arg.isnumeric() == True]
    if len(nums) != 2:
        raise ValueError
    elses = [arg for arg in string if arg.isnumeric() == False]
    for el in elses:
        if is_operator(el, ops) == True:
            count += 1
            op = el
    if count != 1:
        raise ValueError

def get_op(string , ops) -> str:
    string = string.split()
    nums = [arg for arg in string if arg.isnumeric() == True]
    if len(nums) != 2:
        raise ValueError
    elses = [arg for arg in string if arg.isnumeric() == False]
    for el in elses:
        if is_operator(el, ops) == True:
            return el

def calc(numA, numB, op):
    if op == '+':
        return add(numA, numB)
    if op == '-':
        return subtract(numA, numB)
    if op == '/':
        return devide(numA, numB)
    if op == '*':
        return multiply(numA, numB)

def is_devided_by_zero(a: int, b: int, op):
    if b == 0:
        if op == '/':
            raise ValueError

def main(expression, ops):
    try: 
        count_ops(expression, ops)
    except ValueError:
        print("Invalid operator.")
        exit()
    op = get_op(expression, ops)
    expression = expression.split()
    args = [el for el in expression if is_operator(el, ops) == False]
    numA, numB = args
    try:
        is_devided_by_zero(int(numA), int(numB), op)
    except ValueError:
        print("Error: Division by zero.")
        exit()
    res = calc(int(numA), int(numB), op)
    print(res)

if __name__ == "__main__":
    ops = "+-*/"
    numbers = input("Enter number: ")
    op = input("Enter operator: ")
    main(numbers + " " + op, ops)
    expression = input("Enter expression: ")
    main(expression, ops)
