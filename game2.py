import player, sys, random
#from world import Tile
#from enemies import *
from items import *


namelist = ['Goblin', 'Ogre', 'Giant Spider', 'Dragon']

""" #goes lower
        elif x == 0:
            print("****************The "+self.name+" attacks you!****************\n\nHe loses!\n")
            php -= (self.hp/2)
            self.hp = 0
            return 'Alive'
""" 

me=player.Player()


x,y=0,0

class Enemy:
    '''A base class for all enemies'''
    def __init__(self, name, hp, description, pview):
        '''Creates a new enemy

        :param name: the name of the enemy
        :param hp: the hit points of the enemy
        :param description: the description the enemy does with each attack
        '''
        self.name = name
        self.hp = hp
        self.description = description
        self.pview = pview

    def is_alive(self):
        return self.hp > 0
    """
    def sees(self, php):
        i = random.randint(1,3)
        if i != 3:
            print("\nIt sees you!\n")
            self.attack(php)
        else:
            print("The "+self.name+" does not see you.")
            m = input('Attack or move on? ')
            if m == 'q' or m == 'Q':
                self.attack(php)
            
    def attack(self, php): #greater advantage if you attack first
        #x = random.randint(0,3)
        if self.hp > php: #and x >=1: #for now, hp = damage too
            print("****************The "+self.name+" attacks you!****************\n\n****************He wins!****************\n\nYou are crying. Boohoohoohoohoo!\n\n")
            return False
            php = 0
        if self.hp < php:
            print("****************The "+self.name+" attacks you!****************\n\nHe loses!\n\n")
            php -= (self.hp/2)
            self.hp = 0
            return True
    """
    def test(self, php):
        self.iphp = php
		self.iphp = 0
        print('me.hp (passed as "php" in enemies) = '+str(self.iphp))
        
class Goblin(Enemy):
    def __init__(self, x, y):
        super().__init__(name='Goblin',
                         hp=20,
                         description='A normal evil minion which does the general evil bidding of its master.',
                         pview='a hunched over figure with an evil smirk on its face.')
        self.x = x
        self.y = y
        
class Ogre(Enemy):
    def __init__(self, x, y):
        super().__init__(name='Ogre',
                         hp=30,
                         description='A fairly stupid bloke, all it does is smash anything that moves.',
                         pview='a giant, stupid, upright animal.')
        self.x = x
        self.y = y
        
class GiantSpider(Enemy):
    def __init__(self, x, y):
        super().__init__(name='Giant Spider',
                         hp=60,
                         description='This extremely dangerous beast will split you in half and then suck out your organs.',
                         pview='a three meter tall spider. Venom drips from its fangs and splatters on the ground.')
        self.x = x
        self.y = y
        
class Dragon(Enemy):
    def __init__(self, x, y):
        super().__init__(name='Dragon',
                         hp=300,
                         description='You definetely do not want to cross paths with this dude!!',
                         pview='a huge, flying, firebreathing menace.') 
        self.x = x
        self.y = y
        

#Blanks
class bspace(Enemy):
	def __init__(self, x, y):
		super().__init__(name='bspace', hp=None, description='An empty cave room with nothing in it.', pview='an empty room with nothing in it at all.')
		self.x = x
		self.y = y
class bspace2(Enemy):
    def __init__(self, x, y):
        super().__init__(name='bspace', hp=None, description='An empty cave room with nothing in it.', pview='a strange and musty smelling room with green, sticky mold on the walls.')
        self.x = x
        self.y = y
class bspace3(Enemy):
	def __init__(self, x, y):
		super().__init__(name='bspace', hp=None, description='An empty cave room with nothing in it.', pview='a very peculiar looking room. Strange shadows dance on the walls and play tricks with your mind.')
		self.x = x
		self.y = y
class bspace4(Enemy):
	def __init__(self, x, y):
		super().__init__(name='bspace', hp=None, description='An empty cave room with nothing in it.', pview="a dimmly lit room with a wet floor. Don't slip!")
		self.x = x
		self.y = y

"""
def atthandle(l,x,y,playhp):
	if l[y][x].name in namelist:
		l[y][x].sees(playhp)
"""		

grid = [
	[bspace(0,0),Goblin(0,1),bspace(0,2)],
	[Dragon(1,0),bspace2(1,1),bspace3(1,2)],
	[GiantSpider(2,0),Ogre(2,1),bspace4(2,2)],
	['',bspace(3,1),''],
	['',bspace2(4,1),''],
	[bspace(5,0),bspace4(5,1),''],
	[bspace3(6,0),'',''],
	[bspace2(7,0),bspace(7,1),''],
	['',bspace4(8,1),''],
	['',Gold(10,9,1),''],
	[bspace2(10,0),bspace3(10,1),bspace(10,2),Ogre(10,3)],
	['','','',bspace(11,3),bspace(11,4)]
	
]

x = Dragon(1,2)
x.test(me.hp)
print('me.hp in game = '+str(me.hp))

while True:
	i = input('Action: ')
	if i == 'w' or i == 'W':
		y+=1
		try:
			print('You walk forward and see '+grid[y][x].pview)
						
		except:
			y-=1
			print("Bonk! You can't go that way.")
	elif i == 's' or i == 'S':
		y-=1
		try:
			if y>=0:
				print('You take a few steps backward and turn around. You see '+grid[y][x].pview)
			else:
				y+=1
				print("Bonk! You can't go that way!")
		except:
			y+=1
			print("Bonk! You can't go that way.")
	elif i == 'd' or i == 'D':
		x+=1
		try:
			print('You walk to the rightmost room and see '+grid[y][x].pview)
		except:
			x-=1
			print("Bonk! You can't go that way.")
	elif i == 'a' or i == 'A':
		x-=1
		try:
			if x>=0:
				print('You turn around and walk to the left. In front of you, you see '+grid[y][x].pview)
			else:
				x+=1
				print("Bonk! You can't go that way.")				
		except:
			x+=1
			print("Bonk! You can't go that way.")
	else:
		print('Huh?')
	
	############
	if me.isAlive() == False:
		sys.exit()
	############
	
	if x == 4 and y == 11:
		print("\n\n\n\n\n\n\n******************You Win!!!!!!!****************\n\n\n\n\n\n\n\n")
		break