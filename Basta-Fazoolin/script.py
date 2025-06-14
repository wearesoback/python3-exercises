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
		total = 0
		return total


# creating instances for different menus

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50},"11am", "4pm" )
early_bird = Menu("early Bird", "{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}", "3pm", "6pm")
dinner = Menu("dinner", "crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00", "5pm", "11pm")
kids = Menu("kids", "{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}", "11am", "9pm")

print(brunch)

total_bill = Menu.calculate_bill(brunch, ['pancakes', 'home fries', 'coffee'])
print(total_bill)