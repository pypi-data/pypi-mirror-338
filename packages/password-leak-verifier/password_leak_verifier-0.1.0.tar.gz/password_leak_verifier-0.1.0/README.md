# Password Checker

This project is a Python-based password checker that uses the [Have I Been Pwned](https://haveibeenpwned.com/) API to check if a password has been leaked in any data breaches.

## Features

- Check passwords interactively
- Check passwords from a file
- Uses SHA-1 hashing to securely check passwords against the API

## Requirements

- Python 3.9
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rapzodo/password_checker.git
    cd password_checker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3.9 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Check Passwords Interactively

Run the script and enter passwords when prompted:
```sh
python com/danilo/checkmypass.py