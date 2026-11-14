# 🔐 Password Strength Analyzer

A Python-based Password Strength Analyzer with an Apple-inspired, minimalist white graphical interface.

## 🚀 Features

- Password strength evaluation (0–100 score)
- Character pool and entropy calculation
- Lowercase, uppercase, digit and special character detection
- Common password detection
- Repeated character detection
- Predictable sequence and pattern detection
- Personalized improvement recommendations
- Interactive browser-based GUI
- Password visibility toggle
- Unit testing using Python `unittest`
## 📸 Application Preview

![Password Strength Analyzer](screenshots/password-Strength-Analyzer-demo(1).png)
![Password Strength Analyzer](screenshots/password-Strength-Analyzer-demo(2).png)

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Unittest

## 📁 Project Structure

```text
Password-Strength-Analyzer/
│
├── main.py
├── test_main.py
├── app.py
├── README.md
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sachinsachin191207-creator/Password-Strength-Analyzer.git
```

### 2. Open the project folder

```bash
cd Password-Strength-Analyzer
```

### 3. Install dependencies

```bash
python -m pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

Visit:

```text
http://127.0.0.1:5000
```

## 🧪 Run Unit Tests

```bash
python -m unittest -v test_main.py
```

## 🔒 Privacy Note

The application is designed to process password submissions through a local Flask server. It does not intentionally store or transmit passwords to third-party services. Use only test passwords while experimenting.

## 📊 Password Analysis

The application uses a custom educational scoring system based on password length, character diversity, estimated entropy and predictable patterns.

The score is an estimate, not a guarantee of real-world password security.

## 👨‍💻 Author

Sachin Kumar

---

⭐ If you find this project interesting, consider giving the repository a star!
