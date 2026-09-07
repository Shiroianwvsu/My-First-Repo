from operator import add


def greet (name):
    print(f"Hello, {name}!")

def add (a, b):
    """ Adds and returns the value of a and b."""
    return a + b

greet ("World")
print(f"5 + 3 = {add(5, 3)}")
