from State_GamePlay import State_GamePlay
from Player_Freedom import  Player_Freedom

class State_GamePlaySingle(State_GamePlay):

	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GamePlay.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.nextStateId = 4
		
	def initPlayer(self,gameDisplay,gameWidth,gameHeight,FPS):
		freedomPlayerRef = Player_Freedom(gameDisplay,gameWidth,gameHeight,FPS)
		self.playerList = [freedomPlayerRef]

	def updateScore(self):
		self.myScoreRef.setScoreFreedom(self.playerList[0].score)



