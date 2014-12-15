from MySprite import MySprite
from MyClock import MyClock
from MySound import MySound
from random import *

class Enemy:
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.FPS = FPS
		self.myClockRef = MyClock(FPS)
		self.boomSound = MySound("res/sounds/boomSound.ogg")
		self.damageSound = MySound("res/sounds/damage1Sound.ogg")
		self.x = self.gameWidth
		self.y = self.gameHeight/2
		self.isAlive = False
		self.randomRebornTime = randint(4,10)
		self.randomShootTime = randint(3,6)
		self.power = 10
		self.randomBoundaryTop = self.gameHeight/2 - randint(100,300)
		self.randomBoundaryBot = self.gameHeight/2 + randint(100,300)
		self.moveUP = True
		self.moveDown = True
		self.isBoss = False
 
	def render(self):
		self.SP.loop(self.x,self.y,-1)
		self.beam.renderEnemyBeam()

	def update(self):
		self.myClockRef.update()
		if not self.isAlive and self.myClockRef.isSec(self.randomRebornTime):
			self.setPos(self.gameWidth,randint(1,self.gameHeight-225))
		if self.isAlive:
			self.enemyMove()
			self.enemyShoot()

		if self.getHP() < 0 :
			self.isAlive = False
			self.resetPos()
			
		self.beam.updateEnemyBeam()

	def enemyMove(self):
			if self.x > self.gameWidth/2 + 175:
				self.x -= self.speed
			else:
				if self.moveUP:
					self.y -= self.speed
					if self.y < self.randomBoundaryTop or self.y < 0:
						self.moveUP = False
						self.moveDown = True
				elif self.moveDown:
					self.y += self.speed
					if self.y > self.randomBoundaryBot or self.y > self.gameHeight-225:
						self.moveDown = False
						self.moveUP = True
	
	def enemyShoot(self):
		if self.myClockRef.isSec(self.randomShootTime):
			self.beam.setPos(self.x-100,self.y + 100)


	def getHP(self):
		return self.HP

	def HPdamage(self,damage):
		#self.damageSound.play()
		self.HP -= damage

	def setPos(self,x,y):
		self.isAlive = True
		self.x = x 
		self.y = y

	def resetPos(self):
		self.boomSound.play()
		self.speed += 0.5
		self.x = self.gameWidth
		self.y = -500 
		self.HP = self.maxHP
		self.randomRebornTime = randint(1,10)
		self.randomShootime = randint(2,10)
		self.randomBoundaryTop = self.gameHeight/2 - randint(100,300)
		self.randomBoundaryBot = self.gameHeight/2 + randint(100,300)


	def initSP(self,path,total,width,height):
		self.SP = MySprite(self.gameDisplay,path,total,width,height)
