# 🔐 Password Strength & Breach Checker

A powerful Python desktop tool with a modern GUI that evaluates password strength and checks for potential exposure in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3). Built with **Tkinter**, **Python**, and **Requests**, it's perfect for enhancing personal or organizational password hygiene.

---

## 📌 Features

- 🔍 **Password Strength Analysis**
  - Checks for length, uppercase/lowercase, numbers, symbols, and common dictionary words.
  - Grades strength from **Very Weak** to **Very Strong**.

- 🛡️ **Breach Check via Pwned API**
  - Checks if your password has been compromised in past data breaches.
  - Uses SHA1 hashing for secure API queries (only the hash prefix is sent).

- 💡 **Smart Suggestions**
  - Gives you actionable tips to improve weak passwords.

- 🖥️ **Modern GUI**
  - Built with Tkinter, styled for simplicity and clarity.

- 📦 **Modular Codebase**
  - `password_checker.py`, `pwned_checker.py`, and `password_gui.py` separate concerns.


## 🧑‍💻 About Me

Hi, I'm **Ali Haider** — a Python developer passionate about cybersecurity and automation.  
I'm currently building useful tools like this to help people improve their digital safety.

- 🧠 Focus: Python, WordPress, Web Dev, Cybersecurity
- 🌍 From: Bahawalpur, Punjab, Pakistan
- 🔗 GitHub: [chhadi05](https://github.com/chhadi05)

---

## 📁 Project Structure

password-strength-checker/
│
├── password_checker.py # Logic for strength evaluation
├── pwned_checker.py # Checks against data breaches
├── password_gui.py # User interface
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 💻 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chhadi05/password-strength-checker.git
cd password-strength-checker

## 2️⃣ Install Dependencies

## Install the required Python libraries:

pip install -r requirements.txt

## Or manually install:

pip install requests

## 3️⃣ Run the App

python password_gui.py


## Let me know if you want me to:

- Add a **GitHub Pages site** for this project  
- Generate a `.exe` file with **PyInstaller**  
- Help you create a dark-mode version of the GUI

I'm here to help!




