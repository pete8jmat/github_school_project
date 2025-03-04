def get_random_code():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_']

    code = ''

    for i in range(10):
        code += random.choice(letters)
        code += random.choice(numbers)
        code += random.choice(special_chars)

    return code
