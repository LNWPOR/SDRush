from Beam import Beam


class Beam4(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 25
		self.initSP("res/sprites/Beam4.png",3,150,90)
