from datetime import date

class Dog():
	species = "YSJ Dog"

	def __init__(self, name:str, age:int):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age}"

	def speak(self, sound):
		return f"{self.name} says {sound}"

	@staticmethod
	def hi():
		return "HI"

	@classmethod
	def hello(cls, name, year):
		return cls(name, date.today().year - year)



class BullDog(Dog):
	def speak(self, sound):
		return f"{sound}"

class AnotherDog(Dog):
	def speak(self, sound="hello bro"):
		return super().speak(sound)

cuteDog = BullDog("YSJ", 15)

print(cuteDog.speak("HI EveryOne!!"))


anotherDog = AnotherDog("YSH", 17)
print(cuteDog.speak("Hi?"))

dog2 = Dog.hello('mayank', 1996)
print(dog2.age, dog2.name)


print(Dog.hi())
