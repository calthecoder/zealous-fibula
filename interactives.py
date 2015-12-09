class Interactive():
	def __init__(self, name, hp, description, pview, dialogue, dchoices):
		self.name = name
		self.hp = hp
		self.description = description
		self.pview = pview
		self.dialogue = dialogue
		self.dchoices = dchoices
		
	def talk_loop(self, lowrange, dchNum, diaNum):#could do just one arg
		print(self.dialogue[diaNum])
		for i in range(lowrange,len(self.dchoices[dchNum])): #add docs for this
			print(str(i)+') '+self.dchoices[dchNum][i])

class HumanInt(Interactive):
	def __init__(self, y, x, name, hp, description, pview, dialogue, dchoices):
		self.y = y
		self.x = x
		super().__init__(name = 'Human',
						hp = 100,
						description = 'An ordinary trader',
						pview = pview,
						dialogue = dialogue,
						dchoices = dchoices)

class Blacksmith(HumanInt):
	def __init__(self, y, x):
		super().__init__(y = y,
						x = x,
						name = 'Human',
						hp = 100,
						description = 'An older, skilled Blacksmith.',
						pview = ' a Blacksmith forging a new tool.',
						dialogue = ["Welcome to my smithy. How can I help you?", "I can do that. Which one would you like me to make?"], #dialogue[0] leads to dchoices[0]
						dchoices = [["I'd like a new tool.", "Oh, I'm just passing by."],["Rapier", "Broadsword"]])#list

	def act(self): #may work
		self.talk_loop(0,0,0)
		inp = input('Answer (Type the number): ')
		if int(inp) == 0:
			self.talk_loop(0,1,1)
		
#dchoices is a 2d list to show what the user can answer with