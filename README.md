# 🔐 Password Security Analyzer

### A Python-based cybersecurity portfolio project for understanding password security, hashing, entropy, salting, and brute-force search spaces.

------------------------------------------------------------------------

## 📌 About The Project

**Password Security Analyzer** is an educational cybersecurity
application built with Python.

The project demonstrates several important password-security concepts in
a safe and controlled environment. Instead of targeting real accounts or
systems, it helps users understand **why weak passwords are easier to
compromise** and how stronger password practices improve security.

The application provides tools for:

-   Password hashing
-   Password strength analysis
-   Password entropy estimation
-   Salted-hash demonstrations
-   Brute-force search-space calculations
-   Hash-performance benchmarking

> ⚠️ **Educational / Defensive Use Only**
>
> This project is intended for cybersecurity education, security
> awareness, and portfolio demonstration. It should only be used with
> passwords, hashes, and systems that you own or have explicit
> permission to test.

------------------------------------------------------------------------

## ✨ Features

### 🔑 1. Password Hash Generator

Generate cryptographic hashes from a password using supported
algorithms.

**Demonstrates:**

-   Hash functions
-   One-way transformations
-   Hash output formats
-   Differences between hashing algorithms

------------------------------------------------------------------------

### 🛡️ 2. Password Strength Analyzer

Evaluates a password using characteristics such as:

-   Password length
-   Uppercase letters
-   Lowercase letters
-   Numbers
-   Special characters
-   Common weaknesses

It provides a strength rating and suggestions for improvement.

------------------------------------------------------------------------

### 📊 3. Brute-Force Search Space Calculator

Calculates how many possible passwords exist for a selected password
length and character set.

For example:

``` text
Search Space = Character Set Size ^ Password Length
```

The tool can compare estimated search times at different hypothetical
guessing rates.

**Important:** this feature calculates the size of the search space. It
does **not** attempt to guess passwords.

------------------------------------------------------------------------

### 🧂 4. Salted Hash Demonstration

Demonstrates how adding a random salt changes a password hash.

For the same password:

``` text
Password + Salt A → Hash A
Password + Salt B → Hash B
```

This helps demonstrate why salts are important when storing passwords
securely.

------------------------------------------------------------------------

### 📈 5. Password Entropy Calculator

Estimates password entropy in bits.

Higher entropy generally means a larger theoretical search space.

Example concept:

``` text
Low entropy  → easier to predict
High entropy → harder to predict
```

The tool also provides an understandable strength rating.

------------------------------------------------------------------------

### ⚡ 6. Hash Benchmark

Measures the approximate execution time of supported hashing operations.

This demonstrates that different algorithms can have different
performance characteristics.

------------------------------------------------------------------------

## 🧰 Technology Stack

  Technology                Purpose
  ------------------------- ---------------------------------------
  **Python**                Main programming language
  **hashlib**               Cryptographic hashing
  **Rich**                  Terminal interface and formatting
  **math**                  Search-space and entropy calculations
  **CSV / File Handling**   Results and report generation
  **Git & GitHub**          Version control and project hosting

------------------------------------------------------------------------

## 🗂️ Project Structure

``` text
Password-Security-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── modules/
│   ├── hashing.py
│   ├── password_strength.py
│   ├── entropy.py
│   ├── benchmark.py
│   ├── salt.py
│   ├── search_space.py
│   └── dictionary_attack.py
│
├── hashes/
│   └── sample_hashes.txt
│
├── results/
│
└── screenshots/
```

### Module Responsibilities

  Module                   Responsibility
  ------------------------ ----------------------------------------
  `app.py`                 Main application and menu
  `hashing.py`             Password hashing functionality
  `password_strength.py`   Password strength analysis
  `entropy.py`             Entropy calculations
  `search_space.py`        Brute-force search-space calculations
  `salt.py`                Salted-hash demonstration
  `benchmark.py`           Hash-performance benchmarking
  `dictionary_attack.py`   Educational dictionary-attack concepts
  `requirements.txt`       Python dependencies

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Clone the Repository

``` bash
git clone https://github.com/YOUR-USERNAME/Password-Security-Analyzer.git
```

Move into the project:

