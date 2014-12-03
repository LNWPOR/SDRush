import pygame
from pygame.locals import *
from MySprite import MySprite
from MySound import MySound

class Player:
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.FPS = FPS
		self.setUpGlobalHP()
		self.x = 0
		self.y = 0
		self.speed = 10
		
	def render(self):
		pass

	def update(self):
		pass

	def setUpGlobalHP(self):
		global HP
		HP = 100

	def HPdamage(self,damage):
		global HP
		HP -= damage

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