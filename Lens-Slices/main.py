# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

# print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas)+ " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.sort()

# store the cheapest and expensive pizza

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# remove uses

pizza_and_prices.pop()

# insert uses 

pizza_and_prices.insert(4, [2.5, "peppers"])

# print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)