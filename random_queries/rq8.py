def wordsearch(text,word):
    count = 0
    wList = text.split()
    for item in wList:
        if word == item:
            count += 1
    return count
sentence = "The weather was great this weekend"
numW = wordsearch(sentence,"this")
print (f"There are {numW} occurences in the sentence.")