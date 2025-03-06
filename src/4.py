import random

def get_random_python_code():
    """Returns a random Python code snippet."""
    codes = ["print('Hello, world!')", "x = 5", "if x > 3: print('x is greater than 3')", "else: print('x is not greater than 3')"]
    return random.choice(codes)
