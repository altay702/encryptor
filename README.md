# AES-256-GCM Encryption Tool (Windows)


This project provides a Python + Bash-based encryption tool leveraging **Argon2** for key derivation and **AES-256-GCM** for authenticated encryption. 

## Requirements

- **Python 3** installed on Windows.
  - [Download from python.org](https://www.python.org/downloads/) if not already installed.
- **Git Bash** or **WSL (Windows Subsystem for Linux)**.
  - If using Git Bash: [Install Git for Windows](https://git-scm.com/download/win).
  - If using WSL: [Enable WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and install ubuntu (or any distro).
- **Pip** (usually comes with Python 3).
- **(Optional) virtualenv** to create a clean Python environment.

## Installation Steps (Git Bash or WSL)

1. **Clone or Download** this repository onto your Windows machine.
2. **Open Git Bash** (or WSL) and navigate to the project directory:
   ```bash
   cd path/to/encryptor

## (Optional) Create a Virtual Environment:

$ python -m venv venv
$ source venv/bin/activate

## Install Dependencies
$ pip install -r requirements.txt

## Make run.sh Executable
$ chmod +x bin/run.sh

## Run the menu script via:
$ bash bin/run.sh

Example
 Generate Key
   bash bin/run.sh -> Select 1.
   Enter password twice.
   mykey.key will appear in your current directory.
   
  Encrypt a File
   Suppose henta1.pdf is in the same folder.
   Choose 2 and type henta1.pdf as the path.
   Creates henta1.pdf.enc.

  Decrypt a File
   Choose 3 and type henta1.pdf.enc.
   Creates document.pdf.enc.dec (which should match your original file).

