# Sals Shipping project

weight = float(input("What's the weight of your package?: "))

# Ground Shipping

flat_charge = 20.00

if weight <= 2:
    cost = weight * 1.50
    print("Your cost is: ", str(cost))
elif weight > 2 and weight <= 6:
    cost = (weight * 3.00) + flat_charge
    print("Your cost is: ", str(cost))
elif weight > 6 and weight <= 10:
    cost = (weight * 4.00) + flat_charge
    print("Your cost is: ", str(cost))
elif weight > 10:
    cost = (weight * 4.75) + flat_charge
    print("Your cost is: ", str(cost))
else:
    print ("Are you really trying to ship something?")