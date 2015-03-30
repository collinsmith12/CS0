def PE4():
    largestnumber = 0
    for x in range(100, 1000):
        for y in range(100,1000):
            numbers = str(x*y)
            if numbers == numbers[::-1]:
                if int(numbers) > int(largestnumber):
                    largestnumber= int(numbers)
    print largestnumber 