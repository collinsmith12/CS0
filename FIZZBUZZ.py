def FIZZBUZZ():
    for numbers in range(1,101):
        if numbers %15==0:
            print "FIZZBUZZ"
        elif numbers %5==0:
            print "BUZZ"
        elif numbers %3==0:
            print "FIZZ"
        else:
            print numbers
                    