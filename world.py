from enemies import *
from items import *
from interactives import *

village = [
	[Fletcher(0,0),Road(0,1),Blacksmith(0,2)],
	['',Road(1,1),''],
	['',Road(2,1),''],
	['',Road(3,1),''],
	[Road(4,0),Road(4,1),Road(4,2),Road(4,3)],
	[Level1(5,0),Level2(5,1),Level3(5,2),Level4(5,3)]
]
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
	[GiantSpider(2,0),Ogre(2,1),bspace4(2,2),'','','','',Gold(200,2,7)], #win spot
	['',bspace(3,1),'','',Dragon(3,4),'',Goblin(3,6),bspace(3,7)],
	['',bspace2(4,1),'','',bspace3(4,4),bspace4(4,5),bspace2(4,6)],
	[bspace(5,0),bspace4(5,1),Goblin(5,2),bspace(5,3),bspace3(5,4)],
	[bspace3(6,0),'',''],
	[bspace2(7,0),bspace(7,1),''],
	['',Dragon(8,1),'']

]
grid3 = [
	[bspace(0,0)],
	[Orc(1,0),bspace4(1,1),'',Ogre(1,3)],
	['',Goblin(2,1),bspace2(2,2),bspace3(2,3)],
	['','',Ogre(3,2),bspace(3,3)],
	['',Gold(30,4,1),GiantSpider(5,2)]
]
grid4 = [
	[bspace4(0,0),Dragon(0,1),bspace(0,2),'',Gold(78,0,4)],
	[Orc(1,0),bspace2(1,1),Goblin(1,2),bspace3(1,3),bspace4(1,4)],
	[bspace(2,0)],
	[Orc(3,0),bspace4(3,1),'',Ogre(3,3)],
	['',Goblin(4,1),bspace(4,2),bspace3(4,3)],
	['','',bspace2(5,2),bspace(5,3)],
	['',Gold(30,6,1),Orc(6,2)]
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
before_grid2 = """
Light! You see light! Bright rays of sunshine illuminate the cave where
you stand. A long, spiral staircase winds up through the
ceiling. You climb up the staircase. Soon, you reach the top.
Your home is visible from the top of this hill. You begin to walk
to it through the woods.
"""
before_grid3 = """
When you arrive at the your home village, there is nobody there. 
Your home and the others homes are in flames. Your neighbors lie 
dead on the ground. The assailants left tracks leading into the 
mines near your town. You follow the tracks in hopes of destroying
them and their master.
"""
before_grid4 = """
The orcs finally stop moving. They make their camp for the night in a dank 
cave room. You watch them for a while. They keep staring right at the rock 
you are hiding behind. It is late. You go to sleep. When you wake up in the
morning, they are gone. You rush to try and catch them.
"""