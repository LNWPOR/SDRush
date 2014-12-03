from State_GamePlay import *
from MySprite import MySprite
from MySound import MySound
from Player_Freedom import  Player_Freedom
from Player_Justice import  Player_Justice

class State_GamePlayCoop(State_GamePlay):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GamePlay.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.setUpState(gameDisplay,gameWidth,gameHeight,FPS)
	
	def renderState(self):
		self.renderMap()
		self.freedomPlayerRef.render()
		self.justicePlayerRef.render()

	def updateState(self):
		self.playThemeSound(self.themeSound)
		self.freedomPlayerRef.update()
		self.justicePlayerRef.update()

	def setUpState(self,gameDisplay,gameWidth,gameHeight,FPS):
		self.freedomPlayerRef = Player_Freedom(gameDisplay,gameWidth,gameHeight,FPS)
		self.justicePlayerRef = Player_Justice(gameDisplay,gameWidth,gameHeight,FPS)
	



