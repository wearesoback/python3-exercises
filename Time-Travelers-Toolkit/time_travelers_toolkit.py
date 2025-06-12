# main script for this fun project

import custom_module
import datetime as dt
from decimal import Decimal
from random import randint, choice

day = dt.date.today() # exact day
x = dt.datetime.now()

# print(str(day) + "\n" + str(x))
current_year = day.year
print(current_year)
random_year = randint(2025, 2050)

base_cost = Decimal('50.99')
cost_multiplier = abs(random_year - current_year)

time_travel_cost = base_cost * cost_multiplier
random_destinations = ['France', 'Portugal', 'Hawaii', 'Australia', 'Italy', 'Colombia', 'Japan']
final_cost = round(time_travel_cost, 2)

final_destination = choice(random_destinations)

print(custom_module.generate_time_travel_message(random_year, final_destination, final_cost))