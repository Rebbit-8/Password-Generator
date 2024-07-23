import random
import string
import time

print("Welcome To Password Generator")
time.sleep(1)
print("Please answer the following question")
time.sleep(1)
try:
    character = int(input("How many digits do you want your password to have? "))
except ValueError:
    print("Please enter a number")
    time.sleep(1)
    character = int(input("How many digits do you want your password to have? "))
time.sleep(1)
print("Your password is ",character," digits long")
time.sleep(1)
print("""Please answer the following questions with options 1 or 2
1 = True
2 = False""")
time.sleep(1)
uppercase_A = int(input("How many uppercase letters do you want your password to have? "))
if uppercase_A == 1:
    uppercase = True
    print("Your password is uppercase")
elif uppercase_A == 2:
    uppercase = False
    print("Your password is not  uppercase")
elif uppercase_A is not 1 or 2:
    print("Please enter to 1 or 2")
time.sleep(1)
lowercase_A = int(input("How many lowercase letters do you want your password to have? "))
if lowercase_A == 1:
    lowercase = True
    print("Your password is lowercase")
elif lowercase_A == 2:
    lowercase = False
    print("Your password is not  lowercase")
elif lowercase_A is not 1 or 2:
    print("Please enter to 1 or 2")
time.sleep(1)
digits_A = int(input("How many digits do you want your password to have? "))
if digits_A == 1:
    digits = True
    print("Your password is digits")
elif digits_A == 2:
    digits = False
    print("Your password is not  digits")
elif digits_A is not 1 or 2:
    print("Please enter to 1 or 2")
time.sleep(1)
punctuation_A = int(input("How many punctuation do you want your password to have? "))
if punctuation_A == 1:
    punctuation = True
    print("Your password is punctuation")
elif punctuation_A == 2:
    punctuation = False
    print("Your password is not  punctuation")
elif punctuation_A is not 1 or 2:
    print("Please enter to 1 or 2")
time.sleep(1)

print("Generating password")

time.sleep(1)

def generate_password(length=character, use_uppercase=uppercase, use_lowercase=lowercase, use_digits=digits, use_punctuation=punctuation):
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

# Example usage:
password = generate_password(length=character, use_uppercase=uppercase, use_lowercase=lowercase, use_digits=digits, use_punctuation=punctuation)
print("Generated Password:", password)
