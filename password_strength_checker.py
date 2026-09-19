import re


def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, suggestions


print("=" * 45)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 45)

password = input("Enter your password: ")

strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions to improve your password:")

    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nExcellent!")
    print("Your password meets all the basic requirements.")

print("\n" + "=" * 45)
print("Basic Password Security Assessment Tool")
print("=" * 45)
