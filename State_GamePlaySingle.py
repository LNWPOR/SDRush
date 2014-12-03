from State_GamePlay import *
from MySprite import MySprite
from MySound import MySound
from Player_Freedom import  Player_Freedom

class State_GamePlaySingle(State_GamePlay):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GamePlay.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)

		self.freedomPlayer = Player_Freedom(gameDisplay,gameWidth,gameHeight,FPS)

	def renderState(self):
		self.renderMap()
		self.freedomPlayer.render()
		pygame.draw.rect(self.gameDisplay,(0,0,0),[400,300,150,20])

	def updateState(self):
		self.playThemeSound(self.themeSound)
		self.freedomPlayer.update()
