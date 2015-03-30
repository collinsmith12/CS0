def vendingMachine (money, choice):
    ''' Enter choice and money, choice must be from the item list.
    if not vendingMachine will return money and say "invalid choice".
    if from items list but not enough money it will say "not enough money" '''
    items = ["water", "coke", "sprite", "pepsi","goldfish","doritos","sunchips","popcorn"]
    
    if money >= 1.5:
        if choice in items:
            return (choice, money - 1.5)
        else:
            return ('invalid choice!', money)
    else:
        return ('not enough money', money)
    if money == 1.5:
                return('Thank you!, 1.5 - 1.5')