# Name: Anton Overby
# Prog Purpose: PVCC Wordle (Pordle): Work Guessing Game
# Program chooses random word from a file of words. User tries to figure out the word in fewest guesses by guessing letters in the word.
# Program uses an input file, lists, and string slices.

import random

word_list = []
input_file = 'saintsplayers.txt'
global word_file 

def main():
    global word_list
    
    
    
    play_again = True
    while play_again:
        printHeadings()
        printMenu()

        word_file = open(input_file, 'r') #open file in READ mode
        for line in word_file: # read in a line of text from the file
            for word in line.split(): # split the line of text into words
                word_list.append(word) # add each word ot the word list
        word_file.close()

        playGame()
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == 'n' or yesno == 'N':
            play_again = False
            print('Thank you for playing PORDLE!')
            return()
        
def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")
    print("\nGet ready for a new word ... ")
    
def printMenu():
    global input_file
    print("\nChoose a PORDLE category:")
    print("\t1. Animals")
    print("\t2. Players on the New Orleans Saints (last names capitalized)")
    print("\t3. Foods")
    print("\t4. Lanugages (languages are capitalized)")
    category = input("Please enter the category number: ")

    if category == "1":
        input_file = 'animals.txt'
    elif category == "2":
        input_file = 'saintsplayers.txt'
    elif category == "3":
        input_file = 'foods.txt'
    elif category == "4":
        input_file = 'languages.txt'
    else:
        input_file = 'animals.txt'
        print("This will be an ANIMAL Pordle")

def playGame():
    numguesses = 1
    lettersUsed = []
    
    wordChosen = random.choice(word_list)
    pordle = wordChosen
    for i in range (len(pordle)): 
        pordle = pordle[0:i] + "_" + pordle[i+1:] # Use SLICE to replace each letter with a '_'
    print(" ".join(pordle)) #the "join" will put a space between in underscore
    
    while pordle != wordChosen: # keep asking the player until player guesses the word
        letterGuess = input('Please enter a letter: ')
        letterGuess = letterGuess
        lettersUsed.append(letterGuess) # Add the players' letter to the list of guessed letters
        print(f"Number of guesses: {numguesses}")
        
        for i in range(len(wordChosen)): #Search through the letters to find a match
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]
                
        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle)) # Print the string with guessed letters with spaces in between
        numguesses += 1
        
    print(f"Well done! You guessed in {numguesses-1} guesses!")
        
    
    
    
    
main()
    
