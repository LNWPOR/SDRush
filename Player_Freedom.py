from Player import Player
from MySprite import MySprite
from MySound import MySound

class Player_Freedom(Player):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Player.__init__(self,gameDisplay, gameWidth, gameHeight)
		self.setUpGlobalSP()

	def render(self):
		flySP.loop(100,100,-1)

	def update(self):
		pass

	def setUpGlobalSP(self):
		global flySP
		flySP = MySprite(self.gameDisplay,"res/sprites/freedomFlySP.png",2,225,175)