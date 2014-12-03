from Beam import Beam


class Beam3(Beam):
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		Beam.__init__(self,gameDisplay,gameWidth,gameHeight)
		self.speed = 100
		self.power = 10
		self.setUpSP("res/sprites/Beam3.png",3,150,40)

