import enemies, items, player
#enterable from all sides?

class Tile:
	
	def __init__(self, **kwargs):
		for key in kwargs:
			self.key = kwargs[key]
		print(self.key)
		
