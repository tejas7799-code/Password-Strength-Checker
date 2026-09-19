# Password Strength Checker

## Intern Details

| Field | Details |
|---|---|
| **Intern ID** | CITS8842 |
| **Full Name** | KOLA TEJAS |
| **No. of Weeks** | 8 Weeks |
| **Project Name** | Password Strength Checker |
| **Project Scope** | A Python-based cybersecurity tool that evaluates password strength using length, uppercase letters, lowercase letters, numbers, and special characters, and provides suggestions for creating stronger passwords. |

---

## Project Overview

Password Strength Checker is a basic cybersecurity project developed using Python.

The application evaluates a password based on common password security requirements such as:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Based on these criteria, the application calculates a strength score and classifies the password as **Weak, Medium, or Strong**.

The application also provides suggestions to help users improve the security of weak passwords.

---

## Objectives

The main objectives of this project are:

- To check the strength of a password.
- To identify basic password security requirements.
- To evaluate password length and character types.
- To provide suggestions for creating stronger passwords.
- To demonstrate basic Python programming concepts.
- To demonstrate basic cybersecurity concepts.

---

## Features

The Password Strength Checker provides the following features:

- Password length validation
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Password strength scoring
- Weak, Medium, and Strong classification
- Suggestions for improving password security
- Simple console-based interface

---

## Technologies Used

- **Python 3**
- **Regular Expressions (`re`)**
- **GitHub**

The project uses Python's built-in `re` module and does not require any external Python packages.

---

## Password Strength Criteria

The application checks the following criteria:

| Criteria | Description |
|---|---|
| Length | Checks whether the password contains at least 8 characters |
| Uppercase | Checks for at least one uppercase letter |
| Lowercase | Checks for at least one lowercase letter |
| Number | Checks for at least one numeric character |
| Special Character | Checks for at least one special character |

The score is calculated based on the number of security criteria satisfied.

---

## How the Program Works

1. The user enters a password.
2. The program checks the password length.
3. It checks for uppercase letters.
4. It checks for lowercase letters.
5. It checks for numbers.
6. It checks for special characters.
7. A score is calculated based on the satisfied criteria.
8. The password is classified as Weak, Medium, or Strong.
9. Suggestions are displayed when security requirements are missing.

---

## How to Run

### Option 1: Run on Your Computer

1. Install **Python 3.x**.
2. Download or clone this repository.
3. Open a terminal or command prompt inside the project folder.
4. Run the following command:


### Option 2: Run Using an Online Python Compiler

The project can also be tested using an online Python compiler without installing Python.

#### Steps:

1. Open an online Python compiler such as **Programiz, OnlineGDB, or Replit**.
2. Open `password_strength_checker.py` from this GitHub repository.
3. Copy the complete Python source code.
4. Paste the code into the online Python editor.
5. Click the **Run** button.
6. Enter a password when prompted.
7. The program will display the password strength and improvement suggestions.

No external packages need to be installed because the project uses Python's built-in `re` module.


```bash
python password_strength_checker.py
