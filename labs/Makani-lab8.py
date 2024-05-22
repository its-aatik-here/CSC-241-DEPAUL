import code

def printNth(lst, nth):
    for num in range(0,len(lst),nth):
        print(lst[num])




def inBoth(list1, list2):
    found = False
    for num in list1:
        if num in list2:
            found = True
            break
    print (found)

stateList = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

def findAvgLen():
    avg = 0
    for state in stateList:
        avg += len(state)
    avg = avg / len(stateList) 
    return round(avg)
AVGLength = findAvgLen()
print(f"The average length of state names is {AVGLength} letters")


code.interact(local=dict(globals(),**locals()))