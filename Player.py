import pygame
from pygame.locals import *
from MySprite import MySprite
from MySound import MySound

class Player:
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.setUpGlobalHP()
		self.speed = 1
		
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