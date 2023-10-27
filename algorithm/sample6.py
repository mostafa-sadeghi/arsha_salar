# def is_even(number):
#     if number % 2 == 0:
#         return "Yes, is even"
#     else:
#         return "No, is Odd"

# print(is_even(43))
import random
import pyperclip
# pyperclip.copy("salaam, chetori?")
import string
# LOWER_CASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARS = '!@#$%*&_'
def generate_password(site_name, length):
    if length < 8:
        length = 8
    password = []
    password.append(random.choice(LOWERCASE_LETTERS))
    password.append(random.choice(UPPERCASE_LETTERS))
    password.append(random.choice(DIGITS))
    password.append(random.choice(SPECIAL_CHARS))
    random.shuffle(password)
    password = "".join(password)
    pyperclip.copy(password)
    return password
print(generate_password("",12))