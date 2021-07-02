# A guess the number game

import random

print('Hello, what\'s your name?')
name = input()
secretNumber = random.randint(1, 7)
print('Hi ' + name + ', I\'m thinking of a number between 1 and 7, try to guess it!')

# Ask the player to guess 6 times
for guessesTaken in range (1, 7):
    print('You have ' + str(7 - guessesTaken) + ' guesses')
    guess = int(input())
    try:
        if guess < 1 or guess > 7:
            print("Your guess was out of range!")
        else:
            if guess < secretNumber:
                print('Your guess is too low!')
            elif guess > secretNumber:
                print('Your guess is too high!')
            else:
                break
    except:
        print("You didn't input a number")

if guess == secretNumber:
    print("Good job " + name + "! You guessed my number in " + str(guessesTaken) + " goes!")
else:
    print("Bad luck, " + name + ". The number was " + str(secretNumber))

print("Goodbye!")