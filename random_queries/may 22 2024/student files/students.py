def getData(filename):
    try:
        #your code here
        
        return sList
    except:
        print("cannot access file")
        
studentList = getData('students.txt')
print(studentList)

def getGradeTotals(fileName):
    sList = getData(fileName)
    gradeTotals = []
    #your code here
    
    
    return gradeTotals

gradeNums = getGradeTotals('students.txt')
print(f'There are {gradeNums[0]} freshman, {gradeNums[1]} sophomores, {gradeNums[0]} juniors, and {gradeNums[0]} seniors.')
        
 
        
                
        
