import random

MIN_NUMBER = 0
MAX_NUMBER = 10

def init_number():
    pass

def player_guess():
    pass

def play():
    print("Very well, player. Let's start with an easy question ...")
    playerName = input("What's your name ? ")
    print(f"Nice to meet you, {playerName} !")

    stillPlaying = True
    while stillPlaying:
        print(f"I'm going to select a number between {MIN_NUMBER} and {MAX_NUMBER}. Your goal is to guess it as quickly as possible.")
        toGuess = init_number()
        guesses = 0

        #Player guesses here

        print(f"It took you {guesses} to find the right number.")

        while True:
            stillPlayingInput = input("Would you like to keep playing ? ").lower()
            if stillPlayingInput == "no":
                stillPlaying = False
                break
            elif stillPlayingInput == "yes":
                break
            else:
                print("You must choose Yes or No.")

def main():
    playing = True

    while playing:
        inputPlaying = input("Would you like to play a guessing game with me ? ").lower()
        if inputPlaying == "yes":
            play()
            playing = False
        elif inputPlaying == "no":
            playing = False
        else :
            print("You must choose Yes or No.")


main()