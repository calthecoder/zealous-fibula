import random, sys
from time import sleep

enemylist = ['Goblin', 'Ogre', 'Giant Spider', 'Dragon', 'Orc']


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
    
    def act(self, p_obj):
        i = random.randint(1,3)
        ret = p_obj # to return
        if i != 3:
            print("\nIt sees you!\n")
            return self.attack(ret) #needs to be here. if 'return' is omitted, it returns None.
        else:
            print("\nThe "+self.name+" does not see you.")
            m = input('Attack or move on? (Q, M) ')
            if m == 'q' or m == 'Q':
                return self.attack(ret)
            else:
                return ret.hp #needs to be ret.hp, not just ret. See changelog, 0.2.4
        
    def attack(self, p_obj):
        ret = p_obj.hp
        #BATTLE TIME!! for 10 secs
        print("Battle starting...\n")
        sleep(5)
        rand = random.randint(1,p_obj.weapon.accuracy)
        if self.hp>p_obj.weapon.dex*p_obj.weapon.damage and rand != p_obj.weapon.accuracy:
                print("*****************The "+self.name+" attacks you!*****************\n*****************He wins!*****************\n\n")
                ret = 0
                sys.exit()
        else:
                print("*****************The "+self.name+" attacks you!*****************\n*****************He loses!*****************\n\n")
                #include a function to turn the enemy into a bspace that says something dead is on the floor
                ret -= (self.hp/3)
                self.died()
        return ret
        
    def died(self):
        self.pview = 'a room with a dead '+self.name+' lying on the ground in a pool of blood'
        self.name = 'bspace'
        self.hp = -1 #diff than bspace
        self.description = 'An empty cave with nothing but a dead beast in it'
#don't forget to change enemylist when add new           
class Goblin(Enemy):
    def __init__(self, y,x):
        super().__init__(name='Goblin',
                         hp=60,
                         description='A normal evil minion which does the general evil bidding of its master.',
                         pview='a hunched over figure with an evil smirk on its face.')
        self.x = x
        self.y = y
        
class Orc(Enemy):
    def __init__(self, y,x):
        super().__init__(name='Orc',
                         hp=70,
                         description='A slightly eviler version of a Goblin.',
                         pview='an ugly orc with a huge sword.')
        self.x = x
        self.y = y
        
class Ogre(Enemy):
    def __init__(self,y,x):
        super().__init__(name='Ogre',
                         hp=85,
                         description='A fairly stupid bloke, all it does is smash anything that moves.',
                         pview='a giant, stupid, upright animal.')
        self.x = x
        self.y = y
        
class GiantSpider(Enemy):
    def __init__(self, y,x):
        super().__init__(name='Giant Spider',
                         hp=125,
                         description='This extremely dangerous beast will split you in half and then suck out your organs.',
                         pview='a three meter tall spider. Venom drips from its fangs and splatters on the ground.')
        self.x = x
        self.y = y
        
class Dragon(Enemy):
    def __init__(self,y,x):
        super().__init__(name='Dragon',
                         hp=500,
                         description='You definetely do not want to cross paths with this dude!!',
                         pview='a huge, flying, firebreathing menace.') 
        self.x = x
        self.y = y
        

#Blanks
class bspace(Enemy):
	def __init__(self,y,x):
		super().__init__(name='bspace',
                                 hp=-1000, 
                                 description='An empty cave room with nothing in it.',
                                 pview='an empty room with nothing in it at all.')
		self.x = x
		self.y = y
class bspace2(Enemy):
    def __init__(self,y,x):
        super().__init__(name='bspace',
                         hp=-1000,
                         description='An empty cave room with nothing in it.',
                         pview='a strange and musty smelling room with green, sticky mold on the walls.')
        self.x = x
        self.y = y
class bspace3(Enemy):
	def __init__(self,y,x):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='An empty cave room with nothing in it.',
                                 pview='a very peculiar looking room. Strange shadows dance on the walls and play tricks with your mind.')
		self.x = x
		self.y = y
class bspace4(Enemy):
	def __init__(self,y,x):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='An empty cave room with nothing in it.', 
                                 pview="a dimmly lit room with a wet floor. Don't slip!")
		self.x = x
		self.y = y
        
class bspace5(Enemy): #for items that were picked up
	def __init__(self,y,x):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='An empty cave room with nothing in it.', 
                                 pview="a room that has no meaning or value; just empty.")
		self.x = x
		self.y = y
class Road(Enemy):
	def __init__(self,y,x):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='Part of a long road.', 
                                 pview="another segment of the road you have been travelling on.")
		self.x = x
		self.y = y
        
##Level gateways
class Level1(Enemy): #for items that were picked up
	def __init__(self,y,x):
		super().__init__(name='level',
                                 hp=-1000,
                                 description='Portal to Level 1.', 
                                 pview="the gateway to Level 1.")
		self.x = x
		self.y = y
		self.locked = False
		self.num = 1
class Level2(Enemy): #for items that were picked up
	def __init__(self,y,x):
		super().__init__(name='level',
                                 hp=-1000,
                                 description='Portal to Level 2.', 
                                 pview="the gateway to Level 2.")
		self.x = x
		self.y = y
		self.locked = True
		self.num = 2
class Level3(Enemy): #for items that were picked up
	def __init__(self,y,x):
		super().__init__(name='level',
                                 hp=-1000,
                                 description='Portal to Level 3.', 
                                 pview="the gateway to Level 3.")
		self.x = x
		self.y = y
		self.locked = True
		self.num = 3
class Level4(Enemy): #for items that were picked up
	def __init__(self,y,x):
		super().__init__(name='level',
                                 hp=-1000,
                                 description='Portal to Level 4.', 
                                 pview="the gateway to Level 4.")
		self.x = x
		self.y = y
		self.locked = True
		self.num = 4
class Level5(Enemy): #for items that were picked up
	def __init__(self,y,x):
		super().__init__(name='level',
                                 hp=-1000,
                                 description='Portal to Level 5.', 
                                 pview="the gateway to Level 5.")
		self.x = x
		self.y = y
		self.locked = True
		self.num = 5