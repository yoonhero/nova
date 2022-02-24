def add(x, y):
    return x+y


def minus(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero")
    return x / y
