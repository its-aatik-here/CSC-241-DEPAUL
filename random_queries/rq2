#in class problem done on April 24th 2024

def toppings():
    #Ask user for size of pizza and number of toppings
    pizza = input ("Enter size of pizza (small, medium, large or jumbo): ")
    toppings = float (input ("Enter number of toppings you want: "))
    if pizza == "small":
        cost = 1.50*toppings
    elif pizza == "medium":
        cost = 1.75*toppings
    elif pizza == "large":
        cost = 2.00*toppings  
    #Add another pizza which is the jumbo piza and cost is 8.00 for unlimited toppings
    elif pizza == "jumbo":
        cost = 8.00
    print (f"Your total for {pizza} pizza is: ${cost:.2f}")
toppings()



# April 29th 2024

#this function does 3 things, input, computs the price and output which is not the idle function.
#this function is a good example of a function that is not idle.
#We will change this function to a idle function which performs only one action.

def toppings(size, numTop):
    if size == "small":
        cost = 1.50*numTop
    elif size == "medium":
        cost = 1.75*numTop
    elif size == "large":
        cost = 2.00*numTop
    elif size == "jumbo":
        cost = 8.00
    return cost
#not part of function
sizeM = input ("Enter size of pizza (small, medium, large or Jumbo): ")
numTopM = float (input ("Enter number of toppings you want: "))
costM = toppings (sizeM,numTopM)
print (f"Your total for {sizeM} pizza is: ${costM:.2f}")