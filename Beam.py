from MySprite import MySprite
class Beam:
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.resetPos()

	def render(self):
		self.beamSP.loop(self.x,self.y,-1)

	def update(self):
		if self.y > 0:
			self.x += self.speed

		if self.x > self.gameWidth:
			self.resetPos()

	def setPos(self,x,y):
		self.x = x 
		self.y = y

	def resetPos(self):
		self.x = 0
		self.y = -500

	def setUpSP(self,path,num,width,height):
		self.beamSP = MySprite(self.gameDisplay,path,num,width,height)