#problem 1
def convert():
    weight = float (input ( "Enter your weight in pounds " ))
    height = float (input ( "Enter your height in inches " ))
    weightInKg = height/2.205
    heightInCm = height * 2.54

    print (f"Your weight in kilograms is {WeightInKg} and your height in Centimeter is {HeightInCm}")
    
convert ()

#problem 2
def getTipAmount():
    resturantBill = float (input ( "Enter a resturant bill " ))
    percentage = float (input ( "Enter the tip percentage " ))
    tip = (resturantBill * percentage/100)

    print (f"The tip for a bill of ${ResturantBill} at {Percentage}% is {Tip}.")
getTipAmount ()
    
#problem 3
def getFirst2():
    text = input ("Enter a Sentence: ")
    space = text.find(' ')
    #print (space)

    first = text[0: space]
    #print (first)
    remaining = text [space+1:]
    space2 = remaining.find(' ')
    second = remaining [0:space2]

    print(f"the first letter is {first}")
    print(f"the second letter is {second}")

#problem 4
def yodaSpeak():
    text = input ("Enter a Sentence: ")
    space = text.find(' ')
    #print (space)

    first = text[0: space]
    #print (first)
    remaining = text[space+1:]
    space2 = remaining.find(' ')
    second = remaining[0:space2]
    remaining2 = remaining[space2: ]

    print(remaining2,first,second)

yodaSpeak()
