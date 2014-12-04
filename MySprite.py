import pygame
from pygame.locals import *

class MySprite():

	def __init__(self,gameDisplay,sp_Path,sp_Total = 1,sp_Width = 0,sp_Height = 0):
		self.gameDisplay = gameDisplay
		self.SP = pygame.image.load(sp_Path)
		self.SPconvert = self.SP.convert()
		self.SPcollider = self.SP.get_rect()
		self.sp_Total = sp_Total
		self.sp_Width = sp_Width
		self.sp_Height = sp_Height

		self.cImage = 0
		self.delay = 0
		self.pauseDelay = 0
		self.cloop = 0

		self.alphaIn = 0
		self.alphaOut = 255

		

	def resetCountAndDelay(self):
		self.cImage = 0
		self.delay = 0
		self.pauseDelay = 0
		self.cloop = 0
		self.alphaIn = 0
		self.alphaOut = 255

	def play(self,x,y,delay):
		self.setRectPos(x, y)
		if self.cImage != self.sp_Total - 1:
			if self.delay > delay:  
					self.cImage += 1
					self.delay = 0
			else:
				self.delay += 1
		else:
			self.cloop += 1
		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def loop(self,x,y,delay):
		self.setRectPos(x, y)
		if self.cImage == self.sp_Total - 1:
			self.cImage = 0
			self.delay = 0
			self.cloop += 1
		elif self.delay > delay:  
				self.cImage += 1
				self.delay = 0
		else:
			self.delay += 1

		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def stopAt(self,x,y,delay,sp_Num):
		self.setRectPos(x, y)
		if self.cImage != sp_Num:
			if self.delay > delay:  
					self.cImage += 1
					self.delay = 0
			else:
				self.delay += 1
		else:
			self.cloop += 1
		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def pausePlay(self,x, y, delay, sp_Num,pauseDelay):
		self.setRectPos(x, y)
		if self.cImage != self.sp_total - 1:
			if self.cImage != sp_Num:
				if self.delay > delay:  
						self.cImage += 1
						self.delay = 0
				else:
					self.delay += 1
			else:
				if self.pauseDelay > pauseDelay:
					if self.delay > delay:  
						self.cImage += 1
						self.delay = 0
					else:
						self.delay += 1
		else:
			self.cloop += 1
		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def isStop(self):
		if self.cloop == 1:
			return True
		else:
			return False

	def renderImg(self,x,y):
		self.setRectPos(x, y)
		self.gameDisplay.blit(self.SP,(x,y))

	def renderImgConvert(self,x,y):
		self.setRectPos(x, y)
		self.gameDisplay.blit(self.SPconvert,(x,y))

	def setFadeInImg(self,fadeSpeed = 1):
		if self.alphaIn < 255:
			self.alphaIn += fadeSpeed
		self.SPconvert.set_alpha(self.alphaIn)
	
	def setFadeOutImg(self,fadeSpeed = 1):
		if self.alphaOut > 0:
			self.alphaOut -= fadeSpeed
		self.SPconvert.set_alpha(self.alphaOut)
	
	def isCollide(self,other):
		xLT1 = self.SPcollider.x
		yLT1 = self.SPcollider.y
		xRB1 = self.SPcollider.x + self.SPcollider.width/self.sp_Total
		yRB1 = self.SPcollider.y + self.SPcollider.height

		xLT2 = other.SPcollider.x
		yLT2 = other.SPcollider.y
		xRB2 = other.SPcollider.x + other.SPcollider.width/other.sp_Total
		yRB2 = other.SPcollider.y + other.SPcollider.height

		if yRB1 < yLT2 :
			return False
		if xRB1 < xLT2 :
			return False
		if yLT1 > yRB2 :
			return False
		if xLT1 > xRB2 :
			return False
		return True

	def setRectPos(self,x,y):
		self.SPcollider.x = x
		self.SPcollider.y = y


