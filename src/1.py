import random

def get_random_code():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', ',', '.', '<', '>']
    password_length = 10
    password = ''
    for i in range(password_length):
        password += random.choice(numbers)
        password += random.choice(characters)
        password += random.choice(symbols)
    return password