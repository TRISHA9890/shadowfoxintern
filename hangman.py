"""HANGMAN GAME"""

import random
list_word=["lion","deer","tiger","rabbit","beer"]

"""hangman diagram stages"""

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
            |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def hangman_game():
    word=random.choice(list_word).upper()
    word_completed="_" *len(word)
    guessed=False
    guessed_letters=[]
    tries=6

    print(" lets Play hangman")
    print(display_hangman(tries))
    print(word_completed)
    print("\n")
    while not guessed and tries>0:
        guess=input("guess a letter:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess}is not in word")
                tries-=1
                guessed_letters.append(guess)
            else:
                print(f"good job!{guess}is there")
                guessed_letters.append(guess)
                word_as_list = list(word_completed)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completed= "".join(word_as_list)
                 
                if "_" not in word_completed:
                    guessed=True
                else:
                    print("invalid guess")
                    print(display_hangman(tries))
                    print(word_completed)
                    print("\n")


            if guessed:
               print("Congratulations, you won!")
    else:
        print(f"Sorry, you lost.The word was{word}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman_game()
    else:
        print("Thanks for playing!")

# Run the game
hangman_game()