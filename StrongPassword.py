import string

password = input("Enter your password: ")
score = 0

if len(password) > 7:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

special_characters = string.punctuation
if any(char in special_characters for char in password):
    score += 1

if score == 5:
    print("The password is strong.")
elif score >= 3:
    print("The password is moderate.")
else:
    print("The password is weak.")