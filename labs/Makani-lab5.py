import code 
#You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes in the same range. The result of getting the table is returned as a string value as “no”, “maybe”, or “yes”. Write a function dateFashion() that takes two parameters, you and date.  If either of you is very stylish, 8 or more, then the result is “yes”. With the exception that if either of you has style of 2 or less, then the result is “no”. Otherwise the result is “maybe”.
def dateFashion(me, date):
    me=int(me)
    date=int(date)
    if me <= 2 or date <= 2:
        print ("no")
    elif me>=8 or date>=8:
        print ("yes")
    else:
        print ("maybe")

    
    
    
#Write a function printNth() that takes a list lst and a positive (>= 0) integer n as parameters.  It prints every nth item in lst, one per line, beginning with the first item in the list.  For example, if n is 2, the function will print every other item in the list, beginning with the first item.  The function must work regardless of the type of items that are in the list.  If the parameter n is zero or negative the function should not print anything.  The function should not modify the list provided as a parameter. Hint: Use an range loop (i.e. one that uses the range() function see slides from last week.)! The following shows several sample runs of the function:   
def printNth(nList, num):
    for i in range(0,len(nList),num):
        print (nList[i])  
    
#Write a function removeNegatives(lst) that takes a list of integers as input and removes all negative numbers from the list.
#The function should modify the original list in place and return the modified list.

def removeNegatives(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 0:
            lst.pop(i)
    print (lst)
code.interact(local=dict(globals(),**locals()))
