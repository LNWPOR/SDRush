from MySprite import MySprite
from MySound import MySound
class Beam:
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.resetPos()

	def render(self):
		self.beamSP.loop(self.x,self.y,-1)

	def renderEnemyBeam(self):
		self.enemyBeamSP.loop(self.x,self.y,-1)

	def update(self):
		if self.y >= 0:
			self.x += self.speed

		if self.x > self.gameWidth:
			self.resetPos()

	def updateEnemyBeam(self):
		if self.y >= 0:
			self.x -= self.speed

		if self.x < -200:
			self.resetPos()


	def setPos(self,x,y):
		self.beamSound.play()
		self.x = x 
		self.y = y

	def resetPos(self):
		self.x = -500
		self.y = -500

	def initSP(self,path,total,width,height):
		self.beamSP = MySprite(self.gameDisplay,path,total,width,height)

	def initEnemySP(self,path,total,width,height):
		self.enemyBeamSP = MySprite(self.gameDisplay,path,total,width,height)


	def initSound(self,path):
		self.beamSound = MySound(path)
