import random
import string
import time

print("Welcome To Password Generator")
time.sleep(1)
print("Please answer the following question")
time.sleep(1)

while True:
    try:
        character = int(input("How many digits do you want your password to have? "))
        break
    except ValueError:
        print("Please enter a valid number")

time.sleep(1)
print("Your password is", character, "digits long")
time.sleep(1)

def get_boolean_input(prompt):
    while True:
        response = input(prompt + " (1 for True, 2 for False): ")
        if response == '1':
            return True
        elif response == '2':
            return False
        else:
            print("Invalid input. Please enter 1 or 2.")

uppercase = get_boolean_input("Do you want uppercase letters in your password?")
lowercase = get_boolean_input("Do you want lowercase letters in your password?")
digits = get_boolean_input("Do you want digits in your password?")
punctuation = get_boolean_input("Do you want punctuation in your password?")

time.sleep(1)
print("Generating password")
time.sleep(1)

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_punctuation:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one type of characters must be selected")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

password = generate_password(length=character, use_uppercase=uppercase, use_lowercase=lowercase, use_digits=digits, use_punctuation=punctuation)
print("Generated Password:", password)
