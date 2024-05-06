# def countConjuctions(text):
#     countand = 0
#     countbut = 0
#     countor = 0
#     wordList = text.split()
#     for word in wordList:
#         if word == "and":  
#             countand += 1
#         elif word == "but":  
#             countbut += 1
#         elif word == "or":  
#             countor += 1
#     print(f"The number of and is {countand}, the number of or is {countor}, the number of but is {countbut}")

# passage = "and or but hello hi and or but"  
# countConjuctions(passage)  

# #count the number of fish, hamster, cat and dog
# def filterpets ():
#     petList = ['fish', 'hamster', 'fish', 'cat', 'hamster', 'hamster', 'fish', 'fish', 'hamster', 'cat', 'dog', 'cat', 'hamster', 'cat', 'fish', 'fish', 'hamster', 'hamster', 'dog', 'hamster', 'fish', 'dog', 'fish', 'hamster', 'cat', 'dog', 'hamster', 'fish', 'dog', 'fish']
#     fish = 0
#     hamster = 0
#     cat = 0
#     dog = 0
#     for word in petList:
#         if word == "fish":  
#             fish += 1
#         elif word == "hamster":  
#             hamster += 1
#         elif word == "cat":  
#             cat += 1
#         elif word == "dog":
#             dog += 1
#     print(f"The number of fish {fish}")
#     print(f"The number of hamster {hamster}")
#     print(f"The number of cat {cat}")
#     print (f"The number of dog {dog}")
# filterpets()

inviteList =["Tamara Sellers ","Nathanael Trevino","Grover Tanner" ,"Jerry Ho", "Cleo Wood","Bonnie Cooper","Lucia Tucker","Sheree Mcclure","Marshall Moran","Laurie Knox" ]
def guestListCheck ():
    name = input ("Enter your first name: ")
    tableList =[]
    if name in inviteList:
        tableList.append(name)
        print (tableList)
    else:
        print ("sorry you are not on the invite list")
guestListCheck()