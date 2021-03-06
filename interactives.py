from items import *

interlist = ['Blacksmith','Fletcher']
class Interactive():
	def __init__(self, name, hp, description, pview, dialogue, dchoices):
		self.name = name
		self.hp = hp
		self.description = description
		self.pview = pview
		self.dialogue = dialogue
		self.dchoices = dchoices
		
	def talk_loop(self, dchNum, diaNum):#could do just one arg
		print(self.dialogue[diaNum])
		for i in range(0,len(self.dchoices[dchNum])): #add docs for this
			print(str(i)+') '+self.dchoices[dchNum][i])

	def get_inp(self):
		try:
			inp = input('Answer (Type the number): ')
			return int(inp)
		except:
			x = self.get_inp() #return needs to be here
			return x

class Blacksmith(Interactive):
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.tmp = [Rapier(-1,-1),Broadsword(-1,-1),Dagger(-1,-1),Sword(-1,-1)]
		super().__init__(name = 'Blacksmith',
						hp = 100,
						description = 'An older, skilled Blacksmith.',
						pview = 'a Blacksmith forging a new tool.\n',
						dialogue = ["Welcome to my smithy. How can I help you?", "I can do that. Which one would you like me to make?","Would you like to know more about that weapon?","Are you ready to purchase it?"],
						dchoices = [["I'd like a new tool.","Oh, I'm just passing by"],["Rapier","Broadsword","Dagger","Sword"],["Yes","No"],["Yes","No"]])

	def act(self, p_obj): #may work
		wallet = p_obj.wallet
		ret = wallet
		invent = p_obj.invent
		self.talk_loop(0,0)
		inp = self.get_inp()
		if inp == 0:
			self.talk_loop(1,1)
			wc = self.get_inp()
			self.talk_loop(2,2)
			inp = self.get_inp()
			if inp == 0:
				print(self.tmp[wc].name+'\n'+self.tmp[wc].description+'\n'+str(self.tmp[wc].value)+' Gold\nDamage: '+str(self.tmp[wc].damage)+'\nDex (how many times it can be swung each battle): '+str(self.tmp[wc].dex)+'\nAccuracy: '+str(self.tmp[wc].accuracy))
			self.talk_loop(3,3)
			inp = self.get_inp()
			if inp == 0:
				#print(str(wallet))
				if wallet >= self.tmp[wc].value:
					ret = wallet - self.tmp[wc].value
					invent.append(self.tmp[wc])
					print("Here it is!")
					#return wallet
				else:
					print('You do not have enough Gold.')
					#return wall
		return ret

class Fletcher(Interactive):
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.tmp = [Bow_and_Arrow(-1,-1)]
		super().__init__(name = 'Fletcher',
						hp = 100,
						description = 'A fletcher who also makes bows.',
						pview = 'a Fletcher putting some feathers on arrows.\n',
						dialogue = ["Welcome to my shop. How can I help you?", "I can do that. Would you like to know more about that weapon?","Are you ready to purchase it?"],
						dchoices = [["I'd like a new bow and arrow","Oh, I'm just passing by"],["Yes","No"],["Yes","No"]])
	def act(self, p_obj): #may work
		wallet = p_obj.wallet
		ret = wallet
		invent = p_obj.invent
		self.talk_loop(0,0)
		inp = self.get_inp()
		if inp == 0:
			#self.talk_loop(1,1)
			wc = 0
			self.talk_loop(1,1)
			if inp == 0:
				print(self.tmp[wc].name+'\n'+self.tmp[wc].description+'\n'+str(self.tmp[wc].value)+' Gold\nDamage: '+str(self.tmp[wc].damage)+'\nDex (how many times it can be swung each battle): '+str(self.tmp[wc].dex)+'\nAccuracy: '+str(self.tmp[wc].accuracy))
			self.talk_loop(2,2)
			inp = self.get_inp()
			if inp == 0:
				#print(str(wallet))
				if wallet >= self.tmp[wc].value:
					ret = wallet - self.tmp[wc].value
					invent.append(self.tmp[wc])
					print("Here it is!")
					#return wallet
				else:
					print('You do not have enough Gold.')
					#return wall
		return ret