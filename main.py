import random
import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


print("\n===== CYBERSECURITY TOOL =====")
print("1. Check Password Strength")
print("2. Generate Secure Password")
print("3. Exit")

print("\nINSTRUCTIONS:")
print("- Enter 1, 2 or 3 only")
print("- Password must be at least 8 characters long")

choice = input("\nEnter choice: ")

if choice == "1":
    pwd = input("Enter password (min 8 chars): ")

    if len(pwd) < 8:
        print("Error: Password must be at least 8 characters")
    else:
        print("Result:", check_password(pwd))

elif choice == "2":
    print("Generated Password:", generate_password())

elif choice == "3":
    print("Exit")

else:
    print("Invalid choice: Please enter only 1, 2 or 3")