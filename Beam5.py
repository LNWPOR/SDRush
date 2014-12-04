from Beam import Beam


class Beam5(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 25
		self.initSP("res/sprites/Beam5.png",3,75,50)
		self.initSound("res/sounds/beam5Sound.ogg")
