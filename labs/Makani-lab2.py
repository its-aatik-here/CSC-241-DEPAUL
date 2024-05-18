def computeTotal():
    price = float (input ("Enter a price: "))
    quantity =int (input ("Enter the quantity: "))
    if price>0 and quantity>0 :
        total = price*quantity
        print (f"The total price is : ${total}")
computeTotal ()



def computeG():
    G = 6.674e-11  # Gravitational constant in m³/kg/s²
    gravity = 0
    mass = float (input ("Enter the mass of planet in kilograms: "))
    radius = float (input ("Enter the radius of plant in meters: "))
    gravity = (G*mass)/(radius**2)
    print(f"Surface gravity of the planet: {gravity}m/s²")
computeG()