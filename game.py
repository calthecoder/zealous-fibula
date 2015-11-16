"""
Beta 0.0.9 - attack() class function does not work; returns None
Beta 0.1.0 - Fixed Issue 0.0.9. Working but missing a few things
Beta 0.1.1 - Renamed self.sees() to self.act(); added a passive function self.act() to Item
Beta 0.1.2 - Renamed namelist to enemylist and added itemlist
Beta 0.2.1 - Added items to pick up
Beta 0.2.2 - Greatly shortened code
Beta 0.2.3 - Added 'dex' variable in enemies.py - read docstring where defined
Beta 0.2.4 - Programmed 'dex' to be multiplied by 'damage' to give a final damage. Needed to change Enemy.act() and Enemy.attack()
"""
import player, sys
#from world import Tile
from enemies import *
from items import *

me=player.Player()

print('\nWelcome to Zealous Fibula.\nYour goal is to find your way out of the maze\nGood Luck!\n\nCredits:\n    Program: Starfleet Software\n\nPress "h" for help\n')

helplist="""
**  = not added yet

Keylist:
	w = forward
	a = left
	d = right
	s = backward
	q = attack
	i = inventory  **
	wa = wallet **
	h = help
	hp = health
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
x,y=0,0

me.hp = 50
def atthandle(l,x,y,playhp):
	ret = l[y][x].act(playhp)
	return ret



while True:
	i = input('\nAction: ')
	if i == 'w' or i == 'W':
		y+=1
		try:
			print('You walk forward and see '+grid[y][x].pview, end='')			
			# add if statement here to append to me.invent if items are here 
			# You see..."pick up? (Y/n) 
		except:
			y-=1
			print("Bonk! You can't go that way.")
	elif i == 's' or i == 'S':
		y-=1
		try:
			if y>=0:
				print('You take a few steps backward and turn around. You see '+grid[y][x].pview, end='')				
			else:
				y+=1
				print("Bonk! You can't go that way!")
		except:
			y+=1
			print("Bonk! You can't go that way.")
	elif i == 'd' or i == 'D':
		x+=1
		try:
			print('You walk to the rightmost room and see '+grid[y][x].pview, end='')			
		except:
			x-=1
			print("Bonk! You can't go that way.")
	elif i == 'a' or i == 'A':
		x-=1
		try:
			if x>=0:
				print('You turn around and walk to the left. In front of you, you see '+grid[y][x].pview, end='')				
			else:
				x+=1
				print("Bonk! You can't go that way.")				
		except:
			x+=1
			print("Bonk! You can't go that way.")
	############ 
	elif i == 'hp' or i == 'HP':
		me.printHP()
	elif i == 'h' or i == 'H':
		print(helplist)
	elif i == 'i' or i == 'I':
		print(me.invent)
	else:
		print('Huh?')
	
	
	############
	if me.hp<=0:
		break
	
	############
	
	if x == 4 and y == 11:
		print("\n\n\n\n\n\n\n******************You Win!!!!!!!****************\n\n\n\n\n\n\n\n")
		break
		
	if grid[y][x].name in enemylist:#!= 'bspace':
		me.hp = atthandle(grid,x,y,me)
	elif grid[y][x].name in itemlist:
		inp = input(' Pick up? (Y/n) ')
		if inp == 'Y' or inp == 'y':
			me.invent.append(grid[y][x].name)
			grid[y][x] = bspace5(x,y)
			print('Item added to inventory')
		