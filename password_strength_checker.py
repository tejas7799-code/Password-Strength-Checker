import tkinter as tk
from tkinter import messagebox
import re


def check_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

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

    strength_label.config(text=f"Password Strength: {strength}")

    if suggestions:
        suggestion_text = "\n".join("• " + item for item in suggestions)
    else:
        suggestion_text = (
            "Excellent! Your password meets all the basic requirements."
        )

    suggestions_label.config(text=suggestion_text)


def clear_password():
    password_entry.delete(0, tk.END)
    strength_label.config(text="Password Strength: ")
    suggestions_label.config(text="")


# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x450")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=25)

# Description
description_label = tk.Label(
    root,
    text="Enter a password to check its strength",
    font=("Arial", 12)
)
description_label.pack(pady=5)

# Password input
password_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 14),
    show="*"
)
password_entry.pack(pady=20)

# Check button
check_button = tk.Button(
    root,
    text="Check Password",
    font=("Arial", 12, "bold"),
    command=check_password,
    width=18
)
check_button.pack(pady=5)

# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11),
    command=clear_password,
    width=12
)
clear_button.pack(pady=5)

# Strength result
strength_label = tk.Label(
    root,
    text="Password Strength: ",
    font=("Arial", 16, "bold")
)
strength_label.pack(pady=20)

# Suggestions
suggestions_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left",
    wraplength=500
)
suggestions_label.pack(pady=10)

# Footer
footer_label = tk.Label(
    root,
    text="Basic Password Security Assessment Tool",
    font=("Arial", 9)
)
footer_label.pack(side="bottom", pady=15)

# Start application
root.mainloop()
