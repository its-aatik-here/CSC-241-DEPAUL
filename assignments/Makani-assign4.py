#import code 

def crossOffMultiples(multiplesList, num):
    for i in range (num+num,len(multiplesList),num):
        if i % num  == 0 and i!=0:
            multiplesList[i] = False
    return (multiplesList)

multiplesList = [True]*100
crossOffMultiples(multiplesList,2)
print (multiplesList)

def sieve():
    #your code here

    print("you will print all the prime numbers(the indexes for all the remaining True values)")


#code.interact(local=dict(globals(), **locals()))