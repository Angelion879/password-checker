# password-checker

This is a secure terminal-based password checker for you to check if your password was ever leaked on a data breach.

## How to use

1. Clone the repo or download the files `password_checker.py` and `requirments.txt` to the same directory
2. Open the CMD pointing to the directory these files are installed
3. Run the command `pip install -r requirements.txt` and make sure all packages installed correctly
4. Still on the same CMD window, use the command `python password_checker.py` followed by your password(s)

##### NOTE: all passwords must be separated by a empty space.

A correctly executed run should return something similar to this:
    `the password password123 was leaked 294857 times`