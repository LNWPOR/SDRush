from State_GameOver import State_GameOver
from MyTextWriter import MyTextWriter
BLUE_COLOR = (0,0,255)

class State_GameOverSingle(State_GameOver):

	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GameOver.__init__(self,gameDisplay, gameWidth, gameHeight, FPS, stateID)
		self.initSP("res/images/gameOverSingle.png")
		self.myTextWriterRef = MyTextWriter(gameDisplay,gameWidth,gameHeight)

	def renderScore(self):
		self.myTextWriterRef.draw("FreedomScore: %d"%self.myScoreRef.getScoreFreedom(),50,150,BLUE_COLOR)








