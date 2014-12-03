from Beam import Beam


class Beam2(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 10
		self.setUpSP("res/sprites/Beam2.png",3,150,40)


