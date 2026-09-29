Random Password Generator
This is a simple password generator I made in Python. It generates random, strong passwords based on what you want - like length, lowercase, uppercase, numbers, symbols etc.

I used Python's secrets module instead of random because it's more secure for passwords.

What it can do
You can set password length from 4 to 128
You can choose to include/exclude lowercase, uppercase, digits, symbols
It makes sure at least one character from each selected type is included
You can generate multiple passwords at once
It shows password strength and entropy
You can save the passwords to a passwords.txt file if you want
You can generate again without closing the program
Modules used
secrets - for secure random choice
string - for getting a-z, A-Z, 0-9, symbols
math - to calculate entropy
How it works
Pretty simple:

Takes length from user
Asks which character types to include
Builds a character pool
Picks one character from each selected type, then fills the rest randomly
Shuffles it and shows the result with strength.
Strength is checked based on entropy:

< 40 bits = Weak
40-59 = Medium
60-79 = Strong
80+ = Very Strong
Main Functions
make_password() - generates the password
check_power() - calculates entropy and returns strength
yes_no_input() - handles Y/N inputs
number_input() - takes and validates the length

How to run
Make sure you have Python 3 installed
Save the file as password_generator.py
Open terminal in that folder
Run:
