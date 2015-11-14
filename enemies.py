import random, sys

enemylist = ['Goblin', 'Ogre', 'Giant Spider', 'Dragon']


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
    
    def act(self, php):
        i = random.randint(1,3)
        ret = php # to return
        if i != 3:
            print("\nIt sees you!\n")
            return self.attack(ret) #needs to be here. if 'return' is omitted, it returns None.
        else:
            print("The "+self.name+" does not see you.")
            m = input('Attack or move on? (Q, M) ')
            if m == 'q' or m == 'Q':
                return self.attack(ret)
            else:
                return ret
        
    def attack(self, php):
        ret = php
        if self.hp>ret:
                print("*****************The "+self.name+" attacks you!*****************\n*****************He wins!*****************\n\n")
                ret = 0
        elif self.hp <=ret:
                print("*****************The "+self.name+" attacks you!*****************\n*****************He loses!*****************\n\n")
                #include a function to turn the enemy into a bspace that says something dead is on the floor
                ret -= (self.hp/3)
                self.died()
        return ret
        
    def died(self):
        self.pview = 'a room with a dead '+self.name+' lying on the ground in a pool of blood'
        self.name = 'bspace'
        self.hp = -1000
        self.description = 'An empty cave with nothing but a dead beast in it'
                
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
		super().__init__(name='bspace',
                                 hp=-1000, 
                                 description='An empty cave room with nothing in it.',
                                 pview='an empty room with nothing in it at all.')
		self.x = x
		self.y = y
class bspace2(Enemy):
    def __init__(self, x, y):
        super().__init__(name='bspace',
                         hp=-1000,
                         description='An empty cave room with nothing in it.',
                         pview='a strange and musty smelling room with green, sticky mold on the walls.')
        self.x = x
        self.y = y
class bspace3(Enemy):
	def __init__(self, x, y):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='An empty cave room with nothing in it.',
                                 pview='a very peculiar looking room. Strange shadows dance on the walls and play tricks with your mind.')
		self.x = x
		self.y = y
class bspace4(Enemy):
	def __init__(self, x, y):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='An empty cave room with nothing in it.', 
                                 pview="a dimmly lit room with a wet floor. Don't slip!")
		self.x = x
		self.y = y
        
class bspace5(Enemy): #for items that were picked up
	def __init__(self, x, y):
		super().__init__(name='bspace',
                                 hp=-1000,
                                 description='An empty cave room with nothing in it.', 
                                 pview="a room that has no meaning or value; just empty.")
		self.x = x
		self.y = y