``` bash
cd Password-Security-Analyzer
```

------------------------------------------------------------------------

### 2. Create a Virtual Environment

Windows:

``` bash
python -m venv .venv
```

Activate it:

``` powershell
.venv\Scripts\Activate.ps1
```

If PowerShell activation is unavailable, you can also use:

``` cmd
.venv\Scripts\activate
```

------------------------------------------------------------------------

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4. Run the Application

``` bash
python app.py
```

You should see the Password Security Analyzer start in your terminal.

------------------------------------------------------------------------

## 🖥️ Example Workflow

A typical session can look like:

``` text
PASSWORD SECURITY ANALYZER

1. Generate Password Hash
2. Password Strength Checker
3. Brute Force Search Space Calculator
4. Hash Benchmark
5. Salted Hash Demonstration
6. Password Entropy Calculator
7. Exit
```

Select a feature and follow the prompts.

------------------------------------------------------------------------

## 🧠 Cybersecurity Concepts Demonstrated

This project was designed to explore practical cybersecurity concepts
including:

### Password Hashing

A password should not normally be stored as plaintext. Hashing
transforms input into a fixed-length representation.

``` text
Password
   ↓
Hash Function
   ↓
Hash
```

------------------------------------------------------------------------

### Salting

A unique random salt can be combined with a password before hashing.

``` text
Password + Random Salt
          ↓
      Hash Function
          ↓
      Salted Hash
```

This helps defend against attacks that rely on precomputed hash values.

------------------------------------------------------------------------

### Password Entropy

Entropy provides a theoretical measure of uncertainty.

Longer and less predictable passwords generally have a larger possible
search space.

------------------------------------------------------------------------

### Brute-Force Search Space

For a character set of size `C` and password length `L`:

``` text
Search Space = C^L
```

Even a small increase in password length can dramatically increase the
number of possible combinations.

------------------------------------------------------------------------

### Defensive Security

The goal of this project is to demonstrate how password-security
mechanisms work and why strong password practices matter.

------------------------------------------------------------------------

## 🎯 Learning Objectives

Through this project, I explored:

-   Python modular programming
-   Cryptographic hashing
-   Password security principles
-   Password entropy
-   Salting
-   Search-space mathematics
-   Benchmarking
-   Input validation
-   CLI application development
-   Git and GitHub
-   Defensive cybersecurity concepts

------------------------------------------------------------------------

## 🔒 Security Notes

This project is intentionally designed for **authorized and educational
use**.

Do not use it to:

-   Access accounts you do not own
-   Test passwords without authorization
-   Attack third-party systems
-   Process stolen credential databases
-   Attempt unauthorized authentication bypasses

For real-world password storage, applications should use purpose-built
password hashing algorithms such as **Argon2id, scrypt, or bcrypt**,
rather than general-purpose fast hashes such as MD5 or SHA-256.

------------------------------------------------------------------------

## 🔮 Future Improvements

Planned improvements include:

-   [ ] Professional web interface
-   [ ] CSV/TXT report export
-   [ ] Rich data tables
-   [ ] Interactive entropy visualization
-   [ ] Search-space growth charts
-   [ ] Improved input validation
-   [ ] Automated testing with `pytest`
-   [ ] Configuration management
-   [ ] Better documentation
-   [ ] Deployment as a web application

------------------------------------------------------------------------

## 📚 What I Learned

Building this project helped me understand that password security is not
simply about choosing a complicated hash function.

A secure password-storage design involves multiple considerations:

``` text
Strong Password
      +
Appropriate Password Hashing
      +
Unique Salt
      +
Secure Storage
      +
Good Authentication Practices
      =
Better Password Security
```

The project also helped me practice turning cybersecurity concepts into
practical software.

------------------------------------------------------------------------

## 👨‍💻 Author

**Shreya Trivedi**

Cybersecurity / Python Portfolio Project

GitHub: `https://github.com/itishreya18`

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **GNU License**.

See the [`LICENSE`](LICENSE) file for details.

------------------------------------------------------------------------

### 🔐 Password Security Analyzer

**Built for learning. Built for security awareness. Built with Python.**

⭐ If you found this project useful, consider giving the repository a
star!
:::
