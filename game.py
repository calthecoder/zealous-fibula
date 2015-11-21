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
	hp = health
	^C = quit
"""

grid = [
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

def atthandle(l,x,y,playhp):
	ret = l[y][x].act(playhp)
	return ret

def Adventure1():
	print('In the Caverns has been started.\n')
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
		else:
			print('Huh?')


		############
		if me.hp<=0:
			break

		############

		if me.x == 4 and y == 11:
			print("\n\n\n\n\n\n\n******************You Win!!!!!!!****************\n\n\n\n\n\n\n\n")
			break

		if grid[me.y][me.x].name in enemylist:#!= 'bspace':		
			me.hp = atthandle(grid,me.x,me.y,me)		
		elif grid[me.y][me.x].name in itemlist:
			inp = input(' Pick up? (Y/n) ')
			if inp == 'Y' or inp == 'y':
				me.invent.append(grid[me.y][me.x])
				grid[me.y][me.x] = bspace5(me.x,me.y)
				print('Item added to inventory')

def startScreen():
	print('\nWelcome to Zealous Fibula.\nYour goal is to find your way out of the maze\nGood Luck!\n\nCredits:\n    Program: Starfleet Software\n\nPress "h" for help\n')
	print('Available adventures:\n	1) In the Caverns')
	pick = input('Which adventure? Type # here: ')
	if pick == '1':
		Adventure1()
		
startScreen()