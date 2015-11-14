itemlist = ['Rock', 'Dagger', 'Sword', 'Gold']

class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value, pview):
		self.name = name
		self.description = description
		self.value = value
		self.pview = pview
	"""
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
	"""
	def act(self, passed): #change passed to invetory list in Player
		passed = passed #add to inventory with this
		return passed

class Weapon(Item):
	def __init__(self, name, description, value, damage, pview):
		
		self.damage = damage
		super().__init__(name, description, value, pview)
	"""
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
	"""

class Rock(Weapon):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		super().__init__(name="Rock",
						description="A fist-sized rock, suitable for bludgeoning.",
						value=0,
						damage=5,
						pview='a usless rock')


class Dagger(Weapon):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		super().__init__(name="Dagger",
						description="A small dagger. Somewhat more dangerous than a rock.",
						value=10,
						damage=10,
						pview='a sharp, rusty dagger')
		
class Sword(Weapon):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		super().__init__(name="Sword",
						description="A long sword. A bit more dangerous than a dagger.",
						value=55,
						damage=40,
						pview='a long broadsword with a bland handle.')

class Gold(Item):
	def __init__(self, amt, x, y):
		self.amt = amt
		self.x = x
		self.y = y
		super().__init__(name="Gold", description="A round coin with {} stamped on the front.".format(str(self.amt)), value=self.amt, pview='a glittering pile of '+str(self.amt)+' gold coins on the ground.')
