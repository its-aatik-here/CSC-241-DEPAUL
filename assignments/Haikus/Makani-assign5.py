import random
import time

def getText(fname):

    infile = open(fname, 'r')
    text = infile.read()
    infile.close()
    wordList = text.split()

    
    return wordList



def randomPhrase(fname, length):
    wordList = getText(fname)
    spot = random.randrange(0, len(wordList))

    line=""
    for i in range(length):
        line += wordList[spot+i] + " "
    return (line)
randomPhrase ("assignments/Haikus/Araby.txt" , 4)

   


def getHK(fname):
    
    line1_3 = random.randrange(3,4)
    
    if(line1_3 ==3):
        line2 = 4
    else:
        line2 = 3
    HK =[]
    HK.append(randomPhrase(fname, line1_3))
    HK.append(randomPhrase(fname, line2))
    HK.append(randomPhrase(fname,line1_3))

    print(HK[0])
    print(HK[1])
    print(HK[2])
getHK("assignments/Haikus/Araby.txt")


# wished to go 
# decent lives within them, 
# came out on 

# confused that I 
# them, I pressed the 
# our play brought 


# spoke she turned 
# that the bazaar would 
# a come-all-you about