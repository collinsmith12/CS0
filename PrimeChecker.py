def primechecker(numbers):
    for x in range(2,numbers):
        if numbers %x==0:
            return False
    return True
    
    
    
    
    
    
primelist=[]
for n in range (3,1000):
    if primechecker(n):
        primelist.append(n)
        
print primelist, sum(primelist)