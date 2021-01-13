class Vehical:
	def __init__(self, name):
		self.name = name # Public 
		self._name = name # Protected - single undersccore
		self.__name = name # Privated - Double undersccore

x = Vehical("Ashraf")

print(x.name)
print(x._name)
print(x._Vehical__name)