# MAY 1ST 2024

text = "The sun is shinning"
wordList = text.split()
print (wordList)

text = "The*sun*is*shinning"
wordList = text.split("*")
print (wordList)

#write a function to print the words in a sentence in a column
def printCol (sentence):
    wordList = sentence.split()
    print (wordList)
    for word in wordList:
        print (word)
printCol ("The sun is shining today!!!!")

#complete function getRand() below. Your function will use an integer
#value maxInt to determine the macimum range for the random int.
#your function will generate a random int from 0 to maxInt and return
#the value.

import random
def getRand (maxInt):
    randNum = random.randint(0,maxInt)
    print (randNum)
getRand(100)



import random
def randWord(sentence):
    wordlist = sentence.split()
    print (wordlist)
    randNum = random.randint(0,len(wordlist)-1)
    print (randNum)
    print (wordlist[randNum])
randWord("hell my name is Aatik Ali, how are you doing today ?")


import random
def randWord(sentence):
    wordlist = sentence.split()
    print (wordlist)
    randNum = random.randint(0,len(wordlist)-3)
    print (randNum)
    print (wordlist[randNum],wordlist[randNum+1],wordlist[randNum+2])
randWord("hello my name is Aatik Ali, how are you doing today ?")