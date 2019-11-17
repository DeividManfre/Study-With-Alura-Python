from conta import creat_account

class Conta:
	
	def __init__(self, namber, responsible, balance, limit):
		print ("Maker {}".format(self))
		self.__namber = namber 
		self.__responsible = responsible 
		self.__balance = balance 
		self.__limit = limit

	def extract(self):
		print ("balance {}  responsible {} limit {}".format(self.__balance, self.__responsible, self.__limit))

	def deposits(self):
		self.__saldo += value


	def remove(self):
		if (self.__pass_remove(value)):
			self.__remove -= value
		else:
			print ("The value {} has the limit".format(value))

	def __pass_remove(self, value_the_remove):
		value_available_remove = self.__balance + self.__limit
		return value_the_remove <= value_available_remove  		


	def transfer(self, value, origem, destino):
		self.remove(value)
		destino.deposits(value)

	@porperty
	def balance(self):
		return self.__balance
    
    @porperty
	def responsible(self):
		return self.__responsible
	
	@porperty	
	def limit(self):
		return self.__limit
	
	@limit.setter	
	def set_limit(self):
		return self.__limit
