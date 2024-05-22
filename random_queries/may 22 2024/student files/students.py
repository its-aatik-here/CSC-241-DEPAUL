def getData(filename):
    try:
        inFile= open(filename,"r")
        sList = inFile.readlines()
        inFile.close()
        
        return sList
    except:
        print("cannot access file")
        
studentList = getData('random_queries/may 22 2024/student files/students.txt')
print(studentList)

# def getGradeTotals(fileName):
#     sList = getData(fileName)
#     gradeTotals = []
#     #your code here
    
    
#     return gradeTotals

# gradeNums = getGradeTotals('students.txt')
# print(f'There are {gradeNums[0]} freshman, {gradeNums[1]} sophomores, {gradeNums[0]} juniors, and {gradeNums[0]} seniors.')