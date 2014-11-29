import pygame
from pygame.locals import *

class MyTextWriter:
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.fontType = None
		self.fontSize = 80
		self.font = pygame.font.SysFont(self.fontType,self.fontSize)
		self.text = 0

	def draw(self,text,x,y,color = (0,0,0)):
		self.text = self.font.render(text,True,color)
		self.gameDisplay.blit(self.text,(x,y))

	def setFontType(self,fontType):
		self.fontType = fontType

	def setFontSize(self,fontSize):
		self.fontSize = fontSize

