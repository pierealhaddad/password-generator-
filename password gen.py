import string
import random

def generate_password():
    # Define character sets
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_chars = list(string.punctuation)

    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8 characters): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Shuffle character lists to enhance randomness
    random.shuffle(lowercase_letters)
    random.shuffle(uppercase_letters)
    random.shuffle(digits)
    random.shuffle(special_chars)

    # Allocate proportions of character types
    num_letters = round(length * 0.3)
    num_specials = round(length * 0.2)

    # Assemble the password
    password_chars = []
    for i in range(num_letters):
        password_chars.append(lowercase_letters[i])
        password_chars.append(uppercase_letters[i])
    for i in range(num_specials):
        password_chars.append(digits[i])
        password_chars.append(special_chars[i])

    # Shuffle final password characters and convert to string
    random.shuffle(password_chars)
    generated_password = "".join(password_chars)
    
    print("Generated Secure Password:", generated_password)

generate_password()
