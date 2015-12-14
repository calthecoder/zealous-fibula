from enemies import *
from items import *
from interactives import *

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
	['',bspace(3,1),'','',Dragon(3,4),'',Goblin(3,6),bspace(3,7)],
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
before_grid2 = """
Light! You see light! Bright rays of sunshine illuminate the cave where
the Spider had been defeated. A long, spiral staircase winds up through the
ceiling. You step over the dead Giant Spider and climb up the staircase.
Soon, you reach the top. Your village is visible from the top of this hill.
You walk to it.
"""