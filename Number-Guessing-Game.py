import random
number = random.randint(1, 10)
guess = None
while guess != number:
    guess = int(input("Enter a number:"))
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print("Congratulations! You guessed it right")