from State_GamePlay import *
from MySprite import MySprite
from MySound import MySound

class State_GamePlayCoop(State_GamePlay):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GamePlay.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)

	def renderState(self):
		self.renderMap()


	def updateState(self):
		self.playThemeSound(self.themeSound)
