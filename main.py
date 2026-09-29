import math
import secrets
import string

# making a strong password generator - for my project

lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation

def make_password(length=12, lower=True, upper=True, digits=True, symbols=True):
    # collect what user wants
    all_chars = ""
    must_have = []

    if lower:
        all_chars += lower_chars
        must_have.append(secrets.choice(lower_chars))
    if upper:
        all_chars += upper_chars
        must_have.append(secrets.choice(upper_chars))
    if digits:
        all_chars += numbers
        must_have.append(secrets.choice(numbers))
    if symbols:
        all_chars += special_chars
        must_have.append(secrets.choice(special_chars))

    if all_chars == "":
        print("You have to select atleast one type!")
        return None

    if length < len(must_have):
        print(f"Length is too short, need atleast {len(must_have)} chars")
        return None

    # fill the rest randomly
    password_list = must_have[:]
    for i in range(length - len(must_have)):
        password_list.append(secrets.choice(all_chars))

    # shuffle so first chars are not always same pattern
    secrets.SystemRandom().shuffle(password_list)

    final_pwd = "".join(password_list)
    return final_pwd

def check_power(pwd):
    # simple entropy check
    size = 0
    if any(c in lower_chars for c in pwd):
        size += 26
    if any(c in upper_chars for c in pwd):
        size += 26
    if any(c in numbers for c in pwd):
        size += 10
    if any(c in special_chars for c in pwd):
        size += len(special_chars)

    if size == 0:
        return "Weak", 0

    ent = len(pwd) * math.log2(size)

    if ent < 40:
        level = "Weak"
    elif ent < 60:
        level = "Medium"
    elif ent < 80:
        level = "Strong"
    else:
        level = "Very Strong"

    return level, round(ent, 1)

# small helpers for input
def yes_no_input(msg, default_yes=True):
    if default_yes:
        choice = input(f"{msg} [Y/n]: ").strip().lower()
        if choice == "":
            return True
        return choice == 'y' or choice == 'yes'
    else:
        choice = input(f"{msg} [y/N]: ").strip().lower()
        if choice == "":
            return False
        return choice == 'y' or choice == 'yes'

def number_input(msg, default_val):
    while True:
        val = input(f"{msg} (default={default_val}): ").strip()
        if val == "":
            return default_val
        if val.isdigit():
            num = int(val)
            if 4 <= num <= 128:
                return num
        print("Enter a valid number (4-128)")

# main program starts here
print("--------------------------------------------")
print("  RANDOM PASSWORD GENERATOR")
print("--------------------------------------------")

while True:
    l = number_input("Enter password length", 12)
    
    low = yes_no_input("Include lowercase?")
    up = yes_no_input("Include uppercase?")
    dig = yes_no_input("Include numbers?")
    sym = yes_no_input("Include symbols?")

    how_many = number_input("How many passwords you want", 1)

    all_passwords = []
    for _ in range(how_many):
        p = make_password(l, low, up, dig, sym)
        if p:
            all_passwords.append(p)

    if len(all_passwords) == 0:
        print("No password generated, try again\n")
        continue

    print("\n--- Your Passwords ---")
    for p in all_passwords:
        lvl, ent_val = check_power(p)
        print(f"{p}  -> {lvl} ({ent_val} bits)")

    save = yes_no_input("\nDo you want to save to file?", default_yes=False)
    if save:
        with open("passwords.txt", "a") as file:
            for p in all_passwords:
                file.write(p + "\n")
        print("Saved to passwords.txt")

    again = yes_no_input("\nWant to generate more?", default_yes=True)
    if not again:
        print("Ok bye!")
        break
    print("")