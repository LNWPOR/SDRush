from Beam import Beam


class Beam2(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 10
		self.initSP("res/sprites/Beam2.png",3,150,40)
		self.initSound("res/sounds/beam2Sound.ogg")
		self.initEnemySP("res/sprites/enemyBeam2.png",3,150,40)

