from auth import register_user, login_user

print("=" * 40)
print("      PASSWORD MANAGER")
print("=" * 40)

while True:
    print("\nMAIN MENU")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        register_user()

    elif choice == "2":
        login_user()

    elif choice == "3":
        print("Thank you for using Password Manager.")
        break

    else:
        print("Invalid Choice! Please try again.")