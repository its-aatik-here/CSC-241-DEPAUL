#import code 

def crossOffMultiples(multiplesList, num):
    for i in range (len(multiplesList)):
        if i % num  == 0 and i!=0:
            multiplesList[i] = False
    return (multiplesList)

multiplesList = [True]*20
crossOffMultiples(multiplesList,2)
print (multiplesList)

def sieve():
    #your code here

    print("you will print all the prime numbers(the indexes for all the remaining True values)")


#code.interact(local=dict(globals(), **locals()))