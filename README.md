# zealous-fibula
A text based game

Credits: Starfleet Software

CHANGELOG:
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