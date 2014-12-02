import pygame
from pygame.locals import *
from MySound import MySound

class StateBase:
	
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		self.FPS = FPS
		self.stateID = stateID
		self.setCurrentStateID(0)

	def setCurrentStateID(self,nextStateID):
		global currentStateID
		currentStateID = nextStateID

	def getCurrentStateID(self):
		return currentStateID

	def resetState(self):
		pass

	def renderState(self):
		pass

	def updateState(self):
		pass

	def playThemeSound(self,themeSound):
		if not self.themeSound.isPlay():
			self.themeSound.loop()

	def getID(self):
		return self.stateID