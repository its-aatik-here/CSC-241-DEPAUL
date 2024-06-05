import code 
glossary = {}

def getFileText(fname):
    
    try: 
        infile = open(fname,"r")
        lineList=infile.readlines()
        infile.close()
        return (lineList)
    except:
        print(f"{fname} could not be opened.")
        return []  
getFileText("assignments/Glossary/glossary.txt")

    


def glossaryTerms(fname):
    tlst = getFileText(fname)
    dictionary = {}
    word = {}
    freq = {}
    for line in range(0,len(tlst)):
        word,freq = line.split(":")
    
    printWordD(dictionary)
    


# def findTerm(key):
    
#     #your code here
#     print("your key-value pair")

def printWordD(d):
    for word, freq in d.items():
        print(word + ':' + freq)

code.interact(local=dict(globals(), **locals()))