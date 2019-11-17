
class Client:
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		return self.__name.title()
	
	@name.setter
	def set_name(self, name):
		print("chmando set name{}")
		self.__name = name