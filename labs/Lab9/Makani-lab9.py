def displayNames(fname):
    try:
        inFile = open (fname,"r")
        sList = inFile.readlines()
        inFile.close()
        # for senator in sList:
            # print(senator.rstrip())
        return sList
    except:
        print("File not found")
displayNames("labs/Lab9/USSenate.csv")


def findAvgAge(fname):
    sum=0
    senateList = displayNames(fname)
    for row in senateList:
        senator = row.split(",")
        sum += int(senator[3])
    avg = sum/(len(senateList))
    return avg
    return senator
findAvgAge("labs/Lab9/USSenate.csv")

def findSenators(fname, state):
    senateList = displayNames(fname)
    for row in senateList:
        senator = row.split(",")
        if senator[2]==state:
            print(senator[1],senator[0])
findSenators("labs/Lab9/USSenate.csv","Illinois")