word = input ("Enter a word: ")
def countChars():
    lower = 0
    upper = 0
    digit = 0
    for letter in word:
        if (letter.isupper()):
            upper = upper + 1
        elif (letter.islower()):
            lower = lower + 1
        elif (letter.isdigit()):
            digit = digit + 1
    print (f"the number of upper case characters are: {upper}")
    print (f"the number of lower case characters are: {lower} ")
    print (f"the number of digits are: {digit}")
countChars()
    

def printInitials():
    first = input ("enter your first name: ")
    last = input ("enter your last name: ")
    first_initial = (first [0].upper())
    last_initial = (last [0].upper())
    print (f"{first_initial}{last_initial}")
printInitials()