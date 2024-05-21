import code 

def crossOffMultiples(multiplesList, num):
    list = []
    multiplesList.append(True)
    for i in range (num+num,len(multiplesList),num):
        if i % num  == 0 and i!=0:
            multiplesList[i] = False
            list.append(i)
    print (multiplesList)
    print (list)

def sieve():
    #your code here

    print("you will print all the prime numbers(the indexes for all the remaining True values)")


code.interact(local=dict(globals(), **locals()))