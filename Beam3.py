from Beam import Beam


class Beam3(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 10
		self.initSP("res/sprites/Beam3.png",3,150,40)
		self.initSound("res/sounds/beam3Sound.ogg")
		self.initEnemySP("res/sprites/enemyBeam3.png",3,150,40)
