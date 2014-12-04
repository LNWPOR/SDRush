from State_GameOver import State_GameOver
from MyTextWriter import MyTextWriter
RED_COLOR = (240,0,0)
BLUE_COLOR = (0,0,255)


class State_GameOverCoop(State_GameOver):

	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GameOver.__init__(self,gameDisplay, gameWidth, gameHeight, FPS, stateID)
		self.initSP("res/images/gameOverCoop.png")
		self.myTextWriterRef = MyTextWriter(gameDisplay,gameWidth,gameHeight)

	def renderScore(self):
		self.myTextWriterRef.draw("FreedomScore: %d"%self.myScoreRef.getScoreFreedom(),50,150,BLUE_COLOR)
		self.myTextWriterRef.draw("JusticeScore: %d"%self.myScoreRef.getScoreJustice(),50,250,RED_COLOR)

