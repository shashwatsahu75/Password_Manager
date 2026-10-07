# Password Manager

## Introduction

Password Manager is a terminal-based application developed using Python. The main objective of this project is to provide a simple and secure way for users to register and log in while ensuring that their passwords are stored safely. Instead of saving passwords in plain text, the application encrypts them before storing them, making the authentication process more secure.

This project was developed as part of a Python learning assignment to understand concepts such as user authentication, password validation, encryption, file handling, and modular programming.

---

## Features

- User Registration
- User Login
- Password Strength Validation
- Secure Password Encryption
- Login Authentication
- Duplicate Username Detection
- Input Validation
- JSON-Based Data Storage
- Menu-Driven Console Interface

---

## Technologies Used

- Python 3
- JSON
- Cryptography (Fernet Encryption)
- VS Cose

---

## Project Structure

```
Password_Manager/
│
├── main.py
├── auth.py
├── encryption.py
├── strength_checker.py
├── users.json
├── secret.key
├── README.md
└── __pycache__/
```

---

## How to Run the Project

### Step 1

Download or clone the project and open it in Visual Studio Code.

### Step 2

Install the required library by running the following command in the terminal:

```bash
pip install cryptography
```

### Step 3

Run the application using:

```bash
python main.py
```

---

## Working of the Project

1. The user selects **Register** from the main menu.
2. A username and password are entered.
3. The application checks the strength of the password.
4. If the password is strong enough, it is encrypted before being stored.
5. The encrypted password is saved in the `users.json` file.
6. During login, the stored password is decrypted internally and verified with the user's input.
7. If both username and password match, the user is successfully logged in.

---

## Password Strength Criteria

A password is considered strong when it contains:

- At least 8 characters
- One uppercase letter
- One lowercase letter
- One numeric digit
- One special character

Weak passwords are rejected during registration to encourage better security.

---

## Security

This project uses the **Fernet** encryption algorithm from the **Cryptography** library.

The encryption key is automatically generated and stored in the `secret.key` file during the first execution of the project. User passwords are encrypted before being stored and are only decrypted temporarily during the login verification process.

---

## Sample Output

```
========================================
      PASSWORD MANAGER
========================================

MAIN MENU

1. Register
2. Login
3. Exit

Enter your choice:
```

---

## Learning Outcomes

While developing this project, the following Python concepts were implemented:

- Functions
- Modules
- Conditional Statements
- Loops
- File Handling
- Exception Handling
- JSON Data Handling
- Password Encryption
- User Authentication
- Modular Programming

---

## Future Scope

The project can be extended by adding features such as:

- Change Password
- Forgot Password
- Delete User Account
- Password Generator
- Graphical User Interface (GUI)
- Database Integration (SQLite/MySQL)

---

## Author

**Shashwat Sahu**

B.Tech Computer Science and Engineering

---

## Acknowledgement

This project was developed as part of a Python programming project to gain practical experience in authentication, encryption, and secure password management using Python.

---

## License

This project is intended for educational purposes only.
