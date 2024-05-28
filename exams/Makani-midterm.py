def contest(score):
    if score >= 10:
        return ("Gold Medal")
    elif score <10 and score>=8:
        return ("Silver Medal")
    elif score <8 and score>=5:
        return ("Bronze Medal")
    else:
        return ("Thank you For Playing")


def isCSCourse(course):
    list=course.split()
    if list[0]=="CS":
        return ("True")
    else:
        return ("False")


BDayMonthList = ['January', 'December', 'July', 'October', 'March', 'June',
                 'January', 'April', 'September', 'July', 'August', 'October',
                 'January', 'March', 'October', 'October', 'December', 'April',
                 'April', 'December', 'April', 'May', 'October', 'May',
                 'October', 'January', 'September', 'November', 'November',
                 'March']

def sameBDayCounter(month):
    count = BDayMonthList.count(month)
    return(f"There are {count} students with a birthday in {month}.")
