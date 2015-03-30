import random

def loadWord():
    person = ['mike', 'teeter', 'thomas']
    place = ['trinity', 'work', 'ocala']
    thing = ['computer', 'hangman', 'printer']
    listOfLists = [person, place, thing]
    selectedList = random.choice(listOfLists)
    secretWord = random.choice(selectedList)
    hint = ''
    
    if selectedList == person:
        hint = 'person'
    elif selectedList == place:
        hint = 'place'
    else:
        hint = 'thing'
        
    return (secretWord, hint)