from Player import *
from MySprite import MySprite
from MySound import MySound
from MyClock import MyClock
from Beam1 import Beam1
from Beam2 import Beam2
from Beam3 import Beam3
from Beam4 import Beam4

class Player_Freedom(Player):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Player.__init__(self,gameDisplay, gameWidth, gameHeight,FPS)
		self.myClockRef = MyClock(FPS)
		self.setUpGlobalSP()
		self.currentMotion = 0
		self.currentWeapon = 1
		self.x = 100
		self.y = 100
		self.initBeam(gameDisplay, gameWidth, gameHeight)

	def initBeam(self,gameDisplay,gameWidth,gameHeight):
		self.beam1Ref = Beam1(gameDisplay,gameWidth,gameHeight)
		self.beam2Ref = Beam2(gameDisplay,gameWidth,gameHeight)
		self.beam3Ref = Beam3(gameDisplay,gameWidth,gameHeight)
		self.beam4Ref = Beam4(gameDisplay,gameWidth,gameHeight)

	def render(self):
		if self.currentMotion == 0:
		    flySP.loop(self.x,self.y,-1)

		elif self.currentMotion == 1:
			weapon1SP.loop(self.x,self.y,-1)
		
		elif self.currentMotion == 2:
			weapon2SP.loop(self.x,self.y,-1)

		elif self.currentMotion == 3:
			weapon3SP.loop(self.x,self.y,-1)

		elif self.currentMotion == 4:
			weapon4SP.loop(self.x,self.y,-1)

		elif self.currentMotion == 5:
			slashSP.loop(self.x,self.y,-1)

		self.beam1Ref.render()
		self.beam2Ref.render()
		self.beam3Ref.render()
		self.beam4Ref.render()

	def update(self):
		self.myClockRef.update()
		self.handle_basicMove()
		self.handle_AtkMove()
		self.handle_ChangeWeapon()

		self.beam1Ref.update()
		self.beam2Ref.update()
		self.beam3Ref.update()
		self.beam4Ref.update()
		self.resetMove()

	def setUpGlobalSP(self):
		global flySP,slashSP,weapon1SP,weapon2SP,weapon3SP,weapon4SP
		flySP = MySprite(self.gameDisplay,"res/sprites/freedomFlySP.png",2,225,175)
		slashSP = MySprite(self.gameDisplay,"res/sprites/freedomSlashSP.png",2,225,175)
		weapon1SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon1SP.png",2,225,175)
		weapon2SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon2SP.png",2,225,175)
		weapon3SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon3SP.png",2,225,175)
		weapon4SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon4SP.png",2,225,175)

	def handle_basicMove(self):
		if pygame.key.get_pressed()[K_w]:
			self.moveUp()
		if pygame.key.get_pressed()[K_s]:
			self.moveDown()
		if pygame.key.get_pressed()[K_d]:
			self.moveRight()
		if pygame.key.get_pressed()[K_a]:
			self.moveLeft()

	def handle_AtkMove(self):
		if pygame.key.get_pressed()[K_j] and self.currentMotion == 0:
			self.currentMotion = 5

		if pygame.key.get_pressed()[K_h] and self.currentMotion == 0:
			if self.currentWeapon == 1:
				self.currentMotion = 1
				self.beam1Ref.setPos(self.x + 170 ,self.y + 80)

			elif self.currentWeapon == 2:
				self.currentMotion = 2
				self.beam2Ref.setPos(self.x + 170 ,self.y + 90)

			elif self.currentWeapon == 3:
				self.currentMotion = 3
				self.beam3Ref.setPos(self.x + 170 ,self.y + 20)

			elif self.currentWeapon == 4:
				self.currentMotion = 4
				self.beam4Ref.setPos(self.x + 170 ,self.y + 20)

	def handle_ChangeWeapon(self):
		if pygame.key.get_pressed()[K_1]:
			self.currentWeapon = 1
		if pygame.key.get_pressed()[K_2]:
			self.currentWeapon = 2
		if pygame.key.get_pressed()[K_3]:
			self.currentWeapon = 3
		if pygame.key.get_pressed()[K_4]:
			self.currentWeapon = 4	

	def resetMove(self):
		if self.currentMotion != 0:
			if self.myClockRef.isSec(1):
				self.currentMotion = 0
