import random

def show_start_screen():
    print("Let's play Hangman!")

def show_credits():
    print ("by Marcella")

def get_guess():
    guess = input("Guess a letter: ")

    return guess

def check(word, solved, guesses):
    for i in range(len(word)):
            if word[i] in guesses or not word[i].isalpha():
                solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_puzzle():
    words = ["patriots", "soccer", "apple", "banana", "orange", "google", "goggle", "french fries", "happy birthday", "scarowinds"]

    return random.choice(words)

def confirm():
    pass

def play():

    word = get_puzzle()
    solved = "-" * len(word)
    guesses = ""
    strikes = 0
    limit = 6

    solved = check(word, solved, guesses)
    
    print(solved)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        print(solved)

    if word == solved:
        print("You win!")

    else:
        print("You lose")


def main():
    show_start_screen()
    play()
    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
