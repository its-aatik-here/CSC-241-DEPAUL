def exampleA(fName):
    try:
        inFile = open (fName,"r")

        for line in inFile:
            values = line.split()
            print (f'In {values[0]}, the avg temp was {values[1]}c and C02 emissions were {values[2]}')
        inFile.close()
    except:
        print ("cannot access file")

exampleA("random_queries/may 22 2024/FilesAndLists/ccData1.txt")

#-----------------------
# On line 2 we have the statement line = infile.readline(). We call this
# initial read the priming read. It is very important because the while
# condition needs to have a value for the line variable.

def exampleB(fName):
    try:
        inFile = open (fName,"r")
        line = inFile.readline()
        print ("year", "\tavg global tempchange", "\tCo2 emissions")
        while line:
            values = line.split()
            print(values[0] + "\t",values[1] + "\t\t\t",values[2])
            line = inFile.readline()
        inFile.close()
    except:
        print ("cannot access file")
exampleB("random_queries/may 22 2024/FilesAndLists/ccData1.txt")
    
#---------------------
    
def exampleC(fName):
    try:
        inFile = open (fName,"r")
        lineList = inFile.readlines()
        inFile.close()
        print ("year", "\tavg global tempchange", "\tCo2 emissions")
        for line in lineList:
            values = line.split()
            print(values[0] + "\t",values[1] + "\t\t\t",values[2])
    except:
        print ('file not available')
exampleC("random_queries/may 22 2024/FilesAndLists/ccData1.txt")