# 🔐 Password Strength Analyzer

A Python-based cybersecurity project that analyzes password strength using character diversity, password length, estimated entropy, common password detection, and predictable pattern detection.

## 🚀 Features

- Lowercase, uppercase, digit, and special character detection
- Character pool calculation
- Password length analysis
- Estimated entropy calculation
- Password strength classification
- Common password detection
- Repeated character detection
- Predictable sequence detection
- Security recommendations
- Hidden password input using `getpass`
- Automated unit testing using Python `unittest`

## 🛠️ Technologies Used

- Python 3
- String module
- Math module
- Getpass module
- Unittest framework

## 📁 Project Structure

```text
Password-Strength-Analyzer/
│
├── main.py
├── test_main.py
└── README.md
```

## ▶️ How to Run

1. Clone the repository:

   `git clone https://github.com/sachinsachin191207-creator/Password-Strength-Analyzer.git`

2. Open the project folder.

3. Run the analyzer:

   `python main.py`

4. Enter a sample password when prompted.

## 🧪 Automated Testing

This project uses Python's built-in `unittest` framework.

Run the test suite using:

`python -m unittest -v test_main.py`

### Test Coverage

- Empty password validation
- Common password detection
- Repeated character detection
- Predictable pattern detection
- Lowercase detection
- Uppercase detection
- Digit detection
- Special character detection
- Character pool calculation
- Password length calculation

## 📊 Entropy Calculation

The project uses the theoretical entropy formula:

`H = L × log₂(N)`

Where:

- H = Estimated entropy in bits
- L = Password length
- N = Character pool size

This is a theoretical estimate assuming randomly and independently selected characters. It does not represent the actual guessability of human-created passwords.

## 🔒 Privacy

- Password analysis is performed locally.
- The program does not intentionally transmit passwords to external services.
- Never upload real passwords or credentials to GitHub.

## 🎯 Project Objective

To understand password security concepts, Python programming, password analysis techniques, and automated software testing.

## 👨‍💻 Author

Sachin Kumar