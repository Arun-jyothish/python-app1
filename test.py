
class employee():
	def __init__(self,name,age,position):
		self.name=name
		self.age=age
		self.position=position
	def isaged(self):
		if self.age >= 25:
			print("he is aged ")
			return true
		else:
			print("not aged 25")

	def show(self):
		print("Name : "+self.name)
		print("Age : "+str(self.age))
		print("Position : "+self.position)


