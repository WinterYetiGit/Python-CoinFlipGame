################################ 
# WinterYetiy
# Date: 03/21/2024
# Python-CoinFlipGame-v10.py
# Version 1.0
# Description - A simple coin flip guessing game. The user inputs a choice, the program runs, and
# then it tells the user if the guess was right or not on a randomly generated coin flip feature.
# The user can continue the game or exit based on a contingency loop.
################################

# import library functions to use
import random

#Random coin flip for either heads or tails
def coin_flip():
    return random.choice(['Heads', 'Tails'])

#Loop for continuing program until user input is correct
def main():
    while True:
        print("Choose an option: 1 for Heads, 2 for Tails, or 0 to quit:")
        user_choice = input().strip()

        #user exit option
        if user_choice == '0':
            print("Exiting the program.")
            break

        #error check if user inputs wrong choice
        if user_choice not in ['1', '2']:
            print("Invalid input. Please choose 1 for Heads, 2 for Tails, or 0 to quit.")
            continue

        #internal sub-loop for correct answer path
        user_guess = 'Heads' if user_choice == '1' else 'Tails'
        result = coin_flip()
        print(f"The coin landed on: {result}")

        #User output on status of input
        if result == user_guess:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, your guess was incorrect.")

if __name__ == "__main__":
    main()

#End program.
    