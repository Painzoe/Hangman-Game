import random
import sys
def rand_word(num):
    names = ["EINSTEIN", "SHAKESPEARE", "MICHELANGELO" , "BEETHOVEN" , "MOZART", "LEONARDO" , "ELIZABETH" , "MADONNA"]
    countries = ["JAPAN" , "CANADA" , "TURKEY" , "BRAZIL" , "NORWAY" , "MEXICO" , "SWEDEN" , "GERMANY"]
    animals = ["CROCODILE" , "LEOPARD" , "MONKEY" , "SHARK" , "DOLPHIN" , "PENGUIN" , "GIRAFFE" , "BUTTERFLY"]
    movies = ["SPIDERMAN" , "AVATAR" , "TITANIC" , "MATRIX" , "AVENGERS" , "BATMAN" , "FROZEN"]
    if num == 1:
        return random.choice(names)
    elif num == 2:
        return random.choice(countries)
    elif num == 3:
        return random.choice(animals)
    elif num == 4:
        return random.choice(movies)
    else:
        print("Please enter a number between 1 and 4")
        sys.exit()


menu = """
Welcome to the hangman game! First, choose a type, then try to find a word from that type, and don't forget to save the guy while you're at it.
Types:
1. Names
2. Countries
3. Animals
4. Movies
You can choose only 1, 2, 3 and 4 as number. If you want to quit please enter 'q' or 'Q'. Have a good game
"""
def hangman(number):
    hangman_pics = [
        r"""
      ------
      |    |
           |
           |
           |
           |
           |
    ---------
    """,
        r"""
      ------
      |    |
      O    |
           |
           |
           |
           |
    ---------
    """,
        r"""
      ------
      |    |
      O    |
      |    |
           |
           |
           |
    ---------
    """,
        r"""
      ------
      |    |
      O    |
     /|    |
           |
           |
           |
    ---------
    """,
        r"""
      ------
      |    |
      O    |
     /|\   |
           |
           |
           |
    ---------
    """,
        r"""
      ------
      |    |
      O    |
     /|\   |
     /     |
           |
           |
    ---------
    """,
        r"""
      ------
      |    |
      O    |
     /|\   |
     / \   |
           |
           |
    ---------
    """
    ]
    print(hangman_pics[number])

print(menu)
choice = input("Enter your choice: ")
if choice == "q" or choice == "Q":
    sys.exit()
else:
    word = rand_word(int(choice))
    number = 0
    letters_list = ["_"] * len(word)

    while True:
        if number >= 7:
            print("YOU LOSE!The word was " + word)
            sys.exit()
        print("""
           1. Guess a letter (You have seven chances to guess wrong)
           2. Guess the word (You only have one guess)
           """)
        selection = input("Enter your choice: ")
        if selection == "1":
            guess_letter = input("Guess a letter: ")
            if guess_letter.upper() in word:
                for i, letter in enumerate(word):
                    if letter == guess_letter.upper():
                        letters_list[i] = guess_letter.upper()
                print(letters_list)
                if not "_" in letters_list:
                    print("YOU WON!The word was " + word)
                    sys.exit()
            else:
                hangman(number)
                number += 1
                print(f"You have {7-number} attempts left!")
                print(letters_list)

        elif selection == "2":
            guessed_word = input("Guess the word: ")
            if guessed_word.upper() == word:
                print("YOU WON!The word was " + word)
                sys.exit()
            else:
                print("YOU LOST!The word was " + word)
                sys.exit()