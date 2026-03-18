import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number (or 'q' to quit): ")
    
    if guess == 'q':
        print("Game exited.")
        break
    
    guess = int(guess)
    
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break
