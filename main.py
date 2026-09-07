from operator import add


def greet (name):
    print(f"Hello, {name}!")

def add (a, b):
    """Adds and returns the value of a and b."""
    return a + b

def subtract (a, b):
    """Subtracts and returns the value of b from a."""
    return a - b

greet ("World")
print(f"5 + 3 = {add(5, 3)}")
print(f"5 - 3 = {subtract(5, 3)}")
