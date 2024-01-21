import random
import yaml
import getpass

with open("game_config.yml", "r") as f:
    config = yaml.safe_load(f)

range_min = config['range']['min']
range_max = config['range']['max']

guesses_allowed = config['guesses']
mode = config['mode']

solved = False 

if mode == "single":
    correct_number = random.randint(range_min, range_max)
elif mode == "multi":
    correct_number = int(getpass.getpass("Player2, please enter the number to guess: "))
else:
    print("Invalid config")
    exit()

for i in range(guesses_allowed):
    guess = int(input("Enter your guess: "))
    
    if guess == correct_number:
        print(f"Correct!, You need {i+1} tries!")
        solved = True
        break
    elif guess < correct_number:
        print("Too low!")
    else: 
        print("Too high!")


if not solved:
    print("You lost. The number was", correct_number)