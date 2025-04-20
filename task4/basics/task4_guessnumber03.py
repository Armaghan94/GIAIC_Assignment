import random

# Pick a random number between 0 and 99
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# First guess
guess = int(input("Enter a guess: "))

# Loop until the guess is correct
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = int(input("Enter a new number: "))

# When guessed correctly
print("Congrats! The number was:", secret_number)
