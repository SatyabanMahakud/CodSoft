import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_special=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Error! At least one character type must be selected."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def PasswordGenerator():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length (e.g., 12): "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_letters, use_digits, use_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    PasswordGenerator()
