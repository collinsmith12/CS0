import random

def loadWord():
    person = ['mike', 'teeter', 'thomas']
    place = ['trinity', 'work', 'ocala']
    thing = ['computer', 'hangman', 'printer']
    listOfLists = [person, place, thing]
    selectedList = random.choice(listOfLists)
    secretWord = random.choice(selectedList)
    
    
    if selectedList == person:
        hint = 'person'
    elif selectedList == place:
        hint = 'place'
    else:
        hint = 'thing'
        
    return (secretWord, hint)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    printWord=''
    for letter in secretWord:
        if letter in lettersGuessed:
            printWord += letter +  ""
        else:
            printWord += "_ "
    return printWord        
    
def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefgijklmnopqrstuvwxyz" 
    lettersNotGuessed = ''
    alphabet = list(alphabet)
    for letter in alphabet:
        lettersNotGuessed += letter + " "
    return lettersNotGuessed
    
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
def hangmanpicture(wrongGuesses):

        hangman = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
        /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
        /|\  |
        / \  |
            |
        =========''']
    
        return hangman[wrongGuesses]
    

def hangman(): 
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    wrongGuesses = 0
    letterGuessed = []
    loaded = loadWord()
    secretword = loaded[0]
    hint = loaded[1]
    print "The hint is a " +str(hint)
    while isWordGuessed(secretword, letterGuessed)!=True:
        if wrongGuesses == 6:
            return "game over!"
        else:
            
            guess = raw_input('pick a letter')
           
            while (guess not in alphabet or guess in letterGuessed) or len(guess) != 1:
                guess = raw_input("invalid guess. Please pick an avalible letterfrom the English language.    ")
            if guess not in secretword:
               wrongGuesses += 1
            letterGuessed.append(guess)
            print getGuessedWord(secretword, letterGuessed)
            print getAvailableLetters(letterGuessed)
            print hangmanpicture(wrongGuesses)
        ''' get user guest/print correct/incorrect
    if guess is wrong, wrong guesses to 2
    add guess to lettersGuessed
    print new get Guessedword
  
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
ist
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = loadWord()
# hangman(secretWord)

## HANGMAN IMAGES ##

