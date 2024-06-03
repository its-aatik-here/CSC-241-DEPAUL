glossary = {}

def getFileText(fname):
    
    try: 
        #your code here
    except:
        print(f"{fname} could not be opened.")
        return []    
    
    


def glossaryTerms(fname):
    tlst = getFileText(fname)
    #your code here
    
    
    printWordD(dictionary)


def findTerm(key):
    
    #your code here
    print("your key-value pair")
    
    

def printWordD(d):
    for word, freq in d.items():
        print(word + ':' + freq)
        
        