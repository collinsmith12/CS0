def squareOfOdds(numRanege):
    localList = []
    
    for x in range(1, numRange + 1):
         if x % 2 ==1:
             localList.append(x**2)
    print localList
    
def squareOfEvens(numRange):
    localList = []
    
    for x in range(1, numRange + 1):
         if x % 2 ==0:
             localList.append(x**2)
    print localList