import pygame
from pygame.locals import *
from Player import Player
from MySprite import MySprite
from MySound import MySound

from Beam1 import Beam1
from Beam2 import Beam2
from Beam3 import Beam3
from Beam4 import Beam4
BLUE_COLOR = (0,0,255)

class Player_Freedom(Player):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Player.__init__(self,gameDisplay, gameWidth, gameHeight,FPS)
		self.currentMotion = 0
		self.currentWeapon = 1
		self.x = 100
		self.y = 100
		self.playerSoundTime = 10

	def initBeam(self,gameDisplay,gameWidth,gameHeight):
		beam1Ref = Beam1(gameDisplay,gameWidth,gameHeight)
		beam2Ref = Beam2(gameDisplay,gameWidth,gameHeight)
		beam3Ref = Beam3(gameDisplay,gameWidth,gameHeight)
		beam4Ref = Beam4(gameDisplay,gameWidth,gameHeight)
		self.beamList = [beam1Ref,beam2Ref,beam3Ref,beam4Ref]

	def renderScore(self):
		self.myTextWriterRef.setFontSize(40)
		self.myTextWriterRef.draw("P1 Score: %d"%self.score, 40, 25 ,BLUE_COLOR )

	def renderBeam(self):
		for beam in self.beamList:
			beam.render()

	def updateBeam(self):
		for beam in self.beamList:
			beam.update()

	def renderHP(self):
		if self.HP > 0:
				self.myTextWriterRef.setFontSize(40)
				self.myTextWriterRef.draw("HP: %d"%self.HP, self.x + 30,self.y -30 ,BLUE_COLOR )

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

		elif self.currentMotion == 4:
			self.SPList[4].loop(self.x,self.y,-1)

		elif self.currentMotion == 5:
			self.SPList[5].loop(self.x,self.y,-1)

		elif self.currentMotion == 6:
			self.SPList[6].loop(self.x,self.y,-1)

	def initSP(self):
		flySP = MySprite(self.gameDisplay,"res/sprites/freedomFlySP.png",2,225,175)
		slashSP = MySprite(self.gameDisplay,"res/sprites/freedomSlashSP.png",2,225,175)
		weapon1SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon1SP.png",2,225,175)
		weapon2SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon2SP.png",2,225,175)
		weapon3SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon3SP.png",2,225,175)
		weapon4SP = MySprite(self.gameDisplay,"res/sprites/freedomWeapon4SP.png",2,225,175)
		shieldSP = MySprite(self.gameDisplay,"res/sprites/freedomShield.png",2,225,175)
		self.SPList = [flySP,weapon1SP,weapon2SP,weapon3SP,weapon4SP,slashSP,shieldSP]

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
		if pygame.key.get_pressed()[K_k] and self.currentMotion == 0:
			self.currentMotion = 5
			self.slashSound.play()

		if pygame.key.get_pressed()[K_j] and self.currentMotion == 0:
				self.currentMotion = 6
				self.slashSound.play()

		if pygame.key.get_pressed()[K_h] and self.currentMotion == 0:
			if self.currentWeapon == 1:
				self.currentMotion = 1
				self.beamList[0].setPos(self.x + 170 ,self.y + 80)

			elif self.currentWeapon == 2:
				self.currentMotion = 2
				self.beamList[1].setPos(self.x + 170 ,self.y + 90)

			elif self.currentWeapon == 3:
				self.currentMotion = 3
				self.beamList[2].setPos(self.x + 170 ,self.y + 20)

			elif self.currentWeapon == 4:
				self.currentMotion = 4
				self.beamList[3].setPos(self.x + 170 ,self.y + 30)

	def handle_ChangeWeapon(self):
		if pygame.key.get_pressed()[K_1]:
			self.currentWeapon = 1
		if pygame.key.get_pressed()[K_2]:
			self.currentWeapon = 2
		if pygame.key.get_pressed()[K_3]:
			self.currentWeapon = 3
		if pygame.key.get_pressed()[K_4]:
			self.currentWeapon = 4	

