def nameGame(name):
    ''' takes strings as input name.
    
    iterates through name and adds alphanumeric value of each letter to variable totalScore
    
    If letter is a vowel, then adds double points for that letter.
    
    Returns int totalScore. '''
    name = str(name)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowel = 'aeiou'
    totalScore = 0
    for letter in name:
        if letter in vowel:
            totalScore += (alphabet.index ((letter)) +1) * 2
        else:
            totalScore += (alphabet.index ((letter)) +1)
    return totalScore