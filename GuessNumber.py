import random

random_number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    tries += 1
    
    if guess < random_number:
        print("Too low.")
    elif guess > random_number:
        print("Too high.")
    else:
        print(f"Congratulations! You guessed the number, {random_number} correctly.")
        print(f"It took you {tries} tries.")
        break