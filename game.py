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
Beta 0.5.5 - Started before_grid2
Beta 0.5.6 - Started working on interactives.py - a new library for interaction!!
Beta 0.5.7 - Fixed up interactives.py and added some weapons for use in interactives
Beta 0.5.8 - Added a map key
Beta 0.5.9 - Removed HumanInt class
Beta 0.6.1 - Fixed mapg() error
Beta 0.6.2 - Fixed error that happened when you pressed something other than "m" or "q" in Enemy.act()
Beta 0.6.3 - Moved dialogue and maps to world.py
Beta 0.6.4 - Added accuracy variable to weapons
Beta 0.6.5 - Included music (2 soundtracks)
Beta 0.6.6 - Added Inverted control option
Beta 0.6.7 - Added more music and sound effects
Beta 0.6.8 - Fixed pyinstaller music problem
Beta 0.6.9 - Added Fletcher
Beta 0.7.1 - Village is new "store"; can be visited after every level
"""
import player, sys, random
from enemies import *
from world import *
from items import *
from interactives import *

me=player.Player(0,0)

helplist="""

Keylist:

	Type `h:` followed by a specific keystroke for help on a certain function

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
yp, ym = 1, -1 #for inverted controls
oldx, oldy = 0,0
win_statement = """
#*******************#
#******YOU WIN******#
#*******************#
"""
musc = False
try:
	print('Loading music...')
	from pygame import mixer # Load the required library
	mixer.init()
	m_chan = mixer.Channel(0)
	s_chan = mixer.Channel(1)
	if sys.platform.startswith('darwin'):
		seffect1 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/seffect1.ogg')
		seffect2 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/seffect2.ogg')
		strack1 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/A Glimmer in the North.ogg')
		strack2 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/strack2.ogg')
		strack3 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Down Down to Goblin-town.ogg')
		strack4 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Far Ahead the Road Has Gone.ogg')
		strack5 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Hammerhand.ogg')
		strack6 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Lament for Oakenshield.ogg')
		strack7 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Oakenshield.ogg')
		strack8 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Shadows of Angmar.ogg')
		strack9 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/The Creeping Gloom.ogg')
		strack10 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/The Ice Bay.ogg')
		strack11 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/The Road to War.ogg')
		strack12 = mixer.Sound('/Users/calvin/Documents/zealous-fibula-master/zealous-fibula/resources/Where Will Wants Not.ogg')
	else:
		seffect1 = mixer.Sound('resources/seffect1.ogg')
		seffect2 = mixer.Sound('resources/seffect2.ogg')
		strack1 = mixer.Sound('resources/A Glimmer in the North.ogg')
		strack2 = mixer.Sound('resources/strack2.ogg')
		strack3 = mixer.Sound('resources/Down Down to Goblin-town.ogg')
		strack4 = mixer.Sound('resources/Far Ahead the Road Has Gone.ogg')
		strack5 = mixer.Sound('resources/Hammerhand.ogg')
		strack6 = mixer.Sound('resources/Lament for Oakenshield.ogg')
		strack7 = mixer.Sound('resources/Oakenshield.ogg')
		strack8 = mixer.Sound('resources/Shadows of Angmar.ogg')
		strack9 = mixer.Sound('resources/The Creeping Gloom.ogg')
		strack10 = mixer.Sound('resources/The Ice Bay.ogg')
		strack11 = mixer.Sound('resources/The Road to War.ogg')
		strack12 = mixer.Sound('resources/Where Will Wants Not.ogg')
	playlist = [strack1,strack2,strack3,strack4,strack5,strack6,strack7,strack8,strack9,strack10,strack11,strack12]
	musc = True
except:
	print("Music not compatible")
	musc = False

def mapg(l):
	tmp = l
	print('')
	old = tmp[me.y][me.x]
	tmp[me.y][me.x] = me
	if l == grid2:
		yr = 9
	elif l == grid1:
		yr = 12
	elif l == village:
		yr=6 #Don't Forget to change
	for y in range(0,yr):
		for x in range(0,len(tmp[y])):
			try:
				if tmp[y][x].name == me.name:
					print('	Y', end='')
				elif tmp[y][x].name in enemylist and tmp[y][x].hp >= 1:
					print('	+', end='')
				elif tmp[y][x].name == 'bspace' and tmp[y][x].hp == -1:
					print('	x',end='')
				elif tmp[y][x].name in itemlist:
					print('	!',end='')
				elif tmp[y][x].name == 'level':
					print('	'+str(tmp[y][x].num),end='')
				else:
					print('	#',end='')
			except:
				print('	*', end='')
		print('')
	print('\nY = You\n+ = Live Monster\nx = Dead Monster\n! = Item\n# = Blank Space\nAny number = Level Gateway\n* = You cannot go here')
	tmp[me.y][me.x] = old
	
