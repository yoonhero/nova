class Dog():
	species = "YSJ Dog"

	def __init__(self, name:str, age:int):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age}"

	def speak(self, sound):
		return f"{self.name} says {sound}"


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
