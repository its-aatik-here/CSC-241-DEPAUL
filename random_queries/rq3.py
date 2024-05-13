#These are some practice questions I did to practice my python skills on April 26th 2024



#Print characters from a string that are present at an even index number.
def evenOutput():
    string = input ("Enter a string: ")
    for i in range(0, len(string), 2):
        print(string[i])
evenOutput()

#Write a program to remove characters from a string starting from zero up to n and return a new string.
def removeChar():
    string = input ("enter a random string: ")
    n = int(input("enter a number: "))
    print (f"{string[n:]}")
removeChar()

#Check if the first and last number of a list is the same
def checkList():
    list = [10, 20, 30, 40, 10]
    if list[0] == list[-1]:
        print("True")
    else:
        print("false")
checkList()

#Display numbers divisible by 5 from a list
def divisible():
    list = [10, 20, 33, 46, 55]
    for i in list:
        if i % 5 == 0:
            print(i)
divisible()