def atthandle(l,x,y,playhp):
	ret = l[y][x].act(playhp)
	return ret

def switch(l,p1y,p1x,p2y,p2x):
	old = l[p2y][p2x]
	l[p2y][p2x] = l[p1y][p1x]
	l[p1y][p1x] = old
"""
def store(call):
	global callfrom
	dash = "-"*50
	print(dash+'\nIn the marketplace')
	me.x,me.y = 0,0
	callfrom = call
	keyHandle(village,-1,-1,-1,'store')
"""
def keyHandle(grid, pasx, pasy,next_lev,call): #pasy and pasx = spot to win
	while True:
		i = input('\nAction: ')
		if i == 'w' or i == 'W':
			me.y+=yp
			try:
				print('You walk forward and see '+grid[me.y][me.x].pview, end='')			
			except:
				me.y+=ym
				print("Bonk! You can't go that way.")
		elif i == 's' or i == 'S':
			me.y+=ym
			try:
				if me.y>=0:
					print('You take a few steps backward and turn around. You see '+grid[me.y][me.x].pview, end='')				
				else:
					me.y+=yp
					print("Bonk! You can't go that way!")
			except:
				me.y+=yp
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
			if musc == True:
				m_chan.pause()
				s_chan.play(seffect2)
				me.hp = atthandle(grid,me.x,me.y,me)
				s_chan.stop()
				m_chan.unpause()
			else:
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
		elif grid[me.y][me.x].name in interlist:
			me.wallet = grid[me.y][me.x].act(me.invent,me.wallet)
		elif grid[me.y][me.x].name == 'level':
			print("-"*80)
			if grid[me.y][me.x].num == 1 and grid[me.y][me.x].locked == False:
				Adventure1(0,0,True)
			elif grid[me.y][me.x].num == 2 and grid[me.y][me.x].locked == False:
				Adventure2(0,0,True)
				#add more for more levels
		#music
		if m_chan.get_busy() == False and musc == True:
			randnum = random.randint(0,11)
			m_chan.play(playlist[randnum])
			
		if me.x == pasx and me.y == pasy:
			print("-"*80)
			me.hp = 100
			me.x = 0
			me.y = 0
			if next_lev == 2:
				village[5][1].locked = False
			elif next_lev == 3:
				village[5][2].locked = False#add more for more levels
			print("LEVEL BEAT! NEXT LEVEL UNLOCKED!")
			print("")
			print("-"*80)
			i = input('Continue story? (Y/n) ')
			if i == 'Y' or i == 'y':
				if next_lev == 2:
					Adventure2(0,0,True)
				elif next_lev == 3:
					Adventure2(0,0,True)
				elif next_lev == 4:
					Adventure2(0,0,True)
				elif next_lev == 5:
					Adventure2(0,0,True)
				elif next_lev == 6:
					Adventure2(0,0,True)
				elif next_lev == 7:
					Adventure2(0,0,True)
			else:
				print('In the Village')
				Village()
def Adventure1(ox,oy,mess):
	#print('In the Caverns has been started.\n')
	me.x, me.y = oldx, oldy
	if mess == True:
		print(before_grid1)
	keyHandle(grid1,4,11,2,'adventure1')
def Adventure2(ox,oy,mess):
	me.x, me.y = oldx, oldy
	#print('A realllly hard maze has been started.\n')
	if mess == True:
		print(before_grid2)
	keyHandle(grid2,2,7,3,'adventure2')
def Village():
	me.x, me.y = 1, 0
	keyHandle(village,-1,-1,-1,'village')
def startScreen():
	randnum = random.randint(0,11)
	m_chan.play(playlist[randnum])
	print('\nWelcome to Zealous Fibula.\n\nCredits:\n    Program: Starfleet Software\n\nPress "h" for help\n')
	Adventure1(0,0,True)
	
inp = input('Inverted controls? (Y,n) ')
if inp == 'Y' or inp == 'y':
	yp, ym = 1, -1
else:
	yp, ym = -1, 1

startScreen()