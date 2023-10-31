import random
import string
def generate_password(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters)
    for _ in range(length))
    return password

def password_generator():
    length = int(input("Enter the desired length of the password: "))

    if length > 0:
        password = generate_password(length)
        print(f"Generated Password: {password}")
    else:
        print("Invalid length. Please enter a positive integer.")
password_generator()