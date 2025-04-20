# Joke Bot

# Constants
PROMPT = "What do you want? "
JOKE = "Here is a joke for you!  - A programmer’s dog goes missing. He writes a bug report instead of a missing poster because he knows someone will eventually try to reproduce the problem."
SORRY = "Sorry I only tell jokes"

# Get user input
user_input = input(PROMPT)

# Check the input
if user_input == "Joke":
    print(JOKE)
else:
    print(SORRY)
