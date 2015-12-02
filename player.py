from items import *
class Player:	
	
	def __init__(self, x, y):		
		self.x = x
		self.y = y
		self.name = ''
		self.hp = 100
		self.weapon = Dagger(self.y,self.x) #(0,0) placeholders
		self.invent = []
		self.wallet = 0

	def printHP(self):
		print("Health Points: "+str(self.hp))
	
	def printInvent(self):
		for i in range(0,len(self.invent)):
			if self.invent[i].name == 'Gold':
				print('\nSpace #'+str(i+1)+'\n'+self.invent[i].name+'\nAmt: '+str(self.invent[i].amt))
			else:
				print('\nSpace #'+str(i+1)+'\n'+self.invent[i].name)
		