import secrets
import string

def get_user_input():
    """Handles user input and validation."""
    while True:
        try:
            length = int(input("Enter desired password length (min 8): "))
            if length < 8:
                print("Password length should be at least 8 characters for security.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nSelect character types:")
    print("1. Uppercase Letters (A-Z)")
    print("2. Lowercase Letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$%^&*)")
    
    choices = []
    while len(choices) == 0:
        user_choice = input("Enter numbers separated by commas (e.g., 1,2,3): ")
        try:
            choices = [int(x.strip()) for x in user_choice.split(',')]
            valid_choices = {1, 2, 3, 4}
            if not all(c in valid_choices for c in choices):
                print("Invalid selection. Please choose from 1-4.")
                choices = []
        except ValueError:
            print("Invalid input format.")

    return length, choices

def generate_password(length, choices):
    """Generates the password based on choices."""
    char_pool = ""
    
    if 1 in choices:
        char_pool += string.ascii_uppercase
    if 2 in choices:
        char_pool += string.ascii_lowercase
    if 3 in choices:
        char_pool += string.digits
    if 4 in choices:
        char_pool += string.punctuation

    # Ensure at least one character from each selected type is included
    password = []
    if 1 in choices:
        password.append(secrets.choice(string.ascii_uppercase))
    if 2 in choices:
        password.append(secrets.choice(string.ascii_lowercase))
    if 3 in choices:
        password.append(secrets.choice(string.digits))
    if 4 in choices:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest of the length with random characters from the pool
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(char_pool))

    # Shuffle the list to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)

def main():
    print("--- Secure Password Generator ---")
    length, choices = get_user_input()
    password = generate_password(length, choices)
    print(f"\nGenerated Password: {password}")
    print("Stay safe!")

if __name__ == "__main__":
    main()