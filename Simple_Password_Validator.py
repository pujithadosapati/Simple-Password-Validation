import string
password = input("Enter your password: ")
errors = []
# Check minimum length
if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")
# Check uppercase letter
if not any(char.isupper() for char in password):
    errors.append("Password must contain an uppercase letter.")
# Check lowercase letter
if not any(char.islower() for char in password):
    errors.append("Password must contain a lowercase letter.")
# Check digit
if not any(char.isdigit() for char in password):
    errors.append("Password must contain a number.")
# Check special character
if not any(char in string.punctuation for char in password):
    errors.append("Password must contain a special character.")
# Display validation result without printing the password
if errors:
    print("Invalid password!")
    for error in errors:
        print("-", error)
else:
    print("Valid password! All requirements are satisfied.")
