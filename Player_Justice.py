import pygame
from pygame.locals import *
from Player import Player
from MySprite import MySprite
from MySound import MySound

from Beam1 import Beam1
from Beam2 import Beam2
from Beam5 import Beam5
RED_COLOR = (240,0,0)

class Player_Justice(Player):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Player.__init__(self,gameDisplay, gameWidth, gameHeight,FPS)
		self.currentMotion = 0
		self.currentWeapon = 1
		self.x = 100
		self.y = 400
		self.playerSoundTime = 7

	def initBeam(self,gameDisplay,gameWidth,gameHeight):
		beam1Ref = Beam1(gameDisplay,gameWidth,gameHeight)
		beam2Ref = Beam2(gameDisplay,gameWidth,gameHeight)
		beam5Ref = Beam5(gameDisplay,gameWidth,gameHeight)
		self.beamList = [beam1Ref,beam2Ref,beam5Ref]

	def renderScore(self):
		self.myTextWriterRef.setFontSize(40)
		self.myTextWriterRef.draw("P2 Score: %d"%self.score, self.gameWidth/2 - 50, 25 ,RED_COLOR )

	def renderBeam(self):
		for beam in self.beamList:
			beam.render()

	def renderHP(self):
		if self.HP > 0:
				self.myTextWriterRef.setFontSize(40)
				self.myTextWriterRef.draw("HP: %d"%self.HP, self.x + 50,self.y -30 ,RED_COLOR )

	def renderSP(self):
		if self.currentMotion == 0:
		    self.SPList[0].loop(self.x,self.y,-1)
		    for sp in self.SPList:
		    	if sp != self.SPList[0]:
		    		sp.setRectPos(self.x,self.y)

		elif self.currentMotion == 1:
			self.SPList[1].loop(self.x,self.y,-1)
		
		elif self.currentMotion == 2:
			self.SPList[2].loop(self.x,self.y,-1)

		elif self.currentMotion == 3:
			self.SPList[3].loop(self.x,self.y,-1)

		elif self.currentMotion == 5:
			self.SPList[4].loop(self.x,self.y,-1)

		elif self.currentMotion == 6:
			self.SPList[5].loop(self.x,self.y,-1)

	def updateBeam(self):
		for beam in self.beamList:
			beam.update()

	def initSP(self):
		flySP = MySprite(self.gameDisplay,"res/sprites/justiceFlySP.png",2,225,175)
		slashSP = MySprite(self.gameDisplay,"res/sprites/justiceSlashSP.png",2,225,175)
		weapon1SP = MySprite(self.gameDisplay,"res/sprites/justiceWeapon1SP.png",2,225,175)
		weapon2SP = MySprite(self.gameDisplay,"res/sprites/justiceWeapon2SP.png",2,225,175)
		weapon3SP = MySprite(self.gameDisplay,"res/sprites/justiceWeapon3SP.png",2,225,175)
		shieldSP = MySprite(self.gameDisplay,"res/sprites/justiceShield.png",2,225,175)
		self.SPList = [flySP,weapon1SP,weapon2SP,weapon3SP,slashSP,shieldSP]

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
			self.slashSound.play()

		if pygame.mouse.get_pressed() == (0,1,0) and self.currentMotion == 0:
			self.currentMotion = 6
			self.slashSound.play()

		if pygame.mouse.get_pressed() == (1,0,0) and self.currentMotion == 0:
			if self.currentWeapon == 1:
				self.currentMotion = 1
				self.beamList[0].setPos(self.x + 170 ,self.y + 80)

			elif self.currentWeapon == 2:
				self.currentMotion = 2
				self.beamList[1].setPos(self.x + 170 ,self.y + 90)

			elif self.currentWeapon == 3:
				self.currentMotion = 3
				self.beamList[2].setPos(self.x + 170 ,self.y + 20)

	def handle_ChangeWeapon(self):
		if pygame.key.get_pressed()[K_RCTRL]:
			self.currentWeapon = 1
		if pygame.key.get_pressed()[K_RSHIFT]:
			self.currentWeapon = 2
		if pygame.key.get_pressed()[K_RETURN]:
			self.currentWeapon = 3

