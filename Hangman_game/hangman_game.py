import random
def hangman():

    word = random.choice(["ironman" ,"blackpanther", "hawkeye" , "mandarin" , "thor" ,"ghostrider","loki","spiderman","hulk","vision","wolverine","deadpool","iceman","groot" , "thanos"  ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print("\n",main)
            print("\n You win! \n")
            playagain=input("Press 0 to play again and any other key to exit ")
            if playagain=='0':
                print("Welcome Again" , name )
                print("-------------------")
                print("Try to Guess the Superhero  in less than 10 attempts ")
                hangman()
            else:
                print("Thanks for Playing")
                break

        print("Guess the next word: " , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character ")
            guess = input()

        if guess not in word:
            print("Oops! Wrong Guess ")
            turns = turns - 1
            
            if turns == 9:
                print("9 turns left")
                print(" _________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 8:
                print("8 turns left")
                print(" _________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 7:
                print("7 turns left")
                print(" _________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 6:
                print("6 turns left")
                print(" _________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 5:
                print("5 turns left")
                print(" _________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  ________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  ________  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  _________  ")
                print("   \ O / |   ")
                print("     |   |   ")
                print("    / \      ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  ________  ")
                print("   \ O |    ")
                print("     |\|    ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  ________  ")
                print("       |    ")
                print("     O/     ")
                print("    /|\     ")
                print("    / \     ")
                break


name = input("Enter your name ")
print("Welcome" , name )
print("-------------------")
print("Try to Guess the Superhero  in less than 10 attempts ")
hangman()
print()