# import code 


numList = [-2, 0, 1, 5, -7, 3, 8, -13, 0, 20, 0]

def ticketPrice(age, movieType):
    if age>= 13:
        if movieType =="regular":
            return 10
        else:
            return 15
    elif age<=12:
        if movieType =="regular":
            return 7
        else:
            return 10 


def caseCounter(text):
    list = text.split()
    upper=0
    lower=0
    for word in list:
        for char in word:
            if char.isupper():
                upper +=1
            elif char.islower():
                lower +=1
    print (f"Uppercase = {upper}")
    print (f"Lowercase = {lower}")
    
    


def count(nList):
    positive = 0
    negative = 0
    zero = 0
    for num in nList:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    return (f"positives= {positive}, negatives = {negative}, zeros = {zero}")

numList = [-2,0,1,5,-7,3,8,-13,0,20,0]
count(numList)



# code.interact(local=dict(globals(), **locals()))