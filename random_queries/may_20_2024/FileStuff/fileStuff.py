try:
    inFile = open ("random_queries/may_20_2024/FileStuff/example.txt" , "r")
    text = inFile.read()
    print (text)
    inFile.close()
except:
    print ("Error opening file")


print ("-----------")

try:
    inFile = open("random_queries/may_20_2024/FileStuff/example.txt","r")
    wList = []
    for word in inFile:
        wList.append(word)
    inFile.close()
    print (wList)

except:
    print ("oops!")



