"""
Beta 0.0.9 - attack() class function does not work; returns None
Beta 0.1.0 - Fixed Issue 0.0.9. Working but missing a few things
Beta 0.1.1 - Renamed self.sees() to self.act(); added a passive function self.act() to Item
Beta 0.1.2 - Renamed namelist to enemylist and added itemlist
Beta 0.2.1 - Added items to pick up
Beta 0.2.2 - Greatly shortened code
Beta 0.2.3 - Added 'dex' variable in enemies.py - read docstring where defined
Beta 0.2.4 - Programmed 'dex' to be multiplied by 'damage' to give a final damage. Needed to change Enemy.act() and Enemy.attack()
Beta 0.2.5 - Fixed an assignment error
Beta 0.3.1 - Nicely formatted output for inventory
Beta 0.3.2 - Moved the main loop into Adventure1(); allows expansion
Beta 0.3.3 - Added startScreen() function
Beta 0.3.4 - 'Quit' now works to exit
Beta 0.3.5 - Lowered difference of (item.damage multiplied by item.dex) and enemy.hp
Beta 0.3.6 - Lowered battle time to 5 seconds
Beta 0.3.7 - Moved main loop into keyHandle(grid); avoids repition
Beta 0.3.8 - Made new maze option, grid2
Beta 0.3.9 - Added 'win spot' x and y vars
Beta 0.4.1 - Changed x,y order for classes in items.py and enemies.py to y,x (to fit with python list standards)
Beta 0.4.2 - Edited README.md to include a changelog
Beta 0.4.3 - Fixed changelog formatting
Beta 0.4.4 - Moved changelog to CHANGELOG
Beta 0.4.5 - Added the player editor
Beta 0.4.6 - Added switching the weapon out from the inventory
Beta 0.4.7 - Changed grid2; added 'xy' keystroke
Beta 0.4.8 - Added switch() function for moving monsters!
Beta 0.4.9 - Added store()
Beta 0.5.1 - Added a new starting dialouge
Beta 0.5.2 - Added a new visual aid: mapg
Beta 0.5.3 - Shortened store()
Beta 0.5.4 - Made mapg() more detailed
"""
import player, sys
from enemies import *
from items import *

me=player.Player(0,0)

helplist="""

Keylist:
	w = forward
	a = left
	d = right
	s = backward
	q = attack
	i = inventory
	h = help
	p = player editor (change weapon, name...)
	xy = displays coordinates
	store = access the store
	wallet = display your wallet
	map = display map
	hp = health
	quit = quit
"""

grid1 = [
	[bspace(0,0),Goblin(0,1),bspace(0,2)],
	[Dragon(1,0),bspace2(1,1),Gold(21,1,2)],
	[GiantSpider(2,0),Ogre(2,1),bspace4(2,2)],
	['',bspace(3,1),''],
	['',bspace2(4,1),''],
	[bspace(5,0),bspace4(5,1),''],
	[bspace3(6,0),'',''],
	[bspace2(7,0),bspace(7,1),''],
	['',bspace4(8,1),''],
	['',bspace(9,1),''],
	[bspace2(10,0),bspace3(10,1),bspace(10,2),Ogre(10,3)],
	['','','',bspace(11,3),Gold(50,11,4)]
	
]
grid2 = [
	[bspace(0,0),'',bspace(0,2)],
	[Goblin(1,0),bspace2(1,1),''],
	[GiantSpider(2,0),Ogre(2,1),bspace4(2,2),'','','','',Gold(200,2,6)], #win spot
	['',bspace(3,1),'','',Dragon(3,4),'',Goblin(3,6)],
	['',bspace2(4,1),'','',bspace3(4,4),bspace4(4,5),bspace2(4,6)],
	[bspace(5,0),bspace4(5,1),Goblin(5,2),bspace(5,3),Ogre(5,4)],
	[bspace3(6,0),'',''],
	[bspace2(7,0),bspace(7,1),''],
	['',Dragon(8,1),'']

]
before_grid1 = """
It is an ordinary day as you take a quaint walk in the Sand Forest.
The tall pine trees loom over you. It is almost sunset, but you have no torch.
You decide to go back to your village soon. Suddenly, a huge bear jumps 
out of the cover of a tree and bares its teeth at you! It snarls and you run. 
Ahead of you, you see a cave at the bottom of a hill. You sprint towards it.
As you reach the mouth of the cave, you grab a pine branch thick with pitch
that was lying on the ground. The bear is close in pursuit. You dash in the 
cave and take a right turn. Instantly, a boulder slips loose from above 
and lands right in front of the exit! You can't see a way out, 
but at least the bear can't get in.
"""
win_statement = """
#*******************#
#******YOU WIN******#
#*******************#
"""

def mapg(l):
	tmp = l
	print('')
	old = tmp[me.y][me.x]
	tmp[me.y][me.x] = me
	for y in range(0,12):
		for x in range(0,len(tmp[y])):
			try:
				if tmp[y][x].name == me.name:
					print('	Y', end='')
				elif tmp[y][x].name in enemylist and tmp[y][x].hp >= 1:
					print('	+', end='')
				elif tmp[y][x].name == 'bspace' and tmp[y][x].hp == -1:
					print('	x',end='')
				else:
					print('	#',end='')
			except:
				print('	*', end='')
		print('')
	tmp[me.y][me.x] = old
	
def atthandle(l,x,y,playhp):
	ret = l[y][x].act(playhp)
	return ret

