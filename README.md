# Password Manager

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue)](https://python.org)
[![Flask 1.1.2](https://img.shields.io/badge/flask-1.1.2-magenta)](https://palletsprojects.com/p/flask/)

This is a password manager written in python meant to be run on localhost.

## Made with:

- Python3
- Flask
- Sqlite

## Run locally

### Windows: (Python not required)

- Download `password-manager-win32.zip` from the releases tab
- Unzip and run the `app.exe` executable
- Go to http://localhost:3000

### Linux/Mac (Python v3.6 or later required)

- First make sure you have at least python 3.6 or later
- Run `setup_db.py`
- Change `app.secret_key` in `src/__init__.py` to a secret key
- Run `pip install -r requirements.txt` in a venv (or not), use `pip3` if needed
- Run `python app.py`, use `python3` if needed
