# 🔐 Password Strength Analyzer

A Python-based cybersecurity project that analyzes password strength using character diversity, password length, estimated entropy, and predictable pattern detection.

## 🚀 Features

- Character type detection (lowercase, uppercase, digits, special characters)
- Character pool calculation
- Password length analysis
- Estimated entropy calculation
- Password strength classification
- Common password detection
- Repeated character detection
- Predictable sequence detection
- Security recommendations
- Hidden password input using `getpass`

## 🛠️ Technologies Used

- Python 3
- String module
- Math module
- Getpass module

## ▶️ How to Run

1. Clone this repository:

   `git clone https://github.com/sachinsachin191207-creator/Password-Strength-Analyzer.git`

2. Open the project folder.

3. Run:

   `python main.py`

4. Enter a test password when prompted.

## 📊 Analysis Methods

The project uses the following theoretical entropy formula:

`H = L × log₂(N)`

Where:
- H = Estimated entropy in bits
- L = Password length
- N = Character pool size

Entropy is an estimate, not a guarantee of real-world password security. Common passwords and predictable patterns are checked separately.

## 🔒 Privacy

Password analysis is performed locally. The program does not intentionally transmit passwords to external services.

Use sample passwords for testing. Never upload real passwords or secrets to GitHub.

## 🎯 Project Purpose

This project was developed to understand password security concepts, Python programming, and basic cybersecurity practices.

## 👨‍💻 Author

Sachin Kumar