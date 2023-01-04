import art
import random

print(art.logo)


lives = 0
playagain = True


print("Welcome to the number guessing game!")
userName = input("What is your name?\n")

print(f"Awesome {userName}! First select your difficulty.")

while playagain:
    difficulty = input("Would you like to play on easy or hard?: ").lower()

    if difficulty == "easy":
        lives = 10
    else:
        lives= 5

    print(f"Ok your difficulty means you have {lives} guesses. Make them count!")

    randomNumber = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100....")

    while lives > 0:
        guess = int(input("Guess a number: "))
        if guess == randomNumber:
            print(f"Yes the number was {guess} great job!")
            lives = 0
        elif guess < randomNumber:
            lives-= 1
            print(f"Too low! Try again! You have {lives} guesses left.")
        else:
            lives-=1
            print(f"Too High! Try again!You have {lives} guesses left.")

    if lives == 0 and guess != randomNumber:
        print("Sorry you are out of guesses. Try again next time!")
        play2= input("Would you like to play again? y/n: ")
        if play2 == "n":
            playagain = False



