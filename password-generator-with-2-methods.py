import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
#****************************************************
# 1st METHOD: SIMPLE + FAST (uses random.choices)
# - Picks multiple items at once
#****************************************************
random_letters = random.choices(letters, k=nr_letters)
random_numbers = random.choices(numbers, k=nr_numbers)
random_symbols = random.choices(symbols, k=nr_symbols)

password = random_letters + random_numbers + random_symbols
print("1st ")
print(f"Easy password: {''.join(password)}")
random.shuffle(password)
print(f"Hard password: {''.join(password)}")

print("-----------------------------------------------")
print("2nd ")
#****************************************************
# 2nd METHOD: STEP-BY-STEP CONTROL (uses loops)
# - Builds password character by character
#****************************************************characters_sum = nr_letters + nr_numbers + nr_symbols

characters_sum = nr_letters + nr_numbers + nr_symbols

if characters_sum < 12:
    print("This password is too weak.")
else:
    password = []

    for _ in range(nr_letters):
        password.append(random.choice(letters))

    for _ in range(nr_numbers):
        password.append(random.choice(numbers))

    for _ in range(nr_symbols):
        password.append(random.choice(symbols))

    random.shuffle(password)

    str_password = "".join(password)
    password_len = len(str_password)

    print(f"{password_len} characters, secure password:")
    print(str_password)
