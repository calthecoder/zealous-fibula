itemlist = ['Rock', 'Dagger', 'Sword', 'Gold']
weaponlist = ['Rock', 'Dagger', 'Sword']

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
	def __init__(self, name, description, value, damage, pview, dex): #dextrous = how many time it can be swung in a ten second battle
		
		self.damage = damage
		self.dex = dex
		super().__init__(name, description, value, pview)
	"""
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
	"""

class Rock(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Rock",
						description="A fist-sized rock, suitable for bludgeoning.",
						value=5,
						damage=10,
						pview='a usless rock in the corner of the room.',
						dex=6)


class Dagger(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Dagger",
						description="A small dagger. Somewhat more dangerous than a rock.",
						value=20,
						damage=24,
						pview='a sharp, rusty dagger lying at your feet.',
						dex=4)
		
class Sword(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Sword",
						description="A long sword. A bit more dangerous than a dagger.",
						value=55,
						damage=37,
						pview='a long broadsword with a bland handle.',
						dex=4)

class Gold(Item):
	def __init__(self, amt, y,x):
		self.amt = amt
		self.x = x
		self.y = y
		super().__init__(name="Gold", description="A round coin with {} stamped on the front.".format(str(self.amt)), value=self.amt, pview='a glittering pile of '+str(self.amt)+' gold coins on the ground.')
