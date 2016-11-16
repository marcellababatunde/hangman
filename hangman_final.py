#Hangman
#Marcella Babatunde
#10/19/16


import os
import random
import time 

def show_start_screen():
    print("""
██╗     ███████╗████████╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗██╗
██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║██║
██║     █████╗     ██║   ███████╗    ██████╔╝██║     ███████║ ╚████╔╝     ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║██║
██║     ██╔══╝     ██║   ╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝      ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║╚═╝
███████╗███████╗   ██║   ███████║    ██║     ███████╗██║  ██║   ██║       ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║██╗
╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝""")
                                                                                                                                             

def get_guess():

    while True:
    
        guess = input("Guess a letter: ")
    
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Only guess one letter")

def check(word, solved, guesses):
    for i in range(len(word)):
            if word[i] in guesses or not word[i].isalpha():
                solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_puzzle(file):

    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:])

def end_screen():
    print ("""
















 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝""")
                                                                          
def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f

        with open(full_path, 'r') as file:
            print(str(i + 1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)-1

    return path + "/" + files[choice]

def display_board(solved, guesses, strikes):
    if strikes == 6:
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\\\`_.'
        | |         .-`--'.
        | |        /Y     Y\\
        | |       // |   | \\\\
        | |      //  |   |  \\\\
        | |     ')   |   |   (`
        | |          ||-||
        | |          || ||
        | |          || ||
        | |          || ||
        | |         / | | \\
        ''''''''''|_`-' `-' |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)


              
    elif strikes == 5:
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\\\`_.'
        | |         .-`--'.
        | |        /Y     Y\\
        | |       // |   | \\\\
        | |      //  |   |  \\\\
        | |     ')   |   |   (`
        | |          ||-
        | |          || 
        | |          || 
        | |          || 
        | |         / | 
        ''''''''''|_`-'     |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)

    elif strikes == 4:
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\\\`_.'
        | |         .-`--'.
        | |        /Y     Y\\
        | |       // |   | \\\\
        | |      //  |   |  \\\\
        | |     ')   |   |   (`
        | |          -----
        | |         
        | |          
        | |          
        | |          
        ''''''''''|_          |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)

    elif strikes == 3:
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\\\`_.'
        | |         .-`--'.
        | |        /Y     
        | |       // |   | 
        | |      //  |   |  
        | |     ')   |   |   
        | |          -----
        | |         
        | |          
        | |          
        | |          
        ''''''''''|_        |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)

    elif strikes == 2:
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\\\`_.'
        | |         .-`--'.
        | |          |   | 
        | |          |   | 
        | |          |   |  
        | |          |   |   
        | |          -----
        | |         
        | |          
        | |          
        | |          
        ''''''''''|_        |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)

    elif strikes == 1:
        print("""
        ___________.._______
        | .__________))______|
        | | / /      ||
        | |/ /       ||
        | | /        ||.-''.
        | |/         |/  _  \\
        | |          ||  `/,|
        | |          (\\\\`_.'
        | |         .-`--'.
        | |          
        | |          
        | |         
        | |           
        | |          
        | |         
        | |          
        | |          
        | |          
        ''''''''''|_        |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)

    elif strikes == 0:
        print("""
        ___________.._______
        | .__________))______|
        | | / /       |/|
        | |/ /        |/|
        | | /         |/|
        | |/          |/|
        | |           |/|
        | |           (__)
        | |           (__)
        | |          //  \\\\ 
        | |         //    \\\\
        | |        ||      ||
        | |        ||      ||
        | |         \\\\____ //
        | |          ------
        | |          
        | |          
        | |          
        ''''''''''|_        |'''|
        |'|'''''''\\ \\       ''|'|
        | |        \\ \\        | |
        : :         \\ \\       : :  
        . .          `'       . .
        """)
     
 

    print(solved + "{guesses:" + guesses + "}")

def credit():

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("***************************************************************")
    print("*                Made by: Marcella Babatunde                  *")
    print("*                        On: 9/7/16                           *")
    print("***************************************************************")

    for i in range(50):
        time.sleep(.05)
        print("")

        
def play_again():
    while True:
        answer = input("Would you like to play again?")
        answer = answer.lower()

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes' or answer == 'y':
            return True
        else:
            print("Answer yes or no")


def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    word = word.upper()
    solved = "-" * len(word)
    guesses = ""
    strikes = 0
    limit = 6

    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)
    

    while word != solved and strikes < limit:
        letter = get_guess()
        letter = letter.upper()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
        print("You win!")

    else:
        print("You lose")
        print("The word was " + word)


def main():
    show_start_screen()

    playing = True
    
    while playing:
        play()
        playing = play_again()

    end_screen()
    credit()


# code execution begins here
if __name__ == "__main__":
    main()