def switch(l,p1y,p1x,p2y,p2x):
	old = l[p2y][p2x]
	l[p2y][p2x] = l[p1y][p1x]
	l[p1y][p1x] = old

def store():
	dash = "-"*50
	print('Welcome to the store. You can by weapons and other items here in exchange for gold.')
	tmp = [Rock(-1,-1),Dagger(-1,-1),Sword(-1,-1)]
	print(dash)
	for i in range(0, len(tmp)):
		print(tmp[i].name+'\n'+tmp[i].description+'\n'+str(tmp[i].value)+' Gold\nDamage: '+str(tmp[i].damage)+'\nDex (how many times it can be swung each battle): '+str(tmp[i].dex))
		print(dash)
	
	pick = input('Type the name of the item you would like to purchase: ')
	if pick == tmp[0].name:
		if me.wallet >= tmp[0].value:
			me.invent.append(Rock(me.y,me.x))
			me.wallet -= tmp[0].value
			print('Item added to inventory')
		else:
			print('You do not have enough Gold')
	elif pick == tmp[2].name:
		if me.wallet >= tmp[2].value:
			me.invent.append(Sword(me.y,me.x))
			me.wallet -= tmp[2].value
			print('Item added to inventory')
		else:
			print('You do not have enough Gold')
	elif pick == tmp[1].name:
		if me.wallet >= tmp[1].value:
			me.invent.append(Dagger(me.y,me.x))
			me.wallet -= tmp[1].value
			print('Item added to inventory')
		else:
			print('You do not have enough Gold')
	else:
		print('That is not a valid item')
	
def keyHandle(grid, pasx, pasy): #pasy and pasx = spot to win
	while True:
		i = input('\nAction: ')
		if i == 'w' or i == 'W':
			me.y+=1
			try:
				print('You walk forward and see '+grid[me.y][me.x].pview, end='')			
			except:
				me.y-=1
				print("Bonk! You can't go that way.")
		elif i == 's' or i == 'S':
			me.y-=1
			try:
				if me.y>=0:
					print('You take a few steps backward and turn around. You see '+grid[me.y][me.x].pview, end='')				
				else:
					me.y+=1
					print("Bonk! You can't go that way!")
			except:
				me.y+=1
				print("Bonk! You can't go that way.")
		elif i == 'd' or i == 'D':
			me.x+=1
			try:
				print('You walk to the rightmost room and see '+grid[me.y][me.x].pview, end='')			
			except:
				me.x-=1
				print("Bonk! You can't go that way.")
		elif i == 'a' or i == 'A':
			me.x-=1
			try:
				if me.x>=0:
					print('You turn around and walk to the left. In front of you, you see '+grid[me.y][me.x].pview, end='')				
				else:
					me.x+=1
					print("Bonk! You can't go that way.")				
			except:
				me.x+=1
				print("Bonk! You can't go that way.")
		############ 
		elif i == 'hp' or i == 'HP':
			me.printHP()
		elif i == 'h' or i == 'H':
			print(helplist)
		elif i == 'i' or i == 'I':
			me.printInvent()
		elif i == 'p' or i == 'P':
			i = input('Welcome to the Player Editor!\nWhat would you like to change? (w = weapon, n = name) ')
			if i == 'w':
				ct = 0
				for tp in range(0, len(me.invent)):
					if me.invent[tp].name in weaponlist:
						print(str(tp)+') '+me.invent[tp].name)
						ct += 1
				if ct == 0:
					print('Sorry, you have no weapons in your inventory to choose from.')
				else:
					i = input('Type weapon number: ')
					old_weap = me.weapon
					me.weapon = me.invent[int(i)]
					del me.invent[int(i)]
					me.invent.append(old_weap)
					print('Weapon Changed!')
			elif i == 'n':
				i = input('Type your name: ')
				me.name = i
				print('Name Changed!')
			print('You: \n\nName: '+me.name+'\nHP: '+str(me.hp)+'\nWeapon: '+me.weapon.name)
		elif i == 'xy':
			print('\nX: '+str(me.x)+'\nY: '+str(me.y))
		elif i == 'store':
			store()
		elif i == 'wallet':
			print(str(me.wallet)+' Gold')
		elif i == 'quit':
			sys.exit()
		elif i == 'map':
			mapg(grid)
		else:
			print('Huh?')
		############
		if me.hp<=0:
			break
		
		if grid[me.y][me.x].name in enemylist:#!= 'bspace':		
			me.hp = atthandle(grid,me.x,me.y,me)		
		elif grid[me.y][me.x].name in itemlist:
			inp = input(' Pick up? (Y/n) ')
			if inp == 'Y' or inp == 'y':
				if grid[me.y][me.x].name != 'Gold':
					me.invent.append(grid[me.y][me.x])
				else:
					me.wallet += grid[me.y][me.x].amt
				grid[me.y][me.x] = bspace5(me.x,me.y)
				print('Item added to inventory')
				
		if me.x == pasx and me.y == pasy:
			print(win_statement)
			
			
def Adventure1():
	#print('In the Caverns has been started.\n')
	keyHandle(grid1,0,2)
def Adventure2():
	#print('A realllly hard maze has been started.\n')
	keyHandle(grid2,2,6)
def startScreen():
	print('\nWelcome to Zealous Fibula.\n\nCredits:\n    Program: Starfleet Software\n\nPress "h" for help\n')
	print(before_grid1)
	Adventure1()
startScreen()