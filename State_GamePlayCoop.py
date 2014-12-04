from State_GamePlay import State_GamePlay
from Player_Freedom import  Player_Freedom
from Player_Justice import  Player_Justice

class State_GamePlayCoop(State_GamePlay):

	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GamePlay.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)

	def initPlayer(self,gameDisplay,gameWidth,gameHeight,FPS):
		freedomPlayerRef = Player_Freedom(gameDisplay,gameWidth,gameHeight,FPS)
		justicePlayerRef = Player_Justice(gameDisplay,gameWidth,gameHeight,FPS)
		self.playerList = [freedomPlayerRef,justicePlayerRef]


