class Menu:
	
	# Menu constructor

	def __init__(self, name, items, start_time, end_time):
		self.name = name
		self.items = items
		self.start_time = start_time
		self.end_time = end_time
	
	def __repr__(self):
		return '%s menu available from %s to %s' %(self.name, self.start_time, self.end_time) # brunch menu available from 11am to 4pm

	def calculate_bill(self, purchased_items):

		# calculates total bill from specific order

		total = 0
		for item in purchased_items:
			if item in self.items:
				total += self.items[item]

		return total
	
# We are so successful that we need Franchise the entire business 

class Franchise:

	def __init__(self, address, menus):
		self.address = address
		self.menus = menus
   
	def __repr__(self):
		return("The restaurant is in {a}".format(a = self.address))
  
	def available_menus(self, time):
		available_menu = []
		for menu in self.menus:
			if time >= menu.start_time and time < menu.end_time:
				available_menu.append(menu)
		return(available_menu)
	
# Let's define our business

class Business:

	def __init__(self, name, franchises):
		self.name = name
		self.franchises = franchises


# creating instances for different menus

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},"11am", "4pm" )
early_bird = Menu("early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, "3pm", "6pm")
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, "5pm", "11pm")
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11am", "9pm")
arepas_menu = Menu("arepas_menu", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, "10am", "8pm")
# print(brunch)

total_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
total_bill_2 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
#print(total_bill)
#print(total_bill_2)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids, arepas_menu])
new_installment = Franchise("12 East Muberry Street", [brunch, early_bird, dinner, kids, arepas_menu])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a' Arepa", [arepas_place])
