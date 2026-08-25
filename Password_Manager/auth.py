import json
from strength_checker import check_password_strength
from encryption import encrypt_password, decrypt_password


def register_user():
    """Register a new user."""

    username = input("Enter a username: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    password = input("Create a password: ")

    strength = check_password_strength(password)

    print(f"Password Strength: {strength}")

    if strength == "Weak":
        print("Password is too weak.")
        print("Please use at least:")
        print("- 8 characters")
        print("- One uppercase letter")
        print("- One lowercase letter")
        print("- One number")
        print("- One special character")
        return

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except:
        users = {}

    if username in users:
        print("Username already exists.")
        return

    encrypted_password = encrypt_password(password)

    users[username] = encrypted_password

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("Registration completed successfully.")


def login_user():
    """Login an existing user."""

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ")

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except:
        print("No registered users found.")
        return

    if username not in users:
        print("Login Failed!")
        print("Invalid Username or Password.")
        return

    encrypted_password = users[username]

    try:
        saved_password = decrypt_password(encrypted_password)
    except:
        print("Login Failed!")
        print("Invalid Username or Password.")
        return

    if password == saved_password:
        print("Login Successful!")
        print(f"Welcome, {username}")
    else:
        print("Login Failed!")
        print("Invalid Username or Password.")