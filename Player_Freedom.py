from Player import *
from MySprite import MySprite
from MySound import MySound
from MyClock import MyClock

class Player_Freedom(Player):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Player.__init__(self,gameDisplay, gameWidth, gameHeight,FPS)
		self.myClockRef = MyClock(FPS)
		self.setUpGlobalSP()
		self.currentMotion = 0
		self.currentWepon = 1
		self.x = 100
		self.y = 100

	def render(self):
		if self.currentMotion == 0:
		    flySP.loop(self.x,self.y,-1)

		elif self.currentMotion == 1:
			slashSP.loop(self.x,self.y,-1)

		elif self.currentMotion == 2:
			if self.currentWepon == 1:
				weapon1SP.loop(self.x,self.y,-1)
			elif self.currentWepon == 2:
				weapon2SP.loop(self.x,self.y,-1)
			elif self.currentWepon == 3:
				weapon3SP.loop(self.x,self.y,-1)
			elif self.currentWepon == 4:
				weapon4SP.loop(self.x,self.y,-1)


	def update(self):
		self.myClockRef.update()
		self.handle_basicMove()
		self.handle_AtkMove()
		self.handle_ChangeWeapon()

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
			self.currentMotion = 1

		if pygame.key.get_pressed()[K_h] and self.currentMotion == 0:
			self.currentMotion = 2

	def handle_ChangeWeapon(self):
		if pygame.key.get_pressed()[K_1]:
			self.currentWepon = 1
		if pygame.key.get_pressed()[K_2]:
			self.currentWepon = 2
		if pygame.key.get_pressed()[K_3]:
			self.currentWepon = 3
		if pygame.key.get_pressed()[K_4]:
			self.currentWepon = 4	

	def resetMove(self):
		if self.currentMotion != 0:
			if self.myClockRef.isSec(1):
				self.currentMotion = 0
