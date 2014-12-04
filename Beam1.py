from Beam import Beam


class Beam1(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 5
		self.initSP("res/sprites/Beam1.png",3,150,20)
		self.initSound("res/sounds/beam1Sound.ogg")
		self.beamSound.setVolume(0.5)
		self.initEnemySP("res/sprites/enemyBeam1.png",3,150,20)


