# Sals Shipping project

weight = float(input("What's the weight of your package?: "))

# Ground Shipping

flat_charge = 20.00
cost_ground_premium = 125.00

if weight <= 2:
    cost = weight * 1.50
elif weight > 2 and weight <= 6:
    cost = (weight * 3.00) + flat_charge
elif weight > 6 and weight <= 10:
    cost = (weight * 4.00) + flat_charge
elif weight > 10:
    cost = (weight * 4.75) + flat_charge
else:
    print ("Are you really trying to ship something?")

# Drone Shipping

if weight <= 2:
    drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
    drone_cost = (weight * 9.00)
elif weight > 6 and weight <= 10:
    drone_cost = (weight * 12.00)
elif weight > 10:
    drone_cost = (weight * 14.25) 
else:
    print ("Are you really trying to ship something?")

print("Ground Shipping Cost: $", str(cost))
print("Ground Shipping Premium Cost: $", str(cost_ground_premium))
print("Drone Shipping Cost: $", str(drone_cost))

# Determine the cheapest shipping method
if cost < cost_ground_premium and cost < drone_cost:
    print("\nCheapest Shipping Method: Ground Shipping at $", cost)
elif cost_ground_premium < cost and cost_ground_premium < drone_cost:
    print("\nCheapest Shipping Method: Ground Shipping Premium at $", cost_ground_premium)
else:
    print("\nCheapest Shipping Method: Drone Shipping at $", drone_cost)