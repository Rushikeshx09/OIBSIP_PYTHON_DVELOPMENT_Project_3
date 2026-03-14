# 🔐 Password Generator (Beginner + Advanced)

A **secure password generator built with Python** that creates strong and random passwords based on user-defined criteria.

This project contains **two versions**:

1. **Beginner Version** – Command-Line Password Generator
2. **Advanced Version** – GUI Password Generator with password strength checker and clipboard support

The project demonstrates **secure random generation, input validation, GUI development, and password strength analysis**.

---

# 📌 Project Overview

## 🟢 Beginner Version – Command-Line Password Generator

This version runs in the **terminal** and allows users to generate secure passwords by selecting the desired character types.

### Features

* User-defined password length
* Choose character types:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Ensures at least one character from each selected category
* Uses **Python's `secrets` module** for cryptographically secure random generation
* Input validation for better user experience

---

## 🔵 Advanced Version – GUI Password Generator

The advanced version provides a **Graphical User Interface (GUI)** using **Tkinter** with additional functionality.

### Features

* Interactive GUI
* Password length slider
* Select character types (uppercase, lowercase, digits, symbols)
* Option to **exclude specific characters**
* Password strength indicator (Weak / Medium / Strong)
* Copy password to clipboard
* Secure password generation
* User-friendly interface

---

# 🛠️ Technologies Used

* **Python**
* **Tkinter** – GUI development
* **secrets module** – secure random password generation
* **string module** – character sets
* **clipboard API (Tkinter)**

---

# 📂 Project Structure

```
Password-Generator/
│
├── password_generator_cli.py
├── password_generator_gui.py
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/password-generator.git
```

### 2️⃣ Open the Project Folder

```
cd password-generator
```

No external libraries are required. The project uses **built-in Python modules**.

---

# ▶️ Usage

## Run Beginner Version

```
python password_generator_cli.py
```

Steps:

1. Enter desired password length
2. Select character types
3. The program generates a **secure random password**

Example Output:

```
Generated Password: aB3$kL9!pQ
```

---

## Run Advanced GUI Version

```
python password_generator_gui.py
```

Features available in the GUI:

* Adjust password length using slider
* Select character types
* Exclude specific characters
* Generate password
* Check password strength
* Copy password to clipboard

---

# 🔐 Security Features

* Uses **Python's `secrets` module** for cryptographically secure randomness
* Ensures passwords include characters from selected categories
* Random shuffling prevents predictable patterns

---

# 🧠 Key Concepts Implemented

### Secure Random Generation

The project uses the **`secrets` module**, which is recommended for generating strong passwords.

### Input Validation

Ensures users provide valid password length and character selections.

### GUI Programming

The advanced version demonstrates building **desktop applications using Tkinter**.

### Password Strength Analysis

Analyzes generated passwords based on:

* Length
* Character diversity
* Presence of symbols and numbers

---

# 🚀 Future Improvements

* Add **password history**
* Add **password saving with encryption**
* Add **dark mode UI**
* Add **QR code sharing for passwords**
* Add **password entropy calculation**

---

# 🤝 Contribution

Contributions are welcome!
Feel free to fork the repository and submit pull requests.

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Rushikesh Basaveshwar Swami

Python Developer | Learning Cybersecurity, Automation, and Software Development
