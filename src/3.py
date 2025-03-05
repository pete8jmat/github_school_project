import random

def get_random_code():
    return "".join(str(random.randint(0, 9)) for i in range(6))

get_random_code()
