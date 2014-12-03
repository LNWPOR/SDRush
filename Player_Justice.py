from Player import *
from MySprite import MySprite
from MySound import MySound
from MyClock import MyClock
from Beam1 import Beam1
from Beam2 import Beam2
from Beam3 import Beam3
from Beam5 import Beam5

class Player_Justice(Player):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Player.__init__(self,gameDisplay, gameWidth, gameHeight,FPS)
		self.myClockRef = MyClock(FPS)
		self.setUpGlobalSP()
		self.currentMotion = 0
		self.currentWeapon = 1
		self.x = 100
		self.y = 400
		self.initBeam(gameDisplay, gameWidth, gameHeight)

	def initBeam(self,gameDisplay,gameWidth,gameHeight):
		self.beam1Ref = Beam1(gameDisplay,gameWidth,gameHeight)
		self.beam2Ref = Beam2(gameDisplay,gameWidth,gameHeight)
		self.beam3Ref = Beam3(gameDisplay,gameWidth,gameHeight)
		self.beam5Ref = Beam5(gameDisplay,gameWidth,gameHeight)
	def renderBeam(self):
		self.beam1Ref.render()
		self.beam2Ref.render()
		self.beam3Ref.render()
		self.beam5Ref.render()

	def render(self):
		if self.currentMotion == 0:
		    self.flySP.loop(self.x,self.y,-1)

		elif self.currentMotion == 1:
			self.weapon1SP.loop(self.x,self.y,-1)
		
		elif self.currentMotion == 2:
			self.weapon2SP.loop(self.x,self.y,-1)

		elif self.currentMotion == 3:
			self.weapon3SP.loop(self.x,self.y,-1)

		elif self.currentMotion == 5:
			self.slashSP.loop(self.x,self.y,-1)

		self.renderBeam()

	def updateBeam(self):
		self.beam1Ref.update()
		self.beam2Ref.update()
		self.beam3Ref.update()
		self.beam5Ref.update()

	def update(self):
		self.myClockRef.update()
		self.handle_basicMove()
		self.handle_AtkMove()
		self.handle_ChangeWeapon()

		self.updateBeam()
		self.resetMove()

	def setUpGlobalSP(self):
		self.flySP = MySprite(self.gameDisplay,"res/sprites/justiceFlySP.png",2,225,175)
		self.slashSP = MySprite(self.gameDisplay,"res/sprites/justiceSlashSP.png",2,225,175)
		self.weapon1SP = MySprite(self.gameDisplay,"res/sprites/justiceWeapon1SP.png",2,225,175)
		self.weapon2SP = MySprite(self.gameDisplay,"res/sprites/justiceWeapon2SP.png",2,225,175)
		self.weapon3SP = MySprite(self.gameDisplay,"res/sprites/justiceWeapon3SP.png",2,225,175)

	def handle_basicMove(self):
		if pygame.key.get_pressed()[K_UP]:
			self.moveUp()
		if pygame.key.get_pressed()[K_DOWN]:
			self.moveDown()
		if pygame.key.get_pressed()[K_RIGHT]:
			self.moveRight()
		if pygame.key.get_pressed()[K_LEFT]:
			self.moveLeft()

	def handle_AtkMove(self):
		if pygame.mouse.get_pressed() == (0,0,1) and self.currentMotion == 0:
			self.currentMotion = 5

		if pygame.mouse.get_pressed() == (1,0,0) and self.currentMotion == 0:
			if self.currentWeapon == 1:
				self.currentMotion = 1
				self.beam1Ref.setPos(self.x + 170 ,self.y + 80)

			elif self.currentWeapon == 2:
				self.currentMotion = 2
				self.beam2Ref.setPos(self.x + 170 ,self.y + 90)

			elif self.currentWeapon == 3:
				self.currentMotion = 3
				self.beam5Ref.setPos(self.x + 170 ,self.y + 20)

	def handle_ChangeWeapon(self):
		if pygame.key.get_pressed()[K_RCTRL]:
			self.currentWeapon = 1
		if pygame.key.get_pressed()[K_RSHIFT]:
			self.currentWeapon = 2
		if pygame.key.get_pressed()[K_RETURN]:
			self.currentWeapon = 3

	def resetMove(self):
		if self.currentMotion != 0:
			if self.myClockRef.isSec(1):
				self.currentMotion = 0
