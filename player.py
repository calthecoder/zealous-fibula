import items
class Player:	
	
	def __init__(self):#, x, y):		
		#self.x = x
		#self.y = y
		self.name = ''
		self.hp = 50
		self.weapon = items.Dagger(0,0) #(0,0) placeholders
		self.invent = []
	def isAlive(self):
		if self.hp <= 0:#self.hp == None or self.hp <= 0:
			return False
		else:
			return True
	def printHP(self):
		print("Health Points: "+str(self.hp))
		