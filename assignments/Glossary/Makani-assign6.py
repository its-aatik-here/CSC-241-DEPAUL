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
    
    


# def glossaryTerms(fname):
#     tlst = getFileText(fname)
#     #your code here
    
    
#     printWordD(dictionary)


# def findTerm(key):
    
#     #your code here
#     print("your key-value pair")
    
    

# def printWordD(d):
#     for word, freq in d.items():
#         print(word + ':' + freq)
        

code.interact(local=dict(globals(), **locals()))