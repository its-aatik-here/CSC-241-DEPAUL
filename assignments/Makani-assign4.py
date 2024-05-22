import code 

def crossOffMultiples(multiplesList, num):
    for i in range(num * 2, len(multiplesList), num):
        multiplesList[i] = False
    return (multiplesList)

mList = [True] * 20 #after you get working for length 20, change to 100
mList = crossOffMultiples(mList, 2) #test values other than 2
print(mList)

def sieve(n):
    primes = []
    multiplesList = [True] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if multiplesList[num]:
            multiplesList = crossOffMultiples(multiplesList, num)
    for i in range(2, n + 1):
        if multiplesList[i]:
            primes.append(i)
    print("Prime numbers from 2 to 100:", primes)
code.interact(local=dict(globals(), **locals()))