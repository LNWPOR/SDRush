from MySound import MySound
from MyClock import MyClock
class Player:
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.FPS = FPS
		self.HP = 1000
		self.speed = 30
		self.power = 10
		self.slashSound = MySound("res/sounds/slashSound.ogg")
		self.damageSound = MySound("res/sounds/damage1Sound.ogg")
		self.initSP()
		self.myClockRef = MyClock(FPS)
		self.initBeam(gameDisplay, gameWidth, gameHeight)
		self.score = 0

	def render(self):
			self.renderSP()
			self.renderBeam()

	def update(self):
		self.myClockRef.update()
		if self.HP > 0:
			self.handle_basicMove()
			self.handle_AtkMove()
			self.handle_ChangeWeapon()
			self.updateBeam()
			self.resetMove()
		else:
			self.x = -3000
			self.y = -3000
			self.currentMotion = 0

	def getHP(self):
		return self.HP

	def HPdamage(self,damage):
		self.damageSound.play()
		self.HP -= damage

	def moveUp(self):
		if self.y > 0:
			self.y -= self.speed

	def moveDown(self):
		if self.y < self.gameHeight-175:
			self.y += self.speed

	def moveRight(self):
		if self.x < self.gameWidth-450:
			self.x += self.speed

	def moveLeft(self):
		if self.x > 0:
			self.x -= self.speed

	def initSP(self):
		pass

	def initBeam(self):
		pass

	def handle_basicMove(self):
		pass

	def handle_AtkMove(self):
		pass

	def handle_ChangeWeapon(self):
		pass

	def updateBeam(self):
		pass

	def resetMove(self):
		if self.currentMotion != 0:
			if self.myClockRef.isSec(1):
				self.currentMotion = 0

	def renderBeam(self):
		pass

	def renderSP(self):
		pass