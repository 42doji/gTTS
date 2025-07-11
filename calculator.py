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
    for character in string:
        if is_operator(character, ops) == True:
            count += 1
            op = character
    if count != 1:
        raise ValueError

def get_op(characters , ops) -> str:
    for character in characters:
        for op in ops:
            if op == character:
                return op

def calc(numA, numB, op):
    if op == '+':
        return add(numA, numB)
    if op == '-':
        return subtract(numA, numB)
    if op == '/':
        return devide(numA, numB)
    if op == '*':
        return multiply(numA, numB)

if __name__ == "__main__":
    ops = "+-*/"
    expression = input("Enter expression: ")
    try: 
        count_ops(expression, ops)
    except ValueError:
        print("wrong number of operators")
    op = get_op(expression, ops)
    numA, numB = expression.split(op)
    res = calc(int(numA), int(numB), op)
    print(res)
    # todo: devide 0
    # todo: wrong number input
