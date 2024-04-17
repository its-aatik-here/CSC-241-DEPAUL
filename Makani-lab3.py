import math

def valentine():
    nameOfPerson = input ("Enter name of person: ")
    pluralNoun1 = input ("Enter a plural noun: ")
    pluralNoun2 = input ("Enter a plural noun: ")
    pluralNoun3 = input ("Enter a plural noun: ")
    name = input ("Enter name of sender: ")
    print (f"Dear {nameOfPerson}, {pluralNoun1} are red,{pluralNoun2} are blue,You love me and I love {pluralNoun3}! From {name}.")
valentine()

def getAreaCode():
    phoneNumber = input("Enter a phone number in the format 1-area code-prefix-number: ")
    areaCode = phoneNumber[2:5]
    print("Area code:", areaCode)
getAreaCode()

def BSA():
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bsa = math.sqrt((height * weight) / 3600)
    print(f"Your Body Surface Area is: {bsa:.2f} square meters (m2)")
BSA()