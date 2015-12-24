itemlist = ['Rock', 'Dagger', 'Sword', 'Gold','Broadsword','Rapier']
weaponlist = ['Rock', 'Dagger', 'Sword','Broadsword','Rapier', 'Bow and Arrow']

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
	def __init__(self, name, description, value, damage, pview, dex, accuracy): #dextrous = how many time it can be swung in a ten second battle
		
		self.damage = damage
		self.dex = dex
		self.accuracy = accuracy
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
						dex=6,
						accuracy=3)#higher is good


class Dagger(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Dagger",
						description="A small dagger. Somewhat more dangerous than a rock.",
						value=20,
						damage=24,
						pview='a sharp, rusty dagger lying at your feet.',
						dex=4,
						accuracy=5)
		
class Sword(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Sword",
						description="A long sword. A bit more dangerous than a dagger.",
						value=55,
						damage=37,
						pview='a long broadsword with a bland handle.',
						dex=4,
						accuracy=5)
class Rapier(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Rapier",
						description="A long, thin sword. Very manuverable.",
						value=75,
						damage=20,
						pview='a long, thin rapier with an elaborate blade design.',
						dex=6,
						accuracy=6)
class Broadsword(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Broadsword",
						description="A wide sword. Heavy, but gives much damage.",
						value=87,
						damage=70,
						pview='a wide, heavy sword.',
						dex=3,
						accuracy=5)
class Bow_and_Arrow(Weapon):
	def __init__(self,y,x):
		self.x = x
		self.y = y
		super().__init__(name="Bow and Arrow",
						description="A large longbow. Fast and gives alot of damage, but not too accurate.",
						value=100,
						damage=80,
						pview='a longbow.',
						dex=4,
						accuracy=3)
class Gold(Item):
	def __init__(self, amt, y,x):
		self.amt = amt
		self.x = x
		self.y = y
		super().__init__(name="Gold", description="A round coin with {} stamped on the front.".format(str(self.amt)), value=self.amt, pview='a glittering pile of '+str(self.amt)+' gold coins on the ground.')
