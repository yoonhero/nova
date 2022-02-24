class Pizza(object):
	def __init__(self):
		self.toppings = []

	def __call__(self, topping):
		self.toppings.append(topping())

	def __repr__(self):
		return str(self.toppings)

pizza = Pizza()

@pizza 
def cheese():
	return "cheese"

@pizza
def sauce():
	return "sauce"


print(pizza)



def decorator(func):
   return func()


@decorator
def some_func():
    return print("wow")

# dec = decorator()
