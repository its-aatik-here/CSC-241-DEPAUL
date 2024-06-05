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
    keyvaluelist = {}
    for line in tlst:
        keyvaluelist = line.split(": ")
        key = keyvaluelist[0]
        value = keyvaluelist [1]
        glossary[key] = value
    printWordD(glossary)
    


def findTerm(key):
    
    value = glossary.get(key)
    print(f"{key} means {value}")

def printWordD(d):
    for key, value in d.items():
        print(key + ':' + value)

code.interact(local=dict(globals(), **locals()))