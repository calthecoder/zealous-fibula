from items import *
from world import *
from player import *
from enemies import *
""" 

Syntax:

save('saves/save1.txt','saves/save1inv.txt',me.y,village)
me.y.weapon,me.y.name,me.y.wallet,me.y.skill, me.y.invent = load('saves/save1.txt','saves/save1inv.txt',me,village)

Format of save1:

name
weapon
wallet
skill

Level1 locked: True or False - to be added
Level2 locked: True or False
Level3 locked: True or False
Level4 locked: True or False

"""
def find_item(i_name, sprite): 
	#c_item stands for changed item
	c_item = sprite.weapon
	if 'Rock' in i_name:
		c_item = Rock(sprite.x,sprite.y)
	elif 'Dagger' in i_name:
		c_item = Dagger(sprite.x,sprite.y)
	elif 'Sword' in i_name:
		c_item = Sword(sprite.x,sprite.y)
	elif 'Rapier' in i_name:
		c_item = Rapier(sprite.x,sprite.y)
	elif 'Broadsword' in i_name:
		c_item = Broadsword(sprite.x,sprite.y)
	elif 'Bow and Arrow' in i_name:
		c_item = Bow_and_Arrow(sprite.x,sprite.y)
	else:
		#print("Are you crazy? There is no item with that name, doofus!")
		pass
	return c_item

def save(saveto, invsave, sprite, world_village): #sprite is the player
	f = open(saveto, 'r+')
	f.write(sprite.name)
	f.write('\n')
	f.write(sprite.weapon.name)
	f.write('\n')
	f.write(str(sprite.wallet))
	f.write('\n')
	f.write(str(sprite.skill))
	f.write('\n')
	f.write(world_village[5][0].locked) #add to after more levels are made
	f.write('\n')
	f.write(world_village[5][1].locked) #add to after more levels are made
	f.write('\n')
	f.write(world_village[5][2].locked) #add to after more levels are made
	f.write('\n')
	f.write(world_village[5][3].locked) #add to after more levels are made
	f.write('\n')
	f.close()
	finv = open(invsave, 'r+')
	for i in range(0,len(sprite.invent)):
		finv.write(sprite.invent[i].name)
		finv.write('\n')
	finv.close()

def load(loadfrom, loadfrominv, sprite, world_village):
	f = open(loadfrom, 'r')
	sprite.name = f.readline()
	sprite.weapon = find_item(f.readline(), sprite)
	sprite.wallet = int(str(f.readline()))
	sprite.skill = int(str(f.readline()))
	for room in range(0,3):
		read = f.readline()
		if 'True' in read:
			world_village[5][room].locked = True
		elif 'False' in read:
			world_village[5][room].locked = False
		else:
			world_village[5][room].locked = True
	f.close()
	sprite.invent = []
	finv = open(loadfrominv,'r')
	
	for i in range(0,10):
		to_add = find_item(finv.readline(),sprite)
		sprite.invent.append(to_add)
	while sprite.weapon in sprite.invent:
		sprite.invent.remove(sprite.weapon)
	finv.close()	
	return sprite.weapon, sprite.name, sprite.wallet, sprite.skill, sprite.invent